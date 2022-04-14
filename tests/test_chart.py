import unittest
import unittest.mock

from normalizer import Normalizer
from ipyvizzu import Chart, Data, Config, Snapshot, Style


def get_text(normalizer, javascript):
    display_out = []
    for block in javascript.call_args_list:
        display_out.append(block.args[0])
    return normalizer.normalize_id("\n".join(display_out)).strip()


class TestChartInit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.normalizer = Normalizer()

    def setUp(self):
        self.patch = unittest.mock.patch("ipyvizzu.chart.display_javascript")
        self.javascript = self.patch.start()

    def tearDown(self):
        self.patch.stop()

    def test_init(self):
        Chart()

        self.assertEqual(
            self.normalizer.normalize_id(
                self.javascript.call_args_list[0].args[0].strip().splitlines()[-1]
            ).strip(),
            "window.ipyvizzu = "
            + "new window.IpyVizzu("
            + "element, "
            + "id, "
            + '"https://cdn.jsdelivr.net/npm/vizzu@~0.4.0/dist/vizzu.min.js", '
            + '"800px", "480px");',
        )

    def test_init_vizzu(self):
        Chart(vizzu="https://cdn.jsdelivr.net/npm/vizzu@0.4.1/dist/vizzu.min.js")

        self.assertEqual(
            self.normalizer.normalize_id(
                self.javascript.call_args_list[0].args[0].strip().splitlines()[-1]
            ).strip(),
            "window.ipyvizzu = "
            + "new window.IpyVizzu("
            + "element, "
            + "id, "
            + '"https://cdn.jsdelivr.net/npm/vizzu@0.4.1/dist/vizzu.min.js", '
            + '"800px", "480px");',
        )

    def test_init_div(self):
        Chart(width="400px", height="240px")

        self.assertEqual(
            self.normalizer.normalize_id(
                self.javascript.call_args_list[0].args[0].strip().splitlines()[-1]
            ).strip(),
            "window.ipyvizzu = "
            + "new window.IpyVizzu("
            + "element, "
            + "id, "
            + '"https://cdn.jsdelivr.net/npm/vizzu@~0.4.0/dist/vizzu.min.js", '
            + '"400px", "240px");',
        )

    def test_init_display_not_valid(self):
        with self.assertRaises(ValueError):
            Chart(display="invalid")

    def test_init_display_begin(self):
        chart = Chart(display="begin")
        javascript = self.patch.start()

        chart.animate(Snapshot("abc1234"))
        self.assertEqual(
            get_text(self.normalizer, javascript),
            "window.ipyvizzu.animate(element, id, 'begin', true, "
            + "window.ipyvizzu.stored(element, id), "
            + "undefined);",
        )

    def test_init_display_actual(self):
        chart = Chart(display="actual")
        javascript = self.patch.start()

        chart.animate(Snapshot("abc1234"))
        self.assertEqual(
            get_text(self.normalizer, javascript),
            "window.ipyvizzu.animate(element, id, 'actual', true, "
            + "window.ipyvizzu.stored(element, id), "
            + "undefined);",
        )

    def test_init_display_end(self):
        chart = Chart(display="end")
        javascript = self.patch.start()

        chart.animate(Snapshot("abc1234"))
        self.assertEqual(
            get_text(self.normalizer, javascript),
            "window.ipyvizzu.animate(element, id, 'end', true, "
            + "window.ipyvizzu.stored(element, id), "
            + "undefined);",
        )


class TestChartMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.normalizer = Normalizer()

    def setUp(self):
        self.patch = unittest.mock.patch("ipyvizzu.chart.display_javascript")
        self.trash = self.patch.start()
        self.chart = Chart()
        self.javascript = self.patch.start()

    def tearDown(self):
        self.patch.stop()

    def test_animate_chart_target_has_to_be_passed(self):
        with self.assertRaises(ValueError):
            self.chart.animate()

    def test_animate_chart_target_has_to_be_passed_even_if_chart_anim_opts_passed(self):
        with self.assertRaises(ValueError):
            self.chart.animate(duration="500ms")

    def test_animate_one_chart_target(self):
        data = Data()
        data.add_record(["Rock", "Hard", 96])

        self.chart.animate(data)
        self.assertEqual(
            get_text(self.normalizer, self.javascript),
            "window.ipyvizzu.animate(element, id, 'actual', true, "
            + '{"data": {"records": [["Rock", "Hard", 96]]}}, '
            + "undefined);",
        )

    def test_animate_one_chart_target_with_chart_anim_opts(self):
        data = Data()
        data.add_record(["Rock", "Hard", 96])

        self.chart.animate(data, duration="500ms")
        self.assertEqual(
            get_text(self.normalizer, self.javascript),
            "window.ipyvizzu.animate(element, id, 'actual', true, "
            + '{"data": {"records": [["Rock", "Hard", 96]]}}, '
            + '{"duration": "500ms"});',
        )

    def test_animate_snapshot_chart_target(self):
        snapshot = Snapshot("abc1234")

        self.chart.animate(snapshot)
        self.assertEqual(
            get_text(self.normalizer, self.javascript),
            "window.ipyvizzu.animate(element, id, 'actual', true, "
            + "window.ipyvizzu.stored(element, id), "
            + "undefined);",
        )

    def test_animate_snapshot_chart_target_with_chart_anim_opts(self):
        snapshot = Snapshot("abc1234")

        self.chart.animate(snapshot, duration="500ms")
        self.assertEqual(
            get_text(self.normalizer, self.javascript),
            "window.ipyvizzu.animate(element, id, 'actual', true, "
            + "window.ipyvizzu.stored(element, id), "
            + '{"duration": "500ms"});',
        )

    def test_animate_more_chart_target(self):
        data = Data()
        data.add_record(["Rock", "Hard", 96])
        config = Config({"channels": {"label": {"attach": ["Popularity"]}}})
        style = Style({"title": {"backgroundColor": "#A0A0A0"}})

        self.chart.animate(data, config, style)
        self.assertEqual(
            get_text(self.normalizer, self.javascript),
            "window.ipyvizzu.animate(element, id, 'actual', true, "
            + '{"data": {"records": [["Rock", "Hard", 96]]}, '
            + '"config": {"channels": {"label": {"attach": ["Popularity"]}}}, '
            + '"style": {"title": {"backgroundColor": "#A0A0A0"}}}, '
            + "undefined);",
        )

    def test_animate_more_chart_target_with_chart_anim_opts(self):
        data = Data()
        data.add_record(["Rock", "Hard", 96])
        config = Config({"channels": {"label": {"attach": ["Popularity"]}}})
        style = Style({"title": {"backgroundColor": "#A0A0A0"}})

        self.chart.animate(data, config, style, duration="500ms")
        self.assertEqual(
            get_text(self.normalizer, self.javascript),
            "window.ipyvizzu.animate(element, id, 'actual', true, "
            + '{"data": {"records": [["Rock", "Hard", 96]]}, '
            + '"config": {"channels": {"label": {"attach": ["Popularity"]}}}, '
            + '"style": {"title": {"backgroundColor": "#A0A0A0"}}}, '
            + '{"duration": "500ms"});',
        )

    def test_animate_more_chart_target_with_conflict(self):
        data = Data()
        data.add_record(["Rock", "Hard", 96])
        config1 = Config({"channels": {"label": {"attach": ["Popularity"]}}})
        config2 = Config({"title": "Test"})
        style = Style({"title": {"backgroundColor": "#A0A0A0"}})

        with self.assertRaises(ValueError):
            self.chart.animate(data, config1, style, config2)

    def test_animate_more_chart_target_with_snapshot(self):
        data = Data()
        data.add_record(["Rock", "Hard", 96])
        config = Config({"channels": {"label": {"attach": ["Popularity"]}}})
        style = Style({"title": {"backgroundColor": "#A0A0A0"}})
        snapshot = Snapshot("abc1234")

        with self.assertRaises(NotImplementedError):
            self.chart.animate(data, config, style, snapshot)

    def test_animate_more_calls(self):
        data = Data()
        data.add_record(["Rock", "Hard", 96])
        config1 = Config({"channels": {"label": {"attach": ["Popularity"]}}})
        config2 = Config({"title": "Test"})
        style = Style({"title": {"backgroundColor": "#A0A0A0"}})

        self.chart.animate(data, config1, style)
        self.chart.animate(config2)
        self.assertEqual(
            get_text(self.normalizer, self.javascript),
            "window.ipyvizzu.animate(element, id, 'actual', true, "
            + '{"data": {"records": [["Rock", "Hard", 96]]}, '
            + '"config": {"channels": {"label": {"attach": ["Popularity"]}}}, '
            + '"style": {"title": {"backgroundColor": "#A0A0A0"}}}, '
            + "undefined);\n"
            + "window.ipyvizzu.animate(element, id, 'actual', true, "
            + '{"config": {"title": "Test"}}, '
            + "undefined);",
        )

    def test_animate_with_not_scroll_into_view_false(self):
        data = Data()
        data.add_record(["Rock", "Hard", 96])

        self.chart.scroll_into_view = False

        self.chart.animate(data)
        self.assertEqual(
            get_text(self.normalizer, self.javascript),
            "window.ipyvizzu.animate(element, id, 'actual', false, "
            + '{"data": {"records": [["Rock", "Hard", 96]]}}, '
            + "undefined);",
        )

    def test_feature(self):
        self.chart.feature("tooltip", True)
        self.assertEqual(
            get_text(self.normalizer, self.javascript),
            'window.ipyvizzu.feature(element, id, "tooltip", true);',
        )

    def test_store(self):
        self.chart.store()
        self.assertEqual(
            get_text(self.normalizer, self.javascript),
            "window.ipyvizzu.store(element, id, id);",
        )


