import quantities as pq
class ToContainSolution(pq.UncertainQuantity):
    def __rmul__(self, other) -> None:
        ...
