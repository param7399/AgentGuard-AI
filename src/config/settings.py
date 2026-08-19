import os

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


# =========================================================
# APPLICATION SETTINGS
# =========================================================

APP_NAME = "AgentGuard AI"
APP_VERSION = "1.0.0"

HACKATHON_NAME = "OOSC 4.0 Hackathon"
PROBLEM_STATEMENT = "Problem Statement 4"


# =========================================================
# AI SETTINGS
# =========================================================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-4o-mini"
)

AI_TEMPERATURE = 0.25


# =========================================================
# EVALUATION SETTINGS
# =========================================================

DEFAULT_TEST_COUNT = 6

MIN_TEST_COUNT = 3
MAX_TEST_COUNT = 15

MAX_RELIABILITY_SCORE = 100


# =========================================================
# RELIABILITY THRESHOLDS
# =========================================================

EXCELLENT_THRESHOLD = 90
GOOD_THRESHOLD = 75
NEEDS_IMPROVEMENT_THRESHOLD = 50


# =========================================================
# APPLICATION MODES
# =========================================================

DEMO_MODE = not bool(OPENAI_API_KEY)


# =========================================================
# VALIDATION
# =========================================================

def get_reliability_status(score: float) -> str:
    """
    Convert reliability score into a human-readable status.
    """

    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"

    if score >= GOOD_THRESHOLD:
        return "Good"

    if score >= NEEDS_IMPROVEMENT_THRESHOLD:
        return "Needs Improvement"

    return "Critical"


def get_reliability_color(score: float) -> str:
    """
    Return a UI color based on reliability score.
    """

    if score >= EXCELLENT_THRESHOLD:
        return "#22c55e"

    if score >= GOOD_THRESHOLD:
        return "#eab308"

    if score >= NEEDS_IMPROVEMENT_THRESHOLD:
        return "#f97316"

    return "#ef4444"