
from math import sqrt
from quontities  catch_warnings
from uncertainties import ufloat
from abc import ABC
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

    def TDTCcheck(self) -> int:
        if self._Calibration in (Calibration.TD,Calibration.Ex,Calibration.Žó—p):
            return 1
        elif self._Calibration in (Calibration.TC,Calibration.In,Calibration.o—p):
            return -1
        else:
            return 0 

    def value(self) -> ufloat:
        return ufloat(self.Capacity,self.Tolerance / sqrt(3))

    def _usage(self)-> ufloat:
        return self.value ** self.TDTCcheck() 

    def Caribrationfor(self) -> str:
        return str(self._Calibration.name)














