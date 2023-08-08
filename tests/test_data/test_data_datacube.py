# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import unittest

from ipyvizzu import Data


class TestDataDataCube(unittest.TestCase):
    def setUp(self) -> None:
        self.data = Data()

    def test_data_cube(self) -> None:
        self.data.add_dimension("Genres", ["Pop", "Rock"])
        self.data.add_dimension("Kinds", ["Hard"])
        self.data.add_measure("Popularity", [[114, 96]])
        self.assertEqual(
            {
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
            },
            self.data.build(),
        )
