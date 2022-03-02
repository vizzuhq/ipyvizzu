"""
Jupyter notebook integration for Vizzu.
"""

import json
import abc
import typing
import uuid

from IPython.display import display_html


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

    @classmethod
    def from_json(cls, filename):
        with open(filename, "r", encoding="utf8") as file_desc:
            return cls(json.load(file_desc))

    def add_record(self, record):
        self._add_value("records", record)

    def add_series(self, name, values=None, **kwargs):
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


class Style(Animation):
    def __init__(self, data: typing.Optional[dict]):
        self._data = data

    def build(self):
        return {"style": self._data}


class Snapshot(Animation):
    def __init__(self, name: str):
        self._name = name

    def dump(self):
        return self._name

    def build(self):
        raise NotImplementedError("Snapshot cannot be merged with other Animations")


class AnimationMerger(dict, Animation):
    def build(self):
        return self

    def merge(self, animation: Animation):
        data = self._validate(animation)
        self.update(data)

    def _validate(self, animation):
        data = animation.build()
        common_keys = set(data).intersection(self)

        if common_keys:
            raise ValueError(f"Animation is already merged: {common_keys}")

        return data


class Method:
    @abc.abstractmethod
    def dump(self):
        pass


class Animate(Method):
    def __init__(self, data, option=None):
        self._data = data
        self._option = option

    def dump(self):
        data = self._data.dump()
        if self._option:
            data += ", " + PlainAnimation(self._option).dump()
        return f"chart.animate({data})"


class Feature(Method):
    def __init__(self, name, value):
        self._name = name
        self._value = value

    def dump(self):
        name = json.dumps(self._name)
        value = json.dumps(self._value)
        return f"chart.feature({name}, {value})"


class Store(Method):
    def __init__(self, snapshot_name: str):
        self._snaphot_name = snapshot_name

    def dump(self):
        return f"{self._snaphot_name} = chart.store();"


class Chart:
    """
    Wrapper over Vizzu Chart
    """

    VIZZU = "https://cdn.jsdelivr.net/npm/vizzu@latest/dist/vizzu.min.js"

    _INIT = """<div id="myVizzu_{id}" style="width:{div_width}; height:{div_height};"/>
        <script>
        let chart_{id} = import('{vizzu}').then(Vizzu => new Vizzu.default('myVizzu_{id}').initializing);
        </script>"""

    def __init__(self, vizzu=VIZZU, width="800px", height="480px"):
        self._id = uuid.uuid4().hex[:7]
        self._vizzu = vizzu
        self._div_width = width
        self._div_height = height

        display_html(
            self._INIT.format(
                id=self._id,
                vizzu=self._vizzu,
                div_width=self._div_width,
                div_height=self._div_height,
            ),
            raw=True,
        )

    _FEATURE = """<script>
        chart_{id} = chart_{id}.then(chart => {{ 
            {feature};
            return chart;
        }});
        </script>"""

    def feature(self, name, value):
        feature = Feature(name, value).dump()
        display_html(
            self._FEATURE.format(id=self._id, feature=feature),
            raw=True,
        )

    _ANIMATE = """<script>
        chart_{id} = chart_{id}.then(chart => {animation});
        </script>"""

    def animate(self, *animations: Animation, **options):
        """
        Show new animation.
        """
        if not animations:
            raise ValueError("No animation was set.")

        animation = self._merge_animations(animations)
        animation = Animate(animation, options).dump()

        display_html(
            self._ANIMATE.format(id=self._id, animation=animation),
            raw=True,
        )

    @staticmethod
    def _merge_animations(animations):
        if len(animations) == 1:
            return animations[0]

        merger = AnimationMerger()

        for animation in animations:
            merger.merge(animation)

        return merger

    _STORE = """<script>
        let {snapshot_name};
        chart_{id} = chart_{id}.then(chart => {{
            {snapshot_name} = chart.store();
            return chart;
        }});
        </script>"""

    def store(self) -> Snapshot:
        snapshot_name = "snapshot_" + uuid.uuid4().hex[:7]
        display_html(
            self._STORE.format(id=self._id, snapshot_name=snapshot_name),
            raw=True,
        )
        return Snapshot(snapshot_name)
