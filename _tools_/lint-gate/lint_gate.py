#!/usr/bin/env python3
"""lint-gate: stop new oversized or misshapen documents and show size growth cheaply.

Subcommands: check, install, watch, record-check, stub-index, redact. The privacy rule keeps identifiers listed in
.git/privacy-denylist.txt out of staged lines and file names; it never prints a matched text. It runs the reflection convention linter
(~/dtadpole/reflection, or LINT_GATE_REFLECTION / --reflection) with the right --root and --vocabulary and
judges only what the commit adds or changes; legacy findings never block. Standard library only; the word counter
is the linter's own, loaded from the reflection checkout. Exit 0 ok, 1 blocked or limit reached, 2 cannot run.
"""
from __future__ import annotations

import argparse
import fnmatch
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

VERSION = "1.7.0"
GATE_RULES = ("document-concision", "entry-points", "type-instance-trees")
PRIVACY_RULE, PRIVACY_FILE, PRIVACY_CACHE = "privacy", "privacy-denylist.txt", "lint-gate-privacy-cache.json"
# The playbook cards (OD-20261123-15): `_tools_/playbook-check/playbook_check.py changed` runs on the changed _activities_/<a>/INDEX.md pages.
# Only a card that lost its shape or passes the card word cap blocks; every other finding (staleness, an unresolved path, too many rules...)
# is a warning with counts; an INDEX that is not a card is skipped; a repository without the tool, or a tool that cannot run, is silent or a warning.
PLAYBOOK_RULE, PLAYBOOK_TOOL, PLAYBOOK_BLOCKING = "playbook-card", "_tools_/playbook-check/playbook_check.py", ("card-shape-lost", "card-too-long")
PLAYBOOK_TIMEOUT = 60
EXPECT = re.compile(r"^#\s*expect-min\s+(\d+)\s*$", re.IGNORECASE)
MARKER = re.compile(r"^#\s*marker:\s*(.*\S)\s*$", re.IGNORECASE)
EXPECT_MESSAGE = "denylist does not match as expected (regex versus fixed string?)"
CENSUS_FILE, CENSUS_MIN = "privacy-census.json", 10
HUNK = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")
HARD_WORDS, SOFT_WORDS, RECORD_LIMIT = 500, 300, 480
STAGED_TIMEOUT, FULL_TIMEOUT = 25, 600          # seconds; the staged cap keeps the hook under 30 s
BASELINE_REL = "_tools_/state/lint-baseline.json"
HOOKS_REL = "_tools_/lint-gate/hooks"
HOOK_NAMES = ("pre-commit", "pre-merge-commit")
EXEMPT_REL = "_tools_/lint-gate/exempt.txt"
TOP_KEPT, GROWTH, MIN_GROWTH_WORDS, GROWTH_FILE_CAP = 50, 0.20, 20, 400
LIST_CAP = 50           # new, exempt and new-error paths kept in the summary and printed by watch (--list prints them all)
TAG = re.compile(r"\[([a-z][a-z-]*)\]\s*$")
NOT_NAME = re.compile(r" not (.+) \[type-instance-trees\]\s*$")


class GateError(Exception):
    """The gate cannot run (exit 2)."""


# --- helpers -----------------------------------------------------------------------------------------------

def git(root: Path, *args: str, check: bool = True) -> bytes:
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}   # a hook's GIT_DIR must not redirect us
    proc = subprocess.run(["git", "-C", str(root), *args], capture_output=True, env=env)
    if check and proc.returncode:
        raise GateError(f"git {' '.join(args[:2])}: {proc.stderr.decode(errors='replace').strip()}")
    return proc.stdout if proc.returncode == 0 else b""


def repo_top(root: Path) -> Path:
    return Path(git(root, "rev-parse", "--show-toplevel").decode().strip())


def reflection_paths(args) -> dict[str, Path]:
    base = Path(args.reflection or os.environ.get("LINT_GATE_REFLECTION") or "~/dtadpole/reflection").expanduser()
    found = {
        "linter": base / "_tools_/convention-linter/lint-conventions.py",
        "vocabulary": base / "_conventions_/core-conventions/type-vocabulary.md",
        "counter": base / "_tools_/document-word-budget/word-budget.py",
    }
    missing = [str(p) for p in found.values() if not p.is_file()]
    if missing:
        raise GateError(f"reflection checkout incomplete (set --reflection or LINT_GATE_REFLECTION): {missing[0]}")
    return found


def run_linter(paths: dict[str, Path], root: Path, extra: list[str], timeout: int, staged: bool) -> dict:
    cmd = [sys.executable, "-B", str(paths["linter"]), "--root", str(root), "--vocabulary", str(paths["vocabulary"]),
           "--json", *extra]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    if not staged:
        env.pop("GIT_INDEX_FILE", None)   # judge the working tree, not an index a caller left behind
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, env=env, cwd=root, timeout=timeout)
    except subprocess.TimeoutExpired:
        raise GateError(f"the linter did not finish in {timeout}s")
    try:
        report = json.loads(proc.stdout)
    except ValueError:
        raise GateError(f"the linter gave no JSON (exit {proc.returncode}): {proc.stderr.strip()[-300:]}")
    return drop_ignored(root, report)


def ignored_among(top: Path, names) -> set[str]:
    """The names git ignores (a path under an ignored folder counts), by one `git check-ignore`; a tracked path is never ignored. An error from git
    ignores nothing: the gate then judges as it did before."""
    wanted = sorted({n for n in names if n and not n.startswith("/") and ".." not in n.split("/")})
    if not wanted:
        return set()
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_") or k == "GIT_INDEX_FILE"}
    try:
        out = subprocess.run(["git", "-C", str(top), "check-ignore", "-z", "--stdin"], input=("\0".join(wanted) + "\0").encode("utf-8", "surrogateescape"),
                             capture_output=True, env=env, timeout=120)
    except (OSError, subprocess.SubprocessError):
        return set()
    if out.returncode not in (0, 1):
        return set()
    return {n for n in out.stdout.decode("utf-8", "surrogateescape").split("\0") if n}


def drop_ignored(top: Path, report: dict) -> dict:
    """The linter walks the working tree, so a folder `.gitignore` excludes (the queue's live-only completed/ is one) showed up as a content folder
    with no entry point and its documents were counted. Findings and document rows about ignored paths are dropped; everything else is unchanged."""
    errors = report.get("errors", [])
    budgets = report.get("document_budgets") or {}
    rows = budgets.get("documents") or []
    ignored = ignored_among(top, {path_of(e) for e in errors} | {r["path"] for r in rows if isinstance(r, dict) and r.get("path")})
    if not ignored:
        return report
    out = dict(report)
    out["errors"] = [e for e in errors if path_of(e) not in ignored]
    if rows:
        out["document_budgets"] = dict(budgets, documents=[r for r in rows if r.get("path") not in ignored])
    return out


def load_counter(paths: dict[str, Path]):
    spec = importlib.util.spec_from_file_location("lint_gate_word_budget", paths["counter"])
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except ImportError as exc:
        raise GateError(f"the word counter needs a module this python lacks ({exc}); use the python3 that runs the linter")
    return module


def tag_of(finding: str) -> str | None:
    m = TAG.search(finding)
    return m.group(1) if m else None


def path_of(finding: str) -> str:
    return finding.split(": ", 1)[0]


def exemptions(top: Path) -> tuple[list[str], list[str]]:
    """(document globs, folder globs) from exempt.txt; a line `folder GLOB` exempts folders from [entry-points]."""
    f = top / EXEMPT_REL
    docs, folders = [], []
    if f.is_file():
        for ln in f.read_text(encoding="utf-8").splitlines():
            ln = ln.strip()
            if not ln or ln.startswith("#"):
                continue
            if ln.startswith("folder "):
                folders.append(ln[len("folder "):].strip())
            else:
                docs.append(ln)
    return docs, folders


def is_exempt(path: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatchcase(path, p) for p in patterns)


class BaseTree:
    """The files and folders a ref holds; empty when the ref does not resolve (an unborn branch)."""

    def __init__(self, root: Path, ref: str, staged: bool = False):
        self.root = root
        self.staged = staged
        self.files: set[str] = set()
        self.dirs: set[str] = set()
        out = git(root, "ls-tree", "-r", "--name-only", "-z", ref, check=False)
        for name in out.decode("utf-8", errors="surrogateescape").split("\0"):
            if not name:
                continue
            self.files.add(name)
            parts = name.split("/")
            for i in range(1, len(parts)):
                self.dirs.add("/".join(parts[:i]))

    def in_index(self, path: str) -> bool:
        """True when the path is staged or tracked. The linter walks the working tree, so an untracked file it
        flags is no part of a commit that does not stage it."""
        env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_") or k == "GIT_INDEX_FILE"}
        out = subprocess.run(["git", "-C", str(self.root), "ls-files", "--cached", "--", path], capture_output=True,
                             env=env)
        return bool(out.stdout.strip())

    def ignored(self, path: str) -> bool:
        """True when git ignores the path: it can never be committed, so it is no commit's defect."""
        env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
        return subprocess.run(["git", "-C", str(self.root), "check-ignore", "-q", "--", path], capture_output=True,
                              env=env).returncode == 0


