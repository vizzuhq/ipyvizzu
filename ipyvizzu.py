"""
Jupyter notebook integration for Vizzu.
"""

import json
import abc
import typing
import uuid
import enum
from inspect import cleandoc

from IPython.display import display_html


class DisplayTarget(str, enum.Enum):

    BEGIN = "begin"
    END = "end"
    ACTUAL = "actual"


class DisplayTemplate:

    DISPLAY = """<script id="myVizzu_{display_id}">
            document.getElementById("myVizzu_{display_id}").parentNode.style.padding = "0px";
        </script>
        {html}"""

    INIT = """<div id="myVizzu_{id}" style="width:{div_width}; height:{div_height};"/>
        <script>
            let myVizzu_{id} = document.getElementById("myVizzu_{id}")
            let chart_{id} = import("{vizzu}").then(Vizzu => new Vizzu.default("myVizzu_{id}").initializing);
        </script>"""

    ANIMATE = {
        DisplayTarget.BEGIN: """<script>
            chart_{id} = chart_{id}.then(chart => {{
                return {animation}
            }});
        </script>""",
        DisplayTarget.ACTUAL: """<div id="myVizzu_{new_id}"/>
        <script>
            chart_{id} = chart_{id}.then(chart => {{
                document.getElementById("myVizzu_{new_id}").appendChild(myVizzu_{id});
                return {animation}
            }});
        </script>""",
        DisplayTarget.END: """<div id="myVizzu_{new_id}"/>
        <script>
            document.getElementById("myVizzu_{new_id}").appendChild(myVizzu_{id});
            chart_{id} = chart_{id}.then(chart => {{
                return {animation}
            }});
        </script>""",
    }

    STORE = """<script>
            let {snapshot};
            chart_{id} = chart_{id}.then(chart => {{
                {snapshot} = chart.store();
                return chart;
            }});
        </script>"""

    FEATURE = """<script>
            chart_{id} = chart_{id}.then(chart => {{
                {feature};
                return chart;
            }});
        </script>"""


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

    VIZZU = "https://cdn.jsdelivr.net/npm/vizzu@~0.4.0/dist/vizzu.min.js"

    def __init__(
        self,
        vizzu=VIZZU,
        width="800px",
        height="480px",
        display: DisplayTarget = DisplayTarget("actual"),
    ):
        self._id = uuid.uuid4().hex[:7]
        self._vizzu = vizzu
        self._div_width = width
        self._div_height = height
        self._display_target = DisplayTarget(display)

        self._display(
            DisplayTemplate.INIT.format(
                id=self._id,
                vizzu=self._vizzu,
                div_width=self._div_width,
                div_height=self._div_height,
            )
        )

    def feature(self, name, value):
        feature = Feature(name, value).dump()
        self._display(DisplayTemplate.FEATURE.format(id=self._id, feature=feature))

    def animate(self, *animations: Animation, **options):
        """
        Show new animation.
        """
        if not animations:
            raise ValueError("No animation was set.")

        animation = self._merge_animations(animations)
        animation = Animate(animation, options).dump()
        new_id = (
            None
            if self._display_target == DisplayTarget.BEGIN
            else uuid.uuid4().hex[:7]
        )
        self._display(
            DisplayTemplate.ANIMATE[self._display_target].format(
                id=self._id, new_id=new_id, animation=animation
            )
        )

    @staticmethod
    def _merge_animations(animations):
        if len(animations) == 1:
            return animations[0]

        merger = AnimationMerger()

        for animation in animations:
            merger.merge(animation)

        return merger

    def store(self) -> Snapshot:
        snapshot = "snapshot_" + uuid.uuid4().hex[:7]
        self._display(DisplayTemplate.STORE.format(id=self._id, snapshot=snapshot))
        return Snapshot(snapshot)

    @staticmethod
    def _display(html):
        display_html(
            cleandoc(
                DisplayTemplate.DISPLAY.format(
                    display_id=uuid.uuid4().hex[:7], html=html
                )
            ),
            raw=True,
        )
