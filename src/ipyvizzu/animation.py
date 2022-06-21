"""
A module used to work
with animations
"""

import abc
from enum import Enum
import json
from typing import Optional, List, Union

import pandas as pd
from pandas.api.types import is_numeric_dtype

from ipyvizzu.json import RawJavaScript, RawJavaScriptEncoder
from ipyvizzu.schema import DataSchema


class Animation:
    """
    An abstract class used to represent
    an animation object which has dump and build methods
    """

    def dump(self) -> str:
        """
        A method used to convert
        the builded data into json str
        """

        return json.dumps(self.build(), cls=RawJavaScriptEncoder)

    @abc.abstractmethod
    def build(self) -> dict:
        """
        A method used to return
        a dict with native python values that can be converted into json
        """


class PlainAnimation(dict, Animation):
    """
    A class used to represent
    a plain animation which is a custom dictionary
    """

    def build(self) -> dict:
        return self


class InferType(Enum):
    """
    An enum class used to define
    infer type options
    """

    DIMENSION = "dimension"
    MEASURE = "measure"


class Data(dict, Animation):
    """
    A class used to represent
    data animation
    """

    @classmethod
    def filter(cls, filter_expr: str):
        """
        A method used to return
        a Data() class which contains a filter
        """

        data = cls()
        data.set_filter(filter_expr)
        return data

    def set_filter(self, filter_expr: str) -> None:
        """
        A method used to add
        filter to an existing Data() class
        """

        filter_expr = (
            RawJavaScript(f"record => {{ return ({filter_expr}) }}")
            if filter_expr is not None
            else filter_expr
        )
        self.update({"filter": filter_expr})

    @classmethod
    def from_json(cls, filename: str):
        """
        A method used to return
        a Data() class which created from a json file
        """

        with open(filename, "r", encoding="utf8") as file_desc:
            return cls(json.load(file_desc))

    def add_record(self, record: list) -> None:
        """
        A method used to add
        record to an existing Data() class
        """

        self._add_value("records", record)

    def add_records(self, records: List[list]) -> None:
        """
        A method used to add
        records to an existing Data() class
        """

        list(map(self.add_record, records))

    def add_series(self, name: str, values: Optional[list] = None, **kwargs) -> None:
        """
        A method used to add
        series to an existing Data() class
        """

        self._add_named_value("series", name, values, **kwargs)

    def add_dimension(self, name, values=None, **kwargs):
        """
        A method used to add
        dimension to an existing Data() class
        """

        self._add_named_value("dimensions", name, values, **kwargs)

    def add_measure(self, name: str, values: Optional[list] = None, **kwargs) -> None:
        """
        A method used to add
        measure to an existing Data() class
        """

        self._add_named_value("measures", name, values, **kwargs)

    def add_data_frame(
        self,
        data_frame: Union[pd.DataFrame, pd.core.series.Series],
        default_measure_value=0,
        default_dimension_value="",
    ) -> None:
        """
        A method used to add
        dataframe to an existing Data() class
        """

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
        name: str,
    ) -> None:
        """
        A method used to add
        dataframe index to an existing Data() class
        """

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
            value["values"] = values

        self._add_value(dest, value)

    def _add_value(self, dest: str, value: Union[dict, list]) -> None:
        self.setdefault(dest, []).append(value)

    def build(self) -> dict:
        DataSchema.validate(self)
        return {"data": self}


class Config(dict, Animation):
    """
    A class used to represent
    config animation
    """

    def build(self) -> dict:
        return {"config": self}


class Style(Animation):
    """
    A class used to represent
    style animation
    """

    def __init__(self, data: Optional[dict]):
        self._data = data

    def build(self) -> dict:
        return {"style": self._data}


class Snapshot(Animation):
    """
    A class used to represent
    snapshot animation
    """

    def __init__(self, name: str):
        self._name = name

    def dump(self):
        """
        A method used to dump
        snapshot id as a string
        """

        return f"'{self._name}'"

    def build(self) -> NotImplementedError:
        raise NotImplementedError("Snapshot cannot be merged with other Animations")


class AnimationMerger(dict, Animation):
    """
    A class used to store and merge
    different types of animations
    """

    def merge(self, animation: Animation) -> None:
        """
        A method used to merge
        an animation with the previously merged animations
        """

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
