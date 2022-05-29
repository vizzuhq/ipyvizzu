import enum


class DisplayTarget(str, enum.Enum):
    MANUAL = "manual"


class DisplayTemplate:

    PYVIZZUJS = "{pyvizzujs}"

    INIT = "window.ipyvizzu = new window.IpyVizzu(document.getElementById('{init_id}'), '{chart_id}', '{vizzu}', '{div_width}', '{div_height}');"  # pylint: disable=line-too-long

    ANIMATE = "window.ipyvizzu.animate(null, '{chart_id}', '{display_target}', {scroll}, {chart_target}, {chart_anim_opts});"  # pylint: disable=line-too-long
    STORED = "window.ipyvizzu.stored(null, '{id}')"

    FEATURE = "window.ipyvizzu.feature(null, '{chart_id}', {name}, {enabled});"

    STORE = "window.ipyvizzu.store(null, '{chart_id}', '{id}');"


VIZZU = "https://cdn.jsdelivr.net/npm/vizzu@~0.4.0/dist/vizzu.min.js"
