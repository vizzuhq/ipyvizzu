from tests.json import TestRawJavaScriptEncoder
from pyvizzu import RawJavaScriptEncoder, RawJavaScript


class TestRawJavaScriptEncoderPyvizzu(TestRawJavaScriptEncoder):
    def get_raw_javascript_encoder(self):
        return RawJavaScriptEncoder

    def get_raw_javascript(self, javascript):
        return RawJavaScript(javascript)
