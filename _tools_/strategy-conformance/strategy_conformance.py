#!/usr/bin/env python3
"""strategy_conformance: does the strategy reach the queue and the game? Read-only, counts only.

Reads the queue folders (`_queue_/inbox`, `claimed`, `done`) and each unit's frontmatter directly - never a seat's report -
and prints counts, percentages and minutes. It writes nothing. Five alarms, each with its threshold flag:

  no execution      no unit executed (done, partial or failed) for more than --stale-minutes (45)
  idle slot         the latest building-queues, research-queue or troop-training read left a builder, lab or queue slot
                    idle (builders_idle / slots_idle in the unit's stats, less what the same unit started) for more than
                    --idle-minutes (30)
  coverage          units, or unit-hours (result duration, else est_minutes), serving a RANKED item are under
                    --coverage-percent (60) of what executed in the window
  growth partial    partial units are over --partial-percent (35) of executed growth units in the window
  plan item         a top plan item (--plan, rank within --top) has no claimed or finished unit carrying its serves tag
                    --late-hours (2) after its trigger

A unit serves a RANKED item when its `serves` is anything but upkeep, snapshot or baseline; a unit with no serves line is
told by its chain id, regular and file name (growth, convert, collect, promot, capacity, store, inventory, troop-read).
The plan file is a CSV `rank,item,trigger_at,serves` (trigger_at in UTC, ISO 8601), kept by the strategist; without one the
plan-item check is skipped and says so. A kind with no sample (nothing executed, no growth unit) is n/a, never an alarm.

  strategy_conformance.py [--root PATH] [--hours 12] [--now ISO] [--plan CSV] [--format text|json]

Exit 0 conforming, 1 at least one alarm, 2 the queue cannot be read. Standard library only.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
NON_RANKED = {"upkeep", "snapshot", "baseline"}
GROWTH_MARKERS = ("growth", "convert", "collect", "promot", "capacity", "store", "inventory", "troop-read")
EXECUTED = ("done", "partial", "failed")
SLOT_ACTIVITIES = ("building-queues", "research-queue", "troop-training")
IDLE_KEYS = ("builders_idle", "slots_idle", "queue_slots_idle", "queues_idle", "labs_idle", "idle_slots")
STARTED_KEYS = ("upgrades_started", "research_started", "training_started", "batches_started")


def flat_frontmatter(text: str) -> dict:
    """The frontmatter as flat keys: top-level keys as written, nested ones as parent.child (result.status,
    result.stats.builders_idle)."""
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    out: dict = {}
    if not m:
        return out
    stack: list[tuple[int, str]] = []
    for line in m.group(1).splitlines():
        if not line.strip() or ":" not in line:
            continue
        indent = len(line) - len(line.lstrip(" "))
        key, _, value = line.strip().partition(":")
        while stack and indent <= stack[-1][0]:
            stack.pop()
        path = ".".join([k for _i, k in stack] + [key.strip()])
        if value.strip():
            out[path] = value.strip().strip("'\"")
        else:
            stack.append((indent, key.strip()))
    return out


def stamp(value: str | None):
    if not value:
        return None
    try:
        dt = datetime.fromisoformat(str(value).strip().replace("Z", "+00:00"))
    except ValueError:
        return None
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def number(fields: dict, key: str, default=None):
    value = fields.get(key)
    if value is None:
        return default
    m = re.match(r"^-?\d+(?:\.\d+)?", str(value))
    return float(m.group(0)) if m else default


class Unit:
    def __init__(self, folder: str, name: str, fields: dict):
        self.folder, self.name, self.f = folder, name, fields
        self.status = fields.get("result.status", "")
        self.finished = stamp(fields.get("result.finished_at"))
        self.claimed = stamp(fields.get("claimed_at"))
        self.serves = fields.get("serves", "").strip().lower()
        self.activity = fields.get("activity", "")
        hours = number(fields, "result.duration_seconds")
        self.hours = hours / 3600 if hours is not None else (number(fields, "est_minutes", 0) or 0) / 60

    @property
    def ranked(self) -> bool:
        if self.serves:
            return self.serves not in NON_RANKED
        return self.growth_by_name

    @property
    def growth_by_name(self) -> bool:
        text = " ".join([self.f.get("chain_id", ""), self.f.get("regular", ""), self.name]).lower()
        return any(marker in text for marker in GROWTH_MARKERS)


def load(root: Path, folder: str) -> list[Unit]:
    path = root / "_queue_" / folder
    if not path.is_dir():
        raise OSError(f"{path} is not a queue folder")
    units = []
    for entry in sorted(path.iterdir()):
        if entry.name.startswith(".") or entry.suffix != ".md" or entry.name == "device-token.md":
            continue
        units.append(Unit(folder, entry.name, flat_frontmatter(entry.read_text(encoding="utf-8", errors="replace"))))
    return units


def percent(part, whole):
    return None if not whole else 100.0 * part / whole


def read_plan(path: Path | None):
    if path is None or not path.is_file():
        return None
    rows = []
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            try:
                rows.append({"rank": int(row["rank"]), "item": row["item"], "trigger": stamp(row["trigger_at"]),
                             "serves": (row.get("serves") or row["item"]).strip().lower()})
            except (KeyError, ValueError):
                continue
    return sorted(rows, key=lambda r: r["rank"])


def evaluate(root: Path, now: datetime, hours: float, plan_path: Path | None, a) -> dict:
    inbox, claimed, done = load(root, "inbox"), load(root, "claimed"), load(root, "done")
    cut = now - timedelta(hours=hours)
    executed = [u for u in done if u.status in EXECUTED and u.finished and u.finished >= cut]
    alarms, na = [], []
    counts = {"inbox": len(inbox), "claimed": len(claimed), "executed_in_window": len(executed),
              "expired_in_window": sum(1 for u in done if u.status == "expired" and u.finished and u.finished >= cut),
              "by_status": {s: sum(1 for u in executed if u.status == s) for s in EXECUTED},
              "inbox_without_serves": sum(1 for u in inbox if not u.serves),
              "executed_without_serves": sum(1 for u in executed if not u.serves)}
    # no execution
    last = max((u.finished for u in done if u.status in EXECUTED and u.finished), default=None)
    age = None if last is None else (now - last).total_seconds() / 60
    counts["minutes_since_last_execution"] = None if age is None else round(age)
    if age is None or age > a.stale_minutes:
        alarms.append({"alarm": "no-execution", "minutes": None if age is None else round(age), "limit": a.stale_minutes})
    # idle slots
    idle = []
    for activity in SLOT_ACTIVITIES:
        reads = [u for u in done if u.activity == activity and u.status in EXECUTED and u.finished]
        if not reads:
            continue
        latest = max(reads, key=lambda u: u.finished)
        value = next((number(latest.f, f"result.stats.{k}") for k in IDLE_KEYS if number(latest.f, f"result.stats.{k}") is not None), None)
        started = sum(number(latest.f, f"result.stats.{k}", 0) or 0 for k in STARTED_KEYS)
        if value is None:
            continue
        open_slots = max(0, int(value) - int(started))
        minutes = (now - latest.finished).total_seconds() / 60
        idle.append({"activity": activity, "idle_slots": open_slots, "minutes_since_read": round(minutes)})
        if open_slots > 0 and minutes > a.idle_minutes:
            alarms.append({"alarm": "idle-slot", "activity": activity, "idle_slots": open_slots, "minutes": round(minutes),
                           "limit": a.idle_minutes})
    counts["slot_reads"] = idle
    # coverage
    if executed:
        unit_cov = percent(sum(1 for u in executed if u.ranked), len(executed))
        total_hours = sum(u.hours for u in executed)
        hour_cov = percent(sum(u.hours for u in executed if u.ranked), total_hours)
        counts["coverage_units_percent"] = None if unit_cov is None else round(unit_cov)
        counts["coverage_unit_hours_percent"] = None if hour_cov is None else round(hour_cov)
        low = [name for name, v in (("units", unit_cov), ("unit-hours", hour_cov)) if v is not None and v < a.coverage_percent]
        if low:
            alarms.append({"alarm": "coverage", "below": low, "units_percent": counts["coverage_units_percent"],
                           "unit_hours_percent": counts["coverage_unit_hours_percent"], "limit": a.coverage_percent})
    else:
        na.append("coverage")
    # growth partial rate
    growth = [u for u in executed if u.ranked]
    counts["growth_executed"] = len(growth)
    if growth:
        partial = percent(sum(1 for u in growth if u.status == "partial"), len(growth))
        counts["growth_partial_percent"] = round(partial)
        if partial > a.partial_percent:
            alarms.append({"alarm": "growth-partial", "percent": round(partial), "limit": a.partial_percent})
    else:
        na.append("growth-partial")
    # plan items
    plan = read_plan(plan_path)
    if plan is None:
        na.append("plan-item (no plan file)")
    else:
        started_tags = {u.serves for u in claimed + done if u.serves and (u.status != "expired")}
        top = [r for r in plan if r["rank"] <= a.top]
        counts["plan_items_checked"] = len(top)
        for row in top:
            late = row["trigger"] is not None and now > row["trigger"] + timedelta(hours=a.late_hours)
            if late and row["serves"] not in started_tags:
                alarms.append({"alarm": "plan-item", "item": row["item"], "rank": row["rank"],
                               "hours_past_trigger": round((now - row["trigger"]).total_seconds() / 3600, 1), "limit": a.late_hours})
    return {"at": now.strftime("%Y-%m-%dT%H:%MZ"), "window_hours": hours, "counts": counts, "alarms": alarms, "not_applicable": na}


def render(result: dict) -> str:
    c = result["counts"]
    lines = [f"== STRATEGY CONFORMANCE ({result['at']}, window {result['window_hours']:g} h) ==",
             f"queue: inbox {c['inbox']}  claimed {c['claimed']} | executed in window {c['executed_in_window']} {c['by_status']} | "
             f"expired {c['expired_in_window']}",
             f"serves: inbox units without {c['inbox_without_serves']}, executed without {c['executed_without_serves']}"]
    last = c["minutes_since_last_execution"]
    lines.append("last execution: " + ("none on record" if last is None else f"{last} min ago"))
    if "coverage_units_percent" in c:
        lines.append(f"coverage serving a ranked item: units {c['coverage_units_percent']}%, unit-hours {c['coverage_unit_hours_percent']}%")
    lines.append(f"growth units executed {c['growth_executed']}" + (f", partial {c['growth_partial_percent']}%" if "growth_partial_percent" in c else ""))
    for read in c["slot_reads"]:
        lines.append(f"slot read {read['activity']}: {read['idle_slots']} idle, read {read['minutes_since_read']} min ago")
    if "plan_items_checked" in c:
        lines.append(f"plan items checked: {c['plan_items_checked']}")
    for alarm in result["alarms"]:
        detail = ", ".join(f"{k} {v}" for k, v in alarm.items() if k != "alarm")
        lines.append(f"ALARM {alarm['alarm']}: {detail}")
    if result["not_applicable"]:
        lines.append("n/a: " + ", ".join(result["not_applicable"]))
    lines.append("conforming" if not result["alarms"] else f"{len(result['alarms'])} alarm(s)")
    return "\n".join(lines)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=str(HERE.parent.parent), help="the repository (default: the one holding this tool)")
    p.add_argument("--hours", type=float, default=12, help="the window of executed units")
    p.add_argument("--now", default="", help="the instant to judge at, ISO 8601 UTC (default: now)")
    p.add_argument("--plan", default="", help="plan-of-record CSV: rank,item,trigger_at,serves")
    p.add_argument("--top", type=int, default=3, help="plan items up to this rank are checked")
    p.add_argument("--stale-minutes", type=float, default=45)
    p.add_argument("--idle-minutes", type=float, default=30)
    p.add_argument("--coverage-percent", type=float, default=60)
    p.add_argument("--partial-percent", type=float, default=35)
    p.add_argument("--late-hours", type=float, default=2)
    p.add_argument("--format", choices=("text", "json"), default="text")
    a = p.parse_args(argv)
    root = Path(a.root)
    now = stamp(a.now) if a.now else datetime.now(timezone.utc)
    if now is None:
        print("strategy_conformance: --now is not an ISO 8601 time", file=sys.stderr)
        return 2
    plan = Path(a.plan) if a.plan else None
    try:
        result = evaluate(root, now, a.hours, plan, a)
    except OSError as error:
        print(f"strategy_conformance: cannot read the queue: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=1, sort_keys=True) if a.format == "json" else render(result))
    return 1 if result["alarms"] else 0


if __name__ == "__main__":
    sys.exit(main())
