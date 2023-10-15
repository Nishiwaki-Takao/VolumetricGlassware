from VolumetricFlask import VolumetricFlask, VolumetricFlaskWideNeck


class VolumetricFlasks:
    @staticmethod
    def createClassA5ml() -> VolumetricFlask:
        return VolumetricFlask(capacity=5,
                               tolerance=0.025,
                               grade="A",
                               dscore_max=10)

    @staticmethod
    def createClassB5ml() -> VolumetricFlask:
        return VolumetricFlask(capacity=5,
                               tolerance=0.05,
                               grade="B",
                               dscore_max=10)

    @staticmethod
    def createClassA10ml() -> VolumetricFlask:
        return VolumetricFlask(capacity=10,
                               tolerance=0.025,
                               grade="A",
                               dscore_max=10)

    @staticmethod
    def createClassB10ml() -> VolumetricFlask:
        return VolumetricFlask(capacity=10,
                               tolerance=0.05,
                               grade="B",
                               dscore_max=10)

    @staticmethod
    def createClassA20ml() -> VolumetricFlask:
        return VolumetricFlask(capacity=20,
                               tolerance=0.04,
                               grade="A",
                               dscore_max=12)

    @staticmethod
    def createClassB20ml() -> VolumetricFlask:
        return VolumetricFlask(capacity=20,
                               tolerance=0.08,
                               grade="B",
                               dscore_max=12)

    @staticmethod
    def createClassA25ml() -> VolumetricFlask:
        return VolumetricFlask(capacity=25,
                               tolerance=0.04,
                               grade="A",
                               dscore_max=12)

    @staticmethod
    def createClassB25ml() -> VolumetricFlask:
        return VolumetricFlask(capacity=25,
                               tolerance=0.08,
                               grade="B",
                               dscore_max=12)

    @staticmethod
    def createClassA50ml() -> VolumetricFlask:
        return VolumetricFlask(capacity=50,
                               tolerance=0.06,
                               grade="A",
                               dscore_max=14)

    @staticmethod
    def createClassB50ml() -> VolumetricFlask:
        return VolumetricFlask(capacity=50,
                               tolerance=0.12,
                               grade="B",
                               dscore_max=14)

    @staticmethod
    def createClassA100ml() -> VolumetricFlask:
        return VolumetricFlask(capacity=100,
                               tolerance=0.1,
                               grade="A",
                               dscore_max=14)

    @staticmethod
    def createClassB100ml() -> VolumetricFlask:
        return VolumetricFlask(capacity=100,
                               tolerance=0.2,
                               grade="B",
                               dscore_max=14)

    @staticmethod
    def createClassA200ml() -> VolumetricFlask:
        return VolumetricFlask(capacity=200,
                               tolerance=0.15,
                               grade="A",
                               dscore_max=17)

    @staticmethod
    def createClassB200ml() -> VolumetricFlask:
        return VolumetricFlask(capacity=200,
                               tolerance=0.3,
                               grade="B",
                               dscore_max=17)

    @staticmethod
    def createClassA250ml() -> VolumetricFlask:
        return VolumetricFlask(capacity=250,
                               tolerance=0.15,
                               grade="A",
                               dscore_max=17)

    @staticmethod
    def createClassB250ml() -> VolumetricFlask:
        return VolumetricFlask(capacity=250,
                               tolerance=0.3,
                               grade="B",
                               dscore_max=17)

    @staticmethod
    def createClassA300ml() -> VolumetricFlask:
        return VolumetricFlask(capacity=300,
                               tolerance=0.25,
                               grade="A",
                               dscore_max=24)

    @staticmethod
    def createClassB300ml() -> VolumetricFlask:
        return VolumetricFlask(capacity=300,
                               tolerance=0.5,
                               grade="B",
                               dscore_max=24)

    @staticmethod
    def createClassA500ml() -> VolumetricFlask:
        return VolumetricFlask(capacity=500,
                               tolerance=0.25,
                               grade="A",
                               dscore_max=24)

    @staticmethod
    def createClassB500ml() -> VolumetricFlask:
        return VolumetricFlask(capacity=500,
                               tolerance=0.5,
                               grade="B",
                               dscore_max=24)

    @staticmethod
    def createClassA1L() -> VolumetricFlask:
        return VolumetricFlask(capacity=1000,
                               tolerance=0.4,
                               grade="A",
                               dscore_max=24)

    @staticmethod
    def createClassB1L() -> VolumetricFlask:
        return VolumetricFlask(capacity=1000,
                               tolerance=0.8,
                               grade="B",
                               dscore_max=24)

    @staticmethod
    def createClassA2L() -> VolumetricFlask:
        return VolumetricFlask(capacity=2000,
                               tolerance=0.6,
                               grade="A",
                               dscore_max=30)

    @staticmethod
    def createClassB2L() -> VolumetricFlask:
        return VolumetricFlask(capacity=2000,
                               tolerance=1.2,
                               grade="B",
                               dscore_max=30)

    @staticmethod
    def createClassA2dot5L() -> VolumetricFlask:
        return VolumetricFlask(capacity=2500,
                               tolerance=1.5,
                               grade="A",
                               dscore_max=34)

    @staticmethod
    def createClassB2dot5L() -> VolumetricFlask:
        return VolumetricFlask(capacity=2500,
                               tolerance=3,
                               grade="B",
                               dscore_max=34)

    @staticmethod
    def createClassA3L() -> VolumetricFlask:
        return VolumetricFlask(capacity=3000,
                               tolerance=2,
                               grade="A",
                               dscore_max=36)

    @staticmethod
    def createClassB3L() -> VolumetricFlask:
        return VolumetricFlask(capacity=3000,
                               tolerance=4,
                               grade="B",
                               dscore_max=36)

    @staticmethod
    def createClassA5L() -> VolumetricFlask:
        return VolumetricFlask(capacity=5000,
                               tolerance=2,
                               grade="A",
                               dscore_max=50)

    @staticmethod
    def createClassB5L() -> VolumetricFlask:
        return VolumetricFlask(capacity=5000,
                               tolerance=4,
                               grade="B",
                               dscore_max=50)

    @staticmethod
    def createClassA10L() -> VolumetricFlask:
        return VolumetricFlask(capacity=10000,
                               tolerance=5,
                               grade="A",
                               dscore_max=65)

    @staticmethod
    def createClassB10L() -> VolumetricFlask:
        return VolumetricFlask(capacity=10000,
                               tolerance=10,
                               grade="B",
                               dscore_max=65)

    @staticmethod
    def createClassB50mlWide() -> VolumetricFlaskWideNeck:
        return VolumetricFlaskWideNeck(capacity=50,
                                       tolerance=0.2,
                                       grade="B",
                                       dscore_max=20,
                                       dscore_min=14)

    @staticmethod
    def createClassB100mlWide() -> VolumetricFlaskWideNeck:
        return VolumetricFlaskWideNeck(capacity=100,
                                       tolerance=0.25,
                                       grade="B",
                                       dscore_max=20,
                                       dscore_min=14)

    @staticmethod
    def createClassB200mlWide() -> VolumetricFlaskWideNeck:
        return VolumetricFlaskWideNeck(capacity=200,
                                       tolerance=0.3,
                                       grade="B",
                                       dscore_max=25,
                                       dscore_min=17)

    @staticmethod
    def createClassB250mlWide() -> VolumetricFlaskWideNeck:
        return VolumetricFlaskWideNeck(capacity=250,
                                       tolerance=0.3,
                                       grade="B",
                                       dscore_max=25,
                                       dscore_min=17)

    @staticmethod
    def createClassB500mlWide() -> VolumetricFlaskWideNeck:
        return VolumetricFlaskWideNeck(capacity=500,
                                       tolerance=0.3,
                                       grade="B",
                                       dscore_max=25,
                                       dscore_min=17)
