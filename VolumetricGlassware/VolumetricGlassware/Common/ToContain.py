import warnings


class ToContain:
    def __rmul__(self, other) -> None:
        warnings.warn('''"To Contain" Glassware library is to diffuse solution.\n
                        This operator is disabled. Find another way.''')