def is_new(finding: str, base: BaseTree) -> bool:
    """A gate finding is new unless the base tree already had the same defect. A document-concision error is new or
    changed by the linter's own definition; the two structural rules are judged against the base tree here."""
    tag = tag_of(finding)
    folder = path_of(finding)
    if tag == "entry-points" and "no entry point" in finding:
        return folder not in base.dirs or f"{folder}/INDEX.md" in base.files
    if tag == "type-instance-trees":
        m = NOT_NAME.search(finding)
        if m:
            offender = f"{folder}/{m.group(1)}"
            if offender in base.files or offender in base.dirs or base.ignored(offender):
                return False
            return not base.staged or base.in_index(offender)
    return True


def classify(errors: list[str], rules, base: BaseTree, patterns: list[str], folders: list[str] = (), redacted=frozenset()):
    blocking, legacy, exempt, other = [], [], [], 0
    for f in errors:
        tag = tag_of(f)
        if tag not in rules:
            other += 1
        elif tag == "document-concision" and (is_exempt(path_of(f), patterns) or path_of(f) in redacted):
            exempt.append(f)
        elif tag == "entry-points" and "no entry point" in f and is_exempt(path_of(f), list(folders)):
            exempt.append(f)
        elif is_new(f, base):
            blocking.append(f)
        else:
            legacy.append(f)
    return blocking, legacy, exempt, other


def short(finding: str) -> str:
    tag = tag_of(finding) or "?"
    text = TAG.sub("", finding).rstrip()
    if tag == "document-concision":
        text = text.split(" Remove repetition", 1)[0].rstrip()
    return f"[{tag}] {text}"


# --- exempt.txt only shrinks ---------------------------------------------------------------------------------

def exempt_entries(text: str) -> list[str]:
    return [ln.strip() for ln in text.splitlines() if ln.strip() and not ln.lstrip().startswith("#")]


def exempt_additions(top: Path, base_ref: str, staged: bool) -> list[str]:
    """Entries in the exempt list that the base does not have. The list may only shrink: a new exemption is a new way
    round the word budget, so any entry added (or reworded, which is an add and a remove) blocks. A base without the file
    is the file's introduction and is let through."""
    base = git(top, "show", f"{base_ref}:{EXEMPT_REL}", check=False)
    if not base.strip():
        return []
    try:
        now = staged_git(top, "show", f":{EXEMPT_REL}") if staged else (top / EXEMPT_REL).read_bytes()
    except (GateError, OSError):
        return []                                   # not in the index or the tree: nothing was added
    before = set(exempt_entries(base.decode("utf-8", errors="replace")))
    return [e for e in exempt_entries(now.decode("utf-8", errors="replace")) if e not in before]


# --- privacy -----------------------------------------------------------------------------------------------
# A local denylist (.git/privacy-denylist.txt, untracked, one regular expression per line, # comments, matched without
# regard to case) names identifiers that must not enter this public repository. Nothing in this section ever prints,
# logs or returns a matched text or a pattern: findings carry a path, a line number and the pattern's position.

def denylist_path(top: Path) -> Path:
    out = git(top, "rev-parse", "--git-common-dir", check=False).decode().strip()
    base = Path(out) if out else Path(".git")
    return (base if base.is_absolute() else top / base) / PRIVACY_FILE


def load_denylist(top: Path):
    """(numbered patterns, warnings, expectations, markers). Every entry is a regular expression, matched without regard
    to case. Annotation lines right before a pattern belong to it: `# expect-min N` (it must match at least N tracked
    files at HEAD) and `# marker: TEXT` (what `redact` replaces a match with). A missing or empty denylist is a warning,
    never a block."""
    path = denylist_path(top)
    if not path.is_file():
        return [], ["privacy denylist not found at .git/privacy-denylist.txt; the privacy rule is skipped"], {}, {}
    patterns, warnings, expect, markers, n, pending = [], [], {}, {}, 0, {}
    def dropped():
        for kind, (_, lineno) in pending.items():
            warnings.append(f"denylist line {lineno}: {kind} is not immediately followed by a pattern and is ignored")
        pending.clear()
    for lineno, raw in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        line = raw.strip()
        e, m = EXPECT.match(line), MARKER.match(line)
        if e or m:
            kind, value = ("expect-min", int(e.group(1))) if e else ("marker", m.group(1))
            if kind in pending:
                warnings.append(f"denylist line {pending[kind][1]}: {kind} is not immediately followed by a pattern and is ignored")
            pending[kind] = (value, lineno)
            continue
        if not line or line.startswith("#"):
            dropped()
            continue
        n += 1
        try:
            patterns.append((n, re.compile(line, re.IGNORECASE)))
            if "expect-min" in pending:
                expect[n] = pending["expect-min"][0]
            if "marker" in pending:
                markers[n] = pending["marker"][0]
        except re.error:
            warnings.append(f"denylist line {lineno} is not a valid regular expression and is ignored")
        pending.clear()
    dropped()
    if not patterns:
        warnings.append("privacy denylist holds no usable pattern; the privacy rule is skipped")
    return patterns, warnings, expect, markers


def safe_path(path: str, patterns) -> str:
    """The path with any matched part replaced, so a file name that matches is not echoed."""
    for _, pattern in patterns:
        path = pattern.sub("[redacted]", path)
    return path


def staged_git(top: Path, *args: str) -> bytes:
    """git against the staged index: GIT_INDEX_FILE (a hook's or commit -a's temporary index) is kept."""
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_") or k == "GIT_INDEX_FILE"}
    proc = subprocess.run(["git", "-C", str(top), "-c", "core.quotepath=off", *args], capture_output=True, env=env)
    if proc.returncode:
        raise GateError(f"git {args[0]} failed while reading the staged changes")
    return proc.stdout


def unquote(name: str) -> str:
    if name.startswith('"') and name.endswith('"'):
        return name[1:-1].encode("latin-1", "backslashreplace").decode("unicode_escape")
    return name


def added_lines(diff: str):
    """(path, line number, text) of every line a unified -U0 diff adds. Hunk counts say where a hunk ends, so a removed
    line that looks like a file header is never mistaken for one."""
    path, old_left, new_left, lineno = None, 0, 0, 0
    for line in diff.split("\n"):
        if old_left or new_left:
            if line.startswith("-"):
                old_left -= 1
            elif line.startswith("+"):
                yield path, lineno, line[1:]
                lineno += 1
                new_left -= 1
            continue
        if line.startswith("+++ "):
            name = line[4:].split("\t")[0]
            path = None if name == "/dev/null" else unquote(name)[2:]
        elif line.startswith("@@"):
            m = HUNK.match(line)
            if m:
                old_left = int(m.group(2) if m.group(2) is not None else 1)
                new_left = int(m.group(4) if m.group(4) is not None else 1)
                lineno = int(m.group(3))


def head_match_counts(top: Path, patterns) -> dict[int, int] | None:
    """For each pattern, how many tracked files at HEAD it matches. Results are cached per blob in the git directory
    (indices and blob ids only, no pattern text), keyed by the denylist's hash, so a commit only scans its new blobs."""
    if not git(top, "rev-parse", "--verify", "--quiet", "HEAD^{commit}", check=False).strip():
        return None
    entries = []
    for record in git(top, "ls-tree", "-r", "-z", "HEAD").decode("utf-8", errors="surrogateescape").split("\0"):
        if record:
            meta = record.split("\t", 1)[0].split()
            if meta[1] == "blob" and meta[0] != "120000":
                entries.append(meta[2])
    key = hashlib.sha256(denylist_path(top).read_bytes()).hexdigest()
    cache_file = denylist_path(top).parent / PRIVACY_CACHE
    matched: dict = {}
    try:
        stored = json.loads(cache_file.read_text(encoding="utf-8"))
        if stored.get("key") == key:
            matched = stored.get("blobs", {})
    except (OSError, ValueError):
        pass
    missing = sorted({sha for sha in entries if sha not in matched})
    for i in range(0, len(missing), 1500):
        chunk = missing[i:i + 1500]
        data = blob_bytes(top, chunk)
        for sha in chunk:
            raw = data.get(sha, b"")
            if b"\0" in raw[:8000]:
                matched[sha] = []
                continue
            text = raw.decode("utf-8", errors="replace")
            matched[sha] = [n for n, pattern in patterns if pattern.search(text)]
    if missing:
        try:
            tmp = cache_file.with_suffix(".tmp")
            tmp.write_text(json.dumps({"key": key, "blobs": {sha: matched[sha] for sha in set(entries)}}), encoding="utf-8")
            os.replace(tmp, cache_file)
        except OSError:
            pass
    counts = {n: 0 for n, _ in patterns}
    for sha in entries:
        for n in matched[sha]:
            counts[n] += 1
    return counts


def pattern_hash(pattern) -> str:
    """A short hash of a pattern's text: the census is keyed by it, so editing another line of the denylist, or moving a
    pattern, keeps its record, and a changed pattern starts afresh. The text itself is never stored."""
    return hashlib.sha256(pattern.pattern.encode("utf-8")).hexdigest()[:16]


def census_path(top: Path) -> Path:
    return denylist_path(top).parent / CENSUS_FILE


def load_census(top: Path) -> dict[str, int]:
    """Files each pattern matched at HEAD in the last `watch --privacy`, by pattern hash; {} when there is none."""
    try:
        data = json.loads(census_path(top).read_text(encoding="utf-8"))
        return {h: int(v["files"]) for h, v in data.get("patterns", {}).items()}
    except (OSError, ValueError, KeyError, TypeError):
        return {}


