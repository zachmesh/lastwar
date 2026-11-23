#!/usr/bin/env python3
"""lint-gate: stop new oversized or misshapen documents and show size growth cheaply.

Subcommands: check, install, watch, record-check. It runs the reflection convention linter
(~/dtadpole/reflection, or LINT_GATE_REFLECTION / --reflection) with the right --root and --vocabulary and
judges only what the commit adds or changes; legacy findings never block. Standard library only; the word counter
is the linter's own, loaded from the reflection checkout. Exit 0 ok, 1 blocked or limit reached, 2 cannot run.
"""
from __future__ import annotations

import argparse
import fnmatch
import importlib.util
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

VERSION = "1.0.0"
GATE_RULES = ("document-concision", "entry-points", "type-instance-trees")
HARD_WORDS, SOFT_WORDS, RECORD_LIMIT = 500, 300, 480
STAGED_TIMEOUT, FULL_TIMEOUT = 25, 600          # seconds; the staged cap keeps the hook under 30 s
BASELINE_REL = "_tools_/state/lint-baseline.json"
HOOKS_REL = "_tools_/lint-gate/hooks"
EXEMPT_REL = "_tools_/lint-gate/exempt.txt"
TOP_KEPT, GROWTH, MIN_GROWTH_WORDS, GROWTH_FILE_CAP = 50, 0.20, 20, 400
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
        return json.loads(proc.stdout)
    except ValueError:
        raise GateError(f"the linter gave no JSON (exit {proc.returncode}): {proc.stderr.strip()[-300:]}")


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


def exemptions(top: Path) -> list[str]:
    f = top / EXEMPT_REL
    if not f.is_file():
        return []
    return [ln.strip() for ln in f.read_text(encoding="utf-8").splitlines() if ln.strip() and not ln.lstrip().startswith("#")]


def is_exempt(path: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatchcase(path, p) for p in patterns)


class BaseTree:
    """The files and folders a ref holds; empty when the ref does not resolve (an unborn branch)."""

    def __init__(self, root: Path, ref: str):
        self.root = root
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
            return offender not in base.files and offender not in base.dirs and not base.ignored(offender)
    return True


def classify(errors: list[str], rules, base: BaseTree, patterns: list[str]):
    blocking, legacy, exempt, other = [], [], [], 0
    for f in errors:
        tag = tag_of(f)
        if tag not in rules:
            other += 1
        elif tag == "document-concision" and is_exempt(path_of(f), patterns):
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


# --- check -------------------------------------------------------------------------------------------------

def cmd_check(a) -> int:
    started = time.time()
    root = Path(a.root).resolve()
    top = repo_top(root)
    paths = reflection_paths(a)
    rules = tuple(r for r in (a.rules or os.environ.get("LINT_GATE_RULES") or ",".join(GATE_RULES)).split(",") if r)
    if a.staged:
        report = run_linter(paths, top, ["--staged"], STAGED_TIMEOUT, staged=True)
        ref, mode = "HEAD", "staged"
    else:
        ref = a.base or "HEAD"
        report = run_linter(paths, top, ["--base", ref], FULL_TIMEOUT, staged=False)
        mode = f"base {ref}"
    base = BaseTree(top, ref)
    blocking, legacy, exempt, other = classify(report.get("errors", []), rules, base, exemptions(top))
    for f in blocking:
        print(f"BLOCKED {short(f)}")
    seconds = time.time() - started
    note = (f"{len(legacy)} legacy structural finding(s) and {len(exempt)} exempt document(s) ignored, "
            f"{other} error(s) of other rules ignored")
    if blocking:
        print(f"lint-gate: {len(blocking)} blocking finding(s) ({mode}, {seconds:.1f}s); {note}.")
        print("Trim the document under 500 words (300 is recommended) or move measured rows to a CSV beside it; "
              "a folder needs its INDEX.md. See _conventions_/core-conventions/document-concision.md.")
        return 1
    print(f"lint-gate: ok ({mode}, {seconds:.1f}s); {note}.")
    return 0


# --- install -----------------------------------------------------------------------------------------------

def cmd_install(a) -> int:
    top = repo_top(Path(a.root).resolve())
    hook = top / HOOKS_REL / "pre-commit"
    if not hook.is_file():
        raise GateError(f"hook missing: {hook}")
    current = git(top, "config", "--local", "--get", "core.hooksPath", check=False).decode().strip()
    if current and current != HOOKS_REL and not a.force:
        print(f"lint-gate: core.hooksPath is already {current!r}; refusing to replace it (use --force).")
        return 1
    if a.dry_run:
        print(f"lint-gate: would set core.hooksPath to {HOOKS_REL} in {top}")
    else:
        hook.chmod(hook.stat().st_mode | 0o111)
        git(top, "config", "--local", "core.hooksPath", HOOKS_REL)
        print(f"lint-gate: core.hooksPath set to {HOOKS_REL} in {top}")
    print("Rollback: git config --unset core.hooksPath")
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
    patterns = exemptions(top)
    base = BaseTree(top, anchor or "HEAD")
    errors = report.get("errors", [])
    raw = {t: sum(tag_of(e) == t for e in errors) for t in GATE_RULES}
    blocking, legacy_structural, exempt, _ = classify(errors, GATE_RULES, base, patterns)
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
    }
    if a.format == "json":
        print(json.dumps(summary, indent=1))
    else:
        print_watch(summary, largest[:a.top], growth_note, prev.get("generated_at"))
    if not a.no_write:
        baseline_file.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=baseline_file.parent, prefix=".lint-baseline-")
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            json.dump(summary, fh, indent=1)
            fh.write("\n")
        os.replace(tmp, baseline_file)
        print(f"baseline summary written: {baseline_file}")
    return 0


def print_watch(s: dict, largest: list[dict], growth_note: str, prev_at: str | None) -> None:
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
    c.add_argument("--base", metavar="REF", help="judge the tree against REF (a full lint, about a minute)")
    c.add_argument("--rules", help=f"comma list of rule tags that block (default {','.join(GATE_RULES)}; env LINT_GATE_RULES)")
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
    w.add_argument("--no-write", action="store_true")
    w.set_defaults(run=cmd_watch)
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


if __name__ == "__main__":
    sys.exit(main())
