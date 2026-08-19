from src.core.reliability_score import calculate_reliability_score


def test_reliability_score():

    scores = [90, 80, 70]

    result = calculate_reliability_score(scores)

    assert result == 80


def test_perfect_score():

    scores = [100, 100, 100]

    result = calculate_reliability_score(scores)

    assert result == 100


def test_zero_score():

    scores = [0, 0, 0]

    result = calculate_reliability_score(scores)

    assert result == 0


def test_empty_scores():

    result = calculate_reliability_score([])

    assert result == 0