from mvtools.imputers import SimpleImputer


def test_simple_imputer_fill():
    imputer = SimpleImputer(methods={"a": "sum"})
    assert imputer is not None
