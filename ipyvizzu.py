"""
Jupyter notebook integration for vizzu.
"""

import json
import abc
import typing

from IPython.display import HTML, display_html


_HEAD = """
<div id="myVizzu_{div_id}" style="width:800px; height:480px;" />
<script type="module">
import Vizzu from 'https://cdn.jsdelivr.net/npm/vizzu@latest/dist/vizzu.min.js';

let chart = new Vizzu('myVizzu_{div_id}');
chart.initializing.then( chart => {{
"""


class Animation:
    @abc.abstractmethod
    def dump():
        pass


class PlainAnimation(dict, Animation):
    def dump(self):
        return json.dumps(self)


class Data(dict, Animation):
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

    def dump(self):
        return json.dumps({"data": self})


class Config(dict, Animation):
    def dump(self):
        return json.dumps({"config": self})


class Style(dict, Animation):
    def dump(self):
        return json.dumps({"style": self})


class Method:
    @abc.abstractmethod
    def dump(self):
        pass


class Animate(Method):
    def __init__(self, data):
        self._data = data

    def dump(self):
        data = self._data.dump()
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

    def feature(self, name, value):
        self._calls.append(Feature(name, value))

    def animate(self, *animations: typing.Optional[Animation], **options):
        """
        Register new animation.
        """

        if animations and options:
            raise ValueError(
                "`animations` and `options` cannot be used together."
            )

        if options:
            self._calls.append(Animate(PlainAnimation(options)))
        else:
            if len(animations) == 1:
                self._calls.append(Animate(*animations))
            else:
                anim = {}
                for item in animations:
                    anim = self._merge_anims(anim, json.loads(item.dump()))
                self._calls.append(Animate(PlainAnimation(anim)))

    def _merge_anims(self, a, b, path=None):
        if path is None: path = []
        for key in b:
            if key in a:
                if isinstance(a[key], dict) and isinstance(b[key], dict):
                    self._merge_anims(a[key], b[key], path + [str(key)])
                elif a[key] == b[key]:
                    pass
                else:
                    raise ValueError(f"Conflict at `{'.'.join(path + [str(key)])}`.")
            else:
                a[key] = b[key]
        return a

    def show(self):
        """
        Generate a javascript code from the issued animations.
        """

        script = [_HEAD.format(div_id=id(self))]
        script.extend(call.dump() for call in self._calls)
        script.append("} );")
        script.append("</script>")
        display_html("\n".join(script).replace('"null"', "null"), raw=True)
