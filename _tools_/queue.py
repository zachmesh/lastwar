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
             # enqueue refuses a zero-sweep unit whose not_before /
             # expires_at do not match the reset-anchored slots of
             # the roster (issue #147): a hand-staged pair with the
             # old 17:30/18:30/19:00 wall geometry used to pre-empt
             # the sweep subcommand's correct pair - stage the pair
             # with queue.py sweep instead.
  queue.py [--root DIR] list [--state inbox|claimed|done]
  queue.py [--root DIR] validate
             # pool integrity (issue #441): exit 0 when every unit
             # file is free of conflict markers, duplicate
             # top-level frontmatter keys, a unit id that does not
             # match its file name, and a missing unit id; exit 1
             # listing each problem, for a pre-commit / pre-push
             # hook and for the sync/next guard below.
  queue.py [--root DIR] next [--budget-minutes 15]
             # next refuses (exit 1) on a corrupt pool instead of
             # handing out a unit no file on disk matches.
             # next prefers the unit that clears a recorded
             # screen-blocking overlay (issue #436) over every
             # base-screen unit, and prints nothing while the
             # clearing unit is staged but not yet actionable,
             # instead of handing out work that would block on
             # the same overlay.
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
             # a short closing that names its overlay with
             # --stat blocker_overlay=<slug> records the
             # pool-level blocker (the slug maps to its clearing
             # regular in OVERLAY_CLEARING_REGULAR); a done
             # closing by the clearing regular lifts it.
             # every closing also records a completion marker in
             # the main checkout's _queue_/completed/ (issue
             # #438), so a unit closed in a detached worktree is
             # never re-picked by the next pass: next, claim,
             # sync and plan all treat a marker like a local
             # done record, and sync reaps markers once the done
             # record lands in the local pool or after 7 days.
  queue.py [--root DIR] release --unit UNIT      # partial: back to inbox
  queue.py [--root DIR] token-acquire --executor NAME
             # a re-acquire by the same executor within 60 seconds of
             # expiry renews the lease (issue #461); any other holder
             # is refused while the lease is live.
  queue.py [--root DIR] token-release --executor NAME
             # the token lives in the main checkout's _queue_/claimed/,
             # shared by every worktree of the repo (issue #383), so a
             # pass in a fresh worktree still sees a token held by a
             # pass still running; a non-repo root keeps its own token.
  queue.py [--root DIR] reap                      # expired leases to inbox
             # reap, sync and plan warn on stdout (exit still 0)
             # when the root holds no pool state directory at
             # all, so a wrong root never reports a silent zero
             # plan and sync also warn (exit still 0, and name the
             # ids under roster_stale_regulars) when the live pool
             # holds inbox or claimed units for regulars the loaded
             # roster does not name, so a stale roster reads as
             # stale instead of as "no such regular" (issue #198)
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
             # one ticker production pass: refuse (exit 1) on a
             # corrupt pool before reaping or staging anything
             # (issue #441), then reap, expire stale units, drop
             # inbox copies already closed in done (issue #213),
             # then drop inbox copies already done on today's
             # delivered records branch (issue #446) - a unit
             # completed in a detached worktree lands its done
             # record on the branch, never in this pool, so
             # without this step the next tick hands it out
             # again; a branch that cannot be read warns and the
             # tick continues on local state only - production
             # then skips a slot already closed on the branch or
             # by a live completion marker (issue #466), so the
             # drop above cannot be undone by minting the same
             # unit id again in the same tick - then enqueue
             # one unit per regular the tracker marks due
             # (idempotent);
             # without --due-json it calls the sibling regulars.py todo
  queue.py [--root DIR] plan [--hours N]
             # stage the horizon's windows: segment anchors,
             # daily resets, Thursdays, and fixed slots (cadence
             # fixed-slots: wall slots in fixed_slots with expiry
             # clock time in expires_local, or reset-anchored slots
             # in slots_before_reset_minutes with the absolute
             # reset_utc instant as expiry, chain prefix in
             # chain_id_prefix); sync never stages fixed-slot
             # regulars, plan owns them
  queue.py [--root DIR] sweep [--regular zero-sweep]
             [--date YYYY-MM-DD] [--regulars-json FILE]
             # produce the pre-reset sweep pair for one reset day
             # from the fixed-slots regular - slots reset-anchored,
             # expiry at the reset instant itself (issue #147);
             # the planner's manual step calls this instead of
             # hand-computing wall times, so a pair staged through
             # this command can never again carry the old
             # 17:30/18:30/19:00 geometry; enqueue refuses one too
             # (see _sweep_enqueue_refusal), so the manual path
             # cannot pre-empt it any more.
             # refuses when the regular is missing or not
             # reset-anchored, so a stale tree fails loudly
             # instead of staging a wall-clock pair; refuses also
             # when the pool already holds a stale-geometry unit
             # of the day's chain (issue #410), so the stale pair
             # is withdrawn first instead of silently compounded,
             # and plan warns on the same collision through
             # _produce_for_window

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
TOKEN_RENEW_WINDOW_SECONDS = 60  # issue #461: a same-holder
# re-acquire landing this close to expiry renews the lease instead of
# reporting held - the 2026-11-08 ticker-1049 secrets unit re-acquired
# 3 seconds before expiry, was refused, and its game input then ran
# with no token held until the next acquire 6 minutes later.
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


CONFLICT_MARKERS = ("<<<<<<<", "=======", ">>>>>>>", "|||||||")


def _frontmatter_top_keys(text):
    """Top-level keys of the frontmatter block, in order.

    Only indent-0 `key:` lines count: nested keys under result /
    stats live in their own mapping and cannot shadow the unit id,
    so a repeated nested key is not a pool-integrity problem here.
    Returns (keys, frontmatter_present).
    """
    m = re.match(r"---\n(.*?)\n---\n?(.*)", text, re.S)
    if not m:
        return [], False
    keys = []
    for line in m.group(1).splitlines():
        if not line.strip() or line.startswith(" "):
            continue
        key, sep, _ = line.partition(":")
        if sep:
            keys.append(key.strip())
    return keys, True


def validate_pool(root):
    """Pool-integrity problems in the unit files, as strings.

    A bad merge resolution that lands on the records branch used to
    stay silent until next handed out a phantom unit (issue #441):
    the committed file carried two `unit:` lines and the parser kept
    the last, so list_units reported a unit no file on disk matched
    and claim always failed on it. The checks here are the ones that
    failure mode needs: conflict markers anywhere in the file,
    duplicate top-level frontmatter keys, a `unit:` id that does not
    match the file name, and a missing `unit:` key. A clean pool
    returns [].
    """
    problems = []
    for state in STATES:
        folder = state_dir(root, state)
        if not os.path.isdir(folder):
            continue
        for name in sorted(os.listdir(folder)):
            if not name.endswith(".md") or name == TOKEN_NAME:
                continue
            path = os.path.join(folder, name)
            try:
                with open(path, encoding="utf-8") as fh:
                    text = fh.read()
            except OSError as exc:
                problems.append(f"{state}/{name}: unreadable: {exc}")
                continue
            rel = f"{state}/{name}"
            for lineno, line in enumerate(text.splitlines(), 1):
                if line.startswith(CONFLICT_MARKERS):
                    problems.append(
                        f"{rel}:{lineno}: unresolved conflict marker")
            keys, has_fm = _frontmatter_top_keys(text)
            if not has_fm:
                problems.append(f"{rel}: no frontmatter block")
                continue
            seen = set()
            for key in keys:
                if key in seen:
                    problems.append(
                        f"{rel}: duplicate top-level key {key!r}")
                seen.add(key)
            fields, _ = parse_frontmatter(text)
            unit = fields.get("unit")
            if not unit:
                problems.append(f"{rel}: missing unit id")
            elif f"{unit}.md" != name:
                problems.append(
                    f"{rel}: unit id {unit!r} does not match file name")
    return problems


def cmd_validate(args):
    problems = validate_pool(args.root)
    for problem in problems:
        print(problem)
    if problems:
        print(f"pool invalid: {len(problems)} problem(s) (issue #441)")
        return 1
    print("pool valid")
    return 0


def roster_stale_regulars(root, roster_ids):
    """Regular ids of live pool units missing from the loaded roster.

    Issue #198: the planner's live-pool tree loads a stale
    regulars.json (no duel-score, no zero-sweep) while the pool
    still holds their units, so plan stages nothing for them and
    the planner's record asserts "no such regular" as a roster
    fact instead of a stale read. Only live states count - inbox
    and claimed: done is history and may legitimately hold
    retired regulars, and a unit with no regular field is
    ignored. Returns the sorted ids, empty when the roster
    covers every live unit.
    """
    roster = set(roster_ids or [])
    stale = set()
    for state in ("inbox", "claimed"):
        for fields in list_units(root, state):
            regular = fields.get("regular") or ""
            if regular and regular not in roster:
                stale.add(regular)
    return sorted(stale)


