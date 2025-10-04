"""
A basic issue ticket adding/listing/closing system using YAML.

:authors: Gavin Borne
"""

import argparse
import sys

import pyit


def init_parser() -> argparse.ArgumentParser:
    """Initialize the argument parser.

    Returns:
        argparse.ArgumentParser: The argument parser.
    """
    parser = argparse.ArgumentParser(
        prog="yamtik",
        description="Tool for writing, listing, reading, "
        "and closing issue tickets using YAML.",
        epilog="yamtik exited successfully.",
    )

    parser.add_argument("path", help="input yaml file")
    cmd = parser.add_subparsers(dest="cmd", required=True)

    new_cmd = cmd.add_parser("new", help="create a new issue ticket")
    new_cmd.add_argument(
        "urgency",
        choices=(*pyit.URGENCIES, "hi", "med", "lo", "h", "m", "l"),
        help="the urgency of the issue (high | medium | low)",
    )
    new_cmd.add_argument("title", help="the title of the issue")
    new_cmd.add_argument("-d", "--desc", required=False, default="")
    new_cmd.set_defaults(_subparser=new_cmd)

    list_cmd = cmd.add_parser("list", help="list all of the tickets in the given file")
    list_cmd.add_argument(
        "-f",
        "--filter",
        choices=(
            *pyit.FILTER_METHODS,
            "a",
            "o",
            "c",
            "h",
            "m",
            "l",
            "op",
            "cl",
            "hi",
            "med",
            "lo",
        ),
        default="open",
        help="the filter method to use when displaying the tickets",
    )
    list_cmd.add_argument(
        "-s",
        "--sort",
        choices=(
            *pyit.SORT_METHODS,
            "u",
            "urg",
            "r",
            "recent",
            "t",
            "time",
            "most recent",
            "mostrecent",
            "n",
            "no",
        ),
        default="none",
        help="the sorting method to use when displaying the tickets",
    )
    list_cmd.set_defaults(_subparser=list_cmd)

    show_cmd = cmd.add_parser("show", help="show an issue ticket")
    show_cmd.add_argument("tid", type=int, help="the id of the ticket to show")
    show_cmd.set_defaults(_subparser=show_cmd)

    close_cmd = cmd.add_parser("close", help="close an issue ticket")
    close_cmd.add_argument("tid", type=int, help="the id of the ticket to close")
    close_cmd.set_defaults(_subparser=close_cmd)

    return parser


def main() -> None:
    """The main entrypoint of the YAML ticket manager.

    Executes various commands based on the command given in the CLI args.
    """
    parser = init_parser()
    args, unknown = parser.parse_known_args(sys.argv[1:])

    if unknown:
        # try to print the help of the subparser,
        # otherwise default to the regular help
        subparser = getattr(args, "_subparser", None)
        (subparser or parser).print_help()
        parser.exit(2, f"\nerror: unrecognized arguments: {' '.join(unknown)}\n")

    if not args.path.endswith(".yaml"):
        print("The provided path must be a .yaml file.")  # noqa T201
        parser.print_usage()
        sys.exit(-1)

    tickets = pyit.load(args.path)

    if args.cmd == "new":
        urg = pyit.validate_urgency(args.urgency)
        if urg is None:
            sys.exit(f"Unknown urgency: {urg}")

        tid = pyit.next_id(tickets)
        tickets.append(pyit.new_ticket(tid, urg, args.title, args.desc))
        pyit.save(tickets, args.path)
        print(f"Issue ticket #{tid} {args.title} saved!")  # noqa T201

        return

    if args.cmd == "list":
        filt = pyit.validate_filter_method(args.filter)
        if filt is None:
            sys.exit(f"Unknown filter method: {filt}")

        sort = pyit.validate_sort_method(args.sort)
        if sort is None:
            sys.exit(f"Unknown sort method: {sort}")

        pyit.list_tickets(tickets, filter_method=filt, sort_method=sort)
        return

    if args.cmd == "show":
        tid = args.tid
        pyit.show_ticket(tickets, tid)
        return

    if args.cmd == "close":
        tid = args.tid
        found = pyit.close_ticket(tickets, tid)
        if not found:
            sys.exit(f"Issue ticket #{tid} was not found.")

        pyit.save(tickets, args.path)
        print(f"Issue ticked #{tid} closed!")  # noqa T201
        return

    parser.print_usage()


if __name__ == "__main__":
    main()
