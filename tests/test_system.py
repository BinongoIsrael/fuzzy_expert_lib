from fuzzy_expert.system import FuzzyExpertSystem

def test_system_end_to_end():
    system = FuzzyExpertSystem()
    system.add_variable("temp", {"cold": (0, 0, 20), "hot": (20, 40, 40)})
    system.add_output_term("slow", (0, 10, 20))
    system.add_output_term("fast", (20, 30, 40))
    system.add_rule([("temp", "cold")], "slow")
    system.add_rule([("temp", "hot")], "fast")

    crisp, classification = system.assess({"temp": 10})
    assert isinstance(crisp, float)
    assert classification in ("slow", "fast")
