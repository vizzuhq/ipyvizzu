"""A module for storing the information needed to generate javascript code."""

from enum import Enum


VIZZU = "https://cdn.jsdelivr.net/npm/vizzu@~0.4.0/dist/vizzu.min.js"


class ChartProperty(Enum):
    """An enum class for storing chart properties."""

    CONFIG = "config"
    STYLE = "style"


class DisplayTarget(Enum):
    """
    An enum class for storing chart display options.
    BEGIN: Displays all animation steps after the constructor's cell.
    END: Displays all animation steps after the last running cell.
    ACTUAL: Displays the actual animation step after the currently running cell.
    MANUAL: Displays all animation steps after calling a show method.
    """

    BEGIN = "begin"
    END = "end"
    ACTUAL = "actual"
    MANUAL = "manual"


class DisplayTemplate:
    """A class for storing string templates to generate javascript snippets."""

    # pylint: disable=too-few-public-methods

    IPYVIZZUJS = "{ipyvizzujs}"

    INIT = (
        "window.ipyvizzu.createChart({div}, "
        + "'{chart_id}', '{vizzu}', '{div_width}', '{div_height}');"
    )

    ANIMATE = (
        "window.ipyvizzu.animate({div}, "
        + "'{chart_id}', '{display_target}', {scroll}, {chart_target}, {chart_anim_opts});"
    )

    FEATURE = "window.ipyvizzu.feature({div}, '{chart_id}', '{name}', {enabled});"

    STORE = "window.ipyvizzu.store({div}, '{chart_id}', '{id}');"

    SET_EVENT = (
        "window.ipyvizzu.setEvent({div}, "
        + "'{chart_id}', '{id}', '{event}', event => {{ {handler} }});"
    )

    CLEAR_EVENT = "window.ipyvizzu.clearEvent({div}, '{chart_id}', '{id}', '{event}');"

    LOG = "window.ipyvizzu.log({div}, '{chart_id}', '{chart_property}');"

    CLEAR_INHIBITSCROLL = (
        "if (window.IpyVizzu) { window.IpyVizzu.clearInhibitScroll(element); }"
    )
