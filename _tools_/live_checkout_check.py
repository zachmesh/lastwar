#!/usr/bin/env python3
"""Live-checkout drift check - does the live checkout still run main's tools?

The ticker and planner job bodies call ``python3 tools/queue.py`` from
the live checkout (``~/workspace/lastwar``), and no job re-syncs that
checkout to main. After a tools fix merges to main, the live loop keeps
running the old code until a human notices - exactly how issue #410
happened (the #412 guard, #387 enqueue guard, #408 local-date fix and
#384 shared token were all on main while the ticker staged
stale-geometry pairs), and issue #415 is the standing gap that no
check exists to catch the next recurrence.

This tool is the check half of issue #415, candidate 1: a tool-side
check, no loop change. It compares the code tree the live checkout
would execute against main's ``_tools_/`` tree, file by file, by git
blob hash, and reports drift loudly. It never writes to the live
checkout and never changes the loop. Wiring it into a ticker or
planner pre-step touches job bodies and is an owner decision, still
owed on issue #415.

What counts as the code tree: every file under main's ``_tools_/``
except ``state/`` (the live tracker state legitimately advances ahead
of main's snapshots) and ``__pycache__/``. ``regulars.json``,
``duel_schedule.json`` and the other data files under ``_tools_/``
are compared too - the roster they carry is part of what went stale
in #410. Dotfiles inside the live tools directory are ignored.

How the live tools directory is resolved, in order:
  1. ``<live-root>/tools`` exists (symlink or real directory) - that
     is what the ticker executes, so it is what gets compared. A
     symlink is followed; a real directory is compared as-is and
     noted as the pre-rename layout.
  2. otherwise ``<live-root>/_tools_`` exists - compared, with a
     finding that the ``tools`` entry point the ticker calls is
     missing.
  3. otherwise the check cannot run: exit 2.

Which main is compared against: by default the ``main`` ref in
``--repo`` (default: the repository holding this script). The compared
commit is always printed, with its commit time, so a reader can see
whether the comparison used a fresh main or a stale local ref. With
``--remote`` the tool first resolves GitHub's main with
``git ls-remote`` (read-only, no fetch) and refuses to certify when
the remote has moved past the local ref - a stale local ref must
never bless a drifted checkout as in sync.

Exit codes, following records_batch.py:
  0 - the live tools match main's ``_tools_/`` code tree exactly.
  1 - drift detected: a file differs, is missing, is extra, is
      unreadable, or the ``tools`` entry point is missing.
  2 - the check cannot be run: live root missing, no tools
      directory at all, git unavailable, the ref missing, or the
      remote ahead of the local ref under ``--remote``.

Usage:
  live_checkout_check.py [--live-root DIR] [--repo DIR] [--ref REF]
                         [--remote [NAME]] [--format text|json]
"""

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

TOOL_VERSION = "1.0.0"
DEFAULT_LIVE_ROOT = Path.home() / "workspace" / "lastwar"
EXCLUDED_DIRS = ("state", "__pycache__")


def git_blob_sha(data):
    """The git blob id for `data` (sha1 of "blob <len>\\0" + data)."""
    head = ("blob %d\0" % len(data)).encode("ascii")
    return hashlib.sha1(head + data).hexdigest()


