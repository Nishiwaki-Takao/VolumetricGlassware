from enum import Enum,StrEnum, auto


class Calibration(Enum):
	éÛóp = -3
	TC =-2
	In = -1
	Ex = 1
	TD = 2
	èoóp = 3
class ToleranceClass(StrEnum):
	A = auto()
	B = auto()
	SuperGrade = auto()
	HighGrade = auto()

class Color(StrEnum):
	Blue = auto()
	White = auto()
	Red = auto()
	Green = auto()
	Yellow = auto()
	Orange = auto()
	Black = auto()
