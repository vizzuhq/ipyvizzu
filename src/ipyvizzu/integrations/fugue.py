"""
A module for Fugue integration.

Example:
    Users should not instantiate this module directly. As long as you
    installed fugue and ipyvizzu, the extension is auto-registered.

        from fugue import fsql

        fsql('''
        SELECT a, SUM(b) AS b FROM spark.table
        GROUP BY a ORDER BY b

        OUTPUT USING vizzu:bar(x="a", y="b", title="title")
        ''').run(spark_session)
"""

from typing import Any, Dict, Tuple

import pandas as pd
from fugue import DataFrames, Outputter  # type: ignore
from fugue.exceptions import FugueWorkflowError
from fugue.extensions import namespace_candidate  # type: ignore
from fugue.plugins import parse_outputter  # type: ignore
from triad import assert_or_throw  # type: ignore

from ipyvizzu import Chart, Config, Data, DisplayTarget

_TIMELINE_DEFAULT_CONF: Dict[str, Any] = dict(  # pylint: disable=use-dict-literal
    show={"delay": 0},
    hide={"delay": 0},
    title={"duration": 0, "delay": 0},
    duration=0.5,
)


class _Visualize(Outputter):
    """
    A Fugue outputter extension (majorly for Fugue SQL)

    Args:
        func:
            A function name of [Config][ipyvizzu.animation.Config]
        category:
            Can be preset or timeline
    """

    def __init__(self, func: str, category: str) -> None:
        super().__init__()
        self._category = category
        self._func = getattr(Config, func)

    def process(self, dfs: DataFrames) -> None:
        assert_or_throw(len(dfs) == 1, FugueWorkflowError("not single input"))
        df = dfs[0].as_pandas()  # pylint: disable=invalid-name
        if self._category == "timeline":
            self._process_timeline(df)
        else:
            self._process_preset(df)

    def _process_preset(self, df: pd.DataFrame) -> None:  # pylint: disable=invalid-name
        data = Data()
        data.add_df(df)
        chart = Chart(display=DisplayTarget.END)
        chart.animate(data)
        chart.animate(self._func(dict(self.params)))

    def _process_timeline(
        self, df: pd.DataFrame  # pylint: disable=invalid-name
    ) -> None:
        _p = dict(self.params)
        _pc = dict(_p.pop("config", {}))
        title = _pc.pop("title", "%s")
        key = _p.pop("by")
        conf = dict(_TIMELINE_DEFAULT_CONF)
        conf.update(_p)

        data = Data()
        chart = Chart(display=DisplayTarget.END)
        keys = df[key].unique()
        keys.sort()
        idx = pd.DataFrame({"_idx": range(len(keys)), key: keys})
        df = df.sort_values(key).merge(idx)
        data.add_df(df)
        chart.animate(data)

        for i, key in enumerate(keys):
            _p2 = dict(_pc)
            _p2["title"] = (title % key) if "%s" in title else title
            chart.animate(Data.filter(f"record._idx == {i}"), self._func(_p2), **conf)


@parse_outputter.candidate(namespace_candidate("vizzu", lambda x: isinstance(x, str)))
def _parse_vizzu(obj: Tuple[str, str]) -> Outputter:
    if obj[1].startswith("timeline_"):
        return _Visualize(obj[1].split("_", 1)[1], "timeline")
    return _Visualize(obj[1], "preset")
