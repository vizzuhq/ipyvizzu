"""A module for working with chart animations."""

import abc
import json
from os import PathLike
from typing import List, Optional, Tuple, Union
import warnings

import jsonschema  # type: ignore

from ipyvizzu.data.converters.numpy.converter import NumpyArrayConverter
from ipyvizzu.data.converters.pandas.converter import PandasDataFrameConverter
from ipyvizzu.data.converters.spark.converter import SparkDataFrameConverter
from ipyvizzu.data.converters.numpy.type_alias import ColumnName, ColumnDtype
from ipyvizzu.data.type_alias import (
    DimensionValue,
    NestedMeasureValues,
    MeasureValue,
    Record,
    Series,
    SeriesValues,
)
from ipyvizzu.json import RawJavaScript, RawJavaScriptEncoder
from ipyvizzu.schema import DATA_SCHEMA


class AbstractAnimation:
    """
    An abstract class for representing animation objects
    that have `dump` and `build` methods.
    """

    def dump(self) -> str:
        """
        A method for converting the built dictionary into string.

        Returns:
            An str that has been json dumped with
                [RawJavaScriptEncoder][ipyvizzu.json.RawJavaScriptEncoder] from a dictionary.
        """

        return json.dumps(self.build(), cls=RawJavaScriptEncoder)

    @abc.abstractmethod
    def build(self) -> dict:
        """
        An abstract method for returning a dictionary with values
        that can be converted into json string.

        Returns:
            A dictionary that stored in the animation object.
        """


class PlainAnimation(dict, AbstractAnimation):
    """
    A class for representing plain animation.
    It can build any dictionary.
    """

    def build(self) -> dict:
        """
        A method for returning the plain animation dictionary.

        Returns:
            A dictionary that stored in the plain animation object.
        """

        return self


