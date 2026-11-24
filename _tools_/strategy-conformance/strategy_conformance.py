#!/usr/bin/env python3
"""strategy_conformance: does the strategy reach the queue and the game? Read-only, counts only.

Reads the queue folders (`_queue_/inbox`, `claimed`, `done`) and each unit's frontmatter directly - never a seat's report -
and prints counts, percentages and minutes. It writes nothing. Five alarms, each with its threshold flag:

  no execution      no unit executed (done, partial or failed) for more than --stale-minutes (45)
  idle slot         the latest building-queues, research-queue or troop-training read left a builder, lab or queue slot
                    idle (builders_idle / slots_idle in the unit's stats, less what the same unit started) for more than
                    --idle-minutes (30). A slot BLOCKED BY CAPACITY is not idle in the alarm's sense (the barracks queues
                    blocked by Drill Ground Full): the planner's slot-read units write slots_blocked_capacity N beside the idle
                    count (builders_idle, slots_idle, queue_slots_idle, queues_idle, labs_idle or idle_slots, which include the
                    blocked ones) and the blocker text; N, at most the open slots, is subtracted from the idle count and printed
                    beside it, with the blocker text when the stats carry one.
  coverage          units, or unit-hours (result duration, else est_minutes), serving a RANKED item are under
                    --coverage-percent (60) of what executed. Two lines are printed: the ROLLING window (--hours, 12; context, it
                    stays low while old units age out) and SINCE THE CUTOVER (units executed after the roster remap landed): the
                    verdict, which the alarm and the Coach quote. The cutover is, in order: --since TIME; the state file
                    `_tools_/state/strategy-cutover.json` ({"since": "ISO UTC"}); the first-parent commit in git that introduced a
                    plan item id as a roster serves (`_tools_/regulars.json`), i.e. the merge of the remap. With none of them the
                    rolling figure is the verdict and the output says so. Both lines also give the units that serve nothing
                    (not ranked) with their hours of the total. Percentages print to one decimal; the alarm compares the UNROUNDED
                    value (84 of 141 = 59.57 is below 60, though it once rounded to 60 and passed).
  growth partial    partial units are over --partial-percent (35) of executed growth units in the window
  plan item         a top plan item (--plan, rank within --top) has no claimed or finished unit carrying its serves tag
                    --late-hours (2) after its trigger

A unit serves a RANKED item when its `serves` has a part that is a plan item id (PL-17) with a row in the newest forecast ledger -
the same exact check as `queue.py validate`. An exempt word (upkeep, snapshot, baseline, fill idle slot), an id the ledger has no
row for, and any other wording ("snapshot (Story 868)") are NOT ranked and are counted apart in the output; with no ledger to read
an id counts by its shape and the output says so (ranked by wording only). A unit with no serves line is told by its chain id,
regular and file name (growth, convert, collect, promot, capacity, store, inventory, troop-read).
The plan file is a CSV `rank,item,trigger_at,serves` (trigger_at in UTC, ISO 8601), kept by the strategist; without one the
plan-item check is skipped and says so. A kind with no sample (nothing executed, no growth unit) is n/a, never an alarm.

  strategy_conformance.py [--root PATH] [--hours 12] [--since TIME] [--now ISO] [--plan CSV] [--format text|json]

Exit 0 conforming, 1 at least one alarm, 2 the queue cannot be read. Standard library only.
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import math
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
# The exact check of queue.py validate: its constants and its ledger reader are used when it can be loaded; these copies are the fallback
# (a test keeps them equal).
NON_RANKED = {"upkeep", "snapshot", "baseline"}
FILL_IDLE = re.compile(r"^fill[- ]idle[- ]slot\b", re.IGNORECASE)
PLAN_ITEM = re.compile(r"^[A-Z]{2,4}-\d{1,3}$")
RANKING = {"ids": None, "reason": "not configured", "queue": None}


def load_queue_tool():
    try:
        spec = importlib.util.spec_from_file_location("queue_for_conformance", HERE.parent / "queue.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception:                                  # any failure: the fallback copies above decide
        return None


def configure_ranking(root: Path) -> None:
    """Read the newest forecast ledger beside the queue: the plan item ids a unit may serve. None, with a reason, when there is none."""
    tool = load_queue_tool()
    RANKING["queue"] = tool
    if tool is None:
        RANKING.update(ids=None, reason="queue.py could not be loaded")
        return
    try:
        ids, reason = tool.load_forecast_ledger(str(root / "_queue_"))
    except Exception as exc:
        ids, reason = None, f"the ledger reader failed ({type(exc).__name__})"
    RANKING.update(ids=ids, reason=reason or "")


CUTOVER_STATE = "_tools_/state/strategy-cutover.json"


def resolve_cutover(root: Path, since_flag: str):
    """(instant, source) of the roster remap, or (None, why): --since, then the state file, then git (the first-parent commit that introduced a
    plan item id as a roster serves, which is the merge of the remap). Never reads anything but the state file and git log."""
    if since_flag:
        at = stamp(since_flag)
        return (at, "--since") if at else (None, "--since is not an ISO 8601 time")
    state = root / CUTOVER_STATE
    if state.is_file():
        try:
            at = stamp(json.loads(state.read_text(encoding="utf-8")).get("since"))
        except (OSError, ValueError, AttributeError):
            at = None
        if at:
            return at, f"state file {CUTOVER_STATE}"
    try:
        out = subprocess.run(["git", "-C", str(root), "log", "--first-parent", "--format=%cI", "--reverse", "-S", '"serves":"PL-', "--",
                              "_tools_/regulars.json"], capture_output=True, text=True, timeout=60)
        first = next((ln for ln in out.stdout.splitlines() if ln.strip()), "") if out.returncode == 0 else ""
    except (OSError, subprocess.SubprocessError):
        first = ""
    at = stamp(first) if first else None
    return (at, "git: the merge that introduced the roster serves ids") if at else (None, "no cutover: give --since TIME, write " + CUTOVER_STATE + ", or land the remap")


def shown(value, limit):
    """A percentage to one decimal for print and JSON; the alarm compares the unrounded value. A value below the limit is never shown as
    the limit or more (59.96 against 60 shows 59.9, not 60.0), so the printed figure and the alarm agree."""
    if value is None:
        return None
    text = round(value, 1)
    if limit is not None and value < limit <= text:
        text = math.floor(value * 10) / 10
    return text


def coverage_stats(units: list, limit=None) -> dict:
    """Units and unit-hours serving a ranked item, and the units that serve nothing (not ranked) with their hours of the total. The percentages
    are shown to one decimal (`units_percent`, `unit_hours_percent`); the unrounded values the alarm compares are `*_exact`."""
    ranked = [u for u in units if u.ranked]
    total_hours = sum(u.hours for u in units)
    ranked_hours = sum(u.hours for u in ranked)
    unit_pct = percent(len(ranked), len(units))
    hour_pct = percent(ranked_hours, total_hours)
    return {"executed": len(units), "ranked_units": len(ranked),
            "units_percent": shown(unit_pct, limit), "unit_hours_percent": shown(hour_pct, limit),
            "units_percent_exact": unit_pct, "unit_hours_percent_exact": hour_pct,
            "total_hours": round(total_hours, 2), "ranked_hours": round(ranked_hours, 2),
            "serves_nothing_units": len(units) - len(ranked), "serves_nothing_hours": round(total_hours - ranked_hours, 2)}


def serves_kind(serves: str) -> str:
    """ranked, exempt, no-row (an id the ledger lacks) or unrecognised; with no ledger an id counts as ranked by its shape (the basis says so)."""
    tool, ids = RANKING["queue"], RANKING["ids"]
    exempt = getattr(tool, "FORECAST_EXEMPT", NON_RANKED)
    fill = getattr(tool, "FORECAST_FILL", FILL_IDLE)
    plan_id = getattr(tool, "PLAN_ITEM_ID", PLAN_ITEM)
    kinds = []
    for part in re.split(r"[;,]", serves or ""):
        part = " ".join(part.split())
        if not part:
            continue
        if part.lower() in exempt or fill.match(part):
            kinds.append("exempt")
        elif plan_id.match(part):
            kinds.append("ranked" if ids is None or part in ids else "no-row")
        else:
            kinds.append("unrecognised")
    for kind in ("ranked", "no-row", "unrecognised", "exempt"):
        if kind in kinds:
            return kind
    return "exempt"
GROWTH_MARKERS = ("growth", "convert", "collect", "promot", "capacity", "store", "inventory", "troop-read")
EXECUTED = ("done", "partial", "failed")
SLOT_ACTIVITIES = ("building-queues", "research-queue", "troop-training")
IDLE_KEYS = ("builders_idle", "slots_idle", "queue_slots_idle", "queues_idle", "labs_idle", "idle_slots")
STARTED_KEYS = ("upgrades_started", "research_started", "training_started", "batches_started")
BLOCKED_KEYS = ("slots_blocked_capacity", "slots_blocked_by_capacity", "blocked_by_capacity")   # how many idle slots cannot start for want of capacity
BLOCKER_KEYS = ("capacity_blocker", "blocked_by", "blocker", "blocker_text", "slot_blocker", "slots_blocked_note", "slots_blocked_reason")
NOT_A_BLOCKER = ("blocker_category", "blocker_overlay")                      # the screen-blocking stats of another rule


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
        self.serves_raw = fields.get("serves", "").strip()
        self.activity = fields.get("activity", "")
        hours = number(fields, "result.duration_seconds")
        self.hours = hours / 3600 if hours is not None else (number(fields, "est_minutes", 0) or 0) / 60

    @property
    def serves_kind(self) -> str:
        return serves_kind(self.serves_raw) if self.serves_raw else "by-name"

    @property
    def ranked(self) -> bool:
        if self.serves_raw:
            return self.serves_kind == "ranked"
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
    configure_ranking(root)
    inbox, claimed, done = load(root, "inbox"), load(root, "claimed"), load(root, "done")
    cut = now - timedelta(hours=hours)
    executed = [u for u in done if u.status in EXECUTED and u.finished and u.finished >= cut]
    alarms, na = [], []
    counts = {"inbox": len(inbox), "claimed": len(claimed), "executed_in_window": len(executed),
              "expired_in_window": sum(1 for u in done if u.status == "expired" and u.finished and u.finished >= cut),
              "by_status": {s: sum(1 for u in executed if u.status == s) for s in EXECUTED},
              "inbox_without_serves": sum(1 for u in inbox if not u.serves),
              "executed_without_serves": sum(1 for u in executed if not u.serves)}
    kinds = {k: sum(1 for u in executed if u.serves_kind == k) for k in ("ranked", "exempt", "no-row", "unrecognised", "by-name")}
    counts["serves_kinds"] = {"ranked": kinds["ranked"], "exempt": kinds["exempt"], "no_row": kinds["no-row"], "unrecognised": kinds["unrecognised"],
                              "no_serves_line": kinds["by-name"], "ranked_by_name": sum(1 for u in executed if u.serves_kind == "by-name" and u.ranked)}
    counts["ranking_basis"] = "ledger rows" if RANKING["ids"] is not None else f"id shape only, ranked by wording only ({RANKING['reason']})"
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
        blocked = next((number(latest.f, f"result.stats.{k}") for k in BLOCKED_KEYS if number(latest.f, f"result.stats.{k}") is not None), 0) or 0
        text = next((str(latest.f.get(f"result.stats.{k}", "")).strip() for k in BLOCKER_KEYS if str(latest.f.get(f"result.stats.{k}", "")).strip()), "")
        if not text:                                                         # any other stat whose name says blocked or blocker and whose value is words
            text = next((str(v).strip() for k, v in latest.f.items() if k.startswith("result.stats.") and k.rsplit(".", 1)[1] not in NOT_A_BLOCKER
                         and re.search(r"block", k) and not re.fullmatch(r"-?\d+(\.\d+)?", str(v).strip()) and str(v).strip()), "")
        text = re.sub(r"^blocked by capacity:\s*", "", text, flags=re.I)
        exempt = min(open_slots, max(0, int(blocked)))                       # the planner writes it only for a slot it saw blocked
        alarmable = open_slots - exempt
        minutes = (now - latest.finished).total_seconds() / 60
        row = {"activity": activity, "idle_slots": alarmable, "minutes_since_read": round(minutes)}
        if exempt:
            row.update(slots_blocked_capacity=exempt, blocker=text[:40])
        idle.append(row)
        if alarmable > 0 and minutes > a.idle_minutes:
            alarms.append({"alarm": "idle-slot", "activity": activity, "idle_slots": alarmable, "minutes": round(minutes),
                           "limit": a.idle_minutes})
    counts["slot_reads"] = idle
    # coverage: the rolling window is context; the verdict is the units executed since the cutover when one is known
    cutover, cutover_source = resolve_cutover(root, a.since)
    rolling = coverage_stats(executed, a.coverage_percent)
    counts["rolling"] = {"hours": hours, **rolling}
    since_stats = None
    if cutover is not None:
        since_units = [u for u in done if u.status in EXECUTED and u.finished and cutover <= u.finished <= now]
        since_stats = coverage_stats(since_units, a.coverage_percent)
        counts["since_cutover"] = {"since": cutover.strftime("%Y-%m-%dT%H:%M:%SZ"), "source": cutover_source, **since_stats}
    else:
        counts["since_cutover"] = None
        counts["cutover_note"] = cutover_source
    counts["coverage_units_percent"] = rolling["units_percent"]
    counts["coverage_unit_hours_percent"] = rolling["unit_hours_percent"]
    verdict, basis = (since_stats, "since-cutover") if since_stats is not None else (rolling, "rolling")
    counts["coverage_verdict_basis"] = basis
    if verdict["executed"]:
        low = [name for name, v in (("units", verdict["units_percent_exact"]), ("unit-hours", verdict["unit_hours_percent_exact"]))
               if v is not None and v < a.coverage_percent]                  # the unrounded values: 59.57 is below 60
        if low:
            alarm = {"alarm": "coverage", "basis": basis, "below": low, "units_percent": verdict["units_percent"],
                     "unit_hours_percent": verdict["unit_hours_percent"], "limit": a.coverage_percent, "executed": verdict["executed"]}
            if basis == "since-cutover":
                alarm["since"] = counts["since_cutover"]["since"]
            alarms.append(alarm)
    else:
        na.append("coverage" if basis == "rolling" else "coverage-since-cutover")
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
    k = c["serves_kinds"]
    lines.append(f"executed serves: ranked {k['ranked']}, exempt {k['exempt']}, id without a ledger row {k['no_row']} (not ranked), other wording {k['unrecognised']} "
                 f"(not ranked), no serves line {k['no_serves_line']} ({k['ranked_by_name']} ranked by name) | ranking basis: {c['ranking_basis']}")
    last = c["minutes_since_last_execution"]
    lines.append("last execution: " + ("none on record" if last is None else f"{last} min ago"))
    r = c["rolling"]
    if r["executed"]:
        lines.append(f"coverage ROLLING {r['hours']:g} h (context{', not the verdict' if c['coverage_verdict_basis'] == 'since-cutover' else ''}): "
                     f"units {r['units_percent']}%, unit-hours {r['unit_hours_percent']}% of {r['executed']} units | serving nothing "
                     f"{r['serves_nothing_units']} units, {r['serves_nothing_hours']:g} h of {r['total_hours']:g} h")
    sc = c["since_cutover"]
    if sc is None:
        lines.append(f"coverage SINCE CUTOVER: not set ({c['cutover_note']}); the rolling figure is the verdict")
    elif sc["executed"]:
        lines.append(f"coverage SINCE CUTOVER {sc['since']} ({sc['source']}) - THE VERDICT: units {sc['units_percent']}%, unit-hours "
                     f"{sc['unit_hours_percent']}% of {sc['executed']} units | serving nothing {sc['serves_nothing_units']} units, "
                     f"{sc['serves_nothing_hours']:g} h of {sc['total_hours']:g} h")
    else:
        lines.append(f"coverage SINCE CUTOVER {sc['since']} ({sc['source']}): no unit executed since yet (n/a)")
    lines.append(f"growth units executed {c['growth_executed']}" + (f", partial {c['growth_partial_percent']}%" if "growth_partial_percent" in c else ""))
    for read in c["slot_reads"]:
        note = (f" + {read['slots_blocked_capacity']} blocked by capacity" + (f" ({read['blocker']})" if read.get("blocker") else " (blocker not named)")
                if read.get("slots_blocked_capacity") else "")
        lines.append(f"slot read {read['activity']}: {read['idle_slots']} idle{note}, read {read['minutes_since_read']} min ago")
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
    p.add_argument("--since", default="", help="the roster remap's cutover, ISO 8601 UTC: the coverage verdict counts units executed after it "
                                               "(default: the state file, else git)")
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
    if a.since and stamp(a.since) is None:
        print("strategy_conformance: --since is not an ISO 8601 time", file=sys.stderr)
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
