from tests.json import TestRawJavaScriptEncoder
from stpyvizzu import RawJavaScriptEncoder, RawJavaScript


class TestRawJavaScriptEncoderStpyvizzu(TestRawJavaScriptEncoder):
    def get_raw_javascript_encoder(self):
        return RawJavaScriptEncoder

    def get_raw_javascript(self, javascript):
        return RawJavaScript(javascript)
