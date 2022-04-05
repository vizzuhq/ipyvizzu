import unittest
import unittest.mock
import pathlib
import json
import pandas as pd


from normalizer import Normalizer
from ipyvizzu import (
    PlainAnimation,
    Data,
    Config,
    Style,
    Animate,
    Feature,
    AnimationMerger,
    Chart,
    Snapshot,
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

    def test_style_can_be_none(self):
        animation = Style(None)
        self.assertEqual({"style": None}, animation.build())


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

    def test_only_different_type_of_animation_can_be_merged(self):
        self.merger.merge(Config({"channels": {"label": {"attach": ["Popularity"]}}}))
        self.assertRaises(
            ValueError, self.merger.merge, Config({"color": {"set": ["Genres"]}})
        )

    def test_snapshot_can_not_be_merged(self):
        snapshot = Snapshot("snapshot_a")
        self.merger.merge(Config({"channels": {"label": {"attach": ["Popularity"]}}}))
        self.assertRaises(NotImplementedError, self.merger.merge, snapshot)

    def test_merge_none(self):
        self.merger.merge(Config({"channels": {"label": {"attach": ["Popularity"]}}}))
        self.merger.merge(Style(None))
        self.assertEqual(
            """{"config": {"channels": {"label": {"attach": ["Popularity"]}}}, "style": null}""",
            self.merger.dump(),
        )


class TestChart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.asset_dir = pathlib.Path(__file__).parent / "assets"
        cls.normalizer = Normalizer()

    def setUp(self):
        self.patch = unittest.mock.patch("ipyvizzu.display_html")
        self.display_html = self.patch.start()

        self.data = Data()
        self.data.add_series("Foo", ["Alice", "Bob", "Ted"])
        self.data.add_series("Bar", [15, 32, 12])

        self.chart = Chart()

    def tearDown(self):
        self.patch.stop()

    def test_init_div(self):
        chart = Chart(
            vizzu="https://cdn.jsdelivr.net/npm/vizzu@~0.4.0/dist/vizzu.min.js",
            width="400px",
            height="240px",
        )
        chart.animate(self.data)
        chart.animate(Config({"x": "Foo", "y": "Bar", "color": "Foo"}))
        self._assert_display("init.html")

    def test_init_display_begin(self):
        chart = Chart(display="begin")
        chart.animate(self.data)
        chart.animate(Config({"x": "Foo", "y": "Bar", "color": "Foo"}))
        self._assert_display("init_begin.html")

    def test_init_display_end(self):
        chart = Chart(display="end")
        chart.animate(self.data)
        chart.animate(Config({"x": "Foo", "y": "Bar", "color": "Foo"}))
        self._assert_display("init_end.html")

    def test_init_display_actual(self):
        chart = Chart(display="actual")
        chart.animate(self.data)
        chart.animate(Config({"x": "Foo", "y": "Bar", "color": "Foo"}))
        self._assert_display("init_actual.html")

    def test_init_display_invalid_enum(self):
        with self.assertRaises(ValueError):
            Chart(display="invalid_enum")

    def test_animate(self):
        self.chart.animate(self.data)
        self.chart.animate(Config({"x": "Foo", "y": "Bar", "color": "Foo"}))
        self._assert_display("animate.html")

    def test_animate_without_scroll(self):
        self.chart.scroll_into_view = False
        self.chart.animate(self.data)
        self.chart.animate(Config({"x": "Foo", "y": "Bar", "color": "Foo"}))
        self._assert_display("animate_without_scroll.html")

    def test_animate_options(self):
        data = Data()
        data.add_series("Foo", ["Alice", "Bob", "Ted"])
        data.add_series("Bar", [15, 32, 12])
        self.chart.animate(data)
        self.chart.animate(
            Config({"x": "Foo", "y": "Bar", "color": "Foo"}), duration="4s"
        )
        self._assert_display("animate_options.html")

    def test_feature(self):
        self.chart.animate(self.data)
        self.chart.animate(Config({"x": "Foo", "y": "Bar", "color": "Foo"}))
        self.chart.feature("tooltip", True)
        self._assert_display("feature.html")

    def test_style(self):
        self.chart.animate(self.data)
        self.chart.animate(Config({"x": "Foo", "y": "Bar", "color": "Foo"}))
        self.chart.animate(Style({"legend": {"width": 50}}))
        self._assert_display("style.html")

    def test_animation_merge(self):
        self.chart.animate(self.data)
        self.chart.animate(
            Config({"color": {"set": ["Genres"]}}), Style({"legend": {"width": 50}})
        )
        self._assert_display("merge.html")

    def test_args_has_to_be_passed_to_animate(self):
        with self.assertRaises(ValueError):
            self.chart.animate()

    def test_animate_does_not_accept_kwargs_without_args(self):
        with self.assertRaises(ValueError):
            self.chart.animate(duration="500ms")

    def test_ony_different_type_of_animation_can_be_merged(self):
        with self.assertRaises(ValueError):
            self.chart.animate(
                Config({"channels": {"label": {"attach": ["Popularity"]}}}),
                Config({"color": {"set": ["Genres"]}}),
            )

    def test_store(self):
        self.chart.animate(self.data)
        snapshot_a = self.chart.store()
        self.chart.animate(
            Config({"color": {"set": ["Genres"]}}), Style({"legend": {"width": 50}})
        )
        snapshot_b = self.chart.store()
        self.chart.animate(snapshot_a, duration="4s")
        self.chart.animate(snapshot_b)
        self._assert_display("store.html")

    def _assert_display(self, asset_name):
        asset_path = self.asset_dir / asset_name
        display_out = []
        for block in self.display_html.call_args_list:
            display_out.append(block.args[0])
        self.assertEqual(
            self.normalizer.normalize_id("\n".join(display_out)).strip(),
            asset_path.read_text().strip(),
        )
