from tests.json import TestRawJavaScriptEncoder
from ipyvizzu import RawJavaScriptEncoder, RawJavaScript


class TestRawJavaScriptEncoderIpyvizzu(TestRawJavaScriptEncoder):
    def get_raw_javascript_encoder(self):
        return RawJavaScriptEncoder

    def get_raw_javascript(self, javascript):
        return RawJavaScript(javascript)