class Data(dict, AbstractAnimation):
    """
    A class for representing data animation.
    It can build data option of the chart.
    """

    @classmethod
    def filter(cls, filter_expr: Optional[str] = None) -> "Data":
        """
        A class method for creating a [Data][ipyvizzu.animation.Data]
        class instance with a data filter.

        Args:
            filter_expr: The JavaScript data filter expression.

        Returns:
            (Data): A data animation instance that contains a data filter.

        Example:
            Create a [Data][ipyvizzu.animation.Data] class with a data filter:

                filter = Data.filter("record['Genres'] == 'Pop'")
        """

        data = cls()
        data.set_filter(filter_expr)
        return data

    def set_filter(self, filter_expr: Optional[str] = None) -> None:
        """
        A method for adding a filter to an existing
        [Data][ipyvizzu.animation.Data] class instance.

        Args:
            filter_expr: The JavaScript data filter expression.

        Example:
            Add a data filter to a [Data][ipyvizzu.animation.Data] class instance:

                data = Data()
                data.set_filter("record['Genres'] == 'Pop'")
        """

        filter_expr_raw_js = (
            RawJavaScript(f"record => {{ return ({' '.join(filter_expr.split())}) }}")
            if filter_expr is not None
            else filter_expr
        )
        self.update({"filter": filter_expr_raw_js})

    @classmethod
    def from_json(cls, filename: Union[str, bytes, PathLike]) -> "Data":
        """
        A method for returning a [Data][ipyvizzu.animation.Data]
        class instance which has been created from a json file.

        Args:
            filename: The path of the data source json file.

        Returns:
            (Data): A data animation instance that has been created from a json file.
        """

        with open(filename, "r", encoding="utf8") as file_desc:
            return cls(json.load(file_desc))

    def add_record(self, record: Record) -> None:
        """
        A method for adding a record to an existing
        [Data][ipyvizzu.animation.Data] class instance.

        Args:
            record: A list that contains data values.

        Example:
            Adding a record to a [Data][ipyvizzu.animation.Data] class instance:

                data = Data()
                record = ["Pop", "Hard", 114]
                data.add_record(record)
        """

        self._add_value("records", record)

    def add_records(self, records: List[Record]) -> None:
        """
        A method for adding records to an existing
        [Data][ipyvizzu.animation.Data] class instance.

        Args:
            records: A list that contains data records.

        Example:
            Adding records to a [Data][ipyvizzu.animation.Data] class instance:

                data = Data()
                records = [
                    ["Pop", "Hard", 114],
                    ["Rock", "Hard", 96],
                    ["Pop", "Experimental", 127],
                    ["Rock", "Experimental", 83],
                ]
                data.add_records(records)
        """

        list(map(self.add_record, records))

    def add_series(
        self, name: str, values: Optional[SeriesValues] = None, **kwargs
    ) -> None:
        """
        A method for adding a series to an existing
        [Data][ipyvizzu.animation.Data] class instance.

        Args:
            name: The name of the series.
            values: The data values of the series.
            **kwargs (Optional):
                Arbitrary keyword arguments.

                For example infer type can be set with the `type` keywod argument.

        Example:
            Adding a series without values to a [Data][ipyvizzu.animation.Data] class instance:

                data = Data()
                data.add_series("Genres")

            Adding a series without values and with infer type to
            a [Data][ipyvizzu.animation.Data] class instance:

                data = Data()
                data.add_series("Kinds", type="dimension")

            Adding a series with values to a [Data][ipyvizzu.animation.Data] class instance:

                data = Data()
                data.add_series(
                    "Popularity", [114, 96, 127, 83]
                )
        """

        self._add_named_value("series", name, values, **kwargs)

    def add_series_list(self, series: List[Series]) -> None:
        """
        A method for adding list of series to an existing
        [Data][ipyvizzu.animation.Data] class instance.

        Args:
            series: List of series.
        """

        if series:
            self.setdefault("series", []).extend(series)

    def add_dimension(
        self, name: str, values: Optional[List[DimensionValue]] = None, **kwargs
    ) -> None:
        """
        A method for adding a dimension to an existing
        [Data][ipyvizzu.animation.Data] class instance.

        Args:
            name: The name of the dimension.
            values: The data values of the dimension.
            **kwargs (Optional): Arbitrary keyword arguments.

        Example:
            Adding a dimension with values to a [Data][ipyvizzu.animation.Data] class instance:

                data = Data()
                data.add_dimension("Genres", ["Pop", "Rock"])
        """

        self._add_named_value("dimensions", name, values, **kwargs)

    def add_measure(
        self, name: str, values: Optional[NestedMeasureValues] = None, **kwargs
    ) -> None:
        """
        A method for adding a measure to an existing
        [Data][ipyvizzu.animation.Data] class instance.

        Args:
            name: The name of the measure.
            values: The data values of the measure.
            **kwargs (Optional): Arbitrary keyword arguments.

        Example:
            Adding a measure with values to a [Data][ipyvizzu.animation.Data] class instance:

                data = Data()
                data.add_measure(
                    "Popularity",
                    [
                        [114, 96],
                        [127, 83],
                    ],
                )
        """

        self._add_named_value("measures", name, values, **kwargs)

    def add_df(
        self,
        df: Optional[Union["pandas.DataFrame", "pandas.Series"]],  # type: ignore
        default_measure_value: Optional[MeasureValue] = 0,
        default_dimension_value: Optional[DimensionValue] = "",
        include_index: Optional[str] = None,
    ) -> None:
        """
        Add a `pandas` `DataFrame` or `Series` to an existing
        [Data][ipyvizzu.animation.Data] class instance.

        Args:
            df:
                The `pandas` `DataFrame` or `Series` to add.
            default_measure_value:
                The default measure value to fill empty values. Defaults to 0.
            default_dimension_value:
                The default dimension value to fill empty values. Defaults to an empty string.
            include_index:
                Add the data frame's index as a column with the given name. Defaults to `None`.

        Example:
            Adding a data frame to a [Data][ipyvizzu.animation.Data] class instance:

                df = pd.DataFrame(
                    {
                        "Genres": ["Pop", "Rock", "Pop", "Rock"],
                        "Kinds": ["Hard", "Hard", "Experimental", "Experimental"],
                        "Popularity": [114, 96, 127, 83],
                    }
                )
                data = Data()
                data.add_df(df)
        """

        if not isinstance(df, type(None)):
            converter = PandasDataFrameConverter(
                df, default_measure_value, default_dimension_value, include_index
            )
            series_list = converter.get_series_list()
            self.add_series_list(series_list)

    def add_data_frame(
        self,
        data_frame: Optional[Union["pandas.DataFrame", "pandas.Series"]],  # type: ignore
        default_measure_value: Optional[MeasureValue] = 0,
        default_dimension_value: Optional[DimensionValue] = "",
    ) -> None:
        """
        [Deprecated] This function is deprecated and will be removed in future versions.
        Use [add_df][ipyvizzu.animation.Data.add_df] function instead.

        Add a `pandas` `DataFrame` or `Series` to an existing
        [Data][ipyvizzu.animation.Data] class instance.



        Args:
            data_frame:
                The `pandas` `DataFrame` or `Series` to add.
            default_measure_value:
                The default measure value to fill empty values. Defaults to 0.
            default_dimension_value:
                The default dimension value to fill empty values. Defaults to an empty string.
        """

        # pylint: disable=line-too-long

        reference = "https://ipyvizzu.vizzuhq.com/0.16/reference/ipyvizzu/animation/#ipyvizzu.animation.Data.add_df"
        warnings.warn(
            f"'add_data_frame' is deprecated and will be removed in future versions. Use 'add_df' instead - see {reference}",
            DeprecationWarning,
            stacklevel=2,
        )
        self.add_df(data_frame, default_measure_value, default_dimension_value)

    def add_df_index(
        self,
        df: Optional[Union["pandas.DataFrame", "pandas.Series"]],  # type: ignore
        column_name: str = "Index",
    ) -> None:
        """
        Add the index of a `pandas` `DataFrame` as a series to an existing
        [Data][ipyvizzu.animation.Data] class instance.

        Args:
            df:
                The `pandas` `DataFrame` or `Series` from which to extract the index.
            column_name:
                Name for the index column to add as a series.

        Example:
            Adding a data frame's index to a
            [Data][ipyvizzu.animation.Data] class instance:

                df = pd.DataFrame(
                    {"Popularity": [114, 96]},
                    index=["x", "y"]
                )
                data = Data()
                data.add_df_index(df, "DataFrameIndex")
                data.add_df(df)
        """

        if not isinstance(df, type(None)):
            converter = PandasDataFrameConverter(df, include_index=column_name)
            series_list = converter.get_series_from_index()
            self.add_series_list(series_list)

    def add_data_frame_index(
        self,
        data_frame: Optional[Union["pandas.DataFrame", "pandas.Series"]],  # type: ignore
        name: str,
    ) -> None:
        """
        [Deprecated] This function is deprecated and will be removed in future versions.
        Use [add_df_index][ipyvizzu.animation.Data.add_df_index] function instead.

        Add the index of a `pandas` `DataFrame` as a series to an existing
        [Data][ipyvizzu.animation.Data] class instance.

        Args:
            data_frame:
                The `pandas` `DataFrame` or `Series` from which to extract the index.
            name:
                The name of the index series.
        """

        # pylint: disable=line-too-long

        reference = "https://ipyvizzu.vizzuhq.com/0.16/reference/ipyvizzu/animation/#ipyvizzu.animation.Data.add_df_index"
        warnings.warn(
            f"'add_data_frame_index' is deprecated and will be removed in future versions. Use 'add_df_index' instead - see {reference}",
            DeprecationWarning,
            stacklevel=2,
        )
        self.add_df_index(data_frame, name)

    def add_np_array(
        self,
        np_array: Optional["numpy.array"],  # type: ignore
        column_name: Optional[ColumnName] = None,
        column_dtype: Optional[ColumnDtype] = None,
        default_measure_value: Optional[MeasureValue] = 0,
        default_dimension_value: Optional[DimensionValue] = "",
    ) -> None:
        """
        Add a `numpy` `array` to an existing
        [Data][ipyvizzu.animation.Data] class instance.

        Args:
            np_array: The `numpy` `array` to add.
            column_name:
                The name of a column. By default, uses column indices. Can be set with an
                Index:Name pair or, for single-dimensional arrays, with just the Name.
            column_dtype:
                The dtype of a column. By default, uses the np_array's dtype. Can be set
                with an Index:DType pair or, for single-dimensional arrays, with just the DType.
            default_measure_value:
                Default value to use for missing measure values. Defaults to 0.
            default_dimension_value:
                Default value to use for missing dimension values. Defaults to an empty string.

        Example:
            Adding a data frame to a [Data][ipyvizzu.animation.Data] class instance:

                np_array = np.zeros((3, 4))
                data = Data()
                data.add_np_array(np_array)
        """

        # pylint: disable=too-many-arguments

        if not isinstance(np_array, type(None)):
            converter = NumpyArrayConverter(
                np_array,
                column_name,
                column_dtype,
                default_measure_value,
                default_dimension_value,
            )
            series_list = converter.get_series_list()
            self.add_series_list(series_list)

    def add_spark_df(
        self,
        df: Optional["pyspark.sql.DataFrame"],  # type: ignore
        default_measure_value: Optional[MeasureValue] = 0,
        default_dimension_value: Optional[DimensionValue] = "",
    ) -> None:
        """
        Add a `pyspark` `DataFrame` to an existing
        [Data][ipyvizzu.animation.Data] class instance.

        Args:
            df:
                The `pyspark` `DataFrame` to add.
            default_measure_value:
                The default measure value to fill empty values. Defaults to 0.
            default_dimension_value:
                The default dimension value to fill empty values. Defaults to an empty string.
        """

        if not isinstance(df, type(None)):
            converter = SparkDataFrameConverter(
                df, default_measure_value, default_dimension_value
            )
            series_list = converter.get_series_list()
            self.add_series_list(series_list)

    def _add_named_value(
        self,
        dest: str,
        name: str,
        values: Optional[
            Union[
                SeriesValues,
                NestedMeasureValues,
            ]
        ] = None,
        **kwargs,
    ) -> None:
        value = {"name": name, **kwargs}

        if values is not None:
            value["values"] = values

        self._add_value(dest, value)

    def _add_value(self, dest: str, value: Union[dict, list]) -> None:
        self.setdefault(dest, []).append(value)

    def build(self) -> dict:
        """
        A method for validating and returning the data animation dictionary.

        Returns:
            A dictionary that stored in the data animation object.
                It contains a `data` key whose value is the stored animation.
        """

        jsonschema.validate(self, DATA_SCHEMA)
        return {"data": self}


