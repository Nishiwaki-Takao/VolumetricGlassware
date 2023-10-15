from GraduatedPipette import GraduatedPipette
from ..Common.Enums import Color
class GraduatedPipettes:
    @staticmethod
    def CreateClassA0dot1Green() -> GraduatedPipette:
        return GraduatedPipette(capacity=.1,
                                tolerance=0.005,
                                sub_division=0.001,
                                new_grade="A",
                                new_calibration='TD',
                                color=Color.Green.name,
                                number_of_ring=2)

    @staticmethod
    def CreateClassA0dot1Red() -> GraduatedPipette:
        return GraduatedPipette(capacity=.1,
                                tolerance=0.005,
                                sub_division=0.005,
                                new_grade="A",
                                new_calibration='TD',
                                color=Color.Red.name,
                                number_of_ring=1)

    @staticmethod
    def CreateClassA0dot1White() -> GraduatedPipette:
        return GraduatedPipette(capacity=.1,
                                tolerance=0.005,
                                sub_division=0.01,
                                new_grade="A",
                                new_calibration='TD',
                                color=Color.White.name,
                                number_of_ring=1)

    @staticmethod
    def CreateClassA0dot2Blue() -> GraduatedPipette:
        return GraduatedPipette(capacity=.2,
                                tolerance=0.005,
                                sub_division=0.001,
                                new_grade="A",
                                new_calibration='TD',
                                color=Color.Blue.name,
                                number_of_ring=2)

    @staticmethod
    def CreateClassA0dot2White() -> GraduatedPipette:
        return GraduatedPipette(capacity=.2,
                                tolerance=0.005,
                                sub_division=0.002,
                                new_grade="A",
                                new_calibration='TD',
                                color=Color.White.name,
                                number_of_ring=2)

    @staticmethod
    def CreateClassA0dot2Green() -> GraduatedPipette:
        return GraduatedPipette(capacity=.2,
                                tolerance=0.005,
                                sub_division=0.01,
                                new_grade="A",
                                new_calibration='TD',
                                color=Color.Black.name,
                                number_of_ring=1)
    @staticmethod
    def CreateClassA0dot5Green() -> GraduatedPipette:
        return GraduatedPipette(capacity=.2,
                                tolerance=0.005,
                                sub_division=0.005,
                                new_grade="A",
                                new_calibration='TD',
                                color=Color.Green.name,
                                number_of_ring=1)

    @staticmethod
    def CreateClassA0dot5Yellow() -> GraduatedPipette:
        return GraduatedPipette(capacity=.2,
                                tolerance=0.005,
                                sub_division=0.01,
                                new_grade="A",
                                new_calibration='TD',
                                color=Color.Yellow.name,
                                number_of_ring=1)
