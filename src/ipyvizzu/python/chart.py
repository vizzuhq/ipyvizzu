"""A module for working with Vizzu charts."""

from typing import Optional

from ipyvizzu.chartlib.chart import ManualChart
from ipyvizzu.chartlib.template import VIZZU


class Chart(ManualChart):
    """A class for representing a wrapper over Vizzu chart in Python environment."""

    def __init__(
        self,
        vizzu: Optional[str] = VIZZU,
        width: Optional[str] = "800px",
        height: Optional[str] = "480px",
    ):
        super().__init__(vizzu=vizzu, width=width, height=height)

    @property
    def display_location(self) -> str:
        """A property for storing display_location."""

        return f"document.getElementById('{self._init_id}')"

    def show(self) -> str:
        """A method for displaying the assembled javascript code."""

        assert not self._showed, "cannot be used after chart displayed"
        self._showed = True
        script = "\n".join(self._calls)
        return f'<div id="{self._init_id}"><script>{script}</script></div>'
