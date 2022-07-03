"""A module for working with Vizzu charts."""

from typing import Optional
import uuid

from IPython.display import display_javascript
from IPython import get_ipython

from ipyvizzu.chartlib.chart import ChartLib
from ipyvizzu.chartlib.template import VIZZU, DisplayTarget

from ipyvizzu.jupyter.template import DisplayTemplate


class Chart(ChartLib):
    """A class for representing a wrapper over Vizzu chart in Jupyter environment."""

    def __init__(
        self,
        vizzu: Optional[str] = VIZZU,
        width: Optional[str] = "800px",
        height: Optional[str] = "480px",
        display: Optional[DisplayTarget] = DisplayTarget.ACTUAL,
    ):
        self.chart_id = uuid.uuid4().hex[:7]

        self.display_target = display
        self._calls = []
        self._showed = False

        self._scroll_into_view = False

        self._display_ipyvizzujs()

        self._display(
            self.display_template.INIT.format(
                chart_id=self._chart_id,
                vizzu=vizzu,
                div_width=width,
                div_height=height,
            )
        )

        if self.display_target != DisplayTarget.MANUAL:
            self._register_events()

    def _register_events(self) -> None:
        ipy = get_ipython()
        if ipy is not None:
            ipy.events.register("pre_run_cell", self._register_pre_run_cell)

    def _register_pre_run_cell(self) -> None:
        display_javascript(self.display_template.CLEAR_INHIBITSCROLL, raw=True)

    @property
    def display_template(self) -> DisplayTemplate:
        """A property for storing display_template."""
        return DisplayTemplate

    @property
    def display_target(self) -> DisplayTarget:
        """A property for storing display_target."""
        return self._display_target

    @display_target.setter
    def display_target(self, display_target: Optional[DisplayTarget]):
        self._display_target = DisplayTarget(display_target)

    @property
    def chart_id(self) -> str:
        """A property for storing chart_id."""
        return self._chart_id

    @chart_id.setter
    def chart_id(self, chart_id: str):
        self._chart_id = chart_id

    def _repr_html_(self) -> str:
        assert (
            self.display_target == DisplayTarget.MANUAL
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
            self.display_target == DisplayTarget.MANUAL
        ), f'chart.show() can be used with display="{DisplayTarget.MANUAL.value}" only'
        assert not self._showed, "cannot be used after chart displayed"
        display_javascript(
            "\n".join(self._calls),
            raw=True,
        )
        self._showed = True

    def _display(self, javascript: str) -> None:
        """A method for displaying/assembling the javascript code."""
        if self.display_target != DisplayTarget.MANUAL:
            display_javascript(
                javascript,
                raw=True,
            )
        else:
            assert not self._showed, "cannot be used after chart displayed"
            self._calls.append(javascript)