class ConfigAttr(type):
    """
    A metaclass class for the [Config][ipyvizzu.animation.Config] class.
    Returns a [Config][ipyvizzu.animation.Config] class with a chart preset
    if the `__getattr__` method called.

    For information on all available chart presets see the
    [Vizzu Code reference](https://lib.vizzuhq.com/latest/reference/modules/Presets/#interfaces).
    """

    @classmethod
    def __getattr__(mcs, name):
        config_attr = mcs("ConfigAttr", (object,), {"name": name})
        return config_attr._get_preset  # pylint: disable=no-member

    def _get_preset(cls, preset):
        config = Config(RawJavaScript(f"lib.presets.{cls.name}({preset})"))
        return config


class Config(AbstractAnimation, metaclass=ConfigAttr):
    """
    A class for representing config animation.
    It can build config option of the chart.
    """

    def __init__(self, data: Optional[Union[dict, RawJavaScript]]):
        """
        Config constructor.

        Args:
            data:
                A config animation dictionary.
                For information on all available config parameters see the
                [Vizzu Code reference](https://lib.vizzuhq.com/latest/reference/interfaces/Config.Chart/#properties).
        """  # pylint: disable=line-too-long

        self._data = data

    def build(self) -> dict:
        """
        A method for returning the config animation dictionary.

        Returns:
            A dictionary that stored in the config animation object.
                It contains a `config` key whose value is the stored animation.
        """

        return {"config": self._data}


