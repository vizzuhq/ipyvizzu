# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import json
import pathlib
from typing import List
import unittest

import jsonschema  # type: ignore
import pandas as pd

from ipyvizzu.data.typing_alias import Record

from tests import (
    PlainAnimation,
    Data,
    Config,
    Style,
    Keyframe,
    Snapshot,
    Animation,
    AnimationMerger,
)


class TestPlainAnimation(unittest.TestCase):
    def test_plainanimation(self) -> None:
        animation = PlainAnimation(geometry="circle")
        self.assertEqual({"geometry": "circle"}, animation.build())


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


class TestDataClassmethods(unittest.TestCase):
    asset_dir: pathlib.Path

    @classmethod
    def setUpClass(cls) -> None:
        cls.asset_dir = pathlib.Path(__file__).parent / "assets"

    def test_filter(self) -> None:
        data = Data.filter("filter_expr")
        # instead of build() test with dump() because contains raw js
        self.assertEqual(
            '{"data": {"filter": record => { return (filter_expr) }}}',
            data.dump(),
        )

    def test_filter_multiline(self) -> None:
        filter_expr = """
        A && 
            B ||
            C
        """
        data = Data.filter(filter_expr)
        # instead of build() test with dump() because contains raw js
        self.assertEqual(
            '{"data": {"filter": record => { return (A && B || C) }}}',
            data.dump(),
        )

    def test_filter_can_be_none(self) -> None:
        data = Data.filter(None)
        # instead of build() test with dump() because contains raw js
        self.assertEqual(
            '{"data": {"filter": null}}',
            data.dump(),
        )

    def test_from_json(self) -> None:
        data = Data.from_json(self.asset_dir / "data_from_json.json")
        self.assertEqual(
            {
                "data": {
                    "dimensions": [
                        {"name": "Genres", "values": ["Rock", "Pop"]},
                        {"name": "Kinds", "values": ["Hard"]},
                    ],
                    "measures": [{"name": "Popularity", "values": [[114, 96]]}],
                }
            },
            data.build(),
        )


class TestData(unittest.TestCase):
    def setUp(self) -> None:
        self.data = Data()

    def test_set_filter(self) -> None:
        self.data.add_records([["Rock", "Hard", 96], ["Pop", "Hard", 114]])
        self.data.set_filter("filter_expr")
        self.assertEqual(
            '{"data": {"records": '
            + '[["Rock", "Hard", 96], ["Pop", "Hard", 114]], '
            + '"filter": record => { return (filter_expr) }}}',
            self.data.dump(),
        )

    def test_set_filter_can_be_none(self) -> None:
        self.data.add_records([["Rock", "Hard", 96], ["Pop", "Hard", 114]])
        self.data.set_filter(None)
        self.assertEqual(
            '{"data": {"records": [["Rock", "Hard", 96], ["Pop", "Hard", 114]], "filter": null}}',
            self.data.dump(),
        )

    def test_record(self) -> None:
        self.data.add_record(["Rock", "Hard", 96])
        self.data.add_record(["Pop", "Hard", 114])
        self.assertEqual(
            {"data": {"records": [["Rock", "Hard", 96], ["Pop", "Hard", 114]]}},
            self.data.build(),
        )

    def test_records(self) -> None:
        self.data.add_records([["Rock", "Hard", 96], ["Pop", "Hard", 114]])
        self.assertEqual(
            {"data": {"records": [["Rock", "Hard", 96], ["Pop", "Hard", 114]]}},
            self.data.build(),
        )

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


