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

The decision commands (enqueue, sync, plan, sweep, next) run only
from a copy identical to main's _tools_/queue.py (issue #694): a
stale copy refuses, exit 1, so a pass that runs the tool from the
main working tree fails loudly instead of deciding on old
behaviour. Set LASTWAR_QUEUE_ALLOW_STALE_TOOL=1 only for isolated
/tmp fixture validation of a new tool version.

They also refuse when this copy - or the pool it would decide on -
sits under the system temp directory (issue #429): a pass worktree
under /tmp can vanish mid-pass to the runtime's /tmp sweep, so a
decision from there fails loudly at the first command instead of
losing the work at delivery. Set LASTWAR_QUEUE_ALLOW_TMP_ROOT=1
only for isolated /tmp fixture validation of a new tool version.

`next` decides on the live pool (issue #694): it resolves the
given root through live_pool_root first, so a worktree-root
`next` lists the live inbox, not the worktree snapshot - a unit
minted live after the snapshot, and an overlay-clearing unit
staged live, are both visible to the pick, and a unit already
closed live is never handed out again from a stale snapshot
copy. `claim` claims the live-pool copy into the pass root when
the unit sits in the live inbox, so a unit `next` hands out
from the live pool is claimable even when the snapshot never
held it; a unit the live pool holds claimed or done is refused,
and a unit the live pool does not hold at all falls back to
the snapshot copy.

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
             # enqueue mints the unit into the live pool (issue
             # #598): when this copy runs from a linked worktree,
             # the unit lands in the main checkout's _queue_/inbox
             # instead of the worktree's, so a pass that delivers
             # via a worktree cannot strand a unit on the records
             # branch - the next tick reads the live pool only.
             # enqueue refuses a chain head when the chain already
             # has a staged unit under another id (issue #664):
             # the tracker can still show a regular due while its
             # head executes, and the (regular, planned_for)
             # invariant cannot catch the second head because it
             # carries an empty planned_for.
  queue.py [--root DIR] list [--state inbox|claimed|done]
  queue.py [--root DIR] validate [--ref GIT-REF]
             # pool integrity (issue #441): exit 0 when every unit
             # file is free of conflict markers, duplicate
             # top-level frontmatter keys, a unit id that does not
             # match its file name, and a missing unit id; exit 1
             # listing each problem, for a pre-commit / pre-push
             # hook and for the sync/next guard below.
             # --ref checks the committed _queue_ tree at a git
             # ref instead of the working tree, with no checkout
             # (issue #661): a merge resolution is checked with
             # plain validate in the worktree before committing
             # it, a records PR is gated with validate --ref
             # <branch-tip> before it merges to main, and the
             # retro loop-health check is validate --ref main.
             # Exit 2 when the ref cannot be read at all.
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
  queue.py [--root DIR] deadline --unit UNIT
             (--expires-at ISO | --closes-in SECONDS)
             [--priority N] [--reason TEXT]
             # stamp a real deadline onto an inbox unit whose slot
             # expiry is later than its true deadline (issue #623):
             # a train unit staged to its slot end is picked by
             # that expiry, so a boarding closing in minutes is
             # invisible to next - the executor stamps the banner
             # countdown when it sees it and next returns the
             # train first. Only tightens: refuses a deadline at
             # or after the current expiry, a past deadline, and
             # any unit not in inbox; re-stamping the same value
             # is a no-op. The stamp is recorded in the unit body.
  queue.py [--root DIR] complete --unit UNIT --status done
             [--summary TEXT] [--claimed-items a,b] [--evidence PATH]
             [--follow-up TEXT] [--stat key=value ...]
             # complete records the missing keys in
             # result.stats_missing (empty when complete) and warns
             # on stdout (exit still 0) when the closing omits a
             # required result.stats key, so an incomplete closing
             # is flagged in the result itself at the moment it is
             # made instead of surfacing only in the retro.
             # complete also flags a closing whose duration runs
             # over the 15-minute unit cap in result.stats_warnings
             # and warns on stdout (exit still 0), so an overrun is
             # visible in the unit file at the moment it is made
             # instead of surfacing only in the retro (issue #608).
             # a short closing that names its overlay with
             # --stat blocker_overlay=<slug> records the
             # pool-level blocker (the slug maps to its clearing
             # regular in OVERLAY_CLEARING_REGULAR); a done
             # closing by the clearing regular lifts it. The
             # control-lock slug (issue #689) is the exception:
             # it has no clearing regular, next hands out
             # nothing while it stands, and any later closing
             # that sent input lifts it.
             # every closing also records a completion marker in
             # the main checkout's _queue_/completed/ (issue
             # #438), so a unit closed in a detached worktree is
             # never re-picked by the next pass: next, claim,
             # sync and plan all treat a marker like a local
             # done record, and sync reaps markers once the done
             # record lands in the local pool or after 7 days.
  queue.py [--root DIR] release --unit UNIT      # partial: back to inbox
  queue.py [--root DIR] token-acquire --executor NAME
             # a re-acquire by the same executor always renews the
             # lease (issue #461); any other holder is refused
             # while the lease is live.
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
             # regulars, plan owns them. A reset-anchored regular
             # carrying fixup_regulars also stages one pre-reset
             # fix-up unit per ledger regular for each reset day
             # its windows cover (issue #147) - plan is the early
             # path, sweep the just-in-time one.
             # refuses the reset-anchored slots when the roster
             # this copy stages from is stale against main (issue
             # #606): a stale tree used to stage the old pair
             # geometry for a whole day after the roster moved,
             # so plan exits 1 naming the stale regular instead
             # of minting a wrong-geometry pair.
  queue.py [--root DIR] sweep [--regular zero-sweep]
             [--date YYYY-MM-DD] [--regulars-json FILE]
             # produce the pre-reset sweep pair for one reset day
             # from the fixed-slots regular - slots reset-anchored,
             # expiry at the reset instant itself (issue #147);
             # before the pair it stages one fix-up unit per
             # ledger fix-up regular at the pair-midpoint slot,
             # priority 1, expiring at the reset, so the sweep's
             # fix-ups are claimable before the reset instead of
             # sitting in the inbox with not_before at or after
             # it (issue #147, eighth failure running);
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
             # _produce_for_window; refuses also when the roster
             # entry carries no fixup_regulars list, an empty
             # list, or an unknown fix-up regular (issue #147),
             # so a pair with no fix-ups cannot silently repeat
             # the eighth-failure pattern; refuses also when
             # this copy's roster geometry for the regular
             # differs from main's (issue #606), so a stale
             # tree cannot stage the old pair either.
  queue.py [--root DIR] sweep-status [--regular zero-sweep]
             [--date YYYY-MM-DD] [--regulars-json FILE]
             # report one reset day's sweep pair by result.status,
             # never by pool membership (issue #610): a pass counts
             # as executed only when its result.status is done or
             # partial - expired units land in done exactly like
             # executed ones, so the 2040 planner run's "both in
             # done" read reported a false complete while the final
             # pass was expired. Exit 0 when the pair is complete,
             # 1 when it is not, 2 when the roster or regular
             # cannot be read; read-only, and it resolves the root
             # to the live pool (issue #598).
  queue.py [--root DIR] cap-audit [--start YYYY-MM-DD]
             [--end YYYY-MM-DD]
             # list every done closing whose duration runs over the
             # 15-minute unit cap (900 seconds), by local finished
             # date in the window (issue #608): the retro's Nov 4-10
             # window held 12 such units, hand-counted from the
             # pool - this command reproduces that list
             # mechanically. Defaults cover the 7 days ending today
             # local. Exit 0 when no closing is over the cap, 1
             # when any is, 2 on a bad date; read-only, and it
             # resolves the root to the live pool (issue #598).

--root defaults to the repository _queue_ folder; it also accepts
a repository root, resolved to its _queue_ folder, or a pool
directory directly (issue #510). enqueue refuses a root holding
no pool state directory, so a wrong root never mints units into
a fresh empty directory; tests point it at a scratch directory.

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
import tempfile
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

UNIT_CAP_MINUTES = 15           # owner rule 2026-10-28: per unit
UNIT_CAP_SECONDS = UNIT_CAP_MINUTES * 60   # 900: the cap, in seconds
# Issue #461: a same-holder re-acquire always renews the lease.
# The 2026-11-08 rule renewed only within 60 seconds of expiry, but
# the executor loop re-acquires at every unit boundary (design
# section 6), so a re-acquire after a short unit lands minutes before
# expiry and was refused - ticker-0234 (2026-11-10 02:50 PST) and
# ticker-0504 (05:20 PST) both ran game input with no token held
# after exactly that refusal. Renewing only ever extends the current
# pass's own lease (executor names are per-pass), a different holder
# is still refused while the lease is live, and a dead pass's lease
# still expires 15 minutes after its last renewal, so mutual
# exclusion and the expiry safety valve are unchanged.
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
# Miss-audit root-cause classes, task-unit-queue-design.md per-unit
# measurement table (mirrored in _tools_/retro_report.py
# BLOCKER_CLASSES): a window closure, b crowding out, c tap
# method, d inference over live read, e repeated blocker,
# f missing precondition, g true red-line miss, h by-design
# partial, i owner-named without escalation.
BLOCKER_CATEGORIES = "abcdefghi"
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

    A resolved _queue_ pool whose parent still holds top-level
    pool state directories warns too (issue #539): the parent is
    a repository root with a stray pool beside the real one, and
    the stray must be removed rather than silently ignored, or a
    later diff against the repository root reads the wrong pool.
    """
    if any(os.path.isdir(state_dir(root, s)) for s in STATES):
        if os.path.basename(os.path.abspath(root)) == "_queue_":
            parent = os.path.dirname(os.path.abspath(root))
            stray = [s for s in STATES
                     if os.path.isdir(state_dir(parent, s))]
            if stray:
                return (f"warning: stray pool state at {parent}: "
                        f"{', '.join(stray)} beside the resolved pool "
                        "- remove the stray so a later diff against "
                        "the repository root cannot read the wrong "
                        "pool (issue #539)")
        return ""
    return (f"warning: pool root {root} holds no inbox, claimed "
            "or done directory - the counts below describe an "
            "empty or wrong root, not the live pool")


def resolve_pool_root(root):
    """Return the pool directory for a repository root or a pool dir.

    --root names a pool, but the planner body passes the repository
    root (issue #510): the first --apply then wrote units into a
    stray <repo>/inbox/ the ticker never reads. A root holding a
    _queue_ subdirectory and no pool state directory of its own is
    a repository root, so resolve it to <root>/_queue_; a root that
    already holds pool state directories is a pool and passes
    through unchanged, matching pool_gap.py's resolve_pool. Any
    other root passes through unchanged for the caller to judge:
    read commands warn through pool_root_warning, write commands
    refuse (see cmd_enqueue).

    A root holding BOTH top-level pool state directories and a
    _queue_ subdirectory is a repository root with a stray pool
    beside the real one (issue #539: any pre-#512 run minted a
    stray <repo>/inbox/, and the stray is never read by the
    ticker): a genuine pool never contains a _queue_ subdir, so
    resolve it to <root>/_queue_ and let pool_root_warning name
    the stray so it gets removed instead of silently ignored.
    """
    if not root:
        return root
    queue_dir = os.path.join(root, "_queue_")
    if os.path.isdir(queue_dir):
        return queue_dir
    return root


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


def _validate_unit_text(rel, text):
    """Pool-integrity problems in one unit file's text, as strings.

    Shared by validate_pool (working tree) and validate_ref (a git
    ref): the same checks must answer on both, so a branch tip is
    judged by exactly the rule the working tree is judged by.
    """
    problems = []
    for lineno, line in enumerate(text.splitlines(), 1):
        if line.startswith(CONFLICT_MARKERS):
            problems.append(
                f"{rel}:{lineno}: unresolved conflict marker")
    keys, has_fm = _frontmatter_top_keys(text)
    if not has_fm:
        problems.append(f"{rel}: no frontmatter block")
        return problems
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
    elif f"{unit}.md" != os.path.basename(rel):
        problems.append(
            f"{rel}: unit id {unit!r} does not match file name")
    return problems


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
            problems.extend(_validate_unit_text(rel, text))
    return problems


def validate_ref(root, ref):
    """Pool-integrity problems in the _queue_ tree at a git ref.

    Issue #661: merge dd865af64b ("Merge main into
    records/2026-11-10 to reconcile PR #615 queue conflicts")
    committed a rename/add conflict unresolved, and the three
    conflict-marker unit files it created (trucks, events,
    secrets 2026-11-11-1457) rode the records PR onto main,
    because validate only ever ran on a working tree: sync and
    next guard the ticker's own pool, but no check ran on the
    merge resolution before it was committed, and no check ran
    on the branch tip before the records PR merged. This runs
    the same per-file checks as validate_pool against the
    committed tree, with no checkout: the pre-merge gate is
    `validate --ref <branch-tip>` before `gh pr merge`, the
    merge-resolution check is plain `validate` in the worktree
    before committing the resolution, and the retro
    loop-health check is `validate --ref main`. Returns
    (problems, error): error is a short reason string when the
    ref cannot be read at all (unknown ref, not a repo), and
    None otherwise; problems is [] on a clean tree.

    The tree is listed whole and filtered in Python: this
    tool's root is the _queue_ subdir, not the repo top, so a
    `_queue_` pathspec would be read relative to the caller's
    working directory and silently match nothing - and ls-tree
    names are cwd-relative too, so the listing needs
    --full-name for the repo-root-relative filter below to
    hold (same pitfall as records_branch_done_units).
    """
    try:
        listing = subprocess.run(
            ["git", "-C", root, "ls-tree", "-r", "--full-name",
             "--name-only", ref],
            capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError) as exc:
        return [], f"cannot list tree at {ref!r}: {exc}"
    if listing.returncode != 0:
        detail = [line for line in (listing.stderr or "").splitlines()
                  if line.strip()]
        reason = detail[-1].strip() if detail else "git ls-tree failed"
        return [], f"cannot list tree at {ref!r}: {reason[:120]}"
    problems = []
    for path in listing.stdout.splitlines():
        name = path.strip()
        parts = name.split("/")
        if len(parts) != 3 or parts[0] != "_queue_":
            continue
        state, fname = parts[1], parts[2]
        if state not in STATES or not fname.endswith(".md"):
            continue
        if fname == TOKEN_NAME:
            continue
        try:
            shown = subprocess.run(
                ["git", "-C", root, "show", f"{ref}:{name}"],
                capture_output=True, text=True, timeout=30)
        except (OSError, subprocess.SubprocessError) as exc:
            problems.append(f"{state}/{fname}: unreadable at "
                            f"{ref}: {exc}")
            continue
        if shown.returncode != 0:
            problems.append(f"{state}/{fname}: unreadable at "
                            f"{ref}: git show failed")
            continue
        rel = f"{state}/{fname}"
        problems.extend(_validate_unit_text(rel, shown.stdout))
    return problems, None


def cmd_validate(args):
    if getattr(args, "ref", ""):
        problems, error = validate_ref(args.root, args.ref)
        if error is not None:
            print(error, file=sys.stderr)
            return 2
        for problem in problems:
            print(problem)
        if problems:
            print(f"pool invalid at {args.ref}: {len(problems)} "
                  f"problem(s) (issue #661)")
            return 1
        print(f"pool valid at {args.ref}")
        return 0
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
# Control-channel lock (issue #689): the outcome_unknown lock after
# a session drop blocks every input action - read-only inspection
# stays live, new sessions do not clear it, reconcile cannot clear
# it. Evidence: 2026-10-26 to 2026-10-27 froze 18 consecutive
# segment runs and cleared only when the owner submitted locally
# on 2026-10-27; 2026-11-12 01:34-02:07 blocked three consecutive
# ticker passes the same way. No self-clear has ever been observed.
# A unit that closes short naming this slug records a pool-level
# control-lock blocker; next hands out nothing while one stands,
# so a locked night burns no failed units. The lock has no clearing
# regular - any later closing that sent input (done, partial, or
# skipped-needs-owner, without naming the lock) lifts it - and the
# BLOCKER_STALE_HOURS bound is the wait-and-retry rule: sync reaps
# a control-lock blocker older than 4 hours, the next tick probes
# with one input, and a fresh outcome_unknown re-records it.
CONTROL_LOCK_SLUG = "control-lock"
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
    markers = reap_stale_completion_markers(args.root)
    markers_reaped = markers["reaped"]
    markers_lost = markers["lost"]
    if markers_lost:
        print("warning: completion markers aged out with no local "
              f"done record - the delivery never carried these "
              f"closings: {", ".join(markers_lost)} (issue #563)")
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
                      "completion_markers_lost": markers_lost,
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
    # Absolute 24h steps from the anchor (issue #603): the old
    # naive wall-clock subtraction kept the previous duel day
    # until 19:00 local, but since the 2026-11-02 daylight-saving
    # end the roll is 18:00 PST (02:00 UTC, issue #242) - so a
    # slot in the 18:00-19:00 hour was stamped one duel day
    # behind, e.g. radar-2026-11-10-1803 "duel day 2 - radar
    # stack" while the live day was 3 release. Timestamps are
    # the absolute measure here, as in duel.py current() and in
    # cycle_start_local's daily-reset branch: wall-clock
    # arithmetic on an aware datetime sharing one tzinfo is not
    # elapsed time. A naive caller time is read as schedule-local
    # wall time, mirroring duel.py. Both call sites (sync, plan)
    # pass an aware LOCAL_TZ planned_local.
    if planned_local.tzinfo is None:
        planned_local = planned_local.replace(tzinfo=LOCAL_TZ)
    anchor = DUEL_ANCHOR_LOCAL.replace(tzinfo=LOCAL_TZ)
    day_index = int((planned_local.timestamp()
                     - anchor.timestamp()) // 86400)
    duel_day = day_index % 7 + 1
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
                        closed_ids=None, expires_dt=None, priority=None):
    """Enqueue the unit for one (regular, window) pair, or return
    None when that pair already exists in any state - the pool's
    anti-duplication invariant, shared by sync and plan. A pair
    whose unit id is in closed_ids (unit -> where it closed) is
    also not produced: the slot already closed on the delivered
    records branch or in another worktree, and minting a fresh
    unit with the same deterministic id would re-execute it
    (issue #466). Callers that pass no closed set keep the old
    behaviour; plan passes its own set (issue #465) and sweep
    keeps the old behaviour. expires_dt overrides the
    cadence-derived expiry and priority overrides the
    SYNC_PRIORITY default - both are used by the pre-reset
    sweep fix-ups (issue #147), which expire at the reset they
    serve and run at priority 1 regardless of their regular's
    usual cadence and priority."""
    # Live-pool production (issue #598): sync / plan / sweep mint
    # through here, and a pass running this copy from a delivery
    # worktree would otherwise stage the unit into the worktree's
    # inbox, where the live pool never sees it - resolve to the
    # main checkout's _queue_ first; a scratch root keeps itself.
    root = live_pool_root(root)
    regular = item["id"]
    planned_utc = planned_local.astimezone(timezone.utc)
    planned_iso = iso(planned_utc)
    expected = _sweep_slot_geometry(item, planned_local)
    if expected is not None:
        # Roster-freshness gate (issue #606), backstop: the
        # producers pre-check this before staging anything for
        # the regular (plan's per-item loop, sweep before its
        # fix-ups), so a refusal here means a caller staged
        # without pre-checking. Refuse the slot instead of
        # minting a wrong-geometry unit, and record the refusal
        # so the command exits 1 on it.
        refusal = _roster_geometry_refusal(root, item)
        if refusal is not None:
            _ROSTER_FRESH_REFUSALS.append(refusal)
            return None
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
    if expires_dt is None:
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
        "priority": priority if priority is not None else \
            SYNC_PRIORITY.get(regular, 3),
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
ROSTER_FRESH_REF = "refs/queue-fresh/main"


# Roster-freshness gate (issue #606): slots staged from a roster
# this copy has not refreshed against main. _main_roster_offsets
# caches one fetch per process; _ROSTER_FRESH_REFUSALS collects
# the regulars the production path refused to stage, so the
# command can exit 1 on them instead of counting a refused slot
# as already present.
_MAIN_ROSTER_OFFSETS_CACHE = {"attempted": False, "offsets": None,
                              "warning": None, "warned": False}
_ROSTER_FRESH_REFUSALS = []


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


# Main fetch, shared (issues #606, #694): both the roster-freshness
# check and the tool-currency guard read main without touching a
# checked-out branch or the working tree. _fetch_main caches one
# fetch per process per git directory, however many checks the run
# performs.
_MAIN_FETCH_CACHE = {"attempted": False, "ok": False, "warning": None,
                     "dir": None}


def _fetch_main(git_dir):
    """Fetch main into the private ref, or (False, reason).

    Returns (True, None) on success, (False, "no-remote") when
    the repo has no usable remote, (False, "fetch-failed")
    otherwise. The ref is ROSTER_FRESH_REF, the same private ref
    the roster check already used, so a second fetch in one
    process is a no-op fast-forward.
    """
    if (_MAIN_FETCH_CACHE["attempted"]
            and _MAIN_FETCH_CACHE["dir"] == git_dir):
        return _MAIN_FETCH_CACHE["ok"], _MAIN_FETCH_CACHE["warning"]
    _MAIN_FETCH_CACHE["attempted"] = True
    _MAIN_FETCH_CACHE["dir"] = git_dir
    remote = _git_remote(git_dir)
    if remote is None:
        _MAIN_FETCH_CACHE["ok"] = False
        _MAIN_FETCH_CACHE["warning"] = "no-remote"
        return False, "no-remote"
    try:
        fetch = subprocess.run(
            ["git", "-C", git_dir, "fetch", "--depth", "1", remote,
             "+main:%s" % ROSTER_FRESH_REF],
            capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        _MAIN_FETCH_CACHE["ok"] = False
        _MAIN_FETCH_CACHE["warning"] = "fetch-failed"
        return False, "fetch-failed"
    if fetch.returncode != 0:
        _MAIN_FETCH_CACHE["ok"] = False
        _MAIN_FETCH_CACHE["warning"] = "fetch-failed"
        return False, "fetch-failed"
    _MAIN_FETCH_CACHE["ok"] = True
    _MAIN_FETCH_CACHE["warning"] = None
    return True, None


def _main_roster_offsets(root):
    """slots_before_reset_minutes per regular on the main tip.

    Fetches main into a private ref (never a checked-out branch,
    never the working tree), mirroring records_branch_done_units,
    and reads _tools_/regulars.json at that ref. Returns
    (offsets, None) on success - offsets maps regular id to its
    sorted slot offsets - or (None, warning) when main cannot be
    read: no git remote, fetch failed, no roster at the ref, or
    an unparseable roster. A caller that cannot read main warns
    and stages from the local roster, exactly like the branch
    reconcile: an unreadable main never blocks the tick, but a
    readable main whose geometry differs from the local roster
    is positive proof the staging copy is stale (issue #606).
    Cached per process: one fetch per invocation, however many
    windows the run stages.
    """
    if _MAIN_ROSTER_OFFSETS_CACHE["attempted"]:
        return (_MAIN_ROSTER_OFFSETS_CACHE["offsets"],
                _MAIN_ROSTER_OFFSETS_CACHE["warning"])
    _MAIN_ROSTER_OFFSETS_CACHE["attempted"] = True
    fetched, fetch_reason = _fetch_main(root)
    if not fetched:
        if fetch_reason == "no-remote":
            _MAIN_ROSTER_OFFSETS_CACHE["warning"] = (
                "no git remote, roster-freshness check skipped")
        else:
            _MAIN_ROSTER_OFFSETS_CACHE["warning"] = (
                "fetch of main failed, roster-freshness check skipped")
        return None, _MAIN_ROSTER_OFFSETS_CACHE["warning"]
    try:
        show = subprocess.run(
            ["git", "-C", root, "show",
             "%s:_tools_/regulars.json" % ROSTER_FRESH_REF],
            capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        _MAIN_ROSTER_OFFSETS_CACHE["warning"] = (
            "read of main roster failed, roster-freshness check "
            "skipped")
        return None, _MAIN_ROSTER_OFFSETS_CACHE["warning"]
    if show.returncode != 0:
        _MAIN_ROSTER_OFFSETS_CACHE["warning"] = (
            "read of main roster failed, roster-freshness check "
            "skipped")
        return None, _MAIN_ROSTER_OFFSETS_CACHE["warning"]
    try:
        main_regs = json.loads(show.stdout)["regulars"]
    except (ValueError, KeyError, TypeError):
        _MAIN_ROSTER_OFFSETS_CACHE["warning"] = (
            "main roster unparseable, roster-freshness check "
            "skipped")
        return None, _MAIN_ROSTER_OFFSETS_CACHE["warning"]
    offsets = {}
    for entry in main_regs:
        if not isinstance(entry, dict):
            continue
        rid = entry.get("id")
        if not rid:
            continue
        offsets[rid] = _reset_anchored_offsets(entry)
    _MAIN_ROSTER_OFFSETS_CACHE["offsets"] = offsets
    return offsets, None


def _roster_geometry_refusal(root, item):
    """Refusal for a reset-anchored regular staged from a stale
    roster, or None when staging may proceed.

    Issue #606: the Nov 11 pair was staged at the old 16:30/17:30
    geometry five hours after PR #614 moved the roster to 120/60,
    because plan ran from a live tree still on a Nov 3 HEAD and
    nothing compared its roster against main. A readable main
    whose slot offsets differ from this copy's is positive proof
    the staging copy is stale: the caller refuses the regular
    outright - before any fix-up or window is staged, so a
    refused sweep leaves no orphan fix-ups at the old midpoint
    for the corrected re-run to duplicate - and names the remedy
    (update this checkout's _tools_/regulars.json from main).
    Returns None when the item is not reset-anchored, when main
    cannot be read (warn once, fail-open like the branch
    reconcile: a scratch root has no remote at all, and a failed
    fetch must never block the tick), when main does not name
    the regular, or when the geometries match.
    """
    if not _reset_anchored_offsets(item):
        return None
    main_offsets, fresh_warning = _main_roster_offsets(root)
    if fresh_warning:
        if not _MAIN_ROSTER_OFFSETS_CACHE["warned"]:
            print(f"warning: {fresh_warning} (issue #606)",
                  file=sys.stderr)
            _MAIN_ROSTER_OFFSETS_CACHE["warned"] = True
        return None
    if main_offsets is None:
        return None
    main = main_offsets.get(item.get("id"))
    if main is None:
        return None
    local = _reset_anchored_offsets(item)
    if main == local:
        return None
    print(f"refused: {item.get('id')} roster is stale against "
          f"main - this copy stages {local} minutes before the "
          f"reset, main stages {main} - update this checkout's "
          f"_tools_/regulars.json from main before staging "
          f"(issue #606)",
          file=sys.stderr)
    return {"regular": item.get("id"), "local_offsets": local,
            "main_offsets": main}


# ---------------------------------------------------------------------
# Tool-currency guard (issue #694)
# ---------------------------------------------------------------------

TOOL_ALLOW_STALE_ENV = "LASTWAR_QUEUE_ALLOW_STALE_TOOL"
TOOL_GUARDED_COMMANDS = ("enqueue", "sync", "plan", "sweep", "next")


def _tool_dir():
    """Directory holding this copy of queue.py, symlinks resolved."""
    return os.path.dirname(os.path.realpath(__file__))


def main_tool_source():
    """This tool as main carries it, or (None, warning).

    Fetches main into the private ref (shared with the roster
    check) and reads _tools_/queue.py at that ref. Returns
    (bytes, None) on success, or (None, warning) when main
    cannot be read: no git remote, fetch failed, or no tool at
    the ref. A caller that cannot read main warns and continues,
    exactly like the branch reconcile: an unreadable main never
    blocks the tick, but a readable main whose tool differs from
    this copy is positive proof the running copy is stale.
    """
    fetched, reason = _fetch_main(_tool_dir())
    if not fetched:
        if reason == "no-remote":
            return None, "no git remote, tool-currency check skipped"
        return None, "fetch of main failed, tool-currency check skipped"
    try:
        show = subprocess.run(
            ["git", "-C", _tool_dir(), "show",
             "%s:_tools_/queue.py" % ROSTER_FRESH_REF],
            capture_output=True, timeout=30)
    except (OSError, subprocess.SubprocessError):
        return None, ("read of main tool failed, tool-currency check "
                      "skipped")
    if show.returncode != 0:
        return None, ("read of main tool failed, tool-currency check "
                      "skipped")
    return show.stdout, None


def tool_is_current():
    """(True, None) when this copy matches main's queue.py.

    Returns (True, None) when the running file is byte-identical
    to main's copy, (False, None) when main's copy differs, and
    (None, warning) when main cannot be read. The byte compare
    cannot tell ahead from behind: any difference is stale for a
    live pass, which must run main's tool - isolated fixture
    validation of a new tool version sets
    LASTWAR_QUEUE_ALLOW_STALE_TOOL=1 instead.
    """
    try:
        with open(os.path.realpath(__file__), "rb") as handle:
            local = handle.read()
    except OSError as exc:
        return None, "cannot read this copy of queue.py (%s)" % exc
    main_source, warning = main_tool_source()
    if main_source is None:
        return None, warning
    return local == main_source, None


def refuse_if_tool_stale(cmd):
    """Refusal exit code when this copy is stale for a decision.

    Issue #694: the ticker-0334 pass ran queue.py from the main
    working tree - a checkout on another job's branch predating
    PR #692 - and next handed out a unit during the R9
    control-lock pause the stale copy could not see. The
    decision commands (enqueue, sync, plan, sweep, next) refuse
    - exit 1, nothing staged or handed out - when this copy
    differs from main's _tools_/queue.py, so a stale pass fails
    loudly instead of deciding on old behaviour. An unreadable
    main warns and lets the command proceed, like the #606
    roster check. Claim, complete and the token commands stay
    unguarded: a pass that already decided must be able to
    finish even if main advances mid-pass. Returns 1 on refusal,
    else None.
    """
    if os.environ.get(TOOL_ALLOW_STALE_ENV) == "1":
        print(f"warning: {TOOL_ALLOW_STALE_ENV}=1, tool-currency "
              f"check bypassed for isolated validation (issue #694)",
              file=sys.stderr)
        return None
    current, warning = tool_is_current()
    if current is None:
        print(f"warning: {warning} (issue #694)", file=sys.stderr)
        return None
    if current:
        return None
    print(f"{cmd} refused: this copy of queue.py differs from "
          f"main's _tools_/queue.py - run the tool from a fresh "
          f"main checkout (a pass worktree, never the main working "
          f"tree) so the pass decides on current behaviour "
          f"(issue #694)", file=sys.stderr)
    return 1


# ---------------------------------------------------------------------
# Worktree-location guard (issue #429)
# ---------------------------------------------------------------------

TOOL_ALLOW_TMP_ROOT_ENV = "LASTWAR_QUEUE_ALLOW_TMP_ROOT"


def _temp_roots():
    """System temp directories, symlinks resolved.

    /tmp plus the platform temp dir (tempfile.gettempdir, which
    honours TMPDIR): on this VM /tmp is a 512M tmpfs the runtime
    wipes, and on the Mac TMPDIR is a per-user folder the OS
    cleans. Both are the same hazard - a checkout under either
    can vanish mid-pass.
    """
    roots = set()
    for candidate in ("/tmp", tempfile.gettempdir()):
        roots.add(os.path.realpath(candidate))
    return roots


def _is_under(path, root):
    """True when realpath(path) is root or lives under it."""
    path = os.path.realpath(path)
    return path == root or path.startswith(root + os.sep)


def _tmp_location(pool_root):
    """(True, where) when a decision would run from a temp dir.

    Checks the checkout holding this copy of queue.py (the parent
    of _tools_/) and the pool --root resolves to: either one under
    the system temp directory is a doomed checkout. Returns
    (False, None) when neither is under a temp dir. Pure path
    math, no fetch, so there is no unreadable-main case - the
    bypass env is the only escape.
    """
    temps = _temp_roots()
    for where, path in (("tool copy", os.path.dirname(_tool_dir())),
                       ("pool", pool_root)):
        for temp in temps:
            if _is_under(path, temp):
                return True, "%s %s sits under temp dir %s" % (
                    where, path, temp)
    return False, None


def refuse_if_tmp_worktree(cmd, pool_root):
    """Refusal exit code when a decision would run from /tmp.

    Issue #429: on 2026-11-07 three ticker passes created their
    worktrees under /tmp and all three vanished mid-pass to the
    runtime's /tmp sweep, taking uncommitted records, INDEX
    appends and unit completions with them; on 2026-11-08 the
    retro run lost /tmp/retro-1108-branch the same way, after
    PR #432 had already landed pass_worktree.py, which refuses
    /tmp targets at creation - the tool is opt-in, and a pass
    that creates its worktree with a bare `git worktree add`
    under /tmp never touches it. So the decision commands
    (enqueue, sync, plan, sweep, next) refuse - exit 1, nothing
    staged or handed out - when this copy of queue.py, or the
    pool it would decide on, sits under the system temp
    directory, and the pass fails loudly at its first decision
    instead of losing a finished unit's record at delivery.
    LASTWAR_QUEUE_ALLOW_TMP_ROOT=1 bypasses only for isolated
    /tmp fixture validation of a new tool version. Claim,
    complete and the token commands stay unguarded, like the
    #694 guard: a pass that already decided can finish even if
    its worktree was created under /tmp. Returns 1 on refusal,
    else None.
    """
    if os.environ.get(TOOL_ALLOW_TMP_ROOT_ENV) == "1":
        print(f"warning: {TOOL_ALLOW_TMP_ROOT_ENV}=1, worktree-location "
              f"check bypassed for isolated validation (issue #429)",
              file=sys.stderr)
        return None
    is_tmp, where = _tmp_location(pool_root)
    if not is_tmp:
        return None
    print(f"{cmd} refused: {where} - create the pass worktree under "
          f"~/workspace/lastwar-worktrees/ (never /tmp) and run the "
          f"tool from there (issue #429)", file=sys.stderr)
    return 1


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
    fixups_planned, fixups_present = [], 0
    for item in regs:
        current = cycle_start_local(item, now_local)
        windows = plan_windows(item, now_local, horizon_end)
        # Roster-freshness gate (issue #606): refuse the whole
        # regular before any fix-up or window is staged, so a
        # refused pair leaves no orphan fix-ups at the old
        # midpoint for the corrected re-run to duplicate. The
        # helper returns None for a non-reset-anchored item, so
        # this runs for every regular and only ever fires for
        # a reset-anchored one.
        refusal = _roster_geometry_refusal(args.root, item)
        if refusal is not None:
            _ROSTER_FRESH_REFUSALS.append(refusal)
            continue
        # Pre-reset fix-ups (issue #147): a reset-anchored regular
        # carrying fixup_regulars stages one fix-up unit per
        # ledger regular for each reset day its windows cover,
        # before its own windows are produced - so the fix-ups
        # exist from the morning (the planner calls sweep only at
        # about 17:50, ten minutes before the reset, which is too
        # late for more than one fix-up to run) and their
        # created_at precedes the final pass. A roster entry with
        # no fixup_regulars list stages nothing here; a present
        # but invalid list warns and continues - plan never blocks
        # the whole staging run, while sweep refuses outright.
        if item.get("cadence") == "fixed-slots" and \
                _reset_anchored_offsets(item) and \
                item.get("fixup_regulars") is not None:
            for day in sorted({w.date() for w in windows}):
                fix = _stage_sweep_fixups(
                    args.root, regs, item, day, closed_ids=closed)
                if fix["error"]:
                    print(f"warning: sweep fix-ups for "
                          f"{item.get('id')} "
                          f"{day.isoformat()} not staged: "
                          f"{fix['error']} (issue #147)",
                          file=sys.stderr)
                else:
                    fixups_planned.extend(fix["produced"])
                    fixups_present += fix["already_present"]
                    skipped_closed.extend(fix["skipped_closed"])
        for w in windows:
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
                      "fixups_planned": fixups_planned,
                      "fixups_already_present": fixups_present,
                      "skipped_done_current": skipped_done,
                      "skipped_closed": skipped_closed,
                      "roster_stale_regulars": stale_roster,
                      "roster_fresh_refusals": _ROSTER_FRESH_REFUSALS,
                      "aged_p1_windowed": aged_p1_windowed},
                     ensure_ascii=False))
    return 1 if _ROSTER_FRESH_REFUSALS else 0


def _stage_sweep_fixups(root, regs, item, local_date, closed_ids=None):
    """Stage one pre-reset fix-up unit per ledger regular (issue #147).

    The sweep pair walks the ledger and its fix-ups are the units
    that close the not-at-zero lines - but on 2026-11-08 every
    fix-up in the inbox carried not_before at or after the 18:00
    reset (the planner stages the every-run fix-up regulars on a
    4-hour grid whose evening window is 18:03, and the daily-reset
    ones at 18:00 itself), so none could run before the reset and
    the trade day closed with 12 lines not at zero, the eighth
    consecutive failure. The fix-up slot is the midpoint of the
    pair's slots (reset - 90 minutes for the [120, 60] pair, 16:30
    local): after the first pass so the ticker is free to pick
    them, before the reset so they can still close the day, and
    off the planner's 4-hour grid so no ordinary window collides
    with it. Each fix-up runs at priority 1 (the design's fix-up
    priority, section 12) and expires at the reset it serves, so
    an unclaimed fix-up never outlives its trade day. Fix-ups are
    staged before the pair in the same production call, so
    pick_key orders them ahead of the final pass at equal expiry
    (the reset) and priority (1): their created_at stamp is never
    later than the pair's, and on a same-second tie the stable
    sort keeps the alphabetical pool order, in which every
    fix-up regular's name sorts before zero-sweep.

    Returns {"produced": [...], "already_present": n,
    "skipped_closed": [...], "error": str-or-None}. error is set
    (and nothing is staged) when the roster entry carries no
    fixup_regulars list, the list is empty, or it names a regular
    the roster does not hold. A reset day whose reset instant is
    already past stages nothing and reports no error - plan asks
    for every reset day its horizon covers, including one whose
    pair slot already passed.
    """
    fixups = item.get("fixup_regulars")
    if fixups is None:
        return {"produced": [], "already_present": 0,
                "skipped_closed": [],
                "error": f"regular {item.get('id')!r} carries no "
                         f"fixup_regulars list - sync the tree to "
                         f"main before producing the sweep pair"}
    if not isinstance(fixups, list) or not fixups:
        return {"produced": [], "already_present": 0,
                "skipped_closed": [],
                "error": f"regular {item.get('id')!r} carries an "
                         f"empty fixup_regulars list - a sweep pair "
                         f"with no fix-ups repeats the issue #147 "
                         f"defect"}
    by_id = {r.get("id"): r for r in regs}
    for fid in fixups:
        if fid not in by_id:
            return {"produced": [], "already_present": 0,
                    "skipped_closed": [],
                    "error": f"fixup regular {fid!r} is not in the "
                             f"roster - fix fixup_regulars on "
                             f"regular {item.get('id')!r} before "
                             f"producing the sweep pair"}
    reset_local = _reset_instant_for_local_date(item, local_date)
    if reset_local <= datetime.now(LOCAL_TZ):
        return {"produced": [], "already_present": 0,
                "skipped_closed": [], "error": None}
    offsets = _reset_anchored_offsets(item)
    midpoint = (offsets[0] + offsets[-1]) // 2
    slot = reset_local - timedelta(minutes=midpoint)
    reset_utc = reset_local.astimezone(timezone.utc)
    produced, already, skipped = [], 0, []
    for fid in fixups:
        unit_id = _unit_id_for_window(by_id[fid], slot)
        unit = _produce_for_window(
            root, by_id[fid], slot,
            f"pre-reset fix-up for {local_date.isoformat()} sweep",
            closed_ids=closed_ids, expires_dt=reset_utc, priority=1)
        if unit:
            produced.append(unit)
        elif closed_ids and unit_id in closed_ids:
            skipped.append(unit_id)
        else:
            already += 1
    return {"produced": produced, "already_present": already,
            "skipped_closed": skipped, "error": None}


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
    It also stages the day's fix-ups before the pair
    (_stage_sweep_fixups, issue #147, eighth failure running):
    one priority-1 unit per ledger fix-up regular at the
    pair-midpoint slot, expiring at the reset, so the sweep's
    fix-ups are claimable in the pre-reset window instead of
    sitting in the inbox with not_before at or after the reset.
    A roster entry with no fixup_regulars list, an empty list,
    or an unknown fix-up regular is refused the same way - a
    pair with no fix-ups would silently repeat the #147 defect.
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
    # Roster-freshness gate (issue #606): refuse before any
    # fix-up is staged, so a refused sweep leaves no orphan
    # fix-ups at the old midpoint for the corrected re-run to
    # duplicate.
    refusal = _roster_geometry_refusal(args.root, item)
    if refusal is not None:
        _ROSTER_FRESH_REFUSALS.append(refusal)
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
    # Pre-reset fix-ups (issue #147): staged before the pair so
    # their created_at precedes the final pass and pick_key orders
    # them ahead of it. The closed set is the same branch-done +
    # completion-marker set plan consults (issues #465, #466), so
    # a fix-up already closed on the delivered branch is not
    # re-staged as a phantom the way the 1630 pair unit was on
    # 2026-11-08. A branch that cannot be read warns and the run
    # continues on local state only, as in plan.
    branch = "records/%s" % local_date.isoformat()
    branch_done, branch_warning = records_branch_done_units(
        args.root, branch)
    if branch_warning:
        print(f"warning: {branch_warning} (issues #446, #466)",
              file=sys.stderr)
    closed = {unit: "done on %s" % branch for unit in branch_done}
    for unit in completion_marker_units(args.root):
        closed.setdefault(unit, "completion marker in another "
                                "worktree")
    fix = _stage_sweep_fixups(args.root, regs, item, local_date,
                              closed_ids=closed)
    if fix["error"]:
        print(f"refused: {fix['error']} (issue #147)")
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
        "produced": produced, "already_present": already,
        "roster_fresh_refusals": _ROSTER_FRESH_REFUSALS,
        "fixups_produced": fix["produced"],
        "fixups_already_present": fix["already_present"],
        "fixups_skipped_closed": fix["skipped_closed"]},
        ensure_ascii=False))
    return 1 if _ROSTER_FRESH_REFUSALS else 0


def cmd_sweep_status(args):
    """Report one reset day's sweep pair by result status, never by
    pool membership.

    Issue #610: the 2040 planner run reported tonight's sweep pair
    complete because both passes sat in _queue_/done/ - but the
    final pass's result.status was expired (window passed before
    execution), and expired units land in done exactly like
    executed ones. Pool membership in done does not mean executed,
    so a pair check that reads location reports a false complete
    and hides the tenth consecutive sweep failure.

    This command reads the same reset-anchored geometry sweep
    stages from (the fixed-slots regular's slots_before_reset,
    chain id, reset instant) and reports, for each expected pass,
    where its unit file sits and what result.status it carries.
    A pass counts as executed only when its result.status is done
    or partial; expired, failed and skipped-needs-owner are closed
    without execution, a done file with no result status is a bare
    file (not a completed execution, the same rule as
    _has_done_record), and inbox / claimed / absent are pending,
    claimed and missing. pair_complete is true only when every
    pass executed with the expected chain sequence. Exit 0 when
    the pair is complete, 1 when it is not, 2 when the roster or
    regular cannot be read - the gate command's exit-code
    convention (log_append.py), so a planner run can gate on it.

    Read-only: it writes nothing to the pool. It resolves the
    root to the live pool (issue #598), so a copy running from a
    delivery worktree reads the live pool, not the worktree's
    stale copy. Unlike sweep it never refuses a past reset -
    checking a past day's pair is the whole point. Done wins over
    inbox and claimed when a unit id sits in more than one state
    (a stale inbox duplicate, issue #213): the done record is
    the closing, so the status check reads that one.
    """
    root = live_pool_root(args.root)
    warning = pool_root_warning(root)
    if warning:
        print(warning)
    defs_path = args.regulars_json or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "regulars.json")
    try:
        with open(defs_path, encoding="utf-8") as fh:
            regs = json.load(fh)["regulars"]
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"refused: cannot read roster {defs_path}: {exc}")
        return 2
    item = next((r for r in regs if r.get("id") == args.regular), None)
    if item is None:
        print(f"refused: regular {args.regular!r} not in roster "
              f"{defs_path} - sync the tree to main before checking "
              f"the sweep pair")
        return 2
    if item.get("cadence") != "fixed-slots" or \
            not _reset_anchored_offsets(item):
        print(f"refused: regular {args.regular!r} carries no "
              f"reset-anchored slots (reset_utc + "
              f"slots_before_reset_minutes) - no sweep pair to "
              f"check (issue #610)")
        return 2
    if args.date:
        try:
            year, month, day = (int(x) for x in args.date.split("-"))
            local_date = datetime(year, month, day).date()
        except ValueError:
            print(f"refused: --date {args.date!r} is not YYYY-MM-DD")
            return 2
    else:
        local_date = datetime.now(LOCAL_TZ).date()
    reset_local = _reset_instant_for_local_date(item, local_date)
    slots = _reset_anchored_slots(item, local_date)
    chain_id = item.get("chain_id_prefix", "") + \
        local_date.isoformat() if item.get("chain_id_prefix") else ""
    passes = []
    for idx, slot in enumerate(slots):
        unit = _unit_id_for_window(item, slot)
        label = ("first pass" if idx == 0 else "final pass") \
            if len(slots) == 2 else f"pass {idx + 1}"
        record = {"unit": unit, "label": label,
                  "slot": iso(slot.astimezone(timezone.utc)),
                  "seq": idx + 1, "location": "absent",
                  "status": "missing", "executed": False,
                  "geometry_ok": False, "finished_at": ""}
        state, path = None, None
        for cand in ("done", "claimed", "inbox"):
            cand_path = unit_path(root, cand, unit)
            if os.path.exists(cand_path):
                state, path = cand, cand_path
                break
        if state is None:
            passes.append(record)
            continue
        record["location"] = state
        fields, _ = read_unit(path)
        planned = parse_iso(fields.get("planned_for", ""))
        try:
            seq = int(fields.get("chain_seq", 0))
        except (TypeError, ValueError):
            seq = None
        record["geometry_ok"] = (
            planned is not None and
            iso(planned) == iso(slot.astimezone(timezone.utc)) and
            seq == idx + 1)
        result = fields.get("result", {})
        if not isinstance(result, dict):
            result = {}
        if state == "done":
            status = result.get("status", "")
            if not status:
                record["status"] = "done-no-result"
            else:
                record["status"] = status
                record["finished_at"] = \
                    result.get("finished_at", "") or ""
        elif state == "claimed":
            record["status"] = "claimed"
        else:
            record["status"] = "pending"
        record["executed"] = (record["status"] in ("done", "partial")
                              and record["geometry_ok"])
        passes.append(record)
    complete = bool(passes) and all(p["executed"] for p in passes)
    print(json.dumps({
        "regular": args.regular, "date": local_date.isoformat(),
        "chain_id": chain_id,
        "reset_at": iso(reset_local.astimezone(timezone.utc)),
        "passes": passes,
        "executed_passes": sum(1 for p in passes if p["executed"]),
        "total_passes": len(passes),
        "pair_complete": complete},
        ensure_ascii=False))
    return 0 if complete else 1

def cmd_cap_audit(args):
    """List every done closing over the 15-minute unit cap.

    Issue #608: the 2026-11-10 retro found 12 units in the Nov 4-10
    window over 900 seconds (local finished dates) - trucks
    2026-11-09-1857 at 1,226s, donations 2026-11-10-1343 at 1,140s
    and 10 more - hand-counted from the pool, because no tool
    listed them. This command reproduces that list mechanically:
    every done unit whose result.finished_at falls in the window
    (local dates) and whose result.duration_seconds is over
    UNIT_CAP_SECONDS. All closing statuses count - done, partial
    and failed all ran over the cap - and a done file with no
    duration or no finished_at is skipped, not counted. Exit 0
    when no closing is over the cap, 1 when any is, 2 on a bad
    date - the gate command's exit-code convention (log_append.py),
    so a retro run can gate on it.

    Read-only: it writes nothing to the pool. It resolves the
    root to the live pool (issue #598), so a copy running from a
    delivery worktree reads the live pool, not the worktree's
    stale copy.
    """
    root = live_pool_root(args.root)
    warning = pool_root_warning(root)
    if warning:
        print(warning)
    if args.end:
        try:
            year, month, day = (int(x) for x in args.end.split("-"))
            end = datetime(year, month, day).date()
        except ValueError:
            print(f"refused: --end {args.end!r} is not YYYY-MM-DD")
            return 2
    else:
        end = datetime.now(LOCAL_TZ).date()
    if args.start:
        try:
            year, month, day = (int(x) for x in args.start.split("-"))
            start = datetime(year, month, day).date()
        except ValueError:
            print(f"refused: --start {args.start!r} is not YYYY-MM-DD")
            return 2
    else:
        start = end - timedelta(days=6)
    if start > end:
        print(f"refused: --start {args.start!r} is after --end "
              f"{args.end!r}")
        return 2
    over = []
    for f in list_units(root, "done"):
        result = f.get("result", {})
        if not isinstance(result, dict):
            continue
        duration = result.get("duration_seconds")
        if not isinstance(duration, int) or \
                duration <= UNIT_CAP_SECONDS:
            continue
        finished = parse_iso(result.get("finished_at", ""))
        if finished is None:
            continue
        if not (start <= finished.astimezone(LOCAL_TZ).date() <= end):
            continue
        over.append({"unit": f.get("unit"),
                     "regular": f.get("regular"),
                     "status": result.get("status", ""),
                     "finished_at": result.get("finished_at", ""),
                     "duration_seconds": duration})
    over.sort(key=lambda e: (e["finished_at"], e["unit"]))
    print(json.dumps({
        "start": start.isoformat(), "end": end.isoformat(),
        "cap_seconds": UNIT_CAP_SECONDS,
        "over_cap_count": len(over), "over_cap": over},
        ensure_ascii=False))
    return 1 if over else 0


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


def _chain_head_refusal(root, regular, chain_id, chain_seq):
    """Refusal message when a chain head would duplicate work, or None.

    Issue #664: the 16:54 sync minted a second scout chain head
    (scout-scout-2026-11-10-001) while the plan-staged head
    (scout-2026-11-10-1800) was still claimed - the tracker still
    showed scout due mid-execution. The (regular, planned_for)
    invariant could not catch it: the staged head carries
    planned_for 2026-11-11T02:00:00Z while the enqueued head
    carries an empty planned_for, and the staged head carries no
    chain_id at all, so the literal same-chain_id check the issue
    suggests would not have caught this incident either. Two
    cases are refused loudly, scanning inbox, claimed and done:
    - the chain already has units but none carries a sequence
      number, so this mint would restart numbering at seq 1;
    - no unit carries the chain id, but a unit id starts with
      "<chain_id>-" - the plan-staged head for this chain under
      its window id (enqueue chain ids follow the
      "<regular>-<date>" convention, and plan mints
      "<regular>-<date>-<HHMM>" for the same window).
    A chain that already has numbered units is a continuation,
    not a head, and passes: successors keep minting seq N+1. A
    different chain of the same regular on the same date passes
    too - its staged units do not carry this chain id as a
    prefix (scout-discovery-2026-11-10 is not a prefix of
    scout-2026-11-10-1800), so the discovery head is not blocked
    by the base head. Limitation: a chain id that does not follow
    the "<regular>-<date>" convention (scout-midday seeds
    "scout-mid-<date>") cannot match its plan-staged head by
    prefix; renaming it to the convention would extend the guard
    to it.
    """
    same_chain = []
    namesakes = []
    prefix = chain_id + "-"
    for state in STATES:
        for f in list_units(root, state):
            if f.get("chain_id") == chain_id:
                same_chain.append((state, f.get("unit")))
            elif (f.get("unit") or "").startswith(prefix):
                namesakes.append((state, f.get("unit")))
    if same_chain and chain_seq == 1:
        detail = ", ".join(f"{u} ({s})" for s, u in same_chain)
        return (f"refused: chain {chain_id} already has units "
                f"({detail}) but none carries a sequence number - "
                f"a seq 1 unit would restart the numbering; "
                f"withdraw the unsequenced units and re-run "
                f"(issue #664)")
    if not same_chain and namesakes:
        detail = ", ".join(f"{u} ({s})" for s, u in namesakes)
        return (f"refused: chain {chain_id} already has a staged "
                f"unit under another id ({detail}) - the head is "
                f"already in the pool, so minting a second head "
                f"would duplicate it; the (regular, planned_for) "
                f"invariant cannot catch this because the new head "
                f"carries an empty planned_for (issue #664)")
    return None


def cmd_enqueue(args):
    # Live-pool production (issue #598): resolve the pool first,
    # before the wrong-root gate and before anything is read or
    # written - a unit enqueued into a delivery worktree's inbox
    # reaches only the records branch, while the next tick reads
    # the live pool. Every check below (gate, chain, sequence,
    # existence) therefore runs against the live pool, and the
    # note names the redirect so a run log shows where the unit
    # actually landed.
    root = live_pool_root(args.root)
    if root != os.path.abspath(args.root):
        print(f"note: {args.root} is a linked-worktree pool; "
              f"enqueueing into the live pool {root} (issue #598)")
    # Wrong-root gate (issue #510): a root holding no pool state
    # directory is not a pool, so refuse instead of minting an
    # inbox under it - a wrong root used to silently create a stray
    # <root>/inbox/ and report "queued" into a pool nobody reads.
    # Read commands keep the warn-only pool_root_warning convention
    # (issue #199); only this write path refuses, before anything
    # is created or written. The warning also fires here: a stray
    # pool beside the resolved _queue_ pool (issue #539) must be
    # named on the write path too, so it gets removed instead of
    # silently ignored.
    warning = pool_root_warning(root)
    if warning:
        print(warning)
    if not any(os.path.isdir(state_dir(root, s)) for s in STATES):
        print(f"refused: pool root {root} holds no inbox, "
              "claimed or done directory - the pool was not found, "
              "nothing queued (issue #510)")
        return 1
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
            for f in list_units(root, state):
                if f.get("chain_id") == args.chain_id and \
                        f.get("regular") not in ("", args.regular):
                    print(f"refused: chain {args.chain_id} belongs to "
                          f"regular {f.get('regular')}, not "
                          f"{args.regular}")
                    return 1
        chain_seq = chain_seq_next(root, args.chain_id)
        refusal = _chain_head_refusal(
            root, args.regular, args.chain_id, chain_seq)
        if refusal is not None:
            print(refusal)
            return 1
        unit = f"{args.regular}-{args.chain_id}-{chain_seq:03d}"
    else:
        unit = f"{args.regular}-{now_utc().strftime('%Y-%m-%d-%H%M')}"
    path = unit_path(root, "inbox", unit)
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
    os.makedirs(state_dir(root, "inbox"), exist_ok=True)
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
    # Live-pool handout (issue #694): the candidates, the done
    # suppression and the overlay-clearing search all read the
    # live pool, not the given root's snapshot - production,
    # token, blockers and markers already resolve there, and a
    # worktree-root next that listed the snapshot handed out
    # units already closed live while missing units minted live
    # after the snapshot. The redirect note and the pool warning
    # go to stderr, so stdout stays exactly one line: the unit
    # id, or empty.
    root = live_pool_root(args.root)
    if root != os.path.abspath(args.root):
        print(f"note: {args.root} is a linked-worktree pool; "
              f"next decides from the live pool {root} "
              f"(issue #694)", file=sys.stderr)
    warning = pool_root_warning(root)
    if warning:
        print(warning, file=sys.stderr)
    # Pool integrity (issue #441): refuse to hand out a unit from a
    # corrupt pool - a phantom id claim can never find - instead of
    # printing it and letting the pass stall at claim time. Sync
    # runs the same check first in the normal ticker flow; this
    # covers a direct next call on a pool sync never saw.
    problems = validate_pool(root)
    if problems:
        for problem in problems:
            print(problem, file=sys.stderr)
        print(f"next refused: pool invalid, {len(problems)} "
              f"problem(s) - repair the unit files and re-run "
              f"(issue #441)", file=sys.stderr)
        return 1
    stamp = now_utc()
    candidates = sorted(
        (f for f in list_units(root, "inbox")
         if _actionable(f, stamp)
         and not _has_done_record(root, f.get("unit"))
         and not has_completion_marker(root, f.get("unit"))),
        key=lambda f: pick_key(f, stamp))
    # Control-channel lock (issue #689): no unit can clear it -
    # every unit needs input - so while one stands, hand out
    # nothing. The stale bound in sync re-opens the pool for one
    # probe after BLOCKER_STALE_HOURS.
    for blocker in read_blockers(root):
        if blocker.get("kind") == "control-lock":
            print("")
            return 0
    # Screen-blocking overlay (issue #436): a recorded overlay
    # prefers the unit that clears it over every base-screen unit,
    # and pauses base-screen production while the clearing unit is
    # staged but not yet actionable - the next pass re-picks then.
    # Newest blocker first: the most recently recorded overlay is
    # the one on top of the screen.
    for blocker in read_blockers(root):
        clearing = [f for f in list_units(root, "inbox")
                    if f.get("regular") ==
                    blocker["clearing_regular"]
                    and not _has_done_record(root,
                                             f.get("unit"))
                    and not has_completion_marker(
                        root, f.get("unit"))]
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
    # Live-pool claim (issue #694): next decides from the live
    # pool, so the claim must find the unit there - a unit next
    # hands out from the live inbox is claimed from the live
    # inbox, moved into this root's claimed/ so complete and the
    # delivery still see it in the pass tree. A unit the live
    # pool holds claimed or done is refused: the snapshot copy
    # is stale, and claiming it would re-execute a unit another
    # pass already holds or closed. A unit the live pool does
    # not hold at all falls back to this root's inbox, so a unit
    # committed to the pass branch but not yet in the live
    # working tree stays claimable. On a scratch root (no git)
    # the live pool is this root, so the lookup collapses to
    # today's behaviour. The move is one atomic rename; a
    # cross-device failure refuses with nothing moved.
    live = live_pool_root(args.root)
    live_state, live_path = find_unit(live, args.unit)
    if live_state == "inbox":
        source = live_path
        if live != os.path.abspath(args.root):
            print(f"note: {args.root} is a linked-worktree pool; "
                  f"claiming the live-pool unit into {args.root} "
                  f"(issue #694)")
    elif live_state in ("claimed", "done"):
        print(f"cannot claim {args.unit}: state is {live_state} "
              f"in the live pool - the inbox copy is stale, run "
              f"sync to drop it instead of re-executing it")
        return 1
    else:
        state, path = find_unit(args.root, args.unit)
        if state != "inbox":
            print(f"cannot claim {args.unit}: state is {state}")
            return 1
        source = path
    if _has_done_record(live, args.unit) or \
            _has_done_record(args.root, args.unit):
        print(f"cannot claim {args.unit}: already has a done "
              f"record - the inbox copy is stale, run sync to "
              f"drop it instead of re-executing it")
        return 1
    if has_completion_marker(args.root, args.unit):
        print(f"cannot claim {args.unit}: already closed in "
              f"another worktree - the inbox copy is stale, run "
              f"sync to drop it instead of re-executing it")
        return 1
    fields, body = read_unit(source)
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
    try:
        os.rename(source, target)                # atomic claim
    except OSError as exc:
        print(f"cannot claim {args.unit}: cannot move {source} "
              f"to {target}: {exc}")
        return 1
    # A snapshot copy of a live-claimed unit is a stale
    # duplicate: drop it so the delivery cannot re-add the unit
    # to the committed inbox as pending. A failure here only
    # warns - the claim already landed, and sync's branch
    # reconciliation drops the stale copy once the done record
    # lands (issue #446).
    if live_state == "inbox" and \
            live != os.path.abspath(args.root):
        stale = unit_path(args.root, "inbox", args.unit)
        if os.path.exists(stale):
            try:
                os.remove(stale)
            except OSError as exc:
                print(f"warning: cannot drop stale snapshot "
                      f"copy {stale}: {exc}", file=sys.stderr)
    write_unit(target, fields, body)
    print(f"claimed {args.unit} by {args.executor} "
          f"until {fields['lease_until']}")
    return 0


def _parse_closes_in(text):
    """Seconds from a banner countdown: an integer, or HH:MM:SS."""
    try:
        seconds = int(text)
    except (TypeError, ValueError):
        parts = (text or "").split(":")
        if len(parts) != 3:
            return None
        try:
            hours, minutes, seconds = (int(p) for p in parts)
        except ValueError:
            return None
        seconds = hours * 3600 + minutes * 60 + seconds
    return seconds if seconds > 0 else None


def cmd_deadline(args):
    # Real deadlines (issue #623): a unit's slot expiry is not
    # always its true deadline - a train unit staged to its slot
    # end is picked by that expiry, so a boarding closing in
    # minutes is invisible to next and the pass hands out other
    # work while the boarding closes. The executor stamps the
    # boarding close when the banner shows it (countdown from
    # the banner, or an absolute close), and next returns the
    # train first. Only tightens: a deadline at or after the
    # current expiry, a past deadline, and any unit not in
    # inbox are refused, so a stamp can never widen a window
    # or resurrect a closing. Re-stamping the same value is a
    # no-op success, so a banner re-read is idempotent. The
    # stamp is recorded in the unit body, and sync never
    # rewrites it: production skips a (regular, planned_for)
    # pair that already exists instead of re-minting it, and
    # the aged priority-1 windowing only touches units with no
    # planned_for, which a staged train unit always has.
    root = live_pool_root(args.root)
    if root != os.path.abspath(args.root):
        print(f"note: {args.root} is a linked-worktree pool; "
              f"stamping into the live pool {root} (issue #598)")
    warning = pool_root_warning(root)
    if warning:
        print(warning)
    if not any(os.path.isdir(state_dir(root, s)) for s in STATES):
        print(f"refused: pool root {root} holds no inbox, "
              "claimed or done directory - the pool was not found, "
              "nothing stamped (issue #510)")
        return 1
    if args.expires_at and args.closes_in:
        print("refused: pass exactly one of --expires-at and "
              "--closes-in")
        return 1
    stamp = now_utc()
    if args.expires_at:
        deadline = parse_iso(args.expires_at)
        if deadline is None:
            print(f"refused: --expires-at {args.expires_at!r} is not "
                  "a UTC timestamp YYYY-MM-DDTHH:MM:SSZ")
            return 1
    elif args.closes_in:
        seconds = _parse_closes_in(args.closes_in)
        if seconds is None:
            print(f"refused: --closes-in {args.closes_in!r} is not "
                  "seconds or HH:MM:SS")
            return 1
        deadline = stamp + timedelta(seconds=seconds)
    else:
        print("refused: pass --expires-at or --closes-in")
        return 1
    if deadline <= stamp:
        print(f"refused: deadline {iso(deadline)} is not in the "
              "future - the boarding already closed, let reap "
              "expire the unit instead of stamping a dead deadline")
        return 1
    state, path = find_unit(root, args.unit)
    if state != "inbox":
        print(f"cannot stamp {args.unit}: state is {state}")
        return 1
    if _has_done_record(root, args.unit):
        print(f"cannot stamp {args.unit}: already has a done "
              f"record - the inbox copy is stale, run sync to "
              f"drop it instead of stamping it")
        return 1
    if has_completion_marker(root, args.unit):
        print(f"cannot stamp {args.unit}: already closed in "
              f"another worktree - the inbox copy is stale, run "
              f"sync to drop it instead of stamping it")
        return 1
    fields, body = read_unit(path)
    current = parse_iso(fields.get("expires_at", ""))
    if current is not None and deadline >= current:
        if deadline == current:
            print(f"already stamped: {args.unit} expires_at is "
                  f"already {iso(current)}")
            return 0
        print(f"refused: deadline {iso(deadline)} is not earlier "
              f"than the current expiry {iso(current)} - deadline "
              "only tightens, it never widens a window")
        return 1
    old_expires = fields.get("expires_at", "")
    old_priority = fields.get("priority", 3)
    fields["expires_at"] = iso(deadline)
    if args.priority is not None:
        fields["priority"] = args.priority
    reason = args.reason or "no reason given"
    note = (f"Deadline stamped {iso(deadline)} from "
            f"{old_expires or 'no expiry'} ({reason}).")
    body = (body or "").rstrip("\n") + "\n\n" + note + "\n"
    write_unit(path, fields, body)
    rank = None
    total = 0
    for f in sorted(
            (f for f in list_units(root, "inbox")
             if _actionable(f, stamp)
             and not _has_done_record(root, f.get("unit"))
             and not has_completion_marker(root, f.get("unit"))),
            key=lambda f: pick_key(f, stamp)):
        total += 1
        if f.get("unit") == args.unit and rank is None:
            rank = total
    print(f"deadline {args.unit}: expires_at "
          f"{old_expires or '-'} -> {iso(deadline)}"
          + (f", priority {old_priority} -> {args.priority}"
             if args.priority is not None else "")
          + (f", pick rank {rank} of {total} actionable inbox units"
             if rank is not None
             else ", not actionable yet (not_before in the future)"))
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


def points_duplicates_achieved_string(stats, regular=None):
    """True when stats.points copies a total named in a string achieved (issue #672).

    points is score gained in this unit, not a running total
    read: a duel total read belongs in achieved only. The
    equality detector cannot see the copy when achieved is a
    descriptive string instead of a number - _stat_number
    returns None for the string, so the comparison never
    fires - and the no-achieved detector cannot fire either,
    because the achieved key is present. The #672 variant is
    that hole: duel-score-2026-11-10-2230 wrote points
    1650000 beside achieved "personal total 1650000 read
    live, gap 1950000", and the retro summed 1,653,678 as
    points gained against an honest 3,678. This detector
    compares points against every number named in the
    achieved string; a match means points is the running
    total named there, not score gained in the unit.

    A string achieved that names no number equal to points
    stays counted: daily-missions 2026-10-31-1900 carries
    achieved "all-claimable-claimed" with points 40 - the
    genuine 110-to-150 activity gain in its summary - and a
    string naming only a different figure (a gap, a
    before/after read) is not a copy either. Comma-grouped
    totals ("1,650,000") match the same way. Radar is exempt,
    mirroring points_duplicates_achieved. Zero points is not
    flagged: a unit that gained nothing is not a total copy.
    This is a warning, never a block.
    """
    if not isinstance(stats, dict):
        return False
    if regular == "radar":
        return False
    points = _stat_number(stats.get("points"))
    if points is None or points == 0:
        return False
    achieved = stats.get("achieved")
    if not isinstance(achieved, str):
        return False
    if _stat_number(achieved) is not None:
        return False
    for token in re.findall(r"[\d,]+(?:\.\d+)?", achieved):
        try:
            number = float(token.replace(",", ""))
        except ValueError:
            continue
        if number == points:
            return True
    return False


def points_is_progress_delta(stats, regular=None):
    """True when stats.points is a progress-bar delta on a gifts unit (issue #300).

    points is score gained in this unit, for scoring types only
    (task-unit-queue-design.md per-unit measurement table: duel,
    Arms Race, radar). Gifts is not a scoring type - gifts pay
    no score, they feed the alliance Gift Level progress bar,
    and the profile measures them in progress-bar points
    (per-gift points, Claim All points re-grounded). A points
    figure on a gifts closing is therefore the progress-bar
    delta by construction, not a unit score: the only two gifts
    closings ever to carry points both equal the progress delta
    named in their own summaries - gifts-2026-11-09-0230 wrote
    points 1090 against "Gift Level 28 progress 195,637,370
    to 195,638,460" (delta 1,090) and gifts-2026-11-09-1430
    wrote points 46760 against "Gift Level 28 progress
    +46,760" - while their achieved is a claim count (39 and
    1794), so neither the equality detector nor the
    no-achieved detector fires. The retro summed 47,850 as
    points gained; its honest window total is 2,463. This is
    a warning, never a block, and it is scoped to gifts only:
    the genuine non-equal gains stay counted - arms-race
    2026-11-09-1003 points 2000 against achieved 8000 (a
    rally kill, distinct from the phase total), donations
    points 50, daily-missions points 100.
    """
    if not isinstance(stats, dict):
        return False
    if regular != "gifts":
        return False
    points = _stat_number(stats.get("points"))
    return points is not None and points != 0


def points_is_expected_score(stats, regular=None):
    """True when stats.points is a Handbook-rate expected score on a trucks unit (issue #300).

    points is score gained in this unit, for scoring types only
    (task-unit-queue-design.md per-unit measurement table: duel,
    Arms Race, radar). Trucks is not a scoring type - a trucks
    unit never reads the VS panel; duel-score reads belong to
    the duel-score regular, which verifies the gain live. A
    points figure on a trucks closing is therefore a
    Handbook-rate expected score by construction, not a unit
    score: trucks-2026-11-09-2257 wrote points 400000 (4 times
    the 100,000 Handbook rate from tools/duel.py), labeled in
    its own record "expected duel points, Handbook rate,
    pending live verification by the duel-score unit", while
    its achieved is a dispatch/plunder count ("dispatch 4,
    plunder 1"), so neither the equality detector nor the
    no-achieved detector fires. The Nov 10 retro window summed
    403,592 as points gained against an honest 3,592. This is
    a warning, never a block, and it is scoped to trucks only:
    the genuine non-equal gains stay counted - arms-race
    2026-11-09-1003 points 2000 against achieved 8000 (a
    rally kill, distinct from the phase total), donations
    points 50, daily-missions points 100. The trucks profile
    already carries the prevention rule (retro action
    A-2026-11-10-01: never write an expected or Handbook-rate
    score into stats.points); this is the detector half.
    """
    if not isinstance(stats, dict):
        return False
    if regular != "trucks":
        return False
    points = _stat_number(stats.get("points"))
    return points is not None and points != 0


def achieved_is_screen_total(stats, regular=None):
    """True when stats.achieved is a screen total on a star-ceremony unit (issue #483).

    achieved is the unit's own gain against its target, not a running
    total read off another screen: a duel total read belongs to the
    duel-score regular, which carries the duel target 3600000 by
    design (issue #136). Star-ceremony is not a scoring type - its
    target is 1 (one ceremony check) and its achieved is the ceremony
    count, 0 or 1. The two closings that wrote a duel total into
    achieved both carry the duel target 3600000 with 0 ceremonies
    claimed: star-ceremony-2026-11-01-1830 wrote achieved 791250
    ("personal duel total read live 791250 vs target 3600000, gap
    2808750") and star-ceremony-2026-11-04-0630 wrote achieved
    4772100 ("duel total 4772100 vs target 3600000, exceeded by
    1172100"). The Nov 4 unit alone carried the window attainment
    from about 0.093 to 1.1907 (achieved_sum 4813220 against
    target_sum 4042308; without it, achieved 41120). A
    star-ceremony closing whose target is not the ceremony count
    (1) and whose achieved is above 1 therefore carries another
    regular's target/achieved pair by construction. The target
    check keeps a future target-1 closing honest: a ceremony
    count of 2 or more under target 1 is not excluded here.
    This is a warning, never a block.
    """
    if not isinstance(stats, dict):
        return False
    if regular != "star-ceremony":
        return False
    target = _stat_number(stats.get("target"))
    achieved = _stat_number(stats.get("achieved"))
    return (target is not None and achieved is not None
            and target != 1 and achieved > 1)


def blocker_category_not_enum(stats):
    """True when stats.blocker_category is present but not an audit class (issue #130).

    blocker_category is the miss-audit root-cause class, one
    letter a to i (task-unit-queue-design.md per-unit
    measurement table). The 2026-11-09 retro found non-enum
    values persisting in the pool - access-failed, time,
    timer, unverified-close - and named the queue tool
    validation that would enforce the enum as the standing
    gap behind #130; the main-tree pool snapshot carries the
    same family plus none and contested. Acceptance mirrors
    retro_report.py _blocker_class: a single letter, or a
    letter followed by a space, hyphen or colon (so "e -
    repeated blocker" still reads as e). Absence is not
    flagged here - missing_stats_keys owns that. This is a
    warning, never a block.
    """
    if not isinstance(stats, dict):
        return False
    if "blocker_category" not in stats:
        return False
    raw = stats.get("blocker_category")
    if not isinstance(raw, str):
        return True
    text = raw.strip().lower()
    if not text:
        return True
    return not (text[0] in BLOCKER_CATEGORIES
                and (len(text) == 1 or text[1] in " -:"))


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
    points_str_ach = points_duplicates_achieved_string(
        stats, fields.get("regular"))
    points_prog = points_is_progress_delta(stats, fields.get("regular"))
    points_exp = points_is_expected_score(stats, fields.get("regular"))
    achieved_screen = achieved_is_screen_total(stats, fields.get("regular"))
    blocker_bad = blocker_category_not_enum(stats)
    over_cap = isinstance(duration, int) and \
        duration > UNIT_CAP_SECONDS
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
                              if points_noach else [])
                           + (["points duplicates achieved in string"]
                              if points_str_ach else [])
                           + (["points is progress delta"]
                              if points_prog else [])
                           + (["points is expected score"]
                              if points_exp else [])
                           + (["achieved is screen total"]
                              if achieved_screen else [])
                           + (["blocker_category not in enum a-i"]
                              if blocker_bad else [])
                           + (["duration exceeds 15-minute unit cap"]
                              if over_cap else [])),
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
                if overlay == CONTROL_LOCK_SLUG:
                    blocker_note = (f"blocker recorded: control "
                                    f"channel locked "
                                    f"(outcome_unknown) - next "
                                    f"hands out nothing until the "
                                    f"blocker ages out "
                                    f"({BLOCKER_STALE_HOURS}h) or "
                                    f"input succeeds")
                else:
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
    # Control-channel lock (issue #689): a closing that sent input
    # proves the channel is back, so done / partial /
    # skipped-needs-owner without naming the lock lifts it. A
    # failed closing proves nothing either way and leaves the
    # blocker standing; the stale bound re-opens the pool for
    # one probe after BLOCKER_STALE_HOURS.
    if args.status in ("done", "partial", "skipped-needs-owner") \
            and overlay != CONTROL_LOCK_SLUG:
        for blocker in read_blockers(args.root):
            if blocker.get("kind") == "control-lock":
                if clear_blocker(args.root, blocker["overlay"]):
                    blocker_note = (f"blocker cleared: control "
                                    f"channel lock lifted by "
                                    f"{args.unit} (input flowed)")
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
    if points_str_ach:
        print(f"warning: {args.unit} closes with stats.points "
              f"equal to a total named in its string "
              f"stats.achieved - points is score gained in "
              f"this unit, not a running total read; a duel "
              f"total read belongs in achieved only")
    if points_prog:
        print(f"warning: {args.unit} closes with stats.points "
              f"on a gifts unit - points is score gained in "
              f"this unit and gifts pay no score; the Gift "
              f"Level progress gain belongs in the summary and "
              f"resources_gained only")
    if points_exp:
        print(f"warning: {args.unit} closes with stats.points "
              f"on a trucks unit - points is score gained in "
              f"this unit and trucks pay no live-read score; a "
              f"Handbook-rate expected score belongs in the "
              f"summary only, verified live by the duel-score unit")
    if over_cap:
        print(f"warning: {args.unit} ran {duration}s, over the "
              f"{UNIT_CAP_MINUTES}-minute unit cap - split the "
              f"task next time so a unit stays inside one pass")
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


def live_pool_root(root):
    """Live pool for a root that may sit in a linked worktree.

    New units are live pool state: the next tick's `next` reads
    the live pool's inbox, never a records branch's, so a unit
    enqueued into a delivery worktree's inbox is stranded - it
    reaches only the records branch (issue #598: ticker-1806
    seeded the zombie chain head into the records branch inbox
    and the live pool never saw it). The token, blockers and
    completion markers already resolve to the main checkout
    through _shared_token_home (issues #383, #438); production
    does the same, so enqueue and the sync / plan / sweep
    production path always mint into the main checkout's _queue_
    when this copy runs from a linked worktree. A root that is
    not in a repo (tests, scratch dirs) or whose main checkout
    holds no _queue_ keeps the given root, and the main checkout
    itself resolves to itself.
    """
    shared = _shared_token_home(root)
    if shared is not None:
        return shared
    return os.path.abspath(root)


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
    skipped, so a half-written record can never pause the pool -
    except a control-lock blocker (issue #689), which carries a
    kind row and no clearing regular by design. The most recently
    recorded overlay is the one on top of the screen, so
    newest-first is also the clearing order.
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
        kind = fields.get("kind", "overlay")
        if not overlay:
            continue
        if not clearing and kind != "control-lock":
            continue
        recorded = parse_iso(fields.get("recorded_at", ""))
        out.append({"overlay": overlay,
                    "clearing_regular": clearing,
                    "kind": kind,
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
    with no known clearing unit cannot be acted on). The
    control-lock slug (issue #689) is the exception: it has no
    clearing regular by design, so it records a kind row instead
    and returns the slug itself.
    """
    if overlay == CONTROL_LOCK_SLUG:
        home = blocker_home(root)
        folder = os.path.join(home, BLOCKER_DIRNAME)
        os.makedirs(folder, exist_ok=True)
        lines = ["---",
                 f"overlay: {overlay}",
                 "kind: control-lock",
                 f"recorded_at: {iso(now_utc())}",
                 f"recorded_by: {recorded_by or ''}",
                 "---", ""]
        with open(os.path.join(folder, overlay + ".md"),
                  "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines))
        return CONTROL_LOCK_SLUG
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
    directory from holding a blocker no pass can ever clear. A
    control-lock blocker (issue #689) has no clearing regular:
    the same bound is its wait-and-retry rule, so it is stale
    once it is over BLOCKER_STALE_HOURS old and the next tick
    probes with one input.
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
        if blocker.get("kind") == "control-lock":
            if recorded is not None and \
                    (stamp - recorded).total_seconds() <= \
                    BLOCKER_STALE_HOURS * 3600:
                continue
            if clear_blocker(root, blocker["overlay"]):
                dropped.append(blocker["overlay"])
            continue
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
    is dropped too. Returns a dict with the unit ids dropped
    ("reaped") and, separately, the dropped ids whose closing was
    lost (issue #563): a valid marker older than
    COMPLETED_STALE_HOURS with no local done record - the
    delivery never carried that closing, so the retro can triage
    each named unit instead of counting one more bare integer.
    """
    home = completion_home(root)
    folder = os.path.join(home, COMPLETED_DIRNAME)
    if not os.path.isdir(folder):
        return {"reaped": [], "lost": []}
    stamp = now_utc()
    dropped = []
    lost = []
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
        aged_out = False
        if valid:
            if _has_done_record(root, unit):
                keep = False
            elif finished is not None and \
                    (stamp - finished).total_seconds() > \
                    COMPLETED_STALE_HOURS * 3600:
                keep = False
                aged_out = True
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
        if aged_out:
            lost.append(unit)
    return {"reaped": dropped, "lost": lost}


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
            # Issue #461: a re-acquire by the holder itself always
            # renews the lease instead of reporting held - the
            # 2026-11-08 rule renewed only within 60 seconds of
            # expiry, but the executor loop re-acquires at every
            # unit boundary, so a re-acquire after a short unit
            # lands minutes before expiry and was refused, and the
            # holder's game input then ran with no token. A
            # different executor is still refused while the lease
            # is live, so the mutual-exclusion guarantee is
            # unchanged.
            if fields.get("claimed_by") == args.executor:
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
              "stats_points_dup_string": 0,
              "stats_points_dup_string_units": [],
              "stats_blocker_not_enum": 0,
              "stats_blocker_not_enum_units": [],
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
                if points_duplicates_achieved_string(
                        dup_stats if isinstance(dup_stats, dict)
                        else {}, regular):
                    report["stats_points_dup_string"] += 1
                    report["stats_points_dup_string_units"].append(
                        f.get("unit"))
                if blocker_category_not_enum(
                        dup_stats if isinstance(dup_stats, dict)
                        else {}):
                    report["stats_blocker_not_enum"] += 1
                    report["stats_blocker_not_enum_units"].append(
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
        print(f"  stats_points_dup_string: "
              f"{report['stats_points_dup_string']}")
        print("  stats_points_dup_string_units: "
              f"[{', '.join(report['stats_points_dup_string_units'])}]")
        print(f"  stats_blocker_not_enum: "
              f"{report['stats_blocker_not_enum']}")
        print("  stats_blocker_not_enum_units: "
              f"[{', '.join(report['stats_blocker_not_enum_units'])}]")
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
        if report["stats_points_dup_string"]:
            print(f"  stats points duplicates achieved in string: "
                  f"{report['stats_points_dup_string']} "
                  f"({', '.join(report['stats_points_dup_string_units'])})")
        if report["stats_blocker_not_enum"]:
            print(f"  stats blocker_category not in enum: "
                  f"{report['stats_blocker_not_enum']} "
                  f"({', '.join(report['stats_blocker_not_enum_units'])})")
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
    p.add_argument("--ref", default="")
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

    p = sub.add_parser("deadline")
    p.add_argument("--unit", required=True)
    p.add_argument("--expires-at", default="")
    p.add_argument("--closes-in", default="")
    p.add_argument("--priority", type=int, default=None)
    p.add_argument("--reason", default="")
    p.set_defaults(fn=cmd_deadline)

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

    p = sub.add_parser("sweep-status")
    p.add_argument("--regular", default="zero-sweep")
    p.add_argument("--date", default="")
    p.add_argument("--regulars-json", default="")
    p.set_defaults(fn=cmd_sweep_status)

    p = sub.add_parser("cap-audit")
    p.add_argument("--start", default="")
    p.add_argument("--end", default="")
    p.set_defaults(fn=cmd_cap_audit)

    p = sub.add_parser("stats")
    p.add_argument("--format", choices=["text", "yaml", "json"],
                   default="text")
    p.set_defaults(fn=cmd_stats)

    args = parser.parse_args(argv)
    args.root = resolve_pool_root(os.path.abspath(args.root))
    if args.cmd in TOOL_GUARDED_COMMANDS:
        refusal = refuse_if_tmp_worktree(args.cmd, args.root)
        if refusal is not None:
            return refusal
        refusal = refuse_if_tool_stale(args.cmd)
        if refusal is not None:
            return refusal
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
