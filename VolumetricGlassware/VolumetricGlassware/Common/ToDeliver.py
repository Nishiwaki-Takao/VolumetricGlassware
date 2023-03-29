import warnings


class ToDeliver:
    def __rtruediv__(self, other) -> None:
        warnings.warn('''"To Deliver" Glassware library is to pick solution up.\n
                        This operator is disabled. Find another way.''')