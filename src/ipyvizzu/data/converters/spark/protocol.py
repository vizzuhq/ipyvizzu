"""
This module provides protocol classes for pandas data frame converter.
"""

from typing import Any, Callable, Protocol, Sequence, runtime_checkable


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
