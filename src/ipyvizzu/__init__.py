"""
Build animated charts in `Jupyter Notebook`
and similar environments with a simple `Python` syntax.

`ipyvizzu` package consists of the following main modules:

* [Chart][ipyvizzu.chart]
* [Animation][ipyvizzu.animation]
* [Animation Control][ipyvizzu.animationcontrol]
* [Method][ipyvizzu.method]
* [Event][ipyvizzu.event]
* [Json][ipyvizzu.json]
* [Template][ipyvizzu.template]
* [Schema][ipyvizzu.schema]

`ipyvizzu` package imports the following objects in `__init__.py`:

* [Chart][ipyvizzu.chart.Chart]
* [InferType][ipyvizzu.data.infer_type.InferType]
* [Data][ipyvizzu.animation.Data]
* [Config][ipyvizzu.animation.Config]
* [Style][ipyvizzu.animation.Style]
* [Keyframe][ipyvizzu.animation.Keyframe]
* [Snapshot][ipyvizzu.animation.Snapshot]
* [Animation][ipyvizzu.animation.Animation]
* [AbstractAnimation][ipyvizzu.animation.AbstractAnimation]
* [PlainAnimation][ipyvizzu.animation.PlainAnimation]
* [AnimationMerger][ipyvizzu.animation.AnimationMerger]
* [AnimationControl][ipyvizzu.animationcontrol.AnimationControl]
* [Animate][ipyvizzu.method.Animate]
* [Feature][ipyvizzu.method.Feature]
* [Store][ipyvizzu.method.Store]
* [EventOn][ipyvizzu.method.EventOn]
* [EventOff][ipyvizzu.method.EventOff]
* [Log][ipyvizzu.method.Log]
* [Method][ipyvizzu.method.Method]
* [EventHandler][ipyvizzu.event.EventHandler]
* [RawJavaScript][ipyvizzu.json.RawJavaScript]
* [RawJavaScriptEncoder][ipyvizzu.json.RawJavaScriptEncoder]
* [ChartProperty][ipyvizzu.template.ChartProperty]
* [DisplayTarget][ipyvizzu.template.DisplayTarget]
* [DisplayTemplate][ipyvizzu.template.DisplayTemplate]
"""

from .chart import Chart
from .data.infer_type import InferType
from .animation import (
    AbstractAnimation,
    PlainAnimation,
    Data,
    Config,
    Style,
    Keyframe,
    Snapshot,
    Animation,
    AnimationMerger,
)
from .animationcontrol import AnimationControl
from .method import Method, Animate, Feature, Store, EventOn, EventOff, Log
from .json import RawJavaScript, RawJavaScriptEncoder
from .template import ChartProperty, DisplayTarget, DisplayTemplate
from .event import EventHandler

from .__version__ import __version__

__all__ = [
    "Chart",
    "Data",
    "Config",
    "Style",
    "Keyframe",
    "Snapshot",
    "Animation",
    "InferType",
    "AbstractAnimation",
    "PlainAnimation",
    "AnimationMerger",
    "Animate",
    "Feature",
    "Store",
    "EventOn",
    "EventOff",
    "Log",
    "AnimationControl",
    "Method",
    "EventHandler",
    "RawJavaScript",
    "RawJavaScriptEncoder",
    "ChartProperty",
    "DisplayTarget",
    "DisplayTemplate",
]
