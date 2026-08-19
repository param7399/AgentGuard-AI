from src.utils.validators import (
    validate_agent_name,
    validate_agent_task,
    validate_score
)


def test_valid_agent_name():

    assert validate_agent_name(
        "Travel Booking Agent"
    ) is True


def test_empty_agent_name():

    assert validate_agent_name("") is False


def test_valid_agent_task():

    assert validate_agent_task(
        "Book flights based on customer requirements."
    ) is True


def test_empty_agent_task():

    assert validate_agent_task("") is False


def test_valid_score():

    assert validate_score(85) is True


def test_invalid_score():

    assert validate_score(120) is False