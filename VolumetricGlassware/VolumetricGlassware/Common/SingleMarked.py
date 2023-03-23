from AbstractGlassware import VolumetricGlassware
from abc import abstractmethod
import quantities as pq


class SingleMarked(VolumetricGlassware):
    @abstractmethod
    def __init__(self,
                 capacity: float,
                 tolerance: float,
                 new_class: str,
                 new_calibration: str):
        super().__init__(capacity, tolerance, new_class, new_calibration)

    def _unc_qnt(self):
        return pq.uncertainquantity(self.Capacity, pq.mL, self.uncertainty)
