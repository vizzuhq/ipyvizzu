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
class SparkDataFrame(Protocol):
    """
    Represents a pyspark DataFrame Protocol.
    """

    # pylint: disable=too-few-public-methods

    columns: Sequence[str]
    count: Callable[..., int]
    sample: Callable[..., Any]
    limit: Callable[..., Any]
    select: Callable[..., Any]
    withColumn: Callable[..., Any]
    rdd: Any