def write_census(top: Path, patterns, files: dict[int, int], lines: dict[int, int], head: str) -> None:
    record = {"version": 1, "head": head, "at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
              "patterns": {pattern_hash(p): {"files": files.get(n, 0), "lines": lines.get(n, 0)} for n, p in patterns}}
    path = census_path(top)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(record, indent=1), encoding="utf-8")
    os.replace(tmp, path)


def guard_failures(patterns, expect: dict[int, int], counts: dict[int, int] | None, census: dict[str, int]) -> list[str]:
    """Where the denylist stops matching what it should. With a census for a pattern, a decrease is fine (a redaction
    lowers counts) and only a drop to zero from more than CENSUS_MIN files fails; without one (a fresh clone, or a pattern
    just changed) `# expect-min N` applies, so a regex written as a fixed string that matches nothing fails loudly."""
    if counts is None:
        return []
    out = []
    for n, pattern in patterns:
        have, seen = counts.get(n, 0), census.get(pattern_hash(pattern))
        if seen is not None:
            if have == 0 and seen > CENSUS_MIN:
                out.append(f"pattern {n} matches 0 tracked file(s) at HEAD, but the last census saw {seen}; if a redaction "
                           f"landed, record it with `watch --privacy --accept`")
        elif n in expect and have < expect[n]:
            out.append(f"pattern {n} matches {have} tracked file(s) at HEAD, expected at least {expect[n]} (no census yet)")
    return out


def added_runs(diff: str):
    """(path, first line number, text) for each run of consecutive added lines, so a match wrapped over a line break
    inside added text is found as one."""
    path, first, last, buffer = None, 0, 0, []
    for p, lineno, text in added_lines(diff):
        if buffer and (p != path or lineno != last + 1):
            yield path, first, "\n".join(buffer)
            buffer = []
        if not buffer:
            path, first = p, lineno
        buffer.append(text)
        last = lineno
    if buffer:
        yield path, first, "\n".join(buffer)


def privacy_scan_staged(top: Path, staged: bool = True) -> dict:
    patterns, warnings, expect, _ = load_denylist(top)
    result = {"hits": [], "warnings": warnings, "patterns": len(patterns), "lines": 0, "failures": []}
    if not patterns:
        return result
    census = load_census(top)
    if expect or census:
        result["failures"] = guard_failures(patterns, expect, head_match_counts(top, patterns), census)
    if not staged:
        return result
    names = staged_git(top, "diff", "--cached", "--name-only", "-z", "-M", "--diff-filter=ACMR").decode(
        "utf-8", errors="surrogateescape").split("\0")
    for name in filter(None, names):
        for n, pattern in patterns:
            if pattern.search(name):
                result["hits"].append(("name", safe_path(name, patterns), 0, n))
    diff = staged_git(top, "diff", "--cached", "-U0", "--no-color", "--no-ext-diff", "-M", "--diff-filter=ACMR").decode(
        "utf-8", errors="replace")
    for path, first, run in added_runs(diff):
        result["lines"] += run.count("\n") + 1
        for n, pattern in patterns:
            seen = set()
            for m in pattern.finditer(run):               # a name wrapped over added lines is one match
                line = first + run.count("\n", 0, m.start())
                if line not in seen:
                    seen.add(line)
                    result["hits"].append(("line", safe_path(path or "?", patterns), line, n))
    return result


def playbook_findings(top: Path, staged: bool, base: str) -> tuple[list[str], list[str]]:
    """(blocking lines, warning lines) from playbook_check over the changed activity INDEX pages. Counts and codes only: nothing from a card."""
    tool = top / PLAYBOOK_TOOL
    if not tool.is_file():
        return [], []
    command = [sys.executable, "-B", str(tool), "--root", str(top), "--format", "json", "changed"] + (["--staged"] if staged else ["--base", base])
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_") or k == "GIT_INDEX_FILE" and staged}
    try:
        out = subprocess.run(command, capture_output=True, text=True, timeout=PLAYBOOK_TIMEOUT, env=env)
        data = json.loads(out.stdout)
    except (OSError, subprocess.SubprocessError, ValueError):
        return [], [f"{PLAYBOOK_RULE}: the card check could not run; nothing was blocked"]
    block, other = [], {}
    for card in data.get("cards", []):
        path = f"_activities_/{card.get('activity')}/INDEX.md"
        for code in sorted(card.get("errors", {})):
            if code in PLAYBOOK_BLOCKING:
                block.append(f"[{PLAYBOOK_RULE}] {path}: {code}" + (" (a card is 300 words or fewer)" if code == "card-too-long" else
                                                                  " (it was a card and no longer has its Route and Rules sections)"))
            else:
                other[code] = other.get(code, 0) + card["errors"][code]
        for code, n in card.get("warnings", {}).items():
            other["warn " + code] = other.get("warn " + code, 0) + n
    warn = [f"{PLAYBOOK_RULE}: card finding(s) that do not block - " + ", ".join(f"{k} {v}" for k, v in sorted(other.items()))] if other else []
    return block, warn


def print_privacy_hits(hits: list, limit: int = 40) -> None:
    for kind, path, lineno, n in hits[:limit]:
        where = f"{path}:{lineno}" if kind == "line" else path
        what = "an added line matches" if kind == "line" else "the file name matches"
        print(f"BLOCKED [privacy] {where}: {what} denylist pattern {n}")
    if len(hits) > limit:
        print(f"BLOCKED [privacy] and {len(hits) - limit} more")


def cmd_privacy_census(a) -> int:
    """watch --privacy: files and lines per top folder for each pattern, counts and paths only."""
    top = repo_top(Path(a.root).resolve())
    patterns, warnings, expect, _ = load_denylist(top)
    if not patterns:
        raise GateError("; ".join(warnings))
    if a.worktree:
        names = [n for n in git(top, "ls-files", "-z", "--cached", "--others", "--exclude-standard").decode(
            "utf-8", errors="surrogateescape").split("\0") if n and (top / n).is_file() and not (top / n).is_symlink()]
        read = lambda n: (top / n).read_bytes()
        source = "working tree"
    else:
        listing = git(top, "ls-tree", "-r", "-z", "HEAD").decode("utf-8", errors="surrogateescape").split("\0")
        names = [r.split("\t", 1)[1] for r in listing if r and r.split()[1] == "blob" and not r.startswith("120000")]
        blobs = blob_bytes(top, [f"HEAD:{n}" for n in names])
        read = lambda n: blobs.get(f"HEAD:{n}", b"")
        source = "HEAD " + git(top, "rev-parse", "--short", "HEAD").decode().strip()
    stats = {n: {"files": {}, "lines": {}, "names": 0, "per_file": []} for n, _ in patterns}
    any_files = set()
    for name in names:
        folder = name.split("/", 1)[0] if "/" in name else "(root)"
        for n, pattern in patterns:
            if pattern.search(name):
                stats[n]["names"] += 1
        data = read(name)
        if b"\0" in data[:8000]:
            continue
        text = data.decode("utf-8", errors="replace")
        for n, pattern in patterns:
            if not pattern.search(text):
                continue
            count = touched_lines(text, pattern)
            stats[n]["files"][folder] = stats[n]["files"].get(folder, 0) + 1
            stats[n]["lines"][folder] = stats[n]["lines"].get(folder, 0) + count
            stats[n]["per_file"].append((count, safe_path(name, patterns)))
            any_files.add(name)
    summary = {"source": source, "patterns": len(patterns), "files_matching_any": len(any_files), "per_pattern": {}}
    for n, st in stats.items():
        summary["per_pattern"][str(n)] = {
            "files": sum(st["files"].values()), "lines": sum(st["lines"].values()), "file_names": st["names"],
            "by_top_folder": {f: {"files": st["files"][f], "lines": st["lines"][f]} for f in sorted(st["files"], key=lambda f: -st["files"][f])},
            "largest_files": [{"path": p, "lines": c} for c, p in sorted(st["per_file"], reverse=True)[:10]],
        }
    counts = {int(n): info["files"] for n, info in summary["per_pattern"].items()} if not a.worktree else head_match_counts(top, patterns)
    failures = guard_failures(patterns, expect, counts, load_census(top))
    accepted = list(failures) if a.accept else []
    if a.accept:
        failures = []
    recorded = False
    if not a.worktree and not failures:               # only a census taken at HEAD is recorded, and never over a failure
        write_census(top, patterns, counts, {int(n): i["lines"] for n, i in summary["per_pattern"].items()},
                     git(top, "rev-parse", "--short", "HEAD").decode().strip())
        recorded = True
    summary["expect_failures"] = failures
    summary["census_recorded"] = recorded
    if a.format == "json":
        print(json.dumps(summary, indent=1))
        return 1 if failures else 0
    print(f"privacy census of {source}: {len(patterns)} pattern(s) from .git/privacy-denylist.txt; counts and paths only, "
          f"no matched text; {len(any_files)} file(s) match any pattern")
    for w in warnings:
        print(f"warning: {w}")
    for n, info in summary["per_pattern"].items():
        print(f"pattern {n}: {info['files']} files, {info['lines']} lines, {info['file_names']} file name(s)")
        for folder, c in info["by_top_folder"].items():
            print(f"  {folder:<20}{c['files']:>6} files{c['lines']:>8} lines")
        for f in info["largest_files"][:5]:
            print(f"  largest: {f['path']} ({f['lines']} lines)")
    if accepted:
        print(f"lint-gate: accepted {len(accepted)} dropped pattern(s); the census now records their new counts")
    if recorded:
        print("census recorded in .git/privacy-census.json (counts and pattern hashes only)")
    if failures:
        print(f"lint-gate: {EXPECT_MESSAGE}")
        for f in failures:
            print(f"  {f}")
        return 1
    return 0


