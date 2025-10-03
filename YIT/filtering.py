"""
Filtering functions for tickets.

:authors: Gavin Borne
"""

from .tick_types import Status, Ticket, Urgency


def filter_by_status(tickets: list[Ticket], status: Status, /) -> list[Ticket]:
    """Filter a list of tickets, only keeping ones that match the given status.

    Args:
        tickets (list[Ticket]): The initial tickets.
        status (Status): The status to keep.

    Returns:
        list[Ticket]: The filtered tickets.
    """
    return [t for t in tickets if t["status"] == status]


def filter_by_urgency(tickets: list[Ticket], urgency: Urgency, /) -> list[Ticket]:
    """Filter a list of tickets, only keeping ones that match the given urgency.

    Args:
        tickets (list[Ticket]): The initial tickets.
        urgency (Urgency): The urgency to keep.

    Returns:
        list[Ticket]: The filtered tickets.
    """
    return [t for t in tickets if t["urgency"] == urgency]
