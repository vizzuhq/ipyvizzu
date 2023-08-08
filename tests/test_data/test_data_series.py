# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from typing import List
import unittest

from ipyvizzu.data.type_alias import Record

from ipyvizzu import Data


class TestDataSeries(unittest.TestCase):
    def setUp(self) -> None:
        self.data = Data()

    def test_series(self) -> None:
        self.data.add_series("Genres", ["Rock", "Pop"], type="dimension")
        self.data.add_series("Kinds", ["Hard"])
        self.data.add_series("Popularity", [96, 114], type="measure")
        self.assertEqual(
            {
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
            },
            self.data.build(),
        )

    def test_series_without_values(self) -> None:
        self.data.add_series("Genres", type="dimension")
        self.data.add_series("Kinds", type="dimension")
        self.data.add_series("Popularity", type="measure")
        records: List[Record] = [["Rock", "Hard", 96], ["Pop", "Hard", 114]]
        self.data.add_records(records)
        self.assertEqual(
            {
                "data": {
                    "records": [["Rock", "Hard", 96], ["Pop", "Hard", 114]],
                    "series": [
                        {"name": "Genres", "type": "dimension"},
                        {"name": "Kinds", "type": "dimension"},
                        {"name": "Popularity", "type": "measure"},
                    ],
                }
            },
            self.data.build(),
        )
