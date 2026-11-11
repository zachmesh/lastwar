#!/usr/bin/env python3
"""Safe pass worktrees for the Last War routine.

Every ticker, planner and knowledge-organizer pass that needs a
temporary worktree (records branch, delivery branch, PR branch)
creates it through this tool instead of a bare ``git worktree add``.

Why a tool exists for this: on 2026-11-07 three ticker passes
created their worktrees under /tmp (/tmp/ticker-2204-1107,
/tmp/ticker-2304-1107, /tmp/ticker-2334-1107) and all three
vanished between about 23:42 and 23:43 local, taking uncommitted
records, INDEX appends and unit completions with them (issue
#429; recovery note in _records_/2026-11-07/alliance-donations/
2341-queue-run.md). The deleter is the agent runtime's /tmp
sweep on this VM: /tmp here is a 512M tmpfs the runtime wipes
(the same failure already took /tmp/lastwar-ticker-1834 mid-run
on 2026-11-05), while the VPS origin-tmp-cleanup service only
removes /tmp entries untouched for 7 days (0.25 days for
*.bundle), skips anything a process holds open, logs every
deletion, and its log shows its last run before the 2334 pass
deleted only bundles. /tmp is documented ephemeral on this VM,
so the location - not the sweep - is what this tool changes:
pass worktrees live under ~/workspace/lastwar-worktrees/ and
this tool refuses any target under the system temp directory.

Three commands, standard library only:

  create - create a worktree under the worktrees root (default
           <parent of the main checkout>/lastwar-worktrees, so
           ~/workspace/lastwar gives ~/workspace/lastwar-worktrees;
           override with --root or LASTWAR_WORKTREES_ROOT). The
           name must be lowercase kebab-case (letters, digits,
           hyphens, dots). --branch defaults to the name; when
           the branch already exists it is checked out instead
           of created. --base is the start point for a new
           branch (default HEAD). Any --root or target under
           the system temp directory is refused, and a name
           that already exists under the root is refused, so
           a second create is a clean error, never a duplicate.
           Exit 0 on success, 1 when git fails, 2 on a usage
           or input error (bad name, /tmp target, not a repo).
  list   - list the worktrees under the root with branch, HEAD
           and age, plus orphan directories that are not git
           worktrees. Exit 0, 2 when the root cannot be resolved.
  prune  - remove stale worktrees under the root. Dry-run by
           default: report what would be removed. --write
           applies it with ``git worktree remove --force``.
           A worktree is removed only when every gate holds:
           its directory is older than --older-than-hours
           (default 24), nothing under it was written in the
           last hour (a live pass is writing records), it is
           not locked, it is not the main checkout, the
           current working directory is not inside it, its
           branch is fully merged into main (so an open PR
           branch is never pruned), and it holds no
           uncommitted changes. Orphan directories are never
           removed, only reported. Exit 0 when everything
           requested was removed (or nothing qualified), 1
           when a removal failed, 2 on a usage error.

Usage:
  pass_worktree.py [--root DIR] create NAME [--branch BRANCH] [--base REF]
  pass_worktree.py [--root DIR] list [--format text|json]
  pass_worktree.py [--root DIR] prune [--older-than-hours N] [--dry-run|--write]
                   [--format text|json]
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+([-.][a-z0-9]+)*$")
LIVE_WRITE_WINDOW_SECONDS = 3600
DEFAULT_PRUNE_OLDER_HOURS = 24


class ToolError(Exception):
    """An input or usage error: exit 2."""


def run_git(args, cwd):
    """Run a git command, returning the CompletedProcess."""
    return subprocess.run(
        ["git"] + args, cwd=str(cwd), capture_output=True, text=True
    )


def main_checkout():
    """Absolute path of the repository's main worktree.

    ``git worktree list`` prints the main worktree first, so this
    works whether the caller stands in the main checkout or in a
    linked worktree.
    """
    proc = run_git(["worktree", "list", "--porcelain"], cwd=Path.cwd())
    if proc.returncode != 0:
        raise ToolError(
            "not inside a git repository: %s" % proc.stderr.strip()
        )
    for line in proc.stdout.splitlines():
        if line.startswith("worktree "):
            return Path(line[len("worktree "):].strip())
    raise ToolError("git worktree list returned no worktree")


def default_root(main):
    """<parent of the main checkout>/lastwar-worktrees."""
    return Path(main).resolve().parent / "lastwar-worktrees"


def is_under(path, parent):
    """True when resolved path is parent itself or inside it."""
    try:
        Path(path).resolve().relative_to(Path(parent).resolve())
        return True
    except ValueError:
        return False


def resolve_root(cli_root, main):
    """Worktrees root: --root, LASTWAR_WORKTREES_ROOT, or the default.

    Any root under the system temp directory is refused: that is
    the failure this tool exists to prevent (issue #429).
    """
    raw = cli_root or os.environ.get("LASTWAR_WORKTREES_ROOT")
    root = Path(raw).expanduser() if raw else default_root(main)
    root = root.resolve()
    tmp = Path(tempfile.gettempdir()).resolve()
    if is_under(root, tmp):
        raise ToolError(
            "refusing worktrees root under the temp directory: %s "
            "(temp dir %s; pass worktrees must live under "
            "~/workspace/lastwar-worktrees/, never /tmp - issue #429)"
            % (root, tmp)
        )
    return root


def validate_name(name):
    if not NAME_RE.match(name):
        raise ToolError(
            "bad worktree name %r: use lowercase kebab-case "
            "(letters, digits, hyphens, dots)" % name
        )
    return name


def validate_branch(branch):
    """A git branch name: slash-separated components of safe characters."""
    parts = branch.split("/")
    if (
        not parts
        or any(not part or part in (".", "..") or part.startswith(".") for part in parts)
        or not all(re.match(r"^[A-Za-z0-9._-]+$", part) for part in parts)
    ):
        raise ToolError("bad branch name %r" % branch)
    return branch


def worktree_entries(main):
    """Parse ``git worktree list --porcelain`` into dicts."""
    proc = run_git(["worktree", "list", "--porcelain"], cwd=main)
    if proc.returncode != 0:
        raise ToolError("git worktree list failed: %s" % proc.stderr.strip())
    entries = []
    entry = None
    for line in proc.stdout.splitlines():
        if not line.strip():
            if entry is not None:
                entries.append(entry)
            entry = None
        elif line.startswith("worktree "):
            entry = {"path": line[len("worktree "):].strip()}
        elif entry is not None:
            if line.startswith("HEAD "):
                entry["head"] = line[len("HEAD "):].strip()
            elif line.startswith("branch "):
                entry["branch"] = line[len("branch "):].strip()
            elif line == "bare":
                entry["bare"] = True
            elif line == "detached":
                entry["detached"] = True
            elif line == "locked":
                entry["locked"] = True
            elif line.startswith("locked "):
                entry["locked"] = True
                entry["lock_reason"] = line[len("locked "):].strip()
            elif line == "prunable":
                entry["prunable"] = True
    if entry is not None:
        entries.append(entry)
    return entries


def branch_exists(main, branch):
    proc = run_git(
        ["show-ref", "--verify", "--quiet", "refs/heads/" + branch],
        cwd=main,
    )
    return proc.returncode == 0


def newest_mtime(path):
    """Latest mtime of a path and everything under it."""
    newest = 0.0
    for dirpath, dirnames, filenames in os.walk(path):
        for name in dirnames + filenames:
            try:
                newest = max(newest, os.lstat(os.path.join(dirpath, name)).st_mtime)
            except FileNotFoundError:
                continue
    try:
        newest = max(newest, os.lstat(path).st_mtime)
    except FileNotFoundError:
        pass
    return newest


def cmd_create(args, main, root):
    name = validate_name(args.name)
    target = (root / name).resolve()
    if is_under(target, Path(tempfile.gettempdir()).resolve()):
        raise ToolError(
            "refusing worktree under the temp directory: %s "
            "(issue #429)" % target
        )
    if target.exists():
        raise ToolError("worktree path already exists: %s" % target)
    branch = validate_branch(args.branch or name)
    root.mkdir(parents=True, exist_ok=True)
    if branch_exists(main, branch):
        cmd = ["worktree", "add", str(target), branch]
    else:
        cmd = ["worktree", "add", str(target), "-b", branch]
        if args.base:
            cmd.append(args.base)
    proc = run_git(cmd, cwd=main)
    if proc.returncode != 0:
        print(proc.stderr.strip(), file=sys.stderr)
        return 1
    if args.format == "json":
        print(json.dumps({"path": str(target), "branch": branch}, indent=2))
    else:
        print(str(target))
        print("branch %s" % branch)
    return 0


def cmd_list(args, main, root):
    entries = worktree_entries(main)
    under = [e for e in entries if is_under(e["path"], root)]
    now = time.time()
    rows = []
    for entry in under:
        path = Path(entry["path"])
        try:
            age_hours = (now - os.lstat(path).st_mtime) / 3600.0
        except FileNotFoundError:
            age_hours = None
        rows.append(
            {
                "path": entry["path"],
                "name": path.name,
                "branch": entry.get("branch", "(detached)"),
                "head": entry.get("head", "")[:12],
                "locked": bool(entry.get("locked")),
                "prunable": bool(entry.get("prunable")),
                "age_hours": None if age_hours is None else round(age_hours, 1),
            }
        )
    if root.is_dir():
        known = {r["path"] for r in rows}
        for child in sorted(root.iterdir()):
            if child.is_dir() and str(child.resolve()) not in known:
                rows.append(
                    {
                        "path": str(child.resolve()),
                        "name": child.name,
                        "branch": "(not a git worktree)",
                        "head": "",
                        "locked": False,
                        "prunable": False,
                        "age_hours": None,
                        "orphan": True,
                    }
                )
    if args.format == "json":
        print(json.dumps(rows, indent=2))
    else:
        if not rows:
            print("no worktrees under %s" % root)
        for row in rows:
            age = (
                "age %.1fh" % row["age_hours"]
                if row["age_hours"] is not None
                else "age ?"
            )
            flags = "".join(
                [
                    " locked" if row["locked"] else "",
                    " prunable" if row["prunable"] else "",
                    " orphan" if row.get("orphan") else "",
                ]
            )
            print(
                "%s  %s  %s  %s%s"
                % (row["name"], row["branch"], row["head"], age, flags)
            )
    return 0


def cmd_prune(args, main, root):
    now = time.time()
    older_than = args.older_than_hours * 3600.0
    cwd = Path.cwd().resolve()
    entries = worktree_entries(main)
    under = {
        Path(e["path"]).resolve(): e
        for e in entries
        if is_under(e["path"], root)
    }
    removed = []
    skipped = []
    would_remove = []
    failed = []
    if not root.is_dir():
        if args.format == "json":
            print(json.dumps({"removed": [], "skipped": [], "would_remove": []}, indent=2))
        else:
            print("worktrees root does not exist, nothing to prune: %s" % root)
        return 0
    for child in sorted(root.iterdir()):
        if not child.is_dir():
            continue
        path = child.resolve()
        if path == Path(main).resolve():
            skipped.append({"path": str(path), "reason": "is the main checkout"})
            continue
        entry = under.get(path)
        if entry is None:
            skipped.append({"path": str(path), "reason": "not a git worktree"})
            continue
        if entry.get("bare"):
            skipped.append({"path": str(path), "reason": "bare worktree"})
            continue
        if entry.get("locked"):
            skipped.append({"path": str(path), "reason": "locked"})
            continue
        if is_under(cwd, path):
            skipped.append(
                {"path": str(path), "reason": "current working directory is inside it"}
            )
            continue
        try:
            dir_age = now - os.lstat(path).st_mtime
        except FileNotFoundError:
            continue
        if dir_age < older_than:
            skipped.append(
                {
                    "path": str(path),
                    "reason": "younger than %.1fh" % args.older_than_hours,
                }
            )
            continue
        if now - newest_mtime(path) < LIVE_WRITE_WINDOW_SECONDS:
            skipped.append(
                {"path": str(path), "reason": "written in the last hour (live pass?)"}
            )
            continue
        branch = (entry.get("branch") or "").removeprefix("refs/heads/")
        if not branch or entry.get("detached"):
            skipped.append({"path": str(path), "reason": "detached HEAD"})
            continue
        proc = run_git(
            ["merge-base", "--is-ancestor", branch, "main"], cwd=main
        )
        if proc.returncode != 0:
            skipped.append(
                {"path": str(path), "reason": "branch %s not merged into main" % branch}
            )
            continue
        proc = run_git(["status", "--porcelain"], cwd=path)
        if proc.returncode == 0 and proc.stdout.strip():
            skipped.append(
                {"path": str(path), "reason": "has uncommitted changes"}
            )
            continue
        if args.write:
            proc = run_git(["worktree", "remove", "--force", str(path)], cwd=main)
            if proc.returncode != 0:
                failed.append({"path": str(path), "reason": proc.stderr.strip()})
            else:
                removed.append(str(path))
        else:
            would_remove.append(str(path))
    if args.format == "json":
        print(
            json.dumps(
                {
                    "removed": removed,
                    "skipped": skipped,
                    "would_remove": would_remove,
                    "failed": failed,
                },
                indent=2,
            )
        )
    else:
        for path in would_remove:
            print("would-remove %s" % path)
        for path in removed:
            print("removed %s" % path)
        for item in skipped:
            print("skip %s (%s)" % (item["path"], item["reason"]))
        for item in failed:
            print("FAILED %s: %s" % (item["path"], item["reason"]), file=sys.stderr)
        if not would_remove and not removed and not skipped and not failed:
            print("nothing to prune under %s" % root)
    return 1 if failed else 0


def build_parser():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--root",
        default=None,
        help="worktrees root (default <parent of main checkout>/"
        "lastwar-worktrees; env LASTWAR_WORKTREES_ROOT)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_create = sub.add_parser("create", help="create a worktree under the root")
    p_create.add_argument("name", help="worktree directory name (lowercase kebab-case)")
    p_create.add_argument("--branch", default=None, help="branch (default: the name)")
    p_create.add_argument("--base", default=None, help="start point for a new branch")
    p_create.add_argument("--format", choices=["text", "json"], default="text")

    p_list = sub.add_parser("list", help="list worktrees under the root")
    p_list.add_argument("--format", choices=["text", "json"], default="text")

    p_prune = sub.add_parser("prune", help="remove stale worktrees (dry-run by default)")
    p_prune.add_argument(
        "--older-than-hours",
        type=float,
        default=DEFAULT_PRUNE_OLDER_HOURS,
        help="only worktrees older than this (default 24)",
    )
    p_prune.add_argument("--write", action="store_true", help="actually remove (default dry-run)")
    p_prune.add_argument("--dry-run", action="store_true", help="report only (the default)")
    p_prune.add_argument("--format", choices=["text", "json"], default="text")
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        main = main_checkout()
        root = resolve_root(args.root, main)
    except ToolError as exc:
        print("pass_worktree: %s" % exc, file=sys.stderr)
        return 2
    try:
        if args.command == "create":
            return cmd_create(args, main, root)
        if args.command == "list":
            return cmd_list(args, main, root)
        if args.command == "prune":
            return cmd_prune(args, main, root)
    except ToolError as exc:
        print("pass_worktree: %s" % exc, file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    sys.exit(main())
