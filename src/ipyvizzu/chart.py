"""
Jupyter notebook integration of Vizzu.
"""

import pkgutil

from IPython.display import display_javascript
from IPython import get_ipython

from pyvizzu.chart import Chart as PyvizzuChart

from ipyvizzu.template import DisplayTarget, DisplayTemplate, VIZZU


class Chart(PyvizzuChart):
    def __init__(
        self,
        vizzu=VIZZU,
        width="800px",
        height="480px",
        display: DisplayTarget = DisplayTarget("actual"),
    ):
        super().__init__(display)

        pyvizzu_js = pkgutil.get_data("pyvizzu", "templates/pyvizzu.js").decode("utf-8")

        if self._display_target != DisplayTarget.MANUAL:
            self._register_events()

        self._display(
            DisplayTemplate.INIT.format(
                pyvizzu_js=pyvizzu_js,
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

    def _display(self, javascript):
        if self._display_target != DisplayTarget.MANUAL:
            display_javascript(
                javascript,
                raw=True,
            )
        else:
            assert not self._showed, "cannot be used after chart.show()"
            self._calls.append(javascript)

    def show(self):
        assert (
            self._display_target == DisplayTarget.MANUAL
        ), f'chart.show() can be used with display="{DisplayTarget.MANUAL}" only'
        assert not self._showed, "cannot be used after chart.show()"
        display_javascript(
            "\n".join(self._calls),
            raw=True,
        )
        self._showed = True