def blob_bytes(top: Path, specs: list[str]) -> dict[str, bytes]:
    """Contents of the named blobs in one git call."""
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    proc = subprocess.run(["git", "-C", str(top), "cat-file", "--batch"], capture_output=True, env=env,
                          input="".join(f"{spec}\n" for spec in specs).encode("utf-8", errors="surrogateescape"))
    data, pos, out = proc.stdout, 0, {}
    for spec in specs:
        end = data.find(b"\n", pos)
        header = data[pos:end].split()
        if len(header) == 3 and header[1] == b"blob":
            size = int(header[2])
            out[spec] = data[end + 1:end + 1 + size]
            pos = end + 2 + size
        else:
            pos = end + 1
    return out


# --- redact ------------------------------------------------------------------------------------------------
# Rewrites the files it is given so no denylist pattern matches: each match becomes the pattern's `# marker:` text, the
# same text for every match, line by line, so line endings, the final newline and indentation stay as they were. Dry run
# by default. Nothing here prints a matched string, a pattern or a marker.

PROTECTED = (("_records_",), ("_queue_", "done"))
SEPARATORS = re.compile(r"(\r\n|\n|\r)")
VERSION_LINE = re.compile(r"^(version:\s*)(['\"]?)(\d+)\.(\d+)\.(\d+)(['\"]?)(\s*)$")
MODIFIED_LINE = re.compile(r"^(modified:\s*)(['\"]?)(.*?)(['\"]?)(\s*)$")


def is_binary(data: bytes) -> bool:
    return b"\0" in data[:8000]


def under(rel: tuple, prefix: tuple) -> bool:
    return rel[:len(prefix)] == prefix


def fit_marker(match: str, marker: str) -> str:
    """The marker laid over the match's words. The whitespace between the match's words, line breaks and indentation
    included, is kept exactly, so a wrapped match stays wrapped: the marker's words fill the match's word slots in order
    (extra words join the last slot, missing ones leave an empty slot)."""
    if not match:
        return ""
    pieces = re.split(r"(\s+)", match)
    slots = [i for i in range(0, len(pieces), 2) if pieces[i]]
    words = marker.split()
    if not slots:
        return marker
    for k, i in enumerate(slots):
        pieces[i] = (" ".join(words[k:]) if k == len(slots) - 1 else (words[k] if k < len(words) else ""))
    return "".join(pieces)


def redact_text(text: str, patterns, markers) -> tuple[str, dict[int, int]]:
    """(new text, matches per pattern counted on the original text). A match may span line breaks (a pattern with \\s+):
    its replacement keeps the whitespace between the words, so line count, wrapping and indentation do not change."""
    counts = {n: sum(1 for _ in pattern.finditer(text)) for n, pattern in patterns}
    for n, pattern in patterns:
        if n in markers:
            marker = markers[n]
            text = pattern.sub(lambda m, k=marker: fit_marker(m.group(0), k), text)
    return text, counts


def still_matches(text: str, patterns) -> bool:
    return any(pattern.search(text) for _, pattern in patterns)


def touched_lines(text: str, pattern) -> int:
    """How many lines carry a match, a wrapped match counting each line it covers."""
    lines = set()
    for m in pattern.finditer(text):
        lines.update(range(text.count("\n", 0, m.start()), text.count("\n", 0, m.end()) + 1))
    return len(lines)


def bump_front(text: str, now: str) -> tuple[str, tuple[str, str] | None]:
    """Minor version up and modified set in the frontmatter, touching nothing else; (text, (old, new)) or (text, None)."""
    parts = SEPARATORS.split(text)
    contents = parts[0::2]
    if not contents or contents[0] != "---":
        return text, None
    end = next((i for i in range(1, len(contents)) if contents[i] in ("---", "...")), None)
    if end is None:
        return text, None
    v = next((i for i in range(1, end) if VERSION_LINE.match(contents[i])), None)
    m = next((i for i in range(1, end) if MODIFIED_LINE.match(contents[i])), None)
    if v is None or m is None:
        return text, None
    a = VERSION_LINE.match(contents[v])
    old, new = f"{a.group(3)}.{a.group(4)}.{a.group(5)}", f"{a.group(3)}.{int(a.group(4)) + 1}.0"
    contents[v] = f"{a.group(1)}{a.group(2)}{new}{a.group(6)}{a.group(7)}"
    b = MODIFIED_LINE.match(contents[m])
    contents[m] = f"{b.group(1)}{b.group(2)}{now}{b.group(4)}{b.group(5)}"
    parts[0::2] = contents
    return "".join(parts), (old, new)


def collect_files(top: Path, names: list[str], allow_records: bool, allow_outside: bool = False):
    """(files, refusals, skipped). A named file under .git, outside the repository, in the records or done queue
    (unless allowed) or binary is refused; a folder is walked and skips those, counting what it skipped. With allow_outside an
    explicit file under /tmp is accepted although it is outside the repository."""
    files, refusals, skipped = [], [], {"binary": 0, "records": 0, "other": 0}
    def rel_of(p: Path):
        try:
            return p.resolve().relative_to(top).parts
        except ValueError:
            return None
    def guarded(p: Path, explicit: bool) -> bool:
        rel = rel_of(p)
        if rel is None and allow_outside and explicit and p.is_file() and ".git" not in p.resolve().parts \
                and (p.resolve().parts[:2] == ("/", "tmp") or p.resolve().parts[:3] == ("/", "private", "tmp")):
            return True
        if rel is None or ".git" in rel:
            if explicit:
                refusals.append(f"{p}: outside the repository or under .git/"
                                + ("; --allow-outside takes only an explicit file under /tmp" if rel is None else ""))
            else:
                skipped["other"] += 1
            return False
        if not allow_records and any(under(rel, pre) for pre in PROTECTED):
            if explicit:
                refusals.append(f"{p}: immutable play records (C1); pass --allow-records to include them")
            else:
                skipped["records"] += 1
            return False
        return True
    for name in names:
        p = Path(name)
        if p.is_symlink():
            refusals.append(f"{p}: a symbolic link is not rewritten")
        elif p.is_dir():
            if not guarded(p, True):
                continue
            for cur, dirs, fnames in os.walk(p, followlinks=False):
                dirs[:] = sorted(d for d in dirs if d != ".git" and not (Path(cur) / d).is_symlink())
                for f in sorted(fnames):
                    q = Path(cur) / f
                    if q.is_symlink() or not q.is_file() or not guarded(q, False):      # sockets, pipes, links: never read
                        skipped["other"] += 1 if not q.is_file() else 0
                        continue
                    try:
                        binary = is_binary(q.read_bytes())
                    except OSError:
                        skipped["other"] += 1
                        continue
                    if binary:
                        skipped["binary"] += 1
                    else:
                        files.append(q)
        elif p.is_file():
            if not guarded(p, True):
                continue
            if is_binary(p.read_bytes()):
                refusals.append(f"{p}: a binary file is not rewritten")
            else:
                files.append(p)
        else:
            refusals.append(f"{p}: no such file or folder")
    return files, refusals, skipped


# --- redaction-only proof ----------------------------------------------------------------------------------
# `redact --verify-diff` and the narrow exemption in `check --staged` rest on one test: the changed text must EQUAL the
# deterministic substitution applied to the base text, apart from the frontmatter `version:` and `modified:` lines of a
# versioned (non-record) file. Nothing here prints a matched value, only paths, counts and line numbers.

FRONT_MOVES = re.compile(r"^(version|modified):")


def front_range(contents: list[str]) -> tuple[int, int] | None:
    if not contents or contents[0] != "---":
        return None
    end = next((i for i in range(1, len(contents)) if contents[i] in ("---", "...")), None)
    return (1, end) if end is not None else None


def neutral_front(text: str) -> str:
    parts = SEPARATORS.split(text)
    contents = parts[0::2]
    span = front_range(contents)
    if span:
        for i in range(*span):
            if FRONT_MOVES.match(contents[i]):
                contents[i] = contents[i].split(":", 1)[0] + ": <moved>"
    parts[0::2] = contents
    return "".join(parts)


def yaml_still_sane(base: str, new: str) -> bool:
    """Frontmatter lines the substitution changed keep their shape: same kind of line, no new `: ` or ` #`, same quote parity.
    (A sanity check, not a YAML parser: the tool is standard library only.)"""
    b, n = SEPARATORS.split(base)[0::2], SEPARATORS.split(new)[0::2]
    span = front_range(b)
    if not span or len(b) != len(n):
        return True if not span else False
    for i in range(*span):
        if b[i] == n[i]:
            continue
        kind = lambda line: re.match(r"^\s*(- |[\w.-]+:)", line) is not None
        if kind(b[i]) != kind(n[i]) or n[i].count(": ") > b[i].count(": ") or n[i].count(" #") > b[i].count(" #") \
                or n[i].count('"') % 2 != b[i].count('"') % 2 or n[i].count("'") % 2 != b[i].count("'") % 2:
            return False
    return True


