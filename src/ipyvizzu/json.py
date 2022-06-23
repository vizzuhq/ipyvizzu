"""A module for inserting javascript code into a json string."""

import json
from typing import Optional
import uuid


class RawJavaScript:
    """A class for representing and storing raw javascript code."""

    # pylint: disable=too-few-public-methods

    def __init__(self, raw: Optional[str]):
        self._raw = raw

    @property
    def raw(self) -> Optional[str]:
        """A property for storing raw javascript code as a string."""

        return self._raw


class RawJavaScriptEncoder(json.JSONEncoder):
    """
    A class for encoding json object that contains RawJavaScript values.
    It is derived from the json.JSONEncoder() class.
    """

    def __init__(self, *args, **kwargs):
        """
        Extends json.JSONEncoder() with an instance variable - _raw_replacements.
        _raw_replacements dictionary stores the uuids and
        javascript codes of the replaced RawJavaScript objects.
        """

        json.JSONEncoder.__init__(self, *args, **kwargs)
        self._raw_replacements = {}

    def default(self, o):
        """
        Overrides json.JSONEncoder().default() method.
        It replaces RawJavaScript object with uuid and
        it stores raw javascript code with uuid key in _raw_replacements dictionary.
        """

        if isinstance(o, RawJavaScript):
            key = uuid.uuid4().hex
            self._raw_replacements[key] = o.raw
            return key
        return json.JSONEncoder.default(self, o)

    def encode(self, o):
        """
        Overrides json.JSONEncoder().encode() method.
        It replaces uuids with raw javascript code without apostrophes.
        """

        result = json.JSONEncoder.encode(self, o)
        for key, val in self._raw_replacements.items():
            result = result.replace(f'"{key}"', val)
        return result
