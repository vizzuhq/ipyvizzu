import abc
import unittest
import unittest.mock

from tests.normalizer import Normalizer


class TestChartInit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if cls is TestChartInit:
            raise unittest.SkipTest()
        super(TestChartInit, cls).setUpClass()
        cls.normalizer = Normalizer()

    @abc.abstractmethod
    def get_mock(self):
        """
        Return mock
        """

    @abc.abstractmethod
    def get_chart(self, *args, **kwargs):
        """
        Return Chart(*args, **kwargs)
        """

    def test_init(self, ref=None):
        with unittest.mock.patch(self.get_mock()) as output:
            self.get_chart()
            self.assertEqual(
                self.normalizer.normalize_output(output, 1),
                ref,
            )

    def test_init_vizzu(self, ref=None):
        with unittest.mock.patch(self.get_mock()) as output:
            self.get_chart(
                vizzu="https://cdn.jsdelivr.net/npm/vizzu@0.4.1/dist/vizzu.min.js"
            )
            self.assertEqual(
                self.normalizer.normalize_output(output, 1),
                ref,
            )

    def test_init_div(self, ref=None):
        with unittest.mock.patch(self.get_mock()) as output:
            self.get_chart(width="400px", height="240px")
            self.assertEqual(
                self.normalizer.normalize_output(output, 1),
                ref,
            )


class TestChartMethods(unittest.TestCase):

    # pylint: disable=too-many-public-methods

    @classmethod
    def setUpClass(cls):
        if cls is TestChartMethods:
            raise unittest.SkipTest()
        super(TestChartMethods, cls).setUpClass()
        cls.normalizer = Normalizer()

    def setUp(self):
        self.chart = self.get_chart()

    @abc.abstractmethod
    def get_mock(self):
        """
        Return mock
        """

    @abc.abstractmethod
    def get_chart(self, *args, **kwargs):
        """
        Return Chart(*args, **kwargs)
        """

    @abc.abstractmethod
    def get_data(self):
        """
        Return Data()
        """

    @abc.abstractmethod
    def get_config(self, config):
        """
        Return Config(config)
        """

    @abc.abstractmethod
    def get_style(self, style):
        """
        Return Style(style)
        """

    @abc.abstractmethod
    def get_snapshot(self, snapshot_id):
        """
        Return Snapshot(snapshot_id)
        """

    def test_animate_chart_target_has_to_be_passed(self):
        with self.assertRaises(ValueError):
            self.chart.animate()

    def test_animate_chart_target_has_to_be_passed_even_if_chart_anim_opts_passed(self):
        with self.assertRaises(ValueError):
            self.chart.animate(duration="500ms")

    def test_animate_one_chart_target(self, ref=None):
        with unittest.mock.patch(self.get_mock()) as output:
            data = self.get_data()
            data.add_record(["Rock", "Hard", 96])
            self.chart.animate(data)
            self.assertEqual(
                self.normalizer.normalize_output(output),
                ref,
            )

    def test_animate_one_chart_target_with_chart_anim_opts(self, ref=None):
        with unittest.mock.patch(self.get_mock()) as output:
            data = self.get_data()
            data.add_record(["Rock", "Hard", 96])
            self.chart.animate(data, duration="500ms")
            self.assertEqual(
                self.normalizer.normalize_output(output),
                ref,
            )

    def test_animate_snapshot_chart_target(self, ref=None):
        with unittest.mock.patch(self.get_mock()) as output:
            snapshot = self.get_snapshot("abc1234")
            self.chart.animate(snapshot)
            self.assertEqual(
                self.normalizer.normalize_output(output),
                ref,
            )

    def test_animate_snapshot_chart_target_with_chart_anim_opts(self, ref=None):
        with unittest.mock.patch(self.get_mock()) as output:
            snapshot = self.get_snapshot("abc1234")
            self.chart.animate(snapshot, duration="500ms")
            self.assertEqual(
                self.normalizer.normalize_output(output),
                ref,
            )

    def test_animate_more_chart_target(self, ref=None):
        with unittest.mock.patch(self.get_mock()) as output:
            data = self.get_data()
            data.add_record(["Rock", "Hard", 96])
            config = self.get_config(
                {"channels": {"label": {"attach": ["Popularity"]}}}
            )
            style = self.get_style({"title": {"backgroundColor": "#A0A0A0"}})
            self.chart.animate(data, config, style)
            self.assertEqual(
                self.normalizer.normalize_output(output),
                ref,
            )

    def test_animate_more_chart_target_with_chart_anim_opts(self, ref=None):
        with unittest.mock.patch(self.get_mock()) as output:
            data = self.get_data()
            data.add_record(["Rock", "Hard", 96])
            config = self.get_config(
                {"channels": {"label": {"attach": ["Popularity"]}}}
            )
            style = self.get_style({"title": {"backgroundColor": "#A0A0A0"}})
            self.chart.animate(data, config, style, duration="500ms")
            self.assertEqual(
                self.normalizer.normalize_output(output),
                ref,
            )

    def test_animate_more_chart_target_with_conflict(self):
        data = self.get_data()
        data.add_record(["Rock", "Hard", 96])
        config1 = self.get_config({"channels": {"label": {"attach": ["Popularity"]}}})
        config2 = self.get_config({"title": "Test"})
        style = self.get_style({"title": {"backgroundColor": "#A0A0A0"}})
        with self.assertRaises(ValueError):
            self.chart.animate(data, config1, style, config2)

    def test_animate_more_chart_target_with_snapshot(self):
        data = self.get_data()
        data.add_record(["Rock", "Hard", 96])
        config = self.get_config({"channels": {"label": {"attach": ["Popularity"]}}})
        style = self.get_style({"title": {"backgroundColor": "#A0A0A0"}})
        snapshot = self.get_snapshot("abc1234")
        with self.assertRaises(NotImplementedError):
            self.chart.animate(data, config, style, snapshot)

    def test_animate_more_calls(self, ref=None):
        with unittest.mock.patch(self.get_mock()) as output:
            data = self.get_data()
            data.add_record(["Rock", "Hard", 96])
            config1 = self.get_config(
                {"channels": {"label": {"attach": ["Popularity"]}}}
            )
            config2 = self.get_config({"title": "Test"})
            style = self.get_style({"title": {"backgroundColor": "#A0A0A0"}})
            self.chart.animate(data, config1, style)
            self.chart.animate(config2)
            self.assertEqual(
                self.normalizer.normalize_output(output),
                ref,
            )

    def test_animate_with_not_default_scroll_into_view(self, ref=None):
        with unittest.mock.patch(self.get_mock()) as output:
            data = self.get_data()
            data.add_record(["Rock", "Hard", 96])
            scroll_into_view = not self.chart.scroll_into_view
            self.chart.scroll_into_view = scroll_into_view
            self.chart.animate(data)
            self.assertEqual(
                self.normalizer.normalize_output(output),
                ref,
            )

    def test_feature(self, ref=None):
        with unittest.mock.patch(self.get_mock()) as output:
            self.chart.feature("tooltip", True)
            self.assertEqual(
                self.normalizer.normalize_output(output),
                ref,
            )

    def test_store(self, ref=None):
        with unittest.mock.patch(self.get_mock()) as output:
            self.chart.store()
            self.assertEqual(
                self.normalizer.normalize_output(output),
                ref,
            )


