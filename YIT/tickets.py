"""
Tools for working with tickets.

:authors: Gavin Borne
"""

from datetime import UTC, datetime

from .tick_types import FilterMethod, SortMethod, Ticket, Urgency


def next_id(tickets: list[Ticket], /) -> int:
    """Get the next ticket id based on the existing tickets.

    Args:
        tickets (list[Ticket]): The existing tickets.

    Returns:
        int: The next ticket id.
    """
    return max((t["id"] for t in tickets), default=0) + 1


def new_ticket(tid: int, urgency: Urgency, title: str, description: str = "") -> Ticket:
    """Create a new ticket.

    Args:
        tid (int): The id of the ticket.
        urgency (Urgency): The urgency of the ticket.
        title (str): The title of the ticket.
        description (str, optional): The description of the ticket. Defaults to "".

    Returns:
        Ticket: The new ticket.
    """
    return {
        "id": tid,
        "title": title,
        "description": description,
        "urgency": urgency,
        "status": "open",
        "created": datetime.now(tz=UTC).date().isoformat(),
    }


def list_tickets(
    tickets: list[Ticket],
    /,
    *,
    filter_method: FilterMethod = "all",
    sort_method: SortMethod = "none",
) -> None:
    """List all the tickets with optional filter and sort methods.

    Args:
        tickets (list[Ticket]): The tickets to list.
        filter_method (FilterMethod, optional): The filter method. Defaults to "all".
        sort_method (SortMethod, optional): The sort method. Defaults to "none".
    """
