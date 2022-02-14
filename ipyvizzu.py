"""
Jupyter notebook integration for vizzu.
"""

import json
import abc
import typing

from IPython.display import display_html


_HEAD = """
<div id="myVizzu_{div_id}" style="width:800px; height:480px;" />
<script type="module">
import Vizzu from 'https://cdn.jsdelivr.net/npm/vizzu@latest/dist/vizzu.min.js';

let chart = new Vizzu('myVizzu_{div_id}');
chart.initializing.then( chart => {{
"""


class Animation:
    def dump(self):
        return json.dumps(self.build())

    @abc.abstractmethod
    def build(self) -> typing.Mapping:
        """
        Return a dict with native python values that can be converted into json.
        """


class PlainAnimation(dict, Animation):
    def build(self):
        return self


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

    def build(self):
        return {"data": self}


class Config(dict, Animation):
    def build(self):
        return {"config": self}


class AnimationMerger(dict, Animation):
    def build(self):
        return self

    def merge(self, animation: Animation):
        data = self._validate(animation)
        self.update(data)

    def _validate(self, animation):
        data = animation.build()
        common_keys = set(data).intersection(self)
        assert not common_keys, f"Animation is already merged: {common_keys}"
        return data


class Style(dict, Animation):
    def build(self):
        return {"style": self}


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

    def __init__(self):
        self._calls = []

    def feature(self, name, value):
        self._calls.append(Feature(name, value))

    def animate(self, *animations: Animation, **config):
        """
        Register new animation.
        """
        if animations and config:
            raise ValueError(
                "`animations` parameter cannot be updated with keyword arguments."
            )

        if not animations and not config:
            raise ValueError("No animation was set.")

        if config:
            animation = PlainAnimation(config)

        else:
            animation = self._merge_animations(animations)

        self._calls.append(Animate(animation))

    def _merge_animations(self, animations):
        merger = AnimationMerger()

        for animation in animations:
            merger.merge(animation)

        return merger

    def show(self):
        """
        Generate a javascript code from the issued animations.
        """

        script = [_HEAD.format(div_id=id(self))]
        script.extend(call.dump() for call in self._calls)
        script.append("} );")
        script.append("</script>")
        display_html("\n".join(script), raw=True)
