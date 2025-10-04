"""
Tools for reading and writing tickets to YAML files.

:authors: Gavin Borne
"""

from pathlib import Path

import yaml

from .tick_types import Ticket

__all__ = ["load", "save"]


def load(loc: str) -> list[Ticket]:
    """Load a tickets YAML file.

    Args:
        loc (str): The path to the YAML file.

    Raises:
        ValueError: If a filetype other than .yaml is given.
        FileNotFoundError: If loc is not a valid path.

    Returns:
        list[Ticket]: The loaded data.
    """
    if not loc.endswith(".yaml"):
        raise ValueError("Load only accepts .yaml files")

    path = Path(loc)
    if not path.exists():
        raise FileNotFoundError("Could not find file: " + loc)

    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or []


def save(tickets: list[Ticket], loc: str) -> None:
    """Save tickets to a YAML file.

    This function overrides the file.

    Args:
        tickets (list[Ticket]): The tickets to save.
        loc (str): The path to the YAML file.
    """
    with Path(loc).open("w", encoding="utf-8") as f:
        yaml.safe_dump(tickets, f, sort_keys=False)
