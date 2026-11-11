#!/usr/bin/env python3
"""Pre-push tree check: a sparse-checkout delivery must never push a poisoned tree.

A records-branch delivery committed from a detached sparse-checkout
worktree records the sparse index as the whole tree. Issue #541
(2026-11-09) is the live instance: commit bcad9a0e4, the
pr-catchall 1739 run record, was committed from a worktree whose
index held only ``_records_``, so it deleted 4,510 files from the
records/2026-11-09 branch tree (AGENTS.md, README.md, ``_activities_/``,
``_conventions_/``, ``_knowledge_/``, ``_tools_/``, ``tools/``,
``_logs_/``). Later deliveries only partially healed the tree, and
PR #531 had to be held out of the 19:00 batch until the branch was
repaired by hand. The failure mode is a missing distinction: nothing
in the delivery path checks that the tree about to be pushed still
holds the repository's top-level entries, so a sparse index passes
as a complete tree.

This tool makes the check explicit. The repository's top-level
contract is ten entries, verified against main:

  AGENTS.md, README.md, _activities_, _conventions_, _knowledge_,
  _logs_, _queue_, _records_, _tools_, tools

One command, standard library only:

  check - verify the expected top-level entries are present.
          Without --tree it checks the git index (``git ls-files
          --cached`` - the exact thing a commit would record) and
          the working tree on disk. With --tree REF it checks a
          committed tree (``git ls-tree --name-only REF``) - the
          branch tip about to be pushed. --expect NAME adds an
          entry to the expected list. Exit 0 when every expected
          entry is present, 1 when entries are missing (each
          missing entry is printed, per source), 2 when the tree
          cannot be verified (not a git repository, the ref does
          not resolve, or git fails).

Run it twice on a sparse-worktree delivery: ``check`` before
committing the delivery, and ``check --tree <branch-tip>`` before
pushing. A non-zero exit stops the delivery. The check is read-only:
it writes nothing and moves no ref.

Usage:
  tree_check.py check --repo PATH [--tree REF] [--expect NAME ...]
                      [--format text|json]
"""

import argparse
import json
import os
import subprocess
import sys

TOOL_VERSION = "1.0.0"

EXPECTED_TOP_LEVEL = [
    "AGENTS.md",
    "README.md",
    "_activities_",
    "_conventions_",
    "_knowledge_",
    "_logs_",
    "_queue_",
    "_records_",
    "_tools_",
    "tools",
]


def _run_git(args, cwd):
    """Run git and return the completed process (never raises)."""
    try:
        return subprocess.run(
            ["git"] + args, cwd=cwd, capture_output=True, text=True,
            timeout=120)
    except (OSError, subprocess.TimeoutExpired):
        return None


def _top_level(paths):
    """First path component of each path, as a set."""
    names = set()
    for path in paths:
        if not path:
            continue
        names.add(path.split("/", 1)[0])
    return names


def _index_entries(repo):
    """Top-level entries in the git index, or None when unreadable."""
    proc = _run_git(["ls-files", "--cached", "-z"], cwd=repo)
    if proc is None or proc.returncode != 0:
        return None
    return _top_level(proc.stdout.split("\0"))


def _worktree_entries(repo):
    """Top-level entries present on disk, or None when unreadable."""
    try:
        return set(os.listdir(repo))
    except OSError:
        return None


def _tree_entries(repo, ref):
    """Top-level entries in a committed tree, or None when unreadable."""
    proc = _run_git(["ls-tree", "--name-only", ref], cwd=repo)
    if proc is None or proc.returncode != 0:
        return None
    return set(proc.stdout.splitlines())


def _missing(expected, present):
    return sorted(set(expected) - set(present))


def _render(result, fmt):
    if fmt == "json":
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        for line in result["text"]:
            print(line)


def cmd_check(args):
    expected = list(EXPECTED_TOP_LEVEL)
    for extra in args.expect:
        if extra not in expected:
            expected.append(extra)

    sources = {}
    if args.tree is not None:
        entries = _tree_entries(args.repo, args.tree)
        if entries is None:
            result = {
                "ok": False,
                "error": "cannot read tree %s" % args.tree,
                "text": ["tree_check: cannot read tree %s in %s"
                         % (args.tree, args.repo)],
            }
            _render(result, args.format)
            return 2
        sources["tree %s" % args.tree] = entries
    else:
        index = _index_entries(args.repo)
        if index is None:
            result = {
                "ok": False,
                "error": "cannot read git index",
                "text": ["tree_check: cannot read git index in %s "
                         "(not a git repository?)" % args.repo],
            }
            _render(result, args.format)
            return 2
        sources["index"] = index
        worktree = _worktree_entries(args.repo)
        if worktree is None:
            result = {
                "ok": False,
                "error": "cannot list working tree",
                "text": ["tree_check: cannot list working tree in %s"
                         % args.repo],
            }
            _render(result, args.format)
            return 2
        sources["worktree"] = worktree

    missing = {}
    for source, entries in sources.items():
        absent = _missing(expected, entries)
        if absent:
            missing[source] = absent

    ok = not missing
    text = []
    if ok:
        text.append("tree_check: OK - all %d expected top-level entries "
                    "present in %s"
                    % (len(expected), ", ".join(sources)))
    else:
        for source, absent in missing.items():
            text.append("tree_check: %s is missing %d expected top-level "
                        "entr%s: %s"
                        % (source, len(absent),
                           "y" if len(absent) == 1 else "ies",
                           ", ".join(absent)))
        text.append("tree_check: refusing - a sparse index records only "
                    "what it holds; do not commit or push this tree")

    result = {
        "ok": ok,
        "expected": expected,
        "missing": missing,
        "text": text,
    }
    _render(result, args.format)
    return 0 if ok else 1


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="tree_check.py",
        description="Verify a repo tree holds every expected top-level "
                    "entry before a delivery commit or push (issue #541).")
    sub = parser.add_subparsers(dest="command", required=True)

    check = sub.add_parser("check", help="check index/worktree or a "
                           "committed tree")
    check.add_argument("--repo", required=True,
                       help="repository root to check")
    check.add_argument("--tree", default=None,
                       help="check a committed tree REF instead of the "
                            "index and working tree")
    check.add_argument("--expect", action="append", default=[],
                       help="extra top-level entry to expect "
                            "(repeatable)")
    check.add_argument("--format", choices=["text", "json"],
                       default="text")
    check.set_defaults(func=cmd_check)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
