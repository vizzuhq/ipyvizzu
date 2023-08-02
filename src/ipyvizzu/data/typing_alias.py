"""
This module provides typing aliases for data used in ipyvizzu.
"""

from typing import Dict, List, Sequence, Union


DimensionValue = str
"""
Represents a value that can be either a string or a number,
but both will be treated as strings.
"""

MeasureValue = Union[int, float]
"""
Represents a numerical value, which can be either an int or a float.
"""

NestedMeasureValues = Union[MeasureValue, List["NestedMeasureValues"]]
"""
Represents a nested structure of MeasureValues.
It can be a single MeasureValue or a list containing other NestedMeasureValues.
"""

RecordValue = Union[DimensionValue, MeasureValue]
"""
Represents a value that can be either a DimensionValue or a MeasureValue.
"""

Record = List[RecordValue]
"""
Represents a Record, which is a list of RecordValues.
In other words, it's a list containing a mix of DimensionValues and MeasureValues.
"""

SeriesValues = Union[Sequence[DimensionValue], Sequence[MeasureValue]]
"""
Represents a collection of values for a Series.
It can be a list of DimensionValues or a list of MeasureValues.
"""

Series = Dict[str, Union[str, SeriesValues]]
"""
Represents a Series in a dictionary format.
It consists of a name (string), an optional type (also a string),
and a values key which contains a SeriesValues.
"""
