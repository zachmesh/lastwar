#!/usr/bin/env python3
"""tool_sync: bring the live checkout's _tools_/ up to origin main, safely, so the stale-tool guard never refuses a tick.

The queue's tool-currency guard (issue 694) refuses `next`, `enqueue`, `sync`, `plan` and `sweep` when the live copy of queue.py
differs from main's and is not ahead of it. Every PR that changes queue.py therefore stopped the planner until someone synced the live
checkout by hand. Run this as the first step of every tick; it is silent when there is nothing to do.

  1. fetch origin main into the guard's private ref (refs/queue-fresh/main; whole, no tags, no remote-tracking ref touched);
  2. list the tool files under _tools_/ (not _tools_/state/) that differ between HEAD and that ref and classify each from the file's own
     history: behind (origin has a newer version: sync it), ahead (this checkout holds a later or its own version: leave it), or
     diverged (both changed);
  3. if no file to sync has an uncommitted change, check those files out from origin and commit just them, through the gate (the repo's
     own hooks run; never --no-verify), as `chore(tools): sync live tools from origin after PR N`;
  4. otherwise REFUSE and print the file names; nothing is overwritten.

Prints `synced N files` or nothing when equal (or only ahead). Exit 0 equal or synced, 1 refused (a local change, a diverged file, or a
branch other than --branch), 2 a git error (the fetch, the commit; a refused commit is rolled back). --dry-run reports `would sync` and
changes nothing. Standard library only; no secret is ever printed.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REF = "refs/queue-fresh/main"            # the private ref queue.py's guard fetches into, so one fetch serves both
TOOLS = "_tools_"
SKIP = "_tools_/state"


class GitError(Exception):
    pass


def git(root: Path, *args: str, ok=(0,), text=True, timeout=120):
    try:
        out = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=text, timeout=timeout)
    except (OSError, subprocess.SubprocessError) as exc:
        raise GitError(f"git {args[0]}: {type(exc).__name__}")
    if out.returncode not in ok:
        tail = (out.stderr if text else out.stderr.decode("utf-8", "replace")).strip().splitlines()[-3:]
        raise GitError(f"git {args[0]} failed: {' | '.join(tail)[:300]}")
    return out.stdout


def remote_of(root: Path, name: str = "") -> str:
    remotes = [r.strip() for r in git(root, "remote").splitlines() if r.strip()]
    if name:
        if name not in remotes:
            raise GitError(f"no remote {name}")
        return name
    for preferred in ("origin", "github"):
        if preferred in remotes:
            return preferred
    if remotes:
        return remotes[0]
    raise GitError("no git remote")


def fetch_main(root: Path, remote: str) -> None:
    git(root, "fetch", "--no-tags", "--refmap=", remote, f"+main:{REF}", timeout=180)


def blob(root: Path, rev: str, path: str):
    out = subprocess.run(["git", "-C", str(root), "rev-parse", "--verify", "-q", f"{rev}:{path}"], capture_output=True, text=True)
    return out.stdout.strip() if out.returncode == 0 else None


def history(root: Path, rev: str, path: str) -> set[str]:
    """Every blob id this path has had in rev's history (what the guard's _history_has_blob reads)."""
    out = git(root, "log", "--format=", "--raw", "--no-abbrev", "-m", rev, "--", path)
    ids = set()
    for line in out.splitlines():
        parts = line.split()
        if line.startswith(":") and len(parts) >= 5:
            ids.update(parts[2:4])
    ids.discard("0" * 40)
    return ids


def differing(root: Path) -> list[tuple[str, str]]:
    out = git(root, "diff", "--no-renames", "--name-status", "HEAD", REF, "--", TOOLS, f":(exclude){SKIP}")
    rows = []
    for line in out.splitlines():
        status, _tab, path = line.partition("\t")
        if status[:1] in ("A", "M", "D") and path:
            rows.append((status[:1], path))
    return rows


def classify(root: Path, rows) -> dict:
    """behind (sync), ahead (leave), diverged (refuse): from the file's own history on both sides."""
    out = {"behind": [], "ahead": [], "diverged": []}
    for status, path in rows:
        local, origin = blob(root, "HEAD", path), blob(root, REF, path)
        if status == "A":                                    # origin has it, this checkout does not
            kind = "ahead" if origin in history(root, "HEAD", path) else "behind"
        elif status == "D":                                  # this checkout has it, origin does not
            kind = "behind" if local in history(root, REF, path) else "ahead"
        elif origin in history(root, "HEAD", path):
            kind = "ahead"
        elif local in history(root, REF, path):
            kind = "behind"
        else:
            kind = "diverged"
        out[kind].append((status, path))
    return out


