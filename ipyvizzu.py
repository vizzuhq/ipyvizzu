"""
Jupyter notebook integration for vizzu.
"""

import json
import enum

from IPython.display import HTML, display_html


_HEAD = """
<div id="myVizzu" style="width:800px; height:480px;" />
<script type="module">
import Vizzu from 'https://cdn.jsdelivr.net/npm/vizzu@latest/dist/vizzu.min.js';

let chart = new Vizzu('myVizzu');
"""


class Data(dict):
    """
    Vizzu data with the required keys: records, series, dimensions or measures.
    """

    def add_record(self, record):
        self._add_value("records", record)

    def add_serie(self, name, values=None, **kwargs):
        self._add_named_value("series", name, values, **kwargs)

    def add_dimension(self, name, values=None, **kwargs):
        self._add_named_value("dimensions", name, values, **kwargs)

    def add_measure(self, name, values=None, **kwargs):
        self._add_named_value("measures", name, values, **kwargs)

    def _add_named_value(self, dest, name, values=None, **kwargs):
        value = {"name": name, **kwargs}

        if values is not None:
            value["values"] = values

        self._add_value(dest, value)

    def _add_value(self, dest, value):
        self.setdefault(dest, []).append(value)


class Chart:
    """
    Wrapper over vizzu Chart
    """

    def __init__(self, **data):
        self._animations = []

    def set_data(self, data: Data):
        """
        Set new data for animation.
        """

        self._animations.append({"data": data})

    def animate(self, **config):
        """
        Change the animation config.
        """

        self._animations.append(config)

    def show(self):
        """
        Generate a javascript code from the issued animations.
        """

        script = [_HEAD]

        for animation in self._animations:
            data = json.dumps(animation)
            script.append(f"chart.animate({data});")

        script.append("</script>")

        display_html("\n".join(script), raw=True)
