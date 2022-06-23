"""A module for storing data schema."""


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
