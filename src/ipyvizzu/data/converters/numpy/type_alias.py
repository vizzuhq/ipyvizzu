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

ColumnConfig = TypeVar("ColumnConfig", Name, DType)
"""
Represents a column config. It can be Name or DType.
"""
