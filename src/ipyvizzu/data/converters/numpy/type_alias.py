"""
This module provides typing aliases for numpy converter.
"""

from typing import Dict, TypeVar, Union


Index = int
"""Represents the index of a column."""

Name = str
"""Represents the name of a column."""

DType = type
"""Represents the dtype of a column."""

Unit = str
"""Represents the unit of a column."""

ColumnName = Union[Name, Dict[Index, Name]]
"""
Represents a column name. It is a dictionary of Index:Name pairs
or for single-dimensional arrays, it can be just a Name.
"""

ColumnDtype = Union[DType, Dict[Index, DType]]
"""
Represents a column dtype. It is a dictionary of Index:DType pairs
or for single-dimensional arrays, it can be just a DType.
"""

ColumnUnit = Union[Unit, Dict[Index, Unit]]
"""
Represents a column unit. It is a dictionary of Index:Unit pairs
or for single-dimensional arrays, it can be just a Unit.
"""

ColumnConfig = TypeVar("ColumnConfig", Name, DType, Unit)
"""
Represents a column config. It can be Name, DType or Unit.
"""
