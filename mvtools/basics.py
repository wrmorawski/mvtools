"""This module consists of basic functions for missing values analysis."""

import pandas as pd


def get_missing_values_columns(df: pd.DataFrame, as_list=True):
    """Function to get all column names where any value is missing.

    Args:
        df (pd.DataFrame): Our data

    Returns:
        list[str]: List of columns
    """
    return df.columns[df.isna().any()].to_list()
