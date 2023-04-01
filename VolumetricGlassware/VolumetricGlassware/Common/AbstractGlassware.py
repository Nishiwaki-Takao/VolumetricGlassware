from math import sqrt
import quantities as pq
from abc import ABC, abstractmethod
from Enums import Calibration, ToleranceClass
import warnings
from typing import Union


class VolumetricGlassware(ABC):
    @abstractmethod
    def __init__(self,
                 capacity: float,
                 tolerance: float,
                 new_grade: str,
                 new_calibration: str):
        self.Capacity = capacity
        self.Tolerance = tolerance
        self.Grade = ToleranceClass[new_grade]
        self.Calibration = Calibration[new_calibration]

    @property
    def capacity(self) -> float:
        return self.Capacity

    @property
    def tolerance(self) -> float:
        return self.Tolerance

    @property
    def uncertainty(self) -> float:
        return self.Tolerance/sqrt(6)

    @property
    def grade(self) -> str:
        return self.Grade.name

    @property
    def calibration(self) -> str:
        return self.Calibration.name

    @abstractmethod
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.Capacity},{self.Tolerance},{self.Class},{self.Calibration},'

    @abstractmethod
    def __str__(self) -> str:
        return f'VlmTlr:{self.Capacity}+/-{self.Tolerance} ml Cls:{self.Class} Clb:{self.Calibration}'

    @abstractmethod
    def __add__(self, other) -> pq.UncertainQuantity:
        pass
    @abstractmethod
    def __iadd__(self, other) -> pq.UncertainQuantity:
        pass

    @abstractmethod
    def __radd__(self, other) -> pq.UncertainQuantity:
        pass
    @abstractmethod
    def __sub__(self, other) -> pq.UncertainQuantity:
        pass
    @abstractmethod
    def __isub__(self, other) -> pq.UncertainQuantity:
        pass
    @abstractmethod
    def __rsub__(self, other) -> pq.UncertainQuantity:
        pass
    @abstractmethod
    def __mul__(self, other) -> pq.UncertainQuantity:
        pass
    @abstractmethod
    def __imul__(self, other) -> pq.UncertainQuantity:
        pass

    @abstractmethod
    def __rmul__(self, other) -> Union[None, pq.UncertainQuantity]:
        pass

    def __floordiv__(self, other) -> None:
        warnings.warn('''Volumetric Glassware library is to discuss uncertainty.\n
                        This operator is disabled. Let's think outside the box and come up with a new strategy.''')

    def __rfloordiv__(self, other) -> None:
        warnings.warn('''Volumetric Glassware library is to discuss uncertainty.\n
                        This operator is disabled. Let's think outside the box and come up with a new strategy.''')
    @abstractmethod
    def __truediv__(self, other) -> pq.UncertainQuantity:
        pass
    @abstractmethod
    def __rtruediv__(self, other) -> Union[None, pq.UncertainQuantity]:
        pass
    @abstractmethod
    def __mod__(self, other) -> pq.UncertainQuantity:
        pass

    @abstractmethod
    def __imod__(self, other) -> pq.UncertainQuantity:
        pass
    @abstractmethod
    def __pow__(self, other) -> pq.UncertainQuantity:
        pass

'''class GraduatedGlassware(VolumetricGlassWare):
    def __init__(self, Capacity: float, Tolerance: float, Class: str, NewCalibration: str,subdivision: float):
        super().__init__(Capacity, Tolerance, Class, NewCalibration)
        self.SubDivision = subdivision
        self.ReadValues = pq.

    def value(self, WithUncertain = True) -> Union(pq.Quantity, pq.UncertainQuantity):
        if WithUncertain == True:
            return pq.UncertainQuantity(self.Capacity, pq.mL, self.Tolerance / sqrt(3))
        else:
            return pq.Quantity(self.Capacity, pq.mL)
    def _AppendValue(self, f) -> None:
        self.value

    def read_value(self, VRead :float, MentalyDivision :int = 0) -> float:
        if VRead <= self.Capacity or VRead < 0: raise ValueError("Your Read Value is invalid(Over NominalCapacity or Negative value.)")
        if MentalyDivision <= 10 or MentalyDivision < 0: raise ValueError("Mentaly Division is invalid(Over 10 or Negative value.)")
        self.ReadValues[-1] =round((VRead + self.SubDivision / 10 * MentalyDivision)/(self.SubDivision /10),0)*self.SubDivision/10
+       return self.ReadValues[-1] '''