#!/usr/bin/env python3
"""playbook_check: validates the activity playbook cards (OD-20261123-15, IMP-20261123-14). Read-only, counts only.

An activity's INDEX.md becomes a card of 300 words or fewer: Goal, Route (at most 8 numbered steps), Rules (at most 5, each with a
status and a date, citing RECORDS), Failures (at most 3), Open questions (at most 3, each with its test), Numbers (one line from the
records) and Links (at most 5). See card-template.md. Checks:

  shape      the seven sections in order, no Errata section, the counts above, every rule line `- R1 [verified|unverified DATE] text
             (evidence: _records_/...)`, a `test:` on every open question, a Numbers line with a digit and a record path
  citations  every `_records_/`, `_activities_/`, `_run_notes_/`, `_knowledge_/` ... path and every relative link in the card resolves:
             directly, or through `_run_notes_/moved-paths/moved-paths.csv` (flagged as a citation to update); a rule cites a record,
             never a run note or a run article
  stale      an unverified rule dated more than --stale-days (14) ago

  playbook_check.py check PATH...            each file as a card; exit 1 on a shape or citation error (stale is a warning)
  playbook_check.py changed [--staged | --base REV]
                                             the changed _activities_/*/INDEX.md files: a card is checked in full, a card that lost its
                                             shape is an error, a page that was never a card is skipped (for the commit)
  playbook_check.py daily                    every activity: counts of cards, passes, findings by code, rules verified and stale, the
                                             verified share, citations by how they resolve (for the coach); exit 1 on a failing card
                                             or a stale rule

Output is counts and finding codes with the activity name: never a rule, a failure or a number from a card. --stale-fail makes stale
fail `check` and `changed` too. Exit 0 clean, 1 findings, 2 cannot run. Standard library only.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import os
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
SECTIONS = ("Goal", "Route", "Rules", "Failures", "Open questions", "Numbers", "Links")
LIMITS = {"Route": 8, "Rules": 5, "Failures": 3, "Open questions": 3, "Links": 5}
RULE = re.compile(r"^- (R\d+) \[(verified|unverified|superseded) (\d{4}-\d{2}-\d{2})\] (.+?) \(evidence: ([^)]+)\)\s*$")
PATH = re.compile(r"_(?:records|activities|run_notes|knowledge|conventions|tools|seats|queue)_/[A-Za-z0-9._/-]*[A-Za-z0-9]")
LINK = re.compile(r"\]\(([^)\s#]+)(?:#[^)\s]*)?\)")
MAP_REL = "_run_notes_/moved-paths/moved-paths.csv"
_COUNTER = []


def body_words(text: str) -> int:
    if not _COUNTER:
        path = Path(os.environ.get("PLAYBOOK_WORD_COUNTER") or "~/dtadpole/reflection/_tools_/document-word-budget/word-budget.py").expanduser()
        try:
            spec = importlib.util.spec_from_file_location("playbook_word_budget", path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            _COUNTER.append(module.check_text)
        except Exception:
            _COUNTER.append(None)
    if _COUNTER[0] is not None:
        try:
            return int(_COUNTER[0](text, "INDEX.md")["body_words"])
        except Exception:
            pass
    body = text.split("\n---\n", 1)[1] if text.startswith("---\n") and "\n---\n" in text else text
    return len(body.split())


def sections_of(text: str):
    """[(heading, [lines])] for each `## ` section after the frontmatter."""
    body = text.split("\n---\n", 1)[1] if text.startswith("---\n") and "\n---\n" in text else text
    out, current = [], None
    for line in body.splitlines():
        if line.startswith("## "):
            current = (line[3:].strip(), [])
            out.append(current)
        elif current is not None:
            current[1].append(line)
    return out


def is_card(text: str) -> bool:
    names = {h.lower() for h, _l in sections_of(text)}
    return "route" in names and "rules" in names


def moved_table(root: Path) -> dict:
    path = root / MAP_REL
    if not path.is_file():
        return {}
    with open(path, newline="", encoding="utf-8") as handle:
        return {r["old_path"]: r["new_path"] for r in csv.DictReader(handle)}


def resolve(root: Path, card_dir: str, target: str, table: dict) -> str:
    """direct, moved (through the table) or missing."""
    rel = target if re.match(r"^_[a-z_]+_/", target) else os.path.normpath(os.path.join(card_dir, target)).replace(os.sep, "/")
    if (root / rel).exists():
        return "direct"
    new = table.get(rel)
    return "moved" if new and (root / new).exists() else "missing"


def check_card(root: Path, rel: str, text: str, now: datetime, a, table: dict) -> dict:
    """Findings (error codes) and warnings for one card, plus counts. Nothing from the card's text is returned."""
    errors, warnings = Counter(), Counter()
    counts = Counter()
    words = body_words(text)
    if words > a.card_words:
        errors["card-too-long"] += 1
    secs = sections_of(text)
    names = [h for h, _l in secs]
    lowered = [n.lower() for n in names]
    for name in SECTIONS:
        if name.lower() not in lowered:
            errors["missing-section"] += 1
    present = [n.lower() for n in names if n.lower() in {s.lower() for s in SECTIONS}]
    if present != [s.lower() for s in SECTIONS if s.lower() in present]:
        errors["section-order"] += 1
    for n in names:
        if n.lower() not in {s.lower() for s in SECTIONS} and n.lower() != "changelog":
            errors["unexpected-section"] += 1                      # an Errata section grows, a card is rewritten in place
    by = {h.lower(): lines for h, lines in secs}
    route = [l for l in by.get("route", []) if re.match(r"^\d+\.\s+\S", l)]
    if by.get("route") is not None and not route:
        errors["route-empty"] += 1
    if len(route) > LIMITS["Route"]:
        errors["route-too-long"] += 1
    rules_ids, rules = [], []
    for line in by.get("rules", []):
        if not line.strip():
            continue
        m = RULE.match(line)
        if not m:
            errors["rule-format"] += 1
            continue
        rid, status, date, _t, evidence = m.groups()
        rules.append((rid, status, date, evidence))
        rules_ids.append(rid)
        if status == "superseded":
            errors["rule-superseded-left"] += 1
        for cited in re.split(r"[;,]\s*|\s+", evidence.strip()):
            if cited and not cited.startswith("_records_/"):
                errors["evidence-not-a-record"] += 1
        if status == "unverified" and (now.date() - datetime.strptime(date, "%Y-%m-%d").date()).days > a.stale_days:
            warnings["stale-unverified"] += 1                       # older than --stale-days whole days: 14 old is still fine
    if len(rules) > LIMITS["Rules"]:
        errors["too-many-rules"] += 1
    if len(set(rules_ids)) != len(rules_ids):
        errors["rule-id-repeats"] += 1
    if by.get("rules") is not None and not rules:
        errors["rules-empty"] += 1
    fails = [l for l in by.get("failures", []) if l.strip().startswith("- ")]
    if len(fails) > LIMITS["Failures"]:
        errors["too-many-failures"] += 1
    qs = [l for l in by.get("open questions", []) if l.strip().startswith("- ")]
    if len(qs) > LIMITS["Open questions"]:
        errors["too-many-questions"] += 1
    errors["open-question-without-test"] += sum(1 for q in qs if not re.search(r"\btest:", q, re.I))
    numbers = [l for l in by.get("numbers", []) if l.strip()]
    if by.get("numbers") is not None and not (len(numbers) == 1 and re.search(r"\d", PATH.sub("", numbers[0])) and "_records_/" in numbers[0]):
        errors["numbers-line"] += 1
    links = [m for l in by.get("links", []) for m in LINK.findall(l)]
    if len(links) > LIMITS["Links"]:
        errors["too-many-links"] += 1
    card_dir = os.path.dirname(rel)
    for token in sorted(set(PATH.findall(text)) | {t for t in LINK.findall(text) if not re.match(r"^[a-z]+:", t)}):
        how = resolve(root, card_dir, token, table)
        counts["citations_" + how] += 1
        if how == "missing":
            errors["unresolved-path"] += 1
        elif how == "moved":
            warnings["cites-moved-path"] += 1
    counts.update(rules_total=len(rules), rules_verified=sum(1 for r in rules if r[1] == "verified"),
                  rules_unverified=sum(1 for r in rules if r[1] == "unverified"), words=words)
    return {"path": rel, "errors": {k: v for k, v in errors.items() if v}, "warnings": {k: v for k, v in warnings.items() if v},
            "counts": dict(counts)}


