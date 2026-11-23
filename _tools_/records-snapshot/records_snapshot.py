#!/usr/bin/env python3
"""records_snapshot: land the records the live checkout holds, and converge local main with origin, without a merge.

Local main and origin main are different lines (a real merge shows hundreds of conflicts), and other seats' records are untracked in the
live checkout. `snapshot` therefore does not merge: it builds a branch on the origin tip and copies onto it only what local main adds or
changes. It never pushes, never touches main, the index or the working tree of the live checkout, and never deletes.

  records_snapshot.py snapshot [--base origin/main] [--branch land/records-<UTC>] [--exclude PATH ...] [--on-conflict main|origin|stop] [--dry-run]
  records_snapshot.py converge [--base origin/main] [--exclude PATH ...] [--dry-run]

snapshot: refuse unless the clone is whole and the working branch is main; make a scratch worktree of the branch on the base tip; take, from
local main, every ADDED or MODIFIED file (a rename is an add of the new path) outside the excluded paths, plus `_tools_/state/`; copy those
files (content and mode, binary-safe) onto the branch; run the gate on them and commit ONCE with a counts-only message; scan the whole branch
tree for denylist matches (patterns, file names, commit messages and authors); run the landing check (`check --base BASE --landing`);
remove the worktree. A file is judged against the merge base: only local main changed it (apply), only origin changed it (skip, origin is
newer), both changed it or both added it differently (--on-conflict: main's version by default, origin's, or stop), origin deleted it since
(skip). A path origin has and main lacks is never touched. Exit 0 only when the scan finds nothing, the landing check passes and the
parent is the base tip. Default excludes: `_tools_` code (not `_tools_/state/`) and `_activities_`, which the scribe's branches own;
giving any --exclude replaces the defaults.

converge: when every tracked file of local main outside the excluded paths equals origin's, move the branch ref main to the base without
touching the working tree (`git update-ref`, then a mixed `git reset`), keep the old tip under refs/backup/, and print how many tracked
paths then differ (the uncommitted work of other seats); otherwise refuse and print counts by folder.

Output is counts and folder names only. Exit 0 done, 1 refused or failed a check, 2 cannot run. Standard library only.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_EXCLUDES = ("_tools_", "_activities_")
STATE = "_tools_/state"
IMAGES = (".png", ".jpg", ".jpeg", ".gif", ".webp")
GATE_REL = "_tools_/lint-gate/lint_gate.py"


class Refusal(Exception):
    """A refusal (code 1: a rule said no) or a failure to run (code 2: git itself failed)."""

    def __init__(self, message: str, code: int = 1):
        super().__init__(message)
        self.code = code


def git(root: Path, *args: str, ok=(0,), text=True, input=None, timeout=600):
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    try:
        out = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=text, input=input, timeout=timeout, env=env)
    except (OSError, subprocess.SubprocessError) as exc:
        raise Refusal(f"git {args[0]}: {type(exc).__name__}", 2)
    if out.returncode not in ok:
        err = out.stderr if text else out.stderr.decode("utf-8", "replace")
        raise Refusal(f"git {args[0]} failed: {' | '.join(err.strip().splitlines()[-2:])[:240]}", 2)
    return out.stdout if text else out.stdout


def excluded(path: str, excludes) -> bool:
    for e in excludes:
        e = e.strip("/")
        if path == e or path.startswith(e + "/"):
            if e == "_tools_" and (path == STATE or path.startswith(STATE + "/")):
                continue                                   # the state is landed even when the code is excluded
            return True
    return False


def tree(root: Path, rev: str) -> dict[str, tuple[str, str]]:
    out = git(root, "ls-tree", "-r", "-z", "--full-tree", rev, text=False)
    files = {}
    for rec in out.split(b"\0"):
        if not rec:
            continue
        meta, _tab, name = rec.partition(b"\t")
        mode, _kind, blob = meta.decode().split()
        files[name.decode("utf-8", "surrogateescape")] = (mode, blob)
    return files


def folder(path: str) -> str:
    return path.split("/", 1)[0] if "/" in path else "(root)"


def preflight(root: Path, base: str) -> str:
    if git(root, "rev-parse", "--is-shallow-repository").strip() != "false":
        raise Refusal("this clone is shallow; fetch the whole history first (git fetch --unshallow origin)")
    branch = git(root, "symbolic-ref", "--short", "-q", "HEAD", ok=(0, 1)).strip()
    if branch != "main":
        raise Refusal(f"the working branch is {branch or 'a detached HEAD'}, not main")
    sha = git(root, "rev-parse", "--verify", "-q", f"{base}^{{commit}}", ok=(0, 1)).strip()
    if not sha:
        raise Refusal(f"the base {base} does not resolve")
    return sha


def histories(root: Path, rev: str, paths) -> dict[str, set[str]]:
    """path -> every blob id the path has had in rev's history, from one `git log --raw` (no rename detection)."""
    seen: dict[str, set[str]] = {p: set() for p in paths}
    if not paths:
        return seen
    for chunk in range(0, len(paths), 400):
        out = git(root, "log", "--format=", "--raw", "--no-abbrev", "--no-renames", "-m", "-z", rev, "--", *paths[chunk:chunk + 400], text=False)
        fields = out.split(b"\0")
        i = 0
        while i < len(fields):                                  # -z raw: ":modes old new status" then the path
            meta = fields[i].lstrip(b"\n").decode("ascii", "ignore")
            if meta.startswith(":") and i + 1 < len(fields):
                parts = meta.split()
                path = fields[i + 1].decode("utf-8", "surrogateescape")
                if path in seen and len(parts) >= 4:
                    seen[path].update(parts[2:4])
                i += 2
            else:
                i += 1
    for ids in seen.values():
        ids.discard("0" * 40)
    return seen


