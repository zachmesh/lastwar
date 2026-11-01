---
title: Task Unit Queue Design
created: 2026-10-28T10:22:00Z
modified: 2026-11-01T05:00:00Z
version: 0.7.0
description: Run the routine as short task units drawn from a file queue instead of long segment runs - implemented 2026-10-28
status: implemented
grounded_in:
  - source: owner request 2026-10-28 to design a task unit pool with short bounded executions
  - source: run records of 2026-10-27 and 2026-10-28 in _records_
  - source: miss audit of 2026-10-31 and the owner instruction of 2026-10-31 to reflect and fix
---

# Task unit queue design

Status - implemented 2026-10-28 on the owner's direction. The ticker
`lastwar-queue-ticker` is live, the three segment schedules and the
Zombie Invasion rounds schedule are deleted (definitions backed up
under the goal backup folder, cutover-2026-10-28), and execution runs
on the queue. Section 9 records the validation evidence.

## 1. Problem

The 3 segment schedules work, but each segment run is one long subagent
session, and the evidence of 2026-10-27 and 2026-10-28 shows the cost.

- Segment runs take 37 to 50 minutes of wall time (segment 1 of
  2026-10-27 22:03 finished at 22:40, segment 3 of 18:57 at about
  19:46). One window, one game - the whole routine serializes behind
  whichever run is active.
- Segment 2 of 2026-10-28 02:30 found a separate owner-directed Zombie
  Invasion session controlling the same Mac window and had to stand
  down, deferring mail, gifts, VIP, train and star-ceremony to the next
  cycle. Contention is handled by surrender, not by queueing.
- Expiring work has no way to jump the queue. On 2026-10-27 the owner
  had to ask manually at 18:43 because a free shop pack and the VIP
  freebie were about to lapse at the 19:00 reset while the long runs
  were still blocked or busy.
- A dead executor strands its work. The outcome_unknown control lock of
  2026-10-26 to 2026-10-27 froze 18 consecutive segment runs; inside a
  long run, a mid-run death loses the whole segment, not one item.

## 2. Concepts

- **Task unit** - one regular from `tools/regulars.json`, sized to
  finish in a few minutes. A unit is a Markdown file whose frontmatter
  is one structured YAML document describing the task, its queue state
  and, once executed, its result and result statistics (sections 4
  and 5). The prose body is instructions for the executor; tools read
  only the YAML. Units are the only thing executors run.
- **One unit, one task type** - owner rule of 2026-10-28. A unit
  names exactly one regular and one activity, an executor never
  merges two types into one unit or one result, and a chain is
  homogeneous - every unit in it shares the same regular (the queue
  tool refuses to extend a chain with a different regular). Work
  that belongs to another type, even when a screen flow touches it
  on the way, is executed and counted under that type's own unit.
  This is what keeps the per-type statistics - durations, failures,
  late finishes - clean enough to judge execution quality by type.
- **Pool** - the `_queue_` type folder with three state subfolders.
  `inbox` holds pending units, `claimed` holds units under execution,
  `done` holds finished units. Moving a file is the state transition.
- **Producer** - a short job that reads the due list from
  `tools/regulars.py` and writes one unit file per due regular into
  `inbox`. It never touches the device.
- **Executor loop** - the main agent's standing job under this
  design. It keeps executing where work is needed - take the device
  token, pick the best unit, run it, write its result, pick the next
  one. The loop is driven by one periodic ticker (section 6), not by
  the three segment schedules, which this design retires.
- **The 15 minute unit** - owner rule of 2026-10-28 - **each unit
  runs at most 15 minutes**. The unit is the scheduling quantum -
  when a unit ends, the loop re-reads the pool, so work that became
  due or urgent in the meantime is picked up at the next boundary,
  at most 15 minutes later. A task that cannot fit in 15 minutes is
  split into units at intake, never stretched.
- **Continuation chain** - a long activity is a chain of units under
  one `chain_id`. Each finished unit reports in its result stats
  whether the activity is exhausted; if not, the next unit of the
  chain is enqueued and the activity keeps going across as many
  quanta as it needs. Zombie Invasion is the model case - it runs
  until the nearby zombies are cleared, unit after unit, under its
  standing stop rules (for Zombie Invasion there is no hour
  budget and no daily limit - when the nearby zombies are cleared
  the chain pauses 1 hour and then checks again, owner correction
  2026-10-28), while higher priority units slip in between its
  units whenever their time arrives.
- **Device token** - exactly one executor may hold the Mac window at
  a time, for one unit at a time. The token is itself a lease file
  in `claimed`; taking the game window without the token is out of
  bounds for every session, including owner-directed ad hoc
  sessions, which join the pool as units instead of colliding.

