import unittest.mock

from tests.chart import TestChartInit, TestChartMethods, TestChartShow
from ipyvizzu import Chart, Data, Config, Snapshot, Style


class TestChartInitIpyvizzu(TestChartInit):
    def setUp(self):
        self.patch = unittest.mock.patch("ipyvizzu.chart.display_javascript")
        self.trash = self.patch.start()
        super().setUp()

    def tearDown(self):
        super().tearDown()
        self.patch.stop()

    def get_mock(self):
        return "ipyvizzu.chart.display_javascript"

    def get_chart(self, *args, **kwargs):
        return Chart(*args, **kwargs)

    def get_snapshot(self, snapshot_id):
        return Snapshot(snapshot_id)

    def test_init(self, ref=None):
        ref = (
            "window.ipyvizzu = "
            + "new window.PyVizzu("
            + "element, "
            + "id, "
            + "'https://cdn.jsdelivr.net/npm/vizzu@~0.4.0/dist/vizzu.min.js', "
            + "'800px', '480px');"
        )
        super().test_init(ref)

    def test_init_vizzu(self, ref=None):
        ref = (
            "window.ipyvizzu = "
            + "new window.PyVizzu("
            + "element, "
            + "id, "
            + "'https://cdn.jsdelivr.net/npm/vizzu@0.4.1/dist/vizzu.min.js', "
            + "'800px', '480px');"
        )
        super().test_init_vizzu(ref)

    def test_init_div(self, ref=None):
        ref = (
            "window.ipyvizzu = "
            + "new window.PyVizzu("
            + "element, "
            + "id, "
            + "'https://cdn.jsdelivr.net/npm/vizzu@~0.4.0/dist/vizzu.min.js', "
            + "'400px', '240px');"
        )
        super().test_init_div(ref)

    def test_init_display_not_valid(self):
        with self.assertRaises(ValueError):
            self.get_chart(display="invalid")

    def test_init_display_begin(self):
        chart = self.get_chart(display="begin")
        with unittest.mock.patch(self.get_mock()) as output:
            chart.animate(self.get_snapshot("abc1234"))
            self.assertEqual(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.animate(element, id, 'begin', false, "
                + "window.ipyvizzu.stored(element, id), "
                + "undefined);",
            )

    def test_init_display_actual(self):
        chart = self.get_chart(display="actual")
        with unittest.mock.patch(self.get_mock()) as output:
            chart.animate(self.get_snapshot("abc1234"))
            self.assertEqual(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.animate(element, id, 'actual', false, "
                + "window.ipyvizzu.stored(element, id), "
                + "undefined);",
            )

    def test_init_display_end(self):
        chart = self.get_chart(display="end")
        with unittest.mock.patch(self.get_mock()) as output:
            chart.animate(self.get_snapshot("abc1234"))
            self.assertEqual(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.animate(element, id, 'end', false, "
                + "window.ipyvizzu.stored(element, id), "
                + "undefined);",
            )


class TestChartMethodsIpyvizzu(TestChartMethods):
    def setUp(self):
        self.patch = unittest.mock.patch("ipyvizzu.chart.display_javascript")
        self.trash = self.patch.start()
        super().setUp()

    def tearDown(self):
        super().tearDown()
        self.patch.stop()

    def get_mock(self):
        return "ipyvizzu.chart.display_javascript"

    def get_chart(self, *args, **kwargs):
        return Chart(*args, **kwargs)

    def get_data(self):
        return Data()

    def get_config(self, config):
        return Config(config)

    def get_style(self, style):
        return Style(style)

    def get_snapshot(self, snapshot_id):
        return Snapshot(snapshot_id)

    def test_animate_one_chart_target(self, ref=None):
        ref = (
            "window.ipyvizzu.animate(element, id, 'actual', false, "
            + '{"data": {"records": [["Rock", "Hard", 96]]}}, '
            + "undefined);"
        )
        super().test_animate_one_chart_target(ref)

    def test_animate_one_chart_target_with_chart_anim_opts(self, ref=None):
        ref = (
            "window.ipyvizzu.animate(element, id, 'actual', false, "
            + '{"data": {"records": [["Rock", "Hard", 96]]}}, '
            + '{"duration": "500ms"});'
        )
        super().test_animate_one_chart_target_with_chart_anim_opts(ref)

    def test_animate_snapshot_chart_target(self, ref=None):
        ref = (
            "window.ipyvizzu.animate(element, id, 'actual', false, "
            + "window.ipyvizzu.stored(element, id), "
            + "undefined);"
        )
        super().test_animate_snapshot_chart_target(ref)

    def test_animate_snapshot_chart_target_with_chart_anim_opts(self, ref=None):
        ref = (
            "window.ipyvizzu.animate(element, id, 'actual', false, "
            + "window.ipyvizzu.stored(element, id), "
            + '{"duration": "500ms"});'
        )
        super().test_animate_snapshot_chart_target_with_chart_anim_opts(ref)

    def test_animate_more_chart_target(self, ref=None):
        ref = (
            "window.ipyvizzu.animate(element, id, 'actual', false, "
            + '{"data": {"records": [["Rock", "Hard", 96]]}, '
            + '"config": {"channels": {"label": {"attach": ["Popularity"]}}}, '
            + '"style": {"title": {"backgroundColor": "#A0A0A0"}}}, '
            + "undefined);"
        )
        super().test_animate_more_chart_target(ref)

    def test_animate_more_chart_target_with_chart_anim_opts(self, ref=None):
        ref = (
            "window.ipyvizzu.animate(element, id, 'actual', false, "
            + '{"data": {"records": [["Rock", "Hard", 96]]}, '
            + '"config": {"channels": {"label": {"attach": ["Popularity"]}}}, '
            + '"style": {"title": {"backgroundColor": "#A0A0A0"}}}, '
            + '{"duration": "500ms"});'
        )
        super().test_animate_more_chart_target_with_chart_anim_opts(ref)

    def test_animate_more_calls(self, ref=None):
        ref = (
            "window.ipyvizzu.animate(element, id, 'actual', false, "
            + '{"data": {"records": [["Rock", "Hard", 96]]}, '
            + '"config": {"channels": {"label": {"attach": ["Popularity"]}}}, '
            + '"style": {"title": {"backgroundColor": "#A0A0A0"}}}, '
            + "undefined);\n"
            + "window.ipyvizzu.animate(element, id, 'actual', false, "
            + '{"config": {"title": "Test"}}, '
            + "undefined);"
        )
        super().test_animate_more_calls(ref)

    def test_animate_with_not_default_scroll_into_view(self, ref=None):
        ref = (
            "window.ipyvizzu.animate(element, id, 'actual', true, "
            + '{"data": {"records": [["Rock", "Hard", 96]]}}, '
            + "undefined);"
        )
        super().test_animate_with_not_default_scroll_into_view(ref)

    def test_feature(self, ref=None):
        ref = 'window.ipyvizzu.feature(element, id, "tooltip", true);'
        super().test_feature(ref)

    def test_store(self, ref=None):
        ref = "window.ipyvizzu.store(element, id, id);"
        super().test_store(ref)


class TestChartShowIpyvizzu(TestChartShow):
    def setUp(self):
        self.patch = unittest.mock.patch("ipyvizzu.chart.display_javascript")
        self.trash = self.patch.start()
        super().setUp()

    def tearDown(self):
        super().tearDown()
        self.patch.stop()

    def get_mock(self):
        return "ipyvizzu.Chart._display"

    def get_chart(self):
        return Chart(display="manual")

    def get_snapshot(self, snapshot_id):
        return Snapshot(snapshot_id)

    def test_show_if_display_is_not_manual(self):
        chart = Chart()
        chart.animate(self.get_snapshot("abc1234"))
        with self.assertRaises(AssertionError):
            chart.show()

    def test_show(self, ref=None):
        ref = (
            "window.ipyvizzu.animate(element, id, 'manual', false, "
            + "window.ipyvizzu.stored(element, id), "
            + "undefined);"
        )
        super().test_show(ref)
