"""A module for working with template methods."""

import json
from typing import Optional, Union

from ipyvizzu.animation import PlainAnimation, Animation, AnimationMerger
from ipyvizzu.event import EventHandler
from ipyvizzu.template import ChartProperty


class Method:
    """A class for storing and dumping any kind of data."""

    # pylint: disable=too-few-public-methods

    _data: dict

    def dump(self) -> dict:
        """A method for returning the stored data."""

        return self._data


class Animate(Method):
    """
    A class for dumping Chart()-independent parameters to DisplayTemplate.ANIMATE template.
    It dumps chart_target and chart_anim_opts (or undefined) parameters.
    """

    # pylint: disable=too-few-public-methods

    def __init__(
        self,
        chart_target: Union[Animation, AnimationMerger],
        chart_anim_opts: Optional[dict] = None,
    ):
        self._data = {
            "chart_target": chart_target.dump(),
            "chart_anim_opts": PlainAnimation(chart_anim_opts).dump()
            if chart_anim_opts
            else "undefined",
        }


class Feature(Method):
    """
    A class for dumping Chart()-independent parameters to DisplayTemplate.FEATURE template.
    It dumps name and enabled parameters.
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, name: str, enabled: bool):
        self._data = {"name": name, "enabled": json.dumps(enabled)}


class Store(Method):
    """
    A class for dumping Chart()-independent parameters to DisplayTemplate.STORE template.
    It dumps snapshot_id (as id) parameter.
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, snapshot_id: str):
        self._data = {"id": snapshot_id}


class EventOn(Method):
    """
    A class for dumping Chart()-independent parameters to DisplayTemplate.SET_EVENT template.
    It dumps event_handler.id (as id), event_handler.event (as event) and
    event_handler.handler (as handler) parameters.
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, event_handler: EventHandler):
        self._data = {
            "id": event_handler.id,
            "event": event_handler.event,
            "handler": event_handler.handler,
        }


class EventOff(Method):
    """
    A class for dumping Chart()-independent parameters to DisplayTemplate.CLEAR_EVENT template.
    It dumps event_handler.id (as id) and event_handler.event (as event) parameters.
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, event_handler: EventHandler):
        self._data = {"id": event_handler.id, "event": event_handler.event}


class Log(Method):
    """
    A class for dumping Chart()-independent parameters to DisplayTemplate.LOG template.
    It dumps chart_property parameter.
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, chart_property: ChartProperty):
        self._data = {"chart_property": chart_property.value}
