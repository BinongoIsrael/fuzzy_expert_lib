import pytest
from fuzzy_expert.membership import triangular, trapezoidal

def test_triangular_peak():
    assert triangular(5, (0, 5, 10)) == 1.0

def test_triangular_left_side():
    assert triangular(2.5, (0, 5, 10)) == 0.5

def test_triangular_invalid():
    with pytest.raises(ValueError):
        triangular(5, (5, 3, 1))

def test_trapezoidal_plateau():
    assert trapezoidal(5, (0, 3, 7, 10)) == 1.0

def test_trapezoidal_left_side():
    assert trapezoidal(2, (0, 3, 7, 10)) == pytest.approx(2/3)

def test_trapezoidal_invalid():
    with pytest.raises(ValueError):
        trapezoidal(5, (3, 2, 1, 0))
