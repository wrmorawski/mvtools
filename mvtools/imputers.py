import pandas as pd

from mvtools.utils.messeges import NOT_FOUND_DEFAULT_METHOD

# methods = [
#     "mean",
#     "median",
#     "mean",
#     "max",
#     "min"
# ]

METHODS = {
    "mean": lambda df: df.mean(),
    "median": lambda df: df.median(),
    "max": lambda df: df.max(),
    "min": lambda df: df.min(),
}


class SimpleImputer:

    def impute(
        self,
        data: pd.DataFrame,
        methods: dict = None,
        default: str = None,
        skip: list = [],
    ) -> pd.DataFrame:

        if default is not None:
            if default in METHODS.keys():
                value = METHODS[default](data)
                data = data.fillna(value)
            else:
                raise ValueError(NOT_FOUND_DEFAULT_METHOD(default))
        return data

    def fill():
        pass


# All methods, max, sum, mean, 0
# TODO add custom values to fill
# TODO default_method
