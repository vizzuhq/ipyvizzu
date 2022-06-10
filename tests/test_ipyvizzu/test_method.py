import unittest

from ipyvizzu import Method, Animate, Feature, Store, Snapshot


class TestMethod(unittest.TestCase):
    def test_method(self):
        method = Method()
        self.assertEqual(None, method.dump())

    def test_animate_without_option(self):
        animation = Snapshot("abc1234")
        method = Animate(animation)
        self.assertEqual(
            {
                "chart_target": "window.ipyvizzu.stored(element, 'abc1234')",
                "chart_anim_opts": "undefined",
            },
            method.dump(),
        )

    def test_animate_with_option(self):
        animation = Snapshot("abc1234")
        option = {"duration": 1, "easing": "linear"}
        method = Animate(animation, option)
        self.assertEqual(
            {
                "chart_target": "window.ipyvizzu.stored(element, 'abc1234')",
                "chart_anim_opts": '{"duration": 1, "easing": "linear"}',
            },
            method.dump(),
        )

    def test_feature(self):
        method = Feature("tooltip", True)
        self.assertEqual({"name": '"tooltip"', "enabled": "true"}, method.dump())

    def test_store(self):
        method = Store("abc1234")
        self.assertEqual({"id": "abc1234"}, method.dump())
