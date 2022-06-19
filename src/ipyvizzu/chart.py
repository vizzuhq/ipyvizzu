"""
Jupyter notebook integration for Vizzu.
"""

import pkgutil
import uuid

from IPython.display import display_javascript
from IPython import get_ipython

from ipyvizzu.animation import Animation, Snapshot, AnimationMerger
from ipyvizzu.method import Animate, Feature, Store
from ipyvizzu.template import DisplayTarget, DisplayTemplate
from ipyvizzu.event import EventHandler


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

        self._display_target = DisplayTarget(display)
        self._calls = []
        self._showed = False

        self._scroll_into_view = False

        if self._display_target != DisplayTarget.MANUAL:
            self._register_events()

        ipyvizzujs = pkgutil.get_data(__name__, "templates/ipyvizzu.js").decode("utf-8")
        self._display(DisplayTemplate.IPYVIZZUJS.format(ipyvizzujs=ipyvizzujs))

        self._display(
            DisplayTemplate.INIT.format(
                chart_id=self._chart_id,
                vizzu=vizzu,
                div_width=width,
                div_height=height,
            )
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

        self._display(
            DisplayTemplate.ANIMATE.format(
                display_target=self._display_target,
                chart_id=self._chart_id,
                scroll=str(self._scroll_into_view).lower(),
                **animate.dump(),
            )
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
        self._display(
            DisplayTemplate.FEATURE.format(
                chart_id=self._chart_id,
                **Feature(name, enabled).dump(),
            )
        )

    def store(self) -> Snapshot:
        snapshot_id = uuid.uuid4().hex[:7]
        self._display(
            DisplayTemplate.STORE.format(
                chart_id=self._chart_id, **Store(snapshot_id).dump()
            )
        )
        return Snapshot(snapshot_id)

    def on(  # pylint: disable=invalid-name
        self, event: str, handler: str
    ) -> EventHandler:
        """A method used to register the given handler for the given event"""
        event_handler = EventHandler(event, handler)
        self._display(
            DisplayTemplate.SET_EVENT.format(
                chart_id=self._chart_id,
                id=event_handler.id,
                event=event_handler.event,
                handler=event_handler.handler,
            )
        )
        return event_handler

    def off(self, event_handler: EventHandler) -> None:
        """A method used to unregister the given event handler"""
        self._display(
            DisplayTemplate.CLEAR_EVENT.format(
                chart_id=self._chart_id, id=event_handler.id, event=event_handler.event
            )
        )

    def _repr_html_(self):
        assert (
            self._display_target == DisplayTarget.MANUAL
        ), f'chart._repr_html_() can be used with display="{DisplayTarget.MANUAL}" only'
        assert not self._showed, "cannot be used after chart displayed."
        self._showed = True
        html_id = uuid.uuid4().hex[:7]
        script = (
            self._calls[0]
            + "\n"
            + "\n".join(self._calls[1:]).replace(
                "element", f'document.getElementById("{html_id}")'
            )
        )
        return f'<div id="{html_id}"><script>{script}</script></div>'

    def show(self):
        assert (
            self._display_target == DisplayTarget.MANUAL
        ), f'chart.show() can be used with display="{DisplayTarget.MANUAL}" only'
        assert not self._showed, "cannot be used after chart displayed"
        display_javascript(
            "\n".join(self._calls),
            raw=True,
        )
        self._showed = True

    def _display(self, javascript):
        if self._display_target != DisplayTarget.MANUAL:
            display_javascript(
                javascript,
                raw=True,
            )
        else:
            assert not self._showed, "cannot be used after chart.show()"
            self._calls.append(javascript)
