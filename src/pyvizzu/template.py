import enum


class DisplayTarget(str, enum.Enum):
    BEGIN = "begin"
    END = "end"
    ACTUAL = "actual"
    MANUAL = "manual"


VIZZU = "https://cdn.jsdelivr.net/npm/vizzu@~0.4.0/dist/vizzu.min.js"