def read_roster_stale(root):
    """Stale regular ids against the roster next to this tool.

    Returns [] when the roster cannot be read, so a caller that
    does not otherwise need the roster (sync) never fails on it.
    """
    defs_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "regulars.json")
    try:
        with open(defs_path, encoding="utf-8") as fh:
            roster_ids = [r.get("id") for r in json.load(fh)["regulars"]]
    except (OSError, ValueError, KeyError, TypeError):
        return []
    return roster_stale_regulars(root, roster_ids)


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
# Screen-blocking overlay (issue #436): when a unit closes partial
# with a screen-blocking overlay as the blocker, the pool records
# the overlay and the picker prefers the unit that clears it - the
# Star Ceremony overlay (Event 40) loops on its own controls and
# holds the screen, so without this the picker keeps handing out
# base-screen units that all block identically. OVERLAY_CLEARING_REGULAR
# maps the overlay slug (stats.blocker_overlay) to the regular that
# clears it; an overlay with no row records nothing and complete
# warns, so a new overlay needs a row here, not a silent default.
# BLOCKER_STALE_HOURS bounds the pause: sync drops a blocker whose
# clearing regular has no unit in inbox or claimed for longer than
# this, so a vanished clearing unit cannot pause the pool forever.
OVERLAY_CLEARING_REGULAR = {"star-ceremony": "star-ceremony"}
BLOCKER_STALE_HOURS = 4
BLOCKER_DIRNAME = "blockers"
# Completed-unit markers (issue #438): a unit closed in a detached
# worktree leaves its done record in that worktree, so the main
# tree's inbox still holds it and the next pass re-executes it -
# the two scout units in #438, then a third donations unit. A
# closing therefore also records a small marker in the main
# checkout's _queue_/completed/ (live-only state, like the device
# token and the blockers), and next / claim / sync / plan treat a
# marker exactly like a local done record. COMPLETED_STALE_HOURS
# bounds the live directory: sync reaps a marker once the done
# record lands in the local pool (the delivery caught up) or after
# this long - the records-to-main batch merges run at least daily,
# so 7 days is several batch cycles; a marker older than that with
# no local done record means the delivery never carried the
# closing, and the suppression lapsing makes that gap visible
# instead of hiding it behind a stale file.
COMPLETED_DIRNAME = "completed"
COMPLETED_STALE_HOURS = 168


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
    # Pool integrity (issue #441): a bad merge resolution that leaves
    # conflict markers or a duplicate unit id in a committed unit
    # file used to stay silent until next handed out a phantom unit
    # claim could never find. Refuse to reap or stage anything on a
    # corrupt pool - repair the unit files and re-run.
    problems = validate_pool(args.root)
    if problems:
        for problem in problems:
            print(problem, file=sys.stderr)
        print(f"sync refused: pool invalid, {len(problems)} "
              f"problem(s) - repair the unit files and re-run "
              f"(issue #441)", file=sys.stderr)
        return 1
    # Branch reconciliation (issue #446) is fetched FIRST, before
    # expiry (issue #465): a unit whose true done record lives
    # only on the delivered records branch must not take a bogus
    # local expiry - _expire_stale drops its stale inbox copy
    # instead. A branch that cannot be read warns and the tick
    # continues on local state only.
    branch = "records/%s" % datetime.now(LOCAL_TZ).date().isoformat()
    branch_done, branch_warning = records_branch_done_units(
        args.root, branch)
    if branch_warning:
        print(f"warning: {branch_warning} (issue #446)", file=sys.stderr)
    # 1. reap expired claims, expire stale inbox units, and drop
    # inbox copies of units already closed in done (issue #213).
    # A unit completed in a detached worktree lands its done
    # record on the branch, never in this pool, so the local drop
    # below cannot see it - without the branch drop the next tick
    # hands the same unit out again.
    reaped = _reap_claimed(args.root)
    expired = _expire_stale(args.root, branch_done, branch)
    stale_done_dropped = _drop_done_duplicates(args.root)
    branch_done_dropped = drop_branch_done_duplicates(
        args.root, branch_done, branch)
    # Screen-blocking overlay (issue #436): drop blockers whose
    # clearing unit is gone, so a vanished clearing unit cannot
    # leave a stale blocker file in the live pool directory.
    blockers_reaped = reap_stale_blockers(args.root)
    # Completed-unit markers (issue #438): drop markers the local
    # pool no longer needs - the done record landed, or the marker
    # outlived the delivery lag - so the live directory stays
    # bounded; a live marker still suppresses its unit below.
    markers_reaped = reap_stale_completion_markers(args.root)
    # Roster staleness (issue #198): sync stages from the tracker,
    # which reads the roster next to this tool, so a stale tree
    # stages nothing for a regular the live pool still holds
    # units for. Warn only, never a block, matching
    # pool_root_warning.
    stale_roster = read_roster_stale(args.root)
    if stale_roster:
        print("warning: live pool holds units for regulars missing "
              f"from the loaded roster: {', '.join(stale_roster)} - "
              "the roster is stale relative to the pool (issue #198)")
    # 2. load the due list - the tracker call gets the local date
    # explicitly (issue #407) so the subprocess can never resolve
    # a different day than this pass.
    now_local = datetime.now(LOCAL_TZ)
    if args.due_json:
        with open(args.due_json, encoding="utf-8") as fh:
            due_doc = json.load(fh)
    else:
        tracker = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "regulars.py")
        out = subprocess.run(
            [sys.executable, tracker, "todo", "--json",
             "--date", now_local.date().isoformat()],
            capture_output=True, text=True, check=True)
        due_doc = json.loads(out.stdout)
    due_items = [i for i in due_doc.get("items", []) if i.get("due")]
    # 3. produce the unit for each due regular's current window -
    #    the (regular, window) invariant in _produce_for_window is
    #    what keeps sync and the planner from ever duplicating.
    #    A slot already closed on the delivered branch or by a
    #    live completion marker is not produced at all (issue
    #    #466): the branch drop above removes the stale inbox
    #    copy, but without this the same tick mints a fresh unit
    #    with the same deterministic id and re-executes the slot
    #    - ticker-1352 did exactly that to radar-2026-11-08-1003.
    #    Markers are read after the step-1 reap, so only live
    #    markers count.
    closed = {unit: "done on %s" % branch for unit in branch_done}
    for unit in completion_marker_units(args.root):
        closed.setdefault(unit, "completion marker in another "
                                "worktree")
    produced, already, skipped_closed = [], [], []
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
            duel_window_text(item["id"], planned_local),
            closed_ids=closed)
        if unit:
            produced.append(unit)
        elif _unit_id_for_window(item, planned_local) in closed:
            skipped_closed.append(
                _unit_id_for_window(item, planned_local))
        else:
            already.append(item["id"])
    # 4. window aged unscheduled priority-1 units (issue #128) -
    #    runs every tick, so the next tick after the 4 hour mark
    #    windows the unit instead of letting it age further.
    aged_p1_windowed = _window_aged_priority1(args.root)
    print(json.dumps({"reaped": reaped, "expired": expired,
                      "stale_done_dropped": stale_done_dropped,
                      "branch_done_reconciled": branch_done_dropped,
                      "branch_done_reconcile_warning": branch_warning,
                      "blockers_reaped": blockers_reaped,
                      "completion_markers_reaped": markers_reaped,
                      "due": len(due_items), "produced": produced,
                      "already_queued": already,
                      "skipped_closed": skipped_closed,
                      "roster_stale_regulars": stale_roster,
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


def _reset_anchored_offsets(item):
    """Minutes-before-reset slot offsets of a reset-anchored
    fixed-slots regular, or [] when the regular carries no
    reset_utc or no offsets - such a regular keeps the
    wall-clock fixed_slots behaviour below."""
    if _parse_hhmm(item.get("reset_utc", "")) is None:
        return []
    offsets = []
    for raw in item.get("slots_before_reset_minutes", []) or []:
        try:
            off = int(raw)
        except (TypeError, ValueError):
            continue
        if off >= 0:
            offsets.append(off)
    return sorted(set(offsets))


def _reset_instant_for_local_date(item, local_date):
    """The reset instant ending local_date, as a LOCAL_TZ datetime.

    Reset instants are absolute (issue #247): reset_utc on the
    UTC date after the local date, so 02:00 UTC is the previous
    local evening - 18:00 PST in winter, 19:00 PDT in summer.
    Computing from the UTC date, never from a wall-clock time,
    keeps the slot geometry fixed across the daylight-saving
    transition instead of drifting an hour with it."""
    hh, mm = _parse_hhmm(item.get("reset_utc", ""))
    utc_day = local_date + timedelta(days=1)
    reset_utc = datetime(utc_day.year, utc_day.month, utc_day.day,
                         hh, mm, tzinfo=timezone.utc)
    return reset_utc.astimezone(LOCAL_TZ)


def _reset_anchored_slots(item, local_date):
    """Local datetimes of the reset-anchored slots for local_date,
    earliest first."""
    offsets = _reset_anchored_offsets(item)
    if not offsets:
        return []
    reset_local = _reset_instant_for_local_date(item, local_date)
    return sorted(reset_local - timedelta(minutes=off)
                  for off in offsets)


def _next_reset_utc(after_utc, hhmm):
    """Next reset_utc instant strictly after after_utc."""
    hh, mm = hhmm
    cand = after_utc.replace(hour=hh, minute=mm, second=0,
                             microsecond=0)
    if cand <= after_utc:
        cand += timedelta(days=1)
    return cand


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
        anchored = _reset_anchored_slots(item, when_local.date())
        if anchored:
            past = [s for s in anchored if s <= when_local]
            if past:
                return past[-1]
            prev = _reset_anchored_slots(
                item, when_local.date() - timedelta(days=1))
            if prev:
                return prev[-1]
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
        if _reset_anchored_offsets(item):
            out = []
            start = cycle_start_local(item, now_local)
            day = start.date()
            while day <= horizon_end.date():
                for cand in _reset_anchored_slots(item, day):
                    if start <= cand <= horizon_end:
                        out.append(cand)
                day += timedelta(days=1)
            return out
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


def _sweep_slot_geometry(item, planned_local):
    """Expected geometry of one reset-anchored slot, or None.

    For a reset-anchored fixed-slots regular (issue #410): the
    chain sequence of the slot, the chain id of its reset day, and
    the reset instant the unit must expire at. Callers use it to
    tell a correct pair unit from a stale-geometry one sitting on
    the same slot - the (regular, planned_for) dedupe alone cannot,
    so without this check a stale first pass at 17:30 is silently
    counted as the correct final pass and the pair comes out
    half-correct, with two chain_seq 1 units and no final pass.
    """
    if item.get("cadence") != "fixed-slots" or \
            not _reset_anchored_offsets(item):
        return None
    day_slots = _reset_anchored_slots(item, planned_local.date())
    minute = planned_local.replace(second=0, microsecond=0)
    seq = None
    for idx, slot in enumerate(day_slots):
        if slot.replace(second=0, microsecond=0) == minute:
            seq = idx + 1
            break
    if seq is None:
        return None
    prefix = item.get("chain_id_prefix", "")
    chain_id = prefix + planned_local.strftime("%Y-%m-%d") \
        if prefix else ""
    planned_utc = planned_local.astimezone(timezone.utc)
    expires_dt = _next_reset_utc(
        planned_utc, _parse_hhmm(item.get("reset_utc")))
    return {"seq": seq, "chain_id": chain_id,
            "expires_at": iso(expires_dt)}


def _unit_id_for_window(item, planned_local):
    """Deterministic unit id for one (regular, window) pair.

    The id is the regular plus the window's local start - the
    same formula _produce_for_window writes into the unit file -
    so a caller can name the unit a production would mint
    without minting it (sync reports which closed slots it
    skipped, issue #466).
    """
    return "%s-%s" % (item["id"],
                      planned_local.strftime("%Y-%m-%d-%H%M"))


def _produce_for_window(root, item, planned_local, window="",
                        closed_ids=None):
    """Enqueue the unit for one (regular, window) pair, or return
    None when that pair already exists in any state - the pool's
    anti-duplication invariant, shared by sync and plan. A pair
    whose unit id is in closed_ids (unit -> where it closed) is
    also not produced: the slot already closed on the delivered
    records branch or in another worktree, and minting a fresh
    unit with the same deterministic id would re-execute it
    (issue #466). Callers that pass no closed set keep the old
    behaviour; plan passes its own set (issue #465) and sweep
    keeps the old behaviour."""
    regular = item["id"]
    planned_utc = planned_local.astimezone(timezone.utc)
    planned_iso = iso(planned_utc)
    expected = _sweep_slot_geometry(item, planned_local)
    for state in STATES:
        for f in list_units(root, state):
            if f.get("regular") == regular and \
                    f.get("planned_for") == planned_iso:
                if expected is not None:
                    # Issue #410: a stale-geometry unit on this slot
                    # (the old 17:30/18:30/19:00 pair) is not the
                    # correct pair - warn loudly instead of silently
                    # counting it as already present, so the run log
                    # names the stale pair instead of staging a
                    # half-correct chain around it. The unit itself
                    # is left alone: withdrawing it is the
                    # planner's call, and sweep refuses outright
                    # when a stale chain unit is present.
                    problems = []
                    if f.get("expires_at") != expected["expires_at"]:
                        problems.append(
                            f"expires_at {f.get('expires_at')} is not "
                            f"the reset instant {expected['expires_at']}")
                    if expected["chain_id"] and f.get("chain_id") != \
                            expected["chain_id"]:
                        problems.append(
                            f"chain_id {f.get('chain_id')!r} is not "
                            f"{expected['chain_id']!r}")
                    try:
                        seq = int(f.get("chain_seq", 0))
                    except (TypeError, ValueError):
                        seq = None
                    if seq != expected["seq"]:
                        problems.append(
                            f"chain_seq {f.get('chain_seq')!r} is not "
                            f"{expected['seq']} for this slot")
                    if problems:
                        print(f"warning: pool holds a stale-geometry "
                              f"{regular} unit {f.get('unit')} on the "
                              f"{planned_iso} slot: "
                              f"{'; '.join(problems)} - withdraw the "
                              f"stale pair and re-run plan or sweep "
                              f"(issue #410)")
                return None
    # Closed-slot guard (issue #466): the live-pool scan above
    # cannot see a closing that lives only on the delivered
    # records branch or in another worktree's marker, so a
    # caller that knows the closed set passes it in and the
    # slot is not minted again. Checked after the live scan so
    # the stale-geometry warning above still fires first.
    unit_id = _unit_id_for_window(item, planned_local)
    if closed_ids and unit_id in closed_ids:
        print(f"warning: {unit_id} already closed "
              f"({closed_ids[unit_id]}) - not producing a fresh "
              f"unit for the same slot (issue #466)",
              file=sys.stderr)
        return None
    cadence = item.get("cadence", "")
    if cadence == "fixed-slots" and _reset_anchored_offsets(item):
        # The slot's own reset instant is its expiry: a sweep
        # unit never outlives the trade day it walks (issue #147).
        expires_dt = _next_reset_utc(
            planned_utc, _parse_hhmm(item.get("reset_utc")))
    elif cadence == "fixed-slots" and item.get("expires_local"):
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
        elif cadence == "fixed-slots" and _reset_anchored_offsets(item):
            day_slots = _reset_anchored_slots(item,
                                              planned_local.date())
            minute = planned_local.replace(second=0, microsecond=0)
            for idx, slot in enumerate(day_slots):
                if slot.replace(second=0, microsecond=0) == minute:
                    chain_seq = idx + 1
                    break
    fields = {
        "unit": unit_id,
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


def _expire_stale(root, branch_done=None, branch=None):
    """Inbox units whose window has fully passed move to done with
    status expired - the next window's unit supersedes them, and the
    statistics keep the miss visible instead of losing it. The
    expiry result carries the same stats_missing flag complete
    writes (issue #130), so the retro reads the miss from the
    flag instead of recomputing it. A done
    file already carrying an execution result for the same unit is
    never overwritten: the stale inbox copy is dropped and the
    executed record kept. A records-branch snapshot can hold both
    copies at once, and expiry used to clobber the executed result
    with an expiry (queue-planning 1457 follow-up). A completion
    marker for the same unit counts as a done record here (issue
    #438): the unit closed in another worktree, so expiry must not
    overwrite that result either. A unit id in branch_done counts
    the same (issue #465): the unit closed on the delivered
    records branch, so expiry must not overwrite that result with
    a bogus miss either - the stale inbox copy is dropped
    instead. Callers that pass no branch set keep the old
    behaviour; sync and plan fetch the branch first and pass it."""
    moved = 0
    stamp = now_utc()
    for f in list_units(root, "inbox"):
        expires = parse_iso(f.get("expires_at", ""))
        if expires and expires <= stamp and f.get("unit"):
            if branch_done and f["unit"] in branch_done:
                # The unit already closed on the delivered records
                # branch (issue #465): writing an expiry here
                # would clobber that executed result with a miss,
                # the same bug class the done-exists branch guards
                # for a local record.
                print(f"warning: {f['unit']} already done on "
                      f"{branch or 'the records branch'} - dropping "
                      f"the stale inbox copy instead of "
                      f"overwriting it with an expiry",
                      file=sys.stderr)
                os.remove(unit_path(root, "inbox", f["unit"]))
                continue
            done_path = unit_path(root, "done", f["unit"])
            if os.path.exists(done_path) or has_completion_marker(
                    root, f["unit"]):
                # A completion marker means the unit already closed
                # in another worktree (issue #438): writing an
                # expiry here would clobber that executed result
                # with a miss, the same bug class the done-exists
                # branch guards for a local record.
                reason = ("already has a done record" if
                          os.path.exists(done_path) else
                          "already closed in another worktree")
                print(f"warning: {f['unit']} {reason} - dropping "
                      f"the stale inbox copy instead of "
                      f"overwriting it with an expiry",
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
                "follow_up": "none", "stats": {},
                # Same close-out flag as complete (issue #130):
                # an expired unit never executed, so all five
                # required keys are missing; the retro counts it
                # from this flag instead of recomputing.
                "stats_missing": missing_stats_keys("expired", {}),
                "stats_warnings": []}
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
    the unexpired remainder is counted here. A completion marker
    counts the same as a done record (issue #438): the unit closed
    in a detached worktree whose done file this tree never saw, so
    the inbox copy is dropped on the marker alone.
    """
    dropped = []
    for f in list_units(root, "inbox"):
        unit = f.get("unit")
        if not unit:
            continue
        if _has_done_record(root, unit):
            reason = "already has a done record"
        elif has_completion_marker(root, unit):
            reason = "already closed in another worktree"
        else:
            continue
        print(f"warning: {unit} {reason} - dropping the stale "
              f"inbox copy instead of re-executing it",
              file=sys.stderr)
        os.remove(unit_path(root, "inbox", unit))
        dropped.append(unit)
    return dropped


# ---------------------------------------------------------------------
# Records-branch reconciliation (issue #446)
# ---------------------------------------------------------------------

BRANCH_RECONCILE_REF = "refs/remotes/queue-reconcile"


def _git_remote(root):
    """First usable remote for branch reconciliation, or None.

    Prefer origin, then github (this repository's push remote),
    then any remote at all. A root with no remote cannot
    reconcile, and the caller warns instead of failing the sync.
    """
    try:
        out = subprocess.run(["git", "-C", root, "remote"],
                             capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.SubprocessError):
        return None
    if out.returncode != 0:
        return None
    remotes = [line.strip() for line in out.stdout.splitlines()
               if line.strip()]
    for preferred in ("origin", "github"):
        if preferred in remotes:
            return preferred
    return remotes[0] if remotes else None


def records_branch_done_units(root, branch):
    """Unit ids already closed on the delivered records branch.

    Fetches branch into a private remote-tracking ref (never a
    checked-out branch, never the working tree) and lists its
    _queue_/done/ unit ids. Returns (done_ids, warning): warning
    is None on success, else a short reason the branch could not
    be read - no remote, fetch failed, branch not yet pushed
    today - so the caller warns and the tick continues on local
    state only. A reconcile that cannot read the branch never
    blocks the tick. The tree is listed whole and filtered in
    Python: a git pathspec would be read relative to the caller's
    working directory, and this tool's root is the _queue_
    subdir, not the repo top, so `_queue_/done/` as a pathspec
    would silently match nothing - and ls-tree names are
    cwd-relative too, so the listing needs --full-name for the
    repo-root-relative filter below to hold.
    """
    remote = _git_remote(root)
    if remote is None:
        return set(), "no git remote, branch reconcile skipped"
    ref = "%s/%s" % (BRANCH_RECONCILE_REF, branch.replace("/", "-"))
    # The leading + force-updates the private ref: the records
    # branch is rebased by the integration runs, so its tip moves
    # non-linearly and a plain fetch would reject the update as a
    # non-fast-forward on the second sync of the day.
    try:
        fetch = subprocess.run(
            ["git", "-C", root, "fetch", "--depth", "1", remote,
             "+%s:%s" % (branch, ref)],
            capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        return set(), ("fetch of %s failed, branch reconcile "
                       "skipped" % branch)
    if fetch.returncode != 0:
        detail = [line for line in (fetch.stderr or "").splitlines()
                  if line.strip()]
        reason = ""
        for line in detail:
            if "fatal" in line or "error" in line:
                reason = line.strip()
                break
        if not reason and detail:
            # git's first stderr line is the "From <url>" header,
            # not the error - take the last line instead.
            reason = detail[-1].strip()
        if not reason:
            reason = "fetch failed"
        return set(), ("fetch of %s failed (%s), branch reconcile "
                       "skipped" % (branch, reason[:120]))
    try:
        listing = subprocess.run(
            ["git", "-C", root, "ls-tree", "-r", "--full-name",
             "--name-only", ref],
            capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return set(), ("ls-tree of %s failed, branch reconcile "
                       "skipped" % branch)
    if listing.returncode != 0:
        return set(), ("ls-tree of %s failed, branch reconcile "
                       "skipped" % branch)
    done = set()
    for line in listing.stdout.splitlines():
        name = line.strip()
        if not name.startswith("_queue_/done/"):
            continue
        if not name.endswith(".md"):
            continue
        unit = os.path.basename(name)[:-len(".md")]
        if unit:
            done.add(unit)
    return done, None


def drop_branch_done_duplicates(root, done_ids, branch):
    """Drop inbox copies already closed on the records branch.

    Mirrors _drop_done_duplicates (issue #213) with the
    delivered branch as the authority instead of the local done
    directory: a unit completed in a detached worktree lands its
    done record on the records branch, and until something
    reconciles the branch back into this pool the inbox copy is
    handed out again (issue #446: ticker-0534 re-ran three units
    already done on records/2026-11-08). Dropping is
    result-preserving by construction: the done record lives on
    the branch and is never touched, only the stale inbox file is
    removed, with a stderr warning naming the unit. Runs in sync
    after the local drop, so a unit closed both locally and on
    the branch is counted once, under the local drop.
    """
    dropped = []
    for unit in sorted(done_ids):
        if not unit:
            continue
        if not os.path.exists(unit_path(root, "inbox", unit)):
            continue
        print(f"warning: {unit} already done on {branch} - dropping "
              f"the stale inbox copy instead of re-executing it",
              file=sys.stderr)
        os.remove(unit_path(root, "inbox", unit))
        dropped.append(unit)
    return dropped


def cmd_plan(args):
    warning = pool_root_warning(args.root)
    if warning:
        print(warning)
    # Branch reconciliation (issues #446, #465): fetch today's
    # delivered records branch first, so expiry drops (never
    # expires) inbox copies already closed on the branch and
    # staging below skips their slots. A branch that cannot be
    # read warns and the run continues on local state only.
    branch = "records/%s" % datetime.now(LOCAL_TZ).date().isoformat()
    branch_done, branch_warning = records_branch_done_units(
        args.root, branch)
    if branch_warning:
        print(f"warning: {branch_warning} (issue #446)",
              file=sys.stderr)
    reaped = _reap_claimed(args.root)
    expired = _expire_stale(args.root, branch_done, branch)
    stale_done_dropped = _drop_done_duplicates(args.root)
    branch_done_dropped = drop_branch_done_duplicates(
        args.root, branch_done, branch)
    defs_path = args.regulars_json or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "regulars.json")
    with open(defs_path, encoding="utf-8") as fh:
        regs = json.load(fh)["regulars"]
    # Roster staleness (issue #198): the live pool may hold units
    # for regulars this roster does not name - a stale tree stages
    # nothing for them while the ticker's live pool keeps their
    # units. Warn only, never a block, matching pool_root_warning.
    stale_roster = roster_stale_regulars(
        args.root, [r.get("id") for r in regs])
    if stale_roster:
        print("warning: live pool holds units for regulars missing "
              f"from the loaded roster: {', '.join(stale_roster)} - "
              "the roster is stale relative to the pool (issue #198)")
    # Tracker truth for the current window - a regular the tracker
    # already counts as done for this window gets no phantom unit;
    # future windows are always staged.
    # The tracker call gets the local date explicitly (issue #407)
    # so the subprocess can never resolve a different day than
    # this pass.
    now_local = datetime.now(LOCAL_TZ)
    if args.tracker_json:
        with open(args.tracker_json, encoding="utf-8") as fh:
            tracker_doc = json.load(fh)
    else:
        tracker = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "regulars.py")
        out = subprocess.run(
            [sys.executable, tracker, "list", "--json",
             "--date", now_local.date().isoformat()],
            capture_output=True, text=True, check=True)
        tracker_doc = json.loads(out.stdout)
    due_now = {i["id"]: bool(i.get("due"))
               for i in tracker_doc.get("items", [])}
    horizon_end = now_local + timedelta(hours=args.hours)
    # Closed slots (issue #465): a slot already closed on the
    # delivered branch or by a live completion marker is not
    # staged at all - the tracker has no per-slot done state for
    # fixed-slots regulars, so without this the planner re-stages
    # a slot another worktree already executed, exactly what the
    # 1340 run did to training/donations/arms-race-2026-11-08-1003.
    # Markers are read after the step-1 reap, so only live
    # markers count.
    closed = {unit: "done on %s" % branch for unit in branch_done}
    for unit in completion_marker_units(args.root):
        closed.setdefault(unit, "completion marker in another "
                                "worktree")
    planned, present, skipped_done, skipped_closed = [], 0, 0, []
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
                args.root, item, w, duel_window_text(item["id"], w),
                closed_ids=closed)
            if unit:
                planned.append(unit)
            elif _unit_id_for_window(item, w) in closed:
                skipped_closed.append(_unit_id_for_window(item, w))
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
                      "branch_done_reconciled": branch_done_dropped,
                      "branch_done_reconcile_warning": branch_warning,
                      "planned": planned,
                      "already_present": present,
                      "skipped_done_current": skipped_done,
                      "skipped_closed": skipped_closed,
                      "roster_stale_regulars": stale_roster,
                      "aged_p1_windowed": aged_p1_windowed},
                     ensure_ascii=False))
    return 0


def cmd_sweep(args):
    """Produce the pre-reset sweep pair for one reset day.

    The planner's manual sweep-production step used to hand-compute
    the pair (17:30/18:30 local, expiring 19:00 local) and copy the
    previous day's task text, so the reset-anchored geometry PR #267
    put in the regular never reached the pair - and the Nov 4 pair
    expired unexecuted half an hour after the true 18:00 PST reset
    (issue #147, fourth failure running). This command reads the
    geometry from the roster instead: the reset-anchored slots of
    the fixed-slots regular, expiring at the reset instant itself,
    produced through _produce_for_window so the (regular,
    planned_for) anti-duplication invariant holds against plan.

    It refuses - exit 1, no unit staged - when the regular is
    missing from the roster or carries no reset anchoring, so a
    stale tree fails loudly instead of staging a wall-clock pair
    with the old 19:00 expiry, and when the reset instant for the
    date is already past, so a late call cannot stage dead units.
    It also refuses when the pool already holds a stale-geometry
    unit of the day's chain (issue #410): the (regular,
    planned_for) dedupe would otherwise count the stale first
    pass at 17:30 as the correct final pass and stage a second
    chain_seq 1 at 16:30, leaving a corrupted chain with no final
    pass and a post-reset 18:30 unit. A correct pair already in
    the pool passes, so an idempotent re-run still succeeds.
    """
    warning = pool_root_warning(args.root)
    if warning:
        print(warning)
    defs_path = args.regulars_json or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "regulars.json")
    try:
        with open(defs_path, encoding="utf-8") as fh:
            regs = json.load(fh)["regulars"]
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"refused: cannot read roster {defs_path}: {exc}")
        return 1
    item = next((r for r in regs if r.get("id") == args.regular), None)
    if item is None:
        print(f"refused: regular {args.regular!r} not in roster "
              f"{defs_path} - sync the tree to main before producing "
              f"the sweep pair")
        return 1
    if item.get("cadence") != "fixed-slots" or \
            not _reset_anchored_offsets(item):
        print(f"refused: regular {args.regular!r} carries no "
              f"reset-anchored slots (reset_utc + "
              f"slots_before_reset_minutes) - a wall-clock pair "
              f"would repeat the issue #147 defect")
        return 1
    if args.date:
        try:
            year, month, day = (int(x) for x in args.date.split("-"))
            local_date = datetime(year, month, day).date()
        except ValueError:
            print(f"refused: --date {args.date!r} is not YYYY-MM-DD")
            return 1
    else:
        local_date = datetime.now(LOCAL_TZ).date()
    reset_local = _reset_instant_for_local_date(item, local_date)
    if reset_local <= datetime.now(LOCAL_TZ):
        print(f"refused: reset instant "
              f"{iso(reset_local.astimezone(timezone.utc))} for "
              f"{local_date.isoformat()} is already past - pass "
              f"--date for the next reset day")
        return 1
    slots = _reset_anchored_slots(item, local_date)
    # Issue #410: refuse when the pool already holds a stale-geometry
    # unit of this reset day's chain - the old 17:30/18:30/19:00 pair
    # a stale tree staged. The (regular, planned_for) dedupe below
    # would otherwise count the stale first pass at 17:30 as the
    # correct final pass and stage a second chain_seq 1 at 16:30,
    # leaving a corrupted chain with no final pass and a post-reset
    # 18:30 unit. A correct pair already in the pool passes this
    # check, so an idempotent re-run still exits 0.
    reset_iso = iso(reset_local.astimezone(timezone.utc))
    slot_iso = {iso(s.astimezone(timezone.utc)): idx + 1
                for idx, s in enumerate(slots)}
    chain_id = item.get("chain_id_prefix", "") + \
        local_date.isoformat() if item.get("chain_id_prefix") else ""
    stale = []
    for state in STATES:
        for f in list_units(args.root, state):
            if f.get("regular") != args.regular:
                continue
            planned = parse_iso(f.get("planned_for", ""))
            on_chain = bool(chain_id) and \
                f.get("chain_id") == chain_id
            on_slot = planned is not None and \
                iso(planned) in slot_iso
            if not on_chain and not on_slot:
                continue
            problems = []
            if planned is None:
                problems.append("unparseable planned_for "
                                f"{f.get('planned_for')!r}")
            elif iso(planned) not in slot_iso:
                problems.append(
                    f"planned_for {f.get('planned_for')} is not a "
                    f"reset-anchored slot for {local_date.isoformat()}")
            if f.get("expires_at") != reset_iso:
                problems.append(
                    f"expires_at {f.get('expires_at')} is not the "
                    f"reset instant {reset_iso}")
            if on_chain:
                try:
                    seq = int(f.get("chain_seq", 0))
                except (TypeError, ValueError):
                    seq = None
                want = slot_iso.get(iso(planned)) \
                    if planned is not None else None
                if want is not None and seq != want:
                    problems.append(
                        f"chain_seq {f.get('chain_seq')!r} is not "
                        f"{want} for its slot")
            if problems:
                stale.append((f.get("unit"), "; ".join(problems)))
    if stale:
        print(f"refused: pool holds stale-geometry {args.regular} "
              f"units for {local_date.isoformat()}: " +
              "; ".join(f"{u} ({p})" for u, p in stale) +
              " - withdraw the stale pair and re-run sweep "
              "(issue #410)")
        return 1
    produced, already = [], 0
    for idx, slot in enumerate(slots):
        if len(slots) == 2:
            label = "first pass" if idx == 0 else "final pass"
        else:
            label = f"pass {idx + 1}"
        unit = _produce_for_window(
            args.root, item, slot, f"pre-reset zero sweep, {label}")
        if unit:
            produced.append(unit)
        else:
            already += 1
    print(json.dumps({
        "regular": args.regular, "date": local_date.isoformat(),
        "reset_at": iso(reset_local.astimezone(timezone.utc)),
        "produced": produced, "already_present": already},
        ensure_ascii=False))
    return 0


def _sweep_enqueue_refusal(args):
    """Refusal message when a hand-enqueued zero-sweep unit does not
    match the reset-anchored geometry, or None when it may proceed.

    The sweep pair is produced by plan/sweep from the roster (design
    section 12); the manual enqueue path predates that interface and
    kept staging the pair on the old wall-clock geometry (17:30/18:30
    local, expiring 19:00 local) from stale trees, which pre-empted
    the subcommand's correct pair through the inbox (issue #147,
    sixth failure running on 2026-11-06). A hand-enqueued zero-sweep
    unit must therefore carry the roster's reset-anchored geometry:
    expires_at at the reset instant ending its local date, not_before
    at one of that day's reset-anchored slots, and - when a chain id
    is given - the chain for that local date. Anything else is
    refused loudly, naming the expected geometry and the sweep
    command that stages it, so a stale tree fails instead of
    staging a dead pair. Other regulars are unaffected.
    """
    if args.regular != "zero-sweep":
        return None
    defs_path = args.regulars_json or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "regulars.json")
    try:
        with open(defs_path, encoding="utf-8") as fh:
            regs = json.load(fh)["regulars"]
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return (f"refused: cannot read roster {defs_path}: {exc} - "
                f"sync the tree to main before hand-enqueueing the "
                f"sweep pair")
    item = next((r for r in regs if r.get("id") == "zero-sweep"), None)
    if item is None:
        return ("refused: regular 'zero-sweep' not in roster "
                f"{defs_path} - sync the tree to main before "
                f"hand-enqueueing the sweep pair")
    if not _reset_anchored_offsets(item):
        return ("refused: regular 'zero-sweep' carries no "
                "reset-anchored slots (reset_utc + "
                "slots_before_reset_minutes) - a wall-clock pair "
                "would repeat the issue #147 defect; stage the pair "
                "with queue.py sweep from a current tree")
    expires = parse_iso(args.expires_at)
    not_before = parse_iso(args.not_before)
    if expires is None or not_before is None:
        return ("refused: a zero-sweep unit needs not_before at a "
                "reset-anchored slot and expires_at at the reset "
                "instant - stage the pair with queue.py sweep "
                "--date YYYY-MM-DD instead")
    local_date = expires.astimezone(LOCAL_TZ).date()
    reset_local = _reset_instant_for_local_date(item, local_date)
    if expires != reset_local.astimezone(timezone.utc):
        return (f"refused: zero-sweep expires_at "
                f"{iso(expires)} is not the reset instant "
                f"{iso(reset_local.astimezone(timezone.utc))} ending "
                f"{local_date.isoformat()} - stage the pair with "
                f"queue.py sweep --date {local_date.isoformat()} "
                f"instead")
    slots = _reset_anchored_slots(item, local_date)
    if not_before not in [s.astimezone(timezone.utc) for s in slots]:
        want = ", ".join(iso(s.astimezone(timezone.utc))
                         for s in slots)
        return (f"refused: zero-sweep not_before "
                f"{iso(not_before)} is not a reset-anchored slot "
                f"for {local_date.isoformat()} (want one of {want}) "
                f"- stage the pair with queue.py sweep --date "
                f"{local_date.isoformat()} instead")
    prefix = item.get("chain_id_prefix", "")
    if args.chain_id and prefix and \
            args.chain_id != prefix + local_date.isoformat():
        return (f"refused: zero-sweep chain {args.chain_id} does not "
                f"match the reset day {local_date.isoformat()} "
                f"(want {prefix}{local_date.isoformat()}) - stage "
                f"the pair with queue.py sweep --date "
                f"{local_date.isoformat()} instead")
    return None


def cmd_enqueue(args):
    if args.est_minutes > UNIT_CAP_MINUTES:
        print(f"refused: est_minutes {args.est_minutes} exceeds the "
              f"{UNIT_CAP_MINUTES} minute unit cap - split the task")
        return 1
    refusal = _sweep_enqueue_refusal(args)
    if refusal is not None:
        print(refusal)
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


def _est_minutes(fields):
    try:
        return int(fields.get("est_minutes", DEFAULT_EST_MINUTES))
    except (TypeError, ValueError):
        return DEFAULT_EST_MINUTES


def cmd_next(args):
    # Pool integrity (issue #441): refuse to hand out a unit from a
    # corrupt pool - a phantom id claim can never find - instead of
    # printing it and letting the pass stall at claim time. Sync
    # runs the same check first in the normal ticker flow; this
    # covers a direct next call on a pool sync never saw.
    problems = validate_pool(args.root)
    if problems:
        for problem in problems:
            print(problem, file=sys.stderr)
        print(f"next refused: pool invalid, {len(problems)} "
              f"problem(s) - repair the unit files and re-run "
              f"(issue #441)", file=sys.stderr)
        return 1
    stamp = now_utc()
    candidates = sorted(
        (f for f in list_units(args.root, "inbox")
         if _actionable(f, stamp)
         and not _has_done_record(args.root, f.get("unit"))
         and not has_completion_marker(args.root, f.get("unit"))),
        key=lambda f: pick_key(f, stamp))
    # Screen-blocking overlay (issue #436): a recorded overlay
    # prefers the unit that clears it over every base-screen unit,
    # and pauses base-screen production while the clearing unit is
    # staged but not yet actionable - the next pass re-picks then.
    # Newest blocker first: the most recently recorded overlay is
    # the one on top of the screen.
    for blocker in read_blockers(args.root):
        clearing = [f for f in list_units(args.root, "inbox")
                    if f.get("regular") ==
                    blocker["clearing_regular"]
                    and not _has_done_record(args.root,
                                             f.get("unit"))
                    and not has_completion_marker(
                        args.root, f.get("unit"))]
        if not clearing:
            # No unit can clear this overlay: nothing to wait for,
            # so this blocker does not steer the pick; a unit that
            # blocks on the overlay again re-records it.
            continue
        fit = [f for f in sorted(
            (f for f in clearing if _actionable(f, stamp)),
            key=lambda f: pick_key(f, stamp))
            if _est_minutes(f) <= args.budget_minutes]
        if fit:
            print(fit[0].get("unit", ""))
            return 0
        # A clearing unit is staged but cannot run yet (not_before
        # in the future, or over this pass's remaining budget):
        # hand out nothing rather than a base-screen unit that
        # would block identically on the same overlay.
        print("")
        return 0
    for f in candidates:
        if _est_minutes(f) <= args.budget_minutes:
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
    if has_completion_marker(args.root, args.unit):
        print(f"cannot claim {args.unit}: already closed in "
              f"another worktree - the inbox copy is stale, run "
              f"sync to drop it instead of re-executing it")
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


def points_duplicates_achieved(stats, regular=None):
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

    Radar is exempt (issue #296): a radar unit's achieved is a
    claim count, and its radar-screen points rise exactly one
    per claim, so points equal to achieved is the mechanism,
    not a copy - radar-2026-11-04-0203 read 194 to 205 for 11
    claims, radar-2026-11-04-1003 read 206 to 219 for 13
    claims, and radar-2026-11-02-0203 read 101 to 103 for 2
    claims, each with a before/after read in its execution
    record. The exemption covers only this equality
    heuristic; score-total regulars (arms-race,
    star-ceremony) stay flagged, and a radar unit's points
    still count under its own regular in the retro.
    """
    if not isinstance(stats, dict):
        return False
    if regular == "radar":
        return False
    points = _stat_number(stats.get("points"))
    achieved = _stat_number(stats.get("achieved"))
    return (points is not None and achieved is not None
            and points != 0 and points == achieved)


def points_without_achieved(stats):
    """True when stats.points is a nonzero gain with no achieved (issue #300).

    points is score gained in this unit, not a running total
    read (task-unit-queue-design.md per-unit measurement table:
    points is "score gained, for scoring types"). A closing
    that writes a screen total into points and no achieved key
    at all therefore carries a wrong-semantics value the
    equality detector cannot see - with no achieved there is
    nothing to compare. The known cases are the three legacy
    radar closings that wrote the radar-screen total into
    points (2924/2948/2989, 2026-10-28/29) and one arms-race
    closing (37500, 2026-10-29-0603), all with no achieved
    key; the retro summed them as points gained. Presence is
    by key, not by number: a closing whose achieved is a
    descriptive string still carries its achieved read and is
    not flagged (daily-missions 2026-10-31-1900, achieved
    all-claimable-claimed, points 40 - the 110-to-150 activity
    gain in its summary). Zero points is not flagged: a unit
    that gained nothing is not a total copy, mirroring the
    zero rule in points_duplicates_achieved. This is a
    warning, never a block.
    """
    if not isinstance(stats, dict):
        return False
    points = _stat_number(stats.get("points"))
    return (points is not None and points != 0
            and "achieved" not in stats)


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
    points_dup = points_duplicates_achieved(stats, fields.get("regular"))
    points_noach = points_without_achieved(stats)
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
        "stats_warnings": ((["points duplicates achieved"]
                            if points_dup else [])
                           + (["points without achieved"]
                              if points_noach else [])),
    }
    # Screen-blocking overlay (issue #436): a short closing that
    # names its overlay records the pool-level blocker, so the
    # picker prefers the clearing unit next; a done closing by
    # the clearing regular lifts the blocker it clears. A short
    # closing by the clearing regular that names the same overlay
    # refreshes the blocker - the overlay is still open.
    blocker_note = ""
    overlay = stats.get("blocker_overlay")
    if isinstance(overlay, str) and overlay.strip():
        overlay = _blocker_slug(overlay)
        if args.status in SHORT_CLOSING_STATUSES:
            clearing = record_blocker(args.root, overlay,
                                      args.unit)
            if clearing:
                blocker_note = (f"blocker recorded: overlay "
                                f"{overlay} - next picks prefer "
                                f"{clearing} units until one "
                                f"closes done")
            else:
                blocker_note = (f"warning: {args.unit} names "
                                f"unknown overlay {overlay} - no "
                                f"clearing regular mapped, no "
                                f"blocker recorded")
    if args.status == "done":
        for blocker in read_blockers(args.root):
            if blocker["clearing_regular"] == fields.get("regular"):
                if clear_blocker(args.root, blocker["overlay"]):
                    blocker_note = (f"blocker cleared: overlay "
                                    f"{blocker['overlay']} cleared "
                                    f"by {args.unit}")
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
    if points_noach:
        print(f"warning: {args.unit} closes with stats.points "
              f"and no stats.achieved - points is score gained "
              f"in this unit, not a running total read; a screen "
              f"total belongs in achieved only")
    if blocker_note:
        print(blocker_note)
    # Completed-unit marker (issue #438): the done record above
    # lives in this worktree only, so record the closing in the
    # shared main-checkout pool too - otherwise the main tree's
    # inbox still holds the unit and the next pass re-executes
    # it. Best effort: a marker that cannot be written never fails
    # the closing itself, it only warns.
    if record_completion(args.root, args.unit, args.status,
                         fields.get("claimed_by", "")):
        print(f"completion recorded: {args.unit} closed "
              f"{args.status} - shared marker suppresses re-picks")
    else:
        print(f"warning: {args.unit} completion marker not "
              f"recorded - the next pass may re-pick this unit",
              file=sys.stderr)
    return 0


def _dead_letter(root, path, fields, body):
    """Attempts-exhausted closing, stamped with the same
    stats_missing flag complete writes (issue #130)."""
    # A dead letter is a closing too (issue #438): record the
    # marker so no worktree re-picks the exhausted unit. The
    # executor and unit are read before the claim fields are
    # cleared below.
    executor = fields.get("claimed_by", "")
    unit = fields.get("unit", "")
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
        # Same close-out flag as complete (issue #130): a dead
        # letter never produced stats, so all five required keys
        # plus blocker_category (failed status) are missing.
        "stats_missing": missing_stats_keys("failed", {}),
        "stats_warnings": [],
    }
    for key in ("claimed_by", "claimed_at", "lease_until"):
        fields[key] = ""
    os.makedirs(state_dir(root, "done"), exist_ok=True)
    target = unit_path(root, "done", fields.get("unit", ""))
    write_unit(path, fields, body)
    os.rename(path, target)
    record_completion(root, unit, "failed", executor)


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


def _shared_token_home(root):
    """Main-checkout _queue_ dir for a root that may be a worktree.

    Each ticker pass runs in its own fresh detached worktree, so a token
    file under the pass's own _queue_/claimed/ is invisible to the next
    pass and the section-6 overlap guard fails (issue #383). The token
    therefore lives in the main checkout's _queue_/claimed/, which every
    worktree of the repo shares: ask git for the common git dir of the
    root - for a linked worktree that is <main>/.git, whose parent is the
    main checkout; for the main checkout itself it is <root>/.git. When
    git is unavailable or the root is not a worktree (tests, scratch
    dirs), return None and the caller falls back to the root itself.
    """
    try:
        out = subprocess.run(
            ["git", "-C", root, "rev-parse", "--git-common-dir"],
            capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.SubprocessError):
        return None
    if out.returncode != 0:
        return None
    common = out.stdout.strip()
    if not common:
        return None
    if not os.path.isabs(common):
        common = os.path.normpath(os.path.join(root, common))
    if os.path.basename(os.path.normpath(common)) != ".git":
        return None
    main_queue = os.path.join(
        os.path.dirname(os.path.normpath(common)), "_queue_")
    if os.path.isdir(main_queue):
        return main_queue
    return None


def token_path(root):
    shared = _shared_token_home(root)
    home = shared if shared is not None else root
    return os.path.join(state_dir(home, "claimed"), TOKEN_NAME)


# ---------------------------------------------------------------------
# Screen-blocking overlay blockers (issue #436)
# ---------------------------------------------------------------------

def blocker_home(root):
    """Shared pool home for blocker files, like the device token.

    Blockers are live pool state, not records: they must be visible
    to the next pass, so they live in the main checkout's _queue_
    (issue #383) exactly like the token, never in a pass worktree's
    own _queue_, and _queue_/.gitignore excludes the directory so
    they are never committed.
    """
    shared = _shared_token_home(root)
    return shared if shared is not None else root


def blocker_path(root, overlay):
    return os.path.join(blocker_home(root), BLOCKER_DIRNAME,
                        overlay + ".md")


def _blocker_slug(text):
    return re.sub(r"[^a-z0-9_-]+", "-", (text or "").strip().lower()
                  ).strip("-")


def read_blockers(root):
    """Active overlay blockers, newest recorded first.

    Each file is the small frontmatter the completion path wrote; a
    file that does not parse or names no clearing regular is
    skipped, so a half-written record can never pause the pool.
    The most recently recorded overlay is the one on top of the
    screen, so newest-first is also the clearing order.
    """
    home = blocker_home(root)
    folder = os.path.join(home, BLOCKER_DIRNAME)
    out = []
    if not os.path.isdir(folder):
        return out
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".md"):
            continue
        fields, _ = read_unit(os.path.join(folder, name))
        overlay = fields.get("overlay", "")
        clearing = fields.get("clearing_regular", "")
        if not overlay or not clearing:
            continue
        recorded = parse_iso(fields.get("recorded_at", ""))
        out.append({"overlay": overlay,
                    "clearing_regular": clearing,
                    "recorded_at": recorded,
                    "recorded_by": fields.get("recorded_by", ""),
                    "path": os.path.join(folder, name)})
    out.sort(key=lambda b: b["recorded_at"] or datetime.min.replace(
        tzinfo=timezone.utc), reverse=True)
    return out


def record_blocker(root, overlay, recorded_by):
    """Record (or refresh) the pool-level blocker for an overlay.

    Returns the clearing regular, or "" when the overlay has no
    row in OVERLAY_CLEARING_REGULAR (the caller warns; a blocker
    with no known clearing unit cannot be acted on).
    """
    clearing = OVERLAY_CLEARING_REGULAR.get(overlay, "")
    if not clearing:
        return ""
    home = blocker_home(root)
    folder = os.path.join(home, BLOCKER_DIRNAME)
    os.makedirs(folder, exist_ok=True)
    lines = ["---",
             f"overlay: {overlay}",
             f"clearing_regular: {clearing}",
             f"recorded_at: {iso(now_utc())}",
             f"recorded_by: {recorded_by or ''}",
             "---", ""]
    with open(os.path.join(folder, overlay + ".md"),
              "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    return clearing


def clear_blocker(root, overlay):
    """Remove the blocker for an overlay. True when one existed."""
    path = blocker_path(root, overlay)
    if os.path.exists(path):
        os.remove(path)
        return True
    return False


def reap_stale_blockers(root):
    """Drop blockers whose clearing unit is gone (sync hygiene).

    A blocker is stale when its clearing regular has no unit in
    inbox or claimed and it was recorded over BLOCKER_STALE_HOURS
    ago; the picker already ignores a blocker with no clearing
    unit, so reaping changes no pick - it only keeps the live
    directory from holding a blocker no pass can ever clear.
    Returns the list of overlay slugs dropped.
    """
    stamp = now_utc()
    live = set()
    for state in ("inbox", "claimed"):
        for f in list_units(root, state):
            if f.get("regular"):
                live.add(f["regular"])
    dropped = []
    for blocker in read_blockers(root):
        recorded = blocker["recorded_at"]
        if blocker["clearing_regular"] in live:
            continue
        if recorded is not None and \
                (stamp - recorded).total_seconds() <= \
                BLOCKER_STALE_HOURS * 3600:
            continue
        if clear_blocker(root, blocker["overlay"]):
            dropped.append(blocker["overlay"])
    return dropped


# ---------------------------------------------------------------------
# Completed-unit markers (issue #438)
# ---------------------------------------------------------------------

def completion_home(root):
    """Shared pool home for completion markers, like the token.

    Markers are live pool state, not records: they must be visible
    to the next pass, so they live in the main checkout's _queue_
    (issue #383) exactly like the token and the blockers, never in
    a pass worktree's own _queue_, and _queue_/.gitignore excludes
    the directory so they are never committed.
    """
    shared = _shared_token_home(root)
    return shared if shared is not None else root


def completion_marker_path(root, unit):
    return os.path.join(completion_home(root), COMPLETED_DIRNAME,
                        unit + ".md")


def has_completion_marker(root, unit):
    """True when the shared pool holds a completion marker for unit.

    A marker is a small frontmatter file the completion path wrote
    in another worktree; it suppresses the inbox copy exactly like
    a local done record. A file that does not parse, names a
    different unit, or carries no closing status suppresses
    nothing, so a half-written record can never hide fresh work.
    """
    if not unit:
        return False
    path = completion_marker_path(root, unit)
    if not os.path.exists(path):
        return False
    try:
        fields, _ = read_unit(path)
    except (OSError, ValueError, UnicodeDecodeError):
        return False
    return (fields.get("unit") == unit
            and bool(fields.get("status")))


def completion_marker_units(root):
    """Unit ids holding a live, valid completion marker.

    Mirrors has_completion_marker's validity rule (the marker
    names its own unit and carries a closing status); a file
    that does not parse, names a different unit, or carries no
    status suppresses nothing. Used by sync production (issue
    #466): a unit closed in another worktree whose done record
    has not landed anywhere this tree can see must still block
    a fresh unit for its slot.
    """
    home = completion_home(root)
    folder = os.path.join(home, COMPLETED_DIRNAME)
    if not os.path.isdir(folder):
        return set()
    units = set()
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".md"):
            continue
        unit = name[:-len(".md")]
        if not unit:
            continue
        try:
            fields, _ = read_unit(os.path.join(folder, name))
        except (OSError, ValueError, UnicodeDecodeError):
            continue
        if fields.get("unit") == unit and bool(fields.get("status")):
            units.add(unit)
    return units


def record_completion(root, unit, status, executor):
    """Record the closing of unit in the shared pool. Best effort.

    Returns True when the marker was written, False when the shared
    home cannot be written (a non-repo scratch root, a read-only
    checkout): the caller warns but never fails the closing itself
    over a marker. The marker is deliberately small - unit, status,
    finished_at, executor - because the full result lives in the
    done record; the marker only has to answer "did this unit
    already close somewhere".
    """
    if not unit or not status:
        return False
    try:
        home = completion_home(root)
        folder = os.path.join(home, COMPLETED_DIRNAME)
        os.makedirs(folder, exist_ok=True)
        lines = ["---",
                 f"unit: {unit}",
                 f"status: {status}",
                 f"finished_at: {iso(now_utc())}",
                 f"executor: {executor or ''}",
                 "---", ""]
        with open(os.path.join(folder, unit + ".md"),
                  "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))
    except OSError:
        return False
    return True


def clear_completion_marker(root, unit):
    """Remove the marker for unit. True when one existed."""
    path = completion_marker_path(root, unit)
    if os.path.exists(path):
        os.remove(path)
        return True
    return False


def reap_stale_completion_markers(root):
    """Drop markers the local pool no longer needs (sync hygiene).

    A marker is stale when the unit's done record has landed in
    this pool - the delivery caught up, so the local record now
    suppresses the inbox copy on its own - or when the marker is
    older than COMPLETED_STALE_HOURS: the delivery never carried
    the closing, and the suppression lapsing makes that gap
    visible instead of hiding it behind a stale file. A file that
    does not parse to a unit and status suppresses nothing, so it
    is dropped too. Returns the list of unit ids dropped.
    """
    home = completion_home(root)
    folder = os.path.join(home, COMPLETED_DIRNAME)
    if not os.path.isdir(folder):
        return []
    stamp = now_utc()
    dropped = []
    for name in sorted(os.listdir(folder)):
        if not name.endswith(".md"):
            continue
        unit = name[:-len(".md")]
        path = os.path.join(folder, name)
        try:
            fields, _ = read_unit(path)
        except (OSError, ValueError, UnicodeDecodeError):
            fields = {}
        finished = parse_iso(fields.get("finished_at", ""))
        valid = (fields.get("unit") == unit
                 and bool(fields.get("status")))
        keep = False
        if valid:
            if _has_done_record(root, unit):
                keep = False
            elif finished is not None and \
                    (stamp - finished).total_seconds() > \
                    COMPLETED_STALE_HOURS * 3600:
                keep = False
            else:
                keep = True
        if keep:
            continue
        # An invalid marker file falls through here too: it
        # suppresses nothing, so dropping it changes no pick.
        try:
            os.remove(path)
        except OSError:
            continue
        dropped.append(unit)
    return dropped


def _write_token_file(path, fields):
    """Write the token file atomically (temp file + rename)."""
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write("---\n"
                 f"claimed_by: {fields['claimed_by']}\n"
                 f"claimed_at: {fields['claimed_at']}\n"
                 f"lease_until: {fields['lease_until']}\n"
                 "---\n\n# Device token\n")
    os.rename(tmp, path)


def cmd_token_acquire(args):
    path = token_path(args.root)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):
        fields, _ = read_unit(path)
        lease = parse_iso(fields.get("lease_until", ""))
        if lease and lease > now_utc():
            remaining = (lease - now_utc()).total_seconds()
            # Issue #461: a re-acquire by the holder itself that lands
            # just before expiry renews the lease instead of reporting
            # held - the old code refused it, so the holder's game
            # input ran with no token until the next acquire. A
            # different executor is still refused, and a holder with
            # ample lease left is still refused, so the
            # mutual-exclusion guarantee is unchanged.
            if (fields.get("claimed_by") == args.executor
                    and remaining <= TOKEN_RENEW_WINDOW_SECONDS):
                fields = {"claimed_by": args.executor,
                          "claimed_at": fields.get("claimed_at", "")
                          or iso(now_utc()),
                          "lease_until": iso(now_utc() + timedelta(
                              minutes=UNIT_CAP_MINUTES))}
                _write_token_file(path, fields)
                print(f"token renewed by {args.executor} "
                      f"until {fields['lease_until']}")
                return 0
            print(f"token held by {fields.get('claimed_by', '?')} "
                  f"until {fields.get('lease_until')}")
            return 1
    fields = {"claimed_by": args.executor,
              "claimed_at": iso(now_utc()),
              "lease_until": iso(now_utc() + timedelta(
                  minutes=UNIT_CAP_MINUTES))}
    _write_token_file(path, fields)
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
              "stats_points_no_achieved": 0,
              "stats_points_no_achieved_units": [],
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
                        else {}, regular):
                    report["stats_points_dup"] += 1
                    report["stats_points_dup_units"].append(
                        f.get("unit"))
                if points_without_achieved(
                        dup_stats if isinstance(dup_stats, dict)
                        else {}):
                    report["stats_points_no_achieved"] += 1
                    report["stats_points_no_achieved_units"].append(
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
        print(f"  stats_points_no_achieved: "
              f"{report['stats_points_no_achieved']}")
        print("  stats_points_no_achieved_units: "
              f"[{', '.join(report['stats_points_no_achieved_units'])}]")
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
        if report["stats_points_no_achieved"]:
            print(f"  stats points without achieved: "
                  f"{report['stats_points_no_achieved']} "
                  f"({', '.join(report['stats_points_no_achieved_units'])})")
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
    p.add_argument("--regulars-json", default="")
    p.set_defaults(fn=cmd_enqueue)

    p = sub.add_parser("list")
    p.add_argument("--state", choices=STATES, default="")
    p.set_defaults(fn=cmd_list)

    p = sub.add_parser("validate")
    p.set_defaults(fn=cmd_validate)

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

    p = sub.add_parser("sweep")
    p.add_argument("--regular", default="zero-sweep")
    p.add_argument("--date", default="")
    p.add_argument("--regulars-json", default="")
    p.set_defaults(fn=cmd_sweep)

    p = sub.add_parser("stats")
    p.add_argument("--format", choices=["text", "yaml", "json"],
                   default="text")
    p.set_defaults(fn=cmd_stats)

    args = parser.parse_args(argv)
    args.root = os.path.abspath(args.root)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
