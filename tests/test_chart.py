# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import abc
from typing import Callable
import unittest
import unittest.mock

from ipyvizzu import (
    Animation,
    Chart,
    ChartProperty,
    Config,
    Data,
    EventHandler,
    Snapshot,
    Style,
)

from tests.utils.normalizer import Normalizer


class TestChart(unittest.TestCase, abc.ABC):
    normalizer: Normalizer

    @classmethod
    def setUpClass(cls) -> None:
        cls.normalizer = Normalizer()

    def setUp(self) -> None:
        self.patch = unittest.mock.patch(self.mock)
        self.trash = self.patch.start()
        self.chart = Chart()
        self.chart.initializing()

    def tearDown(self) -> None:
        self.patch.stop()

    @property
    def mock(self) -> str:
        return "ipyvizzu.chart.display_javascript"


class TestChartInit(TestChart):
    def test_init(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            chart = Chart()
            chart.initializing()
            self.assertEqual(
                self.normalizer.normalize_output(output, 2),
                "window.ipyvizzu.createChart("
                + "element, "
                + "id, "
                + "'https://cdn.jsdelivr.net/npm/vizzu@0.8/dist/vizzu.min.js', "
                + "'800px', '480px');",
            )

    def test_init_vizzu(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            chart = Chart(
                vizzu="https://cdn.jsdelivr.net/npm/vizzu@0.4.1/dist/vizzu.min.js"
            )
            chart.initializing()
            self.assertEqual(
                self.normalizer.normalize_output(output, 2),
                "window.ipyvizzu.createChart("
                + "element, "
                + "id, "
                + "'https://cdn.jsdelivr.net/npm/vizzu@0.4.1/dist/vizzu.min.js', "
                + "'800px', '480px');",
            )

    def test_init_div(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            chart = Chart(width="400px", height="240px")
            chart.initializing()
            self.assertEqual(
                self.normalizer.normalize_output(output, 2),
                "window.ipyvizzu.createChart("
                + "element, "
                + "id, "
                + "'https://cdn.jsdelivr.net/npm/vizzu@0.8/dist/vizzu.min.js', "
                + "'400px', '240px');",
            )

    def test_init_display_invalid(self) -> None:
        with self.assertRaises(ValueError):
            Chart(display="invalid")

    def test_init_display_begin(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            chart = Chart(display="begin")
            chart.animate(Snapshot("abc1234"))
            self.assertEqual(
                self.normalizer.normalize_output(output, 3),
                "window.ipyvizzu.animate(element, id, id, 'begin', false, "
                + "lib => { return id }, "
                + "undefined);",
            )

    def test_init_display_actual(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            chart = Chart(display="actual")
            chart.animate(Snapshot("abc1234"))
            self.assertEqual(
                self.normalizer.normalize_output(output, 3),
                "window.ipyvizzu.animate(element, id, id, 'actual', false, "
                + "lib => { return id }, "
                + "undefined);",
            )

    def test_init_display_end(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            chart = Chart(display="end")
            chart.animate(Snapshot("abc1234"))
            self.assertEqual(
                self.normalizer.normalize_output(output, 3),
                "window.ipyvizzu.animate(element, id, id, 'end', false, "
                + "lib => { return id }, "
                + "undefined);",
            )

    def test_manual_init(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            self.chart.initializing()
            self.chart.initializing()
            self.chart.initializing()
            self.chart.animate(Snapshot("abc1234"))
            self.assertEqual(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.animate(element, id, id, 'actual', false, "
                + "lib => { return id }, "
                + "undefined);",
            )

    def test_init_register_events(self) -> None:
        class IPyEvents:
            # pylint: disable=too-few-public-methods

            @staticmethod
            def register(event: str, function: Callable[[], None]) -> None:
                # pylint: disable=unused-argument

                function()

        class IPy:
            # pylint: disable=too-few-public-methods

            events = IPyEvents

        get_ipython_mock = "ipyvizzu.chart.get_ipython"
        with unittest.mock.patch(get_ipython_mock, return_value=IPy()):
            with unittest.mock.patch(self.mock) as output:
                chart = Chart()
                chart.initializing()
                self.assertEqual(
                    self.normalizer.normalize_output(output, 2, 3),
                    "if (window.IpyVizzu) { window.IpyVizzu.clearInhibitScroll(element); }",
                )


class TestChartMethods(TestChart):
    def test_animate_chart_target_has_to_be_passed(self) -> None:
        with self.assertRaises(ValueError):
            self.chart.animate()

    def test_animate_chart_target_has_to_be_passed_even_if_chart_anim_opts_passed(
        self,
    ) -> None:
        with self.assertRaises(ValueError):
            self.chart.animate(duration="500ms")

    def test_animate_one_chart_target(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            data = Data()
            data.add_record(["Rock", "Hard", 96])
            self.chart.animate(data)
            self.assertEqual(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.animate(element, id, id, 'actual', false, "
                + 'lib => { return {"data": {"records": [["Rock", "Hard", 96]]}} }, '
                + "undefined);",
            )

    def test_animate_one_chart_target_with_chart_anim_opts(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            data = Data()
            data.add_record(["Rock", "Hard", 96])
            self.chart.animate(data, duration="500ms")
            self.assertEqual(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.animate(element, id, id, 'actual', false, "
                + 'lib => { return {"data": {"records": [["Rock", "Hard", 96]]}} }, '
                + '{"duration": "500ms"});',
            )

    def test_animate_snapshot_chart_target(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            snapshot = Snapshot("abc1234")
            self.chart.animate(snapshot)
            self.assertEqual(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.animate(element, id, id, 'actual', false, "
                + "lib => { return id }, "
                + "undefined);",
            )

    def test_animate_snapshot_chart_target_with_chart_anim_opts(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            snapshot = Snapshot("abc1234")
            self.chart.animate(snapshot, duration="500ms")
            self.assertEqual(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.animate(element, id, id, 'actual', false, "
                + "lib => { return id }, "
                + '{"duration": "500ms"});',
            )

    def test_animate_stored_animation_chart_target(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            animation = Animation("abc1234")
            self.chart.animate(animation, duration="500ms")
            self.assertEqual(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.animate(element, id, id, 'actual', false, "
                + "lib => { return id }, "
                + '{"duration": "500ms"});',
            )

    def test_animate_more_chart_target(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            data = Data()
            data.add_record(["Rock", "Hard", 96])
            config = Config({"channels": {"label": {"attach": ["Popularity"]}}})
            style = Style({"title": {"backgroundColor": "#A0A0A0"}})
            self.chart.animate(data, config, style)
            self.assertEqual(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.animate(element, id, id, 'actual', false, "
                + 'lib => { return {"data": {"records": [["Rock", "Hard", 96]]}, '
                + '"config": {"channels": {"label": {"attach": ["Popularity"]}}}, '
                + '"style": {"title": {"backgroundColor": "#A0A0A0"}}} }, '
                + "undefined);",
            )

    def test_animate_more_chart_target_with_chart_anim_opts(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            data = Data()
            data.add_record(["Rock", "Hard", 96])
            config = Config({"channels": {"label": {"attach": ["Popularity"]}}})
            style = Style({"title": {"backgroundColor": "#A0A0A0"}})
            self.chart.animate(data, config, style, duration="500ms")
            self.assertEqual(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.animate(element, id, id, 'actual', false, "
                + 'lib => { return {"data": {"records": [["Rock", "Hard", 96]]}, '
                + '"config": {"channels": {"label": {"attach": ["Popularity"]}}}, '
                + '"style": {"title": {"backgroundColor": "#A0A0A0"}}} }, '
                + '{"duration": "500ms"});',
            )

    def test_animate_more_chart_target_with_conflict(self) -> None:
        data = Data()
        data.add_record(["Rock", "Hard", 96])
        config1 = Config({"channels": {"label": {"attach": ["Popularity"]}}})
        config2 = Config({"title": "Test"})
        style = Style({"title": {"backgroundColor": "#A0A0A0"}})
        with self.assertRaises(ValueError):
            self.chart.animate(data, config1, style, config2)

    def test_animate_more_chart_target_with_snapshot(self) -> None:
        data = Data()
        data.add_record(["Rock", "Hard", 96])
        config = Config({"channels": {"label": {"attach": ["Popularity"]}}})
        style = Style({"title": {"backgroundColor": "#A0A0A0"}})
        snapshot = Snapshot("abc1234")
        with self.assertRaises(ValueError):
            self.chart.animate(data, config, style, snapshot)

    def test_animate_more_calls(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            data = Data()
            data.add_record(["Rock", "Hard", 96])
            config1 = Config({"channels": {"label": {"attach": ["Popularity"]}}})
            config2 = Config({"title": "Test"})
            style = Style({"title": {"backgroundColor": "#A0A0A0"}})
            self.chart.animate(data, config1, style)
            self.chart.animate(config2)
            self.assertEqual(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.animate(element, id, id, 'actual', false, "
                + 'lib => { return {"data": {"records": [["Rock", "Hard", 96]]}, '
                + '"config": {"channels": {"label": {"attach": ["Popularity"]}}}, '
                + '"style": {"title": {"backgroundColor": "#A0A0A0"}}} }, '
                + "undefined);\n"
                + "window.ipyvizzu.animate(element, id, id, 'actual', false, "
                + 'lib => { return {"config": {"title": "Test"}} }, '
                + "undefined);",
            )

    def test_animate_with_not_default_scroll_into_view(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            data = Data()
            data.add_record(["Rock", "Hard", 96])
            scroll_into_view = not self.chart.scroll_into_view
            self.chart.scroll_into_view = scroll_into_view
            self.chart.animate(data)
            self.assertEqual(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.animate("
                + f"element, id, id, 'actual', {str(scroll_into_view).lower()}, "
                + 'lib => { return {"data": {"records": [["Rock", "Hard", 96]]}} }, '
                + "undefined);",
            )

    def test_feature(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            self.chart.feature("tooltip", True)
            self.assertEqual(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.feature(element, id, 'tooltip', true);",
            )

    def test_store(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            self.chart.store()
            self.assertEqual(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.store(element, id, id);",
            )


class TestChartEvents(TestChart):
    def test_on(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            handler_method = """event.renderingContext.fillStyle =
                (event.data.text === 'Jazz') ? 'red' : 'gray';"""
            self.chart.on("plot-axis-label-draw", handler_method)
            self.assertEqual(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.setEvent("
                + "element, id, id, 'plot-axis-label-draw', "
                + "event => "
                + "{ event.renderingContext.fillStyle = "
                + "(event.data.text === 'Jazz') ? 'red' : 'gray'; });",
            )

    def test_off(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            handler_method = "alert(JSON.stringify(event.data));"
            handler = EventHandler("click", handler_method)
            self.chart.off(handler)
            self.assertEqual(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.clearEvent(element, id, id, 'click');",
            )


class TestChartLogs(TestChart):
    def test_log_config(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            self.chart.log(ChartProperty.CONFIG)
            self.assertEqual(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.log(element, id, 'config');",
            )

    def test_log_style(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            self.chart.log(ChartProperty.STYLE)
            self.assertEqual(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.log(element, id, 'style');",
            )

    def test_log_invalid(self) -> None:
        with self.assertRaises(AttributeError):
            self.chart.log(ChartProperty.INVALID)  # type: ignore  # pylint: disable=no-member


class TestChartAnalytics(TestChart):
    def test_analytics_default_value(self) -> None:
        chart = Chart()
        self.assertEqual(
            chart.analytics,
            True,
        )

    def test_change_analytics_before_initializing(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            chart = Chart()
            chart.analytics = False
            chart.initializing()
            self.assertEqual(
                self.normalizer.normalize_output(output, 1),
                "if (window.IpyVizzu) window.IpyVizzu.changeAnalyticsTo(false);" + "\n"
                "window.ipyvizzu.createChart("
                + "element, "
                + "id, "
                + "'https://cdn.jsdelivr.net/npm/vizzu@0.8/dist/vizzu.min.js', "
                + "'800px', '480px');",
            )

    def test_change_analytics_after_initializing(self) -> None:
        with unittest.mock.patch(self.mock) as output:
            chart = Chart()
            chart.initializing()
            chart.analytics = False
            chart.analytics = True
            self.assertEqual(
                self.normalizer.normalize_output(output, 1),
                "if (window.IpyVizzu) window.IpyVizzu.changeAnalyticsTo(true);"
                + "\n"
                + "window.ipyvizzu.createChart("
                + "element, "
                + "id, "
                + "'https://cdn.jsdelivr.net/npm/vizzu@0.8/dist/vizzu.min.js', "
                + "'800px', '480px');"
                + "\n"
                + "if (window.IpyVizzu) window.IpyVizzu.changeAnalyticsTo(false);"
                + "\n"
                + "if (window.IpyVizzu) window.IpyVizzu.changeAnalyticsTo(true);",
            )


class TestChartDisplay(TestChart):
    def test_repr_html_if_display_is_not_manual(self) -> None:
        self.chart.animate(Snapshot("abc1234"))
        with self.assertRaises(AssertionError):
            self.chart._repr_html_()  # pylint: disable=protected-access

    def test_show_if_display_is_not_manual(self) -> None:
        self.chart.animate(Snapshot("abc1234"))
        with self.assertRaises(AssertionError):
            self.chart.show()

    def test_repr_html(self) -> None:
        display_mock = "ipyvizzu.Chart._display"
        with unittest.mock.patch(display_mock) as output:
            chart = Chart(display="manual")
            chart.animate(Snapshot("abc1234"))
            self.assertEqual(
                chart._showed,  # pylint: disable=protected-access
                False,
            )
            chart._repr_html_()  # pylint: disable=protected-access
            self.assertEqual(
                chart._showed,  # pylint: disable=protected-access
                True,
            )
            self.assertEqual(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.animate(element, id, id, 'manual', false, "
                + "lib => { return id }, "
                + "undefined);",
            )

    def test_show(self) -> None:
        self.chart = Chart(display="manual")
        display_mock = "ipyvizzu.Chart._display"
        with unittest.mock.patch(display_mock) as output:
            self.chart.animate(Snapshot("abc1234"))
            self.assertEqual(
                self.chart._showed,  # pylint: disable=protected-access
                False,
            )
            self.chart.show()
            self.assertEqual(
                self.chart._showed,  # pylint: disable=protected-access
                True,
            )
            self.assertEqual(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.animate(element, id, id, 'manual', false, "
                + "lib => { return id }, "
                + "undefined);",
            )

    def test_repr_html_after_repr_html(self) -> None:
        self.chart = Chart(display="manual")
        self.chart.animate(Snapshot("abc1234"))
        self.chart._repr_html_()  # pylint: disable=protected-access
        with self.assertRaises(AssertionError):
            self.chart._repr_html_()  # pylint: disable=protected-access

    def test_repr_html_after_show(self) -> None:
        self.chart = Chart(display="manual")
        self.chart.animate(Snapshot("abc1234"))
        self.chart.show()
        with self.assertRaises(AssertionError):
            self.chart._repr_html_()  # pylint: disable=protected-access

    def test_show_after_show(self) -> None:
        self.chart = Chart(display="manual")
        self.chart.animate(Snapshot("abc1234"))
        self.chart.show()
        with self.assertRaises(AssertionError):
            self.chart.show()

    def test_show_after_repr_html(self) -> None:
        self.chart = Chart(display="manual")
        self.chart.animate(Snapshot("abc1234"))
        self.chart._repr_html_()  # pylint: disable=protected-access
        with self.assertRaises(AssertionError):
            self.chart.show()

    def test_animate_after_repr_html(self) -> None:
        self.chart = Chart(display="manual")
        self.chart.animate(Snapshot("abc1234"))
        self.chart._repr_html_()  # pylint: disable=protected-access
        with self.assertRaises(AssertionError):
            self.chart.animate(Snapshot("abc1234"))

    def test_animate_after_show(self) -> None:
        self.chart = Chart(display="manual")
        self.chart.animate(Snapshot("abc1234"))
        self.chart.show()
        with self.assertRaises(AssertionError):
            self.chart.animate(Snapshot("abc1234"))

    def test_feature_after_repr_html(self) -> None:
        self.chart = Chart(display="manual")
        self.chart.animate(Snapshot("abc1234"))
        self.chart._repr_html_()  # pylint: disable=protected-access
        with self.assertRaises(AssertionError):
            self.chart.feature("tooltip", True)

    def test_feature_after_show(self) -> None:
        self.chart = Chart(display="manual")
        self.chart.animate(Snapshot("abc1234"))
        self.chart.show()
        with self.assertRaises(AssertionError):
            self.chart.feature("tooltip", True)

    def test_store_after_repr_html_(self) -> None:
        self.chart = Chart(display="manual")
        self.chart.animate(Snapshot("abc1234"))
        self.chart._repr_html_()  # pylint: disable=protected-access
        with self.assertRaises(AssertionError):
            self.chart.store()

    def test_store_after_show(self) -> None:
        self.chart = Chart(display="manual")
        self.chart.animate(Snapshot("abc1234"))
        self.chart.show()
        with self.assertRaises(AssertionError):
            self.chart.store()
