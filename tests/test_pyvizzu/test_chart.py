from tests.chart import (
    TestChartInit,
    TestChartMethods,
    TestChartShow,
    TestChartReprHtml,
)
from pyvizzu import Chart, Data, Config, Snapshot, Style


class TestChartInitPyvizzu(TestChartInit):
    def get_mock(self):
        return "pyvizzu.Chart._display"

    def get_chart(self, *args, **kwargs):
        return Chart(*args, **kwargs)

    def test_init(self, ref=None):
        ref = (
            "window.pyvizzu = "
            + "new window.PyVizzu("
            + "document.getElementById(id), "
            + "id, "
            + "'https://cdn.jsdelivr.net/npm/vizzu@~0.4.0/dist/vizzu.min.js', "
            + "'800px', '480px');"
        )
        super().test_init(ref)

    def test_init_vizzu(self, ref=None):
        ref = (
            "window.pyvizzu = "
            + "new window.PyVizzu("
            + "document.getElementById(id), "
            + "id, "
            + "'https://cdn.jsdelivr.net/npm/vizzu@0.4.1/dist/vizzu.min.js', "
            + "'800px', '480px');"
        )
        super().test_init_vizzu(ref)

    def test_init_div(self, ref=None):
        ref = (
            "window.pyvizzu = "
            + "new window.PyVizzu("
            + "document.getElementById(id), "
            + "id, "
            + "'https://cdn.jsdelivr.net/npm/vizzu@~0.4.0/dist/vizzu.min.js', "
            + "'400px', '240px');"
        )
        super().test_init_div(ref)


class TestChartMethodsPyvizzu(TestChartMethods):
    def get_mock(self):
        return "pyvizzu.Chart._display"

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
            "window.pyvizzu.animate(null, id, 'manual', false, "
            + '{"data": {"records": [["Rock", "Hard", 96]]}}, '
            + "undefined);"
        )
        super().test_animate_one_chart_target(ref)

    def test_animate_one_chart_target_with_chart_anim_opts(self, ref=None):
        ref = (
            "window.pyvizzu.animate(null, id, 'manual', false, "
            + '{"data": {"records": [["Rock", "Hard", 96]]}}, '
            + '{"duration": "500ms"});'
        )
        super().test_animate_one_chart_target_with_chart_anim_opts(ref)

    def test_animate_snapshot_chart_target(self, ref=None):
        ref = (
            "window.pyvizzu.animate(null, id, 'manual', false, "
            + "window.pyvizzu.stored(null, id), "
            + "undefined);"
        )
        super().test_animate_snapshot_chart_target(ref)

    def test_animate_snapshot_chart_target_with_chart_anim_opts(self, ref=None):
        ref = (
            "window.pyvizzu.animate(null, id, 'manual', false, "
            + "window.pyvizzu.stored(null, id), "
            + '{"duration": "500ms"});'
        )
        super().test_animate_snapshot_chart_target_with_chart_anim_opts(ref)

    def test_animate_more_chart_target(self, ref=None):
        ref = (
            "window.pyvizzu.animate(null, id, 'manual', false, "
            + '{"data": {"records": [["Rock", "Hard", 96]]}, '
            + '"config": {"channels": {"label": {"attach": ["Popularity"]}}}, '
            + '"style": {"title": {"backgroundColor": "#A0A0A0"}}}, '
            + "undefined);"
        )
        super().test_animate_more_chart_target(ref)

    def test_animate_more_chart_target_with_chart_anim_opts(self, ref=None):
        ref = (
            "window.pyvizzu.animate(null, id, 'manual', false, "
            + '{"data": {"records": [["Rock", "Hard", 96]]}, '
            + '"config": {"channels": {"label": {"attach": ["Popularity"]}}}, '
            + '"style": {"title": {"backgroundColor": "#A0A0A0"}}}, '
            + '{"duration": "500ms"});'
        )
        super().test_animate_more_chart_target_with_chart_anim_opts(ref)

    def test_animate_more_calls(self, ref=None):
        ref = (
            "window.pyvizzu.animate(null, id, 'manual', false, "
            + '{"data": {"records": [["Rock", "Hard", 96]]}, '
            + '"config": {"channels": {"label": {"attach": ["Popularity"]}}}, '
            + '"style": {"title": {"backgroundColor": "#A0A0A0"}}}, '
            + "undefined);\n"
            + "window.pyvizzu.animate(null, id, 'manual', false, "
            + '{"config": {"title": "Test"}}, '
            + "undefined);"
        )
        super().test_animate_more_calls(ref)

    def test_animate_with_not_default_scroll_into_view(self, ref=None):
        ref = (
            "window.pyvizzu.animate(null, id, 'manual', true, "
            + '{"data": {"records": [["Rock", "Hard", 96]]}}, '
            + "undefined);"
        )
        super().test_animate_with_not_default_scroll_into_view(ref)

    def test_feature(self, ref=None):
        ref = 'window.pyvizzu.feature(null, id, "tooltip", true);'
        super().test_feature(ref)

    def test_store(self, ref=None):
        ref = "window.pyvizzu.store(null, id, id);"
        super().test_store(ref)


class TestChartShowPyvizzu(TestChartShow):
    def get_mock(self):
        return "pyvizzu.Chart._display"

    def get_chart(self):
        return Chart()

    def get_snapshot(self, snapshot_id):
        return Snapshot(snapshot_id)

    def test_show(self, ref=None):
        ref = (
            "window.pyvizzu.animate(null, id, 'manual', false, "
            + "window.pyvizzu.stored(null, id), "
            + "undefined);"
        )
        super().test_show(ref)


class TestChartReprHtmlPyvizzu(TestChartReprHtml):
    def get_mock(self):
        return "pyvizzu.Chart._display"

    def get_chart(self):
        return Chart()

    def get_snapshot(self, snapshot_id):
        return Snapshot(snapshot_id)

    def test_repr_html(self, ref=None):
        ref = (
            "window.pyvizzu.animate(null, id, 'manual', false, "
            + "window.pyvizzu.stored(null, id), "
            + "undefined);"
        )
        super().test_repr_html(ref)
