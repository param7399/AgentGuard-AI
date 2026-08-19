from typing import Dict, List, Any


def calculate_reliability_score(
    scores: List[float]
) -> float:

    if not scores:
        return 0

    valid_scores = []

    for score in scores:

        try:
            value = float(score)

            if 0 <= value <= 100:
                valid_scores.append(value)

        except (
            TypeError,
            ValueError,
        ):
            continue

    if not valid_scores:
        return 0

    return round(
        sum(valid_scores) / len(valid_scores)
    )


def calculate_weighted_score(
    results: List[Dict[str, Any]]
) -> float:

    if not results:
        return 0

    weights = {
        "LOW": 1.0,
        "MEDIUM": 1.0,
        "HIGH": 1.1,
        "CRITICAL": 1.2,
    }

    weighted_total = 0
    total_weight = 0

    for result in results:

        try:
            score = float(
                result.get(
                    "score",
                    0
                )
            )
        except (
            TypeError,
            ValueError,
        ):
            continue

        severity = str(
            result.get(
                "severity",
                "LOW"
            )
        ).upper()

        weight = weights.get(
            severity,
            1.0
        )

        weighted_total += (
            score * weight
        )

        total_weight += weight

    if total_weight == 0:
        return 0

    return round(
        weighted_total / total_weight
    )


def get_score_status(
    score: float
) -> str:

    score = float(score)

    if score >= 90:
        return "Excellent"

    if score >= 75:
        return "Good"

    if score >= 50:
        return "Needs Improvement"

    return "Critical"