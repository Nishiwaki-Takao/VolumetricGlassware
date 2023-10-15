import warnings


def read_volume_checker(func):
    def wrapper(self, read_volume: float, *args: int) -> float:
        if read_volume >= self.capacity or read_volume < 0:
            warnings.warn("Your Read Value is invalid.(Over NominalCapacity or Negative value.)"
                          "\nYour value has corrected into your tool capacity.")
            read_volume = self.capacity
        for read_volume_arg in args:
            if abs(read_volume_arg) > 10 or abs(read_volume_arg) <= 0:
                warnings.warn("Your Read Value is invalid(Over 10 or lower -10)")
        result: float = func(self, read_volume, args)
        if result > self.capacity:
            warnings.warn("Your Read Value is invalid.The result is Overed NominalCapacity.")
            result = self.capacity
        return result

    return wrapper


class VolumeConvertor:
    def __init__(self, capacity: float, sub_division: float):
        self._Capacity = capacity
        self._Sub_Division = sub_division

    @property
    def Capacity(self) -> float:
        return self._Capacity

    @property
    def Sub_Division(self) -> float:
        return self._Sub_Division

    @read_volume_checker
    def convert_volume(self, read_volume: float, *args: int) -> float:
        if len(args) >= 3:
            warnings.warn(
                'It appears that the number of readings you have inputted is beyond what the program can handle. ')
            return 0
        no_of_pow = len(args) - 1
        result_volume = 0.0
        result_volume += round(read_volume / (self.Sub_Division * 10 ** no_of_pow), 0) \
                         * (self.Sub_Division * 10 ** no_of_pow)
        no_of_pow -= 1
        if 0 < len(args) <= 2:
            for arg in args:
                result_volume += round(arg / (self.Sub_Division * 10 ** no_of_pow), 0) \
                                 * (self.Sub_Division * 10 ** no_of_pow)
                no_of_pow -= 1
        return result_volume
