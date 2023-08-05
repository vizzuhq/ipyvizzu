"""A module for working JavaScript code in json convertible objects."""

import json
from typing import Any, Optional
import uuid


class RawJavaScript:
    """A class for representing raw JavaScript code."""

    # pylint: disable=too-few-public-methods

    def __init__(self, raw: Optional[str]):
        """
        RawJavaScript constructor.

        It stores raw JavaScript code as a string.

        Args:
            raw: JavaScript code as `str`.
        """

        self._raw = raw

    @property
    def raw(self) -> Optional[str]:
        """
        A property for storing raw JavaScript code as a string.

        Returns:
            Raw JavaScript code as `str`.
        """

        return self._raw


class RawJavaScriptEncoder(json.JSONEncoder):
    """
    A class for representing a custom json encoder,
    it can encode objects that contain
    [RawJavaScript][ipyvizzu.json.RawJavaScript] values.
    """

    def __init__(self, *args, **kwargs):
        """
        RawJavaScriptEncoder constructor.

        It extends [JSONEncoder][json.JSONEncoder] with
        an instance variable (`_raw_replacements`).
        The `_raw_replacements` dictionary stores the `uuids` and
        JavaScript codes of the [RawJavaScript][ipyvizzu.json.RawJavaScript] objects.
        """

        json.JSONEncoder.__init__(self, *args, **kwargs)
        self._raw_replacements = {}

    def default(self, o: Any):
        """
        Overrides [JSONEncoder.default][json.JSONEncoder.default] method.
        It replaces [RawJavaScript][ipyvizzu.json.RawJavaScript] object with `uuid` and
        it stores raw JavaScript code with `uuid` key in the `_raw_replacements` dictionary.
        """

        if isinstance(o, RawJavaScript):
            key = uuid.uuid4().hex
            self._raw_replacements[key] = o.raw
            return key
        return json.JSONEncoder.default(self, o)

    def encode(self, o: Any):
        """
        Overrides [JSONEncoder.encode][json.JSONEncoder.encode] method.
        It replaces `uuids` with raw JavaScript code without apostrophes.
        """

        result = json.JSONEncoder.encode(self, o)
        for key, val in self._raw_replacements.items():
            result = result.replace(f'"{key}"', val)
        return result
