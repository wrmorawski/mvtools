import pytest
from pandas.testing import assert_frame_equal

from mvtools.imputers import SimpleImputer


def test_simple_imputer_fill_default(numerical_input_data, numerical_output_data_mean):
    imputer = SimpleImputer()
    results = imputer.impute(numerical_input_data, default="mean")
    assert_frame_equal(results, numerical_output_data_mean)


def test_simple_imputer_fill_default_fail(numerical_input_data):
    imputer = SimpleImputer()
    with pytest.raises(ValueError) as e:
        results = imputer.impute(numerical_input_data, default="piwo")
    assert str(e.value) == "Method piwo not found in available methods"


def test_simple_imputer_fill_methods(
    simple_methods, numerical_input_data, numerical_output_data
):
    imputer = SimpleImputer()
    results = imputer.impute(numerical_input_data, methods=simple_methods)
    assert_frame_equal(results, numerical_output_data)


def test_simple_imputer_fill_methods_fail(numerical_input_data):
    imputer = SimpleImputer()
    with pytest.raises(ValueError) as e:
        results = imputer.impute(numerical_input_data, methods={"col1": "piwo"})
    assert str(e.value) == "Method piwo not found in available methods"


def test_simple_imputer_fill_no_column_fail(numerical_input_data):
    imputer = SimpleImputer()
    with pytest.raises(ValueError) as e:
        results = imputer.impute(numerical_input_data, methods={"zurek": "mean"})
    print(e.value)
    assert str(e.value) == "Column zurek not found in data"
