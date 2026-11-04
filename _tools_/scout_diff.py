#!/usr/bin/env python3
"""Scout diff - the diff of the perception layer as a program.

Implements the Phase 2 tool design of the perception-driven queue
(_conventions_/local-conventions/perception-driven-queue.md,
sections 5, 6 and 9). A scout pass observes the game and writes
its observed items into the day observation file; this tool reads
that observation, diffs it against the modelled work - the
regulars profile library, the _activities_ roster with its
candidate register, and the pool itself - and produces four
outputs in an output directory:

  1. the enqueue plan (JSONL, one queue.py enqueue argument set
     per line) for the triggered execution units and for the
     exploration units of new candidates;
  2. the candidate filings - one provisional _activities_ profile
     draft per unknown item or unmatched label not already in the
     register;
  3. the coverage report - items observed, actionable, queued,
     already satisfied, not actionable with reasons, candidates,
     unexplained red dots, and the day unmatched_labels printed
     in full (an empty list is printed as empty, never omitted);
     plus the observation frontmatter day counters (passes
     completed, items observed, red dots seen, explained and
     unexplained), reported separately from the classified
     counts, and the per-pass red-dot accounting sections of
     a narrative observation, reconciled section total
     against frontmatter counter. When no structured item
     was parsed at all, the headline items and unexplained
     figures fall back to those
     frontmatter counts (basis recorded as frontmatter-fallback,
     classified counts kept alongside), so a narrative-only
     observation never reads as zero unexplained when its own
     frontmatter says otherwise; when the frontmatter carries
     no unexplained counter either, the headline unexplained
     figure falls back one more tier to the sum of the
     narrative accounting sections stating a count (basis
     recorded as narrative-fallback, with the caveat that
     chained passes may re-state the same dot, so the sum is
     a section total, not a distinct-dot count); a structured
     observation is never overridden, and the narrative seen
     total is never used as items observed, because seen
     counts red-dot signals, not observed items;
  4. the promotion proposals - one entry per registered
     candidate with a completed exploration unit in the pool,
     naming the exploration evidence and the decision owed
     (promote, reject, or keep exploring). A proposal never
     applies itself: promotion or rejection is a metadata edit
     made by the knowledge organizer or the owner, never by
     this tool, and the proposal never blocks the next
     exploration unit the plan enqueues;
  5. the round-summary section - the perception coverage
     scoreboard as one short section, written to be pasted
     verbatim into the day round summary (roadmap Phase 3).
     It carries no new numbers: every figure is copied from
     the coverage counts computed above, including the
     frontmatter day counters when the observation carries
     them, and when the pool was not read (--root absent) it
     says the promotion proposals were not checked instead
     of reporting zero as a finding.

Without --apply the tool is a dry run: it writes its outputs and
changes nothing in any pool. With --apply it feeds the plan's
enqueue entries to _tools_/queue.py enqueue, one call per unit, so
every unit it creates passes the same validation as a manual
enqueue - and --apply refuses to run unless the pool root is
given explicitly with --root.

Idempotency: produced units dedupe on (regular, planned_for)
exactly as sync and plan do, and dynamic units carry their
source observation item (date, surface, label) in their window
text, which the tool checks before enqueueing. A second run over
the same observation reports every entry as already queued and
applies zero new units.

Priority: the formula of section 5 of the perception design -
deadline pressure times value over expected duration - mapped
onto the queue priority classes 1 to 4. Deadline pressure is 1
with no deadline and rises to 8 as the time left approaches the
band of one unit duration plus one retry; inside that band the
unit is priority 1, expiry-critical. Value is the base 10 log of
the largest figure the observation shows for the item, or a
state default when it shows none. Exploration units are fixed
at priority 2 under the design.

Usage:
  scout_diff.py --observation FILE [--date YYYY-MM-DD]
                [--out DIR] [--root POOL] [--repo DIR]
                [--regulars FILE] [--ledger FILE]
                [--now ISO] [--apply] [--format text|json]

Pool reads (the dedupe checks and the learned estimates) happen
only when --root names a pool; without it the diff runs against
an empty pool view. The observation, regulars, activities roster
and ledger default to the repository this tool lives in
(override with --repo).
"""

import argparse
import importlib.util
import json
import math
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))


