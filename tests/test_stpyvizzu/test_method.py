from tests.method import TestMethod
from stpyvizzu import Method, Animate, Feature, Store, Snapshot


class TestMethodStpyvizzu(TestMethod):
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
