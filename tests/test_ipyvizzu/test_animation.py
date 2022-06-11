from tests.animation import (
    TestPlainAnimation,
    TestDataClassMethods,
    TestData,
    TestDataSchema,
    TestConfig,
    TestStyle,
    TestSnapshot,
    TestMerger,
)
from ipyvizzu import (
    PlainAnimation,
    Data,
    Config,
    Style,
    Snapshot,
    AnimationMerger,
)


class TestPlainAnimationPyvizzu(TestPlainAnimation):
    def get_plainanimation(self, **kwargs):
        return PlainAnimation(**kwargs)


class TestDataClassMethodsPyvizzu(TestDataClassMethods):
    def get_data(self):
        return Data


class TestDataPyvizzu(TestData):
    def get_data(self):
        return Data()


class TestDataSchemaPyvizzu(TestDataSchema):
    def get_data(self):
        return Data()


class TestConfigPyvizzu(TestConfig):
    def get_config(self, config):
        return Config(config)


class TestStyleIpyvizzu(TestStyle):
    def get_style(self, style):
        return Style(style)


class TestSnapshotIpyvizzu(TestSnapshot):
    def get_snapshot(self, snapshot):
        return Snapshot(snapshot)

    def test_snapshot(self):
        animation = super().test_snapshot()
        self.assertEqual("window.ipyvizzu.stored(element, 'abc1234')", animation.dump())


class TestMergerIpyvizzu(TestMerger):
    def get_animationmerger(self):
        return AnimationMerger()

    def get_data(self):
        return Data()

    def get_config(self, config):
        return Config(config)

    def get_style(self, style):
        return Style(style)

    def get_snapshot(self, snapshot):
        return Snapshot(snapshot)
