
from MultipleMarked import MultipleMarked,read_volume_checker


class VolumeElementHandler:
    def __init__(self, key: int, parent_object: MultipleMarked) -> None:
        self._parentObject = parent_object
        self._key = key

    @read_volume_checker
    def update_read_value(self,read_volume: float, read_mentally_division=0):
        self._parentObject[self._key] = self._parentObject.volume_convertor(read_volume, read_mentally_division)

    def delete_read_value(self):
        del self._parentObject[self._key]
