#!/usr/bin/env python3
"""Scout diff - the diff of the perception layer as a program.

Implements the Phase 2 tool design of the perception-driven queue
(_conventions_/local-conventions/perception-driven-queue.md,
sections 5, 6 and 9). A scout pass observes the game and writes
its observed items into the day observation file; this tool reads
that observation, diffs it against the modelled work - the
regulars profile library, the _activities_ roster with its
candidate register, and the pool itself - and produces three
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
     in full (an empty list is printed as empty, never omitted).

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
    coverage = {
        "date": date, "observation": args.observation,
        "items_observed": len(items),
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
        "unexplained_red_dots": unexplained_count,
        "unmatched_labels": unmatched,
        "outputs": {"enqueue_plan": plan_path,
                    "candidates": cand_path},
    }
    cov_path = os.path.join(
        out_dir, f"scout-coverage-{date}.md")
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
           "", "## By surface", ""]
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
              f"{coverage['unexplained_red_dots']}")
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