## 3. Pool layout

```text
_queue_/
  INDEX.md          - the type index, points here
  unit-template.md  - the unit file template
  inbox/            - pending units, one file per unit
  claimed/          - units under execution, plus the device token
  done/             - finished units with their result blocks
```

Unit file names are `<unit-id>.md` where the id is
`<regular-id>-<cycle>` and cycle is the local date and hour of the
producing cycle, for example `vip-2026-10-28-1900.md`. Names stay
unique across days without a central counter.

## 4. Unit schema

The unit frontmatter is the single structured source for the unit -
what the task is, where it is (the state subfolder plus the claim
fields below), and what it produced (the result section in section
5). Status, statistics and reports are gathered from these fields by
`tools/queue.py stats`, never by scraping prose. Values are kept
colon-free except timestamps, as elsewhere in this repository.

| Field | Meaning |
|---|---|
| `unit` | unit id, matches the file name |
| `regular` | regular id from tools/regulars.json |
| `activity` | activity type folder name for the run record |
| `segment` | owning segment under the current routine, kept for reporting |
| `priority` | 1 expiry-critical, 2 windowed, 3 standard, 4 background |
| `created_at` | when the producer wrote the unit |
| `expires_at` | after this the unit is worthless or degraded (reset, phase end); empty when none |
| `planned_for` | the cadence window (time slot) this unit serves; with `regular` it is the unit's identity |
| `not_before` | the unit may not be claimed before this time; set to the window start for future windows |
| `window` | execution window constraint, for example an Arms Race phase or a duel posture; empty when none |
| `est_minutes` | typical minutes for this task type, learned per section 5; enqueue rejects anything above the 15 minute cap |
| `chain_id` | continuation chain this unit belongs to; empty for one-off units |
| `chain_seq` | position inside the chain, 1 based |
| `attempts` | how many times the unit has been claimed |
| `max_attempts` | claims allowed before the unit dead-letters as failed (default 3) |
| `claimed_by` | executor name once claimed |
| `claimed_at` | claim time |
| `lease_until` | claim expiry; past it the unit returns to inbox |

Priority classes from the current regulars.

- **1 expiry-critical** - vip (expires at the 19:00 reset), passes when
  a free pack carries its own countdown, events on a check-in day
  boundary.
- **2 windowed** - arms-race (points only count inside the live phase),
  radar on release days (claims score at claim time), donations before
  the daily settlement, trucks on a duel UR day.
- **3 standard** - everything else.
- **4 background** - continuation chains that soak up idle quanta
  and always yield at the next boundary (Zombie Invasion units).

## 5. Result and result statistics

On completion the executor writes a `result` mapping into the same
frontmatter (via `tools/queue.py complete`) and the unit moves to
`done`. A completed unit therefore carries its whole life in one
structured document - task, claim, result and statistics.

```yaml
result:
  status: done            # done, partial, failed, skipped-needs-owner
  started_at: 2026-10-28T10:30:00Z
  finished_at: 2026-10-28T10:34:00Z
  duration_seconds: 240
  executor: executor-1
  summary: Claimed the Daily Freebie and the login points
  claimed: [daily-freebie, login-200]
  claimed_count: 2
  evidence: _records_/2026-10-28/vip-rewards/1030-queue-run.md
  follow_up: none
  stats:
    points_gained: 200
```

Core result fields are fixed (status, times, duration, executor,
claimed list and count, evidence, follow-up). The `stats` mapping is
open - each activity defines its own keys in its `_activities_`
metadata (points gained, chests claimed, donations made, trucks
dispatched), and executors pass them as key values at completion.

**Learned estimates** - owner direction 2026-10-28. A task type's
typical execution time is estimated from the pool itself - the
median `duration_seconds` of its completed units, in minutes rounded
up and clamped to the cap, once at least 3 completed samples exist;
the static production defaults apply before that. `sync` stamps
each new unit with the current learned estimate, and the stats
report shows it next to the sample count, so a type whose typical
time creeps toward the 15 minute cap is visible and gets split at
intake instead of silently overrunning.
Because the keys are structured, `tools/queue.py stats` aggregates
reliably across the whole pool - counts by state and by regular,
result status totals, duration averages and maxima, units finished
after their expiry, units expired while waiting, and claims past
their lease - in text, YAML or JSON.

The matching `_records_` execution file is still written as today
(C1 append-only audit); the unit references it under `evidence`.

## 6. The ticker and the executor loop

One scheduled job drives everything - the **ticker**, firing every
30 minutes (owner direction 2026-10-28). The three segment
schedules are gone; there is nothing else to coordinate. Each tick
runs four steps.

