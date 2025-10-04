"""
Sorting functions for tickets.

:authors: Gavin Borne
"""

from .tick_types import Ticket, Urgency

URGENCY_ORD: dict[Urgency, int] = {"low": 0, "medium": 1, "high": 2}
"""A mapping of urgency strings to their ordinal values."""


def sort_by_urgency(tickets: list[Ticket], /) -> list[Ticket]:
    """Sort a list of tickets by urgency.

    Args:
        tickets (list[Ticket]): The tickets to sort.

    Returns:
        list[Ticket]: The sorted tickets.
    """
    return sorted(tickets, key=lambda t: URGENCY_ORD[t["urgency"]], reverse=True)


def sort_by_recent(tickets: list[Ticket], /) -> list[Ticket]:
    """Sort a list of tickets by how recent they are.

    Args:
        tickets (list[Ticket]): The tickets to sort.

    Returns:
        list[Ticket]: The sorted tickets.
    """
    # ticket numbers are made in order of creation,
    # so reversing is fine here
    return list(reversed(tickets))
