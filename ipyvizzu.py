"""
Jupyter notebook integration for vizzu.
"""

import json

from IPython.display import HTML, display_html


_HEAD = """
<div id="myVizzu_{div_id}" style="width:800px; height:480px;" />
<script type="module">
import Vizzu from 'https://cdn.jsdelivr.net/npm/vizzu@latest/dist/vizzu.min.js';

let chart = new Vizzu('myVizzu_{div_id}');
chart.initializing.then( chart => {{
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


class Method:
    def dump(self):
        raise NotImplementedError


class Animate(Method):
    def __init__(self, data):
        self._data = data

    def dump(self):
        data = json.dumps(self._data)
        return f"chart.animate({data});"



class Feature(Method):
    def __init__(self, name, value):
        self._name = name
        self._value = value

    def dump(self):
        name = json.dumps(self._name)
        value = json.dumps(self._value)
        return f"chart.feature({name}, {value});"


class Chart:
    """
    Wrapper over vizzu Chart
    """

    def __init__(self, **data):
        self._calls = []

    def set_data(self, data: Data):
        """
        Set new data for animation.
        """

        self._calls.append(Animate({"data": data}))

    def set_config(self, config):
        """
        Set new configuration.
        """

        self._calls.append(Animate({"config": config}))

    def set_feature(self, name, value):
        self._calls.append(Feature(name, value))

    def animate(self, **config):
        """
        Change the animation config.
        """

        self._calls.append(Animate(config))

    def show(self):
        """
        Generate a javascript code from the issued animations.
        """

        script = [_HEAD.format(div_id=id(self))]
        script.extend(call.dump() for call in self._calls)
        script.append("} );")
        script.append("</script>")

        display_html("\n".join(script), raw=True)
