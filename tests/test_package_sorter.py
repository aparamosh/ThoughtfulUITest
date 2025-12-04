import pytest
from package_sorter.package_sorter import sort, STANDARD, SPECIAL, REJECTED


def test_standard_package():
    assert sort(50.1, 40, 30, 10) == STANDARD


def test_bulky_by_volume():
    assert sort(100, 100, 100, 5) == SPECIAL


def test_rejected():
    assert sort(200, 200, 200, 25) == REJECTED


def test_invalid_negative_dimension():
    with pytest.raises(ValueError):
        sort(-1, 10, 10, 5)


def test_invalid_zero_mass():
    with pytest.raises(ValueError):
        sort(10, 10, 10, 0)


def test_invalid_type():
    with pytest.raises(TypeError):
        sort("100", 10, 10, 5)
