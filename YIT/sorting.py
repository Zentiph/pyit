"""
Sorting functions for tickets.

:authors: Gavin Borne
"""

from typing import Literal

from .tick_types import Ticket, Urgency


def _urgency_ord(urgency: Urgency, /) -> Literal[0, 1, 2]:
    m: dict[Urgency, Literal[0, 1, 2]] = {"low": 0, "medium": 1, "high": 2}
    return m[urgency]


def priority(tickets: list[Ticket], /, *, low_first: bool = False) -> list[Ticket]:
    """Sort a list of tickets by priority.

    Args:
        tickets (list[Ticket]): The tickets to sort.
        low_first (bool, optional): Whether to sort by lowest priority first.
            Defaults to False.

    Returns:
        list[Ticket]: The sorted tickets.
    """
    return sorted(
        tickets, key=lambda t: _urgency_ord(t["urgency"]), reverse=(not low_first)
    )


def recent(tickets: list[Ticket], /) -> list[Ticket]:
    """Sort a list of tickets by how recent they are.

    Args:
        tickets (list[Ticket]): The tickets to sort.

    Returns:
        list[Ticket]: The sorted tickets.
    """
    # ticket numbers are made in order of creation,
    # so reversing is fine here
    return list(reversed(tickets))
