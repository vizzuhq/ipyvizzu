"""A module for working with template methods."""

import json
from typing import Optional

from ipyvizzu.animation import AbstractAnimation, PlainAnimation
from ipyvizzu.event import EventHandler
from ipyvizzu.template import ChartProperty


class Method:
    """A class for storing and dumping any kind of data."""

    # pylint: disable=too-few-public-methods

    _data: dict

    def dump(self) -> dict:
        """
        A method for returning the stored data.

        Returns:
            The stored data.
        """

        return self._data


class Animate(Method):
    """
    A class for dumping chart independent parameters to
    [DisplayTemplate.ANIMATE][ipyvizzu.template.DisplayTemplate] template.
    """

    # pylint: disable=too-few-public-methods

    def __init__(
        self,
        chart_target: AbstractAnimation,
        chart_anim_opts: Optional[dict] = None,
    ):
        """
        Animate constructor.

        It stores and dumps `chart_target` and `chart_anim_opts` parameters.

        Args:
            chart_target:
                AbstractAnimation inherited object such as
                [Data][ipyvizzu.animation.Data]
                [Config][ipyvizzu.animation.Config] or
                [Style][ipyvizzu.animation.Style].
            chart_anim_opts:
                Animation options' dictionary. If it is not set, it dumps `undefined`.
        """

        self._data = {
            "chart_target": chart_target.dump(),
            "chart_anim_opts": PlainAnimation(chart_anim_opts).dump()
            if chart_anim_opts
            else "undefined",
        }


class Feature(Method):
    """
    A class for dumping chart independent parameters to
    [DisplayTemplate.FEATURE][ipyvizzu.template.DisplayTemplate] template.
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, name: str, enabled: bool):
        """
        Feature constructor.

        It stores and dumps `name` and `enabled` parameters.

        Args:
            name: The name of a chart feature.
            enabled: The new state of a chart feature.
        """

        self._data = {"name": name, "enabled": json.dumps(enabled)}


class Store(Method):
    """
    A class for dumping chart independent parameters to
    [DisplayTemplate.STORE][ipyvizzu.template.DisplayTemplate] template.
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, snapshot_id: str):
        """
        Store constructor.

        It stores and dumps `snapshot_id` parameter.

        Args:
            snapshot_id: The id of snapshot object.
        """

        self._data = {"id": snapshot_id}


class EventOn(Method):
    """
    A class for dumping chart independent parameters to
    [DisplayTemplate.SET_EVENT][ipyvizzu.template.DisplayTemplate] template.
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, event_handler: EventHandler):
        """
        EventOn constructor.

        It stores and dumps the `id`, the `event` and the `handler` of the event handler object.

        Args:
            event_handler: An event handler object.
        """

        self._data = {
            "id": event_handler.id,
            "event": event_handler.event,
            "handler": event_handler.handler,
        }


class EventOff(Method):
    """
    A class for dumping chart independent parameters to
    [DisplayTemplate.CLEAR_EVENT][ipyvizzu.template.DisplayTemplate] template.
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, event_handler: EventHandler):
        """
        EventOff constructor.

        It stores and dumps the `id` and the `event` of the event handler object.

        Args:
            event_handler: An event handler object.
        """

        self._data = {"id": event_handler.id, "event": event_handler.event}


class Log(Method):
    """
    A class for dumping chart independent parameters to
    [DisplayTemplate.LOG][ipyvizzu.template.DisplayTemplate] template.
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, chart_property: ChartProperty):
        """
        Log constructor.

        It stores and dumps the value of the chart property object.

        Args:
            chart_property:
                A chart property such as
                [CONFIG][ipyvizzu.template.ChartProperty] and
                [STYLE][ipyvizzu.template.ChartProperty].
        """

        self._data = {"chart_property": chart_property.value}
