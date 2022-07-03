"""A module for storing the information needed to generate javascript code."""


class DisplayTemplate:
    """A class for storing string templates to generate javascript snippets."""

    # pylint: disable=too-few-public-methods

    IPYVIZZUJS = "{ipyvizzujs}"

    INIT = (
        "window.ipyvizzu.createChart(element, "
        + "'{chart_id}', '{vizzu}', '{div_width}', '{div_height}');"
    )

    ANIMATE = (
        "window.ipyvizzu.animate(element, "
        + "'{chart_id}', '{display_target}', {scroll}, {chart_target}, {chart_anim_opts});"
    )

    FEATURE = "window.ipyvizzu.feature(element, '{chart_id}', '{name}', {enabled});"

    STORE = "window.ipyvizzu.store(element, '{chart_id}', '{id}');"

    SET_EVENT = (
        "window.ipyvizzu.setEvent(element, "
        + "'{chart_id}', '{id}', '{event}', event => {{ {handler} }});"
    )

    CLEAR_EVENT = (
        "window.ipyvizzu.clearEvent(element, '{chart_id}', '{id}', '{event}');"
    )

    LOG = "window.ipyvizzu.log(element, '{chart_id}', '{chart_property}');"

    CLEAR_INHIBITSCROLL = (
        "if (window.IpyVizzu) { window.IpyVizzu.clearInhibitScroll(element); }"
    )
