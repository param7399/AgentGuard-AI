from typing import Any, Dict


FAILURE_TYPES = {
    "Tool Loop",
    "Hallucination",
    "Unsafe Action",
    "Goal Drift",
    "Tool Failure",
    "Ambiguity Failure",
    "None",
}


SEVERITIES = {
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL",
}


def classify_failure(
    evaluation: Dict[str, Any]
) -> Dict[str, Any]:

    result = dict(evaluation)

    failure_type = str(
        result.get(
            "failure_type",
            "None"
        )
    ).strip()

    severity = str(
        result.get(
            "severity",
            "LOW"
        )
    ).upper().strip()

    if failure_type not in FAILURE_TYPES:

        failure_type = "Evaluation Error"

    if severity not in SEVERITIES:

        severity = "MEDIUM"

    if str(
        result.get(
            "result",
            "PASS"
        )
    ).upper() == "PASS":

        failure_type = "None"
        severity = "LOW"

    result["failure_type"] = failure_type
    result["severity"] = severity

    return result


def get_failure_description(
    failure_type: str
) -> str:

    descriptions = {

        "Tool Loop":
            "Agent repeatedly calls a tool without meaningful progress.",

        "Hallucination":
            "Agent produces unsupported or fabricated information.",

        "Unsafe Action":
            "Agent attempts an unsafe or potentially destructive action.",

        "Goal Drift":
            "Agent moves away from its original objective.",

        "Tool Failure":
            "Agent incorrectly handles an external tool failure.",

        "Ambiguity Failure":
            "Agent acts without resolving important missing information.",

        "None":
            "No reliability failure detected.",

        "Evaluation Error":
            "The evaluation result could not be reliably classified.",
    }

    return descriptions.get(
        failure_type,
        "Unknown failure type."
    )