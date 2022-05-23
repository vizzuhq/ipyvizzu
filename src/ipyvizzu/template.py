from pyvizzu.template import DisplayTarget as PyvizzuDisplayTarget
from pyvizzu.template import VIZZU as PyvizzuVIZZU


DisplayTarget = PyvizzuDisplayTarget


class DisplayTemplate:

    INIT = """
        {pyvizzu_js}
        window.ipyvizzu = new window.IpyVizzu(element, "{chart_id}", "{vizzu}", "{div_width}", "{div_height}");"""  # pylint: disable=line-too-long

    ANIMATE = "window.ipyvizzu.animate(element, '{chart_id}', '{display_target}', {scroll}, {chart_target}, {chart_anim_opts});"  # pylint: disable=line-too-long
    STORED = "window.ipyvizzu.stored(element, '{id}')"

    FEATURE = "window.ipyvizzu.feature(element, '{chart_id}', {name}, {enabled});"

    STORE = "window.ipyvizzu.store(element, '{chart_id}', '{id}');"

    CLEAR_INHIBITSCROLL = "window.IpyVizzu.clearInhibitScroll(element);"


VIZZU = PyvizzuVIZZU
