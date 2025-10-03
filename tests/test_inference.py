from fuzzy_expert.inference import evaluate_rules
from fuzzy_expert.rules import Rule

def test_inference_basic():
    fuzzified_inputs = {"temp": {"hot": 0.7, "cold": 0.2}}
    rules = [Rule([("temp", "hot")], "turn_on_fan")]
    output = evaluate_rules(rules, fuzzified_inputs)
    assert output == {"turn_on_fan": 0.7}

def test_inference_conflict():
    fuzzified_inputs = {"temp": {"hot": 0.5}}
    rules = [
        Rule([("temp", "hot")], "fan_high"),
        Rule([("temp", "hot")], "fan_high"),
    ]
    output = evaluate_rules(rules, fuzzified_inputs)
    assert output["fan_high"] == 0.5