def redaction_problems(rel: str, base: bytes, new: bytes, patterns, markers) -> tuple[list[str], bool]:
    """([problems], moved): empty problems prove the change is redaction-only; moved says version or modified moved."""
    try:
        base_text, new_text = base.decode("utf-8"), new.decode("utf-8")
    except UnicodeDecodeError:
        return ["not valid UTF-8 text"], False
    parts = tuple(rel.split("/"))
    versioned = not (under(parts, ("_records_",)) or under(parts, ("_queue_", "done")) or under(parts, ("_logs_",)))
    expected, _ = redact_text(base_text, patterns, markers)
    moved = False
    if new_text != expected:
        if versioned and neutral_front(new_text) == neutral_front(expected):
            moved = True
        else:
            shown_exp, shown_new = (neutral_front(expected), neutral_front(new_text)) if versioned else (expected, new_text)
            exp_lines, new_lines = shown_exp.split("\n"), shown_new.split("\n")
            if len(exp_lines) != len(new_lines):
                return [f"line count {len(new_lines)} instead of the expected {len(exp_lines)}"], False
            differing = [i + 1 for i, (x, y) in enumerate(zip(exp_lines, new_lines)) if x != y]
            return [f"differs from the deterministic substitution on {len(differing)} line(s), first at line {differing[0]}"
                    + ("" if versioned else "; version and modified may not move in a record")], False
    problems = []
    if len(new_text.split("\n")) != len(base_text.split("\n")):
        problems.append("line count changed")
    suffix = rel.rsplit(".", 1)[-1].lower() if "." in rel.rsplit("/", 1)[-1] else ""
    if suffix in ("json", "jsonl", "ndjson"):
        def valid(text):
            try:
                if suffix == "json":
                    json.loads(text)
                else:
                    for line in text.split("\n"):
                        if line.strip():
                            json.loads(line)
                return True
            except ValueError:
                return False
        if valid(base_text) and not valid(new_text):
            problems.append("no longer valid " + ("JSON" if suffix == "json" else "JSON lines"))
    if suffix == "md" and not yaml_still_sane(base_text, new_text):
        problems.append("frontmatter no longer looks like valid YAML")
    return problems, moved


def staged_redaction_only(top: Path, paths: set[str]) -> set[str]:
    """The staged paths proven redaction-only against HEAD; empty without a denylist that has markers."""
    patterns, _, _, markers = load_denylist(top)
    if not patterns or not markers:
        return set()
    proven = set()
    for rel in sorted(paths):
        try:
            base = git(top, "show", f"HEAD:{rel}")
            new = staged_git(top, "show", f":{rel}")
        except (GateError, subprocess.CalledProcessError):
            continue
        problems, _ = redaction_problems(rel, base, new, patterns, markers)
        if not problems and base != new:
            proven.add(rel)
    return proven


def cmd_verify_diff(a, top: Path, patterns, markers) -> int:
    """redact --verify-diff [--base REV]: every changed file must be the deterministic substitution of its base text."""
    base_rev = a.base or "HEAD"
    listing = git(top, "diff", "--name-status", "-z", "--no-renames", base_rev).decode("utf-8", errors="surrogateescape").split("\0")
    changed = [(listing[i], listing[i + 1]) for i in range(0, len(listing) - 1, 2)]
    wanted = [Path(p).resolve() for p in a.paths]
    if wanted:
        changed = [(st, rel) for st, rel in changed if any((top / rel).resolve() == w or w in (top / rel).resolve().parents for w in wanted)]
    texts = blob_bytes(top, [f"{base_rev}:{rel}" for st, rel in changed if st == "M"])
    ok = moved = 0
    violations = []
    for status, rel in changed:
        if status != "M":
            violations.append((rel, f"file {'added' if status == 'A' else 'deleted' if status == 'D' else 'changed'} ({status}), not a substitution"))
            continue
        path = top / rel
        if not path.is_file():
            violations.append((rel, "file missing"))
            continue
        problems, did_move = redaction_problems(rel, texts.get(f"{base_rev}:{rel}", b""), path.read_bytes(), patterns, markers)
        if problems:
            violations.append((rel, "; ".join(problems)))
        else:
            ok += 1
            moved += did_move
            if a.report_all:
                print(f"redaction-only: {safe_path(rel, patterns)}" + (" (version or modified moved)" if did_move else ""))
    for rel, why in violations:
        print(f"violation: {safe_path(rel, patterns)}: {why}")
    print(f"redact --verify-diff against {base_rev}: {len(changed)} changed file(s), {ok} redaction-only "
          f"({moved} with version or modified moved), {len(violations)} violation(s)")
    return 1 if violations else 0


def cmd_redact(a) -> int:
    top = repo_top(Path(a.root).resolve())
    patterns, warnings, _, markers = load_denylist(top)
    if not patterns:
        raise GateError("; ".join(warnings))
    for w in warnings:
        print(f"lint-gate: warning: {w}")
    if a.verify_diff:
        return cmd_verify_diff(a, top, patterns, markers)
    if not a.paths:
        _die("redact needs at least one PATH (or --verify-diff)", 2)
    files, refusals, skipped = collect_files(top, a.paths, a.allow_records, a.allow_outside)
    if refusals:
        for r in refusals:
            print(f"redact: refused: {safe_path(r, patterns)}")
        print("redact: nothing written.")
        return 1
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    plan, totals, per_folder, bad, folder_files = [], {n: [0, 0] for n, _ in patterns}, {}, [], {}
    for f in files:
        try:
            text = f.read_bytes().decode("utf-8")
        except UnicodeDecodeError:
            skipped["binary"] += 1
            continue
        new, counts = redact_text(text, patterns, markers)
        hit = {n: c for n, c in counts.items() if c}
        if not hit:
            continue
        try:
            rel = f.resolve().relative_to(top).as_posix()
            parts = rel.split("/")
            folder = "/".join(parts[:2]) if len(parts) > 2 else parts[0]
        except ValueError:                       # an explicit file under /tmp, allowed by --allow-outside
            rel, folder = str(f.resolve()), "(outside, under /tmp)"
        folder_files[folder] = folder_files.get(folder, 0) + 1
        for n, c in hit.items():
            totals[n][0] += 1
            totals[n][1] += c
            per_folder.setdefault(folder, {}).setdefault(n, [0, 0])
            per_folder[folder][n][0] += 1
            per_folder[folder][n][1] += c
        unmarked = [n for n in hit if n not in markers]
        bad += unmarked
        remaining = [n for n, p in patterns if p.search(new)]
        plan.append((f, rel, text, new, hit, remaining))
    unmarked = sorted(set(bad))
    left = sorted({n for *_, remaining in plan for n in remaining if n in markers})
    if a.verify and not a.apply:
        for f, rel, text, new, hit, _ in plan:
            print(f"still matches: {safe_path(rel, patterns)}: " + ", ".join(f"pattern {n} x{c}" for n, c in sorted(hit.items())))
        print(f"redact --verify: {len(plan)} file(s) still match, of {len(files)} scanned" +
              (f" ({skipped['binary']} binary, {skipped['records']} records skipped)" if any(skipped.values()) else ""))
        return 1 if plan else 0
    mode = "apply" if a.apply else "dry run"
    shown = plan if a.report_all else plan[:40]
    for f, rel, text, new, hit, _ in shown:
        print(f"{safe_path(rel, patterns)}: " + ", ".join(f"pattern {n} x{c}" for n, c in sorted(hit.items())))
    if len(plan) > len(shown):
        print(f"... and {len(plan) - len(shown)} more file(s); --report-all lists them all")
    print(f"redact {mode}: {len(plan)} of {len(files)} file(s) match; per pattern (files/matches): " +
          ", ".join(f"{n}: {t[0]}/{t[1]}" for n, t in totals.items() if t[0]))
    for folder, by in sorted(per_folder.items()):
        total = sum(c[1] for c in by.values())
        print(f"  {folder:<34}{folder_files.get(folder, 0)} files, {total} matches: " +
              ", ".join(f"p{n} {c[0]}f/{c[1]}m" for n, c in sorted(by.items())))
    if any(skipped.values()):
        print(f"  skipped: {skipped['binary']} binary, {skipped['records']} in records or done queue, {skipped['other']} other")
    if unmarked:
        print(f"redact: pattern(s) {', '.join(map(str, unmarked))} match but have no `# marker:` line in the local denylist"
              f"{'; --apply refuses and writes nothing' if a.apply else ' (a dry run only reports)'}")
    if not a.apply:
        print("  dry run; pass --apply to rewrite" if not unmarked else "  dry run")
        return 0
    if unmarked:
        print("redact: refused: add a marker line for each pattern above; nothing written.")
        return 1
    if left:
        print(f"redact: refused: a marker would leave pattern(s) {', '.join(map(str, left))} matching; nothing written.")
        return 1
    bumped, plain_changed = [], []
    for f, rel, text, new, hit, _ in plan:
        rel_parts = tuple(rel.split("/"))
        immutable = under(rel_parts, ("_records_",)) or under(rel_parts, ("_queue_", "done")) or under(rel_parts, ("_logs_",))
        final, change = (new, None) if immutable else bump_front(new, now)      # records change only the name
        tmp = f.with_name(f".{f.name}.redact-tmp")
        tmp.write_bytes(final.encode("utf-8"))
        shutil.copymode(f, tmp)
        os.replace(tmp, f)
        (bumped if change else plain_changed).append((safe_path(rel, patterns), change))
    print(f"redact: rewrote {len(plan)} file(s); {len(bumped)} version(s) bumped, {len(plain_changed)} without version fields")
    for rel, (old, new) in bumped:
        print(f"  needs a changelog line: {rel} (version {old} -> {new})")
    for rel, _ in plain_changed:
        print(f"  no version fields to bump: {rel}")
    rest = [rel for f, rel, *_ in plan if still_matches(f.read_text(encoding="utf-8"), patterns)]
    print(f"redact verified: {len(rest)} file(s) still match")
    return 1 if rest else 0


