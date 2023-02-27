from telnetlib import SE
from uncertainties import ufloat
from abc import ABC
import Enums


class VolumetricGlassWare(ABC):
    def __init__(self,
                 Capacity: float,
                 Tolerance: float,
                 Class: str,
                 Calibration: str):
        self._Capacity = Capacity
        self._Tolerance = Tolerance
        self._Class = Enums.ToleranceClass[Class]
        self._Calibration = Enums.Calibration[Calibration]
        self.