def plan(root: Path, base: str, excludes, on_conflict: str):
    """(apply, skipped, ahead, conflicts). apply is [(path, status)] with status A or M, and includes the ahead files. A file whose blobs differ
    on the two lines is main-ahead when origin's blob is already in main's history of it (origin holds an earlier version of main's: apply, no
    conflict), origin-ahead when main's blob is in origin's history (skip), and a true conflict otherwise (--on-conflict decides)."""
    main, origin = tree(root, "main"), tree(root, base)
    mb = git(root, "merge-base", base, "main", ok=(0, 1)).strip()
    anc = tree(root, mb) if mb else None
    apply, skipped, ahead, conflicts, both = [], Counter(), [], [], []
    for path, (mode, blob) in sorted(main.items()):
        if excluded(path, excludes) or mode == "160000":
            if mode == "160000":
                skipped["submodule"] += 1
            continue
        o = origin.get(path)
        if o == (mode, blob):
            continue
        if o is None:
            if anc is not None and path in anc:
                skipped["origin deleted it"] += 1
                continue
            apply.append((path, "A"))
            continue
        a = anc.get(path) if anc is not None else None
        if anc is not None and a == o:
            apply.append((path, "M"))
        elif anc is not None and a == (mode, blob):
            skipped["origin is newer"] += 1
        else:
            both.append(path)
    if both:
        in_main, in_origin = histories(root, "main", both), histories(root, base, both)
        for path in both:
            if origin[path][1] in in_main[path]:
                ahead.append(path)
                apply.append((path, "M"))
            elif main[path][1] in in_origin[path]:
                skipped["origin is newer"] += 1
            else:
                conflicts.append(path)
                if on_conflict == "main":
                    apply.append((path, "M"))
                elif on_conflict == "origin":
                    skipped["conflict kept origin's"] += 1
    return sorted(apply), skipped, ahead, conflicts


def read_patterns(root: Path):
    common = git(root, "rev-parse", "--git-common-dir").strip()
    path = (Path(common) if os.path.isabs(common) else root / common) / "privacy-denylist.txt"
    if not path.is_file():
        return None
    patterns = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            try:
                patterns.append(re.compile(line, re.IGNORECASE))
            except re.error:
                continue
    return patterns or None


