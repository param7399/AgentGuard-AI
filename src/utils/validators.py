from typing import Any


def validate_agent_name(name: str) -> bool:
    """Validate AI agent name."""

    if not isinstance(name, str):
        return False

    return 2 <= len(name.strip()) <= 100


def validate_agent_task(task: str) -> bool:
    """Validate agent objective/task."""

    if not isinstance(task, str):
        return False

    return len(task.strip()) >= 10


def validate_system_prompt(prompt: str) -> bool:
    """Validate system prompt."""

    if not isinstance(prompt, str):
        return False

    return len(prompt.strip()) >= 10


def validate_score(score: Any) -> bool:
    """Check whether score is between 0 and 100."""

    try:
        value = float(score)
        return 0 <= value <= 100
    except (TypeError, ValueError):
        return False


def validate_severity(severity: str) -> bool:
    """Validate failure severity."""

    if not isinstance(severity, str):
        return False

    return severity.upper() in {
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL",
    }


def validate_result_status(result: str) -> bool:
    """Validate PASS/FAIL status."""

    if not isinstance(result, str):
        return False

    return result.upper() in {
        "PASS",
        "FAIL",
    }


def validate_test_category(category: str) -> bool:
    """Validate test category."""

    valid_categories = {
        "Normal",
        "Adversarial",
        "Safety",
        "Tool Failure",
        "Goal Drift",
        "Hallucination",
        "Ambiguity",
    }

    return category in valid_categories