def pr_label(root: Path) -> str:
    """The newest merged PR number between HEAD and origin main, else the origin tip's short id."""
    subjects = git(root, "log", "--format=%s", f"HEAD..{REF}").splitlines() or git(root, "log", "-1", "--format=%s", REF).splitlines()
    for subject in subjects:
        m = re.search(r"Merge pull request #(\d+)", subject) or re.search(r"\(#(\d+)\)\s*$", subject)
        if m:
            return f"PR {m.group(1)}"
    return "origin " + git(root, "rev-parse", "--short=8", REF).strip()


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=str(HERE.parent.parent), help="the live checkout (default: the one holding this tool)")
    p.add_argument("--remote", default="", help="the remote to fetch main from (default: origin, then github, then the first)")
    p.add_argument("--branch", default="main", help="the only branch a sync is committed on (default main)")
    p.add_argument("--dry-run", action="store_true", help="report what would sync; change nothing")
    a = p.parse_args(argv)
    root = Path(a.root).resolve()
    try:
        fetch_main(root, remote_of(root, a.remote))
        rows = differing(root)
        sets = classify(root, rows)
        behind = [path for _s, path in sets["behind"]]
        if not behind and not sets["diverged"]:
            return 0                                          # equal, or only ahead of origin: nothing to do, nothing to say
        refused = [f"{path} (diverged: both changed)" for _s, path in sets["diverged"]]
        dirty = git(root, "status", "--porcelain=v1", "--untracked-files=all", "--", *behind).splitlines() if behind else []
        refused += [f"{line[3:]} (uncommitted local change)" for line in dirty]
        if refused:
            print(f"tool_sync refused: {len(refused)} tool file(s) cannot be synced and nothing was changed: " + "; ".join(sorted(refused)))
            return 1
        current = git(root, "symbolic-ref", "--short", "-q", "HEAD", ok=(0, 1)).strip()
        if current != a.branch:
            print(f"tool_sync refused: this checkout is on {current or 'a detached HEAD'}, not {a.branch}; a tool sync is committed on {a.branch} "
                  f"only (--branch to say otherwise); {len(behind)} file(s) are behind origin")
            return 1
        if a.dry_run:
            print(f"would sync {len(behind)} files: " + ", ".join(sorted(behind)))
            return 0
        message = f"chore(tools): sync live tools from origin after {pr_label(root)}"
        added = [path for status, path in sets["behind"] if status in ("A", "M")]
        removed = [path for status, path in sets["behind"] if status == "D"]
        try:
            if added:
                git(root, "checkout", REF, "--", *added)
            if removed:
                git(root, "rm", "-q", "--", *removed)
            git(root, "commit", "-q", "-m", message, "--", *behind)
        except GitError as exc:
            for path in behind:                               # put every file back to what HEAD holds: none had a local change
                try:
                    git(root, "reset", "-q", "HEAD", "--", path)
                    if blob(root, "HEAD", path):
                        git(root, "checkout", "HEAD", "--", path)
                    else:                                     # a file origin added: not in HEAD, so it goes
                        (root / path).unlink(missing_ok=True)
                except GitError:
                    pass
            raise GitError(f"the sync commit was refused and rolled back: {exc}")
        print(f"synced {len(behind)} files")
        return 0
    except GitError as exc:
        print(f"tool_sync: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
