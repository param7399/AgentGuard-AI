import json
import re
from datetime import datetime
from typing import Any, Dict, List


def clean_text(text: str) -> str:
    """Remove unnecessary whitespace."""

    if not isinstance(text, str):
        return ""

    return re.sub(
        r"\s+",
        " ",
        text
    ).strip()


def parse_tools(tools: str) -> List[str]:
    """
    Convert multiline tool input into
    a clean list of tool names.
    """

    if not isinstance(tools, str):
        return []

    return [
        tool.strip()
        for tool in tools.splitlines()
        if tool.strip()
    ]


def safe_json_loads(
    text: str,
    default: Any = None
) -> Any:
    """
    Safely parse JSON.
    """

    if not text:
        return default

    try:

        cleaned = text.strip()

        if cleaned.startswith("```"):

            cleaned = (
                cleaned
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )

        return json.loads(cleaned)

    except (
        json.JSONDecodeError,
        TypeError,
    ):
        return default


def format_timestamp(
    timestamp: datetime | None = None
) -> str:
    """Return a readable timestamp."""

    timestamp = timestamp or datetime.now()

    return timestamp.strftime(
        "%d %b %Y, %H:%M:%S"
    )


def clamp_score(
    score: float
) -> float:
    """Keep score within 0–100."""

    try:

        score = float(score)

    except (
        TypeError,
        ValueError,
    ):

        return 0.0

    return max(
        0.0,
        min(
            100.0,
            score
        )
    )


def get_status_from_score(
    score: float
) -> str:
    """Convert reliability score into status."""

    score = clamp_score(score)

    if score >= 90:
        return "Excellent"

    if score >= 75:
        return "Good"

    if score >= 50:
        return "Needs Improvement"

    return "Critical"


def calculate_percentage(
    value: int,
    total: int
) -> float:
    """Calculate percentage safely."""

    if total <= 0:
        return 0.0

    return round(
        (value / total) * 100,
        1
    )


def sort_results_by_score(
    results: List[Dict[str, Any]],
    reverse: bool = False
) -> List[Dict[str, Any]]:
    """Sort evaluation results by score."""

    return sorted(
        results,
        key=lambda item: float(
            item.get(
                "score",
                0
            )
        ),
        reverse=reverse
    )