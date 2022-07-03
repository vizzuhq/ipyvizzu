"""Python integration of Vizzu."""


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


ENV = False


if not ENV:
    try:
        from IPython import get_ipython

        IPY = get_ipython()
        if IPY is not None:
            from .jupyter.chart import Chart
            from .jupyter.template import DisplayTemplate

            ENV = True
    except ImportError as error:
        """ipyvizzu is not running in Jupyter environment."""
        pass


if not ENV:
    from .python.chart import Chart
    from .python.template import DisplayTemplate

    ENV = True
