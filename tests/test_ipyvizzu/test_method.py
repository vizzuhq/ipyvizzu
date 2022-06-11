from tests.method import TestMethod
from ipyvizzu import Method, Animate, Feature, Store, Snapshot


class TestMethodIpyvizzu(TestMethod):
    def get_method(self):
        return Method()

    def get_animate(self, chart_target, chart_anim_opts=None):
        return Animate(chart_target, chart_anim_opts)

    def get_snapshot(self, snapshot_id):
        return Snapshot(snapshot_id)

    def get_feature(self, name, enabled):
        return Feature(name, enabled)

    def get_store(self, snapshot_id):
        return Store(snapshot_id)

    def test_animate_without_option(self):
        animation = self.get_snapshot("abc1234")
        method = self.get_animate(animation)
        self.assertEqual(
            {
                "chart_target": "window.ipyvizzu.stored(element, 'abc1234')",
                "chart_anim_opts": "undefined",
            },
            method.dump(),
        )

    def test_animate_with_option(self):
        animation = self.get_snapshot("abc1234")
        option = {"duration": 1, "easing": "linear"}
        method = self.get_animate(animation, option)
        self.assertEqual(
            {
                "chart_target": "window.ipyvizzu.stored(element, 'abc1234')",
                "chart_anim_opts": '{"duration": 1, "easing": "linear"}',
            },
            method.dump(),
        )
