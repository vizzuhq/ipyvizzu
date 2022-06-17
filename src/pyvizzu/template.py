import enum


class DisplayTarget(str, enum.Enum):
    MANUAL = "manual"


class DisplayTemplate:

    PYVIZZUJS = "{pyvizzujs}"

    INIT = "window.pyvizzu = new window.PyVizzu(document.getElementById('{init_id}'), '{chart_id}', '{vizzu}', '{div_width}', '{div_height}');"  # pylint: disable=line-too-long

    ANIMATE = "window.pyvizzu.animate(null, '{chart_id}', '{display_target}', {scroll}, {chart_target}, {chart_anim_opts});"  # pylint: disable=line-too-long
    STORED = "window.pyvizzu.stored(null, '{id}')"

    FEATURE = "window.pyvizzu.feature(null, '{chart_id}', {name}, {enabled});"

    STORE = "window.pyvizzu.store(null, '{chart_id}', '{id}');"


VIZZU = "https://cdn.jsdelivr.net/npm/vizzu@~0.4.0/dist/vizzu.min.js"
