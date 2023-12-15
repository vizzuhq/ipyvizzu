# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import copy
import unittest

from ipyvizzu import Data


class TestDataDataCube(unittest.TestCase):
    ref = {
        "data": {
            "dimensions": [
                {"name": "Genres", "values": ["Pop", "Rock"]},
                {"name": "Kinds", "values": ["Hard"]},
            ],
            "measures": [
                {
                    "name": "Popularity",
                    "values": [[114, 96]],
                }
            ],
        }
    }

    def setUp(self) -> None:
        self.data = Data()

    def test_data_cube(self) -> None:
        self.data.add_dimension("Genres", ["Pop", "Rock"])
        self.data.add_dimension("Kinds", ["Hard"])
        self.data.add_measure("Popularity", [[114, 96]])
        self.assertEqual(
            TestDataDataCube.ref,
            self.data.build(),
        )

    def test_data_cube_with_unit(self) -> None:
        self.data.add_dimension("Genres", ["Pop", "Rock"])
        self.data.add_dimension("Kinds", ["Hard"])
        self.data.add_measure("Popularity", [[114, 96]], unit="songs")
        ref = copy.deepcopy(TestDataDataCube.ref)
        ref["data"]["measures"][-1]["unit"] = "songs"  # type: ignore
        self.assertEqual(
            ref,
            self.data.build(),
        )
