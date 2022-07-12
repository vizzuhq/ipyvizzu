"""IPython - Jupyter notebook integration of Vizzu."""

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
