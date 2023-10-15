from VolumetricPipette import VolumetricPipette

class VolumetricPipettes:
    @staticmethod
    def classA01ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=.1,
                                 tolerance=0.005,
                                 grade="A",
                                 calibration="TD",
                                 color="Blue",
                                 number_of_ring=1)

    @staticmethod
    def classB01ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=.1,
                                 tolerance=0.01,
                                 grade="B",
                                 calibration="TD",
                                 color="Blue",
                                 number_of_ring=1)

    @staticmethod
    def classA015ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=.15,
                                 tolerance=0.005,
                                 grade="A",
                                 calibration="TD",
                                 color="White",
                                 number_of_ring=1)

    @staticmethod
    def classB015ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=.15,
                                 tolerance=0.01,
                                 grade="B",
                                 calibration="TD",
                                 color="White",
                                 number_of_ring=1)

    @staticmethod
    def classA02ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=.2,
                                 tolerance=0.005,
                                 grade="A",
                                 calibration="TD",
                                 color="Red",
                                 number_of_ring=1)

    @staticmethod
    def classB02ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=.2,
                                 tolerance=0.01,
                                 grade="B",
                                 calibration="TD",
                                 color="Red",
                                 number_of_ring=1)

    @staticmethod
    def classA025ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=.25,
                                 tolerance=0.005,
                                 grade="A",
                                 calibration="TD",
                                 color="Green",
                                 number_of_ring=2)

    @staticmethod
    def classB025ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=.25,
                                 tolerance=0.01,
                                 grade="B",
                                 calibration="TD",
                                 color="Green",
                                 number_of_ring=2)

    @staticmethod
    def classA03ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=.3,
                                 tolerance=0.005,
                                 grade="A",
                                 calibration="TD",
                                 color="Yellow",
                                 number_of_ring=1)

    @staticmethod
    def classB03ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=.3,
                                 tolerance=0.01,
                                 grade="B",
                                 calibration="TD",
                                 color="Yellow",
                                 number_of_ring=1)

    @staticmethod
    def classA04ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=.4,
                                 tolerance=0.005,
                                 grade="A",
                                 calibration="TD",
                                 color="Red",
                                 number_of_ring=2)

    @staticmethod
    def classB04ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=.4,
                                 tolerance=0.01,
                                 grade="B",
                                 calibration="TD",
                                 color="Red",
                                 number_of_ring=2)

    @staticmethod
    def classA05ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=.5,
                                 tolerance=0.005,
                                 grade="A",
                                 calibration="TD",
                                 color="Black",
                                 number_of_ring=2)

    @staticmethod
    def classB05ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=.5,
                                 tolerance=0.01,
                                 grade="B",
                                 calibration="TD",
                                 color="Black",
                                 number_of_ring=2)

    @staticmethod
    def classA1ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=1,
                                 tolerance=0.01,
                                 grade="A",
                                 calibration="TD",
                                 color="Blue",
                                 number_of_ring=1)

    @staticmethod
    def classB1ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=1,
                                 tolerance=0.02,
                                 grade="B",
                                 calibration="TD",
                                 color="Blue",
                                 number_of_ring=1)

    @staticmethod
    def classA2ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=2,
                                 tolerance=0.01,
                                 grade="A",
                                 calibration="TD",
                                 color="Orange",
                                 number_of_ring=1)

    @staticmethod
    def classB2ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=1,
                                 tolerance=0.02,
                                 grade="B",
                                 calibration="TD",
                                 color="Orange",
                                 number_of_ring=1)

    @staticmethod
    def classA3ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=3,
                                 tolerance=0.015,
                                 grade="A",
                                 calibration="TD",
                                 color="Black",
                                 number_of_ring=1)

    @staticmethod
    def classB3ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=3,
                                 tolerance=0.03,
                                 grade="B",
                                 calibration="TD",
                                 color="Black",
                                 number_of_ring=1)

    @staticmethod
    def classA4ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=4,
                                 tolerance=0.015,
                                 grade="A",
                                 calibration="TD",
                                 color="Red",
                                 number_of_ring=2)

    @staticmethod
    def classB4ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=4,
                                 tolerance=0.03,
                                 grade="B",
                                 calibration="TD",
                                 color="Red",
                                 number_of_ring=2)

    @staticmethod
    def classA5ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=5,
                                 tolerance=0.015,
                                 grade="A",
                                 calibration="TD",
                                 color="White",
                                 number_of_ring=1)

    @staticmethod
    def classB5ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=5,
                                 tolerance=0.03,
                                 grade="B",
                                 calibration="TD",
                                 color="White",
                                 number_of_ring=1)

    @staticmethod
    def classA6ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=6,
                                 tolerance=0.02,
                                 grade="A",
                                 calibration="TD",
                                 color="Orange",
                                 number_of_ring=2)

    @staticmethod
    def classB6ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=6,
                                 tolerance=0.04,
                                 grade="B",
                                 calibration="TD",
                                 color="Orange",
                                 number_of_ring=2)

    @staticmethod
    def classA7ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=7,
                                 tolerance=0.02,
                                 grade="A",
                                 calibration="TD",
                                 color="Green",
                                 number_of_ring=2)

    @staticmethod
    def classB7ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=7,
                                 tolerance=0.04,
                                 grade="B",
                                 calibration="TD",
                                 color="Green",
                                 number_of_ring=2)

    @staticmethod
    def classA8ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=8,
                                 tolerance=0.02,
                                 grade="A",
                                 calibration="TD",
                                 color="Blue",
                                 number_of_ring=1)

    @staticmethod
    def classB8ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=8,
                                 tolerance=0.04,
                                 grade="B",
                                 calibration="TD",
                                 color="Blue",
                                 number_of_ring=1)

    @staticmethod
    def classA9ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=9,
                                 tolerance=0.02,
                                 grade="A",
                                 calibration="TD",
                                 color="Black",
                                 number_of_ring=2)

    @staticmethod
    def classB9ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=9,
                                 tolerance=0.04,
                                 grade="B",
                                 calibration="TD",
                                 color="Black",
                                 number_of_ring=1)

    @staticmethod
    def classA10ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=10,
                                 tolerance=0.02,
                                 grade="A",
                                 calibration="TD",
                                 color="Red",
                                 number_of_ring=1)

    @staticmethod
    def classB10ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=10,
                                 tolerance=0.04,
                                 grade="B",
                                 calibration="TD",
                                 color="Red",
                                 number_of_ring=1)

    @staticmethod
    def classA15ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=15,
                                 tolerance=0.02,
                                 grade="A",
                                 calibration="TD",
                                 color="Green",
                                 number_of_ring=1)

    @staticmethod
    def classB15ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=15,
                                 tolerance=0.06,
                                 grade="B",
                                 calibration="TD",
                                 color="Green",
                                 number_of_ring=1)

    @staticmethod
    def classA20ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=20,
                                 tolerance=0.02,
                                 grade="A",
                                 calibration="TD",
                                 color="Yellow",
                                 number_of_ring=1)

    @staticmethod
    def classB20ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=20,
                                 tolerance=0.06,
                                 grade="B",
                                 calibration="TD",
                                 color="Yellow",
                                 number_of_ring=1)

    @staticmethod
    def classA25ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=25,
                                 tolerance=0.03,
                                 grade="A",
                                 calibration="TD",
                                 color="Blue",
                                 number_of_ring=1)

    @staticmethod
    def classB25ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=25,
                                 tolerance=0.06,
                                 grade="B",
                                 calibration="TD",
                                 color="Blue",
                                 number_of_ring=1)

    @staticmethod
    def classA30ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=30,
                                 tolerance=0.05,
                                 grade="A",
                                 calibration="TD",
                                 color="Black",
                                 number_of_ring=1)

    @staticmethod
    def classB30ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=30,
                                 tolerance=0.1,
                                 grade="B",
                                 calibration="TD",
                                 color="Black",
                                 number_of_ring=1)

    @staticmethod
    def classA40ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=40,
                                 tolerance=0.05,
                                 grade="A",
                                 calibration="TD",
                                 color="White",
                                 number_of_ring=1)

    @staticmethod
    def classB40ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=40,
                                 tolerance=0.1,
                                 grade="B",
                                 calibration="TD",
                                 color="White",
                                 number_of_ring=1)

    @staticmethod
    def classA50ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=50,
                                 tolerance=0.05,
                                 grade="A",
                                 calibration="TD",
                                 color="Red",
                                 number_of_ring=1)

    @staticmethod
    def classB50ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=50,
                                 tolerance=0.1,
                                 grade="B",
                                 calibration="TD",
                                 color="Red",
                                 number_of_ring=1)

    @staticmethod
    def classA75ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=75,
                                 tolerance=0.08,
                                 grade="A",
                                 calibration="TD",
                                 color="Green",
                                 number_of_ring=1)

    @staticmethod
    def classB75ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=75,
                                 tolerance=0.15,
                                 grade="B",
                                 calibration="TD",
                                 color="Green",
                                 number_of_ring=1)

    @staticmethod
    def classA100ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=100,
                                 tolerance=0.08,
                                 grade="A",
                                 calibration="TD",
                                 color="Yellow",
                                 number_of_ring=1)

    @staticmethod
    def classB100ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=100,
                                 tolerance=0.15,
                                 grade="B",
                                 calibration="TD",
                                 color="Yellow",
                                 number_of_ring=1)

    @staticmethod
    def classA150ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=150,
                                 tolerance=0.1,
                                 grade="A",
                                 calibration="TD",
                                 color="Black",
                                 number_of_ring=1)

    @staticmethod
    def classB150ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=150,
                                 tolerance=0.2,
                                 grade="B",
                                 calibration="TD",
                                 color="Black",
                                 number_of_ring=1)

    @staticmethod
    def classA200ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=200,
                                 tolerance=0.1,
                                 grade="A",
                                 calibration="TD",
                                 color="Blue",
                                 number_of_ring=1)

    @staticmethod
    def classB200ml() -> VolumetricPipette:
        return VolumetricPipette(capacity=200,
                                 tolerance=0.2,
                                 grade="B",
                                 calibration="TD",
                                 color="Blue",
                                 number_of_ring=1)
