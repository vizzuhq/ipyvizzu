# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import copy
import json
from pathlib import Path
import unittest

import pandas as pd

from ipyvizzu import Data


class DataWithAssets(unittest.TestCase):
    asset_dir: Path

    in_pd_df_by_series: pd.DataFrame
    ref_pd_df_by_series: dict
    in_pd_df_by_series_with_duplicated_popularity: pd.DataFrame
    ref_pd_df_by_series_with_duplicated_popularity: dict
    in_pd_df_by_series_with_nan: pd.DataFrame
    ref_pd_df_by_series_with_nan: dict
    in_pd_df_by_series_with_index: pd.DataFrame
    ref_pd_df_by_series_with_index: dict
    ref_pd_df_by_series_only_index: dict
    ref_pd_df_by_series_only_index_max_rows: dict
    ref_pd_df_by_series_max_rows: dict

    in_pd_series_dimension: pd.Series
    in_pd_series_measure: pd.Series
    ref_pd_series: dict
    in_pd_series_dimension_with_nan: pd.Series
    in_pd_series_measure_with_nan: pd.Series
    ref_pd_series_with_nan: dict
    in_pd_series_dimension_with_index: pd.Series
    in_pd_series_measure_with_index: pd.Series
    ref_pd_series_with_index: dict
    ref_pd_series_only_index: dict

    def setUp(self) -> None:
        self.data = Data()

    @classmethod
    def setUpClass(cls) -> None:
        cls.asset_dir = Path(__file__).parent.parent / "assets"
        cls.set_up_pd_df()
        cls.set_up_pd_series()

    @classmethod
    def set_up_pd_df(cls) -> None:
        with open(cls.asset_dir / "in_pd_df_by_series.json", encoding="utf8") as fh_in:
            in_pd_df_by_series = json.load(fh_in)
            cls.in_pd_df_by_series = pd.DataFrame(in_pd_df_by_series)

            in_pd_df_by_series_with_duplicated_popularity = in_pd_df_by_series
            in_pd_df_by_series_with_duplicated_popularity[
                "PopularityAsDimension"
            ] = in_pd_df_by_series_with_duplicated_popularity["Popularity"]
            in_pd_df_by_series_with_duplicated_popularity = pd.DataFrame(
                in_pd_df_by_series_with_duplicated_popularity
            )
            cls.in_pd_df_by_series_with_duplicated_popularity = (
                in_pd_df_by_series_with_duplicated_popularity.astype(
                    {"PopularityAsDimension": str}
                )
            )

        with open(
            cls.asset_dir / "ref_pd_df_by_series_with_duplicated_popularity.json",
            encoding="utf8",
        ) as fh_in:
            cls.ref_pd_df_by_series_with_duplicated_popularity = json.load(fh_in)

            cls.ref_pd_df_by_series = copy.deepcopy(
                cls.ref_pd_df_by_series_with_duplicated_popularity
            )
            cls.ref_pd_df_by_series["data"]["series"] = cls.ref_pd_df_by_series["data"][
                "series"
            ][:-1]

        with open(
            cls.asset_dir / "ref_pd_df_by_series_max_rows.json", encoding="utf8"
        ) as fh_in:
            cls.ref_pd_df_by_series_max_rows = json.load(fh_in)

        with open(
            cls.asset_dir / "in_pd_df_by_series_with_nan.json", encoding="utf8"
        ) as fh_in:
            cls.in_pd_df_by_series_with_nan = pd.DataFrame(json.load(fh_in))

        with open(
            cls.asset_dir / "ref_pd_df_by_series_with_nan.json", encoding="utf8"
        ) as fh_in:
            cls.ref_pd_df_by_series_with_nan = json.load(fh_in)

        with open(
            cls.asset_dir / "in_pd_df_by_series_with_index.json", encoding="utf8"
        ) as fh_in:
            in_pd_df_by_series_with_index = pd.DataFrame(json.load(fh_in))
            cls.in_pd_df_by_series_with_index = in_pd_df_by_series_with_index.set_index(
                "Index"
            )

        with open(
            cls.asset_dir / "ref_pd_df_by_series_with_index.json", encoding="utf8"
        ) as fh_in:
            ref_pd_df_by_series_with_index = json.load(fh_in)

            cls.ref_pd_df_by_series_with_index = ref_pd_df_by_series_with_index
            cls.ref_pd_df_by_series_only_index = copy.deepcopy(
                ref_pd_df_by_series_with_index
            )
            cls.ref_pd_df_by_series_only_index["data"][
                "series"
            ] = cls.ref_pd_df_by_series_only_index["data"]["series"][:1]

            cls.ref_pd_df_by_series_only_index_max_rows = copy.deepcopy(
                cls.ref_pd_df_by_series_only_index
            )
            cls.ref_pd_df_by_series_only_index_max_rows["data"]["series"][0][
                "values"
            ] = [
                "111",
                "110",
            ]

    @classmethod
    def set_up_pd_series(cls) -> None:
        cls.in_pd_series_dimension = pd.Series(["1", "2"], name="DimensionSeries")
        cls.in_pd_series_measure = pd.Series([3, 4], name="MeasureSeries")

        with open(cls.asset_dir / "ref_pd_series.json", encoding="utf8") as fh_in:
            cls.ref_pd_series = json.load(fh_in)

        cls.in_pd_series_dimension_with_nan = pd.Series(
            ["1", None], name="DimensionSeries"
        )
        cls.in_pd_series_measure_with_nan = pd.Series([3, None], name="MeasureSeries")

        with open(
            cls.asset_dir / "ref_pd_series_with_nan.json", encoding="utf8"
        ) as fh_in:
            cls.ref_pd_series_with_nan = json.load(fh_in)

        cls.in_pd_series_dimension_with_index = pd.Series(
            {"x1": "1", "x2": "2", "x3": "3"},
            index=["x1", "x2"],
            name="DimensionSeries",
        )
        cls.in_pd_series_measure_with_index = pd.Series(
            {"y1": 3, "y2": 4, "y3": 5}, index=["y1", "y2"], name="MeasureSeries"
        )

        with open(
            cls.asset_dir / "ref_pd_series_with_index.json", encoding="utf8"
        ) as fh_in:
            cls.ref_pd_series_with_index = json.load(fh_in)

        with open(
            cls.asset_dir / "ref_pd_series_only_index.json", encoding="utf8"
        ) as fh_in:
            cls.ref_pd_series_only_index = json.load(fh_in)