class Style(AbstractAnimation):
    """
    A class for representing style animation.
    It can build style option of the chart.
    """

    def __init__(self, data: Optional[dict]):
        """
        Style constructor.

        Args:
            data:
                A style animation dictionary.
                For information on all available style parameters see the [Style][styling-properties]
                chapter or the
                [Vizzu Code reference](https://lib.vizzuhq.com/latest/reference/interfaces/Styles.Chart/#properties).
        """  # pylint: disable=line-too-long

        self._data = data

    def build(self) -> dict:
        """
        A method for returning the style animation dictionary.

        Returns:
            A dictionary that stored in the style animation object.
                It contains a `style` key whose value is the stored animation.
        """

        return {"style": self._data}


class Keyframe(AbstractAnimation):
    """
    A class for representing keyframe animation.
    It can build keyframe of the chart.
    """

    def __init__(
        self,
        *animations: AbstractAnimation,
        **options: Optional[Union[str, int, float, dict]],
    ):
        """
        Keyframe constructor.

        Args:
            *animations:
                List of AbstractAnimation inherited objects such as [Data][ipyvizzu.animation.Data],
                [Config][ipyvizzu.animation.Config] and [Style][ipyvizzu.animation.Style].
            **options: Dictionary of animation options for example `duration=1`.
                For information on all available animation options see the
                [Vizzu Code reference](https://lib.vizzuhq.com/latest/reference/interfaces/Anim.Options/#properties).

        Raises:
            ValueError: If `animations` is not set.
            ValueError: If initialized with a `Keyframe`.
        """  # pylint: disable=line-too-long

        if not animations:
            raise ValueError("No animation was set.")
        if [animation for animation in animations if isinstance(animation, Keyframe)]:
            raise ValueError("A Keyframe cannot contain a Keyframe.")

        self._keyframe = {}
        self._keyframe["target"] = AnimationMerger.merge_animations(animations).build()
        if options:
            self._keyframe["options"] = options

    def build(self) -> dict:
        """
        A method for returning the keyframe animation dictionary.

        Returns:
            A dictionary that stored in the keyframe animation object.
                It contains a `target` key whose value is the stored animation
                and an optional `options` key whose value is the stored animation options.
        """

        return self._keyframe


