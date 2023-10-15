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

    def unc_qnt(self, capacity=capacity) -> pq.UncertainQuantity:
        return pq.UncertainQuantity(capacity, pq.mL, self.uncertainty)