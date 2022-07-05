"""A module for testing the ipyvizzu.jupyter.chart module."""

import unittest
import unittest.mock
from typing import Callable

from tests.normalizer import Normalizer
from tests.chart import (
    TestChartABC,
    TestChartInitABC,
    TestChartMethodsABC,
    TestChartEventsABC,
    TestChartLogsABC,
)
from ipyvizzu import Snapshot
from ipyvizzu.jupyter.chart import Chart


class TestChart(TestChartABC):
    """
    An abstract class for testing Chart() class.
    It is responsible for setup and teardown.
    """

    def get_mock(self):
        return "ipyvizzu.jupyter.chart.display_javascript"

    def get_chart(self, *args, **kwargs):
        return Chart(*args, **kwargs)


class TestChartInit(TestChart, TestChartInitABC, unittest.TestCase):
    """
    A class for testing Chart() class.
    It tests the constructor of the Chart().
    """

    def _assert_equal(self, *args, **kwargs):
        self.assertEqual(*args, **kwargs)

    def _assert_raises(self, *args, **kwargs):
        return self.assertRaises(*args, **kwargs)

    def test_init(
        self,
        reference="window.ipyvizzu.createChart("
        + "element, "
        + "id, "
        + "'https://cdn.jsdelivr.net/npm/vizzu@~0.4.0/dist/vizzu.min.js', "
        + "'800px', '480px');",
    ) -> None:
        """A method for testing the default constructor parameters."""

        super().test_init(reference)

    def test_init_vizzu(
        self,
        reference="window.ipyvizzu.createChart("
        + "element, "
        + "id, "
        + "'https://cdn.jsdelivr.net/npm/vizzu@0.4.1/dist/vizzu.min.js', "
        + "'800px', '480px');",
    ) -> None:
        """A method for testing the "vizzu" constructor parameter."""

        super().test_init_vizzu(reference)

    def test_init_div(
        self,
        reference="window.ipyvizzu.createChart("
        + "element, "
        + "id, "
        + "'https://cdn.jsdelivr.net/npm/vizzu@~0.4.0/dist/vizzu.min.js', "
        + "'400px', '240px');",
    ) -> None:
        """A method for testing the "width" and "height" constructor parameters."""

        super().test_init_div(reference)

    def test_init_display_invalid(self) -> None:
        """A method for testing the "display" constructor parameter (display=invalid)."""

        with self._assert_raises(ValueError):
            self.get_chart(display="invalid")

    def test_init_display_begin(self) -> None:
        """A method for testing the "display" constructor parameter (display=begin)."""

        self.chart = self.get_chart(display="begin")
        with unittest.mock.patch(self.get_mock()) as output:
            self.chart.animate(Snapshot("abc1234"))
            self._assert_equal(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.animate(element, id, 'begin', false, "
                + "id, "
                + "undefined);",
            )

    def test_init_display_actual(self) -> None:
        """A method for testing the "display" constructor parameter (display=actual)."""

        self.chart = self.get_chart(display="actual")
        with unittest.mock.patch(self.get_mock()) as output:
            self.chart.animate(Snapshot("abc1234"))
            self._assert_equal(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.animate(element, id, 'actual', false, "
                + "id, "
                + "undefined);",
            )

    def test_init_display_end(self) -> None:
        """A method for testing the "display" constructor parameter (display=end)."""

        self.chart = self.get_chart(display="end")
        with unittest.mock.patch(self.get_mock()) as output:
            self.chart.animate(Snapshot("abc1234"))
            self._assert_equal(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.animate(element, id, 'end', false, "
                + "id, "
                + "undefined);",
            )

    def test_init_register_events(self) -> None:
        """A method for testing Chart()._register_events() method."""

        class IPyEvents:
            """A class for mocking get_ipython().events object."""

            # pylint: disable=too-few-public-methods

            @staticmethod
            def register(event: str, function: Callable) -> None:
                """A method for mocking get_ipython().events.register() method."""

                # pylint: disable=unused-argument

                function()

        class IPy:
            """A class for mocking get_ipython() object."""

            # pylint: disable=too-few-public-methods

            events = IPyEvents

        get_ipython_mock = "ipyvizzu.jupyter.chart.get_ipython"
        with unittest.mock.patch(get_ipython_mock, return_value=IPy()):
            with unittest.mock.patch(self.get_mock()) as output:
                self.get_chart()
                self._assert_equal(
                    self.normalizer.normalize_output(output, 2),
                    "if (window.IpyVizzu) { window.IpyVizzu.clearInhibitScroll(element); }",
                )


class TestChartMethods(TestChart, TestChartMethodsABC, unittest.TestCase):
    """
    A class for testing Chart() class.
    It tests ipyvizzu.method-related methods.
    """

    def _assert_equal(self, *args, **kwargs):
        self.assertEqual(*args, **kwargs)

    def _assert_raises(self, *args, **kwargs):
        return self.assertRaises(*args, **kwargs)

    def test_animate_one_chart_target(
        self,
        reference="window.ipyvizzu.animate(element, id, 'actual', false, "
        + '{"data": {"records": [["Rock", "Hard", 96]]}}, '
        + "undefined);",
    ) -> None:
        """
        A method for testing Chart().animate() method.
        It tests with chart target.
        """

        super().test_animate_one_chart_target(reference)

    def test_animate_one_chart_target_with_chart_anim_opts(
        self,
        reference="window.ipyvizzu.animate(element, id, 'actual', false, "
        + '{"data": {"records": [["Rock", "Hard", 96]]}}, '
        + '{"duration": "500ms"});',
    ) -> None:
        """
        A method for testing Chart().animate() method.
        It tests with chart target and anim options.
        """

        super().test_animate_one_chart_target_with_chart_anim_opts(reference)

    def test_animate_snapshot_chart_target(
        self,
        reference="window.ipyvizzu.animate(element, id, 'actual', false, "
        + "id, "
        + "undefined);",
    ) -> None:
        """
        A method for testing Chart().animate() method.
        It tests with Snapshot chart target.
        """

        super().test_animate_snapshot_chart_target(reference)

    def test_animate_snapshot_chart_target_with_chart_anim_opts(
        self,
        reference="window.ipyvizzu.animate(element, id, 'actual', false, "
        + "id, "
        + '{"duration": "500ms"});',
    ) -> None:
        """
        A method for testing Chart().animate() method.
        It tests with Snapshot chart target and anim options.
        """

        super().test_animate_snapshot_chart_target_with_chart_anim_opts(reference)

    def test_animate_more_chart_target(
        self,
        reference="window.ipyvizzu.animate(element, id, 'actual', false, "
        + '{"data": {"records": [["Rock", "Hard", 96]]}, '
        + '"config": {"channels": {"label": {"attach": ["Popularity"]}}}, '
        + '"style": {"title": {"backgroundColor": "#A0A0A0"}}}, '
        + "undefined);",
    ) -> None:
        """
        A method for testing Chart().animate() method.
        It tests with multiple chart targets.
        """

        super().test_animate_more_chart_target(reference)

    def test_animate_more_chart_target_with_chart_anim_opts(
        self,
        reference="window.ipyvizzu.animate(element, id, 'actual', false, "
        + '{"data": {"records": [["Rock", "Hard", 96]]}, '
        + '"config": {"channels": {"label": {"attach": ["Popularity"]}}}, '
        + '"style": {"title": {"backgroundColor": "#A0A0A0"}}}, '
        + '{"duration": "500ms"});',
    ) -> None:
        """
        A method for testing Chart().animate() method.
        It tests with multiple chart targets and anim options.
        """

        super().test_animate_more_chart_target_with_chart_anim_opts(reference)

    def test_animate_more_calls(
        self,
        reference="window.ipyvizzu.animate(element, id, 'actual', false, "
        + '{"data": {"records": [["Rock", "Hard", 96]]}, '
        + '"config": {"channels": {"label": {"attach": ["Popularity"]}}}, '
        + '"style": {"title": {"backgroundColor": "#A0A0A0"}}}, '
        + "undefined);\n"
        + "window.ipyvizzu.animate(element, id, 'actual', false, "
        + '{"config": {"title": "Test"}}, '
        + "undefined);",
    ) -> None:
        """
        A method for testing Chart().animate() method.
        It tests multiple calls.
        """

        super().test_animate_more_calls(reference)

    def test_animate_with_not_default_scroll_into_view(
        self,
        reference="window.ipyvizzu.animate(element, id, 'actual', {}, "
        + '{{"data": {{"records": [["Rock", "Hard", 96]]}}}}, '
        + "undefined);",
    ) -> None:
        """
        A method for testing Chart().animate() method.
        It tests with "scroll_into_view=True".
        """

        super().test_animate_with_not_default_scroll_into_view(reference)

    def test_feature(
        self, reference="window.ipyvizzu.feature(element, id, 'tooltip', true);"
    ) -> None:
        """A method for testing Chart().feature() method."""

        super().test_feature(reference)

    def test_store(self, reference="window.ipyvizzu.store(element, id, id);") -> None:
        """A method for testing Chart().store() method."""

        super().test_store(reference)


class TestChartEvents(TestChart, TestChartEventsABC, unittest.TestCase):
    """
    A class for testing Chart() class.
    It tests event-related methods.
    """

    def _assert_equal(self, *args, **kwargs):
        self.assertEqual(*args, **kwargs)

    def _assert_raises(self, *args, **kwargs):
        return self.assertRaises(*args, **kwargs)

    def test_on(
        self,
        reference="window.ipyvizzu.setEvent("
        + "element, id, id, 'plot-axis-label-draw', "
        + "event => "
        + "{ event.renderingContext.fillStyle = "
        + "(event.data.text === 'Jazz') ? 'red' : 'gray'; });",
    ) -> None:
        """A method for testing Chart().on() method."""

        super().test_on(reference)

    def test_off(
        self, reference="window.ipyvizzu.clearEvent(element, id, id, 'click');"
    ) -> None:
        """A method for testing Chart().off() method."""

        super().test_off(reference)


class TestChartLogs(TestChart, TestChartLogsABC, unittest.TestCase):
    """
    A class for testing Chart() class.
    It tests log-related methods.
    """

    def _assert_equal(self, *args, **kwargs):
        self.assertEqual(*args, **kwargs)

    def _assert_raises(self, *args, **kwargs):
        return self.assertRaises(*args, **kwargs)

    def test_log_config(
        self, reference="window.ipyvizzu.log(element, id, 'config');"
    ) -> None:
        """A method for testing Chart().log() method (ChartProperty.CONFIG)."""

        super().test_log_config(reference)

    def test_log_style(
        self, reference="window.ipyvizzu.log(element, id, 'style');"
    ) -> None:
        """A method for testing Chart().log() method (ChartProperty.STYLE)."""

        super().test_log_style(reference)


class TestChartShow(unittest.TestCase):
    """
    A class for testing Chart() class.
    It tests display-related methods.
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.normalizer = Normalizer()

    def setUp(self):
        self.patch = unittest.mock.patch("ipyvizzu.jupyter.chart.display_javascript")
        self.trash = self.patch.start()

    def tearDown(self):
        self.patch.stop()

    def test_show_if_display_is_not_manual(self) -> None:
        """A method for testing Chart().show() method (display!=manual)."""

        chart = Chart()
        chart.animate(Snapshot("abc1234"))
        with self.assertRaises(AssertionError):
            chart.show()

    def test_show(self) -> None:
        """A method for testing Chart().show() method (display=manual)."""

        chart = Chart(display="manual")
        display_mock = "ipyvizzu.jupyter.chart.Chart._display"
        with unittest.mock.patch(display_mock) as output:
            chart.animate(Snapshot("abc1234"))
            self.assertEqual(
                chart._showed,  # pylint: disable=protected-access
                False,
            )
            chart.show()
            self.assertEqual(
                chart._showed,  # pylint: disable=protected-access
                True,
            )
            self.assertEqual(
                self.normalizer.normalize_output(output),
                "window.ipyvizzu.animate(element, id, 'manual', false, "
                + "id, "
                + "undefined);",
            )

    def test_show_after_show(self) -> None:
        """
        A method for testing Chart().show() method.
        It raises an error if called after Chart().show().
        """

        chart = Chart(display="manual")
        chart.animate(Snapshot("abc1234"))
        chart.show()
        with self.assertRaises(AssertionError):
            chart.show()

    def test_animate_after_show(self) -> None:
        """
        A method for testing Chart().animate() method.
        It raises an error if called after Chart().show().
        """

        chart = Chart(display="manual")
        chart.animate(Snapshot("abc1234"))
        chart.show()
        with self.assertRaises(AssertionError):
            chart.animate(Snapshot("abc1234"))

    def test_feature_after_show(self) -> None:
        """
        A method for testing Chart().feature() method.
        It raises an error if called after Chart().show().
        """

        chart = Chart(display="manual")
        chart.animate(Snapshot("abc1234"))
        chart.show()
        with self.assertRaises(AssertionError):
            chart.feature("tooltip", True)

    def test_store_after_show(self) -> None:
        """
        A method for testing Chart().store() method.
        It raises an error if called after Chart().show().
        """

        chart = Chart(display="manual")
        chart.animate(Snapshot("abc1234"))
        chart.show()
        with self.assertRaises(AssertionError):
            chart.store()


class TestChartReprHtml(unittest.TestCase):
    """
    A class for testing Chart() class.
    It tests display-related methods.
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.normalizer = Normalizer()

    def setUp(self):
        self.patch = unittest.mock.patch("ipyvizzu.jupyter.chart.display_javascript")
        self.trash = self.patch.start()

    def tearDown(self):
        self.patch.stop()

    def test_repr_html_if_display_is_not_manual(self) -> None:
        """A method for testing Chart()._repr_html_() method (display!=manual)."""

        chart = Chart()
        chart.animate(Snapshot("abc1234"))
        with self.assertRaises(AssertionError):
            chart._repr_html_()  # pylint: disable=protected-access

    def test_repr_html(self) -> None:
        """A method for testing Chart()._repr_html_() method (display=manual)."""

        chart = Chart(display="manual")
        display_mock = "ipyvizzu.jupyter.chart.Chart._display"
        with unittest.mock.patch(display_mock) as output:
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
                "window.ipyvizzu.animate(element, id, 'manual', false, "
                + "id, "
                + "undefined);",
            )

    def test_repr_html_after_repr_html(self) -> None:
        """
        A method for testing Chart()._repr_html_() method.
        It raises an error if called after Chart()._repr_html_().
        """

        chart = Chart(display="manual")
        chart.animate(Snapshot("abc1234"))
        chart._repr_html_()  # pylint: disable=protected-access
        with self.assertRaises(AssertionError):
            chart._repr_html_()  # pylint: disable=protected-access

    def test_repr_html_after_show(self) -> None:
        """
        A method for testing Chart()._repr_html_() method.
        It raises an error if called after Chart().show().
        """

        chart = Chart(display="manual")
        chart.animate(Snapshot("abc1234"))
        chart.show()
        with self.assertRaises(AssertionError):
            chart._repr_html_()  # pylint: disable=protected-access

    def test_show_after_repr_html(self) -> None:
        """
        A method for testing Chart().show() method.
        It raises an error if called after Chart()._repr_html_().
        """

        chart = Chart(display="manual")
        chart.animate(Snapshot("abc1234"))
        chart._repr_html_()  # pylint: disable=protected-access
        with self.assertRaises(AssertionError):
            chart.show()

    def test_animate_after_repr_html(self) -> None:
        """
        A method for testing Chart().animate() method.
        It raises an error if called after Chart()._repr_html_().
        """

        chart = Chart(display="manual")
        chart.animate(Snapshot("abc1234"))
        chart._repr_html_()  # pylint: disable=protected-access
        with self.assertRaises(AssertionError):
            chart.animate(Snapshot("abc1234"))

    def test_feature_after_repr_html(self) -> None:
        """
        A method for testing Chart().feature() method.
        It raises an error if called after Chart()._repr_html_().
        """

        chart = Chart(display="manual")
        chart.animate(Snapshot("abc1234"))
        chart._repr_html_()  # pylint: disable=protected-access
        with self.assertRaises(AssertionError):
            chart.feature("tooltip", True)

    def test_store_after_repr_html_(self) -> None:
        """
        A method for testing Chart().store() method.
        It raises an error if called after Chart()._repr_html_().
        """

        chart = Chart(display="manual")
        chart.animate(Snapshot("abc1234"))
        chart._repr_html_()  # pylint: disable=protected-access
        with self.assertRaises(AssertionError):
            chart.store()