class Snapshot(AbstractAnimation):
    """
    A class for representing a stored chart state.
    It can build the snapshot id of the chart.
    """

    def __init__(self, snapshot_id: str):
        """
        Snapshot constructor.

        Args:
            snapshot_id: A snapshot id.
        """

        self._snapshot_id = snapshot_id

    def build(self) -> str:  # type: ignore
        """
        A method for returning the snapshot id str.

        Returns:
            An str snapshot id that stored in the snapshot animation object.
        """

        return self._snapshot_id


class Animation(Snapshot):
    """
    A class for representing a stored animation.
    It can build the snapshot id of the animation.
    """


class AnimationMerger(AbstractAnimation):
    """A class for merging different types of animations."""

    def __init__(self) -> None:
        """AnimationMerger constructor."""

        self._dict: dict = {}
        self._list: list = []

    @classmethod
    def merge_animations(
        cls, animations: Tuple[AbstractAnimation, ...]
    ) -> AbstractAnimation:
        """
        A class method for merging animations.

        Args:
            animations: List of `AbstractAnimation` inherited objects.

        Returns:
            An `AnimationMerger` class with the merged animations.
        """

        if len(animations) == 1 and not isinstance(animations[0], Keyframe):
            return animations[0]

        merger = cls()
        for animation in animations:
            merger.merge(animation)

        return merger

    def merge(self, animation: AbstractAnimation) -> None:
        """
        A method for merging an animation with the previously merged animations.

        Args:
            animation: An animation to be merged with with previously merged animations.

        Raises:
            ValueError: If the type of an animation is already merged.
            ValueError: If `Keyframe` is merged with different type of animation.
        """

        if isinstance(animation, Keyframe):
            if self._dict:
                raise ValueError("Keyframe cannot be merged with other animations.")
            data = animation.build()
            self._list.append(data)
        else:
            if self._list:
                raise ValueError("Keyframe cannot be merged with other animations.")
            data = self._validate(animation)
            self._dict.update(data)

    def _validate(self, animation: AbstractAnimation) -> dict:
        if isinstance(animation, Snapshot):
            raise ValueError("Snapshot cannot be merged with other animations.")
        data = animation.build()
        common_keys = set(data).intersection(self._dict)

        if common_keys:
            raise ValueError(f"{common_keys} is already merged.")

        return data

    def build(self) -> Union[dict, list]:  # type: ignore
        """
        A method for returning a merged list of `Keyframes`
        or a merged dictionary from different types of animations.

        Returns:
            A merged list of [Keyframes][ipyvizzu.animation.Keyframe] or
                a merged dictionary from
                [Data][ipyvizzu.animation.Data],
                [Config][ipyvizzu.animation.Config] and
                [Style][ipyvizzu.animation.Style] animations.
        """

        if self._dict:
            return self._dict
        return self._list
