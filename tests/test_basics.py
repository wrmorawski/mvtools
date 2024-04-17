from mvtools.basics import get_missing_values_columns


def test_get_missing_values_columns(data):
    result = get_missing_values_columns(data)
    assert result == list(["col1", "col2", "col4"])
