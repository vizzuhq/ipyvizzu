# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import unittest

import numpy as np

from ipyvizzu import Data

from tests.utils.import_modifiers import RaiseImportError


class TestDataNpArray(unittest.TestCase):
    def setUp(self) -> None:
        self.data = Data()

    def test_add_np_array_if_numpy_not_installed(self) -> None:
        with RaiseImportError.module_name("numpy"):
            with self.assertRaises(ImportError):
                self.data.add_np_array(np.empty(()))

    def test_add_np_array_none(self) -> None:
        self.data.add_np_array(None)
        self.assertEqual(
            {"data": {}},
            self.data.build(),
        )

    def test_add_np_array_empty(self) -> None:
        np_array = np.empty([])
        self.data.add_np_array(np_array)
        self.assertEqual(
            {"data": {}},
            self.data.build(),
        )

    def test_add_np_array1dim(self) -> None:
        np_array = np.array([127, 128, 129])
        self.data.add_np_array(np_array)
        self.assertEqual(
            {
                "data": {
                    "series": [
                        {"name": "0", "type": "measure", "values": [127, 128, 129]},
                    ]
                }
            },
            self.data.build(),
        )

    def test_add_np_array1dim_with_str_value(self) -> None:
        np_array = np.array([127, "128", 129])
        self.data.add_np_array(np_array)
        self.assertEqual(
            {
                "data": {
                    "series": [
                        {
                            "name": "0",
                            "type": "dimension",
                            "values": ["127", "128", "129"],
                        },
                    ]
                }
            },
            self.data.build(),
        )

    def test_add_np_array1dim_with_str_and_na_value_and_column_name_and_dtype(
        self,
    ) -> None:
        np_array = np.array([127, "128", np.nan])
        self.data.add_np_array(np_array, column_name="First", column_dtype=int)
        self.assertEqual(
            {
                "data": {
                    "series": [
                        {
                            "name": "First",
                            "type": "measure",
                            "values": [127, 128, 0],
                        },
                    ]
                }
            },
            self.data.build(),
        )

    def test_add_np_array2dim(self) -> None:
        np_array = np.array([[127, 128, 129], [255, 256, 257], [511, 512, 513]])
        self.data.add_np_array(np_array)
        self.assertEqual(
            {
                "data": {
                    "series": [
                        {"name": "0", "type": "measure", "values": [127, 255, 511]},
                        {"name": "1", "type": "measure", "values": [128, 256, 512]},
                        {"name": "2", "type": "measure", "values": [129, 257, 513]},
                    ]
                }
            },
            self.data.build(),
        )

    def test_add_np_array2dim_with_str_and_na_value_and_column_name_and_dtype(
        self,
    ) -> None:
        np_array = np.array([[127, "128", 129], [255, np.nan, 257], [511, 512, 513]])
        self.data.add_np_array(
            np_array, column_name={0: "First"}, column_dtype={2: int}
        )
        self.assertEqual(
            {
                "data": {
                    "series": [
                        {
                            "name": "First",
                            "type": "dimension",
                            "values": ["127", "255", "511"],
                        },
                        {
                            "name": "1",
                            "type": "dimension",
                            "values": ["128", "", "512"],
                        },
                        {
                            "name": "2",
                            "type": "measure",
                            "values": [129, 257, 513],
                        },
                    ]
                }
            },
            self.data.build(),
        )

    def test_add_np_array2dim_with_non_dict_column_name(self) -> None:
        np_array = np.zeros((2, 2))
        with self.assertRaises(ValueError):
            self.data.add_np_array(np_array, column_name="First")

    def test_add_np_array2dim_with_non_dict_column_dtype(self) -> None:
        np_array = np.zeros((2, 2))
        with self.assertRaises(ValueError):
            self.data.add_np_array(np_array, column_dtype=str)

    def test_add_np_array3dim(self) -> None:
        np_array = np.zeros((3, 3, 3))
        with self.assertRaises(ValueError):
            self.data.add_np_array(np_array)
