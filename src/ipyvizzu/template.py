import enum


class DisplayTarget(str, enum.Enum):

    BEGIN = "begin"
    END = "end"
    ACTUAL = "actual"
    MANUAL = "manual"


class DisplayTemplate:

    INIT = """
        {ipyvizzu_js}
        window.ipyvizzu = new window.IpyVizzu(element, "{chart_id}", "{vizzu}", "{div_width}", "{div_height}");"""  # pylint: disable=line-too-long

    ANIMATE = "window.ipyvizzu.animate(element, '{chart_id}', '{display_target}', {scroll}, {chart_target}, {chart_anim_opts});"  # pylint: disable=line-too-long
    STORED = "window.ipyvizzu.stored(element, '{id}')"

    FEATURE = "window.ipyvizzu.feature(element, '{chart_id}', {name}, {enabled});"

    STORE = "window.ipyvizzu.store(element, '{chart_id}', '{id}');"

    CLEAR_INHIBITSCROLL = "window.IpyVizzu.clearInhibitScroll(element);"
