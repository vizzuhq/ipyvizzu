from jsonschema import validate


NAMED_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "values": {"type": "array"},
            "type": {"type": "string", "optional": True},
        },
        "required": ["name", "values"],
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
    @staticmethod
    def validate(data):
        validate(data, DATA_SCHEMA)
