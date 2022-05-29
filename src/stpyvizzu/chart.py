"""
Streamlit integration of Vizzu.
"""
from streamlit.components.v1 import html

from pyvizzu.chart import Chart as PyvizzuChart

from stpyvizzu.animation import Snapshot
from stpyvizzu.template import DisplayTemplate, VIZZU


class Chart(PyvizzuChart):
    def __init__(self, vizzu=VIZZU, width="800px", height="480px"):
        self._classes["DisplayTemplate"] = DisplayTemplate
        self._classes["Snapshot"] = Snapshot

        super().__init__(vizzu, width, height)

        if not width.endswith("px") or not height.endswith("px"):
            raise ValueError("width and height can be px only")
        self._js["width"] = int(width[:-2]) + 10  # margin
        self._js["height"] = int(height[:-2]) + 10  # margin

    def show(self):
        assert not self._js["showed"], "cannot be used after chart displayed."
        self._js["showed"] = True
        script = "\n".join(self._js["calls"])
        html(
            f'<div id="{self._ids["init"]}"><script>{script}</script></div>',
            width=self._js["width"],
            height=self._js["height"],
        )
