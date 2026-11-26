"""The serves exempt list: parser, validation and the dated baseline, read by strategy_conformance.py (owner of the parser: the Toolsmith;
owner of the content: the Strategist - one line per regular in `_records_/<date>/strategy/serves-exempt-list.csv`, Steer A's ruling of 2026-11-25).

Columns: regular_id, class, serves, reason, decided_utc, review_utc, and an OPTIONAL kind (blank or `regular`: the id is a roster regular; `oneoff`: a
one-off unit the roster does not hold - a test, a probe, a single reading - which may be on the list without a roster row and is held to its review date). class is
  plan    the regular feeds a plan item with a ledger row (serves: PL ids)           - counts as served
  income  its claims are daily claims income, ledger line PL-19 (serves: PL ids)      - counts as served
  exempt  it only looks (a read; presses nothing that claims); serves names no plan item - leaves the denominator, with its reason

Validation, all read-only: every regular in the roster (`_tools_/regulars.json`) is on the list, no listed id is outside the roster, no
duplicate, a valid class and dates, every plan or income serves part a PL id with a ledger row, no exempt line names a plan item. Warnings: a
review date that has passed, a roster `serves` that differs from the list's (units carry the roster's, so the figure by unit serves and the
figure by this list drift apart until the roster follows). The list is dated, never silently re-based: an accepted baseline
(`_tools_/state/serves-exempt-baseline.json`, written ONLY by `strategy_conformance.py --accept-exempt-list`) is compared on every run;
a line whose class, serves or reason changed must carry a new decided_utc, and a changed list is printed as +added -removed ~edited
until it is accepted. No finding ever contains a reason text.
"""
from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path

LIST_NAME = "serves-exempt-list.csv"
BASELINE_REL = "_tools_/state/serves-exempt-baseline.json"
HEADER = ["regular_id", "class", "serves", "reason", "decided_utc", "review_utc"]
CLASSES = ("plan", "income", "exempt")
KINDS = ("regular", "oneoff")
PLAN_ID = re.compile(r"^PL-\d{1,3}$")
STAMP_FORMATS = ("%Y-%m-%dT%H:%MZ", "%Y-%m-%dT%H:%M:%SZ")


