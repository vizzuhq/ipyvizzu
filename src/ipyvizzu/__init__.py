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
* [Data][ipyvizzu.data]
* [Integrations][ipyvizzu.integrations]

`ipyvizzu` package imports the following objects in `__init__.py`:

* [Chart][ipyvizzu.chart.Chart]
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
* [InferType][ipyvizzu.data.infer_type.InferType]
* [NumpyArrayConverter][ipyvizzu.data.converters.numpy.converter.NumpyArrayConverter]
* [PandasDataFrameConverter][ipyvizzu.data.converters.pandas.converter.PandasDataFrameConverter]
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

import warnings

from .chart import Chart
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
from .data.converters.numpy.converter import NumpyArrayConverter
from .data.converters.pandas.converter import PandasDataFrameConverter
from .data.infer_type import InferType
from .method import Method, Animate, Feature, Store, EventOn, EventOff, Log
from .json import RawJavaScript, RawJavaScriptEncoder
from .template import ChartProperty, DisplayTarget, DisplayTemplate
from .event import EventHandler

from .__version__ import __version__, PYENV

__all__ = [
    "Chart",
    "Data",
    "Config",
    "Style",
    "Keyframe",
    "Snapshot",
    "Animation",
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
    "NumpyArrayConverter",
    "PandasDataFrameConverter",
    "InferType",
    "Method",
    "EventHandler",
    "RawJavaScript",
    "RawJavaScriptEncoder",
    "ChartProperty",
    "DisplayTarget",
    "DisplayTemplate",
]


# TODO: remove once support for Python 3.6 is dropped
if PYENV < (3, 7):
    warnings.warn(
        "Python 3.6 support will be dropped in future versions.",
        FutureWarning,
        stacklevel=2,
    )
