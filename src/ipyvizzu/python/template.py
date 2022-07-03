"""A module for storing the information needed to generate javascript code."""


class DisplayTemplate:
    """A class for storing string templates to generate javascript snippets."""

    # pylint: disable=too-few-public-methods

    IPYVIZZUJS = "{ipyvizzujs}"

    INIT = (
        "window.ipyvizzu.createChart(document.getElementById('{init_id}'), "
        + "'{chart_id}', '{vizzu}', '{div_width}', '{div_height}');"
    )

    ANIMATE = (
        "window.ipyvizzu.animate(null, "
        + "'{chart_id}', '{display_target}', {scroll}, {chart_target}, {chart_anim_opts});"
    )

    FEATURE = "window.ipyvizzu.feature(null, '{chart_id}', '{name}', {enabled});"

    STORE = "window.ipyvizzu.store(null, '{chart_id}', '{id}');"

    SET_EVENT = (
        "window.ipyvizzu.setEvent(null, "
        + "'{chart_id}', '{id}', '{event}', event => {{ {handler} }});"
    )

    CLEAR_EVENT = "window.ipyvizzu.clearEvent(null, '{chart_id}', '{id}', '{event}');"

    LOG = "window.ipyvizzu.log(null, '{chart_id}', '{chart_property}');"
