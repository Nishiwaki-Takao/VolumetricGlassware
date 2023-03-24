from AbstractGlassware import VolumetricGlassware
from abc import abstractmethod
import quantities as pq


class SingleMarked(VolumetricGlassware):
    @abstractmethod
    def __init__(self,
                 capacity: float,
                 tolerance: float,
                 new_grade: str,
                 new_calibration: str):
        super().__init__(capacity, tolerance, new_grade, new_calibration)

    def unc_qnt(self) -> pq.UncertainQuantity:
        return pq.uncertainquantity(self.Capacity, pq.mL, self.uncertainty)
