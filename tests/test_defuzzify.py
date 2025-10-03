import pytest
from fuzzy_expert.defuzzify import defuzzify_centroid

def test_defuzzify_basic():
    rules_output = [
        ("low", 0.8, (0, 5, 10), 3.0, 2.0),
        ("high", 0.6, (5, 10, 15), 8.0, 3.0),
    ]
    result = defuzzify_centroid(rules_output)
    expected = (3.0*2.0 + 8.0*3.0) / (2.0+3.0)
    assert result == pytest.approx(expected)

def test_defuzzify_empty():
    assert defuzzify_centroid([]) == 0.0

def test_defuzzify_with_invalid():
    rules_output = [("low", 0.0, (0, 5, 10), 3.0, 0.0)]
    assert defuzzify_centroid(rules_output) == 0.0
