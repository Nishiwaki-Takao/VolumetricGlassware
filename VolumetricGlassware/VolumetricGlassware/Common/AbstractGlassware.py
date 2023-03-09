from asyncio.windows_events import NULL
from operator import mul, truediv
from math import sqrt
import quantities as pq
from abc import ABC, abstractclassmethod
from Enums import Calibration, ToleranceClass
from Typing import Union



class VolumetricGlassWare(ABC):
    def __init__(self,
                 Capacity: float,
                 Tolerance: float,
                 Class: str,
                 NewCalibration: str):
        self.Capacity = Capacity
        self.Tolerance = Tolerance
        self.Class = ToleranceClass[Class]
        self.Calibration = Calibration[NewCalibration]
    
    @abstractclassmethod
    def __repr__(self) -> str:
        pass

    def _TDTCcheck(self) -> function:
        if self.Calibration in (Calibration.TD,Calibration.Ex,Calibration.Žó—p):
            return mul
        elif self.Calibration in (Calibration.TC,Calibration.In,Calibration.o—p):
            return truediv
        else:
            return None

    def value(self,WithUncertain = True) -> Union(pq.Quantity,pq.UncertainQuantity):
        if WithUncertain == True:
            return pq.UncertainQuantity(self.Capacity, pq.mL, self.Tolerance / sqrt(3))
        else:
            return pq.Quantity(self.Capacity,pq.mL)

    def _use(self)-> tuple:
        return (self.TDTCcheck(), self.value)


    def Caribrationfor(self) -> str:
        return str(self.Calibration.name)

#class GraduatedGlassware(VolumetricGlassWare):














