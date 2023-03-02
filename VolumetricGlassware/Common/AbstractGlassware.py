
from math import sqrt
from quantities import uncertainquantity,mL
from abc import ABC, abstractclassmethod
from Enums import Calibration, ToleranceClass


class VolumetricGlassWare(ABC):
    def __init__(self,
                 Capacity: float,
                 Tolerance: float,
                 Class: str,
                 Calibration: str):
        self.Capacity = Capacity
        self.Tolerance = Tolerance
        self.Class = ToleranceClass[Class]
        self._Calibration = Calibration[Calibration]
    
    @abstractclassmethod
    def __repr__(self) -> str:
        pass

    def _TDTCcheck(self) -> int:
        if self._Calibration in (Calibration.TD,Calibration.Ex,Calibration.Žó—p):
            return 1
        elif self._Calibration in (Calibration.TC,Calibration.In,Calibration.o—p):
            return -1
        else:
            return 0 

    def value(self) -> uncertainquantity:
        return uncertainquantity(self.Capacity, mL, self.Tolerance / sqrt(3))

    def _use(self)-> uncertainquantity:
        return self.value ** self.TDTCcheck() 

    def Caribrationfor(self) -> str:
        return str(self._Calibration.name)

class GraduatedGlassware(VolumetricGlassWare):














