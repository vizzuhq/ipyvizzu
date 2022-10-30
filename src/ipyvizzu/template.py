"""A module for storing the JavaScript templates."""

from enum import Enum


class ChartProperty(Enum):
    """An enum class for storing chart properties."""

    CONFIG = "config"
    """An enum key-value for storing config chart property."""

    STYLE = "style"
    """An enum key-value for storing style chart property."""


class DisplayTarget(Enum):
    """An enum class for storing chart display options."""

    BEGIN = "begin"
    """Display all animation steps after the constructor's cell."""

    END = "end"
    """Display all animation steps after the last running cell."""

    ACTUAL = "actual"
    """Display the actual animation step after the currently running cell."""

    MANUAL = "manual"
    """Display all animation steps after calling a show method."""


class DisplayTemplate:
    """A class for storing JavaScript snippet templates."""

    # pylint: disable=too-few-public-methods

    IPYVIZZUJS = "{ipyvizzujs}"
    """`str`: ipyvizzu JavaScript class."""

    INIT = (
        "window.ipyvizzu.createChart(element, "
        + "'{chart_id}', '{vizzu}', '{div_width}', '{div_height}');"
    )
    """`str`: Call createChart JavaScript method."""

    ANIMATE = (
        "window.ipyvizzu.animate(element, "
        + "'{chart_id}', '{display_target}', {scroll}, "
        + "lib => {{ return {chart_target} }}, {chart_anim_opts});"
    )
    """`str`: Call animate JavaScript method."""

    FEATURE = "window.ipyvizzu.feature(element, '{chart_id}', '{name}', {enabled});"
    """`str`: Call feature JavaScript method."""

    STORE = "window.ipyvizzu.store(element, '{chart_id}', '{id}');"
    """`str`: Call store JavaScript method."""

    SET_EVENT = (
        "window.ipyvizzu.setEvent(element, "
        + "'{chart_id}', '{id}', '{event}', event => {{ {handler} }});"
    )
    """`str`: Call setEvent JavaScript method."""

    CLEAR_EVENT = (
        "window.ipyvizzu.clearEvent(element, '{chart_id}', '{id}', '{event}');"
    )
    """`str`: Call clearEvent JavaScript method."""

    LOG = "window.ipyvizzu.log(element, '{chart_id}', '{chart_property}');"
    """`str`: Call log JavaScript method."""

    CLEAR_INHIBITSCROLL = (
        "if (window.IpyVizzu) { window.IpyVizzu.clearInhibitScroll(element); }"
    )
    """`str`: Call clearInhibitScroll JavaScript method if ipyvizzu JavaScript class exists."""