def activity_of(rel: str) -> str:
    parts = rel.split("/")
    return parts[1] if len(parts) > 2 and parts[0] == "_activities_" else rel


def git_lines(root: Path, *args) -> list[str]:
    out = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)
    if out.returncode:
        raise OSError(f"git {args[0]} failed: {out.stderr.strip()[:120]}")
    return [l for l in out.stdout.splitlines() if l]


def report(results, skipped, a, fmt, title) -> int:
    failing = [r for r in results if r["errors"] or (a.stale_fail and r["warnings"].get("stale-unverified"))]
    total = Counter()
    for r in results:
        for k, v in r["errors"].items():
            total["error:" + k] += v
        for k, v in r["warnings"].items():
            total["warning:" + k] += v
        total.update({k: v for k, v in r["counts"].items() if k != "words"})
    summary = {"checked": len(results), "failing": len(failing), "skipped_not_cards": skipped, "totals": dict(total),
               "cards": [{"activity": activity_of(r["path"]), "errors": r["errors"], "warnings": r["warnings"], "counts": r["counts"]} for r in results]}
    if total["rules_total"]:
        summary["verified_share_percent"] = round(100.0 * total["rules_verified"] / total["rules_total"], 1)
    if fmt == "json":
        print(json.dumps(summary, indent=1, sort_keys=True))
    else:
        print(f"{title}: {len(results)} card(s) checked, {len(failing)} failing, {skipped} page(s) not a card yet")
        for r in results:
            codes = [f"{k} {v}" for k, v in sorted(r["errors"].items())] + [f"warn {k} {v}" for k, v in sorted(r["warnings"].items())]
            print(f"  {activity_of(r['path'])}: " + ("ok" if not codes else ", ".join(codes)) + f" ({r['counts'].get('words', 0)} words)")
        if total["rules_total"]:
            print(f"rules: {total['rules_total']} (verified {total['rules_verified']}, unverified {total['rules_unverified']}, "
                  f"verified share {summary['verified_share_percent']}%, stale over {a.stale_days} days {total['warning:stale-unverified']})")
        print(f"citations: direct {total['citations_direct']}, via moved-paths {total['citations_moved']}, unresolved {total['citations_missing']}")
    return 1 if failing else 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=str(HERE.parent.parent), help="the repository (default: the one holding this tool)")
    p.add_argument("--now", default="", help="the instant to judge at, ISO 8601 UTC (default: now)")
    p.add_argument("--stale-days", type=int, default=14)
    p.add_argument("--card-words", type=int, default=300)
    p.add_argument("--stale-fail", action="store_true", help="a stale unverified rule fails check and changed too")
    p.add_argument("--format", choices=("text", "json"), default="text")
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check")
    c.add_argument("paths", nargs="+")
    ch = sub.add_parser("changed")
    ch.add_argument("--staged", action="store_true")
    ch.add_argument("--base", default="")
    sub.add_parser("daily")
    a = p.parse_args(argv)
    root = Path(a.root).resolve()
    try:
        now = datetime.fromisoformat(a.now.replace("Z", "+00:00")) if a.now else datetime.now(timezone.utc)
        now = now if now.tzinfo else now.replace(tzinfo=timezone.utc)
    except ValueError:
        print("playbook_check: --now is not ISO 8601", file=sys.stderr)
        return 2
    table, results, skipped = moved_table(root), [], 0
    try:
        if a.cmd == "check":
            for name in a.paths:
                path = Path(name) if os.path.isabs(name) else root / name
                rel = path.resolve().relative_to(root).as_posix()
                results.append(check_card(root, rel, path.read_text(encoding="utf-8"), now, a, table))
        elif a.cmd == "changed":
            if a.staged == bool(a.base):
                print("playbook_check: changed needs exactly one of --staged or --base REV", file=sys.stderr)
                return 2
            diff = ["diff", "--cached", "--name-only", "--diff-filter=ACMR"] if a.staged else ["diff", "--name-only", "--diff-filter=ACMR", a.base]
            before = "HEAD" if a.staged else a.base
            for rel in git_lines(root, *diff, "--", "_activities_"):
                if not re.fullmatch(r"_activities_/[^/]+/INDEX\.md", rel):
                    continue
                text = (git_lines_text(root, f":{rel}") if a.staged else (root / rel).read_text(encoding="utf-8"))
                was = git_lines_text(root, f"{before}:{rel}", allow_missing=True)
                if is_card(text):
                    results.append(check_card(root, rel, text, now, a, table))
                elif was and is_card(was):
                    results.append({"path": rel, "errors": {"card-shape-lost": 1}, "warnings": {}, "counts": {}})
                else:
                    skipped += 1
        else:
            for path in sorted((root / "_activities_").glob("*/INDEX.md")):
                rel = path.relative_to(root).as_posix()
                text = path.read_text(encoding="utf-8")
                if is_card(text):
                    results.append(check_card(root, rel, text, now, a, table))
                else:
                    skipped += 1
    except (OSError, ValueError) as error:
        print(f"playbook_check: cannot read: {error}", file=sys.stderr)
        return 2
    code = report(results, skipped, a, a.format, {"check": "playbook-check", "changed": "playbook-check (changed)", "daily": "playbook daily"}[a.cmd])
    if a.cmd == "daily" and any(r["warnings"].get("stale-unverified") for r in results):
        code = 1                                                   # the coach's daily run alarms on stale rules
    return code


def git_lines_text(root: Path, spec: str, allow_missing: bool = False) -> str:
    out = subprocess.run(["git", "-C", str(root), "show", spec], capture_output=True, text=True)
    if out.returncode:
        if allow_missing:
            return ""
        raise OSError(f"git show {spec} failed")
    return out.stdout


if __name__ == "__main__":
    sys.exit(main())
