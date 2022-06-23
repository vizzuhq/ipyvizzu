"""A module for testing the ipyvizzu.json module."""

import json
import unittest

from ipyvizzu import RawJavaScriptEncoder, RawJavaScript


class TestRawJavaScriptEncoder(unittest.TestCase):
    """A class for testing RawJavaScriptEncoder()."""

    def test_encoder_with_rawjavascript(self) -> None:
        """A method for testing RawJavaScriptEncoder() with RawJavaScript() object."""

        raw_javascript = RawJavaScript("null")
        self.assertEqual(
            json.dumps({"test": raw_javascript}, cls=RawJavaScriptEncoder),
            '{"test": null}',
        )

    def test_encoder_with_not_rawjavascript(self) -> None:
        """A method for testing RawJavaScriptEncoder() with NotRawJavaScript() object."""

        class NotRawJavaScript:
            """A class for representing a custom object which is not RawJavaScript()."""

            # pylint: disable=too-few-public-methods

            def __init__(self):
                pass

        not_raw_javascript = NotRawJavaScript()
        with self.assertRaises(TypeError):
            json.dumps({"test": not_raw_javascript}, cls=RawJavaScriptEncoder)
