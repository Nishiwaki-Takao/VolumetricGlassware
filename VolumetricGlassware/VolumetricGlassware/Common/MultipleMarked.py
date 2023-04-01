from abc import abstractmethod

from VolumetricGlassware import VolumetricGlassware
from VolumeConvertor import VolumeConvertor
import quantities as pq



def data_check_convertor(func):
    def wrapper(self,*args,data):
        if isinstance(data, pq.UncertainQuantity) \
                and data.magnitude <= self.capacity \
                and data.units == pq.ml:
            result=data
            func(self,*args,result)
        elif isinstance(data, tuple) and len(data) == 2:
            result= pq.UncertainQuantity(data=self.volume_convertor(data[0],data[1]),
                                        units=pq.ml,
                                        uncertainty=self.uncertainty)
            func(self,*args,result)
        elif isinstance(data, float) and data <= self.capacity:
            result = pq.UncertainQuantity(data=self.volume_convertor(data),
                                        units=pq.ml,
                                        uncertainty=self.uncertainty)
            func(self,*args,result)
        else:
            raise ValueError("Invalid input")
    return wrapper


def read_volume_checker(func):
    def wrapper(self,read_volume:float,read_mentally_division:int):
        if read_volume <= self.capacity or read_volume < 0: raise ValueError(
            "Your Read Value is invalid(Over NominalCapacity or Negative value.)")
        if abs(read_mentally_division) <= 10 or read_mentally_division < 0: raise ValueError(
            "Mentally Division is invalid(Over 10 or lower -10)")
        return func(self,read_volume,read_mentally_division)
    return wrapper


class MultipleMarked(VolumetricGlassware):
    @abstractmethod
    def __init__(self,
                 capacity: float,
                 tolerance: float,
                 sub_division: float,
                 new_grade: str,
                 new_calibration: str):
        super().__init__(capacity, tolerance, new_grade, new_calibration)
        self.SubDivision = sub_division
        self._value_list = [].append(pq.UncertainQuantity(data=0, units=pq.ml, uncertainty=self.uncertainty))
    @property
    def subdivision(self) ->float:
        return self.SubDivision

    def __len__(self):
        return len(self._value_list)

    def __getitem__(self, index):
        return VolumeConvertor(key=index, parent_object=self)

    @data_check_convertor
    def __setstate__(self, index, value):
            self._value_list[index] = value
    def __delitem__(self, key):
        del self._value_list[key]

    def __contains__(self, item):
        if isinstance(item, pq.UncertainQuantity):

    @read_volume_checker
    def volume_convertor(self, read_volume: float, read_mentally_division=0) -> float:
            return round((read_volume + self.subdivision / 10 * read_mentally_division) / (self.subdivision / 10),
                0) * self.subdivision / 10





