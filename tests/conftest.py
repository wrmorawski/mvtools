import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def numerical_input_data():
    return pd.DataFrame(
        {
            "col1": [1, 2, 3, np.nan, 5, 6, np.nan, 8, 9, 10],
            "col2": [1.1, np.nan, 3.5, 4.4, np.nan, 6.1, 7.2, 8.8, np.nan, 10],
            "col3": [1, 1, 2, 3, 5, 8, 13, 21, 34, 55],
            "col4": [1.1, 5, 3.5, 4.7, 5, np.nan, 2.2, 8.1, np.nan, 20.0],
            "col5": [6, 3, 7, 1, 5, 3, 7, 23, 6, 2],
            # 'Category': pd.Categorical(['dog', 'cat', np.nan, 'mouse',
            # 'rabbit', 'dog', 'cat', 'rabbit', np.nan, 'rabbit']),
            # 'String': ['apple', 'banana', np.nan, 'cherry', 'date',
            # 'fig', 'grape', np.nan, 'honeydew', 'jackfruit'],
            # 'Datetime': pd.to_datetime(['2021-01-01', np.nan, '2021-01-03',
            # '2021-01-04', np.nan, '2021-01-06', '2021-01-07', '2021-01-08',
            # np.nan, '2021-01-10']),
            # 'Timedelta': pd.to_timedelta([np.nan, '1 days', '2 days',
            # np.nan, '4 days', '5 days', '6 days', np.nan,
            # '8 days', '9 days']),
            # 'Mixed': [1, 'two', 3, 4, 'five', np.nan, 7, 8, 9, 'ten']
        }
    )


@pytest.fixture
def numerical_output_data_mean():
    return pd.DataFrame(
        {
            "col1": [1, 2, 3, 5.5, 5, 6, 5.5, 8, 9, 10],
            "col2": [
                1.1,
                5.871428571428572,
                3.5,
                4.4,
                5.871428571428572,
                6.1,
                7.2,
                8.8,
                5.871428571428572,
                10.0,
            ],
            "col3": [1, 1, 2, 3, 5, 8, 13, 21, 34, 55],
            "col4": [1.1, 5, 3.5, 4.7, 5, 6.2, 2.2, 8.1, 6.2, 20.0],
            "col5": [6, 3, 7, 1, 5, 3, 7, 23, 6, 2],
        }
    )


@pytest.fixture
def numerical_output_data():
    return pd.DataFrame(
        {
            "col1": [1, 2, 3, 5.5, 5, 6, 5.5, 8, 9, 10],
            "col2": [1.1, 6.1, 3.5, 4.4, 6.1, 6.1, 7.2, 8.8, 6.1, 10.0],
            "col3": [1, 1, 2, 3, 5, 8, 13, 21, 34, 55],
            "col4": [1.1, 5, 3.5, 4.7, 5, 20.0, 2.2, 8.1, 20.0, 20.0],
            "col5": [6, 3, 7, 1, 5, 3, 7, 23, 6, 2],
        }
    )


@pytest.fixture
def simple_methods():
    return {"col1": "mean", "col2": "median", "col4": "max"}


@pytest.fixture
def data():
    df = {
        "col1": [1, 2, 3, np.nan, 5, 6, np.nan, 8, 9, 10],
        "col2": [1.1, np.nan, 3.5, 4.4, np.nan, 6.1, 7.2, 8.8, np.nan, 10.0],
        "col3": [
            "text1",
            "text2",
            "text3",
            "text4",
            "text5",
            "text6",
            "text7",
            "text8",
            "text9",
            "text10",
        ],
        "col4": [
            "dog",
            "cat",
            np.nan,
            "mouse",
            "rabbit",
            "dog",
            "cat",
            np.nan,
            "mouse",
            "rabbit",
        ],
        "col5": [1, 1, 2, 3, 5, 8, 13, 21, 34, 55],
    }

    yield pd.DataFrame(df)
