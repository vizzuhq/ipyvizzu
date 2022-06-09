"""
Jupyter Notebook integration of Vizzu.
"""
from IPython.display import display_javascript
from IPython import get_ipython

from pyvizzu.chart import Chart as PyvizzuChart

from ipyvizzu.animation import Snapshot
from ipyvizzu.template import DisplayTarget, DisplayTemplate, VIZZU


class Chart(PyvizzuChart):
    def __init__(
        self,
        vizzu=VIZZU,
        width="800px",
        height="480px",
        display: DisplayTarget = DisplayTarget("actual"),
    ):
        self._display_target = display

        super().__init__(vizzu, width, height)

        if self._display_target != DisplayTarget.MANUAL:
            self._register_events()

    @property
    def _display_target(self):
        return self.__display_target

    @_display_target.setter
    def _display_target(self, display):
        self.__display_target = DisplayTarget(display)

    @property
    def _display_template_class(self):
        return DisplayTemplate

    @property
    def _snapshot_class(self):
        return Snapshot

    def _register_events(self):
        ipy = get_ipython()
        if ipy is not None:
            ipy.events.register("pre_run_cell", self._register_pre_run_cell)

    def _register_pre_run_cell(self):
        display_javascript(self._display_template_class.CLEAR_INHIBITSCROLL, raw=True)

    def _display(self, javascript):
        if self._display_target != DisplayTarget.MANUAL:
            display_javascript(
                javascript,
                raw=True,
            )
        else:
            super()._display(javascript)

    def _repr_html_(self):
        assert (
            self._display_target == DisplayTarget.MANUAL
        ), f'chart._repr_html_() can be used with display="{DisplayTarget.MANUAL}" only'
        assert not self._js["showed"], "cannot be used after chart displayed."
        self._js["showed"] = True
        script = (
            self._js["calls"][0]
            + "\n"
            + "\n".join(self._js["calls"][1:]).replace(
                "element", f'document.getElementById("{self._ids["init"]}")'
            )
        )
        return f'<div id="{self._ids["init"]}"><script>{script}</script></div>'

    def show(self):
        assert (
            self._display_target == DisplayTarget.MANUAL
        ), f'chart.show() can be used with display="{DisplayTarget.MANUAL}" only'
        assert not self._js["showed"], "cannot be used after chart displayed."
        self._js["showed"] = True
        display_javascript(
            "\n".join(self._js["calls"]),
            raw=True,
        )
