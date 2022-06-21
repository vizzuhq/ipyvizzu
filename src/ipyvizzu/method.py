"""
A module used to work
with ipyvizzu methods
"""

import json
from typing import Optional, Union

from ipyvizzu.animation import PlainAnimation, Animation, AnimationMerger


class Method:
    """
    A class used to store and return
    any data
    """

    # pylint: disable=too-few-public-methods

    _data = None

    def dump(self) -> dict:
        """
        A method used to return
        the stored data
        """

        return self._data


class Animate(Method):
    """
    A Method class used to create
    data based on chart target and chart anim parameters
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
    A Method class used to create
    data based on name and enabled parameters
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, name: str, enabled: bool):
        self._data = {"name": json.dumps(name), "enabled": json.dumps(enabled)}


class Store(Method):
    """
    A Method class used to create
    data based on snapshot id parameter
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, snapshot_id: str):
        self._data = {"id": snapshot_id}