1. **Reap** - return units whose leases expired to `inbox` (or
   dead-letter them when their attempts are spent).
2. **Produce** - ask the tracker what is due and enqueue one unit
   per due regular, idempotently, so a regular already queued or
   running is never duplicated. Chain continuations are enqueued at
   completion time by the executor (step 4 below); the producer
   only seeds a chain's first unit and tops up chains whose next
   unit is missing.
3. **Execute** - run the executor loop below until no due unit
   remains or the pass budget runs out (proposed 25 minutes,
   inside the 30 minute interval). Partial units requeue safely,
   so stopping mid-drain loses nothing.
4. **Skip** - when nothing was enqueued and nothing executed, the
   tick exits silently. An empty tick costs one tracker call.

Overlap is expected and harmless - a pass still executing when the
next tick fires holds the device token, and the new tick sees the
token held and skips its execute step. Only one pass ever plays.

Latency is bounded and measurable - a fresh unit waits at most one
tick interval plus the remainder of the unit currently running
(itself capped at 15 minutes). Expiry-critical work is protected by
construction - the producer enqueues it ahead of its deadline
(reset and phase times are known in advance) and the loop picks
earliest expiry first. The stats report's `late` list is the
feedback signal - if units start finishing late, the interval
shortens to 15 minutes; the mechanism does not change.

The executor loop itself, run by the main agent inside the tick's
execute step, and equally by any owner-directed session that takes
the token.

1. Take the device token. No token, no game input - whoever holds
   it finishes their unit first (at most 15 minutes). Contention
   becomes a short wait, never a collision or a stand-down.
2. Pick the inbox unit with the earliest `expires_at`, ties broken
   by priority then by age. Claim it by atomic rename `inbox` to
   `claimed`, stamping `claimed_by`, `claimed_at`, `lease_until`
   (default lease 20 minutes - longer than the unit cap, so a unit
   is never requeued out from under a live executor) and
   incrementing `attempts`.
3. Run the unit, at most 15 minutes. On time, finish the current
   atomic in-game action, write the `_records_` file, and complete
   the unit with a `partial` result noting the remaining work. The
   partial unit is an attempt record in `done`; the tracker still
   shows the regular as due, so the next tick re-produces it and
   the work resumes as a fresh unit - and the attempt stays in the
   statistics instead of vanishing.
4. On completion, write the `_records_` file, complete the unit
   (the result section lands in its frontmatter), rename `claimed`
   to `done`, and update the regulars tracker exactly as segment
   runs do today. If the unit belongs to a chain and its result
   stats say the activity is not exhausted, enqueue the next unit
   of the chain. A chain ends only when its activity ends. For
   Zombie Invasion a unit whose stats say cleared does not end
   the chain - its successor is enqueued with `not_before` 1 hour
   later, because new zombies may appear (waves arrive about
   hourly); there is no daily limit and no hour budget (owner
   correction 2026-10-28).
5. Release the token and go back to step 1. Every unit boundary is
   a scheduling point - a VIP unit that lands while a background
   chain is mid-run waits at most for the current unit to end.
6. A reaper pass (part of the producer job) returns any `claimed`
   unit whose `lease_until` has passed to `inbox`, clearing the
   claim stamps. A crashed executor therefore strands at most one
   unit for at most one lease period - the direct fix for the
   2026-10-26 lock failure mode at the work level.
7. Dead letters - a unit whose `attempts` reach `max_attempts` is
   not requeued again. It moves to `done` with result status
   `failed`, and the stats report surfaces it, so a poison unit
   cannot spin the loop forever.

All steps are idempotent at the unit level - before acting, the
executor checks the game state the unit acts on (the standing
check-first rule), so a re-executed unit does not double-claim.

One honest limit - the loop runs inside the ticker's passes, not
as a literal daemon; between ticks the pool simply waits in
`inbox`. The unit cap is what makes that safe - no pass can be
captured by one task for longer than 15 minutes, and no unit can
starve the pool behind a long task the way the segment runs did.

## 7. The planner - a 12 hour horizon

Production has two layers (owner direction 2026-10-28).

- **The planner** (`lastwar-queue-planner`, every 4 hours) is the
  primary producer. Each run stages the next 12 hours of work -
  one unit per (regular, time slot): every-run regulars at every
  4 hour boundary inside the horizon, the daily-reset regular at
  its reset, the Thursday regular on Thursdays. Future units carry
  `planned_for` (their slot) and `not_before` (the slot start);
  the executor's pick and claim both refuse a unit before its
  time, so staged work waits in the pool until its slot arrives.
