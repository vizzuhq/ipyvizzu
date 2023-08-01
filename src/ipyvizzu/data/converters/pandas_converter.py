"""
This module provides the `PandasDataFrameConverter` class,
which allows converting a `pandas` `DataFrame` or `Series`
into a list of dictionaries representing series.
"""

from typing import Optional, Any, List, Dict, Union, Tuple

from ipyvizzu.data.infer_type import InferType


class PandasDataFrameConverter:
    """
    Converts a `pandas` `DataFrame` or `Series` into a list of dictionaries representing series.
    Each dictionary contains information about the series `name`, `values` and `type`.

    Parameters:
        df: The `pandas` `DataFrame` or `Series` to convert.
        default_measure_value:
            Default value to use for missing measure values. Defaults to 0.
        default_dimension_value:
            Default value to use for missing dimension values. Defaults to an empty string.
        include_index:
            Name for the index column to include as a series.
            If provided, the index column will be added. Defaults to None.

    Example:
        Get series list from `DataFrame` columns:

            converter = PandasDataFrameConverter(df)
            series_list = converter.get_series_list_from_columns()
    """

    def __init__(
        self,
        df: Union["pd.DataFrame", "pd.Series"],  # type: ignore
        default_measure_value: Optional[Any] = 0,
        default_dimension_value: Optional[Any] = "",
        include_index: Optional[str] = None,
    ) -> None:
        self._df = self._get_df(df)
        self._default_measure_value = default_measure_value
        self._default_dimension_value = default_dimension_value
        self._include_index = include_index

    def _get_df(self, df: Union["pd.DataFrame", "pd.Series"]) -> "pd.DataFrame":  # type: ignore
        try:
            import pandas as pd  # pylint: disable=import-outside-toplevel

            if isinstance(df, pd.DataFrame):
                return df
            if isinstance(df, pd.Series):
                return pd.DataFrame(df)
            if df is None:
                return pd.DataFrame()
            raise TypeError(
                "df must be an instance of pandas.DataFrame or pandas.Series"
            )
        except ImportError as error:
            raise ImportError(
                "pandas is not available. Please install pandas to use this feature."
            ) from error

    def get_series_list_from_columns(self) -> List[Dict[str, Union[str, List[Any]]]]:
        """
        Convert the `DataFrame` columns to a list of dictionaries representing series.

        Returns:
            A list of dictionaries representing series,
            where each dictionary has `name`, `values` and `type` keys.
        """

        series_list = []
        for name in self._df.columns:
            series_list.append(self._get_series_from_column(name))
        index_series = self.get_series_from_index()
        if index_series:
            series_list.append(index_series)
        return series_list

    def get_series_from_index(self) -> Optional[Dict[str, Union[str, List[Any]]]]:
        """
        Convert the `DataFrame` index to a dictionary representing a series,
        if `include_index` is provided.

        Returns:
            A dictionary representing the index series with `name`, `values` and `type` keys.
            Returns `None` if `include_index` is not provided.
        """

        if not self._include_index:
            return None
        name = self._include_index
        values, infer_type = self._get_column_data(self._df.index)
        return self._convert_to_series(name, values, infer_type)

    def _get_series_from_column(
        self, column_name: str
    ) -> Dict[str, Union[str, List[Any]]]:
        column = self._df[column_name]
        values, infer_type = self._get_column_data(column)
        return self._convert_to_series(column_name, values, infer_type)

    def _get_column_data(self, column: "pd.Series") -> Tuple[List[Any], InferType]:  # type: ignore
        try:
            from pandas.api.types import (  # pylint: disable=import-outside-toplevel
                is_numeric_dtype,
            )

            if is_numeric_dtype(column.dtype):
                return self._get_measure_column_data(column)
            return self._get_dimension_column_data(column)
        except ImportError as error:
            raise ImportError(
                "pandas is not available. Please install pandas to use this feature."
            ) from error

    def _get_measure_column_data(
        self, column: "pd.Series"  # type: ignore
    ) -> Tuple[List[Any], InferType]:
        return (
            column.fillna(self._default_measure_value).astype(float).values.tolist(),
            InferType.MEASURE,
        )

    def _get_dimension_column_data(
        self, column: "pd.Series"  # type: ignore
    ) -> Tuple[List[Any], InferType]:
        return (
            column.fillna(self._default_dimension_value).astype(str).values.tolist(),
            InferType.DIMENSION,
        )

    def _convert_to_series(
        self, name: str, values: List[Any], infer_type: InferType
    ) -> Dict[str, Union[str, List[Any]]]:
        return {
            "name": name,
            "values": values,
            "type": infer_type.value,
        }
