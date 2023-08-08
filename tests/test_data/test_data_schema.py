# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import unittest

import jsonschema  # type: ignore

from ipyvizzu import Data


class TestDataSchema(unittest.TestCase):
    def setUp(self) -> None:
        self.data = Data()

    def test_schema_dimension_only(self) -> None:
        self.data.add_dimension("Genres", ["Pop", "Rock"])
        with self.assertRaises(jsonschema.ValidationError):
            self.data.build()

    def test_schema_measure_only(self) -> None:
        self.data.add_measure("Popularity", [[114, 96]])
        with self.assertRaises(jsonschema.ValidationError):
            self.data.build()

    def test_schema_data_cube_and_series(self) -> None:
        self.data.add_dimension("Genres", ["Pop", "Rock"])
        self.data.add_measure("Popularity", [[114, 96]])
        self.data.add_series("Kinds", ["Hard"])
        with self.assertRaises(jsonschema.ValidationError):
            self.data.build()

    def test_schema_data_cube_and_records(self) -> None:
        self.data.add_dimension("Genres", ["Pop", "Rock"])
        self.data.add_measure("Popularity", [[114, 96]])
        self.data.add_records([["Rock", "Hard", 96], ["Pop", "Hard", 114]])
        with self.assertRaises(jsonschema.ValidationError):
            self.data.build()
