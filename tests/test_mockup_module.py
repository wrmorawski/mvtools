import pytest

from mvtools.mockup_module import mockup_function


@pytest.fixture
def a():
    return 10


@pytest.fixture
def b():
    return 2.5


def test_mockup_function(a, b):
    result = mockup_function(a, b)
    assert result == 4.0
