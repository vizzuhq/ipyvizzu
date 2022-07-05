"""A module for testing the ipyvizzu.pyhton.chart module."""

from abc import ABC, abstractmethod
import unittest
import unittest.mock

from tests.normalizer import Normalizer
from ipyvizzu import ChartProperty, Data, Config, Snapshot, Style, EventHandler


class TestChartABC(ABC):
    """
    An abstract class for testing Chart() class.
    It is responsible for setup and teardown.
    """

    @classmethod
    def setUpClass(cls) -> None:  # pylint: disable=invalid-name
        """A method for representing unittest setUpClass."""

        cls.normalizer = Normalizer()

    def setUp(self) -> None:  # pylint: disable=invalid-name
        """A method for representing unittest setUp."""

        self.patch = unittest.mock.patch(self.get_mock())
        self.trash = self.patch.start()
        self.chart = self.get_chart()

    def tearDown(self) -> None:  # pylint: disable=invalid-name
        """A method for representing unittest tearDown."""

        self.patch.stop()

    @abstractmethod
    def _assert_equal(self, *args, **kwargs):
        """An abstract method for representing unittest assertEqual."""

    @abstractmethod
    def _assert_raises(self, *args, **kwargs):
        """An abstract method for representing unittest assertRaises."""

    @abstractmethod
    def get_mock(self):
        """An abstract property for returning the method's name that needs to be mocked."""

    @abstractmethod
    def get_chart(self, *args, **kwargs):
        """An abstract property for returning Chart()."""


class TestChartInitABC(TestChartABC):
    """
    An abstract class for testing Chart() class.
    It tests the constructor of the Chart().
    """

    def test_init(self, reference) -> None:
        """A method for testing the default constructor parameters."""

        with unittest.mock.patch(self.get_mock()) as output:
            self.get_chart()
            self._assert_equal(
                self.normalizer.normalize_output(output, 1),
                reference,
            )

    def test_init_vizzu(self, reference) -> None:
        """A method for testing the "vizzu" constructor parameter."""

        with unittest.mock.patch(self.get_mock()) as output:
            self.get_chart(
                vizzu="https://cdn.jsdelivr.net/npm/vizzu@0.4.1/dist/vizzu.min.js"
            )
            self._assert_equal(
                self.normalizer.normalize_output(output, 1),
                reference,
            )

    def test_init_div(self, reference) -> None:
        """A method for testing the "width" and "height" constructor parameters."""

        with unittest.mock.patch(self.get_mock()) as output:
            self.get_chart(width="400px", height="240px")
            self._assert_equal(
                self.normalizer.normalize_output(output, 1),
                reference,
            )


