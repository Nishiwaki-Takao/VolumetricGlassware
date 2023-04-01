import quantities as pq
from MultipleMarked import MultipleMarked
class VolumeConvertor:
    def __init__(self, key:int, parent_object : MultipleMarked) -> None:
        self._parentObject = parent_object
        self._key = key

    def __volume_convertor(self, read_volume: float, read_mentally_division: int) -> float:
        return self._parentObject.volume_convertor(read_volume,read_mentally_division)

    def update_read_value(self,read_volume: float, read_mentally_division=0):
        self._parentObject[self._key] = self.__volume_convertor(read_volume, read_mentally_division)




