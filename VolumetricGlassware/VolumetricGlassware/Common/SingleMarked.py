from AbstractGlassware import VolumetricGlassware
from abc import abstractmethod
import quantities as pq
from typing import Union
import warnings


class SingleMarked(VolumetricGlassware):
    @abstractmethod
    def __init__(self,
                 capacity: float,
                 tolerance: float,
                 new_grade: str,
                 new_calibration: str):
        super().__init__(capacity, tolerance, new_grade, new_calibration)

    @abstractmethod
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.capacity},{self.tolerance},{self.grade},{self.calibration},'

    @abstractmethod
    def __str__(self) -> str:
        return f'VlmTlr:{self.capacity}+/-{self.tolerance} ml Cls:{self.grade} Clb:{self.calibration}'

    @abstractmethod
    def __add__(self, other) -> pq.UncertainQuantity:
        pass

    @abstractmethod
    def __radd__(self, other) -> pq.UncertainQuantity:
        pass

    @abstractmethod
    def __sub__(self, other) -> pq.UncertainQuantity:
        pass

    @abstractmethod
    def __rsub__(self, other) -> pq.UncertainQuantity:
        pass

    @abstractmethod
    def __mul__(self, other) -> pq.UncertainQuantity:
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
    def __pow__(self, other) -> pq.UncertainQuantity:
        pass

