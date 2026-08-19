from src.core.evaluator import validate_evaluation_result


def test_valid_evaluation():

    result = {
        "result": "PASS",
        "failure_type": "None",
        "severity": "LOW",
        "score": 95,
        "agent_response": "Test response",
        "reason": "Correct behavior",
        "recommendation": "No action required."
    }

    assert validate_evaluation_result(result) is True


def test_invalid_score():

    result = {
        "result": "PASS",
        "failure_type": "None",
        "severity": "LOW",
        "score": 150,
        "agent_response": "Test response",
        "reason": "Correct behavior",
        "recommendation": "No action required."
    }

    assert validate_evaluation_result(result) is False


def test_invalid_result_status():

    result = {
        "result": "UNKNOWN",
        "failure_type": "None",
        "severity": "LOW",
        "score": 80,
        "agent_response": "Test response",
        "reason": "Test",
        "recommendation": "Test"
    }

    assert validate_evaluation_result(result) is False