"""A module for working with template methods."""

import json
from typing import Optional

from ipyvizzu.animation import AbstractAnimation, PlainAnimation
from ipyvizzu.event import EventHandler
from ipyvizzu.json import RawJavaScriptEncoder
from ipyvizzu.template import ChartProperty, VIZZU_VERSION


class Method:
    """
    A class for dumping chart independent parameters to
    [DisplayTemplate.STORE][ipyvizzu.template.DisplayTemplate] template.
    """

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
    It stores and dumps `chart_target` and `chart_anim_opts` parameters.
    """

    # pylint: disable=too-few-public-methods

    def __init__(
        self,
        chart_target: AbstractAnimation,
        chart_anim_opts: Optional[dict] = None,
    ):
        """
        Animate constructor.

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
    It stores and dumps `name` and `enabled` parameters.
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, name: str, enabled: bool):
        """
        Feature constructor.

        Args:
            name: The name of a chart feature.
            enabled: The new state of a chart feature.
        """

        self._data = {"name": name, "enabled": json.dumps(enabled)}


class Plugin(Method):
    """
    It stores and dumps `plugin`, `options` and `name` parameters.
    """

    def __init__(self, plugin: str, options: Optional[dict], name: str, enabled: bool):
        """
        Plugin constructor.

        Args:
            plugin: The package name or the url of the plugin.
            options: The plugin constructor options.
            name: The name of the plugin (default `default`).
            enabled: The state of the plugin (default `True`).
        """

        self._data = {
            "plugin": Plugin.resolve_url(plugin),
            "options": {}
            if options is None
            else json.dumps(options, cls=RawJavaScriptEncoder),
            "name": name,
            "enabled": json.dumps(enabled),
        }

    @staticmethod
    def resolve_url(plugin: str) -> str:
        """
        A static method for resolving the url of the plugin.

        Args:
            plugin: The package name or the url of the plugin.

        Returns:
            The url of the plugin.
        """

        if Plugin._is_url(plugin):
            return plugin
        return Plugin._get_url(plugin)

    @staticmethod
    def _is_url(plugin: str) -> bool:
        return "/" in plugin

    @staticmethod
    def _get_url(plugin: str) -> str:
        jsdelivr = "https://cdn.jsdelivr.net/npm/@vizzu"
        tag = f"vizzu-{VIZZU_VERSION}"
        return f"{jsdelivr}/{plugin}@{tag}/dist/mjs/index.min.js"


class Store(Method):
    """
    It stores and dumps `snapshot_id` parameter.
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, snapshot_id: str):
        """
        Store constructor.

        Args:
            snapshot_id: The id of snapshot object.
        """

        self._data = {"id": snapshot_id}


class EventOn(Method):
    """
    It stores and dumps the `id`, the `event` and the `handler` of the event handler object.
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, event_handler: EventHandler):
        """
        EventOn constructor.

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
    It stores and dumps the `id` and the `event` of the event handler object.
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, event_handler: EventHandler):
        """
        EventOff constructor.

        Args:
            event_handler: An event handler object.
        """

        self._data = {"id": event_handler.id, "event": event_handler.event}


class Log(Method):
    """
    It stores and dumps the value of the chart property object.
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, chart_property: ChartProperty):
        """
        Log constructor.

        Args:
            chart_property:
                A chart property such as
                [CONFIG][ipyvizzu.template.ChartProperty] and
                [STYLE][ipyvizzu.template.ChartProperty].
        """

        self._data = {"chart_property": chart_property.value}
