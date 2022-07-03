"""A module for working with Vizzu charts."""

from typing import Optional
import uuid

from streamlit.components.v1 import html

from ipyvizzu.chartlib.chart import ChartLib
from ipyvizzu.chartlib.template import VIZZU, DisplayTarget

from ipyvizzu.python.template import DisplayTemplate


class Chart(ChartLib):
    """A class for representing a wrapper over Vizzu chart in Streamlit environment."""

    def __init__(
        self,
        vizzu: Optional[str] = VIZZU,
        width: Optional[str] = "800px",
        height: Optional[str] = "480px",
    ):
        self.chart_id = uuid.uuid4().hex[:7]

        self._calls = []
        self._showed = False

        self._scroll_into_view = False

        self._display_ipyvizzujs()

        self._init_id = uuid.uuid4().hex[:7]

        if not width.endswith("px") or not height.endswith("px"):
            raise ValueError("width and height can be px only")

        self._canvas = {
            "width": int(width[:-2]) + 10,  # margin
            "height": int(height[:-2]) + 10,  # margin
        }

        self._display(
            self.display_template.INIT.format(
                init_id=self._init_id,
                chart_id=self._chart_id,
                vizzu=vizzu,
                div_width=width,
                div_height=height,
            )
        )

    @property
    def display_template(self) -> DisplayTemplate:
        """A property for storing display_template."""
        return DisplayTemplate

    @property
    def display_target(self) -> DisplayTarget:
        """A property for storing display_target."""
        return DisplayTarget.MANUAL

    @property
    def chart_id(self) -> str:
        """A property for storing chart_id."""
        return self._chart_id

    @chart_id.setter
    def chart_id(self, chart_id: str):
        self._chart_id = chart_id

    def show(self) -> None:
        """A method for displaying the assembled javascript code."""

        assert not self._showed, "cannot be used after chart displayed"
        self._showed = True
        script = "\n".join(self._calls)
        print(script)
        html(
            f'<div id="{self._init_id}"><script>{script}</script></div>',
            width=self._canvas["width"],
            height=self._canvas["height"],
        )

    def _display(self, javascript: str) -> None:
        """A method for assembling the javascript code."""

        assert not self._showed, "cannot be used after chart displayed"
        self._calls.append(javascript)
