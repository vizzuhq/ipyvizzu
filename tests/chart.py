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

    def setUp(self):
        self.patch = self.get_patch()
        self.javascript = self.patch.start()

    def tearDown(self):
        self.patch.stop()

    @abc.abstractmethod
    def get_patch(self):
        """
        Return patch
        """

    @abc.abstractmethod
    def get_chart(self, *args, **kwargs):
        """
        Return Chart(*args, **kwargs)
        """

    def test_init(self, ref):
        self.get_chart()
        self.assertEqual(
            self.normalizer.normalize_id(
                self.javascript.call_args_list[1].args[0].strip().splitlines()[-1]
            ).strip(),
            ref,
        )

    def test_init_vizzu(self, ref):
        self.get_chart(
            vizzu="https://cdn.jsdelivr.net/npm/vizzu@0.4.1/dist/vizzu.min.js"
        )
        self.assertEqual(
            self.normalizer.normalize_id(
                self.javascript.call_args_list[1].args[0].strip().splitlines()[-1]
            ).strip(),
            ref,
        )

    def test_init_div(self, ref):
        self.get_chart(width="400px", height="240px")
        self.assertEqual(
            self.normalizer.normalize_id(
                self.javascript.call_args_list[1].args[0].strip().splitlines()[-1]
            ).strip(),
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
        self.patch = self.get_patch()
        self.trash = self.patch.start()
        self.chart = self.get_chart()
        self.javascript = self.patch.start()

    def tearDown(self):
        self.patch.stop()

    @abc.abstractmethod
    def get_patch(self):
        """
        Return patch
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

    def test_animate_one_chart_target(self, ref):
        data = self.get_data()
        data.add_record(["Rock", "Hard", 96])
        self.chart.animate(data)
        self.assertEqual(
            self.normalizer.normalize_id(
                self.javascript.call_args_list[0].args[0].strip().splitlines()[-1]
            ).strip(),
            ref,
        )

    def test_animate_one_chart_target_with_chart_anim_opts(self, ref):
        data = self.get_data()
        data.add_record(["Rock", "Hard", 96])
        self.chart.animate(data, duration="500ms")
        self.assertEqual(
            self.normalizer.normalize_id(
                self.javascript.call_args_list[0].args[0].strip().splitlines()[-1]
            ).strip(),
            ref,
        )

    def test_animate_snapshot_chart_target(self, ref):
        snapshot = self.get_snapshot("abc1234")
        self.chart.animate(snapshot)
        self.assertEqual(
            self.normalizer.normalize_id(
                self.javascript.call_args_list[0].args[0].strip().splitlines()[-1]
            ).strip(),
            ref,
        )

    def test_animate_snapshot_chart_target_with_chart_anim_opts(self, ref):
        snapshot = self.get_snapshot("abc1234")
        self.chart.animate(snapshot, duration="500ms")
        self.assertEqual(
            self.normalizer.normalize_id(
                self.javascript.call_args_list[0].args[0].strip().splitlines()[-1]
            ).strip(),
            ref,
        )

    def test_animate_more_chart_target(self, ref):
        data = self.get_data()
        data.add_record(["Rock", "Hard", 96])
        config = self.get_config({"channels": {"label": {"attach": ["Popularity"]}}})
        style = self.get_style({"title": {"backgroundColor": "#A0A0A0"}})
        self.chart.animate(data, config, style)
        self.assertEqual(
            self.normalizer.normalize_id(
                self.javascript.call_args_list[0].args[0].strip().splitlines()[-1]
            ).strip(),
            ref,
        )

    def test_animate_more_chart_target_with_chart_anim_opts(self, ref):
        data = self.get_data()
        data.add_record(["Rock", "Hard", 96])
        config = self.get_config({"channels": {"label": {"attach": ["Popularity"]}}})
        style = self.get_style({"title": {"backgroundColor": "#A0A0A0"}})
        self.chart.animate(data, config, style, duration="500ms")
        self.assertEqual(
            self.normalizer.normalize_id(
                self.javascript.call_args_list[0].args[0].strip().splitlines()[-1]
            ).strip(),
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

    def test_animate_more_calls(self, ref):
        data = self.get_data()
        data.add_record(["Rock", "Hard", 96])
        config1 = self.get_config({"channels": {"label": {"attach": ["Popularity"]}}})
        config2 = self.get_config({"title": "Test"})
        style = self.get_style({"title": {"backgroundColor": "#A0A0A0"}})
        self.chart.animate(data, config1, style)
        self.chart.animate(config2)
        self.assertEqual(
            self.normalizer.normalize_id(
                self.javascript.call_args_list[0].args[0].strip().splitlines()[-1]
            ).strip()
            + "\n"
            + self.normalizer.normalize_id(
                self.javascript.call_args_list[1].args[0].strip().splitlines()[-1]
            ).strip(),
            ref,
        )

    def test_animate_with_not_default_scroll_into_view(self, ref):
        data = self.get_data()
        data.add_record(["Rock", "Hard", 96])
        scroll_into_view = not self.chart.scroll_into_view
        self.chart.scroll_into_view = scroll_into_view
        self.chart.animate(data)
        self.assertEqual(
            self.normalizer.normalize_id(
                self.javascript.call_args_list[0].args[0].strip().splitlines()[-1]
            ).strip(),
            ref,
        )

    def test_feature(self, ref):
        self.chart.feature("tooltip", True)
        self.assertEqual(
            self.normalizer.normalize_id(
                self.javascript.call_args_list[0].args[0].strip().splitlines()[-1]
            ).strip(),
            ref,
        )

    def test_store(self, ref):
        self.chart.store()
        self.assertEqual(
            self.normalizer.normalize_id(
                self.javascript.call_args_list[0].args[0].strip().splitlines()[-1]
            ).strip(),
            ref,
        )


class TestChartShow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if cls is TestChartShow:
            raise unittest.SkipTest()
        super(TestChartShow, cls).setUpClass()
        cls.normalizer = Normalizer()

    def setUp(self):
        self.patch = self.get_patch()

    def tearDown(self):
        self.patch.stop()

    @abc.abstractmethod
    def get_patch(self):
        """
        Return patch
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

    def test_show(self, ref):
        javascript = self.patch.start()
        chart = self.get_chart()
        chart.animate(self.get_snapshot("abc1234"))
        self.assertEqual(
            chart._js["showed"],  # pylint: disable=protected-access
            False,
        )
        chart.show()
        self.assertEqual(
            self.normalizer.normalize_id(
                javascript.call_args_list[2].args[0].strip().splitlines()[-1]
            ).strip(),
            ref,
        )
        self.assertEqual(
            chart._js["showed"],  # pylint: disable=protected-access
            True,
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
