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

Four commands, standard library only:

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
  sync   - refresh a pass worktree's ``_activities_`` and
           ``_conventions_`` trees from the fresh tip of main,
           so an executor never plays against a superseded
           profile (issue #631: the ticker-0434 pass executed
           its donations unit against a worktree copy of the
           alliance-donations profile at version 1.5.0 while
           main carried 1.96.0, and the stale rule - donate
           until the count reads 0 - spent the last donation
           against the changed route). By default the source
           is fetched from the ``github`` remote first, so a
           stale local main ref can never bless a stale
           worktree as current; ``--no-fetch`` uses the local
           ref as-is. A file the sync would overwrite is
           refused only when its disk content differs from
           both the index and main - a genuine local edit;
           a pristine stale file is updated, a file already
           matching main is in sync (so a re-run is a
           no-op), a file missing on disk is restored, and
           a file main does not have is reported and left
           alone. The sync updates the working tree only -
           never the index, so a delivery commit by explicit
           pathspec cannot sweep the refreshed profiles
           into a records branch - and re-verifies every
           refreshed file against the source blob before
           reporting. Exit 0 when synced (or already
           in sync), 1 when a git operation or the
           post-sync verification fails, 2 when the sync
           cannot run (bad path, not a worktree under the
           root, the main checkout itself, a locally edited
           file, fetch or ref failure).
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
  pass_worktree.py [--root DIR] sync PATH [--ref REF] [--remote NAME] [--no-fetch]
                   [--format text|json]
  pass_worktree.py [--root DIR] list [--format text|json]
  pass_worktree.py [--root DIR] prune [--older-than-hours N] [--dry-run|--write]
                   [--format text|json]
