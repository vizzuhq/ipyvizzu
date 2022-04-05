import json
import pathlib
import unittest
import pandas as pd

from ipyvizzu.animation import Data


asset_dir = pathlib.Path(__file__).parent / "assets"


class TestDataClassMethods(unittest.TestCase):
    def test_filter(self):
        data = Data.filter("filter_expr")
        # instead of build() test with dump() because contains raw js
        self.assertEqual(
            '{"data": {"filter": record => { return (filter_expr) }}}',
            data.dump(),
        )

    def test_filter_can_be_none(self):
        data = Data.filter(None)
        # instead of build() test with dump() because contains raw js
        self.assertEqual(
            '{"data": {"filter": null}}',
            data.dump(),
        )

    def test_from_json(self):
        data = Data.from_json(asset_dir / "data_from_json.json")
        self.assertEqual(
            {
                "data": {
                    "dimensions": [
                        {"name": "Genres", "values": ["Rock", "Pop"]},
                        {"name": "Types", "values": ["Hard"]},
                    ],
                    "measures": [{"name": "Popularity", "values": [[114, 96]]}],
                }
            },
            data.build(),
        )


class TestData(unittest.TestCase):
    def setUp(self):
        self.data = Data()

    def test_set_filter(self):
        self.data.add_records([["Rock", "Hard", 96], ["Pop", "Hard", 114]])
        self.data.set_filter("filter_expr")
        self.assertEqual(
            '{"data": {"records": [["Rock", "Hard", 96], ["Pop", "Hard", 114]], "filter": record => { return (filter_expr) }}}',  # pylint: disable=line-too-long
            self.data.dump(),
        )

    def test_set_filter_can_be_none(self):
        self.data.add_records([["Rock", "Hard", 96], ["Pop", "Hard", 114]])
        self.data.set_filter(None)
        self.assertEqual(
            '{"data": {"records": [["Rock", "Hard", 96], ["Pop", "Hard", 114]], "filter": null}}',
            self.data.dump(),
        )

    def test_record(self):
        self.data.add_record(["Rock", "Hard", 96])
        self.data.add_record(["Pop", "Hard", 114])
        self.assertEqual(
            {"data": {"records": [["Rock", "Hard", 96], ["Pop", "Hard", 114]]}},
            self.data.build(),
        )

    def test_records(self):
        self.data.add_records([["Rock", "Hard", 96], ["Pop", "Hard", 114]])
        self.assertEqual(
            {"data": {"records": [["Rock", "Hard", 96], ["Pop", "Hard", 114]]}},
            self.data.build(),
        )

    def test_series(self):
        self.data.add_series("Genres", ["Rock", "Pop"], type="dimension")
        self.data.add_series("Types", ["Hard"])
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
                        {"name": "Types", "values": ["Hard"]},
                        {"name": "Popularity", "type": "measure", "values": [96, 114]},
                    ]
                }
            },
            self.data.build(),
        )

    def test_dimension(self):
        self.data.add_dimension("Genres", ["Pop", "Rock"])
        self.data.add_dimension("Types", ["Hard"])
        self.assertEqual(
            {
                "data": {
                    "dimensions": [
                        {"name": "Genres", "values": ["Pop", "Rock"]},
                        {"name": "Types", "values": ["Hard"]},
                    ]
                }
            },
            self.data.build(),
        )

    def test_mesure(self):
        self.data.add_measure("Popularity", [[114, 96]])
        self.assertEqual(
            {
                "data": {
                    "measures": [
                        {
                            "name": "Popularity",
                            "values": [[114, 96]],
                        }
                    ]
                }
            },
            self.data.build(),
        )

    def test_data_frame(self):
        with open(asset_dir / "data_frame_in.json", encoding="UTF-8") as fh_in:
            fc_in = json.load(fh_in)
        with open(asset_dir / "data_frame_out.json", encoding="UTF-8") as fh_out:
            fc_out = json.load(fh_out)

        data_frame = pd.DataFrame(fc_in)

        self.data.add_data_frame(data_frame, {"PopularityD": "dimension"})
        self.assertEqual(
            fc_out,
            self.data.build(),
        )
