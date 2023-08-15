# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import unittest

from ipyvizzu import Data


class TestDataRecords(unittest.TestCase):
    def setUp(self) -> None:
        self.data = Data()

    def test_record_list(self) -> None:
        self.data.add_record(["Rock", "Hard", 96])
        self.data.add_record(["Pop", "Hard", 114])
        self.assertEqual(
            {"data": {"records": [["Rock", "Hard", 96], ["Pop", "Hard", 114]]}},
            self.data.build(),
        )

    def test_record_dict(self) -> None:
        self.data.add_record({"Genres": "Rock", "Kinds": "Hard", "Popularity": 96})
        self.data.add_record({"Genres": "Pop", "Kinds": "Hard", "Popularity": 114})
        self.assertEqual(
            {
                "data": {
                    "records": [
                        {"Genres": "Rock", "Kinds": "Hard", "Popularity": 96},
                        {"Genres": "Pop", "Kinds": "Hard", "Popularity": 114},
                    ]
                }
            },
            self.data.build(),
        )

    def test_records(self) -> None:
        self.data.add_records([["Rock", "Hard", 96], ["Pop", "Hard", 114]])
        self.assertEqual(
            {"data": {"records": [["Rock", "Hard", 96], ["Pop", "Hard", 114]]}},
            self.data.build(),
        )
