import quantities as pq
from abc import ABC, abstractmethod


class VolumetricGlassware(ABC):
    @abstractmethod
    def __init__(self,
                 capacity: float,
                 tolerance: float,
                 new_grade: str,
                 new_calibration: str):
        ...

    @property
    def capacity(self) -> float:
        ...

    @property
    def tolerance(self) -> float:
        ...

    @property
    def uncertainty(self) -> float:
        ...

    @property
    def grade(self) -> str:
        ...

    @property
    def calibration(self) -> str:
        ...
    @property
    def _unc_qnt(self,capacity:float = capacity) -> pq.UncertainQuantity:
        ...
    @abstractmethod
    def __repr__(self) -> str:
        ...

    @abstractmethod
    def __str__(self) -> str:
        ...

    @abstractmethod
    def __add__(self, other) -> pq.UncertainQuantity:
        ...

    @abstractmethod
    def __iadd__(self, other) -> pq.UncertainQuantity:
        ...

    @abstractmethod
    def __radd__(self, other) -> pq.UncertainQuantity:
        ...

    @abstractmethod
    def __sub__(self, other) -> pq.UncertainQuantity:
        ...

    @abstractmethod
    def __isub__(self, other) -> pq.UncertainQuantity:
        ...

    @abstractmethod
    def __rsub__(self, other) -> pq.UncertainQuantity:
        ...

    @abstractmethod
    def __mul__(self, other) -> pq.UncertainQuantity:
        ...

    @abstractmethod
    def __imul__(self, other) -> pq.UncertainQuantity:
        ...

    def __floordiv__(self, other) -> None:
        ...

    def __rfloordiv__(self, other) -> None:
        ...
    @abstractmethod
    def __truediv__(self, other) -> pq.UncertainQuantity:
        ...
    @abstractmethod
    def __mod__(self, other) -> pq.UncertainQuantity:
        ...

    @abstractmethod
    def __imod__(self, other) -> pq.UncertainQuantity:
        ...
    @abstractmethod
    def __pow__(self, other) -> pq.UncertainQuantity:
        ...