from typing import Any, Dict, List


def calculate_metrics(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Calculate high-level evaluation metrics.
    """

    if not results:
        return {
            "total_tests": 0,
            "passed": 0,
            "failed": 0,
            "pass_rate": 0.0,
            "failure_rate": 0.0,
            "reliability_score": 0.0,
            "critical_failures": 0,
        }

    total = len(results)

    passed = sum(
        1
        for result in results
        if str(result.get("result", "")).upper() == "PASS"
    )

    failed = total - passed

    scores = [
        float(result.get("score", 0))
        for result in results
    ]

    reliability_score = round(
        sum(scores) / len(scores),
        1
    ) if scores else 0.0

    critical_failures = sum(
        1
        for result in results
        if str(result.get("severity", "")).upper() == "CRITICAL"
    )

    return {
        "total_tests": total,
        "passed": passed,
        "failed": failed,
        "pass_rate": round(
            (passed / total) * 100,
            1
        ),
        "failure_rate": round(
            (failed / total) * 100,
            1
        ),
        "reliability_score": reliability_score,
        "critical_failures": critical_failures,
    }


def get_failure_distribution(
    results: List[Dict[str, Any]]
) -> Dict[str, int]:
    """
    Count failures by failure type.
    """

    distribution = {}

    for result in results:

        if str(result.get("result", "")).upper() != "FAIL":
            continue

        failure_type = result.get(
            "failure_type",
            "Unknown"
        )

        distribution[failure_type] = (
            distribution.get(failure_type, 0) + 1
        )

    return distribution


def get_severity_distribution(
    results: List[Dict[str, Any]]
) -> Dict[str, int]:
    """
    Count failures by severity.
    """

    distribution = {}

    for result in results:

        if str(result.get("result", "")).upper() != "FAIL":
            continue

        severity = str(
            result.get(
                "severity",
                "UNKNOWN"
            )
        ).upper()

        distribution[severity] = (
            distribution.get(severity, 0) + 1
        )

    return distribution