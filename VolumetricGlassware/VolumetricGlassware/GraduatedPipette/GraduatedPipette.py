import warnings

import quantities as pq
from ..VolumetricPipette import VolumetricPipette
from ..Common.VolumeConvertor import VolumeConvertor, read_volume_checker


class GraduatedPipette(VolumetricPipette):
    def __init__(self, capacity: float, tolerance: float,sub_division: float,  new_grade: str, new_calibration: str, color: str,
                 number_of_ring: int):
        super().__init__(capacity, tolerance, new_grade, new_calibration, color, number_of_ring)
        self._Volume_Convertor = VolumeConvertor(capacity, sub_division)
        self._ZeroPoint: float = float(0)
        self._EndPoint: float = capacity

    @property
    def Sub_Division(self):
        return self._Volume_Convertor.Sub_Division

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
    def EndPoint(self):
        return pq.UncertainQuantity(self._EndPoint, pq.mL, self.uncertainty)

    @EndPoint.setter
    @read_volume_checker
    def EndPoint(self, read_value=float(0), *args: int):
        if self._ZeroPoint < self._Volume_Convertor.convert_volume(read_value, *args):
            self._EndPoint = self._Volume_Convertor.convert_volume(read_value, *args)
        else:
            warnings.warn('You input a lower value than the Zero Point. Update the End Point has canceled.')

    def unc_qnt(self):
        return pq.UncertainQuantity(self.EndPoint, pq.mL, self.uncertainty) \
            - pq.UncertainQuantity(self.ZeroPoint, pq.mL, self.uncertainty)

    def __repr__(self) -> str:
        s = super().__repr__()
        s = s + f'color:{self.color},number of ring:{self.NomRing})'
        return s

    def __str__(self) -> str:
        return f"This object represents {self.Capacity}+/-{self.Tolerance} ml Class {self.grade} volumetric " \
               f"pipette. ColorCode:{self.color_code()}. "

    def color_code(self) -> str:
        if self.NomRing == 1:
            pref = ""
        else:
            pref = "{}x".format(self.NomRing)
        return pref + self.color.name

    def __add__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__add__(other)

    def __iadd__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__iadd__(other)

    def __radd__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__radd__(other)

    def __sub__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__sub__(other)

    def __isub__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__isub__(other)

    def __rsub__(self, other):
        return self.ToDeliver.__rsub__(other)

    def __mul__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__mul__(other)

    def __imul__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__imul__(other)

    def __rmul__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__rmul__(other)

    def __truediv__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__truediv__(other)

    def __rtruediv__(self, other) -> None:
        return self.ToDeliver.__rtruediv__(other)

    def __mod__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__mod__(other)

    def __imod__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__imod__(other)

    def __pow__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__pow__(other)
