from IPython.display import display_javascript
from IPython import get_ipython

import pkgutil
import uuid

from pyvizzu.chart import Chart as PyvizzuChart

from ipyvizzu.template import DisplayTarget, DisplayTemplate, VIZZU

"""
Jupyter notebook integration of Vizzu.
"""

class Chart(PyvizzuChart):

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

        try:
            pyvizzu_js = pkgutil.get_data(__name__, "templates/pyvizzu.js").decode(
                "utf-8"
            )
        except OSError:
            pyvizzu_js = pkgutil.get_data("pyvizzu", "templates/pyvizzu.js").decode(
                "utf-8"
            )

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

    def _display(self, javascript):
        if self._display_target != DisplayTarget.MANUAL:
            display_javascript(
                javascript,
                raw=True,
            )
        else:
            assert not self._showed, "cannot be used after chart.show()"
            self._calls.append(javascript)
