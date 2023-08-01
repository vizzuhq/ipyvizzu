"""
This module provides the `InferType` class, which stores data infer types.
"""

from enum import Enum


class InferType(Enum):
    """
    An enum class for storing data infer types.

    Attributes:
        DIMENSION: An enum key-value for storing dimension infer type.
            Dimensions are categorical series that can contain strings and numbers,
            but both will be treated as strings.

        MEASURE: An enum key-value for storing measure infer type.
            Measures can only be numerical.
    """

    DIMENSION: str = "dimension"
    MEASURE: str = "measure"
