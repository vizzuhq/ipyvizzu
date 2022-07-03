"""A module for storing the information needed to generate javascript code."""

from enum import Enum


VIZZU = "https://cdn.jsdelivr.net/npm/vizzu@~0.4.0/dist/vizzu.min.js"


class ChartProperty(Enum):
    """An enum class for storing chart properties."""

    CONFIG = "config"
    STYLE = "style"


class DisplayTarget(Enum):
    """
    An enum class for storing chart display options.
    BEGIN: Displays all animation steps after the constructor's cell.
    END: Displays all animation steps after the last running cell.
    ACTUAL: Displays the actual animation step after the currently running cell.
    MANUAL: Displays all animation steps after calling a show method.
    """

    BEGIN = "begin"
    END = "end"
    ACTUAL = "actual"
    MANUAL = "manual"