def scan_branch(root: Path, branch: str, base: str, patterns) -> dict:
    """Counts only: files whose text matches, file names that match, images skipped, and commit messages or authors in base..branch that match."""
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    proc = subprocess.Popen(["git", "-C", str(root), "archive", "--format=tar", branch], stdout=subprocess.PIPE, env=env)
    files = names = hits = images = 0
    with tarfile.open(fileobj=proc.stdout, mode="r|") as archive:
        for member in archive:
            if not member.isfile():
                continue
            files += 1
            if any(p.search(member.name) for p in patterns):
                names += 1
            if member.name.lower().endswith(IMAGES):
                images += 1
                continue
            text = archive.extractfile(member).read().decode("utf-8", "ignore")
            if any(p.search(text) for p in patterns):
                hits += 1
    proc.wait()
    meta = git(root, "log", "--format=%B%n%an%n%ae", f"{base}..{branch}")
    commits = sum(len(p.findall(meta)) for p in patterns)
    return {"files": files, "matching": hits, "names": names, "images": images, "commits": commits}


def pick_gate(worktree: Path, root: Path, explicit: str) -> tuple[Path | None, bool]:
    """(gate script, supports --landing): the explicit one, else the branch's own, else the live checkout's."""
    candidates = [Path(explicit)] if explicit else [worktree / GATE_REL, root / GATE_REL]
    first = None
    for gate in candidates:
        if not gate.is_file():
            continue
        first = first or gate
        out = subprocess.run([sys.executable, "-B", str(gate), "check", "--help"], capture_output=True, text=True)
        if "--landing" in out.stdout:
            return gate, True
    return first, False


def run_gate(gate: Path, *args: str):
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    return subprocess.run([sys.executable, "-B", str(gate), *args], capture_output=True, text=True, env=env, timeout=1800)


def numbers_line(apply, skipped, ahead, conflicts, on_conflict, would: str) -> str:
    """The three numbers - applied, main ahead, true conflicts - and what was skipped. `would` is "would " in a dry run."""
    clean = len(apply) - len(ahead) - (len(conflicts) if on_conflict == "main" else 0)
    act = "would apply" if would else "applied"
    verb = {"stop": f"{would}stop", "main": f"{act} main's version", "origin": ("would keep" if would else "kept") + " origin's version"}[on_conflict]
    return (f"applied {clean} | main ahead {len(ahead)} ({act}: origin holds an earlier version of main's) | true conflicts "
            f"{len(conflicts)}" + (f" ({verb})" if conflicts else "") + " | skipped: "
            + (", ".join(f"{k} {v}" for k, v in sorted(skipped.items())) or "none"))


def by_folder(rows) -> str:
    counts = {}
    for path, status in rows:
        counts.setdefault(folder(path), Counter())[status] += 1
    return "; ".join(f"{f} " + " ".join(f"{s} {n}" for s, n in sorted(c.items())) for f, c in sorted(counts.items()))


