import warnings

import quantities as pq
from VolumetricGlassware import VolumetricGlassware
from ..Common.MultipleMarked import MultipleMarked
from ..Common.VolumeConvertor import VolumeConvertor, read_volume_checker
from typing import Tuple, List, Union

def list_length_lower_checker(list_attr_name: str, list_length_lower_limit: int, warning_message: str):
    def decorator(func):
        def wrapper(self: MultipleMarked, *args):
            if hasattr(self, list_attr_name) and len(getattr(self, list_attr_name)) >= list_length_lower_limit:
                return func(self, *args)
            else:
                warnings.warn(warning_message)
        return wrapper
    return decorator


class Burette(VolumetricGlassware):
    def __init__(self, capacity: float, tolerance: float, sub_division: float, new_grade: str, new_calibration: str):
        super().__init__(capacity, tolerance, new_grade, new_calibration)
        self._Volume_Convertor = VolumeConvertor(capacity, sub_division)
        self._ZeroPoint: float = float(0)
        self._EndPoints: list[float] = []
    @property
    def ZeroPoint(self):
        return pq.UncertainQuantity(self._ZeroPoint, pq.mL, self.uncertainty)

    @ZeroPoint.setter
    @read_volume_checker
    def ZeroPoint(self, read_value=float(0), *args: int):
        self._ZeroPoint: float = self._Volume_Convertor.convert_volume(read_value, *args)
        if self._ZeroPoint > self._EndPoint:
            self._EndPoint = self._ZeroPoint
            warnings.warn('New Zero point is higher than End point. Both point have same value now.')

    @property
    @list_length_lower_checker("_EndPoints", 2, 'you need to set your read value to show this present value.')
    def integrated_value_list(self)  -> List[pq.UncertainQuantity]:
        return [pq.UncertainQuantity(self._EndPoints[i], pq.mL, self.uncertainty) - self.ZeroPoint
                for i in range(len(self._EndPoints))]

    @property
    @list_length_lower_checker("_EndPoints", 2, 'you need to set your read value to show this present value.')
    def difference_value_list(self) -> List[pq.UncertainQuantity]:

        return
