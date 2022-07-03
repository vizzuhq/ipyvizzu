"""A module for working with Vizzu charts."""

from abc import ABC, abstractmethod
import uuid
from typing import List, Optional, Union

from ipyvizzu.chartlib.animation import Animation, Snapshot, AnimationMerger
from ipyvizzu.chartlib.method import Animate, Feature, Store, EventOn, EventOff, Log
from ipyvizzu.chartlib.template import ChartProperty
from ipyvizzu.chartlib.event import EventHandler


class ChartLib(ABC):
    """An abstract class for representing a wrapper over Vizzu chart."""

    @staticmethod
    @abstractmethod
    def display_template():
        """An abstract method for returning DisplayTemplate."""

    @property
    @abstractmethod
    def display_target(self):
        """An abstract property for storing display_target."""

    @property
    @abstractmethod
    def chart_id(self):
        """An abstract property for storing chart_id."""

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
            ChartLib.display_template.ANIMATE.format(
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
            ChartLib.display_template.FEATURE.format(
                chart_id=self.chart_id,
                **Feature(name, enabled).dump(),
            )
        )

    def store(self) -> Snapshot:
        """A method for saving and storing the actual state of the chart."""

        snapshot_id = uuid.uuid4().hex[:7]
        self._display(
            ChartLib.display_template.STORE.format(
                chart_id=self.chart_id, **Store(snapshot_id).dump()
            )
        )
        return Snapshot(snapshot_id)

    def on(  # pylint: disable=invalid-name
        self, event: str, handler: str
    ) -> EventHandler:
        """A method for creating and turning on an event handler."""

        event_handler = EventHandler(event, handler)
        self._display(
            ChartLib.display_template.SET_EVENT.format(
                chart_id=self.chart_id,
                **EventOn(event_handler).dump(),
            )
        )
        return event_handler

    def off(self, event_handler: EventHandler) -> None:
        """A method for turning off an event handler."""

        self._display(
            ChartLib.display_template.CLEAR_EVENT.format(
                chart_id=self.chart_id,
                **EventOff(event_handler).dump(),
            )
        )

    def log(self, chart_property: ChartProperty) -> None:
        """A method for printing chart properties to the browser console."""

        self._display(
            ChartLib.display_template.LOG.format(
                chart_id=self.chart_id, **Log(chart_property).dump()
            )
        )

    @abstractmethod
    def show(self) -> None:
        """An abstract method for displaying the assembled javascript code."""

    @abstractmethod
    def _display(self, javascript: str) -> None:
        """An abstract method for displaying/assembling the javascript code."""
