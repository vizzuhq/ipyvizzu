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
from .chartlib.template import ChartProperty, DisplayTarget, DisplayTemplate
from .chartlib.event import EventHandler


ENV = False


if not ENV:  # pragma: no cover
    try:
        from IPython import get_ipython

        IPY = get_ipython()  # pragma: no cover
        if IPY is not None:  # pragma: no cover
            from .jupyter.chart import Chart  # pragma: no cover

            ENV = True  # pragma: no cover
    except ImportError as error:
        # ipyvizzu is not running in Jupyter environment.
        pass


if not ENV:  # pragma: no cover
    try:
        from streamlit.scriptrunner.script_run_context import get_script_run_ctx

        if get_script_run_ctx():  # pragma: no cover
            from .streamlit.chart import Chart  # pragma: no cover

            ENV = True  # pragma: no cover
    except ImportError as error:
        # ipyvizzu is not running in Streamlit environment.
        pass


if not ENV:  # pragma: no cover
    from .python.chart import Chart

    ENV = True
