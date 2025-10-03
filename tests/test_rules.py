from fuzzy_expert.rules import Rule

def test_rule_evaluation_basic():
    rule = Rule([("temp", "hot"), ("humidity", "high")], ("fan", "fast"))
    fuzzified_inputs = {"temp": {"hot": 0.7}, "humidity": {"high": 0.5}}
    consequent, strength = rule.evaluate(fuzzified_inputs)
    
    assert consequent == ("fan", "fast") 
    assert strength == 0.5  

def test_rule_missing_input():
    rule = Rule([("temp", "hot")], ("fan", "slow"))
    fuzzified_inputs = {}
    consequent, strength = rule.evaluate(fuzzified_inputs)
    assert consequent == ("fan", "slow")
    assert strength == 0
