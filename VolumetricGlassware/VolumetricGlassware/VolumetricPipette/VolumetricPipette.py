from typing import Union

import quantities as pq
from ..Common.SingleMarked import SingleMarked
from ..Common.ToDeliver import ToDeliver
from ..Common.Enums import Color


class VolumetricPipette(SingleMarked, ToDeliver):

    def __init__(self, capacity: float, tolerance: float, grade: str, calibration: str, color: str,
                 number_of_ring: int):
        super().__init__(capacity, tolerance, grade, calibration)
        self.color = Color[color]
        self.NomRing = number_of_ring

    def __repr__(self) -> str:
        s = super().__repr__()
        s = s + f'color:{self.color},number of ring:{self.NomRing})'
        return s

    def __str__(self) -> str:
        return f"This object represents {self.Capacity}+/-{self.Tolerance} ml Class {self.grade} volumetric " \
               f"pipette. ColorCode:{self.color_code()}. "

    def color_code(self) -> str:
        if self.NomRing == 1:
            pref = ""
        else:
            pref = "{}x".format(self.NomRing)
        return pref + self.color.name

    def __add__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__add__(other)

    def __iadd__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__iadd__(other)

    def __radd__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__radd__(other)

    def __sub__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__sub__(other)

    def __isub__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__isub__(other)

    def __rsub__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__rsub__(other)

    def __mul__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__mul__(other)

    def __imul__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__imul__(other)

    def __rmul__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__rmul__(other)

    def __truediv__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__truediv__(other)

    def __rtruediv__(self, other) -> None:
        return ToDeliver.__rtruediv__(other)

    def __mod__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__mod__(other)

    def __imod__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__imod__(other)

    def __pow__(self, other) -> pq.UncertainQuantity:
        return self.unc_qnt().__pow__(other)
