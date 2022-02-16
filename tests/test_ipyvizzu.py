import unittest
import pathlib
import re

from ipyvizzu import (
    PlainAnimation,
    Data,
    Config,
    Style,
    Animate,
    Feature,
    AnimationMerger,
    Chart,
)


class TestAnimation(unittest.TestCase):
    def test_plainanimation(self):
        animation = PlainAnimation(geometry="circle")
        self.assertEqual({"geometry": "circle"}, animation.build())

    def test_config(self):
        animation = Config({"color": {"set": ["Genres"]}})
        self.assertEqual({"config": {"color": {"set": ["Genres"]}}}, animation.build())

    def test_style(self):
        animation = Style({"title": {"backgroundColor": "#A0A0A0"}})
        self.assertEqual(
            {"style": {"title": {"backgroundColor": "#A0A0A0"}}}, animation.build()
        )


class TestMethod(unittest.TestCase):
    def test_animate(self):
        animation = Config({"color": {"set": ["Genres"]}})
        method = Animate(animation)
        self.assertEqual(f"chart.animate({animation.dump()});", method.dump())

    def test_feature(self):
        method = Feature("tooltip", True)
        self.assertEqual('chart.feature("tooltip", true);', method.dump())


class TestMerger(unittest.TestCase):
    def setUp(self):
        self.merger = AnimationMerger()

    def test_merge(self):
        self.merger.merge(Style({"title": {"backgroundColor": "#A0A0A0"}}))
        self.merger.merge(Config({"channels": {"label": {"attach": ["Popularity"]}}}))
        self.assertEqual(
            {
                "style": {"title": {"backgroundColor": "#A0A0A0"}},
                "config": {"channels": {"label": {"attach": ["Popularity"]}}},
            },
            self.merger.build(),
        )

    def test_ony_different_type_of_animation_can_be_merged(self):
        self.merger.merge(Config({"channels": {"label": {"attach": ["Popularity"]}}}))
        self.assertRaises(
            ValueError, self.merger.merge, Config({"color": {"set": ["Genres"]}})
        )


class TestData(unittest.TestCase):
    def setUp(self):
        self.data = Data()

    def test_record(self):
        self.data.add_record(["Pop", "Hard", 114])
        self.assertEqual(
            {"data": {"records": [["Pop", "Hard", 114]]}}, self.data.build()
        )

    def test_serie(self):
        self.data.add_serie("Genres", ["Pop", "Rock", "Metal"])
        self.assertEqual(
            {
                "data": {
                    "series": [{"name": "Genres", "values": ["Pop", "Rock", "Metal"]}]
                }
            },
            self.data.build(),
        )

    def test_dimension(self):
        self.data.add_dimension("Genres", ["Pop", "Rock", "Metal"])
        self.assertEqual(
            {
                "data": {
                    "dimensions": [
                        {"name": "Genres", "values": ["Pop", "Rock", "Metal"]}
                    ]
                }
            },
            self.data.build(),
        )

    def test_mesure(self):
        self.data.add_measure("Popularity", [[114, 96, 78, 52], [56, 36, 174, 121]])
        self.assertEqual(
            {
                "data": {
                    "measures": [
                        {
                            "name": "Popularity",
                            "values": [[114, 96, 78, 52], [56, 36, 174, 121]],
                        }
                    ]
                }
            },
            self.data.build(),
        )


class TestChart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.asset_dir = pathlib.Path(__file__).parent / "assets"
        cls.div_pattern = re.compile(r"myVizzu_\d+", flags=re.MULTILINE)

    @classmethod
    def normalize_div_id(cls, output):
        normalized_output = cls.div_pattern.sub("myVizzu", output, count=2)
        return normalized_output

    def setUp(self):
        self.patch = unittest.mock.patch("ipyvizzu.display_html")
        self.display_html = self.patch.start()
        self.chart = Chart()

    def tearDown(self):
        self.patch.stop()

    def test_animate(self):
        data = Data()
        data.add_serie("Foo", ["Alice", "Bob", "Ted"])
        data.add_serie("Bar", [15, 32, 12])

        self.chart.animate(data)
        self.chart.animate(x="Foo", y="Bar", color="Foo")

        self.chart.show()
        self._assert_display("animate.html")

    def test_feature(self):
        data = Data()
        data.add_serie("Foo", ["Alice", "Bob", "Ted"])
        data.add_serie("Bar", [15, 32, 12])

        self.chart.animate(data)
        self.chart.animate(x="Foo", y="Bar", color="Foo")
        self.chart.feature("tooltip", True)

        self.chart.show()
        self._assert_display("feature.html")

    def test_style(self):
        data = Data()
        data.add_serie("Foo", ["Alice", "Bob", "Ted"])
        data.add_serie("Bar", [15, 32, 12])

        self.chart.animate(data)
        self.chart.animate(x="Foo", y="Bar", color="Foo")
        self.chart.animate(Style({"legend": {"width": 50}}))

        self.chart.show()
        self._assert_display("style.html")

    def test_animation_merge(self):
        data = Data()
        data.add_serie("Foo", ["Alice", "Bob", "Ted"])
        data.add_serie("Bar", [15, 32, 12])

        self.chart.animate(data)
        self.chart.animate(
            Config({"color": {"set": ["Genres"]}}), Style({"legend": {"width": 50}})
        )

        self.chart.show()
        self._assert_display("merge.html")

    def test_animate_does_not_accept_args_and_kwargs_together(self):
        with self.assertRaises(ValueError):
            self.chart.animate(Config({"color": {"set": ["Genres"]}}), x="Foo")

    def test_args_or_kwargs_has_to_be_passed_to_animate(self):
        with self.assertRaises(ValueError):
            self.chart.animate()

    def test_ony_different_type_of_animation_can_be_merged(self):
        with self.assertRaises(ValueError):
            self.chart.animate(
                Config({"channels": {"label": {"attach": ["Popularity"]}}}),
                Config({"color": {"set": ["Genres"]}}),
            )

    def _assert_display(self, asset_name):
        asset_path = self.asset_dir / asset_name
        self.assertEqual(
            self.normalize_div_id(self.display_html.call_args.args[0]).strip(),
            asset_path.read_text().strip(),
        )
