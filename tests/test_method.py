# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import unittest

from ipyvizzu import (
    Animate,
    AnimationMerger,
    ChartProperty,
    Config,
    EventHandler,
    EventOff,
    EventOn,
    Feature,
    Log,
    Method,
    Snapshot,
    Store,
    Style,
)


class TestMethod(unittest.TestCase):
    def test_method(self) -> None:
        method = Method()
        with self.assertRaises(AttributeError):
            method.dump()

    def test_animate_with_anim_without_option(self) -> None:
        animation = Snapshot("abc1234")
        method = Animate(chart_target=animation)
        self.assertEqual(
            {
                "chart_target": '"abc1234"',
                "chart_anim_opts": "undefined",
            },
            method.dump(),
        )

    def test_animate_with_animmerger_without_option(self) -> None:
        config = Config({"title": "My first chart"})
        style = Style({"title": {"backgroundColor": "#A0A0A0"}})
        animation_merger = AnimationMerger()
        animation_merger.merge(config)
        animation_merger.merge(style)
        method = Animate(chart_target=animation_merger)
        self.assertEqual(
            {
                "chart_target": '{"config": '
                + '{"title": "My first chart"}, '
                + '"style": {"title": {"backgroundColor": "#A0A0A0"}}}',
                "chart_anim_opts": "undefined",
            },
            method.dump(),
        )

    def test_animate_with_anim_with_option(self) -> None:
        animation = Snapshot("abc1234")
        option = {"duration": 1, "easing": "linear"}
        method = Animate(chart_target=animation, chart_anim_opts=option)
        self.assertEqual(
            {
                "chart_target": '"abc1234"',
                "chart_anim_opts": '{"duration": 1, "easing": "linear"}',
            },
            method.dump(),
        )

    def test_animate_with_animmerger_with_option(self) -> None:
        config = Config({"title": "My first chart"})
        style = Style({"title": {"backgroundColor": "#A0A0A0"}})
        animation_merger = AnimationMerger()
        animation_merger.merge(config)
        animation_merger.merge(style)
        option = {"duration": 1, "easing": "linear"}
        method = Animate(chart_target=animation_merger, chart_anim_opts=option)
        self.assertEqual(
            {
                "chart_target": '{"config": '
                + '{"title": "My first chart"}, '
                + '"style": {"title": {"backgroundColor": "#A0A0A0"}}}',
                "chart_anim_opts": '{"duration": 1, "easing": "linear"}',
            },
            method.dump(),
        )

    def test_feature(self) -> None:
        method = Feature(name="tooltip", enabled=True)
        self.assertEqual({"name": "tooltip", "enabled": "true"}, method.dump())

    def test_store(self) -> None:
        method = Store(snapshot_id="abc1234")
        self.assertEqual({"id": "abc1234"}, method.dump())

    def test_event_on(self) -> None:
        event_handler = EventHandler(
            event="click", handler="alert(JSON.stringify(event.data));"
        )
        method = EventOn(event_handler=event_handler)
        method_dump = method.dump()
        self.assertEqual(
            {
                "id": method_dump["id"],
                "event": "click",
                "handler": "alert(JSON.stringify(event.data));",
            },
            method_dump,
        )

    def test_event_off(self) -> None:
        event_handler = EventHandler(
            event="click", handler="alert(JSON.stringify(event.data));"
        )
        method = EventOff(event_handler=event_handler)
        method_dump = method.dump()
        self.assertEqual(
            {
                "id": method_dump["id"],
                "event": "click",
            },
            method_dump,
        )

    def test_log(self) -> None:
        method = Log(chart_property=ChartProperty.CONFIG)
        self.assertEqual(
            {
                "chart_property": "config",
            },
            method.dump(),
        )
