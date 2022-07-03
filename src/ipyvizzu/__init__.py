"""Jupyter notebook integration of Vizzu."""

from .jupyter.chart import Chart
from .jupyter.template import DisplayTemplate
from .chartlib.animation import (
    Animation,
    PlainAnimation,
    InferType,
    Data,
    Config,
    Style,
    Snapshot,
    AnimationMerger,
)
from .chartlib.method import Method, Animate, Feature, Store, EventOn, EventOff, Log
from .chartlib.json import RawJavaScript, RawJavaScriptEncoder
from .chartlib.template import ChartProperty, DisplayTarget
from .chartlib.event import EventHandler
