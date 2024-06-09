import pandas as pd

from mvtools.utils.messeges import COLUMN_NOT_FOUND, METHOD_NOT_FOUND

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

        if methods:
            for col, method in methods.items():
                if method in METHODS.keys() and col in data.columns:
                    value = METHODS[method](data[col])
                    data[col] = data[col].fillna(value)
                elif method not in METHODS.keys():
                    raise ValueError(METHOD_NOT_FOUND.format(method=method))
                elif col not in data.columns:
                    raise ValueError(COLUMN_NOT_FOUND.format(column=col))

        if default:
            if default in METHODS.keys():
                value = METHODS[default](data)
                data = data.fillna(value)
            else:
                raise ValueError(METHOD_NOT_FOUND.format(method=default))
        return data

    def fill():
        pass


# All methods, max, sum, mean, 0
# TODO add custom values to fill
# TODO default_method
