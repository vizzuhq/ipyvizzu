import abc
import json
import unittest


class NotRawJavaScript:
    def __init__(self):
        pass


class TestRawJavaScriptEncoder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if cls is TestRawJavaScriptEncoder:
            raise unittest.SkipTest()
        super(TestRawJavaScriptEncoder, cls).setUpClass()

    @abc.abstractmethod
    def get_raw_javascript_encoder(self):
        """
        Return RawJavaScriptEncoder
        """

    @abc.abstractmethod
    def get_raw_javascript(self, javascript):
        """
        Return RawJavaScript(javascript)
        """

    def test_encoder_with_rawjavascript(self):
        raw_javascript = self.get_raw_javascript("null")
        self.assertEqual(
            json.dumps({"test": raw_javascript}, cls=self.get_raw_javascript_encoder()),
            '{"test": null}',
        )

    def test_encoder_with_not_rawjavascript(self):
        not_raw_javascript = NotRawJavaScript()
        with self.assertRaises(TypeError):
            json.dumps(
                {"test": not_raw_javascript}, cls=self.get_raw_javascript_encoder()
            )
