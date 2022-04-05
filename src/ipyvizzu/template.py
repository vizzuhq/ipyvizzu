import enum


class DisplayTarget(str, enum.Enum):

    BEGIN = "begin"
    END = "end"
    ACTUAL = "actual"


class DisplayTemplate:

    INIT = """
        {ipyvizzu_js}
        window.ipyvizzu = new window.IpyVizzu(element, "{chart_id}", "{vizzu}", "{div_width}", "{div_height}");
        """

    ANIMATE = "window.ipyvizzu.animate(element, '{chart_id}', '{display_target}', {scroll}, {chart_target}, {chart_anim_opts});"  # pylint: disable=line-too-long
    STORE = "window.ipyvizzu.store('{chart_id}', '{id}');"
    STORED = "window.ipyvizzu.stored('{id}')"
    FEATURE = "window.ipyvizzu.feature('{chart_id}', {name}, {enabled});"

    CLEAR_INHIBITSCROLL = "window.IpyVizzu.clearInhibitScroll();"
