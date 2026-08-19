from typing import Dict, List, Any


def calculate_reliability_trend(
    evaluation_history: List[Dict[str, Any]]
) -> List[float]:
    """
    Extract reliability scores from previous evaluations.
    """

    trend = []

    for evaluation in evaluation_history:

        score = evaluation.get(
            "reliability_score"
        )

        if score is not None:
            trend.append(
                float(score)
            )

    return trend


def calculate_average_score(
    scores: List[float]
) -> float:
    """
    Calculate average reliability score.
    """

    if not scores:
        return 0.0

    return round(
        sum(scores) / len(scores),
        1
    )


def calculate_score_change(
    current_score: float,
    previous_score: float
) -> float:
    """
    Calculate change between two evaluation scores.
    """

    return round(
        current_score - previous_score,
        1
    )


def get_trend_direction(
    current_score: float,
    previous_score: float
) -> str:
    """
    Determine whether reliability is improving,
    declining, or stable.
    """

    difference = current_score - previous_score

    if difference > 2:
        return "improving"

    if difference < -2:
        return "declining"

    return "stable"