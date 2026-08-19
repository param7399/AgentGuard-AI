from typing import Any, Dict


def search_flights(
    destination: str = "",
    date: str = ""
) -> Dict[str, Any]:

    if not destination:
        return {
            "success": False,
            "error": "Destination is required."
        }

    return {
        "success": True,
        "tool": "search_flights",
        "data": [
            {
                "flight": "AG101",
                "destination": destination,
                "date": date or "2026-09-01",
                "price": 5499
            },
            {
                "flight": "AG205",
                "destination": destination,
                "date": date or "2026-09-01",
                "price": 6299
            }
        ]
    }


def book_flight(
    flight_id: str = ""
) -> Dict[str, Any]:

    if not flight_id:
        return {
            "success": False,
            "error": "Flight ID is required."
        }

    return {
        "success": True,
        "tool": "book_flight",
        "booking_id": "AG-" + flight_id,
        "message": "Flight booking confirmed."
    }


def cancel_booking(
    booking_id: str = ""
) -> Dict[str, Any]:

    if not booking_id:
        return {
            "success": False,
            "error": "Booking ID is required."
        }

    return {
        "success": True,
        "tool": "cancel_booking",
        "booking_id": booking_id,
        "message": "Booking cancellation processed."
    }


def simulate_tool_failure(
    tool_name: str
) -> Dict[str, Any]:

    return {
        "success": False,
        "tool": tool_name,
        "error": "Simulated tool failure.",
        "error_code": "MOCK_TOOL_ERROR"
    }


TOOL_REGISTRY = {
    "search_flights": search_flights,
    "book_flight": book_flight,
    "cancel_booking": cancel_booking,
}


def execute_mock_tool(
    tool_name: str,
    **kwargs
) -> Dict[str, Any]:

    tool = TOOL_REGISTRY.get(tool_name)

    if tool is None:
        return {
            "success": False,
            "tool": tool_name,
            "error": f"Unknown tool: {tool_name}"
        }

    try:
        return tool(**kwargs)

    except Exception as exc:
        return {
            "success": False,
            "tool": tool_name,
            "error": str(exc)
        }