class TestChartMethodsABC(TestChartABC):
    """
    An abstract class for testing Chart() class.
    It tests ipyvizzu.method-related methods.
    """

    def test_animate_chart_target_has_to_be_passed(self) -> None:
        """
        A method for testing Chart().animate() method.
        It raises an error if called without chart target.
        """

        with self._assert_raises(ValueError):
            self.chart.animate()

    def test_animate_chart_target_has_to_be_passed_even_if_chart_anim_opts_passed(
        self,
    ) -> None:
        """
        A method for testing Chart().animate() method.
        It raises an error if only called with anim options.
        """

        with self._assert_raises(ValueError):
            self.chart.animate(duration="500ms")

    def test_animate_one_chart_target(self, reference) -> None:
        """
        A method for testing Chart().animate() method.
        It tests with chart target.
        """

        with unittest.mock.patch(self.get_mock()) as output:
            data = Data()
            data.add_record(["Rock", "Hard", 96])
            self.chart.animate(data)
            self._assert_equal(
                self.normalizer.normalize_output(output),
                reference,
            )

    def test_animate_one_chart_target_with_chart_anim_opts(self, reference) -> None:
        """
        A method for testing Chart().animate() method.
        It tests with chart target and anim options.
        """

        with unittest.mock.patch(self.get_mock()) as output:
            data = Data()
            data.add_record(["Rock", "Hard", 96])
            self.chart.animate(data, duration="500ms")
            self._assert_equal(
                self.normalizer.normalize_output(output),
                reference,
            )

    def test_animate_snapshot_chart_target(self, reference) -> None:
        """
        A method for testing Chart().animate() method.
        It tests with Snapshot chart target.
        """

        with unittest.mock.patch(self.get_mock()) as output:
            snapshot = Snapshot("abc1234")
            self.chart.animate(snapshot)
            self._assert_equal(
                self.normalizer.normalize_output(output),
                reference,
            )

    def test_animate_snapshot_chart_target_with_chart_anim_opts(
        self, reference
    ) -> None:
        """
        A method for testing Chart().animate() method.
        It tests with Snapshot chart target and anim options.
        """

        with unittest.mock.patch(self.get_mock()) as output:
            snapshot = Snapshot("abc1234")
            self.chart.animate(snapshot, duration="500ms")
            self._assert_equal(
                self.normalizer.normalize_output(output),
                reference,
            )

    def test_animate_more_chart_target(self, reference) -> None:
        """
        A method for testing Chart().animate() method.
        It tests with multiple chart targets.
        """

        with unittest.mock.patch(self.get_mock()) as output:
            data = Data()
            data.add_record(["Rock", "Hard", 96])
            config = Config({"channels": {"label": {"attach": ["Popularity"]}}})
            style = Style({"title": {"backgroundColor": "#A0A0A0"}})
            self.chart.animate(data, config, style)
            self._assert_equal(
                self.normalizer.normalize_output(output),
                reference,
            )

    def test_animate_more_chart_target_with_chart_anim_opts(self, reference) -> None:
        """
        A method for testing Chart().animate() method.
        It tests with multiple chart targets and anim options.
        """

        with unittest.mock.patch(self.get_mock()) as output:
            data = Data()
            data.add_record(["Rock", "Hard", 96])
            config = Config({"channels": {"label": {"attach": ["Popularity"]}}})
            style = Style({"title": {"backgroundColor": "#A0A0A0"}})
            self.chart.animate(data, config, style, duration="500ms")
            self._assert_equal(
                self.normalizer.normalize_output(output),
                reference,
            )

    def test_animate_more_chart_target_with_conflict(self) -> None:
        """
        A method for testing Chart().animate() method.
        It tests with same types of chart target.
        """

        data = Data()
        data.add_record(["Rock", "Hard", 96])
        config1 = Config({"channels": {"label": {"attach": ["Popularity"]}}})
        config2 = Config({"title": "Test"})
        style = Style({"title": {"backgroundColor": "#A0A0A0"}})
        with self._assert_raises(ValueError):
            self.chart.animate(data, config1, style, config2)

    def test_animate_more_chart_target_with_snapshot(self) -> None:
        """
        A method for testing Chart().animate() method.
        It raises an error if called with multiple chart targets and Snapshot chart target.
        """

        data = Data()
        data.add_record(["Rock", "Hard", 96])
        config = Config({"channels": {"label": {"attach": ["Popularity"]}}})
        style = Style({"title": {"backgroundColor": "#A0A0A0"}})
        snapshot = Snapshot("abc1234")
        with self._assert_raises(NotImplementedError):
            self.chart.animate(data, config, style, snapshot)

    def test_animate_more_calls(self, reference) -> None:
        """
        A method for testing Chart().animate() method.
        It tests multiple calls.
        """

        with unittest.mock.patch(self.get_mock()) as output:
            data = Data()
            data.add_record(["Rock", "Hard", 96])
            config1 = Config({"channels": {"label": {"attach": ["Popularity"]}}})
            config2 = Config({"title": "Test"})
            style = Style({"title": {"backgroundColor": "#A0A0A0"}})
            self.chart.animate(data, config1, style)
            self.chart.animate(config2)
            self._assert_equal(
                self.normalizer.normalize_output(output),
                reference,
            )

    def test_animate_with_not_default_scroll_into_view(self, reference) -> None:
        """
        A method for testing Chart().animate() method.
        It tests with "scroll_into_view=True".
        """

        with unittest.mock.patch(self.get_mock()) as output:
            data = Data()
            data.add_record(["Rock", "Hard", 96])
            scroll_into_view = not self.chart.scroll_into_view
            self.chart.scroll_into_view = scroll_into_view
            self.chart.animate(data)
            self._assert_equal(
                self.normalizer.normalize_output(output),
                reference.format(str(scroll_into_view).lower()),
            )

    def test_feature(self, reference) -> None:
        """A method for testing Chart().feature() method."""

        with unittest.mock.patch(self.get_mock()) as output:
            self.chart.feature("tooltip", True)
            self._assert_equal(
                self.normalizer.normalize_output(output),
                reference,
            )

    def test_store(self, reference) -> None:
        """A method for testing Chart().store() method."""

        with unittest.mock.patch(self.get_mock()) as output:
            self.chart.store()
            self._assert_equal(
                self.normalizer.normalize_output(output),
                reference,
            )


class TestChartEventsABC(TestChartABC):
    """
    An abstract class for testing Chart() class.
    It tests event-related methods.
    """

    def test_on(self, reference) -> None:
        """A method for testing Chart().on() method."""

        with unittest.mock.patch(self.get_mock()) as output:
            handler_method = """event.renderingContext.fillStyle =
                (event.data.text === 'Jazz') ? 'red' : 'gray';"""
            self.chart.on("plot-axis-label-draw", handler_method)
            self._assert_equal(
                self.normalizer.normalize_output(output),
                reference,
            )

    def test_off(self, reference) -> None:
        """A method for testing Chart().off() method."""

        with unittest.mock.patch(self.get_mock()) as output:
            handler_method = "alert(JSON.stringify(event.data));"
            handler = EventHandler("click", handler_method)
            self.chart.off(handler)
            self._assert_equal(
                self.normalizer.normalize_output(output),
                reference,
            )


class TestChartLogsABC(TestChartABC):
    """
    An abstract class for testing Chart() class.
    It tests log-related methods.
    """

    def test_log_config(self, reference) -> None:
        """A method for testing Chart().log() method (ChartProperty.CONFIG)."""

        with unittest.mock.patch(self.get_mock()) as output:
            self.chart.log(ChartProperty.CONFIG)
            self._assert_equal(
                self.normalizer.normalize_output(output),
                reference,
            )

    def test_log_style(self, reference) -> None:
        """A method for testing Chart().log() method (ChartProperty.STYLE)."""

        with unittest.mock.patch(self.get_mock()) as output:
            self.chart.log(ChartProperty.STYLE)
            self._assert_equal(
                self.normalizer.normalize_output(output),
                reference,
            )

    def test_log_invalid(self) -> None:
        """A method for testing Chart().log() method with an invalid value."""

        with self._assert_raises(AttributeError):
            self.chart.log(ChartProperty.INVALID)  # pylint: disable=no-member
