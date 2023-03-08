from ..Common.AbstractGlassware import  VolumetricGlassWare
from ..Common.Enums import Color


class VolumetricPipette(VolumetricGlassWare):
    def __init__(self, Capacity: float, Tolerance: float, Class: str, NewCalibration: str, ColorCode: dict):
        super().__init__(Capacity, Tolerance, Class, NewCalibration)
        self.color = Color(ColorCode['Color'])
        self.NomRing= ColorCode['NumberOfRing']

    def __str__(self) -> str:
        return f"This object represents {self.Capacity }\u00B1{self.Tolerance } ml Class {self.Class.name } volumetric pipette. ColorCode:{ self.colorCode }."
        
    def colorCode(self) -> str:
        pref = str
        if self.NomRing == 1:
            pref = ""
        else:
            pref = "{}x".format(self.NomRing)
        return pref + self.color.name