- **No duplication** means exactly this - the same unit for the
  same time slot is never added twice. The (regular, planned_for)
  pair is the invariant, enforced in one shared production path:
  if a unit with that pair exists in inbox, claimed or done, no
  producer adds another. A regular the tracker already counts as
  done for the current slot gets no phantom unit either - the
  planner checks the tracker before staging the current slot.
- **The ticker's sync** is the safety net under the planner - it
  produces the current slot's unit for anything the tracker marks
  due (work that appeared between planner runs, manual tracker
  changes), through the same invariant, so the two producers can
  never double-stage.
- A unit whose slot has fully passed unexecuted is expired into
  `done` with status `expired` by the next reap - the following
  slot's unit supersedes it, and the miss stays visible in the
  statistics. Chains are not planned; they are seeded and
  continued by the ticker as before.

## 8. What stays the same

- The red lines, the kick rule for the different-device dialog, the
  Arms Race just-enough rule and every other standing order bind units
  exactly as they bind segment runs. A unit inherits its regular's
  activity metadata in `_activities_`.
- The regulars tracker stays the cadence source of truth; the pool is
  a work distribution layer over it, not a replacement.
- The `segment` field survives only as a reporting tag recording
  which slice a regular belonged to under the old routine; nothing
  schedules by it anymore.
- The round summary for Slack assembles from the `done` units'
  structured result sections, gathered by `tools/queue.py stats`,
  instead of three segment records. The same command doubles as the
  pool health report for the owner.

## 9. Migration - executed 2026-10-28

The owner directed the full move after validation, the same day.

1. **Validation** - the queue tool passed scratch-root end-to-end
   tests for enqueue, priority and expiry picking, token mutual
   exclusion, atomic claim, completion with structured results,
   lease reaping, dead-lettering after 3 attempts, chain numbering
   and chain type homogeneity, sync idempotency (a second sync
   produces nothing), VIP expiry stamping from the 19:00 reset,
   and learned estimates (samples of 600, 660 and 720 seconds
   produce an 11 minute estimate for the next unit of that type).
   A live shadow sync against the real tracker produced exactly
   the tracker's due set (zero at that moment - the skip path).
2. **Switch** - the ticker `lastwar-queue-ticker` (every 30
   minutes) was created with the full operating rules; the three
   segment schedules and the Zombie Invasion rounds schedule were
   deleted, their definitions backed up in the goal backup folder
   under cutover-2026-10-28. Zombie Invasion became chain
   production inside the ticker. The Slack round summary job is
   unchanged for now - it reads `_records_`, which the ticker
   keeps writing per unit.
3. **Settle** - watch the stats report for a few days - late
   finishes, dead letters, chain progress, learned estimates.
   Tune only two knobs if the evidence asks for it - the tick
   interval and the pass budget.

## 10. Questions put to the owner

- Lease length - 20 minutes proposed. Longer is safer against slow
  screens, shorter recovers crashed work faster. **Still open.**
- Ad hoc sessions as units or token-only - **resolved by the owner
  2026-10-28** - they join the pool as continuation chains (section
  2), Zombie Invasion first.
- Batch size - **resolved by the owner 2026-10-28** - there is no
  batch. The cap is per unit (15 minutes) and the executor loop
  re-picks after every unit, which is what lets other tasks ingest
  when their time arrives.

## 11. Execution discipline rules - the 2026-10-31 audit fixes

The miss audit of 2026-10-31 classified the 100 non-done units of
2026-10-30 and 2026-10-31 by root cause. 61 of them were one
failure repeated - a tap or search method that did not work, used
again in the next unit with no pivot and no escalation (audit
categories C and E). Only 4 were true red-line misses. The rules
below are the fix. They bind every executor and every unit, and
the [reflection of 2026-10-31](reflection-2026-10-31.md) maps each
one to the audit cause it answers.

- **R1 - live read or unverified.** A unit closes only on figures
  read live on screen inside that same unit. If a closing counter
  is hidden or blocked - the greyed donation button timer is the
  standing example - the unit closes as unverified, the tracker
  stays untouched, and the executor enqueues a named re-read unit
  for after the blocker clears. Arithmetic, presumed, by-result
  and ranking-row figures are banned as closing counts. Donation
  counts and truck trade counts are the named cases; the rule is
  general.
- **R2 - pivot, then escalate.** Two no-change taps at one point
  end that method inside the unit. The executor re-grounds the
  point fresh (entry icons are measured in every unit, never
  inherited), takes a second observation, and switches variant -
  fresh measured centre, long-press, or a different entry path.
  The second consecutive partial of a regular with the same
  blocker must arrive with a changed method. The third writes the
  blocker into the activity metadata, changes the entry route
  before any further unit of that type runs, and is named in that
  day round summary. A fourth identical partial is a process
  failure, not a result, and is reported to the owner as one.
