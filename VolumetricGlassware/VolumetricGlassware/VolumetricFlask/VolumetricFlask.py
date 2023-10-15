from typing import Union

import quantities as pq
from ..Common.SingleMarked import SingleMarked
from ..Common.ToContainSolution import ToContainSolution


class VolumetricFlask(SingleMarked):

    def __init__(self, capacity: float, tolerance: float, grade: str, dscore_max: int):
        super().__init__(capacity, tolerance, grade, "TC")
        self.Narrow_Wide = "Narrow"
        self.Dscore_Max = dscore_max

    @property
    def narrow_wide(self) -> str:
        return self.Narrow_Wide

    @property
    def dscore_max(self) -> int:
        return self.Dscore_Max

    def __unc_qnt(self) -> ToContainSolution:
        return ToContainSolution(self.capacity, pq.mL, self.uncertainty*2)

    def __repr__(self) -> str:
        s = super().__repr__()
        s = s + f'N/W:{self.narrow_wide},dscore_max:{self.dscore_max})'
        return s

    def __str__(self) -> str:
        return f"This object is {self.Capacity}+/-{self.Tolerance} ml Class {self.grade} volumetric flask." \
               f" Necks Nrw/Wid:{self.narrow_wide} max inner diameter:{self.dscore_max}mm."

    def __add__(self, other) -> pq.UncertainQuantity:
        return self.__unc_qnt().__add__(other)

    def __iadd__(self, other) -> pq.UncertainQuantity:
        return self.__unc_qnt().__iadd__(other)

    def __radd__(self, other) -> pq.UncertainQuantity:
        return self.__unc_qnt().__radd__(other)

    def __sub__(self, other) -> pq.UncertainQuantity:
        return self.__unc_qnt().__sub__(other)

    def __isub__(self, other) -> pq.UncertainQuantity:
        return self.__unc_qnt().__isub__(other)

    def __rsub__(self, other) -> pq.UncertainQuantity:
        return self.__unc_qnt().__rsub__(other)

    def __mul__(self, other) -> pq.UncertainQuantity:
        return self.__unc_qnt().__mul__(other)

    def __imul__(self, other) -> pq.UncertainQuantity:
        return self.__unc_qnt().__imul__(other)

    def __rmul__(self, other) -> Union[None, pq.UncertainQuantity]:
        return ToContainSolution.__rmul__(other)

    def __truediv__(self, other) -> pq.UncertainQuantity:
        return self.__unc_qnt().__truediv__(other)

    def __rtruediv__(self, other) -> Union[None, pq.UncertainQuantity]:
        return self.__unc_qnt().__rtruediv__(other)

    def __mod__(self, other) -> pq.UncertainQuantity:
        return self.__unc_qnt().__mod__(other)

    def __imod__(self, other) -> pq.UncertainQuantity:
        return self.__unc_qnt().__imod__(other)

    def __pow__(self, other) -> pq.UncertainQuantity:
        return self.__unc_qnt().__pow__(other)


class VolumetricFlaskWideNeck(VolumetricFlask):
    def __init__(self, capacity: float, tolerance: float, grade: str, dscore_max: int, dscore_min):
        super().__init__(capacity, tolerance, grade, dscore_max)
        self.Narrow_Wide = "Wide"
        self.Dscore_Min = dscore_min

    def __repr__(self):
        s = super().__repr__()
        s.replace(')', '')
        s = s + f', dscore_min:{self.dscore_min})'
        return s

    def __str__(self):
        s = super().__str__()
        s.replace(')','')
        s = s + f',inner min diameter on mark; {self.dscore_min} mm '

    @property
    def dscore_min(self) -> int:
        return self.Dscore_Min

