import abc
import json
import pathlib
import unittest
import jsonschema
import pandas as pd


class TestPlainAnimation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if cls is TestPlainAnimation:
            raise unittest.SkipTest()
        super(TestPlainAnimation, cls).setUpClass()

    @abc.abstractmethod
    def get_plainanimation(self, **kwargs):
        """
        Return PlainAnimation(**kwargs)
        """

    def test_plainanimation(self):
        animation = self.get_plainanimation(geometry="circle")
        self.assertEqual({"geometry": "circle"}, animation.build())


class TestDataClassMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if cls is TestDataClassMethods:
            raise unittest.SkipTest()
        super(TestDataClassMethods, cls).setUpClass()
        cls.asset_dir = pathlib.Path(__file__).parent / "assets"

    @abc.abstractmethod
    def get_data(self):
        """
        Return Data
        """

    def test_filter(self):
        data = self.get_data().filter("filter_expr")
        # instead of build() test with dump() because contains raw js
        self.assertEqual(
            '{"data": {"filter": record => { return (filter_expr) }}}',
            data.dump(),
        )

    def test_filter_can_be_none(self):
        data = self.get_data().filter(None)
        # instead of build() test with dump() because contains raw js
        self.assertEqual(
            '{"data": {"filter": null}}',
            data.dump(),
        )

    def test_from_json(self):
        data = self.get_data().from_json(self.asset_dir / "data_from_json.json")
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
        if cls is TestData:
            raise unittest.SkipTest()
        super(TestData, cls).setUpClass()
        cls.asset_dir = pathlib.Path(__file__).parent / "assets"

    @abc.abstractmethod
    def get_data(self):
        """
        Return Data()
        """

    def setUp(self):
        self.data = self.get_data()

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
        data = self.get_data()
        with self.assertRaises(TypeError):
            data.add_data_frame("not_data_frame", None)

    def test_data_frame_with_none(self):
        data = self.get_data()
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
        data = self.get_data()
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
        data = self.get_data()
        with self.assertRaises(TypeError):
            data.add_data_frame_index("not_data_frame", None)

    def test_data_frame_index_with_none_and_none(self):
        data = self.get_data()
        data.add_data_frame_index(None, None)
        self.assertEqual(
            {"data": {}},
            data.build(),
        )

    def test_data_frame_index_with_df_and_none(self):
        data = self.get_data()
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
        data = self.get_data()
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
        data = self.get_data()
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
    @classmethod
    def setUpClass(cls):
        if cls is TestDataSchema:
            raise unittest.SkipTest()
        super(TestDataSchema, cls).setUpClass()

    @abc.abstractmethod
    def get_data(self):
        """
        Return Data()
        """

    def setUp(self):
        self.data = self.get_data()

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
    @classmethod
    def setUpClass(cls):
        if cls is TestConfig:
            raise unittest.SkipTest()
        super(TestConfig, cls).setUpClass()

    @abc.abstractmethod
    def get_config(self, config):
        """
        Return Config(config)
        """

    def test_config(self):
        animation = self.get_config({"color": {"set": ["Genres"]}})
        self.assertEqual({"config": {"color": {"set": ["Genres"]}}}, animation.build())


class TestStyle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if cls is TestStyle:
            raise unittest.SkipTest()
        super(TestStyle, cls).setUpClass()

    @abc.abstractmethod
    def get_style(self, style):
        """
        Return Style(style)
        """

    def test_style(self):
        animation = self.get_style({"title": {"backgroundColor": "#A0A0A0"}})
        self.assertEqual(
            {"style": {"title": {"backgroundColor": "#A0A0A0"}}}, animation.build()
        )

    def test_style_can_be_none(self):
        animation = self.get_style(None)
        self.assertEqual({"style": None}, animation.build())


class TestSnapshot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if cls is TestSnapshot:
            raise unittest.SkipTest()
        super(TestSnapshot, cls).setUpClass()

    @abc.abstractmethod
    def get_snapshot(self, snapshot):
        """
        Return Snapshot(snapshot)
        """

    def test_snapshot(self):
        return self.get_snapshot("abc1234")

    def test_snapshot_can_not_be_built(self):
        animation = self.get_snapshot("abc1234")
        self.assertRaises(NotImplementedError, animation.build)


class TestMerger(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if cls is TestMerger:
            raise unittest.SkipTest()
        super(TestMerger, cls).setUpClass()

    @abc.abstractmethod
    def get_animationmerger(self):
        """
        Return AnimationMerger()
        """

    @abc.abstractmethod
    def get_data(self):
        """
        Return Data()
        """

    @abc.abstractmethod
    def get_config(self, config):
        """
        Return Config(config)
        """

    @abc.abstractmethod
    def get_style(self, style):
        """
        Return Style(style)
        """

    @abc.abstractmethod
    def get_snapshot(self, snapshot):
        """
        Return Snapshot(snapshot)
        """

    def setUp(self):
        self.merger = self.get_animationmerger()

        self.data = self.get_data()
        self.data.add_record(["Rock", "Hard", 96])

        self.config = self.get_config(
            {"channels": {"label": {"attach": ["Popularity"]}}}
        )

    def test_merge(self):
        self.merger.merge(self.data)
        self.merger.merge(self.config)
        self.merger.merge(self.get_style({"title": {"backgroundColor": "#A0A0A0"}}))
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
        self.merger.merge(self.get_style(None))
        self.assertEqual(
            '{"config": {"channels": {"label": {"attach": ["Popularity"]}}}, "style": null}',
            self.merger.dump(),
        )

    def test_snapshot_can_not_be_merged(self):
        self.merger.merge(self.data)
        self.merger.merge(self.config)
        self.merger.merge(self.get_style({"title": {"backgroundColor": "#A0A0A0"}}))
        self.assertRaises(
            NotImplementedError, self.merger.merge, self.get_snapshot("abc1234")
        )

    def test_only_different_animations_can_be_merged(self):
        self.merger.merge(self.data)
        self.merger.merge(self.config)
        self.merger.merge(self.get_style({"title": {"backgroundColor": "#A0A0A0"}}))

        data = self.get_data()
        data.add_record(["Pop", "Hard", 114])

        self.assertRaises(ValueError, self.merger.merge, data)
        self.assertRaises(
            ValueError, self.merger.merge, self.get_config({"title": "Test"})
        )
        self.assertRaises(ValueError, self.merger.merge, self.get_style(None))