- **R3 - quota checkpoints.** Quota types - trucks (dispatch 5,
  plunder 4 per trade day) and donations (30 coin donations per
  reset day), and any type that later gains a per-cycle quota -
  carry two checkpoints per cycle, six hours and two hours
  before the cycle end (the 19:00 local reset for reset-day
  quotas, the trade-day end for trucks). Each checkpoint reads
  the counter live. A shortfall at a checkpoint raises the next
  unit of that type to priority 1 and is named in the round
  summary - a quota may never be discovered short in the cycle
  final unit for the first time.
- **R4 - Arms Race judged at the phase start.** The first unit
  inside a phase reads the phase, the score and every scoring
  path, and works the just-enough plan from there. A phase whose
  paths all sit inside the red lines is reported to the owner as
  skipped-needs-owner early in the phase, with the queue contents
  as evidence - never discovered in the phase last minutes, and
  never re-checked identically inside the same phase.
- **R5 - owner-named tasks escalate.** A task the owner named
  that is not completed within 24 hours rises to priority 1 and
  is named in every round summary, with its age in days, until
  it closes. No owner-named task ages in silence. Crystal, named
  2026-10-25 and unlocated for six days, is the case this rule
  exists for; the Glittering Market, named 2026-10-31, entered
  under it from its first day.
- **R6 - no gap crosses a window boundary at the end.** Inside
  the last 60 minutes of a window - a phase, a trade day, a
  reset - a remaining gap is never left for the next re-check.
  The unit finishes inside itself, or enqueues a priority 1
  successor with its expiry set to the window close and names
  that successor in its closing summary.
- **R7 - starved subtasks are promoted.** A subtask deferred
  twice in one day inside its unit - radar map pins after the
  claims, truck plunder after dispatch, a shop step after combat
  work - becomes the first action of the next unit of that type,
  or a unit of its own. It is never again the last action of a
  unit that has already spent its budget.
- **R8 - reporting splits by-design partials.** Chain
  continuation and radar stack posture carry their own label in
  the round summary, split from misses. The daily miss count
  counts only units that failed their own objective, so the real
  blockers stay visible instead of hiding inside a raw partial
  count.

## 12. The daily collection ledger and the pre-reset zero sweep

The [daily collection ledger](daily-collection-ledger.md) is the
master list of everything collectible or due in one reset day,
each line with the live read that closes it. It is part of this
design - a unit that works a ledger line closes it by the ledger
standard, and the round summary reports ledger lines with no
producing unit as unscheduled, never as absent.

**The zero sweep.** Twice before each 19:00 local reset, at about
17:30 and about 18:30 local, a sweep unit walks the ledger item
by item. Each line is read live - at zero, not at zero, or
unreadable. A line not at zero gets a priority 1 unit of its own
type enqueued before the sweep closes, named in the sweep record;
the final sweep repeats the walk so the fix-up units it spawned
are themselves verified. Both sweeps expire at the reset.

**Generation - current practice and the planner interface.** The
planner (section 7) stages windows from three cadences - the 4
hour segment anchors, the daily reset and Thursdays. It cannot
yet express fixed clock slots such as 17:30 and 18:30, so until
it can, the sweep pair is enqueued manually with
`tools/queue.py enqueue` - regular `zero-sweep`, one chain per
reset day (chain id `pre-reset-sweep-<local date>`), priority 1,
`not_before` set to the slot start in UTC, `expires_at` set to
the reset, `est_minutes` 15. The pair for the 2026-11-01 reset
(chain pre-reset-sweep-2026-11-01, units 001 and 002) was enqueued
this way with the 0.7.0 change. The planner-side interface still
to build - a fixed-slot daily cadence in `tools/queue.py plan`,
taking a list of local clock slots per regular and staging them
through the same (regular, planned_for) invariant, so the sweep
becomes a produced regular with two daily slots instead of a
manual enqueue. Until that lands, the operator or the planner
pass enqueues the pair for the next reset as part of its run,
and a reset with no sweep pair staged is itself reported in the
round summary.

## Changelog

- 0.7.0, 2026-11-01 - sections 11 and 12 added under the owner
  instruction of 2026-10-31 to reflect and fix the miss audit -
  execution discipline rules R1 to R8, the daily collection
  ledger reference, and the pre-reset zero sweep with its manual
  enqueue practice and pending planner interface.
- 0.6.1, 2026-10-28 - implemented version, as written at the
  queue cutover.
