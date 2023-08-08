# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from pathlib import Path
import sys
import unittest

import numpy as np
import pandas as pd

from tests.test_data import DataWithAssets


class TestDf(DataWithAssets):
    docs_dir: Path

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.docs_dir = (
            Path(__file__).parent.parent.parent.parent / "docs" / "assets" / "data"
        )

    def test_add_df_with_csv(self) -> None:
        df = pd.read_csv(self.docs_dir / "music_data.csv")
        self.data.add_df(df)
        self.assertEqual(
            self.ref_pd_df_by_series,
            self.data.build(),
        )

    # TODO: remove decorator once support for Python 3.6 is dropped
    @unittest.skipUnless(sys.version_info >= (3, 7), "at least Python 3.7 is required")
    def test_add_df_with_xlsx(self) -> None:
        df = pd.read_excel(self.docs_dir / "music_data.xlsx")
        self.data.add_df(df)
        self.assertEqual(
            self.ref_pd_df_by_series,
            self.data.build(),
        )

    def test_add_df_with_googlesheet(self) -> None:
        base_url = "https://docs.google.com/spreadsheets/d"
        sheet_id = "1WS56qHl9lDK6gjUSfbEVHRmF9mvud1js5SQDcb-mtQs"
        sheet_name = "sheet1"
        df = pd.read_csv(
            f"{base_url}/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
        )
        self.data.add_df(df)
        self.assertEqual(
            self.ref_pd_df_by_series,
            self.data.build(),
        )


class TestNpArray(DataWithAssets):
    def test_add_np_array(self) -> None:
        numpy_array = np.array(
            [
                ["Pop", "Hard", 114],
                ["Rock", "Hard", 96],
                ["Jazz", "Hard", 78],
                ["Metal", "Hard", 52],
                ["Pop", "Smooth", 56],
                ["Rock", "Experimental", 36],
                ["Jazz", "Smooth", 174],
                ["Metal", "Smooth", 121],
                ["Pop", "Experimental", 127],
                ["Rock", "Experimental", 83],
                ["Jazz", "Experimental", 94],
                ["Metal", "Experimental", 58],
            ]
        )
        self.data.add_np_array(
            numpy_array,
            column_name={0: "Genres", 1: "Kinds", 2: "Popularity"},
            column_dtype={2: int},
        )
        self.assertEqual(
            self.ref_pd_df_by_series,
            self.data.build(),
        )
