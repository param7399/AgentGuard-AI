from typing import Any, Dict, List


def generate_test_suite(
    categories: List[str],
    count: int = 6
) -> List[Dict[str, Any]]:
    """
    Create a basic test-suite configuration.

    Detailed AI scenario generation is handled by
    src.core.scenario_generator.
    """

    if not categories:
        categories = ["Normal"]

    tests = []

    for index in range(count):

        category = categories[
            index % len(categories)
        ]

        tests.append(
            {
                "id": index + 1,
                "category": category,
                "status": "PENDING",
            }
        )

    return tests


def filter_tests_by_category(
    tests: List[Dict[str, Any]],
    category: str
) -> List[Dict[str, Any]]:

    return [
        test
        for test in tests
        if test.get("category") == category
    ]