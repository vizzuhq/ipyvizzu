"""
Streamlit integration of Vizzu.
"""

import pkgutil
import uuid

from streamlit.components.v1 import html

from pyvizzu.chart import Chart as PyvizzuChart

from stpyvizzu.template import DisplayTarget, DisplayTemplate, VIZZU


class Chart(PyvizzuChart):
    def __init__(
        self,
        vizzu=VIZZU,
        width="800px",
        height="480px",
        display: DisplayTarget = DisplayTarget("manual"),
    ):
        super().__init__(display)

        pyvizzu_js = pkgutil.get_data("pyvizzu", "templates/pyvizzu.js").decode("utf-8")

        if not width.endswith("px") or not height.endswith("px"):
            raise ValueError("width and height can be px only")
        self._width = int(width[:-2]) + 10  # margin
        self._height = int(height[:-2]) + 10  # margin

        self._st_id = uuid.uuid4().hex[:7]

        self._display(
            DisplayTemplate.INIT.format(
                pyvizzu_js=pyvizzu_js,
                st_id=self._st_id,
                chart_id=self._chart_id,
                vizzu=vizzu,
                div_width=width,
                div_height=height,
            )
        )

    def _display(self, javascript):
        if self._display_target != DisplayTarget.MANUAL:
            raise ValueError("display can be manual only")

        super()._display(javascript)

    def show(self):
        script = "\n".join(self._calls)
        html(
            f'<div id="{self._st_id}"><script>{script}</script></div>',
            width=self._width,
            height=self._height,
        )
        self._showed = True
