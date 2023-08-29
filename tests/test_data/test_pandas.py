# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import pandas as pd

from tests.test_data import DataWithAssets
from tests.utils.import_modifiers import RaiseImportError


class TestDf(DataWithAssets):
    def test_add_df_if_pandas_not_installed(self) -> None:
        with RaiseImportError.module_name("pandas"):
            with self.assertRaises(ImportError):
                self.data.add_df(pd.DataFrame())

    def test_add_df_with_none(self) -> None:
        self.data.add_df(None)
        self.assertEqual(
            {"data": {}},
            self.data.build(),
        )

    def test_add_df_with_empty_df(self) -> None:
        self.data.add_df(pd.DataFrame())
        self.assertEqual(
            {"data": {}},
            self.data.build(),
        )

    def test_add_df_with_df(self) -> None:
        df = self.in_pd_df_by_series_with_duplicated_popularity
        self.data.add_df(df)
        self.assertEqual(
            self.ref_pd_df_by_series_with_duplicated_popularity,
            self.data.build(),
        )

    def test_add_df_with_df_contains_na(self) -> None:
        df = self.in_pd_df_by_series_with_nan
        self.data.add_df(df)
        self.assertEqual(
            self.ref_pd_df_by_series_with_nan,
            self.data.build(),
        )

    def test_add_df_with_df_and_with_include_index(self) -> None:
        df = self.in_pd_df_by_series_with_index
        self.data.add_df(df, include_index="Index")
        self.assertEqual(
            self.ref_pd_df_by_series_with_index,
            self.data.build(),
        )

    def test_add_df_with_df_and_max_rows(self) -> None:
        df = self.in_pd_df_by_series
        self.data.add_df(df, max_rows=2)
        self.assertEqual(
            self.ref_pd_df_by_series_max_rows,
            self.data.build(),
        )


class TestDataFrame(DataWithAssets):
    def test_add_data_frame_with_none(self) -> None:
        self.data.add_data_frame(None)
        self.assertEqual(
            {"data": {}},
            self.data.build(),
        )

    def test_add_data_frame_with_empty_df(self) -> None:
        self.data.add_data_frame(pd.DataFrame())
        self.assertEqual(
            {"data": {}},
            self.data.build(),
        )

    def test_add_data_frame_with_df(self) -> None:
        df = self.in_pd_df_by_series_with_duplicated_popularity
        self.data.add_data_frame(df)
        self.assertEqual(
            self.ref_pd_df_by_series_with_duplicated_popularity,
            self.data.build(),
        )

    def test_add_data_frame_with_df_contains_na(self) -> None:
        df = self.in_pd_df_by_series_with_nan
        self.data.add_data_frame(df)
        self.assertEqual(
            self.ref_pd_df_by_series_with_nan,
            self.data.build(),
        )


class TestDfWithSeries(DataWithAssets):
    def test_add_df_with_empty_series(self) -> None:
        self.data.add_df(pd.Series())
        self.assertEqual(
            {"data": {}},
            self.data.build(),
        )

    def test_add_df_with_series(self) -> None:
        self.data.add_df(self.in_pd_series_dimension)
        self.data.add_df(self.in_pd_series_measure)
        self.assertEqual(
            self.ref_pd_series,
            self.data.build(),
        )

    def test_add_df_with_series_contains_na(self) -> None:
        self.data.add_df(self.in_pd_series_dimension_with_nan)
        self.data.add_df(self.in_pd_series_measure_with_nan)
        self.assertEqual(
            self.ref_pd_series_with_nan,
            self.data.build(),
        )

    def test_add_df_with_series_and_with_include_index(self) -> None:
        self.data.add_df(
            self.in_pd_series_dimension_with_index,
            include_index="DimensionIndex",
        )
        self.data.add_df(
            self.in_pd_series_measure_with_index,
            include_index="MeasureIndex",
        )
        self.assertEqual(
            self.ref_pd_series_with_index,
            self.data.build(),
        )


class TestDataFrameWithSeries(DataWithAssets):
    def test_add_data_frame_with_empty_series(self) -> None:
        self.data.add_data_frame(pd.Series())
        self.assertEqual(
            {"data": {}},
            self.data.build(),
        )

    def test_add_data_frame_with_series(self) -> None:
        self.data.add_data_frame(self.in_pd_series_dimension)
        self.data.add_data_frame(self.in_pd_series_measure)
        self.assertEqual(
            self.ref_pd_series,
            self.data.build(),
        )

    def test_add_data_frame_with_series_contains_na(self) -> None:
        self.data.add_data_frame(self.in_pd_series_dimension_with_nan)
        self.data.add_data_frame(self.in_pd_series_measure_with_nan)
        self.assertEqual(
            self.ref_pd_series_with_nan,
            self.data.build(),
        )


class TestDfIndex(DataWithAssets):
    def test_add_df_index_with_none(self) -> None:
        self.data.add_df_index(None, column_name="Index")
        self.assertEqual(
            {"data": {}},
            self.data.build(),
        )

    def test_add_df_index_with_df(self) -> None:
        df = self.in_pd_df_by_series_with_index
        self.data.add_df_index(df, column_name="Index")
        self.assertEqual(
            self.ref_pd_df_by_series_only_index,
            self.data.build(),
        )

    def test_add_df_index_with_df_and_max_rows(self) -> None:
        df = self.in_pd_df_by_series_with_index
        self.data.add_df_index(df, max_rows=2)
        self.assertEqual(
            self.ref_pd_df_by_series_only_index_max_rows,
            self.data.build(),
        )


class TestDataFrameIndex(DataWithAssets):
    def test_add_data_frame_index_with_none(self) -> None:
        self.data.add_data_frame_index(None, name="Index")
        self.assertEqual(
            {"data": {}},
            self.data.build(),
        )

    def test_add_data_frame_index_with_df(self) -> None:
        df = self.in_pd_df_by_series_with_index
        self.data.add_data_frame_index(df, name="Index")
        self.assertEqual(
            self.ref_pd_df_by_series_only_index,
            self.data.build(),
        )


class TestDfIndexWithSeries(DataWithAssets):
    def test_add_df_index_with_series(self) -> None:
        self.data.add_df_index(
            self.in_pd_series_dimension_with_index,
            column_name="DimensionIndex",
        )
        self.data.add_df_index(
            self.in_pd_series_measure_with_index,
            column_name="MeasureIndex",
        )
        self.assertEqual(
            self.ref_pd_series_only_index,
            self.data.build(),
        )


class TestDataFrameIndexWithSeries(DataWithAssets):
    def test_add_data_frame_index_with_series(self) -> None:
        self.data.add_data_frame_index(
            self.in_pd_series_dimension_with_index,
            name="DimensionIndex",
        )
        self.data.add_data_frame_index(
            self.in_pd_series_measure_with_index,
            name="MeasureIndex",
        )
        self.assertEqual(
            self.ref_pd_series_only_index,
            self.data.build(),
        )
