"""A module for storing the JavaScript templates."""

from enum import Enum

VIZZU_VERSION: str = "0.9"
"""A variable for storing the default version of the `vizzu` package."""

VIZZU: str = f"https://cdn.jsdelivr.net/npm/vizzu@{VIZZU_VERSION}/dist/vizzu.min.js"
"""A variable for storing the default url of the `vizzu` package."""


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

    IPYVIZZUJS: str = "{ipyvizzujs}"
    """ipyvizzu JavaScript class."""

    INIT: str = (
        "window.ipyvizzu.createChart(element, "
        + "'{chart_id}', '{vizzu}', '{div_width}', '{div_height}');"
    )
    """Call createChart JavaScript method."""

    CHANGE_ANALYTICS_TO: str = (
        "if (window.IpyVizzu) window.IpyVizzu.changeAnalyticsTo({analytics});"
    )
    """Call changeAnalyticsTo JavaScript method."""

    ANIMATE: str = (
        "window.ipyvizzu.animate(element, "
        + "'{chart_id}', '{anim_id}', '{display_target}', {scroll}, "
        + "lib => {{ return {chart_target} }}, {chart_anim_opts});"
    )
    """Call animate JavaScript method."""

    FEATURE: str = (
        "window.ipyvizzu.feature(element, '{chart_id}', '{name}', {enabled});"
    )
    """Call feature JavaScript method."""

    PLUGIN: str = (
        "window.ipyvizzu.plugin(element, "
        + "'{chart_id}', '{plugin}', {options}, '{name}', {enabled});"
    )
    """Call plugin JavaScript method."""

    STORE: str = "window.ipyvizzu.store(element, '{chart_id}', '{id}');"
    """Call store JavaScript method."""

    SET_EVENT: str = (
        "window.ipyvizzu.setEvent(element, "
        + "'{chart_id}', '{id}', '{event}', event => {{ {handler} }});"
    )
    """Call setEvent JavaScript method."""

    CLEAR_EVENT: str = (
        "window.ipyvizzu.clearEvent(element, '{chart_id}', '{id}', '{event}');"
    )
    """Call clearEvent JavaScript method."""

    LOG: str = "window.ipyvizzu.log(element, '{chart_id}', '{chart_property}');"
    """Call log JavaScript method."""

    CONTROL: str = "window.ipyvizzu.control(element, '{method}', {params});"
    """Call animation control JavaScript methods."""

    CLEAR_INHIBITSCROLL: str = (
        "if (window.IpyVizzu) { window.IpyVizzu.clearInhibitScroll(element); }"
    )
    """Call clearInhibitScroll JavaScript method if ipyvizzu JavaScript class exists."""
