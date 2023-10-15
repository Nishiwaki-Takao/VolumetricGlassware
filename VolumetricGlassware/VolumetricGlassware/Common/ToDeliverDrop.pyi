import quantities as pq
class ToDeliverDrop(pq.UncertainQuantity):
    def __rsub__(self, other):
        ...

    def __rtruediv__(self, other):
        ...