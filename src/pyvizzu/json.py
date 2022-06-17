import json
import typing
import uuid


class RawJavaScript:
    def __init__(self, raw: typing.Optional[str]):
        self._raw = raw

    @property
    def raw(self):
        return self._raw


class RawJavaScriptEncoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        json.JSONEncoder.__init__(self, *args, **kwargs)
        self._raw_replacements = {}

    def default(self, o):
        if isinstance(o, RawJavaScript):
            key = uuid.uuid4().hex
            self._raw_replacements[key] = o.raw
            return key
        return json.JSONEncoder.default(self, o)

    def encode(self, o):
        result = json.JSONEncoder.encode(self, o)
        for key, val in self._raw_replacements.items():
            result = result.replace(f'"{key}"', val)
        return result
