from types import ModuleType
from typing import Dict, List, Optional, Tuple, Type, Union

from ipyvizzu.data.converters.converter import ToSeriesListConverter
from ipyvizzu.data.infer_type import InferType
from ipyvizzu.data.typing_alias import (
    DimensionValue,
    MeasureValue,
    Series,
    SeriesValues,
)

NpArrayColumnNames = Union[str, Dict[int, str]]
NpArrayColumnDtypes = Union[Type, Dict[int, Type]]


class NumpyArrayConverter(ToSeriesListConverter):
    # pylint: disable=too-few-public-methods

    def __init__(
        self,
        np_array: Optional["np.array"],
        column: Optional[NpArrayColumnNames] = None,
        dtype: Optional[NpArrayColumnDtypes] = None,
        default_measure_value: Optional[MeasureValue] = 0,
        default_dimension_value: Optional[DimensionValue] = "",
    ) -> None:
        # pylint: disable=too-many-arguments

        self._np = self._get_numpy()
        self._np_array = np_array
        self._column = self._get_settings(column)
        self._dtype = self._get_settings(dtype)
        self._default_measure_value = default_measure_value
        self._default_dimension_value = default_dimension_value

    def get_series_list(self) -> List[Series]:
        if isinstance(self._np_array, type(None)) or self._np_array.ndim == 0:  # type: ignore
            return []
        if self._np_array.ndim == 1:  # type: ignore
            return self._get_series_list_from_array1dim()
        if self._np_array.ndim == 2:  # type: ignore
            return self._get_series_list_from_array2dim()
        raise ValueError("arrays larger than 2D are not supported")

    def _get_series_list_from_array1dim(self) -> List[Series]:
        i = 0
        name = self._column.get(i, i)
        values, infer_type = self._convert_to_series_values_and_type(
            (i, self._np_array)
        )
        return [self._convert_to_series(name, values, infer_type)]

    def _get_series_list_from_array2dim(self) -> List[Series]:
        series_list = []
        for i in range(self._np_array.shape[1]):  # type: ignore
            name = self._column.get(i, i)
            values, infer_type = self._convert_to_series_values_and_type(
                (i, self._np_array[:, i])  # type: ignore
            )
            series_list.append(self._convert_to_series(name, values, infer_type))
        return series_list

    def _get_numpy(self) -> ModuleType:
        try:
            import numpy as np  # pylint: disable=import-outside-toplevel

            return np
        except ImportError as error:
            raise ImportError(
                "numpy is not available. Please install numpy to use this feature."
            ) from error

    def _get_settings(
        self, config: Optional[Union[NpArrayColumnNames, NpArrayColumnDtypes]]
    ) -> Union[Dict[int, str], Dict[int, Type]]:
        if isinstance(config, type(None)):
            return {}
        if not isinstance(config, dict):
            if not self._np_array.ndim == 1:
                raise ValueError("non dict value can only be used for a 1D array")
            return {0: config}
        return config

    def _convert_to_series_values_and_type(
        self, obj: Tuple[int, "np.array"]
    ) -> Tuple[SeriesValues, InferType]:
        column = obj
        i = column[0]
        array = column[1]
        dtype = self._dtype.get(i, self._np_array.dtype)  # type: ignore
        if self._np.issubdtype(dtype, self._np.number):
            return self._convert_to_measure_values(array), InferType.MEASURE
        return self._convert_to_dimension_values(array), InferType.DIMENSION

    def _convert_to_measure_values(self, obj: "np.array") -> List[MeasureValue]:
        array = obj
        array_float = array.astype(float)
        return self._np.nan_to_num(
            array_float, nan=self._default_measure_value
        ).tolist()

    def _convert_to_dimension_values(self, obj: "np.array") -> List[DimensionValue]:
        array = obj
        array_str = array.astype(str)
        replace_nan = "nan"
        mask = array_str == replace_nan
        array_str[mask] = self._default_dimension_value
        return array_str.tolist()
