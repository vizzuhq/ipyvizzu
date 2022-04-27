import abc
import enum
import json
import typing
import pandas as pd
from pandas.api.types import is_numeric_dtype

from ipyvizzu.json import RawJavaScript, RawJavaScriptEncoder
from ipyvizzu.template import DisplayTemplate
from ipyvizzu.schema import DataSchema


class Animation:
    def dump(self):
        return json.dumps(self.build(), cls=RawJavaScriptEncoder)

    @abc.abstractmethod
    def build(self) -> typing.Mapping:
        """
        Return a dict with native python values that can be converted into json.
        """


class PlainAnimation(dict, Animation):
    def build(self):
        return self


class InferType(enum.Enum):

    DIMENSION = "dimension"
    MEASURE = "measure"


class Data(dict, Animation):
    """
    Vizzu data with the required keys: records, series, dimensions or measures.
    """

    @classmethod
    def filter(cls, filter_expr):
        data = cls()
        data.set_filter(filter_expr)
        return data

    def set_filter(self, filter_expr):
        filter_expr = (
            RawJavaScript(f"record => {{ return ({filter_expr}) }}")
            if filter_expr is not None
            else filter_expr
        )
        self.update({"filter": filter_expr})

    @classmethod
    def from_json(cls, filename):
        with open(filename, "r", encoding="utf8") as file_desc:
            return cls(json.load(file_desc))

    def add_record(self, record):
        self._add_value("records", record)

    def add_records(self, records):
        list(map(self.add_record, records))

    def add_series(self, name, values=None, **kwargs):
        self._add_named_value("series", name, values, **kwargs)

    def add_dimension(self, name, values=None, **kwargs):
        self._add_named_value("dimensions", name, values, **kwargs)

    def add_measure(self, name, values=None, **kwargs):
        self._add_named_value("measures", name, values, **kwargs)

    def add_data_frame(
        self,
        data_frame,
        default_measure_value=0,
        default_dimension_value="",
    ):
        if not isinstance(data_frame, type(None)):
            if isinstance(data_frame, pd.core.series.Series):
                data_frame = pd.DataFrame(data_frame)
            if not isinstance(data_frame, pd.DataFrame):
                raise TypeError(
                    "data_frame must be instance of pandas.DataFrame or pandas.Series"
                )
            for name in data_frame.columns:
                values = []
                if is_numeric_dtype(data_frame[name].dtype):
                    infer_type = InferType.MEASURE
                    values = [
                        float(i)
                        for i in data_frame[name].fillna(default_measure_value).values
                    ]
                else:
                    infer_type = InferType.DIMENSION
                    values = [
                        str(i)
                        for i in data_frame[name].fillna(default_dimension_value).values
                    ]

                self.add_series(
                    name,
                    values,
                    type=infer_type.value,
                )

    def add_data_frame_index(
        self,
        data_frame,
        name: typing.Optional[str],
    ):
        if data_frame is not None:
            if isinstance(data_frame, pd.core.series.Series):
                data_frame = pd.DataFrame(data_frame)
            if not isinstance(data_frame, pd.DataFrame):
                raise TypeError(
                    "data_frame must be instance of pandas.DataFrame or pandas.Series"
                )
            self.add_series(
                str(name),
                [str(i) for i in data_frame.index],
                type=InferType.DIMENSION.value,
            )

    def _add_named_value(self, dest, name, values=None, **kwargs):
        value = {"name": name, **kwargs}

        if values is not None:
            value["values"] = values

        self._add_value(dest, value)

    def _add_value(self, dest, value):
        self.setdefault(dest, []).append(value)

    def build(self):
        DataSchema.validate(self)
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
        return DisplayTemplate.STORED.format(id=self._name)

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
