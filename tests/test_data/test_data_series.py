# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import copy
from typing import List
import unittest

from ipyvizzu.data.type_alias import Record

from ipyvizzu import Data


class TestDataSeries(unittest.TestCase):
    ref = {
        "data": {
            "series": [
                {
                    "name": "Genres",
                    "type": "dimension",
                    "values": ["Rock", "Pop"],
                },
                {"name": "Kinds", "values": ["Hard"]},
                {"name": "Popularity", "type": "measure", "values": [96, 114]},
            ]
        }
    }

    def setUp(self) -> None:
        self.data = Data()
        self.data.add_series("Genres", ["Rock", "Pop"], type="dimension")
        self.data.add_series("Kinds", ["Hard"])

    def test_series(self) -> None:
        self.data.add_series("Popularity", [96, 114], type="measure")
        self.assertEqual(
            TestDataSeries.ref,
            self.data.build(),
        )

    def test_series_with_unit(self) -> None:
        self.data.add_series("Popularity", [96, 114], type="measure", unit="songs")
        ref = copy.deepcopy(TestDataSeries.ref)
        ref["data"]["series"][-1]["unit"] = "songs"  # type: ignore
        self.assertEqual(
            ref,
            self.data.build(),
        )


class TestDataSeriesWithoutValues(unittest.TestCase):
    ref = {
        "data": {
            "records": [["Rock", "Hard", 96], ["Pop", "Hard", 114]],
            "series": [
                {"name": "Genres", "type": "dimension"},
                {"name": "Kinds", "type": "dimension"},
                {"name": "Popularity", "type": "measure"},
            ],
        }
    }

    def setUp(self) -> None:
        self.data = Data()
        self.data.add_series("Genres", type="dimension")
        self.data.add_series("Kinds", type="dimension")

    def test_series(self) -> None:
        self.data.add_series("Popularity", type="measure")
        records: List[Record] = [["Rock", "Hard", 96], ["Pop", "Hard", 114]]
        self.data.add_records(records)
        self.assertEqual(
            TestDataSeriesWithoutValues.ref,
            self.data.build(),
        )

    def test_series_with_unit(self) -> None:
        self.data.add_series("Popularity", type="measure", unit="songs")
        records: List[Record] = [["Rock", "Hard", 96], ["Pop", "Hard", 114]]
        self.data.add_records(records)
        ref = copy.deepcopy(TestDataSeriesWithoutValues.ref)
        ref["data"]["series"][-1]["unit"] = "songs"  # type: ignore
        self.assertEqual(
            ref,
            self.data.build(),
        )