# --- check -------------------------------------------------------------------------------------------------

def require_landing_ready(top: Path, a, rules: tuple) -> None:
    """The landing form (--base with --landing) refuses to pass what it could not check: a base that does not resolve
    reads as an empty tree, and a missing denylist skips the privacy rule with only a warning. Both are GateErrors here, so
    the exit is 2 and a landing waits until the gate can run. The hooks never pass --landing and keep warn and allow."""
    if a.staged or not a.base:
        raise GateError("--landing is the base form: use --base REF, not --staged")
    if not git(top, "rev-parse", "--verify", "--quiet", f"{a.base}^{{commit}}", check=False).strip():
        raise GateError(f"landing: base {a.base} does not resolve to a commit, so there is nothing to compare against")
    if PRIVACY_RULE not in rules:
        raise GateError("landing: the privacy rule must run; --rules without it is refused")
    patterns, _warnings, _expect, _ = load_denylist(top)
    if not patterns:
        raise GateError("landing: the privacy denylist is missing or empty, so the privacy rule cannot run")


def cmd_check(a) -> int:
    started = time.time()
    root = Path(a.root).resolve()
    top = repo_top(root)
    rules = tuple(r for r in (a.rules or os.environ.get("LINT_GATE_RULES") or ",".join(GATE_RULES + (PRIVACY_RULE, PLAYBOOK_RULE))).split(",") if r)
    if a.landing:
        require_landing_ready(top, a, rules)
    play_block, play_warn = playbook_findings(top, a.staged, a.base or "HEAD") if PLAYBOOK_RULE in rules else ([], [])
    for w in play_warn:
        print(f"lint-gate: warning: {w}")
    privacy = None
    if PRIVACY_RULE in rules:
        privacy = privacy_scan_staged(top, a.staged)
        for w in privacy["warnings"]:
            print(f"lint-gate: warning: {w}")
    hits = privacy["hits"] if privacy else []
    failures = privacy["failures"] if privacy else []
    added = exempt_additions(top, "HEAD" if a.staged else (a.base or "HEAD"), a.staged)
    for entry in added:
        print(f"BLOCKED [exempt-list] {entry}: added to exempt.txt; the list may only shrink (remove entries, never add)")
    if failures:
        print(f"lint-gate: {EXPECT_MESSAGE}")
        for f in failures:
            print(f"BLOCKED [privacy] {f}")
    try:
        paths = reflection_paths(a)
        if a.staged:
            report = run_linter(paths, top, ["--staged"], STAGED_TIMEOUT, staged=True)
            ref, mode = "HEAD", "staged"
        else:
            ref = a.base or "HEAD"
            report = run_linter(paths, top, ["--base", ref], FULL_TIMEOUT, staged=False)
            mode = f"base {ref}"
    except GateError:
        if hits or failures or added or play_block:          # these block even when the linter cannot run
            print_privacy_hits(hits)
            for line in play_block:
                print(f"BLOCKED {line}")
            print(f"lint-gate: {len(hits) + len(failures) + len(added) + len(play_block)} finding(s) block this commit; the linter could not run.")
            return 1
        raise
    base = BaseTree(top, ref, staged=a.staged)
    docs, folders = exemptions(top)
    redacted = set()
    if a.staged and PRIVACY_RULE in rules:       # a staged file proven redaction-only is exempt from the size rule, per file
        sized = {path_of(f) for f in report.get("errors", []) if tag_of(f) == "document-concision"}
        redacted = staged_redaction_only(top, sized) if sized else set()
    blocking, legacy, exempt, other = classify(report.get("errors", []), rules, base, docs, folders, redacted)
    other_findings = [f for f in report.get("errors", []) if tag_of(f) not in rules]
    print_privacy_hits(hits)
    for f in blocking:
        print(f"BLOCKED {short(f)}")
    for line in play_block:
        print(f"BLOCKED {line}")
    seconds = time.time() - started
    seen = (f"privacy {privacy['patterns']} pattern(s) over {privacy['lines']} added line(s)" if privacy and privacy["patterns"]
            else "privacy not checked")
    note = (f"{len(legacy)} legacy structural finding(s) and {len(exempt)} exempt finding(s) ignored, "
            f"{other} error(s) of other rules ignored, {seen}")
    total = len(blocking) + len(hits) + len(failures) + len(added) + len(play_block)
    if getattr(a, "list_ignored", False):
        print_ignored(legacy, exempt, other_findings)
    if total:
        print(f"lint-gate: {total} blocking finding(s) ({mode}, {seconds:.1f}s); {note}.")
        if blocking:
            print("Trim the document under 500 words (300 is recommended) or move measured rows to a CSV beside it; "
                  "a folder needs its INDEX.md. See _conventions_/core-conventions/document-concision.md.")
        if play_block:
            print("Playbook cards: keep a card at 300 words or fewer with its Route and Rules sections (_tools_/playbook-check/INDEX.md).")
        if hits:
            print("Privacy: take the identifier out of the added line or file name (see "
                  "_conventions_/local-conventions/account-privacy.md); the denylist is local and never committed.")
        if failures:
            print("Privacy: fix the pattern or its `# expect-min` line in the local denylist; --no-verify stays the override.")
        if added:
            print("exempt.txt only shrinks: split or trim the document instead of exempting it.")
        return 1
    print(f"lint-gate: ok ({mode}, {seconds:.1f}s); {note}.")
    return 0


def print_ignored(legacy: list, exempt: list, other: list) -> None:
    """What `check` counts and ignores, with its paths and rule names (never the finding text): the legacy structural findings, the exempt
    ones and the errors of rules the gate does not enforce. Sorted, one `path  [rule]` per line (` xN` when a path has N findings of the
    rule), so two runs diff to the new ones."""
    for title, findings in (("legacy structural findings (ignored: they existed at the base)", legacy), ("exempt findings (exempt.txt)", exempt),
                            ("errors of other rules (not enforced by this gate)", other)):
        rows: dict[tuple[str, str], int] = {}
        by_rule: dict[str, int] = {}
        for f in findings:
            key = (path_of(f), tag_of(f) or "?")
            rows[key] = rows.get(key, 0) + 1
            by_rule[key[1]] = by_rule.get(key[1], 0) + 1
        print(f"ignored - {title}: {len(findings)}" + (f" ({', '.join(f'{t} {n}' for t, n in sorted(by_rule.items()))})" if rows else " (none)"))
        for (path, tag), n in sorted(rows.items()):
            print(f"  {path}  [{tag}]" + (f" x{n}" if n > 1 else ""))


# --- install -----------------------------------------------------------------------------------------------

def cmd_install(a) -> int:
    top = repo_top(Path(a.root).resolve())
    hooks = [top / HOOKS_REL / name for name in HOOK_NAMES]
    for hook in hooks:
        if not hook.is_file():
            raise GateError(f"hook missing: {hook}")
    current = git(top, "config", "--local", "--get", "core.hooksPath", check=False).decode().strip()
    if current and current != HOOKS_REL and not a.force:
        print(f"lint-gate: core.hooksPath is already {current!r}; refusing to replace it (use --force).")
        return 1
    if a.dry_run:
        print(f"lint-gate: would set core.hooksPath to {HOOKS_REL} in {top}")
    else:
        for hook in hooks:
            hook.chmod(hook.stat().st_mode | 0o111)
        git(top, "config", "--local", "core.hooksPath", HOOKS_REL)
        print(f"lint-gate: core.hooksPath set to {HOOKS_REL} in {top} ({', '.join(HOOK_NAMES)})")
    print("Rollback: git config --unset core.hooksPath")
    return 0


# --- exempt-prune ------------------------------------------------------------------------------------------

def cmd_exempt_prune(a) -> int:
    """List, and with --apply remove, the exempt.txt entries that no longer exempt anything: no tracked file matching the
    entry has HARD_WORDS or more body words. The list only shrinks, so this is the way entries leave it."""
    top = repo_top(Path(a.root).resolve())
    counter = load_counter(reflection_paths(a))
    path = top / EXEMPT_REL
    lines = path.read_text(encoding="utf-8").splitlines()
    tracked = [n for n in git(top, "ls-files", "-z").decode("utf-8", errors="surrogateescape").split("\0") if n]
    obsolete, kept = [], 0
    for entry in exempt_entries("\n".join(lines)):
        if entry.startswith("folder "):
            kept += 1
            continue
        oversized = False
        for name in (n for n in tracked if is_exempt(n, [entry])):
            try:
                words = counter.check_text((top / name).read_text(encoding="utf-8"), name)["body_words"]
            except (OSError, UnicodeError):
                continue
            if words >= HARD_WORDS:
                oversized = True
                break
        if oversized:
            kept += 1
        else:
            obsolete.append(entry)
    for entry in obsolete:
        print(f"obsolete: {entry}")
    print(f"exempt.txt: {len(obsolete)} obsolete entr{'y' if len(obsolete) == 1 else 'ies'}, {kept} still needed" +
          ("" if a.apply else "; dry run, pass --apply to remove"))
    if a.apply and obsolete:
        path.write_text("\n".join(l for l in lines if l.strip() not in obsolete) + "\n", encoding="utf-8")
        print(f"exempt.txt: removed {len(obsolete)}")
    return 0


