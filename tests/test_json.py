"""
A test module used to test
json module
"""

import json
import unittest

from ipyvizzu import RawJavaScriptEncoder, RawJavaScript


class TestRawJavaScriptEncoder(unittest.TestCase):
    """
    A test class used to test
    RawJavaScriptEncoder()
    """

    def test_encoder_with_rawjavascript(self) -> None:
        """
        A test method used to test
        RawJavaScriptEncoder() with RawJavaScript()
        """
        raw_javascript = RawJavaScript("null")
        self.assertEqual(
            json.dumps({"test": raw_javascript}, cls=RawJavaScriptEncoder),
            '{"test": null}',
        )

    def test_encoder_with_not_rawjavascript(self) -> None:
        """
        A test method used to test
        RawJavaScriptEncoder() with NotRawJavaScript()
        """

        class NotRawJavaScript:
            """
            A class used to represent
            a custom not javascript object
            """

            def __init__(self):
                pass

        not_raw_javascript = NotRawJavaScript()
        with self.assertRaises(TypeError):
            json.dumps({"test": not_raw_javascript}, cls=RawJavaScriptEncoder)
