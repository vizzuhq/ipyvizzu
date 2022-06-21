"""
A module used to work
with data schema
"""

from jsonschema import validate


NAMED_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "values": {"type": "array", "optional": True},
            "type": {"type": "string", "optional": True},
        },
        "required": ["name"],
    },
}


RECORD_SCHEMA = {"type": "array", "items": {"type": "array"}}


DATA_SCHEMA = {
    "type": "object",
    "oneOf": [
        {
            "properties": {
                "series": NAMED_SCHEMA,
                "records": RECORD_SCHEMA,
                "filter": {"optional": True},
            },
            "additionalProperties": False,
        },
        {
            "properties": {
                "dimensions": NAMED_SCHEMA,
                "measures": NAMED_SCHEMA,
                "filter": {"optional": True},
            },
            "additionalProperties": False,
            "required": ["dimensions", "measures"],
        },
    ],
}


class DataSchema:
    """
    A class used to validate
    data by schema
    """

    # pylint: disable=too-few-public-methods

    @staticmethod
    def validate(data: dict) -> None:
        """
        A static method used to compare
        the given data with the DATA_SCHEMA
        """

        validate(data, DATA_SCHEMA)
