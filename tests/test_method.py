"""A module for testing the ipyvizzu.method module."""

import unittest

from tests import (
    Method,
    Animate,
    Feature,
    Store,
    EventOn,
    EventOff,
    Log,
    Config,
    Style,
    Snapshot,
    AnimationMerger,
    EventHandler,
    ChartProperty,
)


class TestMethod(unittest.TestCase):
    """A class for testing Method class and its derived classes."""

    def test_method(self) -> None:
        """
        A method for testing Method.dump method return value.

        Raises:
            AssertionError: If AttributeError is not occurred.
        """

        method = Method()
        with self.assertRaises(AttributeError):
            method.dump()

    def test_animate_with_anim_without_option(self) -> None:
        """
        A method for testing Animate class which is
        initialized with an Animation as `chart_target` and
        without `chart_anim_opts` parameters.
        It tests Animate.dump method return value.

        Raises:
            AssertionError: If the dumped value is not correct.
        """

        animation = Snapshot(name="abc1234")
        method = Animate(chart_target=animation)
        self.assertEqual(
            {
                "chart_target": '"abc1234"',
                "chart_anim_opts": "undefined",
            },
            method.dump(),
        )

    def test_animate_with_animmerger_without_option(self) -> None:
        """
        A method for testing Animate class which is
        initialized with an AnimationMerger as `chart_target` and
        without `chart_anim_opts` parameters.
        It tests Animate.dump method return value.

        Raises:
            AssertionError: If the dumped value is not correct.
        """

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
        """
        A method for testing Animate class which is
        initialized with an Animation as `chart_target` and
        with `chart_anim_opts` parameters.
        It tests Animate.dump method return value.

        Raises:
            AssertionError: If the dumped value is not correct.
        """

        animation = Snapshot(name="abc1234")
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
        """
        A method for testing Animate class which is
        initialized with an AnimationMerger as `chart_target` and
        with `chart_anim_opts` parameters.
        It tests Animate.dump method return value.

        Raises:
            AssertionError: If the dumped value is not correct.
        """

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
        """
        A method for testing Feature class which is
        initialized with `name` and `enabled` parameters.
        It tests Feature.dump method return value.

        Raises:
            AssertionError: If the dumped value is not correct.
        """

        method = Feature(name="tooltip", enabled=True)
        self.assertEqual({"name": "tooltip", "enabled": "true"}, method.dump())

    def test_store(self) -> None:
        """
        A method for testing Store class which is
        initialized with `snapshot_id` parameter.
        It tests Store.dump method return value.

        Raises:
            AssertionError: If the dumped value is not correct.
        """

        method = Store(snapshot_id="abc1234")
        self.assertEqual({"id": "abc1234"}, method.dump())

    def test_event_on(self) -> None:
        """
        A method for testing EventOn class which is
        initialized with `event_handler` parameter.
        It tests EventOn.dump method return value.

        Raises:
            AssertionError: If the dumped value is not correct.
        """

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
        """
        A method for testing EventOff class which is
        initialized with `event_handler` parameter.
        It tests EventOff.dump method return value.

        Raises:
            AssertionError: If the dumped value is not correct.
        """

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
        """
        A method for testing Log class which is
        initialized with `chart_property` parameter.
        It tests Log.dump method return value.

        Raises:
            AssertionError: If the dumped value is not correct.
        """

        method = Log(chart_property=ChartProperty.CONFIG)
        self.assertEqual(
            {
                "chart_property": "config",
            },
            method.dump(),
        )
