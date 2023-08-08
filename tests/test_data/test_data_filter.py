# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import pathlib
import unittest

from ipyvizzu import Data


class TestDataFilter(unittest.TestCase):
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


class TestDataFilterCls(unittest.TestCase):
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
