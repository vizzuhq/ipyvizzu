"""A module for testing the documentation site snippets."""


import json
import pathlib
import unittest
import pandas as pd  # type: ignore

from tests import Data


class TestData(unittest.TestCase):
    """
    A class for testing Data class.
    """

    asset_dir: pathlib.Path
    doc_dir: pathlib.Path

    @classmethod
    def setUpClass(cls) -> None:
        cls.asset_dir = pathlib.Path(__file__).parent / "assets"
        cls.doc_dir = pathlib.Path(__file__).parent.parent / "docs" / "assets" / "data"

    def setUp(self) -> None:
        self.data = Data()

    def test_data_frame_with_csv(self) -> None:
        """
        A method for testing Data.add_data_frame method.
        It tests with a csv.

        Raises:
            AssertionError: If the built value is not correct.
        """

        with open(self.asset_dir / "data_frame_out.json", encoding="UTF-8") as fh_out:
            fc_out = json.load(fh_out)
            fc_out["data"]["series"] = fc_out["data"]["series"][:-1]

        data_frame = pd.read_csv(self.doc_dir / "music_data.csv")

        data = Data()
        data.add_data_frame(data_frame)
        self.assertEqual(
            fc_out,
            data.build(),
        )

    def test_data_frame_with_xlsx(self) -> None:
        """
        A method for testing Data.add_data_frame method.
        It tests with an xlsx.

        Raises:
            AssertionError: If the built value is not correct.
        """

        with open(self.asset_dir / "data_frame_out.json", encoding="UTF-8") as fh_out:
            fc_out = json.load(fh_out)
            fc_out["data"]["series"] = fc_out["data"]["series"][:-1]

        data_frame = pd.read_excel(self.doc_dir / "music_data.xlsx")

        data = Data()
        data.add_data_frame(data_frame)
        self.assertEqual(
            fc_out,
            data.build(),
        )

    def test_data_frame_with_googlesheet(self) -> None:
        """
        A method for testing Data.add_data_frame method.
        It tests with Google Sheets.

        Raises:
            AssertionError: If the built value is not correct.
        """

        with open(self.asset_dir / "data_frame_out.json", encoding="UTF-8") as fh_out:
            fc_out = json.load(fh_out)
            fc_out["data"]["series"] = fc_out["data"]["series"][:-1]

        base_url = "https://docs.google.com/spreadsheets/d"
        sheet_id = "1WS56qHl9lDK6gjUSfbEVHRmF9mvud1js5SQDcb-mtQs"
        sheet_name = "sheet1"
        data_frame = pd.read_csv(
            f"{base_url}/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
        )

        data = Data()
        data.add_data_frame(data_frame)
        self.assertEqual(
            fc_out,
            data.build(),
        )
