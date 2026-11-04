#!/usr/bin/env python3
"""Task unit queue for the Last War routine.

Implements the pool mechanics of the task unit queue design
(_conventions_/local-conventions/task-unit-queue-design.md). A task
unit is a Markdown file whose frontmatter is one structured YAML
document describing the task, its queue state and, once executed, its
result and result stats - so tools can gather status and statistics
reliably without scraping prose. Units move inbox -> claimed -> done
by atomic rename, claims carry a lease, an executor batch is bounded
to 15 minutes, and exactly one executor holds the device token.

This tool manages files only. It never touches the game or the device;
executors do the playing and call this tool around their work.

Usage:
  queue.py [--root DIR] enqueue --regular vip [--priority 1]
             [--expires-at ISO] [--est-minutes 3] [--window TEXT]
  queue.py [--root DIR] list [--state inbox|claimed|done]
  queue.py [--root DIR] next [--budget-minutes 15]
  queue.py [--root DIR] claim --unit UNIT --executor NAME
             [--lease-minutes 20]
  queue.py [--root DIR] complete --unit UNIT --status done
             [--summary TEXT] [--claimed-items a,b] [--evidence PATH]
             [--follow-up TEXT] [--stat key=value ...]
             # complete records the missing keys in
             # result.stats_missing (empty when complete) and warns
             # on stdout (exit still 0) when the closing omits a
             # required result.stats key, so an incomplete closing
             # is flagged in the result itself at the moment it is
             # made instead of surfacing only in the retro.
  queue.py [--root DIR] release --unit UNIT      # partial: back to inbox
  queue.py [--root DIR] token-acquire --executor NAME
  queue.py [--root DIR] token-release --executor NAME
  queue.py [--root DIR] reap                      # expired leases to inbox
             # reap, sync and plan warn on stdout (exit still 0)
             # when the root holds no pool state directory at
             # all, so a wrong root never reports a silent zero
  queue.py [--root DIR] stats [--format text|yaml|json]
             # stats names stalled priority-1 inbox units
             # (age over 4h) under stalled_priority1, for the
             # round summary to name instead of staying silent.
             # stats also names expired units whose whole window
             # saw no executed closing, under stall_expired, so
             # the retro can triage stall-attributable expiries
             # instead of counting every expiry as ordinary.
             # stats also reports the newest executed closing
             # (newest_finished_at, newest_finished_age_minutes,
             # evidence_stale over 180 minutes), so the round
             # summary can tell a stalled pipeline from a quiet
             # one without hand-reading records; the 3-hour
             # active-window alert and its once-per-stall dedup
             # stay the summary job clause (issue #129).
  queue.py [--root DIR] sync [--due-json FILE]
             # one ticker production pass: reap, expire stale
             # units, drop inbox copies already closed in done
             # (issue #213), then enqueue one unit per regular
             # the tracker marks due (idempotent);
             # without --due-json it calls _tools_/regulars.py todo
  queue.py [--root DIR] plan [--hours N]
             # stage the horizon's windows: segment anchors,
             # daily resets, Thursdays, and fixed local clock
             # slots (cadence fixed-slots, slots in fixed_slots,
             # expiry clock time in expires_local, chain prefix
             # in chain_id_prefix); sync never stages fixed-slot
             # regulars, plan owns them

--root defaults to the repository _queue_ folder; tests point it at a
scratch directory.

Frontmatter dialect: the small YAML subset this tool writes - plain
scalars, [a, b] flow lists, and mappings nested by 2 space indents
(the result block and its stats). No external YAML library is needed.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

UNIT_CAP_MINUTES = 15           # owner rule 2026-10-28: per unit
DEFAULT_LEASE_MINUTES = 20
DEFAULT_EST_MINUTES = 5
DEFAULT_MAX_ATTEMPTS = 3
# Required result.stats keys, per section 14 of the task unit queue
# design (mirrored in _tools_/retro_report.py REQUIRED_KEYS):
# target, achieved, resources_gained, costs and verified are always
# required; blocker_category is required whenever the unit fell short
# of its target or closed partial, failed or skipped-needs-owner.
REQUIRED_STATS_KEYS = ("target", "achieved", "resources_gained",
                       "costs", "verified")
SHORT_CLOSING_STATUSES = ("partial", "failed", "skipped-needs-owner")
STATES = ("inbox", "claimed", "done")
TOKEN_NAME = "device-token.md"
FM_ORDER = ["unit", "regular", "activity", "segment", "priority",
            "created_at", "expires_at", "planned_for", "not_before",
            "window", "est_minutes",
            "chain_id", "chain_seq", "attempts", "max_attempts",
            "claimed_by", "claimed_at", "lease_until", "result"]
RESULT_ORDER = ["status", "started_at", "finished_at",
                "duration_seconds", "executor", "summary", "claimed",
                "claimed_count", "evidence", "follow_up", "stats",
                "stats_missing", "stats_warnings"]


def now_utc():
    return datetime.now(timezone.utc).replace(microsecond=0)


def iso(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def parse_iso(text):
    if not text or not isinstance(text, str):
        return None
    try:
        return datetime.strptime(text, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=timezone.utc)
    except ValueError:
        return None


# ---------------------------------------------------------------------
# Frontmatter subset: parse and serialize
# ---------------------------------------------------------------------

def _scalar(text):
    text = text.strip()
    if text.startswith("[") and text.endswith("]"):
        inner = text[1:-1].strip()
        return [i.strip() for i in inner.split(",")] if inner else []
    if re.fullmatch(r"-?\d+", text):
        return int(text)
    return text


def parse_frontmatter(text):
    """Return (fields, body). fields is a nested dict."""
    m = re.match(r"---\n(.*?)\n---\n?(.*)", text, re.S)
    if not m:
        return {}, text
    fields = {}
    stack = [(-1, fields)]          # (indent, container)
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        key, _, value = line.strip().partition(":")
        key = key.strip()
        value = value.strip()
        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if value == "":
            child = {}
            parent[key] = child
            stack.append((indent, child))
        else:
            parent[key] = _scalar(value)
    return fields, m.group(2)


def _fmt(value):
    if isinstance(value, list):
        return "[" + ", ".join(str(v) for v in value) + "]"
    return str(value)


def dump_frontmatter(fields):
    lines = ["---"]
    for key in FM_ORDER:
        if key not in fields:
            continue
        value = fields[key]
        if isinstance(value, dict):
            lines.append(f"{key}:")
            order = RESULT_ORDER if key == "result" else list(value)
            for sub in order:
                if sub not in value:
                    continue
                subval = value[sub]
                if isinstance(subval, dict):
                    lines.append(f"  {sub}:")
                    for k2, v2 in subval.items():
                        lines.append(f"    {k2}: {_fmt(v2)}")
                else:
                    lines.append(f"  {sub}: {_fmt(subval)}")
        elif value in ("", None):
            lines.append(f"{key}:")
        else:
            lines.append(f"{key}: {_fmt(value)}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def read_unit(path):
    with open(path, encoding="utf-8") as fh:
        return parse_frontmatter(fh.read())


def write_unit(path, fields, body):
    if body and not body.startswith("\n"):
        body = "\n" + body
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(dump_frontmatter(fields) + body)


# ---------------------------------------------------------------------
# Pool helpers
# ---------------------------------------------------------------------

def state_dir(root, state):
    return os.path.join(root, state)


def unit_path(root, state, unit):
    return os.path.join(state_dir(root, state), unit + ".md")


def find_unit(root, unit):
    for state in STATES:
        path = unit_path(root, state, unit)
        if os.path.exists(path):
            return state, path
    return None, None


def list_units(root, state):
    folder = state_dir(root, state)
    if not os.path.isdir(folder):
        return []
    out = []
    for name in sorted(os.listdir(folder)):
        if name.endswith(".md") and name != TOKEN_NAME:
            fields, _ = read_unit(os.path.join(folder, name))
            fields["_state"] = state
            fields["_file"] = name
            out.append(fields)
    return out


def pool_root_warning(root):
    """Warning when root holds no pool state directory at all.

    A wrong root reads as an empty pool today: list_units returns
    [] for a missing folder, so reap on a root that is not a pool
    reports expired 0 with nothing to show it never saw the pool
    (issue #199 follow-up: the 2143 run's wrong-root scratch run
    did exactly that). A pool that exists but is empty still has
    its state directories, so only the no-directory case warns.
    Warning only, never a block, matching complete's convention.
    """
    if any(os.path.isdir(state_dir(root, s)) for s in STATES):
        return ""
    return (f"warning: pool root {root} holds no inbox, claimed "
            "or done directory - the counts below describe an "
            "empty or wrong root, not the live pool")


# Aging against starvation (IMP-20261031-09, loop review
# 2026-10-31 open link 4): a no-expiry low-priority chained unit
# used to sort behind every expiring unit forever, because expiry
# is the primary pick key and age was only a tiebreak - the
# 2026-10-30 zombie chain successor was crowded out for five
# beats that way. Two bounded boosts, both computed from
# created_at at pick time and never written back to the unit:
# - effective priority improves by 1 per AGING_STEP_HOURS waited,
#   floored at 1, so a waiting unit climbs the tiebreak order;
# - a unit with no expiry gets a soft deadline of
#   NO_EXPIRY_SOFT_DEADLINE_HOURS after creation, so its
#   effective expiry stops being "never" and it eventually sorts
#   ahead of expiring units whose deadlines are still further out,
#   while still yielding to genuinely imminent expiries. A unit
#   with a real expiry keeps that expiry - aging never moves a
#   hard deadline.
AGING_STEP_HOURS = 2
NO_EXPIRY_SOFT_DEADLINE_HOURS = 2
# Aged priority-1 escalation (issue #128): an inbox unit at
# priority 1 that has waited longer than STALLED_PRIORITY1_HOURS
# without being claimed is stalled - sync gives unscheduled ones
# a real window and stats names every stalled one, so no
# owner-named unit ages in silence.
STALLED_PRIORITY1_HOURS = 4
EVIDENCE_STALE_MINUTES = 180  # issue #129: the round-summary
# stall clause fires when the newest execution evidence is over
# 3 hours old; the tool reports the age, the summary job owns
# the active window and the once-per-stall alert.
AGED_P1_WINDOW_HOURS = 4


def pick_key(fields, now=None):
    """Pick order with aging: effective expiry, then effective
    priority, then age. Units with a real expiry sort as before
    when fresh; no-expiry units gain the soft deadline above."""
    if now is None:
        now = now_utc()
    expires = parse_iso(fields.get("expires_at", ""))
    try:
        priority = int(fields.get("priority", 3))
    except (TypeError, ValueError):
        priority = 3
    created = parse_iso(fields.get("created_at", ""))
    if expires is not None:
        effective_expires = expires
    elif created is not None:
        effective_expires = created + timedelta(
            hours=NO_EXPIRY_SOFT_DEADLINE_HOURS)
    else:
        effective_expires = datetime.max.replace(tzinfo=timezone.utc)
    if created is not None and now > created:
        age_hours = (now - created).total_seconds() / 3600.0
        steps = int(age_hours // AGING_STEP_HOURS)
        effective_priority = max(1, priority - steps)
    else:
        effective_priority = priority
    created_sort = created or datetime.min.replace(tzinfo=timezone.utc)
    return (effective_expires, effective_priority, created_sort)


# ---------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------

# Production metadata for sync (design sections 4 and 6). Estimates
# stay under the 15 minute unit cap; priorities follow the classes in
# the design - vip expires at the daily reset, the windowed regulars
# score inside live windows, the rest are standard. The scout
# entries are the Phase 2 seeds of the perception design (section 9
# of perception-driven-queue.md) - scout passes are windowed work at
# priority 2, seeded at 10 minutes until the pool learns better.
SYNC_PRIORITY = {"vip": 1, "zero-sweep": 1, "passes": 2, "arms-race": 2, "radar": 2,
                 "donations": 2, "trucks": 2, "events": 2,
                 "scout": 2, "scout-midday": 2}
SYNC_EST_MINUTES = {"mail": 4, "help": 2, "gifts": 3, "vip": 2,
                    "passes": 5, "secrets": 6, "treasures": 2,
                    "radar": 10, "survivors": 3, "harvest": 3,
                    "trucks": 12, "train": 4, "training": 4,
                    "donations": 4, "events": 10, "arms-race": 12,
                    "ghost-ops": 8, "star-ceremony": 3,
                    "duel-score": 2,
                    "scout": 10, "scout-midday": 10, "zero-sweep": 15}
LOCAL_TZ = ZoneInfo("America/Los_Angeles")


def next_reset_utc(reset_local):
    """Next occurrence of a local HH:MM reset, as a UTC ISO string."""
    try:
        hh, mm = (int(x) for x in reset_local.split(":"))
    except (ValueError, AttributeError):
        return ""
    now_local = datetime.now(LOCAL_TZ)
    candidate = now_local.replace(hour=hh, minute=mm, second=0,
                                  microsecond=0)
    if candidate <= now_local:
        candidate += timedelta(days=1)
    return iso(candidate.astimezone(timezone.utc))


def typical_minutes(root, regular):
    """Typical execution minutes for one task type, learned from the
    pool itself - the median duration of its completed units, in
    minutes rounded up and clamped to the unit cap, once at least 3
    completed samples exist; the static production estimate before
    that. Returns (minutes, sample_count)."""
    samples = []
    for f in list_units(root, "done"):
        if f.get("regular") != regular:
            continue
        result = f.get("result", {})
        if isinstance(result, dict) and \
                result.get("status") == "done":
            dur = result.get("duration_seconds")
            if isinstance(dur, int) and dur > 0:
                samples.append(dur)
    if len(samples) < 3:
        return SYNC_EST_MINUTES.get(regular, DEFAULT_EST_MINUTES), \
            len(samples)
    samples.sort()
    median = samples[len(samples) // 2]
    minutes = -(-median // 60)          # ceil to whole minutes
    return max(1, min(UNIT_CAP_MINUTES, minutes)), len(samples)


def write_new_unit(root, fields, regular):
    os.makedirs(state_dir(root, "inbox"), exist_ok=True)
    body = (f"# {regular}\n\nProduced by _tools_/queue.py. The "
            "executor reads the activity metadata and the standing "
            "rules before acting.\n")
    write_unit(unit_path(root, "inbox", fields["unit"]), fields, body)


def _fixed_slot_regulars():
    """Ids of fixed-slots regulars from the roster beside this tool.

    Returns an empty set when the roster is unreadable, so the
    caller degrades to the not_before guard instead of failing
    the producer pass.
    """
    try:
        with open(os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "regulars.json"),
            encoding="utf-8") as fh:
            regs = json.load(fh)["regulars"]
    except (OSError, ValueError, KeyError, TypeError):
        return set()
    return {r.get("id") for r in regs
            if r.get("cadence") == "fixed-slots" and r.get("id")}


def _window_aged_priority1(root):
    """Attach a real window to aged unscheduled priority-1 inbox
    units (issue #128 fix 1). Called by both producers - sync and
    plan - so whichever runs first windows the unit; the function
    is idempotent, so the second producer is a no-op for it.
    The windowed execution path keys on
    planned_for windows, so a unit produced without one - the
    owner-named crystal-shop and glittering-market units - is
    bypassed indefinitely even though queue.py next already sorts
    it first. Giving it planned_for=now, an empty not_before and a
    4 hour expiry puts it inside the windowed path and, if it
    still is not executed, makes it surface as an expired miss
    instead of aging silently. Idempotent: a unit with a
    planned_for is never touched again, and the (regular,
    planned_for) invariant is respected. Returns the units
    windowed.
    Two exemptions (issue #147): a fixed-slots regular is never
    re-timed - plan owns its slot timing, and re-timing destroyed
    the 2026-11-02 final pre-reset sweep (its 18:30 slot and 19:00
    reset expiry were rewritten to now and now+4h by the 17:55
    tick, 35 minutes before its slot); and a unit whose
    not_before is still in the future is waiting for its slot,
    not stalled, so it is never re-timed either. A fixed-slot
    unit past its slot is still covered by expiry: it always
    carries a reset expiry, so _expire_stale surfaces it as a
    miss without any windowing.
    """
    stamp = now_utc()
    planned_iso = iso(stamp)
    fixed_slots = _fixed_slot_regulars()
    taken = {(f.get("regular"), f.get("planned_for"))
             for state in STATES for f in list_units(root, state)
             if f.get("planned_for")}
    windowed = []
    for f in list_units(root, "inbox"):
        unit = f.get("unit")
        if not unit or f.get("planned_for"):
            continue
        try:
            priority = int(f.get("priority", 3))
        except (TypeError, ValueError):
            continue
        if priority != 1:
            continue
        if f.get("regular") in fixed_slots:
            continue
        not_before = parse_iso(f.get("not_before", ""))
        if not_before is not None and not_before > stamp:
            continue
        created = parse_iso(f.get("created_at", ""))
        if created is None:
            continue
        if (stamp - created).total_seconds() <= \
                STALLED_PRIORITY1_HOURS * 3600:
            continue
        if (f.get("regular"), planned_iso) in taken:
            continue
        state, path = find_unit(root, unit)
        if state != "inbox" or path is None:
            continue
        fields, body = read_unit(path)
        if fields.get("planned_for"):
            continue
        fields["planned_for"] = planned_iso
        fields["not_before"] = ""
        fields["expires_at"] = iso(
            stamp + timedelta(hours=AGED_P1_WINDOW_HOURS))
        write_unit(path, fields, body)
        taken.add((f.get("regular"), planned_iso))
        windowed.append(unit)
    return windowed


def cmd_sync(args):
    warning = pool_root_warning(args.root)
    if warning:
        print(warning)
    # 1. reap expired claims, expire stale inbox units, and drop
    # inbox copies of units already closed in done (issue #213)
    reaped = _reap_claimed(args.root)
    expired = _expire_stale(args.root)
    stale_done_dropped = _drop_done_duplicates(args.root)
    # 2. load the due list
    if args.due_json:
        with open(args.due_json, encoding="utf-8") as fh:
            due_doc = json.load(fh)
    else:
        tracker = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "regulars.py")
        out = subprocess.run(
            [sys.executable, tracker, "todo", "--json"],
            capture_output=True, text=True, check=True)
        due_doc = json.loads(out.stdout)
    due_items = [i for i in due_doc.get("items", []) if i.get("due")]
    # 3. produce the unit for each due regular's current window -
    #    the (regular, window) invariant in _produce_for_window is
    #    what keeps sync and the planner from ever duplicating
    produced, already = [], []
    now_local = datetime.now(LOCAL_TZ)
    for item in due_items:
        if item.get("cadence") == "fixed-slots":
            # Plan-produced only: the tracker carries no per-slot
            # done state, so sync staging here would mint slot
            # units outside the plan's (regular, planned_for)
            # staging; plan owns fixed-slot production.
            continue
        planned_local = cycle_start_local(item, now_local)
        unit = _produce_for_window(
            args.root, item, planned_local,
            duel_window_text(item["id"], planned_local))
        if unit:
            produced.append(unit)
        else:
            already.append(item["id"])
    # 4. window aged unscheduled priority-1 units (issue #128) -
    #    runs every tick, so the next tick after the 4 hour mark
    #    windows the unit instead of letting it age further.
    aged_p1_windowed = _window_aged_priority1(args.root)
    print(json.dumps({"reaped": reaped, "expired": expired,
                      "stale_done_dropped": stale_done_dropped,
                      "due": len(due_items), "produced": produced,
                      "already_queued": already,
                      "aged_p1_windowed": aged_p1_windowed},
                     ensure_ascii=False))
    return 0


def chain_seq_next(root, chain_id):
    seq = 0
    for state in STATES:
        for f in list_units(root, state):
            if f.get("chain_id") == chain_id:
                try:
                    seq = max(seq, int(f.get("chain_seq", 0)))
                except (TypeError, ValueError):
                    pass
    return seq + 1


SEGMENT_ANCHORS_PLAN = {1: 6 * 60 + 3, 2: 6 * 60 + 30, 3: 6 * 60 + 57}
DUEL_ANCHOR_LOCAL = datetime(2026, 10, 25, 19, 0)
RADAR_RELEASE_DAYS = {1, 3, 5}


def _parse_hhmm(text):
    """Parse a local HH:MM clock time, or return None when malformed."""
    try:
        hh, mm = (int(x) for x in str(text).split(":"))
    except (ValueError, AttributeError):
        return None
    if not 0 <= hh <= 23 or not 0 <= mm <= 59:
        return None
    return hh, mm


def _fixed_slots(item):
    """Sorted (hour, minute) fixed slots of a fixed-slots regular."""
    slots = []
    for raw in item.get("fixed_slots", []) or []:
        parsed = _parse_hhmm(raw)
        if parsed is not None:
            slots.append(parsed)
    return sorted(set(slots))


def _next_local_time(after_local, hhmm):
    """Next occurrence of a local HH:MM strictly after after_local."""
    hh, mm = hhmm
    cand = after_local.replace(hour=hh, minute=mm, second=0,
                               microsecond=0)
    if cand <= after_local:
        cand += timedelta(days=1)
    return cand


def cycle_start_local(item, when_local):
    """Start of the cadence window containing when_local, mirroring
    the tracker rules - every-run windows start at the segment
    anchors every 4 hours, daily-reset at the reset boundary
    (the absolute reset_utc instant when the regular carries one,
    else the reset_local wall time),
    weekly-thu at Thursday 00:00, fixed-slots at the latest
    listed slot at or before now (yesterday's last slot before
    the first slot of the day)."""
    cadence = item.get("cadence", "")
    if cadence == "fixed-slots":
        slots = _fixed_slots(item)
        if slots:
            cur = when_local.hour * 60 + when_local.minute
            past = [s for s in slots if s[0] * 60 + s[1] <= cur]
            if past:
                hh, mm = past[-1]
                return when_local.replace(hour=hh, minute=mm, second=0,
                                          microsecond=0)
            hh, mm = slots[-1]
            day = when_local - timedelta(days=1)
            return day.replace(hour=hh, minute=mm, second=0,
                               microsecond=0)
        # No slots listed: fall through to the anchor handling below.
    if cadence == "daily-reset":
        parsed_utc = _parse_hhmm(item.get("reset_utc", ""))
        if parsed_utc is not None:
            # Absolute UTC boundary (issue #247): the game day
            # resets at 02:00 UTC, so the local wall time shifts
            # with daylight saving - 18:00 PST / 19:00 PDT. A wall
            # step would keep the old day an hour too long after
            # the transition, exactly the duel.py failure in #242.
            # Timestamps are the absolute measure here, as in
            # duel.py: wall-clock arithmetic on an aware datetime
            # sharing one tzinfo is not elapsed time.
            hh, mm = parsed_utc
            if when_local.tzinfo is None:
                when_local = when_local.replace(tzinfo=LOCAL_TZ)
            when_utc = when_local.astimezone(timezone.utc)
            cand = when_utc.replace(hour=hh, minute=mm, second=0,
                                    microsecond=0)
            if cand > when_utc:
                cand -= timedelta(days=1)
            return cand.astimezone(LOCAL_TZ)
        reset = item.get("reset_local") or "19:00"
        hh, mm = (int(x) for x in reset.split(":"))
        boundary = when_local.replace(hour=hh, minute=mm, second=0,
                                      microsecond=0)
        if when_local < boundary:
            boundary -= timedelta(days=1)
        return boundary
    if cadence == "weekly-thu":
        day = when_local - timedelta(days=(when_local.weekday() - 3) % 7)
        return day.replace(hour=0, minute=0, second=0, microsecond=0)
    anchor = SEGMENT_ANCHORS_PLAN.get(item.get("segment", 1), 363)
    cur = when_local.hour * 60 + when_local.minute
    delta = (cur - anchor) % 240
    return when_local - timedelta(minutes=delta,
                                  seconds=when_local.second,
                                  microseconds=when_local.microsecond)


def plan_windows(item, now_local, horizon_end):
    """Window starts to stage for one regular - the current window
    plus every window that starts inside the horizon."""
    cadence = item.get("cadence", "")
    if cadence == "fixed-slots":
        slots = _fixed_slots(item)
        if not slots:
            return []
        out = []
        start = cycle_start_local(item, now_local)
        day = start.replace(hour=0, minute=0, second=0, microsecond=0)
        while day <= horizon_end:
            for hh, mm in slots:
                cand = day.replace(hour=hh, minute=mm, second=0,
                                   microsecond=0)
                if start <= cand <= horizon_end:
                    out.append(cand)
            day += timedelta(days=1)
        return out
    if cadence == "daily-reset":
        step = timedelta(days=1)
    elif cadence == "weekly-thu":
        step = timedelta(days=7)
    else:
        step = timedelta(hours=4)
    out = []
    cand = cycle_start_local(item, now_local)
    while cand <= horizon_end:
        if cadence != "weekly-thu" or \
                cand + timedelta(days=1) > now_local:
            out.append(cand)
        if cadence == "daily-reset" and item.get("reset_utc"):
            # Absolute 24h step, not a wall-clock day: across the
            # daylight-saving transition a wall step would move
            # the boundary to 03:00 UTC instead of 02:00 UTC.
            cand = datetime.fromtimestamp(cand.timestamp() + 86400,
                                          tz=LOCAL_TZ)
        else:
            cand += step
    return out


def duel_window_text(regular, planned_local):
    naive = planned_local.replace(tzinfo=None)
    duel_day = (naive - DUEL_ANCHOR_LOCAL).days % 7 + 1
    if regular == "radar":
        posture = "release" if duel_day in RADAR_RELEASE_DAYS \
            else "stack"
        return f"duel day {duel_day} - radar {posture}"
    if regular == "trucks" and duel_day == 2:
        return "duel day 2 - UR trucks, Mega UR only"
    if regular == "arms-race":
        return f"duel day {duel_day}"
    if regular == "duel-score":
        return f"duel day {duel_day} - target 3600000"
    return ""


def _produce_for_window(root, item, planned_local, window=""):
    """Enqueue the unit for one (regular, window) pair, or return
    None when that pair already exists in any state - the pool's
    anti-duplication invariant, shared by sync and plan."""
    regular = item["id"]
    planned_utc = planned_local.astimezone(timezone.utc)
    planned_iso = iso(planned_utc)
    for state in STATES:
        for f in list_units(root, state):
            if f.get("regular") == regular and \
                    f.get("planned_for") == planned_iso:
                return None
    cadence = item.get("cadence", "")
    if cadence == "fixed-slots" and item.get("expires_local"):
        exp = _parse_hhmm(item.get("expires_local"))
        if exp is not None:
            expires_dt = _next_local_time(
                planned_local, exp).astimezone(timezone.utc)
        else:
            expires_dt = planned_utc + timedelta(hours=4)
    elif cadence in ("daily-reset", "weekly-thu"):
        expires_dt = planned_utc + timedelta(days=1)
    else:
        expires_dt = planned_utc + timedelta(hours=4)
    chain_id, chain_seq = "", ""
    prefix = item.get("chain_id_prefix", "")
    if prefix:
        chain_id = prefix + planned_local.strftime("%Y-%m-%d")
        slots = _fixed_slots(item)
        hhmm = (planned_local.hour, planned_local.minute)
        if cadence == "fixed-slots" and hhmm in slots:
            chain_seq = slots.index(hhmm) + 1
    fields = {
        "unit": f"{regular}-{planned_local.strftime('%Y-%m-%d-%H%M')}",
        "regular": regular,
        "activity": item.get("activity", ""),
        "segment": item.get("segment", ""),
        "priority": SYNC_PRIORITY.get(regular, 3),
        "created_at": iso(now_utc()),
        "expires_at": iso(expires_dt),
        "planned_for": planned_iso,
        "not_before": planned_iso if planned_utc > now_utc() else "",
        "window": window,
        "est_minutes": typical_minutes(root, regular)[0],
        "chain_id": chain_id, "chain_seq": chain_seq, "attempts": 0,
        "max_attempts": DEFAULT_MAX_ATTEMPTS,
        "claimed_by": "", "claimed_at": "", "lease_until": "",
    }
    if os.path.exists(unit_path(root, "inbox", fields["unit"])):
        return None
    write_new_unit(root, fields, regular)
    return fields["unit"]


def _reap_claimed(root):
    moved = 0
    stamp = now_utc()

    class Shim:
        pass
    for f in list_units(root, "claimed"):
        lease = parse_iso(f.get("lease_until", ""))
        if lease and lease <= stamp and f.get("unit"):
            shim = Shim()
            shim.root = root
            if _release(shim, f["unit"]) == 0:
                moved += 1
    return moved


def _expire_stale(root):
    """Inbox units whose window has fully passed move to done with
    status expired - the next window's unit supersedes them, and the
    statistics keep the miss visible instead of losing it. A done
    file already carrying an execution result for the same unit is
    never overwritten: the stale inbox copy is dropped and the
    executed record kept. A records-branch snapshot can hold both
    copies at once, and expiry used to clobber the executed result
    with an expiry (queue-planning 1457 follow-up)."""
    moved = 0
    stamp = now_utc()
    for f in list_units(root, "inbox"):
        expires = parse_iso(f.get("expires_at", ""))
        if expires and expires <= stamp and f.get("unit"):
            done_path = unit_path(root, "done", f["unit"])
            if os.path.exists(done_path):
                print(f"warning: {f['unit']} already has a done "
                      f"record - dropping the stale inbox copy "
                      f"instead of overwriting it with an expiry",
                      file=sys.stderr)
                os.remove(unit_path(root, "inbox", f["unit"]))
                continue
            state, path = find_unit(root, f["unit"])
            fields, body = read_unit(path)
            fields["result"] = {
                "status": "expired", "started_at": "",
                "finished_at": iso(stamp), "duration_seconds": "",
                "executor": "",
                "summary": "window passed before execution",
                "claimed": [], "claimed_count": 0, "evidence": "",
                "follow_up": "none", "stats": {}}
            os.makedirs(state_dir(root, "done"), exist_ok=True)
            write_unit(path, fields, body)
            os.rename(path, unit_path(root, "done", f["unit"]))
            moved += 1
    return moved


def _has_done_record(root, unit):
    """True when done holds a result-bearing record for unit.

    A bare done file with no result status is not a completed
    execution - it may be a placeholder or a half-written move -
    so it does not suppress the inbox copy. Any result status
    (done, partial, failed, skipped-needs-owner, or expired)
    does: the unit already closed, and the inbox copy is a
    stale duplicate, not fresh work.
    """
    if not unit:
        return False
    path = unit_path(root, "done", unit)
    if not os.path.exists(path):
        return False
    fields, _ = read_unit(path)
    result = fields.get("result", {})
    return isinstance(result, dict) and bool(result.get("status"))


def _drop_done_duplicates(root):
    """Drop inbox copies of units already closed in done (issue #213).

    The two units in issue #213 both carry an empty expires_at,
    so _expire_stale never sees them: expiry is gated on a window
    that no-expiry chain and enqueue units do not have, and
    cmd_next / cmd_claim then re-present and re-claim the stale
    inbox copy - ticker-0134 re-executed both units after
    ticker-1755 had already closed them on the delivered branch.
    Dropping is result-preserving by construction: the done
    record is never touched, only the duplicate inbox file is
    removed, with a stderr warning naming the unit. Runs after
    _expire_stale in sync and plan, so an expired duplicate still
    takes the expiry path (and its existing warning) and only
    the unexpired remainder is counted here.
    """
    dropped = []
    for f in list_units(root, "inbox"):
        unit = f.get("unit")
        if unit and _has_done_record(root, unit):
            print(f"warning: {unit} already has a done record - "
                  f"dropping the stale inbox copy instead of "
                  f"re-executing it", file=sys.stderr)
            os.remove(unit_path(root, "inbox", unit))
            dropped.append(unit)
    return dropped


def cmd_plan(args):
    warning = pool_root_warning(args.root)
    if warning:
        print(warning)
    reaped = _reap_claimed(args.root)
    expired = _expire_stale(args.root)
    stale_done_dropped = _drop_done_duplicates(args.root)
    defs_path = args.regulars_json or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "regulars.json")
    with open(defs_path, encoding="utf-8") as fh:
        regs = json.load(fh)["regulars"]
    # Tracker truth for the current window - a regular the tracker
    # already counts as done for this window gets no phantom unit;
    # future windows are always staged.
    if args.tracker_json:
        with open(args.tracker_json, encoding="utf-8") as fh:
            tracker_doc = json.load(fh)
    else:
        tracker = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "regulars.py")
        out = subprocess.run(
            [sys.executable, tracker, "list", "--json"],
            capture_output=True, text=True, check=True)
        tracker_doc = json.loads(out.stdout)
    due_now = {i["id"]: bool(i.get("due"))
               for i in tracker_doc.get("items", [])}
    now_local = datetime.now(LOCAL_TZ)
    horizon_end = now_local + timedelta(hours=args.hours)
    planned, present, skipped_done = [], 0, 0
    for item in regs:
        current = cycle_start_local(item, now_local)
        for w in plan_windows(item, now_local, horizon_end):
            # The tracker has no per-slot done state, so the
            # current-window skip must not drop a fixed-slot unit;
            # the (regular, planned_for) dedupe in _produce already
            # prevents re-staging an existing window.
            if w == current and item.get("cadence") != "fixed-slots" \
                    and not due_now.get(item["id"], True):
                skipped_done += 1
                continue
            unit = _produce_for_window(
                args.root, item, w, duel_window_text(item["id"], w))
            if unit:
                planned.append(unit)
            else:
                present += 1
    # Window aged unscheduled priority-1 units (issue #128) - plan
    # is the hourly producer that demonstrably runs, while sync
    # runs only when the ticker invokes it; the 2240 planner run
    # staged 11 units yet left the aged glittering-market unit
    # unwindowed because plan never called this step. Idempotent,
    # so sync calling it too is harmless.
    aged_p1_windowed = _window_aged_priority1(args.root)
    print(json.dumps({"horizon_hours": args.hours, "reaped": reaped,
                      "expired": expired,
                      "stale_done_dropped": stale_done_dropped,
                      "planned": planned,
                      "already_present": present,
                      "skipped_done_current": skipped_done,
                      "aged_p1_windowed": aged_p1_windowed},
                     ensure_ascii=False))
    return 0


def cmd_enqueue(args):
    if args.est_minutes > UNIT_CAP_MINUTES:
        print(f"refused: est_minutes {args.est_minutes} exceeds the "
              f"{UNIT_CAP_MINUTES} minute unit cap - split the task")
        return 1
    chain_seq = ""
    if args.chain_id:
        # One unit, one task type - a chain is homogeneous. Refuse to
        # extend a chain with a different regular than its existing
        # units, so per-type statistics stay clean.
        for state in STATES:
            for f in list_units(args.root, state):
                if f.get("chain_id") == args.chain_id and \
                        f.get("regular") not in ("", args.regular):
                    print(f"refused: chain {args.chain_id} belongs to "
                          f"regular {f.get('regular')}, not "
                          f"{args.regular}")
                    return 1
        chain_seq = chain_seq_next(args.root, args.chain_id)
        unit = f"{args.regular}-{args.chain_id}-{chain_seq:03d}"
    else:
        unit = f"{args.regular}-{now_utc().strftime('%Y-%m-%d-%H%M')}"
    path = unit_path(args.root, "inbox", unit)
    if os.path.exists(path):
        print(f"already queued: {unit}")
        return 1
    fields = {
        "unit": unit, "regular": args.regular,
        "activity": args.activity or "", "segment": args.segment or "",
        "priority": args.priority,
        "created_at": iso(now_utc()),
        "expires_at": args.expires_at or "",
        "planned_for": "", "not_before": args.not_before or "",
        "window": args.window or "",
        "est_minutes": args.est_minutes,
        "chain_id": args.chain_id or "", "chain_seq": chain_seq,
        "attempts": 0, "max_attempts": args.max_attempts,
        "claimed_by": "", "claimed_at": "", "lease_until": "",
    }
    body = (f"# {args.regular}\n\nProduced by _tools_/queue.py. The "
            "executor reads the activity metadata and the standing "
            "rules before acting.\n")
    os.makedirs(state_dir(args.root, "inbox"), exist_ok=True)
    write_unit(path, fields, body)
    print(f"queued {unit}")
    return 0


def cmd_list(args):
    for state in ([args.state] if args.state else list(STATES)):
        units = list_units(args.root, state)
        print(f"{state}: {len(units)}")
        for f in units:
            result = f.get("result", {})
            status = result.get("status", "") if isinstance(
                result, dict) else ""
            print(f"  {f.get('unit', f['_file'])}"
                  f"  p{f.get('priority', '?')}"
                  f"  expires {f.get('expires_at') or '-'}"
                  f"  by {f.get('claimed_by') or '-'}"
                  f"  {status}")
    return 0


def _actionable(fields, stamp):
    not_before = parse_iso(fields.get("not_before", ""))
    return not (not_before and not_before > stamp)


def cmd_next(args):
    stamp = now_utc()
    candidates = sorted(
        (f for f in list_units(args.root, "inbox")
         if _actionable(f, stamp)
         and not _has_done_record(args.root, f.get("unit"))),
        key=lambda f: pick_key(f, stamp))
    for f in candidates:
        try:
            est = int(f.get("est_minutes", DEFAULT_EST_MINUTES))
        except (TypeError, ValueError):
            est = DEFAULT_EST_MINUTES
        if est <= args.budget_minutes:
            print(f.get("unit", ""))
            return 0
    print("")
    return 0


def cmd_claim(args):
    state, path = find_unit(args.root, args.unit)
    if state != "inbox":
        print(f"cannot claim {args.unit}: state is {state}")
        return 1
    if _has_done_record(args.root, args.unit):
        print(f"cannot claim {args.unit}: already has a done "
              f"record - the inbox copy is stale, run sync to "
              f"drop it instead of re-executing it")
        return 1
    fields, body = read_unit(path)
    if not _actionable(fields, now_utc()):
        print(f"cannot claim {args.unit}: not before "
              f"{fields.get('not_before')}")
        return 1
    stamp = now_utc()
    try:
        fields["attempts"] = int(fields.get("attempts", 0)) + 1
    except (TypeError, ValueError):
        fields["attempts"] = 1
    fields["claimed_by"] = args.executor
    fields["claimed_at"] = iso(stamp)
    fields["lease_until"] = iso(stamp + timedelta(
        minutes=args.lease_minutes))
    os.makedirs(state_dir(args.root, "claimed"), exist_ok=True)
    target = unit_path(args.root, "claimed", args.unit)
    os.rename(path, target)                      # atomic claim
    write_unit(target, fields, body)
    print(f"claimed {args.unit} by {args.executor} "
          f"until {fields['lease_until']}")
    return 0


def _stat_number(value):
    """Coerce a stats scalar to a number, or None (retro _num)."""
    if isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value.replace(",", "").strip())
        except ValueError:
            return None
    return None


def missing_stats_keys(status, stats):
    """Required result.stats keys absent from a closing.

    Mirrors the retro aggregation in _tools_/retro_report.py: the
    five always-required keys, plus blocker_category when the
    unit fell short of its numeric target or closed with a
    short status. Presence counts - a key supplied with an
    empty value is present, exactly as the retro counts it.
    """
    missing = [key for key in REQUIRED_STATS_KEYS if key not in stats]
    target = _stat_number(stats.get("target"))
    achieved = _stat_number(stats.get("achieved"))
    fell_short = (target is not None and achieved is not None
                  and achieved < target)
    if (fell_short or status in SHORT_CLOSING_STATUSES) \
            and "blocker_category" not in stats:
        missing.append("blocker_category")
    return missing


def points_duplicates_achieved(stats):
    """True when stats.points copies stats.achieved (issue #197).

    points is score gained in this unit, not a running total
    read: a duel total read belongs in achieved only. A nonzero
    points value exactly equal to achieved is therefore a copy
    suspect - the star-ceremony unit of 2026-11-01 closed with
    points 791250 equal to its duel total achieved 791250, and
    the retro summed it as points gained. Zero equals zero is
    not flagged: a unit that gained nothing and reached nothing
    is not a copy. This is a warning, never a block: a scoring
    unit that genuinely gained its whole achieved total in one
    unit still closes, flagged for the retro to read.
    """
    if not isinstance(stats, dict):
        return False
    points = _stat_number(stats.get("points"))
    achieved = _stat_number(stats.get("achieved"))
    return (points is not None and achieved is not None
            and points != 0 and points == achieved)


def cmd_complete(args):
    state, path = find_unit(args.root, args.unit)
    if state != "claimed":
        print(f"cannot complete {args.unit}: state is {state}")
        return 1
    fields, body = read_unit(path)
    finished = now_utc()
    started = parse_iso(fields.get("claimed_at", ""))
    duration = int((finished - started).total_seconds()) if started \
        else ""
    claimed_items = [i.strip() for i in args.claimed_items.split(",")
                     if i.strip()] if args.claimed_items else []
    stats = {}
    for pair in args.stat or []:
        if "=" in pair:
            key, value = pair.split("=", 1)
            stats[key.strip()] = _scalar(value)
    missing = missing_stats_keys(args.status, stats)
    points_dup = points_duplicates_achieved(stats)
    fields["result"] = {
        "status": args.status,
        "started_at": fields.get("claimed_at", ""),
        "finished_at": iso(finished),
        "duration_seconds": duration,
        "executor": fields.get("claimed_by", ""),
        "summary": args.summary or "",
        "claimed": claimed_items,
        "claimed_count": len(claimed_items),
        "evidence": args.evidence or "",
        "follow_up": args.follow_up or "none",
        "stats": stats,
        "stats_missing": missing,
        "stats_warnings": (["points duplicates achieved"]
                           if points_dup else []),
    }
    target = unit_path(args.root, "done", args.unit)
    os.makedirs(state_dir(args.root, "done"), exist_ok=True)
    write_unit(path, fields, body)
    os.rename(path, target)
    print(f"completed {args.unit} with status {args.status}")
    if missing:
        print(f"warning: {args.unit} closes with missing required "
              f"result.stats keys: {', '.join(missing)} - the "
              f"closing counts as unverified in the retro "
              f"aggregation")
    if points_dup:
        print(f"warning: {args.unit} closes with stats.points "
              f"equal to stats.achieved - points is score gained "
              f"in this unit, not a running total read; a duel "
              f"total read belongs in achieved only")
    return 0


def _dead_letter(root, path, fields, body):
    fields["result"] = {
        "status": "failed",
        "started_at": fields.get("claimed_at", ""),
        "finished_at": iso(now_utc()),
        "duration_seconds": "",
        "executor": fields.get("claimed_by", ""),
        "summary": "attempts exhausted - dead lettered",
        "claimed": [], "claimed_count": 0,
        "evidence": "", "follow_up": "inspect and re-enqueue manually",
        "stats": {},
    }
    for key in ("claimed_by", "claimed_at", "lease_until"):
        fields[key] = ""
    os.makedirs(state_dir(root, "done"), exist_ok=True)
    target = unit_path(root, "done", fields.get("unit", ""))
    write_unit(path, fields, body)
    os.rename(path, target)


def _release(args, unit):
    state, path = find_unit(args.root, unit)
    if state != "claimed":
        return 1
    fields, body = read_unit(path)
    try:
        attempts = int(fields.get("attempts", 0))
        max_attempts = int(fields.get("max_attempts",
                                      DEFAULT_MAX_ATTEMPTS))
    except (TypeError, ValueError):
        attempts, max_attempts = 0, DEFAULT_MAX_ATTEMPTS
    if attempts >= max_attempts:
        _dead_letter(args.root, path, fields, body)
        return 0
    for key in ("claimed_by", "claimed_at", "lease_until"):
        fields[key] = ""
    fields.pop("result", None)
    os.makedirs(state_dir(args.root, "inbox"), exist_ok=True)
    target = unit_path(args.root, "inbox", unit)
    os.rename(path, target)
    write_unit(target, fields, body)
    return 0


def cmd_release(args):
    if _release(args, args.unit) != 0:
        print(f"cannot release {args.unit}: not claimed")
        return 1
    print(f"released {args.unit} back to inbox")
    return 0


def token_path(root):
    return os.path.join(state_dir(root, "claimed"), TOKEN_NAME)


def cmd_token_acquire(args):
    path = token_path(args.root)
    os.makedirs(state_dir(args.root, "claimed"), exist_ok=True)
    if os.path.exists(path):
        fields, _ = read_unit(path)
        lease = parse_iso(fields.get("lease_until", ""))
        if lease and lease > now_utc():
            print(f"token held by {fields.get('claimed_by', '?')} "
                  f"until {fields.get('lease_until')}")
            return 1
    fields = {"claimed_by": args.executor,
              "claimed_at": iso(now_utc()),
              "lease_until": iso(now_utc() + timedelta(
                  minutes=UNIT_CAP_MINUTES))}
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write("---\n"
                 f"claimed_by: {fields['claimed_by']}\n"
                 f"claimed_at: {fields['claimed_at']}\n"
                 f"lease_until: {fields['lease_until']}\n"
                 "---\n\n# Device token\n")
    os.rename(tmp, path)
    print(f"token acquired by {args.executor} "
          f"until {fields['lease_until']}")
    return 0


def cmd_token_release(args):
    path = token_path(args.root)
    if not os.path.exists(path):
        print("no token held")
        return 0
    fields, _ = read_unit(path)
    if fields.get("claimed_by") not in ("", args.executor):
        print(f"token held by {fields.get('claimed_by')}, not "
              f"{args.executor}")
        return 1
    os.remove(path)
    print(f"token released by {args.executor}")
    return 0


def cmd_reap(args):
    warning = pool_root_warning(args.root)
    if warning:
        print(warning)
    moved = _reap_claimed(args.root)
    expired = _expire_stale(args.root)
    print(f"reaped {moved} expired claim(s), "
          f"expired {expired} stale unit(s)")
    return 0


# Stall-attributable expiry (issue #133): an expired unit is
# stall-suspect when no executed closing finished inside its
# window. Executed closings are done/partial/failed/
# skipped-needs-owner records with a started_at - an expired
# record's finished_at is the reap time, not an execution, so
# it must never count as activity in another unit's window.
# Units whose window cannot be parsed are never suspects: the
# test stays conservative rather than inventing a stall.
EXECUTED_RESULT_STATUSES = ("done", "partial", "failed",
                            "skipped-needs-owner")


def window_start(fields):
    for key in ("not_before", "planned_for", "created_at"):
        stamp = parse_iso(fields.get(key, ""))
        if stamp is not None:
            return stamp
    return None


def is_stall_suspect(fields, executed_finishes):
    expires = parse_iso(fields.get("expires_at", ""))
    start = window_start(fields)
    if expires is None or start is None or not start < expires:
        return False
    return not any(start <= fin <= expires
                   for fin in executed_finishes)


def gather_stats(root):
    stamp = now_utc()
    report = {"generated_at": iso(stamp),
              "by_state": {}, "by_regular": {}, "durations_seconds": {},
              "late": [], "expired_waiting": [], "overdue_claims": [],
              "stalled_priority1": [],
              "result_status": {}, "chains": {}, "upcoming": 0,
              "stats_incomplete": 0, "stats_incomplete_units": [],
              "stats_points_dup": 0, "stats_points_dup_units": [],
              "stall_expired": 0, "stall_expired_units": [],
              "newest_finished_at": None,
              "newest_finished_age_minutes": None,
              "evidence_stale": False}
    durations = []
    reg_durations = {}
    executed_finishes = []
    newest = None
    for f in list_units(root, "done"):
        result = f.get("result", {})
        if not isinstance(result, dict):
            continue
        if result.get("status") not in EXECUTED_RESULT_STATUSES:
            continue
        if not result.get("started_at"):
            continue
        finished = parse_iso(result.get("finished_at", ""))
        if finished is not None:
            executed_finishes.append(finished)
    for state in STATES:
        units = list_units(root, state)
        report["by_state"][state] = len(units)
        for f in units:
            regular = f.get("regular", "?")
            entry = report["by_regular"].setdefault(
                regular, {"inbox": 0, "claimed": 0, "done": 0,
                          "failed": 0, "late": 0,
                          "duration_avg": None, "duration_max": None})
            entry[state] += 1
            chain = f.get("chain_id")
            if chain:
                centry = report["chains"].setdefault(
                    chain, {"done": 0, "pending": 0})
                if state == "done":
                    centry["done"] += 1
                else:
                    centry["pending"] += 1
            expires = parse_iso(f.get("expires_at", ""))
            if state == "inbox" and not _actionable(f, stamp):
                report["upcoming"] += 1
            result = f.get("result", {})
            if not isinstance(result, dict):
                result = {}
            if result.get("status") in EXECUTED_RESULT_STATUSES:
                fin = parse_iso(result.get("finished_at", ""))
                if fin is not None and (newest is None or fin > newest):
                    newest = fin
            if state == "inbox" and expires and expires <= stamp:
                report["expired_waiting"].append(f.get("unit"))
            if ((state == "done"
                    and result.get("status") == "expired")
                    or (state == "inbox" and expires
                        and expires <= stamp)) and \
                    is_stall_suspect(f, executed_finishes):
                report["stall_expired"] += 1
                report["stall_expired_units"].append({
                    "unit": f.get("unit"),
                    "window_start": iso(window_start(f)),
                    "expires_at": f.get("expires_at", "")})
            if state == "inbox":
                try:
                    prio = int(f.get("priority", 3))
                except (TypeError, ValueError):
                    prio = 3
                created = parse_iso(f.get("created_at", ""))
                if prio == 1 and created is not None and \
                        (stamp - created).total_seconds() > \
                        STALLED_PRIORITY1_HOURS * 3600:
                    report["stalled_priority1"].append({
                        "unit": f.get("unit"),
                        "age_hours": round(
                            (stamp - created).total_seconds() / 3600.0, 1),
                        "planned_for": f.get("planned_for", "")})
            if state == "claimed":
                lease = parse_iso(f.get("lease_until", ""))
                if lease and lease <= stamp:
                    report["overdue_claims"].append(f.get("unit"))
            if state == "done":
                status = result.get("status", "?")
                report["result_status"][status] = \
                    report["result_status"].get(status, 0) + 1
                flagged = result.get("stats_missing")
                if isinstance(flagged, list):
                    incomplete = flagged
                else:
                    stats = result.get("stats")
                    incomplete = missing_stats_keys(
                        status, stats if isinstance(stats, dict) else {})
                if incomplete:
                    report["stats_incomplete"] += 1
                    report["stats_incomplete_units"].append(
                        f.get("unit"))
                dup_stats = result.get("stats")
                if points_duplicates_achieved(
                        dup_stats if isinstance(dup_stats, dict)
                        else {}):
                    report["stats_points_dup"] += 1
                    report["stats_points_dup_units"].append(
                        f.get("unit"))
                if status in ("failed", "skipped-needs-owner"):
                    entry["failed"] += 1
                dur = result.get("duration_seconds")
                if isinstance(dur, int):
                    durations.append(dur)
                    reg_durations.setdefault(regular, []).append(dur)
                finished = parse_iso(result.get("finished_at", ""))
                if expires and finished and finished > expires:
                    report["late"].append(f.get("unit"))
                    entry["late"] += 1
    if durations:
        report["durations_seconds"] = {
            "count": len(durations),
            "avg": round(sum(durations) / len(durations), 1),
            "max": max(durations)}
    for regular, values in reg_durations.items():
        entry = report["by_regular"][regular]
        entry["duration_avg"] = round(sum(values) / len(values), 1)
        entry["duration_max"] = max(values)
    for regular, entry in report["by_regular"].items():
        est, samples = typical_minutes(root, regular)
        entry["est_typical_minutes"] = est
        entry["samples"] = samples
    if newest is not None:
        report["newest_finished_at"] = iso(newest)
        age = int((stamp - newest).total_seconds() // 60)
        report["newest_finished_age_minutes"] = age
        report["evidence_stale"] = age > EVIDENCE_STALE_MINUTES
    report["stalled_priority1"].sort(key=lambda s: -s["age_hours"])
    report["stall_expired_units"].sort(
        key=lambda s: s["expires_at"])
    return report


def cmd_stats(args):
    report = gather_stats(args.root)
    if args.format == "json":
        print(json.dumps(report, indent=2, ensure_ascii=False))
    elif args.format == "yaml":
        print("queue_stats:")
        print(f"  generated_at: {report['generated_at']}")
        print(f"  newest_finished_at: "
              f"{report['newest_finished_at'] or '-'}")
        age = report["newest_finished_age_minutes"]
        print(f"  newest_finished_age_minutes: "
              f"{age if age is not None else 'null'}")
        print(f"  evidence_stale: "
              f"{str(report['evidence_stale']).lower()}")
        print("  by_state:")
        for k, v in report["by_state"].items():
            print(f"    {k}: {v}")
        print("  result_status:")
        for k, v in report["result_status"].items():
            print(f"    {k}: {v}")
        print(f"  stats_incomplete: {report['stats_incomplete']}")
        print("  stats_incomplete_units: "
              f"[{', '.join(report['stats_incomplete_units'])}]")
        print(f"  stats_points_dup: {report['stats_points_dup']}")
        print("  stats_points_dup_units: "
              f"[{', '.join(report['stats_points_dup_units'])}]")
        d = report["durations_seconds"]
        if d:
            print(f"  durations_seconds: count {d['count']}, "
                  f"avg {d['avg']}, max {d['max']}")
        for key in ("late", "expired_waiting", "overdue_claims"):
            print(f"  {key}: [{', '.join(report[key])}]")
        if report["stalled_priority1"]:
            print("  stalled_priority1:")
            for s in report["stalled_priority1"]:
                print(f"    - {s['unit']} age_hours {s['age_hours']} "
                      f"planned_for {s['planned_for'] or '-'}")
        print(f"  stall_expired: {report['stall_expired']}")
        if report["stall_expired_units"]:
            print("  stall_expired_units:")
            for s in report["stall_expired_units"]:
                print(f"    - {s['unit']} window_start "
                      f"{s['window_start']} expires_at "
                      f"{s['expires_at']}")
        print("  by_regular:")
        for reg, counts in sorted(report["by_regular"].items()):
            print(f"    {reg}: inbox {counts['inbox']}, "
                  f"claimed {counts['claimed']}, done {counts['done']}, "
                  f"failed {counts['failed']}, late {counts['late']}, "
                  f"duration_avg {counts['duration_avg']}, "
                  f"duration_max {counts['duration_max']}, "
                  f"est_typical_minutes {counts['est_typical_minutes']}"
                  f" (n={counts['samples']})")
        if report["chains"]:
            print("  chains:")
            for chain, counts in sorted(report["chains"].items()):
                print(f"    {chain}: done {counts['done']}, "
                      f"pending {counts['pending']}")
    else:
        print(f"queue stats at {report['generated_at']}")
        print(f"  states: " + ", ".join(
            f"{k} {v}" for k, v in report["by_state"].items())
            + f", upcoming {report['upcoming']}")
        print(f"  results: " + (", ".join(
            f"{k} {v}" for k, v in report["result_status"].items())
            or "none"))
        if report["newest_finished_at"] is None:
            print("  newest executed closing: none on record")
        else:
            stale = (" (stale: over 3h without an executed closing)"
                     if report["evidence_stale"] else "")
            print(f"  newest executed closing: "
                  f"{report['newest_finished_at']} "
                  f"({report['newest_finished_age_minutes']} min ago)"
                  f"{stale}")
        if report["stats_incomplete"]:
            print(f"  stats incomplete: {report['stats_incomplete']} "
                  f"({', '.join(report['stats_incomplete_units'])})")
        if report["stats_points_dup"]:
            print(f"  stats points duplicates achieved: "
                  f"{report['stats_points_dup']} "
                  f"({', '.join(report['stats_points_dup_units'])})")
        d = report["durations_seconds"]
        if d:
            print(f"  durations: n={d['count']} avg={d['avg']}s "
                  f"max={d['max']}s")
        for key, label in (("late", "finished after expiry"),
                           ("expired_waiting", "expired in inbox"),
                           ("overdue_claims", "claims past lease")):
            if report[key]:
                print(f"  {label}: {', '.join(report[key])}")
        if report["stalled_priority1"]:
            print("  stalled priority-1: " + ", ".join(
                f"{s['unit']} ({s['age_hours']}h)"
                for s in report["stalled_priority1"]))
        if report["stall_expired_units"]:
            print("  stall-attributable expired: " + ", ".join(
                f"{s['unit']} (window {s['window_start']} to "
                f"{s['expires_at']})"
                for s in report["stall_expired_units"]))
        for reg, counts in sorted(report["by_regular"].items()):
            extra = ""
            if counts["failed"]:
                extra += f", failed {counts['failed']}"
            if counts["late"]:
                extra += f", late {counts['late']}"
            if counts["duration_avg"] is not None:
                extra += (f", dur avg {counts['duration_avg']}s"
                          f" max {counts['duration_max']}s")
            extra += (f", est ~{counts['est_typical_minutes']}m"
                      f" (n={counts['samples']})")
            print(f"  {reg}: inbox {counts['inbox']}, "
                  f"claimed {counts['claimed']}, done {counts['done']}"
                  f"{extra}")
        for chain, counts in sorted(report["chains"].items()):
            print(f"  chain {chain}: done {counts['done']}, "
                  f"pending {counts['pending']}")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "_queue_"))
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("enqueue")
    p.add_argument("--regular", required=True)
    p.add_argument("--activity", default="")
    p.add_argument("--segment", type=int, default=0)
    p.add_argument("--priority", type=int, default=3)
    p.add_argument("--expires-at", default="")
    p.add_argument("--not-before", default="")
    p.add_argument("--est-minutes", type=int, default=DEFAULT_EST_MINUTES)
    p.add_argument("--window", default="")
    p.add_argument("--chain-id", default="")
    p.add_argument("--max-attempts", type=int,
                   default=DEFAULT_MAX_ATTEMPTS)
    p.set_defaults(fn=cmd_enqueue)

    p = sub.add_parser("list")
    p.add_argument("--state", choices=STATES, default="")
    p.set_defaults(fn=cmd_list)

    p = sub.add_parser("next")
    p.add_argument("--budget-minutes", type=int, default=UNIT_CAP_MINUTES)
    p.set_defaults(fn=cmd_next)

    p = sub.add_parser("claim")
    p.add_argument("--unit", required=True)
    p.add_argument("--executor", required=True)
    p.add_argument("--lease-minutes", type=int,
                   default=DEFAULT_LEASE_MINUTES)
    p.set_defaults(fn=cmd_claim)

    p = sub.add_parser("complete")
    p.add_argument("--unit", required=True)
    p.add_argument("--status", default="done",
                   choices=["done", "partial", "failed",
                            "skipped-needs-owner"])
    p.add_argument("--summary", default="")
    p.add_argument("--claimed-items", default="")
    p.add_argument("--evidence", default="")
    p.add_argument("--follow-up", default="")
    p.add_argument("--stat", action="append", default=[])
    p.set_defaults(fn=cmd_complete)

    p = sub.add_parser("release")
    p.add_argument("--unit", required=True)
    p.set_defaults(fn=cmd_release)

    p = sub.add_parser("token-acquire")
    p.add_argument("--executor", required=True)
    p.set_defaults(fn=cmd_token_acquire)

    p = sub.add_parser("token-release")
    p.add_argument("--executor", required=True)
    p.set_defaults(fn=cmd_token_release)

    p = sub.add_parser("reap")
    p.set_defaults(fn=cmd_reap)

    p = sub.add_parser("sync")
    p.add_argument("--due-json", default="")
    p.set_defaults(fn=cmd_sync)

    p = sub.add_parser("plan")
    p.add_argument("--hours", type=int, default=12)
    p.add_argument("--regulars-json", default="")
    p.add_argument("--tracker-json", default="")
    p.set_defaults(fn=cmd_plan)

    p = sub.add_parser("stats")
    p.add_argument("--format", choices=["text", "yaml", "json"],
                   default="text")
    p.set_defaults(fn=cmd_stats)

    args = parser.parse_args(argv)
    args.root = os.path.abspath(args.root)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
