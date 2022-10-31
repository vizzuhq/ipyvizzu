"""A module for testing the ipyvizzu.json module."""

import json
import unittest

from ipyvizzu import RawJavaScriptEncoder, RawJavaScript


class TestRawJavaScriptEncoder(unittest.TestCase):
    """A class for testing RawJavaScriptEncoder class."""

    def test_encoder_with_rawjavascript(self) -> None:
        """
        A method for testing RawJavaScriptEncoder with RawJavaScript object.

        Raises:
            AssertionError: If the dumped value is not correct.
        """

        raw_javascript = RawJavaScript("null")
        self.assertEqual(
            json.dumps({"test": raw_javascript}, cls=RawJavaScriptEncoder),
            '{"test": null}',
        )

    def test_encoder_with_not_rawjavascript(self) -> None:
        """
        A method for testing RawJavaScriptEncoder with NotRawJavaScript object.

        Raises:
            AssertionError: If TypeError is not occurred.
        """

        class NotRawJavaScript:
            """A class for representing a custom object which is not RawJavaScript."""

            # pylint: disable=too-few-public-methods

            def __init__(self):
                """NotRawJavaScript constructor."""

        not_raw_javascript = NotRawJavaScript()
        with self.assertRaises(TypeError):
            json.dumps({"test": not_raw_javascript}, cls=RawJavaScriptEncoder)
