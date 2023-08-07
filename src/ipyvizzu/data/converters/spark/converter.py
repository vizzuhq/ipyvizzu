"""
This module provides the `SparkDataFrameConverter` class,
which allows converting a `pyspark` `DataFrame`
into a list of dictionaries representing series.
"""

from types import ModuleType
from typing import List, Optional, Tuple

from ipyvizzu.data.converters.converter import DataFrameConverter
from ipyvizzu.data.infer_type import InferType
from ipyvizzu.data.type_alias import (
    DimensionValue,
    MeasureValue,
    SeriesValues,
)


class SparkDataFrameConverter(DataFrameConverter):
    """
    Converts a `pyspark` `DataFrame` into a list of dictionaries representing series.
    Each dictionary contains information about the series `name`, `values` and `type`.

    Parameters:
        df: The `pyspark` `DataFrame` to convert.
        default_measure_value:
            Default value to use for missing measure values. Defaults to 0.
        default_dimension_value:
            Default value to use for missing dimension values. Defaults to an empty string.
        include_index:
            Name for the index column to include as a series.
            If provided, the index column will be added. Defaults to None.

    Example:
        Get series list from `DataFrame` columns:

            converter = SparkDataFrameConverter(df)
            series_list = converter.get_series_list()
    """

    # pylint: disable=too-few-public-methods

    def __init__(
        self,
        df: "pyspark.sql.DataFrame",  # type: ignore
        default_measure_value: Optional[MeasureValue] = 0,
        default_dimension_value: Optional[DimensionValue] = "",
    ) -> None:
        self._pyspark = self._get_pyspark()
        self._df = df
        self._default_measure_value = default_measure_value
        self._default_dimension_value = default_dimension_value

    def _get_pyspark(self) -> ModuleType:
        try:
            import pyspark  # pylint: disable=import-outside-toplevel

            return pyspark
        except ImportError as error:
            raise ImportError(
                "pyspark is not available. Please install pyspark to use this feature."
            ) from error

    def _get_columns(self) -> List[str]:
        return self._df.columns

    def _convert_to_series_values_and_type(
        self, obj: str
    ) -> Tuple[SeriesValues, InferType]:
        column_name = obj
        column = self._df.select(column_name)
        IntegerType = self._pyspark.sql.types.IntegerType
        DoubleType = self._pyspark.sql.types.DoubleType
        if isinstance(column.schema[column_name].dataType, (IntegerType, DoubleType)):
            return self._convert_to_measure_values(column_name), InferType.MEASURE
        return self._convert_to_dimension_values(column_name), InferType.DIMENSION

    def _convert_to_measure_values(self, obj: str) -> List[MeasureValue]:
        column_name = obj
        when = self._pyspark.sql.functions.when
        col = self._pyspark.sql.functions.col
        df = self._df.withColumn(
            column_name,
            when(col(column_name).isNull(), self._default_measure_value).otherwise(
                col(column_name)
            ),
        )
        df = df.withColumn(column_name, col(column_name).cast("float"))
        return df.select(column_name).rdd.flatMap(lambda x: x).collect()

    def _convert_to_dimension_values(self, obj: str) -> List[DimensionValue]:
        column_name = obj
        when = self._pyspark.sql.functions.when
        col = self._pyspark.sql.functions.col
        df = self._df.withColumn(
            column_name,
            when(col(column_name).isNull(), self._default_dimension_value).otherwise(
                col(column_name)
            ),
        )
        df = df.withColumn(column_name, col(column_name).cast("string"))
        return df.select(column_name).rdd.flatMap(lambda x: x).collect()
