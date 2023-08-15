"""
This module provides protocol classes for pandas data frame converter.
"""

from typing import Any, Callable, Sequence

from ipyvizzu.__version__ import PYENV


if PYENV >= (3, 8):
    from typing import Protocol, runtime_checkable
else:
    # TODO: remove once support for Python 3.7 is dropped
    # pylint: disable=duplicate-code
    from typing_extensions import Protocol, runtime_checkable  # type: ignore


@runtime_checkable
class PandasDataFrame(Protocol):
    """
    Represents a pandas DataFrame Protocol.
    """

    # pylint: disable=too-few-public-methods

    index: Any
    columns: Sequence[str]
    sample: Callable[..., Any]
    __len__: Callable[[], int]
    __getitem__: Callable[[Any], Any]


@runtime_checkable
class PandasSeries(Protocol):
    """
    Represents a pandas Series Protocol.
    """

    # pylint: disable=too-few-public-methods

    index: Any
    values: Any
    dtype: Any
    __len__: Callable[[], int]
    __getitem__: Callable[[Any], Any]
