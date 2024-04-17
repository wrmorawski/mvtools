import pandas as pd

methods = [
    "mean",
    "median",
    "mean",
]


class SimpleImputer:
    def __init__(self, methods: dict):
        self.methods = methods

    def fill(self, data: pd.DataFrame) -> pd.DataFrame:
        pass


# All methods, max, sum, mean, 0
# TODO add custom values to fill
# TODO default_method