class TestChartShow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if cls is TestChartShow:
            raise unittest.SkipTest()
        super(TestChartShow, cls).setUpClass()
        cls.normalizer = Normalizer()

    @abc.abstractmethod
    def get_mock(self):
        """
        Return mock
        """

    @abc.abstractmethod
    def get_chart(self):
        """
        Return Chart()
        """

    @abc.abstractmethod
    def get_snapshot(self, snapshot_id):
        """
        Return Snapshot(snapshot_id)
        """

    def test_show(self, ref=None):
        chart = self.get_chart()
        with unittest.mock.patch(self.get_mock()) as output:
            chart.animate(self.get_snapshot("abc1234"))
            self.assertEqual(
                chart._js["showed"],  # pylint: disable=protected-access
                False,
            )
            chart.show()
            self.assertEqual(
                chart._js["showed"],  # pylint: disable=protected-access
                True,
            )
            self.assertEqual(
                self.normalizer.normalize_output(output),
                ref,
            )

    def test_show_after_show(self):
        chart = self.get_chart()
        chart.animate(self.get_snapshot("abc1234"))
        chart.show()
        with self.assertRaises(AssertionError):
            chart.show()

    def test_animate_after_show(self):
        chart = self.get_chart()
        chart.animate(self.get_snapshot("abc1234"))
        chart.show()
        with self.assertRaises(AssertionError):
            chart.animate(self.get_snapshot("abc1234"))

    def test_feature_after_show(self):
        chart = self.get_chart()
        chart.animate(self.get_snapshot("abc1234"))
        chart.show()
        with self.assertRaises(AssertionError):
            chart.feature("tooltip", True)

    def test_store_after_show(self):
        chart = self.get_chart()
        chart.animate(self.get_snapshot("abc1234"))
        chart.show()
        with self.assertRaises(AssertionError):
            chart.store()
