"""
This module provides typing aliases for data used in ipyvizzu.
"""

from typing import Dict, List, Sequence, Union


DimensionValue = str

MeasureValue = Union[int, float]

NestedMeasureValues = Union[MeasureValue, List["NestedMeasureValues"]]

Value = Union[DimensionValue, MeasureValue]

RecordValues = Union[DimensionValue, MeasureValue]

Record = List[RecordValues]

SeriesValues = Union[Sequence[DimensionValue], Sequence[MeasureValue]]

Series = Dict[str, Union[str, SeriesValues]]
