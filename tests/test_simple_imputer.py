from pandas.testing import assert_frame_equal

from mvtools.imputers import SimpleImputer


def test_simple_imputer_fill_default(numerical_input_data, numerical_output_data_mean):
    imputer = SimpleImputer()
    results = imputer.impute(numerical_input_data, default="mean")
    assert_frame_equal(results, numerical_output_data_mean)


# def test_simple_imputer_fill_methods(
#     simple_methods, numerical_input_data, numerical_output_data,
#     methods
# ):
#     imputer = SimpleImputer(methods=simple_methods)
#     data = imputer.fill(numerical_input_data)
#     assert_frame_equal(data, numerical_output_data, methods)
# )

# def test_simple_imputer_fill_default(data):


#     default = 'mean'

#     imp = SimpleImputer()
#     results = imp.impute(data, default=default)


# def test_simple_imputer_fill_methods(data):
#     methods = {'col1': 'mean', 'col2': 'median', 'col4': 'max'}

#     imp = SimpleImputer
#     results = imp.impute(data, methods=methods)
