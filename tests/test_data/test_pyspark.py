# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

from tests.test_data import DataWithAssets
from tests.utils.import_error import RaiseImportError


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

    def test_add_spark_df_if_pyspark_not_installed(self) -> None:
        with RaiseImportError.module_name("pyspark"):
            with self.assertRaises(ImportError):
                self.data.add_spark_df(self.spark.createDataFrame([], StructType([])))

    def test_add_spark_df_with_none(self) -> None:
        self.data.add_spark_df(None)
        self.assertEqual(
            {"data": {}},
            self.data.build(),
        )

    def test_add_spark_df_with_empty_df(self) -> None:
        self.data.add_spark_df(self.spark.createDataFrame([], StructType([])))
        self.assertEqual(
            {"data": {}},
            self.data.build(),
        )

    def test_add_spark_df_with_df(self) -> None:
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
        self.data.add_spark_df(df)
        self.assertEqual(
            self.ref_pd_series,
            self.data.build(),
        )

    def test_add_spark_df_with_df_contains_na(self) -> None:
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
        self.data.add_spark_df(df)
        self.assertEqual(
            self.ref_pd_series_with_nan,
            self.data.build(),
        )

    def test_add_spark_df_with_df_and_max_rows(self) -> None:
        schema = StructType(
            [
                StructField("DimensionSeries", StringType(), True),
                StructField("MeasureSeries", IntegerType(), True),
            ]
        )
        df_data = [
            ("1", 3),
            ("2", 4),
            ("3", 5),
            ("4", 6),
            ("5", 7),
        ]
        df = self.spark.createDataFrame(df_data, schema)
        self.data.add_spark_df(df, max_rows=2)
        self.assertEqual(
            {
                "data": {
                    "series": [
                        {
                            "name": "DimensionSeries",
                            "type": "dimension",
                            "values": ["2", "3", "4"],
                        },
                        {
                            "name": "MeasureSeries",
                            "type": "measure",
                            "values": [4.0, 5.0, 6.0],
                        },
                    ]
                }
            },
            self.data.build(),
        )
