import warnings
import quantities as pq


class ToContainSolution(pq.UncertainQuantity):
    def __rmul__(self, other) -> None:
        warnings.warn('''"To Contain" Glassware library is to diffuse solution.\n
                        This operator is disabled. Find another way.''')