"""
A module used to work
with json
"""

import json
from typing import Optional
import uuid


class RawJavaScript:
    """
    A class used to represent
    a custom object which contains raw javascript code
    """

    # pylint: disable=too-few-public-methods

    def __init__(self, raw: Optional[str]):
        self._raw = raw

    @property
    def raw(self) -> Optional[str]:
        """
        A property used to store
        raw javascript code as str
        """

        return self._raw


class RawJavaScriptEncoder(json.JSONEncoder):
    """
    A JSONEncoder class used to encode
    RawJavaScript() object
    """

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