def parse_stamp(text: str):
    for fmt in STAMP_FORMATS:
        try:
            return datetime.strptime((text or "").strip(), fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def find(root: Path):
    """The newest `_records_/<date>/strategy/serves-exempt-list.csv` (by the date folder), or None."""
    records = root / "_records_"
    if not records.is_dir():
        return None
    for folder in sorted((p for p in records.iterdir() if p.is_dir()), key=lambda p: p.name, reverse=True):
        candidate = folder / "strategy" / LIST_NAME
        if candidate.is_file():
            return candidate
    return None


def serves_parts(text: str) -> list[str]:
    return [p for p in re.split(r"[\s,;]+", (text or "").strip()) if p]


def parse(path: Path):
    """(rows, errors, sha256): the list's rows in file order and the parse errors (codes with regular ids, never a reason text)."""
    raw = path.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    errors, rows = [], []
    reader = csv.DictReader(raw.decode("utf-8", errors="replace").splitlines())
    missing = [c for c in HEADER if c not in (reader.fieldnames or [])]
    if missing:
        return [], [f"header lacks column(s): {', '.join(missing)}"], sha
    seen = set()
    for number, record in enumerate(reader, start=2):
        row = {c: (record.get(c) or "").strip() for c in HEADER}
        row["kind"] = (record.get("kind") or "").strip().lower() or "regular"
        ident = row["regular_id"]
        if not ident:
            errors.append(f"line {number}: regular_id is empty")
            continue
        if ident in seen:
            errors.append(f"{ident}: listed twice")
            continue
        seen.add(ident)
        if row["kind"] not in KINDS:
            errors.append(f"{ident}: kind {row['kind']} is not one of {', '.join(KINDS)} (blank means regular)")
        if row["class"] not in CLASSES:
            errors.append(f"{ident}: class {row['class'] or '(empty)'} is not one of {', '.join(CLASSES)}")
        if not row["serves"]:
            errors.append(f"{ident}: serves is empty")
        if not row["reason"]:
            errors.append(f"{ident}: reason is empty")
        if parse_stamp(row["decided_utc"]) is None:
            errors.append(f"{ident}: decided_utc is not YYYY-MM-DDTHH:MMZ")
        if row["review_utc"] and parse_stamp(row["review_utc"]) is None:
            errors.append(f"{ident}: review_utc is not YYYY-MM-DDTHH:MMZ")
        rows.append(row)
    return rows, errors, sha


def roster(root: Path):
    """({regular id: serves}, error): the roster beside the tool in this repository."""
    path = root / "_tools_" / "regulars.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))["regulars"]
        return {str(r["id"]): str(r.get("serves", "")) for r in data if r.get("id")}, ""
    except (OSError, ValueError, KeyError, TypeError):
        return {}, f"the roster {path.name} could not be read"


def validate(rows, parse_errors, roster_serves: dict, ledger_ids, now: datetime) -> dict:
    """Errors block (alarm), warnings inform. ledger_ids None means the ledger could not be read: the id check is skipped and says so."""
    errors, warnings = list(parse_errors), []
    listed = {r["regular_id"]: r for r in rows}
    unlabeled = sorted(set(roster_serves) - set(listed))
    stale = sorted(i for i in listed if i not in roster_serves and listed[i].get("kind") != "oneoff") if roster_serves else []
    oneoffs = sorted(i for i, r in listed.items() if r.get("kind") == "oneoff")
    if roster_serves:
        errors += [f"{i}: in the roster and not on the list (unlabeled)" for i in unlabeled]
        errors += [f"{i}: on the list and not in the roster" for i in stale]
    for ident in oneoffs:
        if ident in roster_serves:
            warnings.append(f"{ident}: listed as a one-off but the roster holds it (make it a regular line)")
    for ident, row in listed.items():
        parts = serves_parts(row["serves"])
        plan_ids = [p for p in parts if PLAN_ID.match(p)]
        if row["class"] in ("plan", "income"):
            if not plan_ids or len(plan_ids) != len(parts):
                errors.append(f"{ident}: a {row['class']} line's serves must be plan item ids (PL-n) only")
            elif ledger_ids is not None:
                errors += [f"{ident}: {p} has no row in the forecast ledger" for p in plan_ids if p not in ledger_ids]
        elif row["class"] == "exempt" and plan_ids:
            errors.append(f"{ident}: an exempt line must not name a plan item")
        review = parse_stamp(row["review_utc"])
        if review is not None and review < now:
            warnings.append(f"{ident}: review date has passed")
    mismatched = sorted(i for i, r in listed.items() if r["class"] in ("plan", "income") and i in roster_serves
                        and sorted(serves_parts(roster_serves[i])) != sorted(serves_parts(r["serves"])))
    if mismatched:
        warnings.append(f"roster serves differs from the list for {len(mismatched)} regular(s): {', '.join(mismatched[:12])}"
                        + (" ..." if len(mismatched) > 12 else ""))
    classes = {c: sum(1 for r in rows if r["class"] == c) for c in CLASSES}
    return {"errors": errors, "warnings": warnings, "regulars_listed": len(rows), "classes": classes, "roster": len(roster_serves),
            "unlabeled": unlabeled, "stale": stale, "oneoff": oneoffs, "roster_serves_mismatch": mismatched,
            "ledger_checked": ledger_ids is not None}


def _line_key(row: dict) -> dict:
    return {"class": row["class"], "kind": row.get("kind", "regular"), "serves": " ".join(serves_parts(row["serves"])),
            "reason_sha": hashlib.sha256(row["reason"].encode("utf-8")).hexdigest()[:12], "decided_utc": row["decided_utc"]}


def baseline_path(root: Path) -> Path:
    return root / BASELINE_REL


def compare_baseline(root: Path, rows) -> dict:
    """The list against the accepted baseline: nothing silent. {state, accepted_at, added, removed, edited, errors, warnings}."""
    path = baseline_path(root)
    if not path.is_file():
        return {"state": "none", "accepted_at": "", "added": [], "removed": [], "edited": [], "errors": [], "warnings": []}
    try:
        base = json.loads(path.read_text(encoding="utf-8"))
        lines = base["lines"]
        accepted = parse_stamp(base.get("accepted_at", ""))
    except (OSError, ValueError, KeyError, TypeError):
        return {"state": "unreadable", "accepted_at": "", "added": [], "removed": [], "edited": [],
                "errors": [f"the baseline {BASELINE_REL} could not be read"], "warnings": []}
    now_lines = {r["regular_id"]: _line_key(r) for r in rows}
    added = sorted(set(now_lines) - set(lines))
    removed = sorted(set(lines) - set(now_lines))
    edited = sorted(i for i in now_lines if i in lines and {k: now_lines[i][k] for k in ("class", "kind", "serves", "reason_sha")}
                    != {k: lines[i].get(k, "regular" if k == "kind" else None) for k in ("class", "kind", "serves", "reason_sha")})
    errors, warnings = [], []
    for ident in edited:
        old, new = parse_stamp(lines[ident].get("decided_utc", "")), parse_stamp(now_lines[ident]["decided_utc"])
        if new is None or (old is not None and new <= old):
            errors.append(f"{ident}: changed since the accepted baseline without a newer decided_utc")
    for ident in added:
        new = parse_stamp(now_lines[ident]["decided_utc"])
        if accepted is not None and new is not None and new < accepted:
            warnings.append(f"{ident}: added with a decided_utc before the baseline was accepted")
    state = "unchanged" if not (added or removed or edited) else "changed"
    return {"state": state, "accepted_at": base.get("accepted_at", ""), "added": added, "removed": removed, "edited": edited,
            "errors": errors, "warnings": warnings}


def accept_baseline(root: Path, rows, list_rel: str, sha: str, now: datetime) -> str:
    """Record the list as the accepted baseline (the one write this feature makes, on the explicit flag); returns the path written."""
    path = baseline_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    body = {"version": 1, "accepted_at": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "list": list_rel, "sha256": sha,
            "lines": {r["regular_id"]: _line_key(r) for r in rows}}
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=".exempt-baseline-")
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        json.dump(body, fh, indent=1, sort_keys=True)
        fh.write("\n")
    os.replace(tmp, path)
    return str(path)
