import json
import pathlib
import unittest
import jsonschema
import pandas as pd

from ipyvizzu import (
    PlainAnimation,
    Data,
    Config,
    Style,
    Snapshot,
    AnimationMerger,
)


class TestPlainAnimation(unittest.TestCase):
    def test_plainanimation(self):
        animation = PlainAnimation(geometry="circle")
        self.assertEqual({"geometry": "circle"}, animation.build())


class TestDataClassMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.asset_dir = pathlib.Path(__file__).parent / "assets"

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
        data = Data.from_json(self.asset_dir / "data_from_json.json")
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
    @classmethod
    def setUpClass(cls):
        cls.asset_dir = pathlib.Path(__file__).parent / "assets"

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

    def test_data_cube(self):
        self.data.add_dimension("Genres", ["Pop", "Rock"])
        self.data.add_dimension("Types", ["Hard"])
        self.data.add_measure("Popularity", [[114, 96]])
        self.assertEqual(
            {
                "data": {
                    "dimensions": [
                        {"name": "Genres", "values": ["Pop", "Rock"]},
                        {"name": "Types", "values": ["Hard"]},
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

    def test_data_frame_with_not_df(self):
        data = Data()
        with self.assertRaises(TypeError):
            data.add_data_frame("not_data_frame", None)

    def test_data_frame_with_none(self):
        data = Data()
        data.add_data_frame(None)
        self.assertEqual(
            {"data": {}},
            data.build(),
        )

    def test_data_frame(self):
        with open(self.asset_dir / "data_frame_in.json", encoding="UTF-8") as fh_in:
            fc_in = json.load(fh_in)
        with open(self.asset_dir / "data_frame_out.json", encoding="UTF-8") as fh_out:
            fc_out = json.load(fh_out)

        data_frame = pd.DataFrame(fc_in)
        data_frame = data_frame.astype({"PopularityAsDimension": str})
        self.data.add_data_frame(data_frame)
        self.assertEqual(
            fc_out,
            self.data.build(),
        )

    def test_data_frame_na(self):
        data_frame = pd.read_csv(
            self.asset_dir / "data_frame_na.csv", dtype={"PopularityAsDimension": str}
        )
        self.data.add_data_frame(data_frame)
        self.assertEqual(
            {
                "data": {
                    "series": [
                        {
                            "name": "Popularity",
                            "type": "measure",
                            "values": [100.0, 0.0],
                        },
                        {
                            "name": "PopularityAsDimension",
                            "type": "dimension",
                            "values": ["", "100"],
                        },
                    ]
                }
            },
            self.data.build(),
        )

    def test_data_frame_with_pd_series(self):
        data = Data()
        data.add_data_frame(pd.Series([1, 2], name="series1"))
        data.add_data_frame(
            pd.Series({"x": 3, "y": 4, "z": 5}, index=["x", "y"], name="series2")
        )
        self.assertEqual(
            {
                "data": {
                    "series": [
                        {"name": "series1", "type": "measure", "values": [1.0, 2.0]},
                        {"name": "series2", "type": "measure", "values": [3.0, 4.0]},
                    ]
                }
            },
            data.build(),
        )

    def test_data_frame_index_with_not_df(self):
        data = Data()
        with self.assertRaises(TypeError):
            data.add_data_frame_index("not_data_frame", None)

    def test_data_frame_index_with_none_and_none(self):
        data = Data()
        data.add_data_frame_index(None, None)
        self.assertEqual(
            {"data": {}},
            data.build(),
        )

    def test_data_frame_index_with_df_and_none(self):
        data = Data()
        data_frame = pd.DataFrame(
            pd.Series({"x": 1, "y": 2, "z": 3}, index=["x", "y"], name="series")
        )
        data.add_data_frame_index(data_frame, None)
        data.add_data_frame(data_frame)
        self.assertEqual(
            {
                "data": {
                    "series": [
                        {"name": "None", "type": "dimension", "values": ["x", "y"]},
                        {"name": "series", "type": "measure", "values": [1.0, 2.0]},
                    ]
                }
            },
            data.build(),
        )

    def test_data_frame_index_with_df_and_name(self):
        data = Data()
        data_frame = pd.DataFrame({"series": [1, 2, 3]}, index=["x", "y", "z"])
        data.add_data_frame_index(data_frame, "Index")
        data.add_data_frame(data_frame)
        self.assertEqual(
            {
                "data": {
                    "series": [
                        {
                            "name": "Index",
                            "type": "dimension",
                            "values": ["x", "y", "z"],
                        },
                        {
                            "name": "series",
                            "type": "measure",
                            "values": [1.0, 2.0, 3.0],
                        },
                    ]
                }
            },
            data.build(),
        )

    def test_data_frame_index_with_pd_series(self):
        data = Data()
        data_frame = pd.Series(
            {"x": 1, "y": 2, "z": 3}, index=["x", "y"], name="series"
        )
        data.add_data_frame_index(data_frame, "Index")
        data.add_data_frame(data_frame)
        self.assertEqual(
            {
                "data": {
                    "series": [
                        {"name": "Index", "type": "dimension", "values": ["x", "y"]},
                        {"name": "series", "type": "measure", "values": [1.0, 2.0]},
                    ]
                }
            },
            data.build(),
        )


class TestDataSchema(unittest.TestCase):
    def setUp(self):
        self.data = Data()

    def test_schema_dimension_only(self):
        self.data.add_dimension("Genres", ["Pop", "Rock"])
        with self.assertRaises(jsonschema.ValidationError):
            self.data.build()

    def test_schema_measure_only(self):
        self.data.add_measure("Popularity", [[114, 96]])
        with self.assertRaises(jsonschema.ValidationError):
            self.data.build()

    def test_schema_data_cube_and_series(self):
        self.data.add_dimension("Genres", ["Pop", "Rock"])
        self.data.add_measure("Popularity", [[114, 96]])
        self.data.add_series("Types", ["Hard"])
        with self.assertRaises(jsonschema.ValidationError):
            self.data.build()

    def test_schema_data_cube_and_records(self):
        self.data.add_dimension("Genres", ["Pop", "Rock"])
        self.data.add_measure("Popularity", [[114, 96]])
        self.data.add_records([["Rock", "Hard", 96], ["Pop", "Hard", 114]])
        with self.assertRaises(jsonschema.ValidationError):
            self.data.build()


class TestConfig(unittest.TestCase):
    def test_config(self):
        animation = Config({"color": {"set": ["Genres"]}})
        self.assertEqual({"config": {"color": {"set": ["Genres"]}}}, animation.build())


class TestStyle(unittest.TestCase):
    def test_style(self):
        animation = Style({"title": {"backgroundColor": "#A0A0A0"}})
        self.assertEqual(
            {"style": {"title": {"backgroundColor": "#A0A0A0"}}}, animation.build()
        )

    def test_style_can_be_none(self):
        animation = Style(None)
        self.assertEqual({"style": None}, animation.build())


class TestSnapshot(unittest.TestCase):
    def test_snapshot(self):
        animation = Snapshot("abc1234")
        self.assertEqual("window.ipyvizzu.stored(element, 'abc1234')", animation.dump())

    def test_snapshot_can_not_be_built(self):
        animation = Snapshot("abc1234")
        self.assertRaises(NotImplementedError, animation.build)


class TestMerger(unittest.TestCase):
    def setUp(self):
        self.merger = AnimationMerger()

        self.data = Data()
        self.data.add_record(["Rock", "Hard", 96])

        self.config = Config({"channels": {"label": {"attach": ["Popularity"]}}})

    def test_merge(self):
        self.merger.merge(self.data)
        self.merger.merge(self.config)
        self.merger.merge(Style({"title": {"backgroundColor": "#A0A0A0"}}))
        self.assertEqual(
            json.dumps(
                {
                    "data": {"records": [["Rock", "Hard", 96]]},
                    "config": {"channels": {"label": {"attach": ["Popularity"]}}},
                    "style": {"title": {"backgroundColor": "#A0A0A0"}},
                }
            ),
            self.merger.dump(),
        )

    def test_merge_none(self):
        self.merger.merge(self.config)
        self.merger.merge(Style(None))
        self.assertEqual(
            '{"config": {"channels": {"label": {"attach": ["Popularity"]}}}, "style": null}',
            self.merger.dump(),
        )

    def test_snapshot_can_not_be_merged(self):
        self.merger.merge(self.data)
        self.merger.merge(self.config)
        self.merger.merge(Style({"title": {"backgroundColor": "#A0A0A0"}}))
        self.assertRaises(NotImplementedError, self.merger.merge, Snapshot("abc1234"))

    def test_only_different_animations_can_be_merged(self):
        self.merger.merge(self.data)
        self.merger.merge(self.config)
        self.merger.merge(Style({"title": {"backgroundColor": "#A0A0A0"}}))

        data = Data()
        data.add_record(["Pop", "Hard", 114])

        self.assertRaises(ValueError, self.merger.merge, data)
        self.assertRaises(ValueError, self.merger.merge, Config({"title": "Test"}))
        self.assertRaises(ValueError, self.merger.merge, Style(None))