class TestDataAddDf(unittest.TestCase):
    asset_dir: pathlib.Path

    @classmethod
    def setUpClass(cls) -> None:
        cls.asset_dir = pathlib.Path(__file__).parent / "assets"

    def setUp(self) -> None:
        self.data = Data()

    def test_add_df_with_not_df(self) -> None:
        data = Data()
        with self.assertRaises(TypeError):
            data.add_df("")

    def test_add_df_with_none(self) -> None:
        data = Data()
        data.add_df(None)
        self.assertEqual(
            {"data": {}},
            data.build(),
        )

    def test_add_df_with_df(self) -> None:
        with open(self.asset_dir / "df_in.json", encoding="utf8") as fh_in:
            fc_in = json.load(fh_in)
        with open(self.asset_dir / "df_out.json", encoding="utf8") as fh_out:
            fc_out = json.load(fh_out)

        df = pd.DataFrame(fc_in)
        df = df.astype({"PopularityAsDimension": str})
        self.data.add_df(df)
        self.assertEqual(
            fc_out,
            self.data.build(),
        )

    def test_add_df_with_df_contains_na(self) -> None:
        df = pd.read_csv(
            self.asset_dir / "df_na.csv", dtype={"PopularityAsDimension": str}
        )
        self.data.add_df(df)
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

    def test_add_df_with_series(self) -> None:
        data = Data()
        data.add_df(pd.Series([1, 2], name="series1"))
        data.add_df(
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

    def test_add_df_with_df_and_with_include_index(self) -> None:
        data = Data()
        df = pd.DataFrame({"series": [1, 2, 3]}, index=["x", "y", "z"])
        data.add_df(df, include_index="Index")
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

    def test_add_df_with_series_and_with_include_index(self) -> None:
        data = Data()
        df = pd.Series({"x": 1, "y": 2, "z": 3}, index=["x", "y"], name="series")
        data.add_df(df, include_index="Index")
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

    def test_add_df_index(self) -> None:
        data = Data()
        df = pd.Series({"x": 1, "y": 2, "z": 3}, index=["x", "y"], name="series")
        data.add_df_index(df, column_name="Index")
        data.add_df(df)
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

    def test_add_df_index_with_none(self) -> None:
        data = Data()
        df = pd.DataFrame()
        data.add_df_index(df, column_name="Index")
        data.add_df(df)
        self.assertEqual(
            {"data": {}},
            data.build(),
        )


class TestDataAddDataframe(unittest.TestCase):
    asset_dir: pathlib.Path

    @classmethod
    def setUpClass(cls) -> None:
        cls.asset_dir = pathlib.Path(__file__).parent / "assets"

    def setUp(self) -> None:
        self.data = Data()

    def test_add_data_frame_with_not_df(self) -> None:
        data = Data()
        with self.assertRaises(TypeError):
            data.add_data_frame("")

    def test_add_data_frame_with_none(self) -> None:
        data = Data()
        data.add_data_frame(None)
        self.assertEqual(
            {"data": {}},
            data.build(),
        )

    def test_add_data_frame_with_df(self) -> None:
        with open(self.asset_dir / "df_in.json", encoding="utf8") as fh_in:
            fc_in = json.load(fh_in)
        with open(self.asset_dir / "df_out.json", encoding="utf8") as fh_out:
            fc_out = json.load(fh_out)

        df = pd.DataFrame(fc_in)
        df = df.astype({"PopularityAsDimension": str})
        self.data.add_data_frame(df)
        self.assertEqual(
            fc_out,
            self.data.build(),
        )

    def test_add_data_frame_with_df_contains_na(self) -> None:
        df = pd.read_csv(
            self.asset_dir / "df_na.csv", dtype={"PopularityAsDimension": str}
        )
        self.data.add_data_frame(df)
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

    def test_add_data_frame_with_series(self) -> None:
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

    def test_add_data_frame_index(self) -> None:
        data = Data()
        df = pd.Series({"x": 1, "y": 2, "z": 3}, index=["x", "y"], name="series")
        data.add_data_frame_index(df, name="Index")
        data.add_data_frame(df)
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


class TestConfig(unittest.TestCase):
    def test_config(self) -> None:
        animation = Config({"color": {"set": ["Genres"]}})
        self.assertEqual({"config": {"color": {"set": ["Genres"]}}}, animation.build())

    def test_config_preset(self) -> None:
        animation = Config.column({"x": "foo", "y": "bar"})
        # instead of build() test with dump() because contains raw js
        self.assertEqual(
            "{\"config\": lib.presets.column({'x': 'foo', 'y': 'bar'})}",
            animation.dump(),
        )


class TestStyle(unittest.TestCase):
    def test_style(self) -> None:
        animation = Style({"title": {"backgroundColor": "#A0A0A0"}})
        self.assertEqual(
            {"style": {"title": {"backgroundColor": "#A0A0A0"}}}, animation.build()
        )

    def test_style_can_be_none(self) -> None:
        animation = Style(None)
        self.assertEqual({"style": None}, animation.build())


class TestKeyframe(unittest.TestCase):
    def test_animation_has_to_be_passed_even_if_options_passed(
        self,
    ) -> None:
        with self.assertRaises(ValueError):
            Keyframe(duration="500ms")

    def test_keyframe_cannot_be_passed(
        self,
    ) -> None:
        with self.assertRaises(ValueError):
            Keyframe(Keyframe(Style(None)))  # type: ignore

    def test_animation_and_snapshot_cannot_be_passed(
        self,
    ) -> None:
        with self.assertRaises(ValueError):
            Keyframe(Keyframe(Style(None), Snapshot("abc123")))

    def test_animation_and_stored_animation_cannot_be_passed(
        self,
    ) -> None:
        with self.assertRaises(ValueError):
            Keyframe(Keyframe(Style(None), Animation("abc123")))

    def test_keyframe(self) -> None:
        animation = Keyframe(
            Data.filter(None), Style(None), Config({"title": "Keyframe"})
        )
        self.assertEqual(
            animation.build(),
            {
                "target": {
                    "config": {"title": "Keyframe"},
                    "data": {"filter": None},
                    "style": None,
                }
            },
        )

    def test_keyframe_with_snapshot(self) -> None:
        animation = Keyframe(Snapshot("abc123"))
        self.assertEqual(
            animation.build(),
            {
                "target": "abc123",
            },
        )

    def test_keyframe_with_stored_animation(self) -> None:
        animation = Keyframe(Animation("abc123"))
        self.assertEqual(
            animation.build(),
            {
                "target": "abc123",
            },
        )

    def test_keyframe_with_options(self) -> None:
        animation = Keyframe(
            Data.filter(None), Style(None), Config({"title": "Keyframe"}), duration=1
        )
        self.assertEqual(
            animation.build(),
            {
                "target": {
                    "config": {"title": "Keyframe"},
                    "data": {"filter": None},
                    "style": None,
                },
                "options": {"duration": 1},
            },
        )


class TestSnapshot(unittest.TestCase):
    def test_snapshot(self) -> None:
        animation = Snapshot("abc1234")
        self.assertEqual("abc1234", animation.build())

    def test_snapshot_dump(self) -> None:
        animation = Snapshot("abc1234")
        self.assertEqual('"abc1234"', animation.dump())


class TestAnimation(unittest.TestCase):
    def test_animation(self) -> None:
        animation = Animation("abc1234")
        self.assertEqual("abc1234", animation.build())

    def test_animation_dump(self) -> None:
        animation = Animation("abc1234")
        self.assertEqual('"abc1234"', animation.dump())


class TestMerger(unittest.TestCase):
    def setUp(self) -> None:
        self.merger = AnimationMerger()

        self.data = Data()
        self.data.add_record(["Rock", "Hard", 96])

        self.config = Config({"channels": {"label": {"attach": ["Popularity"]}}})

    def test_merge(self) -> None:
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

    def test_merge_none(self) -> None:
        self.merger.merge(self.config)
        self.merger.merge(Style(None))
        self.assertEqual(
            '{"config": {"channels": {"label": {"attach": ["Popularity"]}}}, "style": null}',
            self.merger.dump(),
        )

    def test_snapshot_can_not_be_merged(self) -> None:
        self.merger.merge(self.data)
        self.merger.merge(self.config)
        self.merger.merge(Style({"title": {"backgroundColor": "#A0A0A0"}}))
        self.assertRaises(ValueError, self.merger.merge, Snapshot("abc1234"))

    def test_stored_animation_can_not_be_merged(self) -> None:
        self.merger.merge(self.data)
        self.merger.merge(self.config)
        self.merger.merge(Style({"title": {"backgroundColor": "#A0A0A0"}}))
        self.assertRaises(ValueError, self.merger.merge, Animation("abc1234"))

    def test_only_different_animations_can_be_merged(self) -> None:
        self.merger.merge(self.data)
        self.merger.merge(self.config)
        self.merger.merge(Style({"title": {"backgroundColor": "#A0A0A0"}}))

        data = Data()
        data.add_record(["Pop", "Hard", 114])

        self.assertRaises(ValueError, self.merger.merge, data)
        self.assertRaises(ValueError, self.merger.merge, Config({"title": "Test"}))
        self.assertRaises(ValueError, self.merger.merge, Style(None))

    def test_merge_keyframes(self) -> None:
        self.merger.merge(Keyframe(Style(None)))
        self.merger.merge(Keyframe(Style(None), duration=0))
        self.merger.merge(Keyframe(Style(None)))

        self.assertEqual(
            self.merger.dump(),
            json.dumps(
                [
                    {"target": {"style": None}},
                    {"target": {"style": None}, "options": {"duration": 0}},
                    {"target": {"style": None}},
                ]
            ),
        )

    def test_keyframe_and_animation_can_not_be_merged(self) -> None:
        self.merger.merge(Keyframe(Style(None)))
        self.assertRaises(ValueError, self.merger.merge, self.data)

    def test_animation_and_keyframe_can_not_be_merged(self) -> None:
        self.merger.merge(self.data)
        self.assertRaises(ValueError, self.merger.merge, Keyframe(Style(None)))

    def test_merge_animations_keyframe(self) -> None:
        animations = tuple([Keyframe(Style(None))])
        merger = AnimationMerger.merge_animations(animations)

        self.assertEqual(
            merger.dump(),
            json.dumps(
                [
                    {"target": {"style": None}},
                ]
            ),
        )
