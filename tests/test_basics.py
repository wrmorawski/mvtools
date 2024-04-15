import numpy as np
import pandas as pd
import pytest

from mvtools.basics import get_missing_values_columns


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


def test_get_missing_values_columns(data):
    result = get_missing_values_columns(data)
    assert result == list(["col1", "col2", "col4"])
