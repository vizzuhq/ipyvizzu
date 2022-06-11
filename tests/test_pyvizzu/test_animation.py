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
from pyvizzu import (
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


class TestStylePyvizzu(TestStyle):
    def get_style(self, style):
        return Style(style)


class TestSnapshotPyvizzu(TestSnapshot):
    def get_snapshot(self, snapshot):
        return Snapshot(snapshot)


class TestMergerPyvizzu(TestMerger):
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