def _load_queue():
    spec = importlib.util.spec_from_file_location(
        "lastwar_queue", os.path.join(TOOLS_DIR, "queue.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


Q = _load_queue()
parse_iso = Q.parse_iso
iso = Q.iso
LOCAL_TZ = Q.LOCAL_TZ

ACTIONABLE_STATES = ("claimable", "doable")
KNOWN_STATES = ACTIONABLE_STATES + ("in-progress", "locked",
                                    "info-only")
VALUE_DEFAULTS = {"claimable": 2.0, "doable": 1.5,
                  "in-progress": 1.0, "locked": 1.0, "info-only": 0.5}


def now_utc():
    return datetime.now(timezone.utc).replace(microsecond=0)


# ---------------------------------------------------------------------
# Observation parsing
# ---------------------------------------------------------------------

def _clean_value(text):
    text = text.strip()
    if len(text) >= 2 and text.startswith('"') and \
            text.endswith('"'):
        return text[1:-1]
    return text


def _parse_items_block(lines, start):
    """Parse one observed_items block sequence starting just after
    its key line. Returns (items, next_index)."""
    items = []
    current = None
    i = start
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        m = re.match(r"^(\s*)- (.*)$", line)
        if m:
            current = {}
            items.append(current)
            rest = m.group(2)
            fm = re.match(r"^([a-z_]+): (.*)$", rest)
            if fm:
                current[fm.group(1)] = _clean_value(fm.group(2))
            i += 1
            continue
        fm = re.match(r"^\s+([a-z_]+): (.*)$", line)
        if fm and current is not None:
            current[fm.group(1)] = _clean_value(fm.group(2))
            i += 1
            continue
        break
    return items, i


def _parse_labels_block(lines, start):
    """Parse one unmatched_labels value - an inline flow list, a
    plain scalar, or a block list of scalars."""
    labels = []
    i = start
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^\s*- (.+)$", line)
        if m and not line.lstrip().startswith("- surface"):
            labels.append(m.group(1).strip())
            i += 1
            continue
        break
    return labels, i


def parse_observation_text(text):
    """Collect every observed_items block and unmatched_labels list
    in a Markdown or YAML text - frontmatter, fenced blocks and
    body blocks all count, because a day observation file is
    appended to by every pass of the day."""
    items, labels = [], []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped.startswith("observed_items:"):
            found, i = _parse_items_block(lines, i + 1)
            items.extend(found)
            continue
        if stripped.startswith("unmatched_labels:"):
            rest = stripped.split(":", 1)[1].strip()
            if rest.startswith("["):
                inner = rest.strip("[]").strip()
                if inner:
                    labels.extend(x.strip() for x in
                                  inner.split(",") if x.strip())
                i += 1
                continue
            if rest and rest.lower() not in ("none", "empty"):
                labels.append(rest)
                i += 1
                continue
            if not rest:
                found, i = _parse_labels_block(lines, i + 1)
                labels.extend(found)
                continue
            i += 1
            continue
        i += 1
    seen = set()
    unique = []
    for item in items:
        key = (item.get("surface", ""), item.get("label", ""),
               item.get("state", ""))
        if key not in seen:
            seen.add(key)
            unique.append(item)
    return unique, sorted(set(labels))


def parse_observation_json(doc):
    items, labels = [], []

    def walk(node):
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "observed_items" and \
                        isinstance(value, list):
                    items.extend(v for v in value
                                 if isinstance(v, dict))
                elif key == "unmatched_labels" and \
                        isinstance(value, list):
                    labels.extend(str(v) for v in value)
                else:
                    walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)

    walk(doc)
    return items, sorted(set(labels))


def load_observation(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if path.endswith(".json"):
        return parse_observation_json(json.loads(text))
    try:
        doc = json.loads(text)
        if isinstance(doc, dict):
            return parse_observation_json(doc)
    except ValueError:
        pass
    return parse_observation_text(text)


# ---------------------------------------------------------------------
# Observation day counters - the observation's own accounting
# ---------------------------------------------------------------------

DAY_COUNTER_KEYS = ("passes_completed", "items_observed",
                    "red_dots_seen", "red_dots_explained",
                    "unexplained_red_dots")


def _counter_value(value):
    """A day counter is a non-negative int, or None when absent.

    Absent or malformed values read as None, never as zero: an
    absent counter is unknown, not a finding.
    """
    if isinstance(value, bool):
        return None
    if isinstance(value, int) and value >= 0:
        return value
    if isinstance(value, float) and value.is_integer() \
            and value >= 0:
        return int(value)
    if isinstance(value, str) and value.strip().isdigit():
        return int(value.strip())
    return None


def day_counters_from_fields(fields):
    return {key: _counter_value(fields.get(key))
            for key in DAY_COUNTER_KEYS}


def load_day_counters(path):
    """Read the observation's own day counters, if it carries any.

    Text observations carry them in the leading frontmatter
    block (the design's day counters); JSON observations carry
    them as top-level keys. This reads only the observation's
    own accounting - it classifies nothing, enqueues nothing
    and files nothing, so a narrative-only observation keeps
    its dots visible instead of collapsing to a classified
    zero.
    """
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    try:
        doc = json.loads(text)
    except ValueError:
        doc = None
    if isinstance(doc, dict):
        return day_counters_from_fields(doc)
    fields, _ = Q.parse_frontmatter(text)
    return day_counters_from_fields(fields)


# ---------------------------------------------------------------------
# Narrative red-dot accounting - the per-pass accounting sections
# ---------------------------------------------------------------------

ACCOUNTING_KEYS = ("seen", "explained", "unexplained")
ACCOUNTING_FRONTMATTER = {
    "seen": "red_dots_seen",
    "explained": "red_dots_explained",
    "unexplained": "unexplained_red_dots",
}
_ACCOUNTING_LINE = re.compile(
    r"^-\s*(seen|explained|unexplained)"
    r"(?:\s+red\s+dots?)?\s*:?\s*(\d+)\b",
    re.IGNORECASE)


def parse_narrative_accounting(text):
    """Per-pass red-dot accounting sections of a narrative
    observation, in file order. A section starts at a heading
    naming red dot accounting and ends at the next heading;
    its Seen, Explained and Unexplained lines carry that
    pass's own counts, in either the bare form ("Seen 3:")
    or the spelled-out form ("Unexplained red dots: 0.").
    A count a section does not state reads as None, never
    as zero - a line naming a dot without a number (for
    example "Unexplained: the Alliance Wars dot") states
    no count and invents none, so the same dot re-stated
    by a later pass is never counted twice by inference -
    and a carried-forward line (for example "Carried
    unexplained from ...") is not a count line, so carried
    dots are never double-counted. Structured items are
    untouched: this reads the narrative's own accounting
    only, so the coverage report can reconcile it against
    the frontmatter day counters instead of presenting
    either figure unexamined."""
    sections = []
    current = None
    for raw in text.splitlines():
        stripped = raw.strip()
        if stripped.startswith("#"):
            if "red dot accounting" in stripped.lower():
                current = {key: None for key in ACCOUNTING_KEYS}
                sections.append(current)
            else:
                current = None
            continue
        if current is None:
            continue
        m = _ACCOUNTING_LINE.match(stripped)
        if m:
            current[m.group(1).lower()] = int(m.group(2))
    return sections


def narrative_accounting_summary(sections, day_counters):
    """Totals and frontmatter reconciliation for parsed
    accounting sections. A total is the sum over the sections
    that state that count, or None when no section states
    it; reconciliation per count is matches when the total
    equals the frontmatter counter, differs by N when both
    are stated and unequal, and not comparable otherwise."""
    totals = {}
    for key in ACCOUNTING_KEYS:
        stated = [s[key] for s in sections if s[key] is not None]
        totals[key] = sum(stated) if stated else None
    reconciliation = {}
    for key in ACCOUNTING_KEYS:
        front = day_counters.get(ACCOUNTING_FRONTMATTER[key])
        total = totals[key]
        if front is None or total is None:
            reconciliation[key] = "not comparable"
        elif total == front:
            reconciliation[key] = "matches"
        else:
            reconciliation[key] = f"differs by {total - front:+d}"
    return {"sections": sections, "totals": totals,
            "reconciliation": reconciliation}


def load_narrative_accounting(path):
    """Narrative accounting summary for one observation file.
    JSON observations carry no markdown accounting sections,
    so they read as an empty summary, never as an error."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    try:
        doc = json.loads(text)
    except ValueError:
        doc = None
    if isinstance(doc, dict):
        return narrative_accounting_summary([], {})
    return narrative_accounting_summary(
        parse_narrative_accounting(text),
        load_day_counters(path))


# ---------------------------------------------------------------------
# Roster - regulars, activities with their states, the ledger
# ---------------------------------------------------------------------

def normalize(text):
    text = re.sub(r"[^a-z0-9]+", "-", str(text).lower())
    return re.sub(r"-+", "-", text).strip("-")


def slugify(label):
    """A provisional folder name for a candidate label - 2 to 4
    kebab words, the repository instance naming rule."""
    words = [w for w in normalize(label).split("-") if w][:4]
    if not words:
        return "unknown-candidate"
    if len(words) == 1:
        words.append("task")
    return "-".join(words)


def load_regulars(path):
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    return {r["id"]: r for r in doc.get("regulars", [])}


def load_roster(repo):
    """The _activities_ roster - folder name to its frontmatter
    title and status. The candidate register lives here: a folder
    whose status is candidate or exploring is a filed candidate,
    rejected is kept against rediscovery."""
    roster = {}
    base = os.path.join(repo, "_activities_")
    if not os.path.isdir(base):
        return roster
    for name in sorted(os.listdir(base)):
        index = os.path.join(base, name, "INDEX.md")
        if not os.path.isfile(index):
            continue
        with open(index, encoding="utf-8") as fh:
            fields, _ = Q.parse_frontmatter(fh.read())
        roster[name] = {"title": fields.get("title", name),
                        "status": fields.get("status", "")}
    return roster


def load_ledger_regulars(path, regular_ids):
    """The regulars the daily collection ledger names as producing
    units - read from its numbered lines, best effort."""
    if not path or not os.path.isfile(path):
        return set()
    found = set()
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if re.match(r"^\d+\. ", line):
                for rid in regular_ids:
                    if re.search(r"\b" + re.escape(rid) + r"\b",
                                 line):
                        found.add(rid)
    return found


# ---------------------------------------------------------------------
# Classification and priority
# ---------------------------------------------------------------------

def extract_value(item):
    text = str(item.get("est_value_or_score", ""))
    numbers = []
    for m in re.finditer(r"\d[\d,]*(?:\.\d+)?", text):
        try:
            numbers.append(float(m.group(0).replace(",", "")))
        except ValueError:
            pass
    if numbers:
        biggest = max(numbers)
        if biggest > 0:
            return math.log10(biggest)
    return VALUE_DEFAULTS.get(item.get("state", ""), 1.0)


def compute_priority(item, est_minutes, stamp):
    """The priority formula of the perception design, section 5,
    mapped onto the queue classes. Returns (priority, score)."""
    deadline = parse_iso(item.get("deadline", ""))
    pressure = 1.0
    if deadline:
        time_left = max(1.0, (deadline - stamp).total_seconds()
                        / 60.0)
        band = 2.0 * est_minutes        # one unit plus one retry
        if time_left <= band:
            return 1, float("inf")
        pressure = min(8.0, max(1.0, (8.0 * band) / time_left))
    score = pressure * extract_value(item) / max(1, est_minutes)
    if score >= 1.0:
        return 2, score
    if score >= 0.25:
        return 3, score
    return 4, score


def redline_blocked(item):
    text = str(item.get("redline_check", "")).lower()
    return text.startswith("blocked") or "owner-needed" in text \
        or "owner needed" in text


def classify(item, regulars, roster, reg_by_activity):
    """One observed item into exactly one class. Returns a dict
    with the class and the reason or owner where it applies."""
    label = str(item.get("label", "")).strip()
    state = str(item.get("state", "")).strip()
    suggested = str(item.get("suggested_unit", "")).strip()
    if not label or state not in KNOWN_STATES:
        return {"class": "unexplained",
                "reason": "missing label or unknown state"}
    if suggested and suggested != "new" and suggested in regulars:
        owner = suggested
    elif suggested and suggested != "new" and \
            suggested in reg_by_activity:
        owner = reg_by_activity[suggested]
    else:
        slug = slugify(label)
        if slug in roster:
            entry = roster[slug]
            if entry["status"] == "rejected":
                return {"class": "not-actionable", "owner": "",
                        "reason": "candidate previously rejected, "
                                  "kept against rediscovery"}
            if entry["status"] in ("candidate", "exploring"):
                return {"class": "candidate", "slug": slug,
                        "known_candidate": True}
            owner = reg_by_activity.get(slug, "")
            if not owner:
                return {"class": "not-actionable", "owner": "",
                        "reason": "profiled in the roster with no "
                                  "producing regular"}
        else:
            return {"class": "candidate", "slug": slug,
                    "known_candidate": False}
    if redline_blocked(item):
        return {"class": "not-actionable", "owner": owner,
                "reason": "red line - " +
                          str(item.get("redline_check", ""))}
    if state in ACTIONABLE_STATES:
        return {"class": "actionable", "owner": owner}
    reason = {"in-progress": "already under way",
              "locked": "locked or not yet open - " +
                        str(item.get("redline_check", "")),
              "info-only": "read for the record, day evidence"
              }[state]
    return {"class": "not-actionable", "owner": owner,
            "reason": reason}


# ---------------------------------------------------------------------
# Pool reads - dedupe exactly as sync and plan do
# ---------------------------------------------------------------------

def pool_units(root):
    units = []
    if not root:
        return units
    for state in Q.STATES:
        units.extend(Q.list_units(root, state))
    return units


def marker_for(date, item):
    return (f"scout {date} - {item.get('surface', '')} - "
            f"{item.get('label', '')}")


def find_existing(units, regular, planned_iso, marker):
    """An existing unit covering this entry - by the (regular,
    planned_for) invariant, or by the dynamic source marker in
    its window text (same date, surface and label)."""
    for f in units:
        window = str(f.get("window", ""))
        if marker and marker in window:
            return f
        if planned_iso and f.get("regular") == regular and \
                f.get("planned_for") == planned_iso:
            return f
    return None


# ---------------------------------------------------------------------
# Candidate filing draft
# ---------------------------------------------------------------------

def candidate_draft(slug, label, surface, clues, stamp, date):
    title = " ".join(w.capitalize() for w in slug.split("-"))
    lines = ["---",
             f"title: {title}",
             f"created: {iso(stamp)}",
             f"modified: {iso(stamp)}",
             "level: L1",
             "version: 0.1.0",
             "description: Provisional candidate profile filed by "
             "the scout diff - mechanism not yet learned",
             "status: candidate",
             "grounded_in:",
             f"  - source: scout observation of {date}, surface "
             f"{surface}",
             "---",
             "",
             f"# {title}",
             "",
             "## What is known",
             "",
             f"- On-screen text transcribed - {label}",
             f"- Surface - {surface}",
             ]
    for clue in clues:
        lines.append(f"- Clue in hand - {clue}")
    lines += ["",
              "## Learning checklist",
              "",
              "The exploration unit fills these in from the "
              "task's own screens and the cross-checked sources "
              "of the learning protocol, marking each value "
              "measured or untested - entry point, mechanism, "
              "rewards, cost, cycle and deadline shape, whether "
              "it scores anywhere, and the live read that "
              "verifies it.",
              "",
              "## Red lines for exploration",
              "",
              "Exploration is read-only learning. Nothing priced "
              "is pressed, no diamonds are spent, and any rule "
              "that stays unclear keeps the candidate learn-only "
              "and named to the owner in the round summary.",
              "",
              "## Promotion path",
              "",
              "candidate, then exploring, then active once the "
              "mechanism is clear and inside the free and safe "
              "envelope, or rejected with the reason kept - the "
              "discovery protocol of the perception-driven queue "
              "design, section 6.",
              ""]
    return "\n".join(lines)


# ---------------------------------------------------------------------
# Promotion proposals (Phase 3 slice)
# ---------------------------------------------------------------------

def exploration_done_units(units, slug):
    """Completed exploration units for one candidate slug, from
    any date. Exploration units carry their source in their
    window text - "scout <date> - exploration - <slug> - ..." -
    so the window marker, not the run date, is the match; a
    candidate explored on an earlier day is found by a later
    run instead of aging in silence."""
    needle = f"exploration - {slug} -"
    done = [f for f in units
            if f.get("_state") == "done"
            and needle in str(f.get("window", ""))]
    return sorted(done, key=lambda f: str(f.get("_file", "")))


def _result_text(result, key):
    if not isinstance(result, dict):
        return ""
    value = result.get(key, "")
    return "" if value is None else str(value)


def promotion_proposals(units, roster, candidates):
    """One proposal per registered candidate with a completed
    exploration unit. The proposal aggregates the exploration
    record - it never judges mechanism clarity itself, because
    the pool carries the exploration result, not the judgment:
    the decision owed is promote once the mechanism is clear
    and inside the free and safe envelope, reject with the
    reason kept if priced, red-lined, owner-only or not a task
    at all, and keep exploring otherwise. Candidates with no
    completed exploration unit get no proposal, and a proposal
    changes nothing in the pool or the roster."""
    slugs = set(candidates)
    for name, entry in roster.items():
        if entry.get("status") in ("candidate", "exploring"):
            slugs.add(name)
    proposals = []
    for slug in sorted(slugs):
        done = exploration_done_units(units, slug)
        if not done:
            continue
        rec = candidates.get(slug, {})
        entry = roster.get(slug, {})
        explorations = []
        for f in done:
            result = f.get("result", {})
            stats = result.get("stats", {}) \
                if isinstance(result, dict) else {}
            if not isinstance(stats, dict):
                stats = {}
            explorations.append({
                "file": f.get("_file", ""),
                "status": _result_text(result, "status"),
                "finished_at": _result_text(result,
                                            "finished_at"),
                "duration_seconds": _result_text(
                    result, "duration_seconds"),
                "summary": _result_text(result, "summary"),
                "evidence": _result_text(result, "evidence"),
                "follow_up": _result_text(result, "follow_up"),
                "stats": {str(k): str(v)
                          for k, v in stats.items()}})
        proposals.append({
            "slug": slug,
            "label": rec.get("label", "") or
                     entry.get("title", slug),
            "surface": rec.get("surface", "") or
                       "not observed in this pass",
            "register_status": entry.get("status", "") or
                               rec.get("status", ""),
            "observed_today": slug in candidates,
            "explorations": explorations})
    return proposals


# ---------------------------------------------------------------------
# Main diff
# ---------------------------------------------------------------------

def run(args):
    stamp = parse_iso(args.now) if args.now else now_utc()
    date = args.date
    if not date:
        m = re.search(r"(20\d\d-\d\d-\d\d)", args.observation)
        date = m.group(1) if m else stamp.astimezone(
            LOCAL_TZ).strftime("%Y-%m-%d")
    repo = os.path.abspath(args.repo)
    regulars_path = args.regulars or os.path.join(
        repo, "_tools_", "regulars.json")
    regulars = load_regulars(regulars_path)
    roster = load_roster(repo)
    reg_by_activity = {}
    for rid, item in regulars.items():
        if item.get("activity"):
            reg_by_activity[item["activity"]] = rid
    ledger_path = args.ledger
    if ledger_path is None:
        default_ledger = os.path.join(
            repo, "_conventions_", "local-conventions",
            "daily-collection-ledger.md")
        ledger_path = default_ledger if os.path.isfile(
            default_ledger) else ""
    ledger_regulars = load_ledger_regulars(ledger_path,
                                           set(regulars))
    items, unmatched = load_observation(args.observation)
    day_counters = load_day_counters(args.observation)
    narrative_accounting = load_narrative_accounting(
        args.observation)
    units = pool_units(args.root)
    now_local = stamp.astimezone(LOCAL_TZ)

    actionable = {}          # (regular, planned_iso) -> entry
    candidates = {}          # slug -> candidate record
    not_actionable = []
    unexplained = []
    counts = {"info_satisfied": 0}

    def file_candidate(slug, label, surface, clues, from_item):
        if slug in candidates:
            rec = candidates[slug]
            for clue in clues:
                if clue not in rec["clues"]:
                    rec["clues"].append(clue)
            return
        entry = roster.get(slug)
        candidates[slug] = {
            "slug": slug, "label": label, "surface": surface,
            "clues": list(clues),
            "registered": bool(entry),
            "status": entry["status"] if entry else "",
            "from_item": from_item}

    for item in items:
        verdict = classify(item, regulars, roster, reg_by_activity)
        cls = verdict["class"]
        if cls == "actionable":
            regular = verdict["owner"]
            profile = regulars[regular]
            est = Q.typical_minutes(args.root, regular)[0] \
                if args.root else Q.SYNC_EST_MINUTES.get(
                    regular, Q.DEFAULT_EST_MINUTES)
            priority, score = compute_priority(item, est, stamp)
            planned_local = Q.cycle_start_local(profile, now_local)
            planned_iso = iso(planned_local.astimezone(
                timezone.utc))
            key = (regular, planned_iso)
            entry = actionable.setdefault(key, {
                "regular": regular,
                "activity": profile.get("activity", ""),
                "segment": profile.get("segment", ""),
                "priority": priority, "score": score,
                "est_minutes": est, "planned_for": planned_iso,
                "expires_at": "", "items": []})
            entry["priority"] = min(entry["priority"], priority)
            entry["score"] = max(entry["score"], score)
            deadline = str(item.get("deadline", ""))
            if deadline and (not entry["expires_at"] or
                             deadline < entry["expires_at"]):
                entry["expires_at"] = deadline
            entry["items"].append(item)
        elif cls == "candidate":
            clues = []
            if item.get("deadline"):
                clues.append("visible deadline " +
                             str(item["deadline"]))
            if item.get("est_value_or_score"):
                clues.append("on-screen value " +
                             str(item["est_value_or_score"]))
            if item.get("redline_check"):
                clues.append("redline note " +
                             str(item["redline_check"]))
            file_candidate(verdict["slug"],
                           str(item.get("label", "")),
                           str(item.get("surface", "")), clues,
                           True)
        elif cls == "not-actionable":
            if str(item.get("state", "")) == "info-only":
                counts["info_satisfied"] += 1
            not_actionable.append({"item": item,
                                   "reason": verdict["reason"]})
        else:
            unexplained.append({"item": item,
                                "reason": verdict["reason"]})

    for label in unmatched:
        slug = slugify(label)
        entry = roster.get(slug)
        if entry and entry["status"] == "rejected":
            not_actionable.append({
                "item": {"label": label, "surface": "",
                         "state": "info-only"},
                "reason": "unmatched label previously rejected, "
                          "kept against rediscovery"})
            continue
        if slug in roster and roster[slug]["status"] not in (
                "candidate", "exploring"):
            continue            # already an owned profile
        file_candidate(slug, label, "unmatched label",
                       ["named on the unmatched labels list of " +
                        date], False)

    # Build the enqueue plan - execution entries first, then the
    # exploration entries under the discovery chain.
    plan = []
    for key in sorted(actionable,
                      key=lambda k: (actionable[k]["priority"], k)):
        entry = actionable[key]
        markers = [marker_for(date, it) for it in entry["items"]]
        existing = None
        for marker in markers:
            existing = find_existing(units, entry["regular"],
                                     entry["planned_for"], marker)
            if existing:
                break
        action = "enqueue"
        if existing:
            try:
                have = int(existing.get("priority", 3))
            except (TypeError, ValueError):
                have = 3
            action = "raise" if entry["priority"] < have \
                else "already-queued"
        trigger = "claimable now"
        if entry["priority"] == 1:
            trigger = "deadline approaching, expiry band"
        window = "; ".join(markers)
        plan.append({
            "action": action, "kind": "execution",
            "regular": entry["regular"],
            "activity": entry["activity"],
            "segment": entry["segment"],
            "priority": entry["priority"],
            "expires_at": entry["expires_at"],
            "not_before": "", "planned_for": entry["planned_for"],
            "est_minutes": entry["est_minutes"],
            "window": f"{trigger} - {window}",
            "chain_id": "",
            "source_items": [
                {"surface": it.get("surface", ""),
                 "label": it.get("label", "")}
                for it in entry["items"]]})

    est_scout = Q.typical_minutes(args.root, "scout")[0] \
        if args.root else Q.SYNC_EST_MINUTES.get("scout", 10)
    for slug in sorted(candidates):
        rec = candidates[slug]
        label = rec["label"] or slug
        marker = f"scout {date} - exploration - {slug} - {label}"
        existing = find_existing(units, "scout", "", marker)
        plan.append({
            "action": "already-queued" if existing else "enqueue",
            "kind": "exploration", "regular": "scout",
            "activity": slug,
            "segment": regulars.get("scout", {}).get("segment",
                                                     ""),
            "priority": 2, "expires_at": "", "not_before": "",
            "planned_for": "",
            "est_minutes": est_scout,
            "window": marker + " - read-only learning, "
                              "red lines learn-only",
            "chain_id": f"scout-discovery-{date}",
            "source_items": [{"surface": rec["surface"],
                              "label": label}]})

    # Apply - one queue.py enqueue call per enqueue entry, only
    # against the explicitly given pool root.
    applied, apply_failures = [], []
    if args.apply:
        queue_py = os.path.join(TOOLS_DIR, "queue.py")
        for entry in plan:
            if entry["action"] != "enqueue":
                continue
            cmd = [sys.executable, queue_py, "--root", args.root,
                   "enqueue", "--regular", entry["regular"],
                   "--activity", entry["activity"] or "",
                   "--priority", str(entry["priority"]),
                   "--est-minutes", str(entry["est_minutes"]),
                   "--window", entry["window"]]
            if entry["segment"] != "":
                cmd += ["--segment", str(entry["segment"])]
            if entry["expires_at"]:
                cmd += ["--expires-at", entry["expires_at"]]
            if entry["not_before"]:
                cmd += ["--not-before", entry["not_before"]]
            if entry["chain_id"]:
                cmd += ["--chain-id", entry["chain_id"]]
            out = subprocess.run(cmd, capture_output=True,
                                 text=True)
            text = (out.stdout or "").strip()
            if out.returncode == 0 and text.startswith("queued"):
                applied.append(text.split(" ", 1)[1])
            elif "already queued" in text:
                entry["action"] = "already-queued"
            else:
                apply_failures.append(
                    {"entry": entry["regular"],
                     "output": text or out.stderr.strip()})

    # Promotion proposals - read-only aggregation over the pool
    # units already loaded above; without --root the pool is
    # unread, so no proposal can be grounded and none is made.
    proposals = promotion_proposals(units, roster, candidates) \
        if args.root else []

    # Outputs.
    out_dir = args.out or os.path.join(
        os.path.dirname(os.path.abspath(args.observation)),
        "scout-diff-output")
    os.makedirs(out_dir, exist_ok=True)
    plan_path = os.path.join(
        out_dir, f"scout-enqueue-plan-{date}.jsonl")
    with open(plan_path, "w", encoding="utf-8") as fh:
        for entry in plan:
            fh.write(json.dumps(entry, ensure_ascii=False) + "\n")

    cand_path = os.path.join(
        out_dir, f"scout-candidates-{date}.md")
    cand_lines = ["---",
                  f"title: Scout Candidate Filings {date}",
                  f"created: {iso(stamp)}",
                  "description: Provisional candidate profiles "
                  "the scout diff files for this date",
                  "---", "",
                  f"# Candidate filings - {date}", ""]
    if not candidates:
        cand_lines.append("No candidates filed for this date.")
    for slug in sorted(candidates):
        rec = candidates[slug]
        cand_lines.append(f"## {slug}")
        cand_lines.append("")
        if rec["registered"]:
            cand_lines.append(
                f"Already in the register with status "
                f"{rec['status']} - no new filing; the exploration "
                f"entry in the enqueue plan is its next unit.")
            cand_lines.append("")
            continue
        cand_lines.append(
            "Provisional profile draft - file as "
            f"`_activities_/{slug}/INDEX.md` -")
        cand_lines.append("")
        cand_lines.append("```markdown")
        cand_lines.append(candidate_draft(
            slug, rec["label"], rec["surface"], rec["clues"],
            stamp, date))
        cand_lines.append("```")
        cand_lines.append("")
    with open(cand_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(cand_lines))

    prom_path = os.path.join(
        out_dir, f"scout-promotions-{date}.md")
    prom_lines = ["---",
                  f"title: Scout Promotion Proposals {date}",
                  f"created: {iso(stamp)}",
                  "description: Promotion or rejection proposals "
                  "for candidates whose exploration completed - "
                  "proposals only, never applied by this tool",
                  "---", "",
                  f"# Promotion proposals - {date}", ""]
    if not args.root:
        prom_lines.append(
            "Pool not read (no --root), so completed "
            "explorations could not be checked and no proposal "
            "is grounded in this run.")
    elif not proposals:
        prom_lines.append(
            "No registered candidate has a completed "
            "exploration unit in the pool - no promotion "
            "decision is owed by this run.")
    for prop in proposals:
        prom_lines.append(f"## {prop['slug']}")
        prom_lines.append("")
        prom_lines.append(
            f"Label - {prop['label']}; surface - "
            f"{prop['surface']}; register status - "
            f"{prop['register_status']}; observed in this "
            f"pass - {'yes' if prop['observed_today'] else 'no'}.")
        prom_lines.append("")
        prom_lines.append(
            "Decision owed - promote to active once the "
            "mechanism is clear and inside the free and safe "
            "envelope, reject with the reason kept if priced, "
            "red-lined, owner-only or not a task at all, "
            "otherwise keep exploring. This proposal changes "
            "nothing: promotion or rejection is a metadata "
            "edit made by the knowledge organizer or the "
            "owner."
            + (" The next exploration unit in the enqueue "
               "plan is still enqueued, so a keep-exploring "
               "decision keeps its unit."
               if prop["observed_today"] else
               " No exploration unit is enqueued for it by "
               "this pass, since it was not observed today - "
               "a keep-exploring decision needs its next "
               "unit staged by the planner."))
        prom_lines.append("")
        for ex in prop["explorations"]:
            prom_lines.append(
                f"- exploration unit {ex['file']} - result "
                f"{ex['status'] or 'unrecorded'}"
                + (f", finished {ex['finished_at']}"
                   if ex["finished_at"] else "")
                + (f", {ex['duration_seconds']}s"
                   if ex["duration_seconds"] else ""))
            if ex["summary"]:
                prom_lines.append(f"  summary - {ex['summary']}")
            if ex["evidence"]:
                prom_lines.append(
                    f"  evidence - {ex['evidence']}")
            if ex["follow_up"]:
                prom_lines.append(
                    f"  follow-up - {ex['follow_up']}")
            if ex["stats"]:
                prom_lines.append(
                    "  stats - " + ", ".join(
                        f"{k}={v}"
                        for k, v in sorted(ex["stats"].items())))
        prom_lines.append("")
    with open(prom_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(prom_lines))

    to_enqueue = [e for e in plan if e["action"] == "enqueue"]
    already = [e for e in plan if e["action"] == "already-queued"]
    raises = [e for e in plan if e["action"] == "raise"]
    surfaces = {}
    for item in items:
        surfaces[item.get("surface", "")] = surfaces.get(
            item.get("surface", ""), 0) + 1
    unexplained_count = len(unexplained) + len(
        [lbl for lbl in unmatched
         if slugify(lbl) not in candidates
         and slugify(lbl) not in roster])
    # Coverage headline fallback (issue 149): with no structured
    # item parsed, the classified counts are 0 by construction,
    # not a finding, and the evaluation metric reads the
    # headline - so a narrative-only day would report 0 items
    # and 0 unexplained dots against its own accounting.
    # The headline then reports the observation's own
    # frontmatter counts first; when the frontmatter carries
    # no unexplained counter, the unexplained headline falls
    # back one more tier to the narrative accounting section
    # total (issue 149, 2026-11-03 shape: narrative sections
    # with no frontmatter counters at all). The narrative
    # seen total is never used as items observed: seen counts
    # red-dot signals, not observed items, so the items
    # headline stays the classified count on that tier. The
    # classified counts are kept alongside so the basis stays
    # auditable. A structured observation (at least one parsed
    # item) is never overridden, and an observation with
    # neither parsed items, frontmatter counters nor a stated
    # narrative unexplained total stays honestly empty.
    classified_items = len(items)
    classified_unexplained = unexplained_count
    headline_items = classified_items
    headline_unexplained = classified_unexplained
    frontmatter_used = False
    narrative_used = False
    if classified_items == 0:
        if day_counters["items_observed"] is not None:
            headline_items = day_counters["items_observed"]
            frontmatter_used = True
        if day_counters["unexplained_red_dots"] is not None:
            headline_unexplained = \
                day_counters["unexplained_red_dots"]
            frontmatter_used = True
        elif narrative_accounting["totals"]["unexplained"] \
                is not None:
            headline_unexplained = \
                narrative_accounting["totals"]["unexplained"]
            narrative_used = True
    if classified_items > 0:
        coverage_basis = "classified"
    elif frontmatter_used and narrative_used:
        coverage_basis = "frontmatter+narrative-fallback"
    elif frontmatter_used:
        coverage_basis = "frontmatter-fallback"
    elif narrative_used:
        coverage_basis = "narrative-fallback"
    else:
        coverage_basis = "empty"
    coverage = {
        "date": date, "observation": args.observation,
        "items_observed": headline_items,
        "items_observed_classified": classified_items,
        "coverage_basis": coverage_basis,
        "actionable_items": sum(len(e["items"]) for e in
                                actionable.values()),
        "queued_entries": len(plan),
        "to_enqueue": len(to_enqueue),
        "already_queued": len(already),
        "raises": len(raises),
        "applied": len(applied),
        "already_satisfied": counts["info_satisfied"],
        "not_actionable": len(not_actionable),
        "unknown_items": len([c for c in candidates.values()
                              if c["from_item"]]),
        "candidates_filed": len([c for c in candidates.values()
                                 if not c["registered"]]),
        "candidates_registered": len([c for c in
                                      candidates.values()
                                      if c["registered"]]),
        "unexplained_red_dots": headline_unexplained,
        "unexplained_red_dots_classified": classified_unexplained,
        "observation_day_counters": day_counters,
        "narrative_accounting": narrative_accounting,
        "unmatched_labels": unmatched,
        "promotion_proposals": len(proposals),
        "outputs": {"enqueue_plan": plan_path,
                    "candidates": cand_path,
                    "promotions": prom_path},
    }
    cov_path = os.path.join(
        out_dir, f"scout-coverage-{date}.md")
    narrative_seen = narrative_accounting["totals"]["seen"]
    narrative_unexplained = \
        narrative_accounting["totals"]["unexplained"]
    if coverage_basis == "frontmatter-fallback":
        basis_note = (" (no structured observed_items parsed; "
                      "the items and unexplained figures above "
                      "are the observation frontmatter counts, "
                      f"classified items {classified_items}, "
                      "classified unexplained "
                      f"{classified_unexplained})")
    elif coverage_basis == "narrative-fallback":
        basis_note = (" (no structured observed_items parsed "
                      "and no frontmatter counters stated; "
                      "the unexplained figure above is the sum "
                      "of the narrative accounting sections "
                      "stating a count, so chained passes may "
                      "re-state the same dot and the sum is a "
                      "section total, not a distinct-dot "
                      "count; the items figure above is the "
                      "classified count, not a day total - "
                      "the narrative seen total is "
                      f"{narrative_seen} red-dot signals, not "
                      "observed items)")
    elif coverage_basis == "frontmatter+narrative-fallback":
        basis_note = (" (no structured observed_items parsed; "
                      "the items figure above is the "
                      "observation frontmatter count, the "
                      "unexplained figure above is the sum of "
                      "the narrative accounting sections "
                      "stating a count, so chained passes may "
                      "re-state the same dot and the sum is a "
                      "section total, not a distinct-dot "
                      "count)")
    elif coverage_basis == "empty":
        basis_note = (" (no structured items parsed and no "
                      "frontmatter counters stated; the zeros "
                      "above are an absence of signal, not a "
                      "finding)")
    else:
        basis_note = " (classified structured items)"
    cov = ["---",
           f"title: Scout Coverage {date}",
           f"created: {iso(stamp)}",
           "description: Coverage report of the scout diff for "
           "this date",
           "---", "",
           f"# Scout coverage - {date}", "",
           f"Observation - {args.observation}", "",
           f"- items observed - {coverage['items_observed']}",
           f"- actionable items - {coverage['actionable_items']}",
           f"- queue entries produced - "
           f"{coverage['queued_entries']} (to enqueue "
           f"{coverage['to_enqueue']}, already queued "
           f"{coverage['already_queued']}, priority raises "
           f"{coverage['raises']}, applied this run "
           f"{coverage['applied']})",
           f"- already satisfied, read as day evidence - "
           f"{coverage['already_satisfied']}",
           f"- known, not actionable - "
           f"{coverage['not_actionable']}",
           f"- unknown items filed as candidates - "
           f"{coverage['unknown_items']} (new filings "
           f"{coverage['candidates_filed']}, already registered "
           f"{coverage['candidates_registered']})",
           f"- unexplained red dots - "
           f"{coverage['unexplained_red_dots']}",
           f"- coverage basis - {coverage_basis}{basis_note}",
           f"- promotion proposals - "
           f"{coverage['promotion_proposals']} (registered "
           f"candidates with a completed exploration unit, "
           f"decision owed)"]
    cov += ["", "## Observation day counters", ""]
    if all(v is None for v in day_counters.values()):
        if narrative_used:
            cov.append("The observation carries no day counters "
                       "in its frontmatter - the unexplained "
                       "headline above is the narrative "
                       "accounting section total in the next "
                       "section, and the items figure is the "
                       "classified count only.")
        else:
            cov.append("The observation carries no day counters "
                       "in its frontmatter - the classified "
                       "counts above are the only signal, and "
                       "no day total is claimed.")
    else:
        for key in DAY_COUNTER_KEYS:
            value = day_counters[key]
            cov.append(f"- {key} - "
                       f"{value if value is not None else 'not stated'}")
        front_unexplained = day_counters["unexplained_red_dots"]
        if front_unexplained is not None:
            if coverage_basis == "frontmatter-fallback":
                cov.append(
                    "Headline fallback - the items and "
                    "unexplained figures above are these "
                    "frontmatter counts, because no structured "
                    "items were parsed; the classified counts "
                    f"are items {classified_items}, unexplained "
                    f"{classified_unexplained}.")
            elif front_unexplained == unexplained_count:
                cov.append("The frontmatter unexplained count "
                           "matches the classified count above.")
            else:
                cov.append(
                    f"Mismatch - the frontmatter reports "
                    f"{front_unexplained} unexplained red dots "
                    f"while {unexplained_count} were classified "
                    f"from structured items. The difference is "
                    f"narrative-only dots not yet filed as "
                    f"observed items: this run neither enqueues "
                    f"nor files them, and the classified count "
                    f"above is not the day total.")
    cov += ["", "## Narrative red-dot accounting", ""]
    if not narrative_accounting["sections"]:
        cov.append("No red-dot accounting section was found in "
                   "the observation narrative - the passes wrote "
                   "no per-pass Seen, Explained and Unexplained "
                   "counts to reconcile against the frontmatter.")
    else:
        for idx, section in enumerate(
                narrative_accounting["sections"], 1):
            parts = ", ".join(
                f"{key} "
                f"{section[key] if section[key] is not None else 'not stated'}"
                for key in ACCOUNTING_KEYS)
            cov.append(f"- pass section {idx} - {parts}")
        totals = narrative_accounting["totals"]
        cov.append("- totals over the sections stating each "
                   "count - " + ", ".join(
                       f"{key} "
                       f"{totals[key] if totals[key] is not None else 'not stated'}"
                       for key in ACCOUNTING_KEYS))
        for key in ACCOUNTING_KEYS:
            front = day_counters[ACCOUNTING_FRONTMATTER[key]]
            recon = narrative_accounting["reconciliation"][key]
            if recon == "matches":
                cov.append(f"- frontmatter {key} reconciles - "
                           f"the section total {totals[key]} "
                           f"equals the frontmatter count.")
            elif recon.startswith("differs"):
                cov.append(f"- frontmatter {key} mismatch - "
                           f"the section total {totals[key]} "
                           f"{recon} against the frontmatter "
                           f"count {front}; one of the two "
                           f"accountings is stale.")
            else:
                cov.append(f"- frontmatter {key} not comparable "
                           f"- the section total or the "
                           f"frontmatter count is unstated.")
    cov += ["", "## Promotion proposals", ""]
    if not args.root:
        cov.append("Pool not read (no --root) - completed "
                   "explorations could not be checked.")
    elif not proposals:
        cov.append("None.")
    for prop in proposals:
        cov.append(f"- {prop['slug']} - "
                   f"{len(prop['explorations'])} completed "
                   f"exploration unit(s), register status "
                   f"{prop['register_status']} - decision owed: "
                   f"promote, reject, or keep exploring.")
    cov += ["", "## By surface", ""]
    for surface in sorted(surfaces):
        cov.append(f"- {surface} - {surfaces[surface]}")
    cov += ["", "## Not actionable, with reasons", ""]
    if not not_actionable:
        cov.append("None.")
    for rec in not_actionable:
        cov.append(f"- {rec['item'].get('label', '')} - "
                   f"{rec['reason']}")
    cov += ["", "## Unexplained", ""]
    if not unexplained:
        cov.append("None.")
    for rec in unexplained:
        cov.append(f"- {rec['item'].get('label', '')} - "
                   f"{rec['reason']}")
    cov += ["", "## Unmatched labels", ""]
    if unmatched:
        for lbl in unmatched:
            cov.append(f"- {lbl}")
    else:
        cov.append("The unmatched labels list is empty - the "
                   "passes looked and found nothing outside the "
                   "roster.")
    ledger_unseen = sorted(ledger_regulars - {
        e["regular"] for e in plan} - {
        str(it.get("suggested_unit", "")) for it in items})
    cov += ["", "## Ledger cross-check", "",
            "Ledger producing regulars neither observed nor "
            "queued in this pass (informational - the floor "
            "cadence still covers them) - " +
            (", ".join(ledger_unseen) if ledger_unseen else
             "none")]
    cov.append("")
    with open(cov_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(cov))
    coverage["outputs"]["coverage"] = cov_path

    # Round-summary section - the Phase 3 standing section of
    # the day round summary, paste-ready. It derives every
    # figure from the coverage counts above and adds none of
    # its own, so it can never drift from the coverage report
    # it summarises. An empty observation is reported as no
    # observation, never as a coverage claim.
    exec_entries = [e for e in plan if e["kind"] == "execution"]
    expl_entries = [e for e in plan if e["kind"] == "exploration"]
    new_filings = [c for c in candidates.values()
                   if not c["registered"]]
    rs = ["---",
          f"title: Scout Round Summary Section {date}",
          f"created: {iso(stamp)}",
          "description: Perception coverage section, ready to "
          "paste verbatim into the day round summary - every "
          "figure copied from the coverage report of the same "
          "run, no new numbers",
          "---", "",
          f"## Perception coverage - {date}", ""]
    day_unexplained = day_counters["unexplained_red_dots"]
    narrative_total_unexplained = \
        narrative_accounting["totals"]["unexplained"]
    if coverage["items_observed"] == 0:
        if narrative_used:
            rs.append(
                f"No structured items were parsed, but the "
                f"narrative accounting sections total "
                f"{narrative_total_unexplained} unexplained "
                f"red dot(s) (sum of the sections stating a "
                f"count; chained passes may re-state the same "
                f"dot) - not zero.")
        elif day_unexplained is None and \
                day_counters["items_observed"] is None:
            rs.append("No items were observed in this pass, so "
                      "this section carries no coverage claim - "
                      "the passes, not the summary, are the gap "
                      "to check.")
        else:
            day_items_txt = str(day_counters["items_observed"]) \
                if day_counters["items_observed"] is not None \
                else "an unstated number of"
            day_unexp_txt = str(day_unexplained) \
                if day_unexplained is not None \
                else "an unstated number of"
            rs.append(
                f"No structured items were parsed, but the "
                f"observation frontmatter reports "
                f"{day_items_txt} items observed and "
                f"{day_unexp_txt} unexplained red dot(s) - "
                f"the pass is narrative-only and those dots "
                f"are unclassified, not zero.")
    elif coverage["unexplained_red_dots"] == 0:
        rs.append("Zero unexplained red dots.")
    else:
        rs.append(f"{coverage['unexplained_red_dots']} "
                  f"unexplained red dot(s) - the pass is "
                  f"partial until each is named below.")
    rs.append("")
    rs.append(f"- observed {coverage['items_observed']} items; "
              f"queue entries {coverage['queued_entries']} "
              f"({len(exec_entries)} execution, "
              f"{len(expl_entries)} exploration; to enqueue "
              f"{coverage['to_enqueue']}, already queued "
              f"{coverage['already_queued']}, priority raises "
              f"{coverage['raises']}, applied this run "
              f"{coverage['applied']}); already satisfied "
              f"{coverage['already_satisfied']}, known not "
              f"actionable {coverage['not_actionable']}.")
    if coverage_basis == "frontmatter-fallback":
        rs.append("- coverage basis - frontmatter fallback: "
                  "no structured items were parsed, so the "
                  "observed and unexplained figures above are "
                  "the observation frontmatter counts, not "
                  "classified items.")
    elif coverage_basis == "narrative-fallback":
        rs.append("- coverage basis - narrative fallback: "
                  "no structured items were parsed and no "
                  "frontmatter counters stated, so the "
                  "unexplained figure above is the sum of the "
                  "narrative accounting sections stating a "
                  "count, not classified items; the observed "
                  "figure is the classified count.")
    elif coverage_basis == "frontmatter+narrative-fallback":
        rs.append("- coverage basis - frontmatter+narrative "
                  "fallback: no structured items were parsed; "
                  "the observed figure above is the "
                  "frontmatter count and the unexplained "
                  "figure above is the sum of the narrative "
                  "accounting sections stating a count.")
    elif coverage_basis == "empty":
        rs.append("- coverage basis - empty: no structured "
                  "items parsed and no frontmatter counters "
                  "stated, so the zeros above are an absence "
                  "of signal, not a finding.")
    if any(v is not None for v in day_counters.values()):
        parts = ", ".join(
            f"{key} {day_counters[key]}"
            for key in DAY_COUNTER_KEYS
            if day_counters[key] is not None)
        rs.append(f"- observation day counters (frontmatter, "
                  f"not classified items) - {parts}.")
        if day_unexplained is not None and \
                day_unexplained != coverage["unexplained_red_dots"]:
            rs.append(f"  - mismatch - frontmatter unexplained "
                      f"{day_unexplained} against classified "
                      f"{coverage['unexplained_red_dots']}: the "
                      f"difference is narrative-only dots not "
                      f"yet filed as observed items.")
    if narrative_accounting["sections"]:
        totals = narrative_accounting["totals"]
        recon = narrative_accounting["reconciliation"]
        rs.append("- narrative red-dot accounting - "
                  f"{len(narrative_accounting['sections'])} "
                  "pass section(s), totals " + ", ".join(
                      f"{key} "
                      f"{totals[key] if totals[key] is not None else 'not stated'}"
                      for key in ACCOUNTING_KEYS) + "; "
                  "frontmatter reconciliation - " + ", ".join(
                      f"{key} {recon[key]}"
                      for key in ACCOUNTING_KEYS) + ".")
    rs.append(f"- unknown items - "
              f"{coverage['unknown_items']} filed as "
              f"candidates ({coverage['candidates_filed']} "
              f"new filings, "
              f"{coverage['candidates_registered']} already "
              f"registered).")
    for rec in sorted(new_filings, key=lambda c: c["slug"]):
        rs.append(f"  - new candidate {rec['slug']} - "
                  f"{rec['label'] or rec['slug']} "
                  f"({rec['surface']}).")
    if unmatched:
        rs.append("- unmatched labels - every label the "
                  "passes met that no roster entry owns:")
        for lbl in unmatched:
            rs.append(f"  - {lbl}")
    else:
        rs.append("- unmatched labels - none: the passes "
                  "looked and found nothing outside the "
                  "roster.")
    if not args.root:
        rs.append("- promotion proposals - not checked: the "
                  "pool was not read (no --root), so a zero "
                  "here would be an unread pool, not a "
                  "finding.")
    elif not proposals:
        rs.append("- promotion proposals - none owed: no "
                  "registered candidate has a completed "
                  "exploration unit in the pool.")
    else:
        rs.append("- promotion proposals - decision owed:")
        for prop in proposals:
            rs.append(f"  - {prop['slug']} - "
                      f"{len(prop['explorations'])} completed "
                      f"exploration unit(s), register status "
                      f"{prop['register_status']} - promote, "
                      f"reject, or keep exploring.")
    rs.append("")
    rs.append("Source - the coverage report and the "
              "promotion proposals file in the same output "
              "directory; this section adds no new numbers.")
    rs.append("")
    rs_path = os.path.join(
        out_dir, f"scout-round-summary-{date}.md")
    with open(rs_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(rs))
    coverage["outputs"]["round_summary"] = rs_path
    coverage["apply_failures"] = apply_failures
    coverage["applied_units"] = applied

    if args.format == "json":
        print(json.dumps(coverage, indent=2, ensure_ascii=False))
    else:
        print(f"scout diff for {date} - "
              f"observed {coverage['items_observed']}, "
              f"actionable {coverage['actionable_items']}, "
              f"to enqueue {coverage['to_enqueue']}, "
              f"already queued {coverage['already_queued']}, "
              f"raises {coverage['raises']}, "
              f"candidates {len(candidates)}, "
              f"unexplained red dots "
              f"{coverage['unexplained_red_dots']}, "
              f"promotion proposals "
              f"{coverage['promotion_proposals']}")
        print(f"outputs in {out_dir}")
        if applied:
            print(f"applied {len(applied)} - "
                  f"{', '.join(applied)}")
        for failure in apply_failures:
            print(f"apply failed for {failure['entry']} - "
                  f"{failure['output']}")
    return 1 if apply_failures else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--observation", required=True)
    parser.add_argument("--date", default="")
    parser.add_argument("--out", default="")
    parser.add_argument("--root", default="")
    parser.add_argument("--repo", default=os.path.join(
        TOOLS_DIR, ".."))
    parser.add_argument("--regulars", default="")
    parser.add_argument("--ledger", default=None)
    parser.add_argument("--now", default="")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--format", choices=["text", "json"],
                        default="text")
    args = parser.parse_args(argv)
    if args.apply and not args.root:
        parser.error("--apply requires --root naming the pool "
                     "explicitly")
    if args.root:
        args.root = os.path.abspath(args.root)
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
