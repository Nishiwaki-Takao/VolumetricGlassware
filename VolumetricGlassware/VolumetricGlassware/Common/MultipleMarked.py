from abc import abstractmethod
from math import copysign
from VolumetricGlassware import VolumetricGlassware
from VolumeConvertor import VolumeConvertor,read_volume_checker
from typing import Tuple, List, Union
import quantities as pq
import warnings





class MultipleMarked(VolumetricGlassware):
    @abstractmethod
    def __init__(self,
                 capacity: float,
                 tolerance: float,
                 sub_division: float,
                 new_grade: str,
                 new_calibration: str):
        super().__init__(capacity, tolerance, new_grade, new_calibration)
        self.volume_convertor = VolumeConvertor(capacity,sub_division)
        self.reset_glassware()
        self._ZeroPoint = 0.0
        self._EndPoint = self.capacity
        self.reset_glassware()

    @property
    def subdivision(self) -> float:
        return self.volume_convertor.Sub_Division

    def __len__(self):
        return 2

    def __getitem__(self, index):
        if isinstance(index, int):
            if index == 0:
                return self._ZeroPoint
            elif index == 1:
                return self._EndPoint
            else:
                raise ValueError('Your index is out of range.')

    def __setitem__(self, key: int, value: float):
        if key == 0:
            self._ZeroPoint = self.volume_convertor.convert_volume(value)
        elif key == 1:
            self._EndPoint = self.volume_convertor.convert_volume(value)
        else:
            raise ValueError('Your index is out of range.')

    def reset_glassware(self, read_volume=0.0, *args: int):
        self._ZeroPoint = self.volume_convertor.convert_volume(read_volume, *args)
        self._EndPoint = self._ZeroPoint
    @list_length_lower_checker("_value_list", 2, 'you need to set your read value to show this present value.')
    def present_value(self) -> pq.UncertainQuantity:
        return self.unc_qnt(self._EndPoint - self._ZeroPoint)