# --- record-check ------------------------------------------------------------------------------------------

def cmd_record_check(a) -> int:
    counter = load_counter(reflection_paths(a))
    worst = 0
    for name in a.paths:
        try:
            text = Path(name).read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            raise GateError(f"{name}: {exc}")
        words = counter.check_text(text, name)["body_words"]
        over = words >= a.limit
        print(f"{name}: {words} body words (trim limit {a.limit}, linter hard limit {HARD_WORDS}) "
              f"{'TRIM BEFORE CLOSING' if over else 'ok'}")
        worst = 1 if over else worst
    return worst


# --- stub-index --------------------------------------------------------------------------------------------

STUB = """---
title: Execution records for {activity} on {date}
created: {now}
modified: {now}
version: 1.0.0
description: Execution records for {activity} on {date}, one file per run; the day index lists them.
---

# {activity} records, {date}

Execution records for {activity} on {date}, one file per run; the day index lists them.
"""


def today_pacific() -> str:
    try:
        from zoneinfo import ZoneInfo
        return datetime.now(ZoneInfo("America/Los_Angeles")).strftime("%Y-%m-%d")
    except Exception:   # no tz database: the local date serves
        return datetime.now().strftime("%Y-%m-%d")


def cmd_stub_index(a) -> int:
    """A static INDEX.md in every _records_/<today>/<activity>/ folder that lacks one; never an older day, never an
    existing file (exclusive create), a dry run unless --apply."""
    top = repo_top(Path(a.root).resolve())
    day = a.today or today_pacific()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", day):
        raise GateError(f"--today must be YYYY-MM-DD, got {day!r}")
    folder = top / "_records_" / day
    if not folder.is_dir():
        print(f"lint-gate: no _records_/{day}/ folder; nothing to do.")
        return 0
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    made, kept = [], 0
    for child in sorted(folder.iterdir()):
        if not child.is_dir() or child.is_symlink() or child.name.startswith("."):
            continue
        target = child / "INDEX.md"
        if target.exists():
            kept += 1
            continue
        made.append(target.relative_to(top).as_posix())
        if a.apply:
            with open(target, "x", encoding="utf-8") as fh:   # "x": never overwrite
                fh.write(STUB.format(activity=child.name, date=day, now=now))
    verb = "created" if a.apply else "would create"
    for path in made:
        print(f"{verb} {path}")
    if not (folder / "INDEX.md").exists():
        print(f"note: _records_/{day}/INDEX.md (the day index) is missing; the operator writes it.")
    print(f"lint-gate: stub-index {day}: {len(made)} {verb.split()[-1] if a.apply else 'to create'}, {kept} already had an INDEX.md"
          f"{'' if a.apply else '; dry run, pass --apply to write'}.")
    return 0


# --- watch -------------------------------------------------------------------------------------------------

def top_folder(path: str) -> str:
    return path.split("/", 1)[0] if "/" in path else "(root)"


def blob_texts(top: Path, ref: str, names: list[str]) -> dict[str, str]:
    """Texts of `names` at `ref` in one git call; a name the ref lacks is absent from the result."""
    if not names:
        return {}
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    proc = subprocess.run(["git", "-C", str(top), "cat-file", "--batch"], capture_output=True, env=env,
                          input="".join(f"{ref}:{n}\n" for n in names).encode("utf-8", errors="surrogateescape"))
    data, pos, out = proc.stdout, 0, {}
    for name in names:
        end = data.find(b"\n", pos)
        header = data[pos:end].split()
        if len(header) == 3 and header[1] == b"blob":
            size = int(header[2])
            out[name] = data[end + 1:end + 1 + size].decode("utf-8", errors="replace")
            pos = end + 2 + size
        else:
            pos = end + 1
    return out


def growth_since(top: Path, prev_head: str, words_now: dict[str, int], counter, min_words: int) -> tuple[list[dict], str]:
    """Documents (modified since prev_head) whose body grew more than 20 percent and min_words."""
    probe = subprocess.run(["git", "-C", str(top), "cat-file", "-e", f"{prev_head}^{{commit}}"], capture_output=True,
                           env={k: v for k, v in os.environ.items() if not k.startswith("GIT_")})
    if probe.returncode:
        return [], "previous head not in this repository; growth not computed"
    changed = git(top, "diff", "--name-only", "--no-renames", "--diff-filter=M", "-z", prev_head, "--").decode(
        "utf-8", errors="surrogateescape").split("\0")
    names = [n for n in changed if n.endswith(".md") and n in words_now]
    note = ""
    if len(names) > GROWTH_FILE_CAP:
        note = f"growth checked for the first {GROWTH_FILE_CAP} of {len(names)} modified documents"
        names = names[:GROWTH_FILE_CAP]
    found = []
    for name, text in blob_texts(top, prev_head, names).items():
        before = counter.check_text(text, name)["body_words"]
        now = words_now[name]
        if before > 0 and now > before * (1 + GROWTH) and now - before >= min_words:
            found.append({"path": name, "before": before, "now": now, "growth_pct": round(100 * (now - before) / before)})
    found.sort(key=lambda r: -(r["now"] - r["before"]))
    return found, note


def cmd_watch(a) -> int:
    if a.privacy:
        return cmd_privacy_census(a)
    root = Path(a.root).resolve()
    top = repo_top(root)
    paths = reflection_paths(a)
    baseline_file = Path(a.baseline) if a.baseline else top / BASELINE_REL
    prev = {}
    if baseline_file.is_file():
        try:
            prev = json.loads(baseline_file.read_text(encoding="utf-8"))
        except ValueError:
            prev = {}
    head = git(top, "rev-parse", "--verify", "--quiet", "HEAD^{commit}", check=False).decode().strip()
    anchor_ref = a.anchor or prev.get("anchor") or head or "HEAD"
    anchor = git(top, "rev-parse", "--verify", "--quiet", f"{anchor_ref}^{{commit}}", check=False).decode().strip()
    if a.from_json:
        report = json.loads(Path(a.from_json).read_text(encoding="utf-8"))
    else:
        report = run_linter(paths, top, ["--base", anchor or "HEAD"], FULL_TIMEOUT, staged=False)
    rows = report.get("document_budgets", {}).get("documents")
    if not rows:
        raise GateError("the linter report holds no document budgets")
    words_now = {r["path"]: r["body_words"] for r in rows}
    totals = {
        "documents": len(rows),
        "over_300": sum(r["body_words"] > SOFT_WORDS for r in rows),
        "over_500": sum(r["body_words"] >= HARD_WORDS for r in rows),
        "legacy": sum(bool(r["legacy"] and r["hard_violation"]) for r in rows),
        "new": sum(r["severity"] == "error" for r in rows),
    }
    patterns, folder_patterns = exemptions(top)
    base = BaseTree(top, anchor or "HEAD")
    errors = report.get("errors", [])
    raw = {t: sum(tag_of(e) == t for e in errors) for t in GATE_RULES}
    blocking, legacy_structural, exempt, _ = classify(errors, GATE_RULES, base, patterns, folder_patterns)
    new_by_rule = {t: sum(tag_of(e) == t for e in blocking) for t in GATE_RULES}
    folders: dict[str, dict] = {}
    for r in rows:
        f = folders.setdefault(top_folder(r["path"]), {"documents": 0, "over_300": 0, "over_500": 0, "legacy": 0, "new": 0,
                                                       "words": 0})
        f["documents"] += 1
        f["over_300"] += r["body_words"] > SOFT_WORDS
        f["over_500"] += r["body_words"] >= HARD_WORDS
        f["legacy"] += bool(r["legacy"] and r["hard_violation"])
        f["new"] += r["severity"] == "error"
        f["words"] += r["body_words"]
    largest = sorted(rows, key=lambda r: (-r["body_words"], r["path"]))
    # Which documents the counts are about (the daily review names each new one over 500 and its owner): the new ones at or over 500 words
    # (marked when exempt.txt covers them), the exempt ones, and the new gate errors that block. Paths and word counts only.
    exempt_list = sorted({(path_of(f), tag_of(f) or "?") for f in exempt})
    exempt_set = {p for p, _ in exempt_list}
    new_docs = sorted(({"path": r["path"], "words": r["body_words"], "exempt": r["path"] in exempt_set}
                       for r in rows if r["severity"] == "error"), key=lambda d: (-d["words"], d["path"]))
    blocking_list = sorted({(path_of(f), tag_of(f) or "?") for f in blocking})
    prev_head, growth, growth_note = prev.get("git_head"), [], ""
    if prev_head:
        try:
            growth, growth_note = growth_since(top, prev_head, words_now, load_counter(paths), a.min_growth_words)
        except GateError as exc:
            growth_note = str(exc)
    else:
        growth_note = "no previous run; growth is measured from the next run"
    summary = {
        "version": 1, "tool_version": VERSION, "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "git_head": head, "anchor": anchor, **totals, "gate_errors": raw, "new_errors": new_by_rule,
        "new_errors_total": len(blocking), "exempt_documents": len(exempt),
        "legacy_structural": len(legacy_structural), "by_top_folder": folders,
        "top": [{"path": r["path"], "words": r["body_words"]} for r in largest[:TOP_KEPT]],
        "growth": growth[:20],
        "new_documents": new_docs[:LIST_CAP], "new_documents_more": max(0, len(new_docs) - LIST_CAP),
        "exempt_list": [{"path": p, "rule": t} for p, t in exempt_list[:LIST_CAP]], "exempt_list_more": max(0, len(exempt_list) - LIST_CAP),
        "new_error_list": [{"path": p, "rule": t} for p, t in blocking_list[:LIST_CAP]], "new_error_list_more": max(0, len(blocking_list) - LIST_CAP),
    }
    if a.format == "json":
        print(json.dumps(summary, indent=1))
    else:
        print_watch(summary, largest[:a.top], growth_note, prev.get("generated_at"),
                    {"new": new_docs, "exempt": exempt_list, "errors": blocking_list} if a.list else None)
    if not a.no_write:
        baseline_file.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=baseline_file.parent, prefix=".lint-baseline-")
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(summary, fh, indent=1)
            fh.write("\n")
        os.replace(tmp, baseline_file)
        print(f"baseline summary written: {baseline_file}")
    return 0


