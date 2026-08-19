import csv
import io
from typing import Any, Dict, List


REPORT_COLUMNS = [
    "test_id",
    "category",
    "result",
    "failure_type",
    "severity",
    "score",
    "scenario",
    "agent_response",
    "reason",
    "recommendation",
]


def prepare_report(
    results: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Convert evaluation results into a consistent
    report structure.
    """

    report = []

    for result in results:

        row = {
            column: result.get(
                column,
                ""
            )
            for column in REPORT_COLUMNS
        }

        report.append(row)

    return report


def generate_csv_report(
    results: List[Dict[str, Any]]
) -> str:
    """
    Generate CSV content from evaluation results.
    """

    report = prepare_report(results)

    output = io.StringIO()

    writer = csv.DictWriter(
        output,
        fieldnames=REPORT_COLUMNS
    )

    writer.writeheader()

    writer.writerows(report)

    return output.getvalue()


def generate_summary(
    results: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Generate a compact report summary.
    """

    if not results:
        return {
            "total_tests": 0,
            "passed": 0,
            "failed": 0,
            "reliability_score": 0,
        }

    scores = [
        float(result.get("score", 0))
        for result in results
    ]

    passed = sum(
        1
        for result in results
        if str(
            result.get("result", "")
        ).upper() == "PASS"
    )

    total = len(results)

    return {
        "total_tests": total,
        "passed": passed,
        "failed": total - passed,
        "reliability_score": round(
            sum(scores) / len(scores),
            1
        ),
    }