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


class Environment:
    """A class for selecting the runtime environment."""

    # pylint: disable=import-outside-toplevel
    # pylint: disable=unused-import

    @staticmethod
    def get_chart() -> None:
        """A static method for importing the appropriate chart for the environment."""

        if Environment.is_ipython():  # pragma: no cover
            from .jupyter.chart import Chart

            return Chart
        elif Environment.is_streamlit():  # pragma: no cover
            from .streamlit.chart import Chart

            return Chart
        else:
            from .python.chart import Chart

            return Chart

    @staticmethod
    def is_ipython():
        """A static method for detecting Jupyter environment."""
        try:
            from IPython import get_ipython

            return get_ipython()
        except ImportError:  # pragma: no cover
            return None

    @staticmethod
    def is_streamlit():
        """A static method for detecting Streamlit environment."""
        try:
            from streamlit.scriptrunner.script_run_context import get_script_run_ctx

            return get_script_run_ctx()
        except ImportError:  # pragma: no cover
            return None


Chart = Environment.get_chart()
