from pyvizzu.template import DisplayTarget as PyvizzuDisplayTarget
from pyvizzu.template import VIZZU as PyvizzuVIZZU


DisplayTarget = PyvizzuDisplayTarget


class DisplayTemplate:

    INIT = """
        {pyvizzu_js}
        window.ipyvizzu = new window.IpyVizzu(document.getElementById("{st_id}"), "{chart_id}", "{vizzu}", "{div_width}", "{div_height}");"""  # pylint: disable=line-too-long

    ANIMATE = "window.ipyvizzu.animate(false, '{chart_id}', '{display_target}', {scroll}, {chart_target}, {chart_anim_opts});"  # pylint: disable=line-too-long
    STORED = "window.ipyvizzu.stored(false, '{id}')"

    FEATURE = "window.ipyvizzu.feature(false, '{chart_id}', {name}, {enabled});"

    STORE = "window.ipyvizzu.store(false, '{chart_id}', '{id}');"


VIZZU = PyvizzuVIZZU
