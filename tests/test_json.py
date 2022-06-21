"""
A test module used to test
the json module
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
        RawJavaScriptEncoder() with RawJavaScript() custom object
        """

        raw_javascript = RawJavaScript("null")
        self.assertEqual(
            json.dumps({"test": raw_javascript}, cls=RawJavaScriptEncoder),
            '{"test": null}',
        )

    def test_encoder_with_not_rawjavascript(self) -> None:
        """
        A test method used to test
        RawJavaScriptEncoder() with NotRawJavaScript() custom object
        """

        class NotRawJavaScript:
            """
            A class used to represent
            a custom object which is not RawJavaScript
            """

            # pylint: disable=too-few-public-methods

            def __init__(self):
                pass

        not_raw_javascript = NotRawJavaScript()
        with self.assertRaises(TypeError):
            json.dumps({"test": not_raw_javascript}, cls=RawJavaScriptEncoder)
