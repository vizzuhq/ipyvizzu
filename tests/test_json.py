# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

import json
import unittest

from ipyvizzu import RawJavaScriptEncoder, RawJavaScript


class TestRawJavaScriptEncoder(unittest.TestCase):
    def test_encoder_with_rawjavascript(self) -> None:
        raw_javascript = RawJavaScript("null")
        self.assertEqual(
            json.dumps({"test": raw_javascript}, cls=RawJavaScriptEncoder),
            '{"test": null}',
        )

    def test_encoder_with_not_rawjavascript(self) -> None:
        class NotRawJavaScript:
            # pylint: disable=too-few-public-methods

            def __init__(self) -> None:
                pass

        not_raw_javascript = NotRawJavaScript()
        with self.assertRaises(TypeError):
            json.dumps({"test": not_raw_javascript}, cls=RawJavaScriptEncoder)
