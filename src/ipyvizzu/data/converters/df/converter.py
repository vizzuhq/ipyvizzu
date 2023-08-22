"""
This module provides the `DataFrameConverter` abstract class.
"""

from abc import abstractmethod
from typing import List
import warnings

from ipyvizzu.data.converters.converter import ToSeriesListConverter
from ipyvizzu.data.converters.df.type_alias import DataFrame
from ipyvizzu.data.type_alias import (
    DimensionValue,
    MeasureValue,
    Series,
)


class DataFrameConverter(ToSeriesListConverter):
    """
    Converts data frame into a list of dictionaries representing series.
    Each dictionary contains information about the series `name`, `values` and `type`.
    """

    # pylint: disable=too-few-public-methods

    def __init__(
        self,
        default_measure_value: MeasureValue,
        default_dimension_value: DimensionValue,
        max_rows: int,
    ) -> None:
        super().__init__(default_measure_value, default_dimension_value)
        self._max_rows = max_rows

    def get_series_list(self) -> List[Series]:
        """
        Convert the `DataFrame` columns to a list of dictionaries representing series.

        Returns:
            A list of dictionaries representing series,
            where each dictionary has `name`, `values` and `type` keys.
        """

        series_list = []
        for name in self._get_columns():
            series_list.append(self._get_series_from_column(name))
        return series_list

    def _get_series_from_column(self, column_name: str) -> Series:
        values, infer_type = self._convert_to_series_values_and_type(column_name)
        return self._convert_to_series(column_name, values, infer_type)

    def _is_max_rows_exceeded(self, row_number: int) -> bool:
        if row_number > self._max_rows:
            warnings.warn(
                "The number of rows of the dataframe exceeds the set `max_rows`, "
                f"the dataframe is randomly sampled to the set value ({self._max_rows}).",
                UserWarning,
                stacklevel=2,
            )
            return True
        return False

    @abstractmethod
    def _get_sampled_df(self, df: DataFrame) -> DataFrame:
        """
        Returns a sampled data frame for the maximum number of rows.
        """

    @abstractmethod
    def _get_columns(self) -> List[str]:
        """
        Return column names of the data frame.
        """
