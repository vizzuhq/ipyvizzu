import unittest

from ipyvizzu import (
    PlainAnimation,
    Data,
    Config,
    Style,
    Animate,
    Feature,
    AnimationMerger,
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