def cmd_snapshot(a, root: Path) -> int:
    base_sha = preflight(root, a.base)
    excludes = tuple(a.exclude) if a.exclude else DEFAULT_EXCLUDES
    branch = a.branch or "land/records-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    if git(root, "rev-parse", "--verify", "-q", f"refs/heads/{branch}", ok=(0, 1)).strip():
        raise Refusal(f"the branch {branch} already exists")
    apply, skipped, ahead, conflicts = plan(root, a.base, excludes, a.on_conflict)
    if a.dry_run:
        counts = Counter(s for _p, s in apply)
        print(f"records_snapshot snapshot (dry run, nothing created): would land A {counts['A']}, M {counts['M']} on {a.base} {base_sha[:8]} | by folder: "
              f"{by_folder(apply)}")
        print(numbers_line(apply, skipped, ahead, conflicts, a.on_conflict, "would "))
        if conflicts:
            print("true conflicts by folder: " + by_folder([(p, "conflict") for p in conflicts]))
        return 1 if conflicts and a.on_conflict == "stop" else 0
    if conflicts and a.on_conflict == "stop":
        print(f"records_snapshot refused: {len(conflicts)} true conflict(s) - origin holds a version of a file that main's history never had "
              f"(--on-conflict stop; main ahead {len(ahead)} would have applied); by folder: " + by_folder([(p, 'conflict') for p in conflicts]))
        return 1
    if not apply:
        print("records_snapshot: nothing to land - local main adds or changes no file origin lacks"
              + (f" (skipped: {', '.join(f'{k} {v}' for k, v in sorted(skipped.items()))})" if skipped else ""))
        return 0
    patterns = read_patterns(root)
    scratch = Path(tempfile.mkdtemp(prefix="records-snapshot-"))
    work = scratch / "wt"
    created = False
    try:
        git(root, "worktree", "add", "-q", "-b", branch, str(work), base_sha)
        created = True
        names = "\0".join(p for p, _s in apply) + "\0"
        git(work, "checkout", "main", "--pathspec-from-file=-", "--pathspec-file-nul", input=names)
        staged = git(work, "diff", "--cached", "--name-only", "-z", text=False).split(b"\0")
        if len([s for s in staged if s]) != len(apply):
            raise Refusal(f"staged {len([s for s in staged if s])} paths, planned {len(apply)}; nothing was committed")
        counts = Counter(s for _p, s in apply)
        folders = by_folder(apply)
        gate, landing_ok = pick_gate(work, root, a.gate)
        if gate is not None:
            blocked = run_gate(gate, "check", "--staged", "--root", str(work))
            if blocked.returncode == 1:
                lines = [l for l in blocked.stdout.splitlines() if l.startswith("BLOCKED")]
                print(f"records_snapshot refused: the gate blocks {len(lines)} staged finding(s); nothing was committed")
                for line in lines[:20]:
                    print("  " + line)
                raise Refusal("the gate blocked the commit")
        msg = (f"chore(records): land local main's records snapshot (A {counts['A']}, M {counts['M']})\n\n"
               f"Copied from local main onto the origin tip by records_snapshot.py; nothing was deleted.\n"
               f"By top folder: {folders}.\n"
               f"{numbers_line(apply, skipped, ahead, conflicts, a.on_conflict, '')}\n")
        git(work, "commit", "-q", "-m", msg)
        parent_ok = git(work, "rev-parse", "HEAD^").strip() == base_sha
        scan = scan_branch(root, branch, a.base, patterns) if patterns else None
        landing = None
        if gate is not None and landing_ok:
            landing = run_gate(gate, "check", "--base", a.base, "--landing", "--root", str(work))
    except Refusal:
        if created:
            git(root, "worktree", "remove", "--force", str(work), ok=(0, 128))
            git(root, "branch", "-D", branch, ok=(0, 1))
        shutil.rmtree(scratch, True)
        raise
    git(root, "worktree", "remove", "--force", str(work), ok=(0, 128))
    git(root, "worktree", "prune")
    shutil.rmtree(scratch, True)
    print(f"records_snapshot: branch {branch} on {a.base} {base_sha[:8]}; parent is the base tip: {'yes' if parent_ok else 'NO'}; never pushed, main untouched")
    print(f"files: A {counts['A']}, M {counts['M']} | by folder: {folders}")
    print(numbers_line(apply, skipped, ahead, conflicts, a.on_conflict, ""))
    clean = True
    if scan is None:
        print("denylist scan: NOT RUN - no privacy denylist found at .git/privacy-denylist.txt")
        clean = False
    else:
        print(f"denylist scan of the branch tree ({scan['files']} files): files matching {scan['matching']}, file names {scan['names']}, "
              f"commit messages and authors {scan['commits']} (images in tree {scan['images']}, not read)")
        clean = scan["matching"] == 0 and scan["names"] == 0 and scan["commits"] == 0
    if landing is None:
        print("landing check: NOT RUN - " + ("no gate script found" if gate is None else "the gate has no --landing form (land lint_gate landing first)"))
        clean = False
    else:
        tail = [l for l in landing.stdout.splitlines() if l.startswith("lint-gate:")][-1:] or [f"exit {landing.returncode}"]
        print(f"landing check: {'ok' if landing.returncode == 0 else 'FAILED'} (exit {landing.returncode}) {tail[0][:200]}")
        for line in [l for l in landing.stdout.splitlines() if l.startswith("BLOCKED")][:20]:
            print("  " + line)
        clean = clean and landing.returncode == 0
    return 0 if clean and parent_ok else 1


