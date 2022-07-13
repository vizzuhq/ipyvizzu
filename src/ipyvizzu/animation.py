"""A module for working with chart animations."""

import abc
from enum import Enum
from os import PathLike
import json
from typing import Optional, Union, List
import jsonschema  # type: ignore

import pandas as pd  # type: ignore
from pandas.api.types import is_numeric_dtype  # type: ignore

from ipyvizzu.json import RawJavaScript, RawJavaScriptEncoder
from ipyvizzu.schema import DATA_SCHEMA


class Animation:
    """
    An abstract class for representing animation objects
    that have dump and build methods.
    """

    def dump(self) -> str:
        """A method for converting the builded dictionary into json string."""

        return json.dumps(self.build(), cls=RawJavaScriptEncoder)

    @abc.abstractmethod
    def build(self) -> dict:
        """
        A method for returning a dictionary
        with native python values that can be converted into json.
        """


class PlainAnimation(dict, Animation):
    """
    A class for representing plain animation.
    It can build any dictionary.
    """

    def build(self) -> dict:
        return self


class InferType(Enum):
    """An enum class for storing infer types."""

    DIMENSION = "dimension"
    MEASURE = "measure"


class Data(dict, Animation):
    """
    A class for representing data animation.
    It can build data of the chart.
    """

    @classmethod
    def filter(cls, filter_expr: Optional[str] = None):  # -> Data:
        """A method for returning a Data() class with a filter."""

        data = cls()
        data.set_filter(filter_expr)
        return data

    def set_filter(self, filter_expr: Optional[str] = None) -> None:
        """A method used to add a filter to a Data() class instance."""

        filter_expr_raw_js = (
            RawJavaScript(f"record => {{ return ({' '.join(filter_expr.split())}) }}")
            if filter_expr is not None
            else filter_expr
        )
        self.update({"filter": filter_expr_raw_js})

    @classmethod
    def from_json(cls, filename: Union[str, bytes, PathLike]):  # -> Data:
        """A method for returning a Data() class which created from a json file."""

        with open(filename, "r", encoding="utf8") as file_desc:
            return cls(json.load(file_desc))

    def add_record(self, record: list) -> None:
        """A method used to add a record to a Data() class instance."""

        self._add_value("records", record)

    def add_records(self, records: List[list]) -> None:
        """A method used to add a records to a Data() class instance."""

        list(map(self.add_record, records))

    def add_series(self, name: str, values: Optional[list] = None, **kwargs) -> None:
        """A method used to add a series to a Data() class instance."""

        self._add_named_value("series", name, values, **kwargs)

    def add_dimension(self, name: str, values: Optional[list] = None, **kwargs) -> None:
        """A method used to add a dimension to a Data() class instance."""

        self._add_named_value("dimensions", name, values, **kwargs)

    def add_measure(self, name: str, values: Optional[list] = None, **kwargs) -> None:
        """A method used to add a measure to a Data() class instance."""

        self._add_named_value("measures", name, values, **kwargs)

    def add_data_frame(
        self,
        data_frame: Union[pd.DataFrame, pd.core.series.Series],
        default_measure_value=0,
        default_dimension_value="",
    ) -> None:
        """A method used to add a dataframe to a Data() class instance."""

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
                    values = (
                        data_frame[name]
                        .fillna(default_measure_value)
                        .astype(float)
                        .values.tolist()
                    )
                else:
                    infer_type = InferType.DIMENSION
                    values = (
                        data_frame[name]
                        .fillna(default_dimension_value)
                        .astype(str)
                        .values.tolist()
                    )
                self.add_series(
                    name,
                    values,
                    type=infer_type.value,
                )

    def add_data_frame_index(
        self,
        data_frame: Union[pd.DataFrame, pd.core.series.Series],
        name: Optional[str],
    ) -> None:
        """A method used to add a dataframe's index to a Data() class instance."""

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

    def _add_named_value(
        self, dest: str, name: str, values: Optional[list] = None, **kwargs
    ) -> None:
        value = {"name": name, **kwargs}

        if values is not None:
            value["values"] = values  # type: ignore

        self._add_value(dest, value)

    def _add_value(self, dest: str, value: Union[dict, list]) -> None:
        self.setdefault(dest, []).append(value)

    def build(self) -> dict:
        jsonschema.validate(self, DATA_SCHEMA)
        return {"data": self}


class ConfigAttr(type):
    """
    A class for representing config attribute metaclass.
    It returns a Config class with a chart preset if __getattr__ called.
    """

    @classmethod
    def __getattr__(cls, name):
        config_attr = cls("ConfigAttr", (object,), {"name": name})
        return config_attr._get_preset  # pylint: disable=no-member

    def _get_preset(cls, preset):
        config = Config(RawJavaScript(f"lib.presets.{cls.name}({preset})"))
        return config


class Config(Animation, metaclass=ConfigAttr):
    """
    A class for representing config animation.
    It can build config of the chart.
    """

    def __init__(self, data: Optional[dict]):
        self._data = data

    def build(self) -> dict:
        return {"config": self._data}


class Style(Animation):
    """
    A class for representing style animation.
    It can build style of the chart.
    """

    def __init__(self, data: Optional[dict]):
        self._data = data

    def build(self) -> dict:
        return {"style": self._data}


class Snapshot(Animation):
    """
    A class for representing snapshot animation.
    It can build a snapshot id of the chart.
    """

    def __init__(self, name: str):
        self._name = name

    def dump(self) -> str:
        """A method for dumping snapshot id as a string."""

        return f"'{self._name}'"

    def build(self):
        raise NotImplementedError("Snapshot cannot be merged with other Animations")


class AnimationMerger(dict, Animation):
    """A class for merging different types of animations."""

    def merge(self, animation: Animation) -> None:
        """A method for merging an animation with previously merged animations."""

        data = self._validate(animation)
        self.update(data)

    def _validate(self, animation: Animation) -> dict:
        data = animation.build()
        common_keys = set(data).intersection(self)

        if common_keys:
            raise ValueError(f"Animation is already merged: {common_keys}")

        return data

    def build(self) -> dict:
        return self
