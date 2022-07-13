"""A module for working with Vizzu charts."""

import pkgutil
import uuid
from typing import List, Optional, Union, Tuple

from IPython.display import display_javascript  # type: ignore
from IPython import get_ipython  # type: ignore

from ipyvizzu.animation import Animation, Snapshot, AnimationMerger
from ipyvizzu.method import Animate, Feature, Store, EventOn, EventOff, Log
from ipyvizzu.template import ChartProperty, DisplayTarget, DisplayTemplate
from ipyvizzu.event import EventHandler


class Chart:
    """A class for representing a wrapper over Vizzu chart."""

    VIZZU = "https://cdn.jsdelivr.net/npm/vizzu@~0.5.0/dist/vizzu.min.js"

    def __init__(
        self,
        vizzu: Optional[str] = VIZZU,
        width: Optional[str] = "800px",
        height: Optional[str] = "480px",
        display: Optional[Union[DisplayTarget, str]] = DisplayTarget.ACTUAL,
    ):
        self._chart_id = uuid.uuid4().hex[:7]

        self._display_target = DisplayTarget(display)
        self._calls: List[str] = []
        self._showed = False

        self._scroll_into_view = False

        ipyvizzurawjs = pkgutil.get_data(__name__, "templates/ipyvizzu.js")
        ipyvizzujs = ipyvizzurawjs.decode("utf-8")  # type: ignore
        self._display(DisplayTemplate.IPYVIZZUJS.format(ipyvizzujs=ipyvizzujs))

        self._display(
            DisplayTemplate.INIT.format(
                chart_id=self._chart_id,
                vizzu=vizzu,
                div_width=width,
                div_height=height,
            )
        )

        if self._display_target != DisplayTarget.MANUAL:
            self._register_events()

    @staticmethod
    def _register_events() -> None:
        ipy = get_ipython()
        if ipy is not None:
            ipy.events.register("pre_run_cell", Chart._register_pre_run_cell)

    @staticmethod
    def _register_pre_run_cell() -> None:
        display_javascript(DisplayTemplate.CLEAR_INHIBITSCROLL, raw=True)

    @property
    def scroll_into_view(self) -> bool:
        """A property for turning on/off scroll into view."""

        return self._scroll_into_view

    @scroll_into_view.setter
    def scroll_into_view(self, scroll_into_view: Optional[bool]):
        self._scroll_into_view = bool(scroll_into_view)

    def animate(
        self, *animations: Animation, **options: Optional[Union[str, int, float, dict]]
    ) -> None:
        """A method for animating the chart."""

        if not animations:
            raise ValueError("No animation was set.")

        animation = self._merge_animations(animations)
        animate = Animate(animation, options)

        self._display(
            DisplayTemplate.ANIMATE.format(
                display_target=self._display_target.value,
                chart_id=self._chart_id,
                scroll=str(self._scroll_into_view).lower(),
                **animate.dump(),
            )
        )

    @staticmethod
    def _merge_animations(
        animations: Tuple[Animation, ...],
    ) -> Union[Animation, AnimationMerger]:
        if len(animations) == 1:
            return animations[0]

        merger = AnimationMerger()
        for animation in animations:
            merger.merge(animation)

        return merger

    def feature(self, name: str, enabled: bool) -> None:
        """A method for turning on/off a feature of the chart."""

        self._display(
            DisplayTemplate.FEATURE.format(
                chart_id=self._chart_id,
                **Feature(name, enabled).dump(),
            )
        )

    def store(self) -> Snapshot:
        """A method for saving and storing the actual state of the chart."""

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
        """A method for creating and turning on an event handler."""

        event_handler = EventHandler(event, handler)
        self._display(
            DisplayTemplate.SET_EVENT.format(
                chart_id=self._chart_id,
                **EventOn(event_handler).dump(),
            )
        )
        return event_handler

    def off(self, event_handler: EventHandler) -> None:
        """A method for turning off an event handler."""

        self._display(
            DisplayTemplate.CLEAR_EVENT.format(
                chart_id=self._chart_id,
                **EventOff(event_handler).dump(),
            )
        )

    def log(self, chart_property: ChartProperty) -> None:
        """A method for printing chart properties to the browser console."""

        self._display(
            DisplayTemplate.LOG.format(
                chart_id=self._chart_id, **Log(chart_property).dump()
            )
        )

    def _repr_html_(self) -> str:
        assert (
            self._display_target == DisplayTarget.MANUAL
        ), f'chart._repr_html_() can be used with display="{DisplayTarget.MANUAL.value}" only'
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

    def show(self) -> None:
        """A method for displaying the assembled javascript code."""

        assert (
            self._display_target == DisplayTarget.MANUAL
        ), f'chart.show() can be used with display="{DisplayTarget.MANUAL.value}" only'
        assert not self._showed, "cannot be used after chart displayed"
        display_javascript(
            "\n".join(self._calls),
            raw=True,
        )
        self._showed = True

    def _display(self, javascript: str) -> None:
        if self._display_target != DisplayTarget.MANUAL:
            display_javascript(
                javascript,
                raw=True,
            )
        else:
            assert not self._showed, "cannot be used after chart displayed"
            self._calls.append(javascript)
