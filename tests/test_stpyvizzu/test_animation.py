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
from stpyvizzu import (
    PlainAnimation,
    Data,
    Config,
    Style,
    Snapshot,
    AnimationMerger,
)


class TestPlainAnimationStpyvizzu(TestPlainAnimation):
    def get_plainanimation(self, **kwargs):
        return PlainAnimation(**kwargs)


class TestDataClassMethodsStpyvizzu(TestDataClassMethods):
    def get_data(self):
        return Data


class TestDataStpyvizzu(TestData):
    def get_data(self):
        return Data()


class TestDataSchemaStpyvizzu(TestDataSchema):
    def get_data(self):
        return Data()


class TestConfigStpyvizzu(TestConfig):
    def get_config(self, config):
        return Config(config)


class TestStyleStpyvizzu(TestStyle):
    def get_style(self, style):
        return Style(style)


class TestSnapshotStpyvizzu(TestSnapshot):
    def get_snapshot(self, snapshot):
        return Snapshot(snapshot)


class TestMergerStpyvizzu(TestMerger):
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
