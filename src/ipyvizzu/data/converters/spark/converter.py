"""
This module provides the `SparkDataFrameConverter` class,
which allows converting a `pyspark` `DataFrame`
into a list of dictionaries representing series.
"""

from types import ModuleType
from typing import List, Tuple

from ipyvizzu.data.converters.defaults import NAN_DIMENSION, NAN_MEASURE
from ipyvizzu.data.converters.df.defaults import MAX_ROWS
from ipyvizzu.data.converters.df.converter import DataFrameConverter
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
        max_rows: The maximum number of rows to include in the converted series list.
            If the `df` contains more rows,
            a random sample of the given number of rows (approximately) will be taken.

    Example:
        Get series list from `DataFrame` columns:

            converter = SparkDataFrameConverter(df)
            series_list = converter.get_series_list()
    """

    # pylint: disable=too-few-public-methods

    def __init__(
        self,
        df: "pyspark.sql.DataFrame",  # type: ignore
        default_measure_value: MeasureValue = NAN_MEASURE,
        default_dimension_value: DimensionValue = NAN_DIMENSION,
        max_rows: int = MAX_ROWS,
    ) -> None:
        super().__init__(default_measure_value, default_dimension_value, max_rows)
        self._pyspark, self._pyspark_func = self._get_pyspark()
        self._df = self._get_sampled_df(df)

    def _get_pyspark(self) -> Tuple[ModuleType, ModuleType]:
        try:
            import pyspark  # pylint: disable=import-outside-toplevel
            from pyspark.sql import functions  # pylint: disable=import-outside-toplevel

            return pyspark, functions
        except ImportError as error:
            raise ImportError(
                "pyspark is not available. Please install pyspark to use this feature."
            ) from error

    def _get_sampled_df(
        self, df: "pyspark.sql.DataFrame"  # type: ignore
    ) -> "pyspark.sql.DataFrame":  # type: ignore
        row_number = df.count()
        if self._is_max_rows_exceeded(row_number):
            fraction = self._max_rows / row_number
            sample_df = df.sample(withReplacement=False, fraction=fraction, seed=42)
            return sample_df.limit(self._max_rows)
        return df

    def _get_columns(self) -> List[str]:
        return self._df.columns

    def _convert_to_series_values_and_type(
        self, obj: str
    ) -> Tuple[SeriesValues, InferType]:
        column_name = obj
        column = self._df.select(column_name)
        integer_type = self._pyspark.sql.types.IntegerType
        double_type = self._pyspark.sql.types.DoubleType
        if isinstance(column.schema[column_name].dataType, (integer_type, double_type)):
            return self._convert_to_measure_values(column_name), InferType.MEASURE
        return self._convert_to_dimension_values(column_name), InferType.DIMENSION

    def _convert_to_measure_values(self, obj: str) -> List[MeasureValue]:
        column_name = obj
        func = self._pyspark_func
        df = self._df.withColumn(
            column_name,
            func.when(
                func.col(column_name).isNull(), self._default_measure_value
            ).otherwise(func.col(column_name)),
        )
        df_rdd = (
            df.withColumn(column_name, func.col(column_name).cast("float"))
            .select(column_name)
            .rdd
        )
        return df_rdd.flatMap(list).collect()

    def _convert_to_dimension_values(self, obj: str) -> List[DimensionValue]:
        column_name = obj
        func = self._pyspark_func
        df = self._df.withColumn(
            column_name,
            func.when(
                func.col(column_name).isNull(), self._default_dimension_value
            ).otherwise(func.col(column_name)),
        )
        df_rdd = (
            df.withColumn(column_name, func.col(column_name).cast("string"))
            .select(column_name)
            .rdd
        )
        return df_rdd.flatMap(list).collect()