"""

import argparse
import hashlib
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
SYNC_TREES = ("_activities_", "_conventions_")
DEFAULT_SYNC_REMOTE = "github"


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


def git_blob_sha(data):
    """The git blob id for `data` (sha1 of "blob <len>" + NUL + data)."""
    head = ("blob %d" % len(data)).encode("ascii") + bytes([0])
    return hashlib.sha1(head + data).hexdigest()


def index_blobs(worktree):
    """Map of relpath -> blob sha for the sync trees in the index."""
    proc = run_git(
        ["ls-files", "-s", "--"] + list(SYNC_TREES), cwd=worktree
    )
    if proc.returncode != 0:
        raise ToolError(
            "git ls-files of %s failed: %s" % (worktree, proc.stderr.strip())
        )
    tree = {}
    for line in proc.stdout.splitlines():
        if not line.strip():
            continue
        meta, _, path = line.partition("\t")
        parts = meta.split()
        if len(parts) < 3 or not path:
            raise ToolError("unparsable ls-files line: %r" % line)
        tree[path] = parts[1]
    return tree


def working_tree_blobs(path):
    """Map of relpath -> blob sha for the sync trees on disk under `path`.

    A regular file is hashed with ``git hash-object``, which applies
    the same clean filters (line-ending and text-attribute conversion)
    git itself would apply, so a checked-out file compares equal to
    its source blob even where the checkout converted line endings.
    A symlink contributes the blob id of its target string, the same
    value git stores for a mode-120000 entry, so a symlinked profile
    compares equal to the source tree instead of looking stale.
    """
    tree = {}
    for tree_name in SYNC_TREES:
        base = Path(path) / tree_name
        if not base.is_dir():
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            for name in filenames:
                full = Path(dirpath) / name
                rel = str(full.relative_to(path))
                try:
                    if full.is_symlink():
                        data = os.readlink(full).encode()
                        tree[rel] = git_blob_sha(data)
                        continue
                except OSError as exc:
                    raise ToolError("cannot read %s: %s" % (full, exc))
                proc = run_git(["hash-object", rel], cwd=path)
                if proc.returncode != 0:
                    raise ToolError(
                        "git hash-object of %s failed: %s"
                        % (full, proc.stderr.strip())
                    )
                tree[rel] = proc.stdout.strip()
    return tree


def source_tree_blobs(main, sha):
    """Map of relpath -> blob sha for the sync trees at commit `sha`."""
    proc = run_git(
        ["ls-tree", "-r", "--full-name", sha, "--"] + list(SYNC_TREES),
        cwd=main,
    )
    if proc.returncode != 0:
        raise ToolError(
            "git ls-tree of %s failed: %s" % (sha, proc.stderr.strip())
        )
    tree = {}
    for line in proc.stdout.splitlines():
        if not line.strip():
            continue
        meta, _, path = line.partition("\t")
        parts = meta.split()
        if len(parts) < 3 or not path:
            raise ToolError("unparsable ls-tree line: %r" % line)
        if not any(
            path == tree_name or path.startswith(tree_name + "/")
            for tree_name in SYNC_TREES
        ):
            continue
        tree[path] = parts[2]
    if not tree:
        raise ToolError(
            "commit %s holds no %s tree" % (sha, " or ".join(SYNC_TREES))
        )
    return tree


def resolve_source(main, ref, remote, fetch):
    """(sha, commit ISO time, fetched) for the sync source.

    With fetch, the remote's ref is fetched first and the source is
    the remote-tracking ref, so a stale local ref can never be the
    source. Without fetch, the local ref is used as-is.
    """
    if fetch:
        proc = run_git(["fetch", remote, ref], cwd=main)
        if proc.returncode != 0:
            raise ToolError(
                "git fetch %s %s failed: %s"
                % (remote, ref, proc.stderr.strip())
            )
        tracking = "refs/remotes/%s/%s" % (remote, ref)
        proc = run_git(
            ["rev-parse", "--verify", tracking + "^{commit}"], cwd=main
        )
        if proc.returncode != 0:
            raise ToolError(
                "no remote-tracking ref %s after fetching %s %s"
                % (tracking, remote, ref)
            )
        sha = proc.stdout.strip()
    else:
        proc = run_git(["rev-parse", "--verify", ref + "^{commit}"], cwd=main)
        if proc.returncode != 0:
            raise ToolError(
                "cannot resolve ref %r: %s" % (ref, proc.stderr.strip())
            )
        sha = proc.stdout.strip()
    proc = run_git(["show", "-s", "--format=%cI", sha], cwd=main)
    when = proc.stdout.strip() if proc.returncode == 0 else "unknown"
    return sha, when, fetch


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


def cmd_sync(args, main, root):
    target = Path(args.path).expanduser().resolve()
    if not target.is_dir():
        raise ToolError("no such worktree directory: %s" % target)
    if not is_under(target, root):
        raise ToolError(
            "worktree %s is not under the worktrees root %s"
            % (target, root)
        )
    if target == Path(main).resolve():
        raise ToolError(
            "refusing to sync the main checkout itself: %s "
            "(sync is for pass worktrees under the root)" % target
        )
    entries = worktree_entries(main)
    entry = next(
        (e for e in entries if Path(e["path"]).resolve() == target), None
    )
    if entry is None:
        raise ToolError(
            "%s is not a git worktree of this repository" % target
        )
    if entry.get("bare"):
        raise ToolError("refusing to sync a bare worktree: %s" % target)
    sha, when, fetched = resolve_source(
        main, args.ref, args.remote, not args.no_fetch
    )
    source = source_tree_blobs(main, sha)
    disk = working_tree_blobs(target)
    index = index_blobs(target)
    # A file the sync would overwrite is refused only when its disk
    # content is a genuine local edit: it differs from both the
    # source blob and the index blob. A pristine stale file (disk ==
    # index) is updated; a file already matching the source (a
    # previous sync left it as an unstaged modification, because the
    # sync updates the working tree only) is in sync, so a re-run is
    # a no-op instead of a refusal. A file missing on disk is
    # restored from the source; a file main does not have is reported
    # as extra and left alone - the restore never touches it.
    refused = sorted(
        p
        for p in source
        if p in disk and disk[p] != source[p] and disk[p] != index.get(p)
    )
    if refused:
        raise ToolError(
            "refusing to sync %s: locally modified under %s "
            "(differs from both the index and %s %s):\n%s"
            % (
                target,
                " / ".join(SYNC_TREES),
                args.ref,
                sha[:12],
                "\n".join("  " + p for p in refused),
            )
        )
    updated = sorted(
        p for p in source if p in disk and disk[p] != source[p]
    )
    added = sorted(p for p in source if p not in disk)
    extra = sorted(p for p in disk if p not in source)
    unchanged = len(source) - len(updated) - len(added)
    report = {
        "worktree": str(target),
        "source": {
            "ref": args.ref,
            "remote": None if args.no_fetch else args.remote,
            "sha": sha,
            "commit_time": when,
            "fetched": fetched,
        },
        "compared": len(source),
        "updated": updated,
        "added": added,
        "extra": extra,
        "unchanged": unchanged,
        "already_in_sync": not updated and not added,
    }
    if updated or added:
        proc = run_git(
            ["restore", "--source=%s" % sha, "--worktree", "--"]
            + list(SYNC_TREES),
            cwd=target,
        )
        if proc.returncode != 0:
            print(proc.stderr.strip(), file=sys.stderr)
            return 1
        after = working_tree_blobs(target)
        still = sorted(p for p in updated + added if after.get(p) != source[p])
        if still:
            print(
                "sync incomplete, still stale after restore: %s"
                % ", ".join(still),
                file=sys.stderr,
            )
            return 1
    if args.format == "json":
        print(json.dumps(report, indent=2))
    else:
        if report["already_in_sync"]:
            print(
                "%s already in sync with %s %s"
                % (target, args.ref, sha[:12])
            )
        else:
            for path in updated:
                print("updated %s" % path)
            for path in added:
                print("restored %s" % path)
            for path in extra:
                print("extra (left alone) %s" % path)
            print(
                "%s synced to %s %s (%s, %d updated, %d restored, "
                "%d unchanged, %d extra left alone)"
                % (
                    target,
                    args.ref,
                    sha[:12],
                    when,
                    len(updated),
                    len(added),
                    unchanged,
                    len(extra),
                )
            )
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

    p_sync = sub.add_parser(
        "sync",
        help="refresh a pass worktree's activity and convention trees "
        "from current main",
    )
    p_sync.add_argument("path", help="worktree directory to sync")
    p_sync.add_argument("--ref", default="main", help="source ref (default main)")
    p_sync.add_argument(
        "--remote",
        default=DEFAULT_SYNC_REMOTE,
        help="remote to fetch the source ref from (default github)",
    )
    p_sync.add_argument(
        "--no-fetch",
        action="store_true",
        help="use the local ref without fetching",
    )
    p_sync.add_argument("--format", choices=["text", "json"], default="text")

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
        if args.command == "sync":
            return cmd_sync(args, main, root)
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
