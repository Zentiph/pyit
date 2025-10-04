"""
Tools for working with tickets.

:authors: Gavin Borne
"""

import json
from datetime import UTC, datetime

from .filtering import filter_by_status, filter_by_urgency
from .sorting import sort_by_recent, sort_by_urgency
from .tick_types import FilterMethod, SortMethod, Ticket, Urgency

__all__ = ["close_ticket", "list_tickets", "new_ticket", "next_id", "show_ticket"]


def next_id(tickets: list[Ticket], /) -> int:
    """Get the next ticket id based on the existing tickets.

    Args:
        tickets (list[Ticket]): The existing tickets.

    Returns:
        int: The next ticket id.
    """
    return max((t["id"] for t in tickets), default=0) + 1


def new_ticket(
    tid: int, urgency: Urgency, /, title: str, description: str = ""
) -> Ticket:
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
    filter_method: FilterMethod = "open",
    sort_method: SortMethod = "none",
) -> None:
    """List all the tickets with optional filter and sort methods.

    Args:
        tickets (list[Ticket]): The tickets to list.
        filter_method (FilterMethod, optional): The filter method. Defaults to "open".
        sort_method (SortMethod, optional): The sort method. Defaults to "none".
    """
    match filter_method:
        case "open" | "closed":
            it = filter_by_status(tickets, filter_method)
        case "high" | "medium" | "low":
            it = filter_by_urgency(tickets, filter_method)
        case _:
            it = tickets

    match sort_method:
        case "urgency":
            it = sort_by_urgency(it)
        case "most-recent":
            it = sort_by_recent(it)
        case _:
            pass

    for t in it:
        print(  # noqa T201
            f"#{t['id']:>3}"
            f"  [{t['urgency'][:1].upper()}]"
            f"  {t['title']}"
            f"  ({t['status']})"
        )


def show_ticket(tickets: list[Ticket], tid: int, /) -> None:
    """Show a singular ticket.

    Args:
        tickets (list[Ticket]): All of the tickets.
        tid (int): The id of the ticket to show.
    """
    ticket = next((t for t in tickets if t["id"] == tid), None)
    if not ticket:
        print(f"Ticket {tid} not found.")  # noqa T201
    else:
        print(json.dumps(ticket, indent=2))  # noqa T201


def close_ticket(tickets: list[Ticket], tid: int, /) -> bool:
    """Close a ticket.

    Args:
        tickets (list[Ticket]): All of the tickets.
        tid (int): The id of the ticket to close.

    Returns:
        bool: Whether this operation successfully closed the ticket.
    """
    found = False
    for ticket in tickets:
        if ticket["id"] == tid:
            ticket["status"] = "closed"
            ticket["closed"] = datetime.now(tz=UTC).date().isoformat()
            found = True
            break

    return found
