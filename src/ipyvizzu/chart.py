"""
Jupyter notebook integration for Vizzu.
"""

import enum
import pkgutil
import uuid

from IPython.display import display_javascript
from IPython import get_ipython

from .animation import Animation, Snapshot, AnimationMerger
from .method import Animate, Feature, Store


class DisplayTarget(str, enum.Enum):

    BEGIN = "begin"
    END = "end"
    ACTUAL = "actual"


class DisplayTemplate:

    INIT = """
        {ipyvizzu_js}
        window.ipyvizzu = new window.IpyVizzu(element, "{chart_id}", "{vizzu}", "{div_width}", "{div_height}");
        """

    CLEAR_INHIBITSCROLL = "window.IpyVizzu.clearInhibitScroll();"
    ANIMATE = "window.ipyvizzu.animate(element, '{chart_id}', '{display_target}', {scroll}, {chart_target}, {chart_anim_opts});"  # pylint: disable=line-too-long
    STORE = "window.ipyvizzu.store('{chart_id}', '{id}');"
    FEATURE = "window.ipyvizzu.feature('{chart_id}', {name}, {enabled});"


class Chart:
    """
    Wrapper over Vizzu Chart
    """

    VIZZU = "https://cdn.jsdelivr.net/npm/vizzu@~0.4.0/dist/vizzu.min.js"

    def __init__(
        self,
        vizzu=VIZZU,
        width="800px",
        height="480px",
        display: DisplayTarget = DisplayTarget("actual"),
    ):
        self._chart_id = uuid.uuid4().hex[:7]
        self._vizzu = vizzu
        self._div_width = width
        self._div_height = height
        self._display_target = DisplayTarget(display)
        self._scroll_into_view = True

        self._register_events()

        ipyvizzu_js = pkgutil.get_data(__name__, "templates/ipyvizzu.js").decode(
            "utf-8"
        )
        display_javascript(
            DisplayTemplate.INIT.format(
                ipyvizzu_js=ipyvizzu_js,
                chart_id=self._chart_id,
                vizzu=self._vizzu,
                div_width=self._div_width,
                div_height=self._div_height,
            ),
            raw=True,
        )

    @staticmethod
    def _register_events():
        ipy = get_ipython()
        if ipy is not None:
            ipy.events.register("pre_run_cell", Chart._register_pre_run_cell)

    @staticmethod
    def _register_pre_run_cell():
        display_javascript(DisplayTemplate.CLEAR_INHIBITSCROLL, raw=True)

    @property
    def scroll_into_view(self):
        return self._scroll_into_view

    @scroll_into_view.setter
    def scroll_into_view(self, scroll_into_view):
        self._scroll_into_view = bool(scroll_into_view)

    def animate(self, *animations: Animation, **options):
        """
        Show new animation.
        """
        if not animations:
            raise ValueError("No animation was set.")

        animation = self._merge_animations(animations)
        animate = Animate(animation, options)

        display_javascript(
            DisplayTemplate.ANIMATE.format(
                display_target=self._display_target,
                chart_id=self._chart_id,
                scroll=str(self._scroll_into_view).lower(),
                **animate.dump(),
            ),
            raw=True,
        )

    @staticmethod
    def _merge_animations(animations):
        if len(animations) == 1:
            return animations[0]

        merger = AnimationMerger()
        for animation in animations:
            merger.merge(animation)

        return merger

    def feature(self, name, enabled):
        display_javascript(
            DisplayTemplate.FEATURE.format(
                chart_id=self._chart_id,
                **Feature(name, enabled).dump(),
            ),
            raw=True,
        )

    def store(self) -> Snapshot:
        snapshot_id = uuid.uuid4().hex[:7]
        display_javascript(
            DisplayTemplate.STORE.format(
                chart_id=self._chart_id, **Store(snapshot_id).dump()
            ),
            raw=True,
        )
        return Snapshot(snapshot_id)