def cmd_converge(a, root: Path) -> int:
    base_sha = preflight(root, a.base)
    excludes = tuple(a.exclude) if a.exclude else DEFAULT_EXCLUDES
    main, origin = tree(root, "main"), tree(root, a.base)
    differ = [(p, "differs") for p, v in main.items() if not excluded(p, excludes) and origin.get(p) != v]
    if differ:
        print(f"records_snapshot converge refused: {len(differ)} tracked file(s) of local main outside the excluded paths differ from "
              f"{a.base}; by folder: {by_folder(differ)}")
        return 1
    old = git(root, "rev-parse", "main").strip()
    if old == base_sha:
        print("records_snapshot converge: main already is the base")
        return 0
    held = sum(1 for p, v in main.items() if excluded(p, excludes) and origin.get(p) != v)
    if a.dry_run:
        print(f"records_snapshot converge (dry run): would move main from {old[:8]} to {base_sha[:8]}; {held} excluded tracked file(s) would stay as "
              f"uncommitted differences; nothing changed")
        return 0
    backup = "refs/backup/main-before-converge-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    git(root, "update-ref", backup, old)
    git(root, "update-ref", "refs/heads/main", base_sha, old)
    git(root, "reset", "-q")                                   # mixed: the index follows the new main, the working tree is not touched
    differing = len([l for l in git(root, "diff", "--name-only").splitlines() if l])
    print(f"records_snapshot converge: main moved from {old[:8]} to {base_sha[:8]} ({a.base}); index reset, working tree untouched; "
          f"the old tip is kept as {backup}")
    print(f"tracked paths that now differ from the index: {differing} (the uncommitted work of other seats and of the excluded paths; "
          f"{held} of them were commits of local main outside the base)")
    return 0


def main(argv=None) -> int:
    common = argparse.ArgumentParser(add_help=False)          # the same options before or after the subcommand
    common.add_argument("--root", default=argparse.SUPPRESS, help="the live checkout (default: the one holding this tool)")
    common.add_argument("--base", default=argparse.SUPPRESS, help="the line to land on (default origin/main)")
    common.add_argument("--exclude", action="append", default=argparse.SUPPRESS,
                        help="a path to leave out (repeatable; replaces the defaults _tools_ and _activities_)")
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter, parents=[common])
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("snapshot", parents=[common])
    s.add_argument("--branch", default="")
    s.add_argument("--on-conflict", choices=("main", "origin", "stop"), default="stop",
                   help="a TRUE conflict - origin holds a version of the file that main's history never had (default stop)")
    s.add_argument("--gate", default="", help="the lint gate script to use (default: the branch's own, else the live checkout's)")
    s.add_argument("--dry-run", action="store_true", help="print what would land (counts by folder); create no branch or worktree")
    c = sub.add_parser("converge", parents=[common])
    c.add_argument("--dry-run", action="store_true")
    a = p.parse_args(argv)
    for name, value in (("root", str(HERE.parent.parent)), ("base", "origin/main"), ("exclude", [])):
        if not hasattr(a, name):                              # not given before or after the subcommand
            setattr(a, name, value)
    root = Path(a.root).resolve()
    try:
        return {"snapshot": cmd_snapshot, "converge": cmd_converge}[a.cmd](a, root)
    except Refusal as exc:
        if exc.code == 1:
            print(f"records_snapshot refused: {exc}")
        else:
            print(f"records_snapshot: {exc}", file=sys.stderr)
        return exc.code


if __name__ == "__main__":
    sys.exit(main())