def run_git(repo, *args):
    """Run git in `repo`; return (returncode, stdout, stderr)."""
    try:
        proc = subprocess.run(
            ["git", "-C", str(repo)] + list(args),
            capture_output=True, text=True, timeout=60,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise CheckError(f"could not run git: {exc}")
    return proc.returncode, proc.stdout, proc.stderr


class CheckError(Exception):
    """The check cannot be run; exit 2 with this message."""


def main_tree(repo, ref):
    """Map of relpath -> blob sha for main's _tools_/ code tree."""
    code, out, err = run_git(
        repo, "ls-tree", "-r", "--full-name", ref, "--", "_tools_")
    if code != 0:
        raise CheckError(
            f"git ls-tree of {ref!r} in {repo} failed: {err.strip()}")
    tree = {}
    for line in out.splitlines():
        if not line.strip():
            continue
        meta, _, path = line.partition("\t")
        parts = meta.split()
        if len(parts) < 3 or not path:
            raise CheckError(f"unparsable ls-tree line: {line!r}")
        sha = parts[2]
        if not path.startswith("_tools_/"):
            continue
        rel = path[len("_tools_/"):]
        if any(part in EXCLUDED_DIRS for part in rel.split("/")):
            continue
        tree[rel] = sha
    if not tree:
        raise CheckError(
            f"ref {ref!r} in {repo} holds no _tools_/ code tree")
    return tree


def main_head(repo, ref):
    """(short sha, commit ISO time) of `ref` in `repo`."""
    code, out, err = run_git(repo, "rev-parse", "--short", ref)
    if code != 0:
        raise CheckError(
            f"git rev-parse of {ref!r} in {repo} failed: {err.strip()}")
    sha = out.strip()
    code, out, err = run_git(repo, "show", "-s", "--format=%cI", ref)
    when = out.strip() if code == 0 else "unknown"
    return sha, when


def remote_main_sha(repo, remote):
    """The sha of main on `remote`, via read-only ls-remote."""
    try:
        proc = subprocess.run(
            ["git", "-C", str(repo), "ls-remote", remote,
             "refs/heads/main"],
            capture_output=True, text=True, timeout=60,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise CheckError(f"could not run git ls-remote: {exc}")
    if proc.returncode != 0:
        raise CheckError(
            f"git ls-remote {remote} failed: {proc.stderr.strip()}")
    fields = proc.stdout.split()
    if not fields:
        raise CheckError(f"remote {remote!r} has no refs/heads/main")
    return fields[0]


def resolve_live_tools(live_root):
    """Return (directory, layout, notes) for what the ticker executes.

    Layout is one of "symlink", "real-dir", "_tools_-only".
    Raises CheckError when the live checkout holds no tools at all.
    """
    notes = []
    tools_path = live_root / "tools"
    tools_dir = live_root / "_tools_"
    if tools_path.is_symlink() or tools_path.is_dir():
        target = os.path.realpath(tools_path)
        if tools_path.is_symlink():
            layout = "symlink"
            notes.append(f"tools -> {os.readlink(tools_path)}")
        else:
            layout = "real-dir"
            notes.append("tools is a real directory, not the "
                         "tools -> _tools_ symlink (pre-rename layout)")
        if not os.path.isdir(target):
            raise CheckError(
                f"live tools entry {tools_path} resolves to {target}, "
                "which is not a directory")
        return Path(target), layout, notes
    if tools_dir.is_dir():
        notes.append("tools entry point missing; comparing _tools_/ "
                     "instead (the ticker's python3 tools/... call "
                     "would fail)")
        return tools_dir, "_tools_-only", notes
    raise CheckError(
        f"live checkout {live_root} holds neither tools/ nor _tools_/; "
        "the ticker has nothing to execute")


def hash_live_tree(directory):
    """Map of relpath -> blob sha for the live tools directory.

    Skips state/, __pycache__/ and dotfiles, mirroring main_tree.
    A file that cannot be read is recorded under the sentinel sha
    "unreadable" so the comparison flags it instead of crashing.
    """
    tree = {}
    for dirpath, dirnames, filenames in os.walk(directory):
        dirnames[:] = [d for d in dirnames
                       if d not in EXCLUDED_DIRS
                       and not d.startswith(".")]
        for name in filenames:
            if name.startswith("."):
                continue
            full = Path(dirpath) / name
            rel = str(full.relative_to(directory))
            try:
                with open(full, "rb") as handle:
                    data = handle.read()
            except OSError:
                tree[rel] = "unreadable"
                continue
            tree[rel] = git_blob_sha(data)
    return tree


def compare(expected, live):
    """Return (differing, missing, extra, unreadable) sorted lists."""
    differing = sorted(
        rel for rel, sha in expected.items()
        if rel in live and live[rel] not in (sha, "unreadable"))
    missing = sorted(rel for rel in expected if rel not in live)
    extra = sorted(rel for rel in live if rel not in expected)
    unreadable = sorted(
        rel for rel, sha in live.items() if sha == "unreadable")
    return differing, missing, extra, unreadable


def render_text(result):
    """The text report; deterministic, no wall-clock timestamps."""
    lines = [
        f"live-checkout-check {TOOL_VERSION}",
        f"live root: {result['live_root']}",
        f"repo: {result['repo']}  ref: {result['ref']}  "
        f"main head: {result['main_head']} ({result['main_head_time']})",
        f"live tools: {result['live_tools']} ({result['layout']})",
    ]
    lines.extend(f"note: {note}" for note in result["notes"])
    if result["status"] == "in-sync":
        lines.append(
            f"status: IN SYNC ({result['checked']} files match "
            f"{result['ref']} {result['main_head']})")
    else:
        lines.append(
            f"status: DRIFTED ({result['checked']} files checked)")
        for kind in ("differing", "missing", "extra", "unreadable"):
            names = result[kind]
            if names:
                lines.append(f"  {kind} ({len(names)}):")
                lines.extend(f"    _tools_/{name}" for name in names)
    return "\n".join(lines) + "\n"


def check(live_root, repo, ref, remote):
    """Run the comparison; return (exit_code, result dict)."""
    if not live_root.is_dir():
        raise CheckError(f"live root {live_root} is not a directory")
    if not (repo / ".git").exists() and not run_git(
            repo, "rev-parse", "--git-dir")[0] == 0:
        raise CheckError(f"repo {repo} is not a git checkout")
    short, when = main_head(repo, ref)
    if remote is not None:
        remote_sha = remote_main_sha(repo, remote)
        code, out, _ = run_git(repo, "rev-parse", ref)
        local_sha = out.strip() if code == 0 else ""
        if remote_sha != local_sha:
            raise CheckError(
                f"remote {remote} main is {remote_sha[:12]} but the "
                f"local ref {ref} in {repo} is "
                f"{local_sha[:12] or 'unknown'}; re-fetch before "
                "certifying the live checkout, a stale local ref "
                "must not bless it as in sync")
    expected = main_tree(repo, ref)
    live_dir, layout, notes = resolve_live_tools(live_root)
    live = hash_live_tree(live_dir)
    differing, missing, extra, unreadable = compare(expected, live)
    drifted = bool(differing or missing or extra or unreadable
                   or layout == "_tools_-only")
    if layout == "_tools_-only":
        notes.append("tools entry point missing (drift)")
    result = {
        "tool": "live_checkout_check",
        "version": TOOL_VERSION,
        "live_root": str(live_root),
        "repo": str(repo),
        "ref": ref,
        "main_head": short,
        "main_head_time": when,
        "live_tools": str(live_dir),
        "layout": layout,
        "notes": notes,
        "checked": len(expected),
        "differing": differing,
        "missing": missing,
        "extra": extra,
        "unreadable": unreadable,
        "status": "drifted" if drifted else "in-sync",
    }
    return (1 if drifted else 0), result


def main(argv=None):
    """Parse args, run the check, print the report, exit 0/1/2."""
    parser = argparse.ArgumentParser(
        prog="live_checkout_check.py",
        description="Check the live checkout's tools against main's "
                    "_tools_/ (issue #415).")
    parser.add_argument("--live-root", type=Path, default=DEFAULT_LIVE_ROOT,
                        help="live checkout the ticker executes from "
                             "(default: %(default)s)")
    parser.add_argument("--repo", type=Path,
                        default=Path(__file__).resolve().parent.parent,
                        help="git checkout holding the ref to compare "
                             "against (default: the repo holding this "
                             "script)")
    parser.add_argument("--ref", default="main",
                        help="ref in --repo to compare against "
                             "(default: %(default)s)")
    parser.add_argument("--remote", nargs="?", const="origin", default=None,
                        metavar="NAME",
                        help="also resolve main on NAME with git "
                             "ls-remote and refuse to certify when it "
                             "has moved past the local ref "
                             "(default NAME: origin)")
    parser.add_argument("--format", choices=("text", "json"),
                        default="text")
    args = parser.parse_args(argv)
    try:
        code, result = check(args.live_root, args.repo, args.ref,
                             args.remote)
    except CheckError as exc:
        print(f"live-checkout-check: cannot run: {exc}", file=sys.stderr)
        return 2
    if args.format == "json":
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(render_text(result), end="")
    return code


if __name__ == "__main__":
    sys.exit(main())