def print_watch_lists(s: dict, full: dict | None) -> None:
    """The documents behind the counts, with their paths: new ones at or over 500 words, exempt ones, and new blocking errors. The first LIST_CAP of
    each (what the summary keeps) unless `--list` passes `full`, which holds all of them."""
    def section(title: str, shown: list, total: int, line) -> None:
        print(title + ("" if total else " (none)"))
        for item in shown:
            print(line(item))
        if total > len(shown):
            print(f"  ({total - len(shown)} more; run with --list for all)")

    new = full["new"] if full else s["new_documents"]
    exempt = full["exempt"] if full else [(e["path"], e["rule"]) for e in s["exempt_list"]]
    errors = full["errors"] if full else [(e["path"], e["rule"]) for e in s["new_error_list"]]
    new_total = len(s["new_documents"]) + s["new_documents_more"]
    exempt_total = len(s["exempt_list"]) + s["exempt_list_more"]
    errors_total = len(s["new_error_list"]) + s["new_error_list_more"]
    section(f"new documents at or over {HARD_WORDS} words: {new_total:,}", new, new_total,
            lambda d: f"  {d['words']:>7,}  {d['path']}" + ("  [exempt: exempt.txt]" if d["exempt"] else ""))
    section(f"exempt documents: {exempt_total:,}", exempt, exempt_total, lambda e: f"  {e[0]}  [{e[1]}]")
    if errors_total:
        section(f"new gate errors vs anchor, by path: {errors_total:,}", errors, errors_total, lambda e: f"  {e[0]}  [{e[1]}]")


def print_watch(s: dict, largest: list[dict], growth_note: str, prev_at: str | None, full: dict | None = None) -> None:
    n = s["new_errors"]
    print(f"lint-gate watch {s['generated_at']}  head {s['git_head'][:8]}  anchor {s['anchor'][:8]}")
    print(f"documents {s['documents']:,} | over 300 words: {s['over_300']:,} | at or over 500: {s['over_500']:,} "
          f"(legacy {s['legacy']:,}, new {s['new']:,})")
    print("gate errors in the tree: " + ", ".join(f"{k} {v}" for k, v in s["gate_errors"].items()))
    print(f"NEW ERRORS vs anchor: {s['new_errors_total']} (document-concision {n['document-concision']}, entry-points "
          f"{n['entry-points']}, type-instance-trees {n['type-instance-trees']}); exempt documents {s['exempt_documents']}, "
          f"legacy structural {s['legacy_structural']}")
    if s["new_errors_total"]:
        print("  -> assign the owning seat a fix")
    print_watch_lists(s, full)
    print(f"{'top folder':<22}{'docs':>7}{'>300':>7}{'>=500':>7}{'legacy':>8}{'new':>5}")
    for name, f in sorted(s["by_top_folder"].items(), key=lambda kv: -kv[1]["over_500"]):
        print(f"{name:<22}{f['documents']:>7}{f['over_300']:>7}{f['over_500']:>7}{f['legacy']:>8}{f['new']:>5}")
    print(f"{len(largest)} largest documents:")
    for r in largest:
        print(f"  {r['body_words']:>7,}  {r['path']}")
    since = f" since {prev_at}" if prev_at else ""
    if s["growth"]:
        print(f"grown more than {int(GROWTH * 100)} percent{since}:")
        for g in s["growth"]:
            print(f"  {g['before']} -> {g['now']} (+{g['growth_pct']}%)  {g['path']}")
    else:
        print(f"grown more than {int(GROWTH * 100)} percent{since}: none" + (f" ({growth_note})" if growth_note else ""))
    if growth_note and s["growth"]:
        print(f"  note: {growth_note}")


# --- command line ------------------------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--root", default=".", help="the repository to judge (default: the current directory)")
    common.add_argument("--reflection", help="the reflection checkout (default: ~/dtadpole/reflection or LINT_GATE_REFLECTION)")
    p = argparse.ArgumentParser(prog="lint_gate.py", description=__doc__.split("\n\n")[0])
    p.add_argument("--version", action="version", version=VERSION)
    sub = p.add_subparsers(dest="command", required=True)
    c = sub.add_parser("check", parents=[common], help="block new or changed oversized or misshapen documents")
    c.add_argument("--staged", action="store_true", help="judge the staged commit (the hook; seconds)")
    c.add_argument("--list-ignored", action="store_true", help="also print the path and rule of every ignored finding: legacy structural, exempt and other rules")
    c.add_argument("--base", metavar="REF", help="judge the tree against REF (a full lint, about a minute)")
    c.add_argument("--rules", help=f"comma list of rule tags that block (default {','.join(GATE_RULES)}; env LINT_GATE_RULES)")
    c.add_argument("--landing", action="store_true", help="the Integrator's form with --base: exit 2 (never a pass) when the base "
                   "does not resolve, the denylist is missing or empty, or a rule crashes")
    c.set_defaults(run=cmd_check)
    i = sub.add_parser("install", parents=[common], help="point core.hooksPath at the tracked pre-commit hook")
    i.add_argument("--dry-run", action="store_true")
    i.add_argument("--force", action="store_true", help="replace a different core.hooksPath")
    i.set_defaults(run=cmd_install)
    w = sub.add_parser("watch", parents=[common], help="size counts, largest documents and growth; writes a summary")
    w.add_argument("--anchor", metavar="REF", help="the commit whose oversized documents count as legacy (kept in the baseline)")
    w.add_argument("--baseline", help=f"summary file (default {BASELINE_REL} in the repository)")
    w.add_argument("--from-json", help="reuse a saved linter --json report instead of running the linter")
    w.add_argument("--top", type=int, default=10)
    w.add_argument("--min-growth-words", type=int, default=MIN_GROWTH_WORDS, help="ignore growth smaller than this")
    w.add_argument("--format", choices=("text", "json"), default="text")
    w.add_argument("--list", action="store_true", help="print every new, exempt and new-error path (default: the first 50 of each)")
    w.add_argument("--no-write", action="store_true")
    w.add_argument("--privacy", action="store_true", help="count files and lines per top folder for each denylist pattern; "
                   "counts and paths only, no matched text")
    w.add_argument("--worktree", action="store_true", help="with --privacy, read the working tree instead of HEAD")
    w.add_argument("--accept", action="store_true", help="with --privacy, record the census even where a pattern dropped to zero "
                   "(a redaction landed)")
    w.set_defaults(run=cmd_watch)
    st = sub.add_parser("stub-index", parents=[common], help="static INDEX.md for today's records folders that lack one")
    st.add_argument("--apply", action="store_true", help="write the files (the default is a dry run)")
    st.add_argument("--today", metavar="YYYY-MM-DD", help="override the Pacific date (tests, replays)")
    st.set_defaults(run=cmd_stub_index)
    d = sub.add_parser("redact", parents=[common], help="replace denylist matches with each pattern's marker text (dry run default)")
    d.add_argument("paths", nargs="*", metavar="PATH", help="files or folders; only these are touched")
    d.add_argument("--verify-diff", action="store_true", help="prove every changed file is the redaction-only substitution of "
                   "its base text (frontmatter version and modified aside); exit 1 otherwise")
    d.add_argument("--base", default="", help="with --verify-diff, the revision to compare against (default HEAD)")
    d.add_argument("--apply", action="store_true", help="rewrite the files")
    d.add_argument("--verify", action="store_true", help="re-scan the paths; exit 1 if any pattern still matches")
    d.add_argument("--allow-records", action="store_true", help="include _records_/ and _queue_/done (immutable play records)")
    d.add_argument("--allow-outside", action="store_true", help="accept an explicit absolute file path under /tmp (a saved original)")
    d.add_argument("--report-all", action="store_true", help="list every matching file, not the first 40")
    d.set_defaults(run=cmd_redact)
    x = sub.add_parser("exempt-prune", parents=[common], help="remove exempt.txt entries that exempt nothing any more (dry run unless --apply)")
    x.add_argument("--apply", action="store_true")
    x.set_defaults(run=cmd_exempt_prune)
    r = sub.add_parser("record-check", parents=[common], help="body words of a play record; exit 1 at the limit")
    r.add_argument("paths", nargs="+", metavar="PATH")
    r.add_argument("--limit", type=int, default=RECORD_LIMIT)
    r.set_defaults(run=cmd_record_check)
    return p


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.run(args)
    except GateError as exc:
        print(f"lint-gate: cannot run: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:                      # a crashed rule: exit 1 would read as "blocked", and 0 never
        if not getattr(args, "landing", False):
            raise
        print(f"lint-gate: cannot run: a rule crashed ({type(exc).__name__})", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
