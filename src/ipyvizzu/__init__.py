"""
Build animated charts in Jupyter Notebook and
in many other environments with a simple Python syntax.
"""

from .chart import Chart
from .animation import (
    Animation,
    PlainAnimation,
    InferType,
    Data,
    Config,
    Style,
    Snapshot,
    AnimationMerger,
)
from .method import Method, Animate, Feature, Store, EventOn, EventOff, Log
from .json import RawJavaScript, RawJavaScriptEncoder
from .template import ChartProperty, DisplayTarget, DisplayTemplate
from .event import EventHandler

__all__ = [
    "Chart",
    "Animation",
    "PlainAnimation",
    "InferType",
    "Data",
    "Config",
    "Style",
    "Snapshot",
    "AnimationMerger",
    "Method",
    "Animate",
    "Feature",
    "Store",
    "EventOn",
    "EventOff",
    "Log",
    "RawJavaScript",
    "RawJavaScriptEncoder",
    "ChartProperty",
    "DisplayTarget",
    "DisplayTemplate",
    "EventHandler",
]
