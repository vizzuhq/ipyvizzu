# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

from tests.test_data import DataWithAssets
from tests.utils.import_modifiers import RaiseImportError


class TestDataSpark(DataWithAssets):
    spark: SparkSession

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.spark = SparkSession.builder.appName("SparkTest").getOrCreate()

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()
        cls.spark.stop()

    def test_add_df_if_pyspark_not_installed(self) -> None:
        with RaiseImportError.module_name("pyspark"):
            with self.assertRaises(ImportError):
                self.data.add_df(self.spark.createDataFrame([], StructType([])))

    def test_add_df_with_none(self) -> None:
        self.data.add_df(None)
        self.assertEqual(
            {"data": {}},
            self.data.build(),
        )

    def test_add_df_with_empty_df(self) -> None:
        self.data.add_df(self.spark.createDataFrame([], StructType([])))
        self.assertEqual(
            {"data": {}},
            self.data.build(),
        )

    def test_add_df_with_df(self) -> None:
        schema = StructType(
            [
                StructField("DimensionSeries", StringType(), True),
                StructField("MeasureSeries", IntegerType(), True),
            ]
        )
        df_data = [
            ("1", 3),
            ("2", 4),
        ]
        df = self.spark.createDataFrame(df_data, schema)
        self.data.add_df(df)
        self.assertEqual(
            self.ref_pd_series,
            self.data.build(),
        )

    def test_add_df_with_df_contains_na(self) -> None:
        schema = StructType(
            [
                StructField("DimensionSeries", StringType(), True),
                StructField("MeasureSeries", IntegerType(), True),
            ]
        )
        df_data = [
            ("1", 3),
            (None, None),
        ]
        df = self.spark.createDataFrame(df_data, schema)
        self.data.add_df(df)
        self.assertEqual(
            self.ref_pd_series_with_nan,
            self.data.build(),
        )

    def test_add_df_with_df_and_with_include_index(self) -> None:
        df = self.spark.createDataFrame([], StructType([]))
        with self.assertRaises(ValueError):
            self.data.add_df(df, include_index="Index")

    def test_add_df_with_df_and_max_rows(self) -> None:
        max_rows = 2

        dimension_data = ["0", "1", "2", "3", "4"]
        measure_data = [0, 1, 2, 3, 4]
        df_data = []
        for i, dimension_value in enumerate(dimension_data):
            measure_value = measure_data[i]
            df_data.append((dimension_value, measure_value))
        schema = StructType(
            [
                StructField("DimensionSeries", StringType(), True),
                StructField("MeasureSeries", IntegerType(), True),
            ]
        )
        df = self.spark.createDataFrame(df_data, schema)
        self.data.add_df(df, max_rows=max_rows)

        data_series = self.data.build()["data"]["series"]

        dimension_series = data_series[0]["values"]
        measure_series = data_series[1]["values"]

        self.assertTrue(1 <= len(dimension_series) <= max_rows)
        self.assertTrue(1 <= len(measure_series) <= max_rows)

        is_dimension_series_sublist = all(
            item in dimension_data for item in dimension_series
        )
        is_measure_series_sublist = all(item in measure_data for item in measure_series)
        self.assertTrue(is_dimension_series_sublist)
        self.assertTrue(is_measure_series_sublist)

        del data_series[0]["values"]
        del data_series[1]["values"]
        self.assertEqual(
            [
                {
                    "name": "DimensionSeries",
                    "type": "dimension",
                },
                {
                    "name": "MeasureSeries",
                    "type": "measure",
                },
            ],
            data_series,
        )
