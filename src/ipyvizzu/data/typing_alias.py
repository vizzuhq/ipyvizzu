"""
This module provides typing aliases for data used in ipyvizzu.
"""

from typing import Dict, List, Sequence, Union


DimensionValue = str

MeasureValue = Union[int, float]

NestedMeasureValues = Union[MeasureValue, List["NestedMeasureValues"]]

RecordValue = Union[DimensionValue, MeasureValue]

Record = List[RecordValue]

SeriesValues = Union[Sequence[DimensionValue], Sequence[MeasureValue]]

Series = Dict[str, Union[str, SeriesValues]]
