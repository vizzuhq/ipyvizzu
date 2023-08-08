# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import json
import unittest

from ipyvizzu import (
    Animation,
    AnimationMerger,
    Config,
    Data,
    Keyframe,
    PlainAnimation,
    Snapshot,
    Style,
)


class TestPlainAnimation(unittest.TestCase):
    def test_plainanimation(self) -> None:
        animation = PlainAnimation(geometry="circle")
        self.assertEqual({"geometry": "circle"}, animation.build())


class TestConfig(unittest.TestCase):
    def test_config(self) -> None:
        animation = Config({"color": {"set": ["Genres"]}})
        self.assertEqual({"config": {"color": {"set": ["Genres"]}}}, animation.build())

    def test_config_preset(self) -> None:
        animation = Config.column({"x": "foo", "y": "bar"})
        # instead of build() test with dump() because contains raw js
        self.assertEqual(
            "{\"config\": lib.presets.column({'x': 'foo', 'y': 'bar'})}",
            animation.dump(),
        )


class TestStyle(unittest.TestCase):
    def test_style(self) -> None:
        animation = Style({"title": {"backgroundColor": "#A0A0A0"}})
        self.assertEqual(
            {"style": {"title": {"backgroundColor": "#A0A0A0"}}}, animation.build()
        )

    def test_style_can_be_none(self) -> None:
        animation = Style(None)
        self.assertEqual({"style": None}, animation.build())


class TestKeyframe(unittest.TestCase):
    def test_animation_has_to_be_passed_even_if_options_passed(
        self,
    ) -> None:
        with self.assertRaises(ValueError):
            Keyframe(duration="500ms")

    def test_keyframe_cannot_be_passed(
        self,
    ) -> None:
        with self.assertRaises(ValueError):
            Keyframe(Keyframe(Style(None)))

    def test_animation_and_snapshot_cannot_be_passed(
        self,
    ) -> None:
        with self.assertRaises(ValueError):
            Keyframe(Keyframe(Style(None), Snapshot("abc123")))

    def test_animation_and_stored_animation_cannot_be_passed(
        self,
    ) -> None:
        with self.assertRaises(ValueError):
            Keyframe(Keyframe(Style(None), Animation("abc123")))

    def test_keyframe(self) -> None:
        animation = Keyframe(
            Data.filter(None), Style(None), Config({"title": "Keyframe"})
        )
        self.assertEqual(
            animation.build(),
            {
                "target": {
                    "config": {"title": "Keyframe"},
                    "data": {"filter": None},
                    "style": None,
                }
            },
        )

    def test_keyframe_with_snapshot(self) -> None:
        animation = Keyframe(Snapshot("abc123"))
        self.assertEqual(
            animation.build(),
            {
                "target": "abc123",
            },
        )

    def test_keyframe_with_stored_animation(self) -> None:
        animation = Keyframe(Animation("abc123"))
        self.assertEqual(
            animation.build(),
            {
                "target": "abc123",
            },
        )

    def test_keyframe_with_options(self) -> None:
        animation = Keyframe(
            Data.filter(None), Style(None), Config({"title": "Keyframe"}), duration=1
        )
        self.assertEqual(
            animation.build(),
            {
                "target": {
                    "config": {"title": "Keyframe"},
                    "data": {"filter": None},
                    "style": None,
                },
                "options": {"duration": 1},
            },
        )


class TestSnapshot(unittest.TestCase):
    def test_snapshot(self) -> None:
        animation = Snapshot("abc1234")
        self.assertEqual("abc1234", animation.build())

    def test_snapshot_dump(self) -> None:
        animation = Snapshot("abc1234")
        self.assertEqual('"abc1234"', animation.dump())


class TestAnimation(unittest.TestCase):
    def test_animation(self) -> None:
        animation = Animation("abc1234")
        self.assertEqual("abc1234", animation.build())

    def test_animation_dump(self) -> None:
        animation = Animation("abc1234")
        self.assertEqual('"abc1234"', animation.dump())


class TestMerger(unittest.TestCase):
    def setUp(self) -> None:
        self.merger = AnimationMerger()

        self.data = Data()
        self.data.add_record(["Rock", "Hard", 96])

        self.config = Config({"channels": {"label": {"attach": ["Popularity"]}}})

    def test_merge(self) -> None:
        self.merger.merge(self.data)
        self.merger.merge(self.config)
        self.merger.merge(Style({"title": {"backgroundColor": "#A0A0A0"}}))
        self.assertEqual(
            json.dumps(
                {
                    "data": {"records": [["Rock", "Hard", 96]]},
                    "config": {"channels": {"label": {"attach": ["Popularity"]}}},
                    "style": {"title": {"backgroundColor": "#A0A0A0"}},
                }
            ),
            self.merger.dump(),
        )

    def test_merge_none(self) -> None:
        self.merger.merge(self.config)
        self.merger.merge(Style(None))
        self.assertEqual(
            '{"config": {"channels": {"label": {"attach": ["Popularity"]}}}, "style": null}',
            self.merger.dump(),
        )

    def test_snapshot_can_not_be_merged(self) -> None:
        self.merger.merge(self.data)
        self.merger.merge(self.config)
        self.merger.merge(Style({"title": {"backgroundColor": "#A0A0A0"}}))
        self.assertRaises(ValueError, self.merger.merge, Snapshot("abc1234"))

    def test_stored_animation_can_not_be_merged(self) -> None:
        self.merger.merge(self.data)
        self.merger.merge(self.config)
        self.merger.merge(Style({"title": {"backgroundColor": "#A0A0A0"}}))
        self.assertRaises(ValueError, self.merger.merge, Animation("abc1234"))

    def test_only_different_animations_can_be_merged(self) -> None:
        self.merger.merge(self.data)
        self.merger.merge(self.config)
        self.merger.merge(Style({"title": {"backgroundColor": "#A0A0A0"}}))

        data = Data()
        data.add_record(["Pop", "Hard", 114])

        self.assertRaises(ValueError, self.merger.merge, data)
        self.assertRaises(ValueError, self.merger.merge, Config({"title": "Test"}))
        self.assertRaises(ValueError, self.merger.merge, Style(None))

    def test_merge_keyframes(self) -> None:
        self.merger.merge(Keyframe(Style(None)))
        self.merger.merge(Keyframe(Style(None), duration=0))
        self.merger.merge(Keyframe(Style(None)))

        self.assertEqual(
            self.merger.dump(),
            json.dumps(
                [
                    {"target": {"style": None}},
                    {"target": {"style": None}, "options": {"duration": 0}},
                    {"target": {"style": None}},
                ]
            ),
        )

    def test_keyframe_and_animation_can_not_be_merged(self) -> None:
        self.merger.merge(Keyframe(Style(None)))
        self.assertRaises(ValueError, self.merger.merge, self.data)

    def test_animation_and_keyframe_can_not_be_merged(self) -> None:
        self.merger.merge(self.data)
        self.assertRaises(ValueError, self.merger.merge, Keyframe(Style(None)))

    def test_merge_animations_keyframe(self) -> None:
        animations = tuple([Keyframe(Style(None))])
        merger = AnimationMerger.merge_animations(animations)

        self.assertEqual(
            merger.dump(),
            json.dumps(
                [
                    {"target": {"style": None}},
                ]
            ),
        )
