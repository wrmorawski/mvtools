from pandas.testing import assert_frame_equal

from mvtools.imputers import SimpleImputer


def test_simple_imputer_fill_basic(
    simple_methods, numerical_input_data, numerical_output_data
):
    imputer = SimpleImputer(methods=simple_methods)
    data = imputer.fill(numerical_input_data)
    assert_frame_equal(data, numerical_output_data)
