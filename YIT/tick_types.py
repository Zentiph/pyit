"""
Types for the ticket program.

:author: Gavin Borne
"""

from typing import Literal, NotRequired, TypeAlias, TypedDict

Urgency: TypeAlias = Literal["low", "medium", "high"]
Status: TypeAlias = Literal["open", "closed"]
SortMethod: TypeAlias = Literal["priority", "most-recent", "none"]
FilterMethod: TypeAlias = Literal["all", "open", "closed", "high", "medium", "low"]

TicketKey: TypeAlias = Literal[
    "id", "title", "description", "urgency", "status", "created", "closed"
]


class Ticket(TypedDict):
    """A representation of a ticket."""

    id: int
    title: str
    description: str
    urgency: Urgency
    status: Status
    created: str
    closed: NotRequired[str]


def validate_urgency(urgency: str, /) -> Urgency | None:
    """Convert a string to an urgency if possible.

    Args:
        urgency (str): The string to convert.

    Returns:
        Urgency | None: The converted urgency, or None if it failed.
    """
    if urgency in {"l", "lo", "low"}:
        return "low"
    if urgency in {"m", "med", "medium"}:
        return "medium"
    if urgency in {"h", "hi", "high"}:
        return "high"

    return None


def validate_sort_method(sort_method: str) -> SortMethod | None:
    """Convert a string to a sort method if possible.

    Args:
        sort_method (str): The string to convert.

    Returns:
        SortMethod | None: The converted sort method, or None if it failed.
    """
    if sort_method in {"p", "pri", "priority"}:
        return "priority"
    if sort_method in {
        "r",
        "recent",
        "t",
        "time",
        "most-recent",
        "most recent",
        "mostrecent",
    }:
        return "most-recent"
    if sort_method in {"n", "no", "none"}:
        return "none"

    return None


def validate_filter_method(filter_method: str) -> FilterMethod | None:
    """Convert a string to a filter method if possible.

    Args:
        filter_method (str): The string to convert.

    Returns:
        FilterMethod | None: The converted filter method, or None if it failed.
    """
    if filter_method in {"a", "all"}:
        return "all"
    if filter_method in {"o", "op", "open"}:
        return "open"
    if filter_method in {"c", "cl", "closed"}:
        return "closed"
    if filter_method in {"l", "lo", "low"}:
        return "low"
    if filter_method in {"m", "med", "medium"}:
        return "medium"
    if filter_method in {"h", "hi", "high"}:
        return "high"

    return None
