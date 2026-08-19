from src.core.scenario_generator import validate_scenarios


def test_valid_scenarios():
    scenarios = [
        {
            "id": 1,
            "category": "Safety",
            "severity": "HIGH",
            "scenario": "Test scenario",
            "expected_behavior": "Safe response"
        }
    ]

    assert validate_scenarios(scenarios) is True


def test_empty_scenarios():
    assert validate_scenarios([]) is False


def test_missing_required_field():
    scenarios = [
        {
            "id": 1,
            "category": "Safety"
        }
    ]

    assert validate_scenarios(scenarios) is False