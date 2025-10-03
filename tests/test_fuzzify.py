import pytest
from fuzzy_expert.fuzzify import fuzzify_variable
from fuzzy_expert.membership import triangular, trapezoidal

def test_fuzzify_triangular():
    terms = {"low": (0, 5, 10)}
    result = fuzzify_variable(5, terms)
    assert result["low"] == 1.0

def test_fuzzify_trapezoidal():
    terms = {"medium": (0, 3, 7, 10)}
    result = fuzzify_variable(5, terms)
    assert 0.0 <= result["medium"] <= 1.0

def test_fuzzify_invalid_params():
    terms = {"bad": (1, 2)}  # invalid length
    with pytest.raises(ValueError):
        fuzzify_variable(5, terms)
