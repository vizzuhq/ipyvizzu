"""
This module provides the `PandasDataFrameConverter` class,
which allows converting a `pandas` `DataFrame` or `Series`
into a list of dictionaries representing series.
"""

from types import ModuleType
from typing import List, Optional, Tuple, Union

from ipyvizzu.data.converters.defaults import NAN_DIMENSION, NAN_MEASURE
from ipyvizzu.data.converters.df.defaults import MAX_ROWS
from ipyvizzu.data.converters.df.converter import DataFrameConverter
from ipyvizzu.data.converters.pandas.protocol import PandasSeries
from ipyvizzu.data.infer_type import InferType
from ipyvizzu.data.type_alias import (
    DimensionValue,
    MeasureValue,
    Series,
    SeriesValues,
)


class PandasDataFrameConverter(DataFrameConverter):
    """
    Converts a `pandas` `DataFrame` or `Series` into a list of dictionaries representing series.
    Each dictionary contains information about the series `name`, `values` and `type`.

    Parameters:
        df: The `pandas` `DataFrame` or `Series` to convert.
        default_measure_value:
            Default value to use for missing measure values. Defaults to 0.
        default_dimension_value:
            Default value to use for missing dimension values. Defaults to an empty string.
        max_rows: The maximum number of rows to include in the converted series list.
            If the `df` contains more rows,
            a random sample of the given number of rows will be taken.
        include_index:
            Name for the index column to include as a series.
            If provided, the index column will be added. Defaults to None.

    Example:
        Get series list from `DataFrame` columns:

            converter = PandasDataFrameConverter(df)
            series_list = converter.get_series_list()
    """

    def __init__(
        self,
        df: Union["pandas.DataFrame", "pandas.Series"],  # type: ignore
        default_measure_value: MeasureValue = NAN_MEASURE,
        default_dimension_value: DimensionValue = NAN_DIMENSION,
        max_rows: int = MAX_ROWS,
        include_index: Optional[str] = None,
    ) -> None:
        # pylint: disable=too-many-arguments

        super().__init__(default_measure_value, default_dimension_value, max_rows)
        self._pd = self._get_pandas()
        self._df = self._get_sampled_df(
            self._convert_to_df(df) if isinstance(df, PandasSeries) else df
        )
        self._include_index = include_index

    def get_series_list(self) -> List[Series]:
        """
        Convert the `DataFrame` columns to a list of dictionaries representing series.

        Returns:
            A list of dictionaries representing series,
            where each dictionary has `name`, `values` and `type` keys.
        """

        series_list = super().get_series_list()
        index_series = self.get_series_from_index()
        return index_series + series_list

    def get_series_from_index(self) -> List[Series]:
        """
        Convert the `DataFrame` index to a dictionary representing a series,
        if `include_index` is provided.

        Returns:
            A dictionary representing the index series with `name`, `values` and `type` keys.
            Returns `None` if `include_index` is not provided.
        """

        if not self._include_index or self._df.index.empty:
            return []
        df = self._pd.DataFrame({self._include_index: self._df.index})
        index_series_converter = PandasDataFrameConverter(
            df, self._default_measure_value, self._default_dimension_value
        )
        return index_series_converter.get_series_list()

    def _get_pandas(self) -> ModuleType:
        try:
            import pandas as pd  # pylint: disable=import-outside-toplevel

            return pd
        except ImportError as error:
            raise ImportError(
                "pandas is not available. Please install pandas to use this feature."
            ) from error

    def _convert_to_df(self, series: "pandas.Series") -> "pandas.Dataframe":  # type: ignore
        if series.empty:
            return self._pd.DataFrame()
        return self._pd.DataFrame(series)

    def _get_sampled_df(self, df: "pandas.DataFrame") -> "pandas.DataFrame":  # type: ignore
        row_number = len(df)
        if self._is_max_rows_exceeded(row_number):
            frac = self._max_rows / row_number
            sampled_df = df.sample(
                replace=False,
                frac=frac,
                random_state=42,
            )
            return sampled_df
        return df

    def _get_columns(self) -> List[str]:
        return self._df.columns

    def _convert_to_series_values_and_type(
        self, obj: str  # type: ignore
    ) -> Tuple[SeriesValues, InferType]:
        column_name = obj
        column = self._df[column_name]
        if self._pd.api.types.is_numeric_dtype(column.dtype):
            return self._convert_to_measure_values(column), InferType.MEASURE
        return self._convert_to_dimension_values(column), InferType.DIMENSION

    def _convert_to_measure_values(
        self, obj: "pandas.DataFrame"  # type: ignore
    ) -> List[MeasureValue]:
        column = obj
        return column.fillna(self._default_measure_value).astype(float).values.tolist()

    def _convert_to_dimension_values(
        self, obj: "pandas.DataFrame"  # type: ignore
    ) -> List[DimensionValue]:
        column = obj
        return column.fillna(self._default_dimension_value).astype(str).values.tolist()
