#!/usr/bin/env python3
"""Held-patch check: the tool-developer step-2 in-flight check, executable.

Held patches live outside this repository, in the goal ``hidden_files/``
workspace, so the step-2 in-flight check (backlog in-progress status,
matching in-flight commit pattern in the recent git log, PR branch moved
since review) could not see them. Issue #809 is the live instance: issue
#709 was implemented twice (2026-11-14 2032 run and 2026-11-15 0733 run,
same base, two variants) while #712 sat held and was nearly
re-implemented.

The fix is a register this tool reads:
``_conventions_/local-conventions/held-patches.md`` - one row per issue
with its status (HELD for a live patch, SUPERSEDED for an issue merged
on main by the named PR) and its canonical patch path. The register is
the step-2 source; the reconciled inventory in the goal ``hidden_files/``
is the evidence behind it. Run this tool before re-implementing an
issue; a non-zero exit stops the run from re-taking it.

Two commands, standard library only:

  check <issue> - report one issue's held-patch status. Exit 0 when the
                  issue is safe to implement (no row, or SUPERSEDED),
                  1 when a live held patch exists (HELD - do not
                  re-implement), 2 when the register cannot be read or
                  the issue argument is not a number.
  list          - list every registered held patch with its status.
                  Exit 0, or 2 when the register cannot be read.

``--format text|json`` selects the output shape (default text).
``--register PATH`` reads a different register (fixtures, tests).

Usage:
  held_patches.py check <issue> [--format text|json] [--register PATH]
  held_patches.py list [--format text|json] [--register PATH]
"""

import argparse
import json
import os
import sys

TOOL_VERSION = "1.0.0"

STATUS_HELD = "HELD"
STATUS_SUPERSEDED = "SUPERSEDED"
STATUS_NONE = "NONE"

_KNOWN_STATUSES = (STATUS_HELD, STATUS_SUPERSEDED)


def _default_register_path():
    """Register beside the conventions tree, resolved from this script."""
    tools_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(tools_dir)
    return os.path.join(
        repo_root, "_conventions_", "local-conventions", "held-patches.md"
    )


def _read_register(path):
    """Read and parse the register table.

    Returns (entries, error): entries maps issue number (int) to a dict
    with status, patch and note; error is None on success, else a
    message naming why the register cannot be trusted.
    """
    try:
        with open(path, "r", encoding="utf-8") as handle:
            text = handle.read()
    except OSError as exc:
        return None, "cannot read register %s: %s" % (path, exc)
    entries = {}
    in_table = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            in_table = stripped == "## Held patches"
            continue
        if not in_table:
            continue
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) != 4:
            return None, "malformed row in register %s: %s" % (path, line)
        if cells[0].lower() == "issue" or set(cells[0]) <= set("- "):
            continue
        issue_text = cells[0].lstrip("#").strip()
        if not issue_text.isdigit():
            return None, "malformed issue in register %s: %s" % (path, line)
        status = cells[1].split()[0].upper() if cells[1].split() else ""
        if status not in _KNOWN_STATUSES:
            return None, "unknown status in register %s: %s" % (path, line)
        issue = int(issue_text)
        if issue in entries:
            return None, "duplicate issue #%d in register %s" % (issue, path)
        entries[issue] = {
            "status": status,
            "patch": cells[2].strip("`").strip(),
            "note": cells[3].strip(),
        }
    if not in_table and not entries:
        return None, "no Held patches table in register %s" % path
    return entries, None


def _check(entries, issue):
    """Status dict for one issue: HELD, SUPERSEDED, or NONE."""
    entry = entries.get(issue)
    if entry is None:
        return {"issue": issue, "status": STATUS_NONE, "patch": "", "note": ""}
    return {"issue": issue, "status": entry["status"],
            "patch": entry["patch"], "note": entry["note"]}


def _print_check(result, fmt):
    if fmt == "json":
        print(json.dumps(result, sort_keys=True))
        return
    if result["status"] == STATUS_HELD:
        print("issue %d: HELD - live patch at %s (%s); do not re-implement"
              % (result["issue"], result["patch"], result["note"]))
    elif result["status"] == STATUS_SUPERSEDED:
        print("issue %d: SUPERSEDED - implemented on main (%s); nothing held"
              % (result["issue"], result["note"]))
    else:
        print("issue %d: no held patch recorded" % result["issue"])


def _print_list(entries, fmt):
    rows = [{"issue": issue, "status": entry["status"],
             "patch": entry["patch"], "note": entry["note"]}
            for issue, entry in sorted(entries.items())]
    if fmt == "json":
        print(json.dumps(rows, sort_keys=True))
        return
    if not rows:
        print("no held patches registered")
        return
    for row in rows:
        print("#%d %s %s (%s)"
              % (row["issue"], row["status"], row["patch"], row["note"]))


def main(argv=None):
    # Shared options live on the top parser and on each subparser, so they
    # work before and after the subcommand. SUPPRESS keeps a subparser
    # default from overwriting a value already given before the
    # subcommand (argparse would otherwise reset it to None).
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--register", default=argparse.SUPPRESS,
                        help="register path (default: the in-repo register)")
    common.add_argument("--format", choices=("text", "json"),
                        default=argparse.SUPPRESS,
                        help="output shape (default text)")
    parser = argparse.ArgumentParser(
        description="Step-2 in-flight check for held patches (issue #809).",
        parents=[common])
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("check", help="report one issue's status",
                           parents=[common])
    check.add_argument("issue", help="issue number, with or without #")
    sub.add_parser("list", help="list every registered held patch",
                   parents=[common])
    args = parser.parse_args(argv)

    register = getattr(args, "register", None) or _default_register_path()
    fmt = getattr(args, "format", "text")
    entries, error = _read_register(register)
    if error is not None:
        print("held_patches: %s" % error, file=sys.stderr)
        return 2

    if args.command == "list":
        _print_list(entries, fmt)
        return 0

    issue_text = args.issue.lstrip("#").strip()
    if not issue_text.isdigit():
        print("held_patches: issue must be a number, got %r" % args.issue,
              file=sys.stderr)
        return 2
    result = _check(entries, int(issue_text))
    _print_check(result, fmt)
    return 1 if result["status"] == STATUS_HELD else 0


if __name__ == "__main__":
    sys.exit(main())
