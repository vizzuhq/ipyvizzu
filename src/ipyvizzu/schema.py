"""A module for storing the data schema."""


NAMED_SCHEMA: dict = {
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
"""Store the schema of the `series`, `dimensions` and `measures` data types."""


RECORD_SCHEMA: dict = {
    "type": "array",
    "items": {"anyOf": [{"type": "array"}, {"type": "object"}]},
}
"""Store the schema of the `records` data type."""


DATA_SCHEMA: dict = {
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
"""Store the schema of the data animation."""