class TestChartShow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.normalizer = Normalizer()

    def setUp(self):
        self.patch = unittest.mock.patch("ipyvizzu.chart.display_javascript")
        self.javascript = self.patch.start()

    def tearDown(self):
        self.patch.stop()

    def test_show(self):
        chart = Chart(display="manual")
        chart.animate(Snapshot("abc1234"))
        self.assertEqual(
            get_text(self.normalizer, self.javascript),
            "",
        )
        chart.show()
        self.assertEqual(
            self.normalizer.normalize_id(
                self.javascript.call_args_list[0].args[0].strip().splitlines()[-1]
            ).strip(),
            "window.ipyvizzu.animate(element, id, 'manual', true, "
            + "window.ipyvizzu.stored(element, id), "
            + "undefined);",
        )

    def test_show_if_display_is_not_manual(self):
        chart = Chart()
        chart.animate(Snapshot("abc1234"))
        with self.assertRaises(AssertionError):
            chart.show()

    def test_show_after_show(self):
        chart = Chart(display="manual")
        chart.animate(Snapshot("abc1234"))
        chart.show()
        with self.assertRaises(AssertionError):
            chart.show()

    def test_animate_after_show(self):
        chart = Chart(display="manual")
        chart.animate(Snapshot("abc1234"))
        chart.show()
        with self.assertRaises(AssertionError):
            chart.animate(Snapshot("abc1234"))

    def test_feature_after_show(self):
        chart = Chart(display="manual")
        chart.animate(Snapshot("abc1234"))
        chart.show()
        with self.assertRaises(AssertionError):
            chart.feature("tooltip", True)

    def test_store_after_show(self):
        chart = Chart(display="manual")
        chart.animate(Snapshot("abc1234"))
        chart.show()
        with self.assertRaises(AssertionError):
            chart.store()
