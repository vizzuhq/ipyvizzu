"""A module for working with Vizzu charts."""

from abc import ABC, abstractmethod
import pkgutil
import uuid
from typing import List, Optional, Union

from ipyvizzu.chartlib.animation import Animation, Snapshot, AnimationMerger
from ipyvizzu.chartlib.method import Animate, Feature, Store, EventOn, EventOff, Log
from ipyvizzu.chartlib.template import (
    ChartProperty,
    DisplayTemplate,
    DisplayTarget,
)
from ipyvizzu.chartlib.event import EventHandler


class ChartLib(ABC):
    """An abstract class for representing a wrapper over Vizzu chart."""

    @property
    @abstractmethod
    def display_target(self):
        """An abstract property for storing display_target."""

    @property
    @abstractmethod
    def display_location(self):
        """An abstract property for storing display_location."""

    @property
    def chart_id(self) -> str:
        """A property for storing chart_id."""

        return self._chart_id

    @chart_id.setter
    def chart_id(self, chart_id: str):
        self._chart_id = chart_id

    @property
    def scroll_into_view(self) -> bool:
        """A property for turning on/off scroll into view."""

        return self._scroll_into_view

    @scroll_into_view.setter
    def scroll_into_view(self, scroll_into_view: Optional[bool]):
        self._scroll_into_view = bool(scroll_into_view)

    def animate(self, *animations: Animation, **options: Optional[dict]) -> None:
        """A method for animating the chart."""

        if not animations:
            raise ValueError("No animation was set.")

        animation = self._merge_animations(animations)
        animate = Animate(animation, options)

        self._display(
            DisplayTemplate.ANIMATE.format(
                div=self.display_location,
                display_target=self.display_target.value,
                chart_id=self.chart_id,
                scroll=str(self._scroll_into_view).lower(),
                **animate.dump(),
            )
        )

    @staticmethod
    def _merge_animations(
        animations: List[Animation],
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
                div=self.display_location,
                chart_id=self.chart_id,
                **Feature(name, enabled).dump(),
            )
        )

    def store(self) -> Snapshot:
        """A method for saving and storing the actual state of the chart."""

        snapshot_id = uuid.uuid4().hex[:7]
        self._display(
            DisplayTemplate.STORE.format(
                div=self.display_location,
                chart_id=self.chart_id,
                **Store(snapshot_id).dump(),
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
                div=self.display_location,
                chart_id=self.chart_id,
                **EventOn(event_handler).dump(),
            )
        )
        return event_handler

    def off(self, event_handler: EventHandler) -> None:
        """A method for turning off an event handler."""

        self._display(
            DisplayTemplate.CLEAR_EVENT.format(
                div=self.display_location,
                chart_id=self.chart_id,
                **EventOff(event_handler).dump(),
            )
        )

    def log(self, chart_property: ChartProperty) -> None:
        """A method for printing chart properties to the browser console."""

        self._display(
            DisplayTemplate.LOG.format(
                div=self.display_location,
                chart_id=self.chart_id,
                **Log(chart_property).dump(),
            )
        )

    @abstractmethod
    def show(self):
        """An abstract method for displaying/returning the assembled javascript code."""

    @abstractmethod
    def _display(self, javascript: str) -> None:
        """An abstract method for displaying/assembling the javascript code."""

    def _display_ipyvizzujs(self) -> None:
        ipyvizzujs = pkgutil.get_data(__name__, "templates/ipyvizzu.js").decode("utf-8")
        self._display(DisplayTemplate.IPYVIZZUJS.format(ipyvizzujs=ipyvizzujs))


class ManualChart(ChartLib, ABC):
    """
    An abstract class for representing a wrapper over Vizzu chart
    that can only be displayed using chart.show().
    """

    def __init__(
        self,
        vizzu: Optional[str],
        width: Optional[str],
        height: Optional[str],
    ):
        self.chart_id = uuid.uuid4().hex[:7]

        self._calls = []
        self._showed = False

        self._scroll_into_view = False

        self._display_ipyvizzujs()

        self._init_id = uuid.uuid4().hex[:7]

        self._display(
            DisplayTemplate.INIT.format(
                div=self.display_location,
                chart_id=self._chart_id,
                vizzu=vizzu,
                div_width=width,
                div_height=height,
            )
        )

    @property
    def display_target(self) -> DisplayTarget:
        """A property for storing display_target."""

        return DisplayTarget.MANUAL

    @property
    @abstractmethod
    def display_location(self):
        """An abstract property for storing display_location."""

    @abstractmethod
    def show(self):
        """An abstract method for displaying/returning the assembled javascript code."""

    def _display(self, javascript: str) -> None:
        """A method for assembling the javascript code."""

        assert not self._showed, "cannot be used after chart displayed"
        self._calls.append(javascript)
