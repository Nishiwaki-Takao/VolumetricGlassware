import warnings
import quantities as pq


class ToDeliverDrop(pq.UncertainQuantity):
    def __rsub__(self, other):
        warnings.warn('''"To Deliver" Glassware library is to pick solution up.\n
                        This operator is disabled. Find another way.''')
        return other

    def __rtruediv__(self, other) -> None:
        warnings.warn('''"To Deliver" Glassware library is to pick solution up.\n
                        This operator is disabled. Find another way.''')
        return other



