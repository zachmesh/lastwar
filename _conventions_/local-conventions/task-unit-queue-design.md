---
title: Task Unit Queue Design
created: 2026-10-28T10:22:00Z
modified: 2026-11-23T08:05:51Z
version: 0.38.0
description: Run the routine as short task units drawn from a file queue instead of long segment runs - implemented 2026-10-28
status: implemented
grounded_in:
  - source: owner request 2026-10-28 to design a task unit pool with short bounded executions
  - source: run records of 2026-10-27 and 2026-10-28 in _records_
  - source: miss audit of 2026-10-31 and the owner instruction of 2026-10-31 to reflect and fix
  - source: "PR #267 merged 2026-11-04 (Refs #147) - zero-sweep slots reset-anchored (reset_utc 02:00, offsets 90/30 minutes)"
  - source: "PR #614 merged 2026-11-11 (Refs #606) - zero-sweep slots moved from [90, 30] to [120, 60]; section 12 synced to that roster by this change"
  - source: "organizer 0432 run 2026-11-07 (Refs #147) - the four 19:00 mentions flagged as follow-up in 0.15.0 rewritten to the absolute reset instant 02:00 UTC (VIP expiry, scout anchor, quota checkpoints, deadline list)"
  - source: "Issue #689 (tooling) - outcome_unknown control lock after a session drop, implemented 2026-11-12 as the pool-level control-lock blocker and rule R9"
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

- **Task unit** - one regular from `_tools_/regulars.json`, sized to
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
  `_tools_/regulars.py` and writes one unit file per due regular into
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
  completed/        - completion markers for units closed in a detached worktree (live-only state, never committed; see below)
```

Unit file names are `<unit-id>.md` where the id is
`<regular-id>-<cycle>` and cycle is the local date and hour of the
producing cycle, for example `vip-2026-10-28-1900.md`. Names stay
unique across days without a central counter.

### Completion markers (`completed/`)

A unit closed in a detached worktree leaves its done record in that
worktree, so the main checkout's inbox still holds the unit and the
next pass would re-execute it (issue #438). The closing therefore
also records a small marker in the main checkout's `_queue_/completed/`
(`_tools_/queue.py` `record_completion`, called by the complete path
and by the dead-letter path; best effort - a write failure warns but
never fails the closing itself).

A marker is frontmatter only - `unit`, `status`, `finished_at`,
`executor` - because the full result lives in the done record; the
marker only has to answer "did this unit already close somewhere".
A marker suppresses the inbox copy only when it parses, names its
own unit, and carries a closing status; a file that fails any of
those suppresses nothing, so a half-written record can never hide
fresh work. `next`, `claim`, `sync` and `plan` treat a valid marker
exactly like a local done record, and sync production also blocks a
fresh unit for a slot whose closing is visible only as a marker
(issue #466).

Markers are live-only pool state, like the device token and the
blockers: `_queue_/.gitignore` excludes `completed/`, so markers are
never committed and never reach the records branches. `sync` reaps a
marker once the unit's done record lands in the local pool - the
delivery caught up - or after 168 hours (7 days,
`COMPLETED_STALE_HOURS`). A valid marker older than 168 hours with
no local done record is reported as lost (issue #563): the delivery
never carried that closing, so the retro can triage the named unit
instead of counting one more bare integer, and the suppression
lapsing makes the gap visible instead of hiding it behind a stale
file. `sync` also splits every reap by reason in its JSON
(`completion_markers_reaped_by_reason`: done-landed, aged-out,
invalid), so the ticker's sync section quotes the aged-out subset
as lost instead of folding it into the bare reaped count
(issue #826).

The two stranded units of issue #726 - `harvest-2026-11-11-1003`
and `zombie-invasion-zombie-2026-11-10-014` - have no full unit file
in the live pool's `done/` and no live marker: their markers lapsed
under the 168-hour rule, so their closings count as lost to the pool
under issue #563. The marker-count discrepancy this surfaced is
tracked by issue #735.

## 4. Unit schema

The unit frontmatter is the single structured source for the unit -
what the task is, where it is (the state subfolder plus the claim
fields below), and what it produced (the result section in section
5). Status, statistics and reports are gathered from these fields by
`_tools_/queue.py stats`, never by scraping prose. Values are kept
colon-free except timestamps, as elsewhere in this repository.

| Field | Meaning |
|---|---|
| `unit` | unit id, matches the file name |
| `regular` | regular id from _tools_/regulars.json |
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

- **1 expiry-critical** - vip (expires at the next reset after its slot, absolute 02:00 UTC - the slot opens its reset day, so expires_at is planned_for + 24h), passes when
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
frontmatter (via `_tools_/queue.py complete`) and the unit moves to
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
Because the keys are structured, `_tools_/queue.py stats` aggregates
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

The token file lives in the main checkout's `_queue_/claimed/`,
shared by every worktree of the repository, so a pass running in a
fresh detached worktree still sees a token held by a pass still
running (issue #383) - a worktree-local token would be invisible to
the next tick and the guard above would not hold. A re-acquire by the
same executor within 60 seconds of expiry renews the lease instead of
reporting held (issue #461) - the 2026-11-08 ticker-1049 secrets unit
re-acquired 3 seconds before expiry, was refused, and its game input
ran with no token held until the next acquire.

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
   incrementing `attempts`. The claim is gated by rule R25: the
   pass must first record its read of the newest queue-ticker
   record, so a claim on unread state fails loudly instead of
   executing.
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
- Aged unscheduled priority-1 units (issue #128 - owner-named
  units that are not regulars, so no producer ever stages them)
  get a real window from both producers: `sync` and `plan` each
  call the same idempotent windowing step, so whichever producer
  runs first attaches `planned_for` now and a 4 hour expiry, and
  the unit then surfaces as an expired miss instead of aging
  silently if it still is not executed.
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
  structured result sections, gathered by `_tools_/queue.py stats`,
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
  before the cycle end (the trade-day reset, absolute 02:00 UTC, for reset-day
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
- **R9 - control-lock pause (issue #689).** When a unit meets the
  `outcome_unknown` control lock - every input refused after a
  session drop, read-only inspection still live, new sessions do
  not clear it - it stops after its recovery attempts, closes
  failed naming the lock with
  `--stat blocker_overlay=control-lock`, and the pass stops: no
  further unit is attempted that tick. `queue.py` records the
  pool-level control-lock blocker and `next` hands out nothing
  while it stands, so a locked night burns no failed units. The
  wait-and-retry rule is the 4-hour stale bound: `sync` reaps a
  control-lock blocker older than 4 hours, the next tick probes
  with one input, and a fresh `outcome_unknown` re-records it.
  Any closing that sent input (done, partial, or
  skipped-needs-owner, without naming the lock) lifts the
  blocker. No self-clear has ever been observed - the 2026-10-26
  to 2026-10-27 lock cleared only when the owner submitted
  locally - so the probe cadence is a bound on wasted attempts,
  not a prediction that the lock will clear.
- **R10 - run the tool from a fresh main checkout (issue #694).**
  A pass runs `queue.py` only from a fresh main checkout - a pass
  worktree created through `_tools_/pass_worktree.py`, never the
  main working tree, which sits on another job's branch and can
  predate main by days. The tool enforces it: `next`, `sync`,
  `plan`, `sweep` and `enqueue` refuse, exit 1, when this copy
  of `queue.py` differs from main's `_tools_/queue.py`, so a
  stale pass fails loudly instead of deciding on old behaviour -
  the ticker-0334 pass ran the main-tree copy predating PR #692
  and `next` handed out a unit during the R9 control-lock pause
  the stale copy could not see. An unreadable main warns and
  lets the command proceed, like the #606 roster check.
  `LASTWAR_QUEUE_ALLOW_STALE_TOOL=1` is test-only, for isolated
  /tmp fixture validation of a new tool version. `claim`,
  `complete` and the token commands stay unguarded, so a pass
  that already decided can finish even if main advances
  mid-pass.
- **R11 - never decide from a checkout under the system temp directory (issue #429).**
  A pass worktree under /tmp can vanish mid-pass to the runtime's /tmp sweep - on 2026-11-07 three ticker passes lost their worktrees that way, and on 2026-11-08 the retro run lost /tmp/retro-1108-branch the same way, after the pass_worktree.py fix (PR #432) had already landed: the tool is opt-in, and a pass that creates its worktree with a bare `git worktree add` under /tmp never touches it. The tool enforces the location: `next`, `sync`, `plan`, `sweep` and `enqueue` refuse, exit 1, when this copy of `queue.py` - or the pool it would decide on - sits under the system temp directory (/tmp, or the platform temp dir from TMPDIR), so a pass in a doomed checkout fails loudly at its first decision instead of losing a finished unit's record at delivery. `LASTWAR_QUEUE_ALLOW_TMP_ROOT=1` is test-only, for isolated /tmp fixture validation of a new tool version. `claim`, `complete` and the token commands stay unguarded, so a pass that already decided can finish even if its worktree was created under /tmp.
- **R12 - next and claim decide on the live pool (issue #694).**
  `next` resolves the given root through the live pool before
  it lists candidates, so a worktree-root `next` reads the
  live inbox, not the worktree snapshot: a unit minted into
  the live pool after the snapshot - a chain successor, a
  planner-staged unit, an overlay-clearing unit - is visible
  to the pick, and a unit already claimed or closed live is
  never handed out again from a stale snapshot copy. `claim`
  claims the live-pool copy into the pass root, so a unit
  `next` hands out from the live pool is claimable even when
  the snapshot never held it; the done record still lands in
  the pass root, so the delivery is unchanged. A unit the
  live pool holds claimed or done is refused instead of
  claimed from the snapshot copy, and a unit the live pool
  does not hold at all falls back to the snapshot copy, so a
  unit committed to the pass branch but not yet in the live
  working tree stays claimable.

- **R13 - every pass record cites the tool identity (issue #694).**
  A pass runs `queue.py version` first and records its output -
  the resolved path of the invoked copy, its sha256, the git HEAD
  of the checkout holding it, and its currency against main's
  copy - in the pass record, so a later stale-tool handout is
  diagnosable from the record alone. The ticker-0737 handover
  could not be attributed from its record because no version,
  line count or worktree path was named: with the current tool
  the control-lock path is closed, but without the identity in
  the record the next occurrence of the same shape is
  unattributable again. The command only reports, so a stale
  copy still answers stale and a copy under the system temp
  directory still answers; it never refuses.

- **R14 - sync, plan and reap reap and expire the live pool (issue #705).**
  The step-1 reap, expiry and stale-copy drops resolve the given
  root through live_pool_root before they touch anything, so a
  worktree-root run expires the live pool instead of the snapshot:
  an expired claim is released into the live inbox, a stale inbox
  unit moves to live done with status expired, and a stale inbox
  copy of a unit already closed in done - locally or on the
  delivered records branch - is dropped from the live inbox.
  Ticker-1023 expired the 0603 set in the snapshot while the live
  inbox still held it, so the expired units stayed eligible to be
  handed out late. The pool-integrity guard in sync now covers the
  live pool too, since that is the pool being mutated; the aged
  priority-1 windowing step still acts on the given root and is
  not part of this rule.

- **R15 - never stage an already-expired window or a duplicate chain step (issue #712).**
  A window whose computed expiry is already past is never staged:
  plan_windows yields the cycle's current window, and for a
  reset-anchored regular in the morning that is yesterday's last
  slot, whose reset already passed - the 1140 planner run staged
  zero-sweep-2026-11-11-1700 with expires_at 2026-11-12T02:00Z,
  17h44m past at creation, a stillborn unit the next sync
  expires. The production path refuses it at the mint point, so
  sync, plan and sweep are all covered, records the refusal for
  the command to report, and keeps exit 0 - the refusal is the
  filter working, not an error. A reset-anchored slot is likewise
  never staged when the pool already holds the same chain step
  (same chain_id and chain_seq) at another slot: the (regular,
  planned_for) dedupe cannot see a pair staged at the old
  geometry, so without this check plan stages a second seq-1 at
  16:00 beside the 16:30 one the old [90, 30] geometry left in
  the inbox, and a second seq-2 for a reset day whose seq-2
  already closed in done. The duplicate is refused at the mint
  point and recorded for the command to report.
- **R16 - enqueue reconciles the next chain seq across live pool, markers and snapshot (issue #750).**
  `enqueue` mints a chain successor at the highest seq named by
  any of three sources - the live pool's inbox, claimed and
  done; the live pool's completion markers; and the given
  root's snapshot pool - instead of the live pool alone. A
  chain unit closed in a detached worktree lands its done
  record on the delivery branch, and sync drops the stale inbox
  copy, so the live pool can forget the highest finished seq
  and re-mint it: the zombie-036 case, where the finished unit
  survived only as a completion marker after its inbox copy
  was dropped. A worktree whose done pool disagrees with live -
  a completion this checkout has not seen yet, on another
  machine or an undelivered branch - holds a newer seq than
  live does. The mint takes the highest seq any source names
  and prints a note naming the source that raised it, so the
  reconciliation shows in the run log instead of a silent
  jump. Markers carry no chain_id, so only markers whose unit
  id matches the minted `<regular>-<chain_id>-<seq>` shape
  count.
- **R17 - a doomed probe burns the zombie chain unit, never a perception unit (issue #746).**
  A probe burns the unit it claims: the device is offline or
  the control lock just aged out, so the attempt fails and the
  unit is gone. The ticker-2152 rule prefers the zombie chain
  unit for the probe - a chain successor is re-minted, so the
  burn costs the chain nothing - and never burns a real
  perception unit: on Nov 14 six of twelve probes claimed
  scout units 011-016 although a zombie chain unit sat queued
  in inbox, because the plain pick_key order returns scout and
  zombie alternately. A probe pass calls `next --probe`;
  when a zombie chain unit is queued in inbox, actionable and
  inside the pass's budget, `next` hands it out ahead of the
  overlay steering and the normal pick. Otherwise the probe
  falls through to the normal pick, so a pass with no zombie
  unit queued still probes. "Available" means queued in
  inbox: a zombie unit already claimed or closed does not
  count.

- **R18 - enqueue refuses a chain successor after the chain's recorded event end (issue #745).**
  A chain ends only when its activity ends, but the mint must know the
  activity ended: the Glacieradon chain kept minting successors after
  the event expired about 2026-11-14T02:05Z (timer cross-check from
  chain units 001 and 023) - unit 037 was enqueued at
  2026-11-15T00:07:55Z, about 22 hours after the end, and the next pass
  spent its one live access closing a chain that should never have been
  seeded. A chain unit that reads the event timer live records
  `event_ends_at` in result.stats (ISO UTC, the timer reading projected
  to an instant); a unit that verifies the event has ended records it at
  or before now and closes the chain without a successor. `enqueue`
  takes the latest `event_ends_at` reading across the chain's done
  units in the live pool and the given root's snapshot pool (the #750
  reconciliation sources - only done units carry results), latest by
  when the reading was taken rather than the largest instant, and
  refuses to mint when it is past, naming the recording unit; exit 1,
  nothing minted. No reading
  recorded means no signal and the mint proceeds as before - the guard
  can only enforce an end the chain has recorded, so a unit that reads
  the timer must record it. The mint point is `enqueue`: the ticker's
  completion-time enqueue is what seeded 037 (its frontmatter carries
  the enqueue shape - empty planned_for, est 12); sync stages no chain
  successors itself, so no second guard point is needed.
  `_produce_for_window` chain-window units are covered separately by the
  R15 expiry refusal.

- **R19 - already_present counts only units the pool actually holds (issue #744).**
  The 1740 and 1840 planner runs on 2026-11-20 both reported already_present
  one above the post-expiry pre-stage pool count (67 vs 66, 62 vs 61): the
  counting rule, not a one-off miscount. A window the production path
  refuses holds no unit under its id in any pool state - the expired-window
  refusal (R15) was already classified into skipped_expired, but a
  duplicate-chain-step refusal and a stale-roster refusal fell through to
  the else branch and were counted as present. `plan` and `sweep` now
  classify every unproduced window before counting it: expired into
  skipped_expired, duplicate chain step into skipped_chain_seq, stale
  roster into skipped_roster_refusals, and only a genuine (regular,
  planned_for) dedupe hit increments already_present - the same rule in
  the pre-reset fix-up staging, whose refused fix-ups are reported the
  same way. The roster-freshness refusal now carries the refused window's
  unit id so callers can classify it (the per-regular refusal in the
  plan pre-check carries none, and needs none - the whole regular is
  skipped before any window is staged).

- **R20 - the sweep pair carries its ledger-walk task text (issue #748).**
  The pre-reset sweep pair used to carry the ledger-walk task
  section only when the planner appended it by hand (the 2026-11-07
  pair has it; the 2026-11-12 pair staged by `plan` carries the
  generic body instead), so a staged pair could reach the executor
  with no walk instructions. The production path now appends the
  standing section to each pair body - first pass or final pass by
  chain_seq, slot and reset clock times from the unit's own
  planned_for and expires_at, trade day from its chain_id, ledger
  line count read live from the ledger - so a staged pair always
  carries its walk instructions. A unit that is not a sweep pass,
  or a sweep unit with no chain sequence, keeps the generic body.

- **R21 - create refuses a stale existing branch when --base is given (issue #709).**
  `pass_worktree.py create --branch B --base R` reuses an existing
  branch B only when B's tip is R; a branch at any other tip is
  refused, exit 2, naming both tips, so a pass never decides from
  a stale main it did not ask for. Ticker-1047 asked for a fresh
  main worktree and got the stale branch at cc58a605c4 (pre-#704
  main) instead of current main 96520ae0d4, because create checked
  out any existing branch and ignored --base; the pass caught it
  only by verifying the base before deciding, and the defect
  recurred at ticker-1334 on the same shape. Without --base the
  checkout semantics stand - an existing branch is checked out
  as-is, which is how a pass re-opens a records branch - and a
  branch already at the base is reused and reported, so a
  re-created worktree after a removal is not an error.

- **R22 - every scheduled ticker slot leaves a record or a missed-fire marker (issue #743).**
  The ticker fires every 30 minutes on the :04/:34 grid; a slot is covered when a
  `_records_/<date>/queue-ticker/` record states that slot in its title, or when a
  `<slot>-missed-fire.md` marker names it. `_tools_/slot_coverage.py check` reports
  the recordless past-window slots (exit 1) and `mark` writes a marker, refusing a
  slot a record already covers. A late-starting pass names its record by its start
  time and states the slot it served in its title, so the file name alone never
  decides coverage - ticker-1930 serves the 19:04 slot. The retro's prose ruling
  adjudicates a slot, but only a record or a marker closes it for the check.

- **R23 - the missed-VIP-days count comes from the pool, keyed on the slot date (issue #742).**
  The ticker states an "Nth consecutive missed VIP day" count in its run records,
  but the count was kept by hand and the two chains disagreed: the ticker counted
  seven missed days (Nov 14 to Nov 20) while the knowledge-organizer chain counted
  eight (Nov 13 to Nov 20), and the Nov 20 retro ruled eight. The Nov 13 unit is
  the tell - it closed expired with finished_at 2026-11-15T02:22:15Z, a full day
  after its own reset day, so any count keyed on finished dates drops Nov 13.
  `_tools_/vip_missed.py count` counts from `_queue_/done/` and the
  `_queue_/completed/` markers instead: a day is keyed on the date embedded in
  its unit id (vip-YYYY-MM-DD-HHMM), only the 1800 slot defines a day (a pre-reset
  fix-up such as vip-2026-11-14-1630 is an extra, never a second day), and a day
  is missed when its 1800 unit expired/failed or closed done/partial with
  claimed_count 0 - the Nov 20 case, where the unit closed DONE because both items
  were already claimed before it ran, so the loop itself claimed nothing. A day
  with no outcome file, or a marker-only done/partial whose claimed_count is
  unseen, is unknown and never counted. The ticker states the count the tool
  reports, and the tool's per-day table is the audit trail when a later count
  disagrees with a ruling.

- **R24 - a scout chain stops at its reset day: enqueue refuses a successor and next skips the stale units (issue #818).**
  A chain successor inherits the completed unit's chain id, so nothing
  stopped a Nov-20 scout chain from minting on Nov-22: ticker-0957 was
  handed scout-scout-2026-11-20-019, created 2026-11-22T16:25:19Z, two
  days after the chain's reset day, and the pass declined to claim it
  and ended the execute loop. Executing a stale unit appends
  observations to the wrong reset day's observation file, and the chain
  never closes. `enqueue` refuses a successor when the chain's reset
  day has ended, and `next` never hands out a unit whose chain day is
  past - the skipped units are named on stderr, so the pass record
  shows the filter working. The day end is read from the chain id's
  trailing date against the roster's daily reset (02:00 UTC): a
  post-reset chain scout-YYYY-MM-DD ends at the reset ending the
  following local date, a midday chain scout-mid-YYYY-MM-DD at the
  reset ending its own local date. Any other chain id (zombie,
  pre-reset-sweep, scout-discovery) carries another lifetime, so the
  guard does not apply to it; an unreadable roster or an unparsable
  date is likewise no signal and the mint proceeds as before. The 23
  stale units already in the inbox are not removed by this change:
  sync expires the ones that carry an expiry, and the rest sit
  unhanded until the pool is reconciled.

- **R25 - a claim needs a read receipt for the newest queue-ticker record (issue #737).**
  The standing route change - re-read the newest queue-ticker
  record before any claim - was breached eight or more times on
  Nov 18 alone, and three consecutive honoring passes (1504/1604/
  1734) were broken by ticker-1804, which claimed
  gifts-2026-11-18-1430 before reading the 1734 record and
  released it un-executed: the pre-step as written does not
  enforce the route change, so the tool enforces it at the claim,
  the choke point. `queue.py read --record <path> --executor
  <name>` records that a pass read the newest record, writing a
  receipt into the shared live pool (`_queue_/read-receipt.md`,
  gitignored, like the device token and the blockers); `claim`
  refuses, exit 1 with nothing moved, until a receipt names the
  newest record, carries that record's sha256, names the claiming
  executor, and is at most 120 minutes old. A newer record landing
  after the read refuses the claim until it too is read, an
  amended record refuses until re-read, and another pass's read
  never authorises this pass's claim. With no queue-ticker record
  in the tree there is nothing to read and the claim proceeds, so
  the first pass ever and a scratch pool need no receipt. The
  newest record is the maximum by (date directory, file name)
  under `_records_/*/queue-ticker/`, read from the repository the
  pass runs in - a stale checkout defeats this gate exactly as it
  defeats R9 and R10, which is why the ticker runs from a fresh
  worktree. `LASTWAR_QUEUE_ALLOW_UNREAD_CLAIM=1` bypasses the gate
  only for isolated /tmp fixture validation of a new tool version.

- **R26 - sync names each reaped completion marker's reason, so a lost closing reads as lost in the run record (issue #826).**
  `sync` already reported the lost subset as `completion_markers_lost`
  (issue #563), but the ticker's sync section quotes only the bare
  `completion_markers_reaped` list, so the two markers ticker-1248
  reaped as aged out on Nov 18 read in its record as ordinary
  done-landed reaps and the loss stayed invisible until the #735
  forensics reconstructed it from finished_at arithmetic. `sync` now
  also reports `completion_markers_reaped_by_reason` in its JSON -
  every reaped marker under `done-landed` (its done record landed),
  `aged-out` (valid, older than 168 hours, no local done record -
  the delivery never carried the closing) or `invalid` (unparseable,
  or naming another unit, or carrying no closing status) - and the
  ticker's sync section quotes the aged-out subset from
  `completion_markers_lost` as lost, with the reason split as the
  audit trail. The `completion_markers_reaped` and
  `completion_markers_lost` fields are unchanged, so existing
  quoting keeps working. The aged-out warning itself moves to
  stderr, like every other sync warning: it used to print to
  stdout ahead of the JSON, so stdout stopped being one parseable
  object exactly when markers were lost - the case the warning
  exists for.

## 12. The daily collection ledger and the pre-reset zero sweep

The [daily collection ledger](daily-collection-ledger.md) is the
master list of everything collectible or due in one reset day,
each line with the live read that closes it. It is part of this
design - a unit that works a ledger line closes it by the ledger
standard, and the round summary reports ledger lines with no
producing unit as unscheduled, never as absent.

**The zero sweep.** Twice before each daily reset - the absolute instant 02:00 UTC (about 18:00 PST in winter, 19:00 PDT in summer) - at 120 and 60 minutes before the reset instant (16:00 and 17:00 PST in winter, 17:00 and 18:00 PDT in summer), a sweep unit walks the ledger item
by item. Each line is read live - at zero, not at zero, or
unreadable. A line not at zero gets a priority 1 unit of its own
type enqueued before the sweep closes, named in the sweep record;
the final sweep repeats the walk so the fix-up units it spawned
are themselves verified. Both sweeps expire at the reset instant itself.

**Generation - the planner interface.** The planner (section 7)
stages windows from four cadences - the 4 hour segment anchors,
the daily reset, Thursdays, and fixed local clock slots. A
regular with cadence `fixed-slots` lists its slots in
`fixed_slots`, its expiry clock time in `expires_local` and its
chain prefix in `chain_id_prefix`, and `_tools_/queue.py plan`
stages one unit per slot through the same (regular,
planned_for) invariant, with `not_before` at the slot start,
`expires_at` at the next expiry clock time and the chain id
`<prefix><local date>` with one sequence number per slot. The
sweep pair is that regular (`zero-sweep`, reset-anchored: `reset_utc` 02:00 with `slots_before_reset_minutes` [120, 60], expiry at the reset instant, chain `pre-reset-sweep-<local date>`, priority 1,
`est_minutes` 15, activity `daily-activities`); for the reset-anchored form `not_before` is the reset instant minus the slot offset and `expires_at` is the reset instant itself (wall-clock `fixed_slots` behaviour is unchanged for any other regular that uses it); `sync` never
stages it, because the tracker carries no per-slot done state
and plan owns its production. Before this interface landed the
pair was enqueued manually with `_tools_/queue.py enqueue`
(the pair for the 2026-11-01 reset, chain
pre-reset-sweep-2026-11-01, units 001 and 002, was enqueued this
way). A reset with no sweep pair staged is itself reported in
the round summary. `enqueue` refuses a zero-sweep unit whose
`not_before`/`expires_at` do not match the reset-anchored roster
geometry (tool guard, Refs #147): a hand-staged pair with the old
wall-clock geometry pre-empted the subcommand's correct pair on
2026-11-05/06, so the manual path now fails loudly and the pair is
staged with `queue.py sweep` (or `plan`) from a current tree.

2026-11-04 correction (organizer 0432, Refs #147): the sweep geometry above replaces the wall-clock 17:30/18:30 slots expiring 19:00 local, which could not close a trade day after the 2026-11-02 DST end (the Nov 3 final slot staged at 18:30 local fell half an hour after the 18:00 PST reset). Other 19:00 mentions elsewhere in this design (VIP expiry, the scout anchor, quota checkpoints, the deadline list) are not rewritten in this pass and are flagged as follow-up on #147.
2026-11-07 follow-up (organizer 0432, Refs #147): the four flagged mentions are rewritten in version 0.16.0 - VIP expiry (section 4), the scout anchor and the deadline list (section 13), and the quota checkpoints (rule R3) - all now anchor at the absolute reset instant 02:00 UTC (about 18:00 PST in winter, 19:00 PDT in summer). The two dated 19:00 mentions that stay are history, not rules: the 2026-10-27 lapse (section 1) and the 2026-10-28 migration validation (section 9), both from the PDT era when the reset was 19:00 local.
2026-11-18 sync (organizer 1232, Refs #606): the sweep geometry above moves from [90, 30] to [120, 60] per PR #614 (merged 2026-11-11) - seq-1 at 16:00, fix-ups at the 16:30 midpoint, seq-2 at 17:00 PST in winter - so the final pass spans two ticker passes instead of expiring inside one. The 2026-11-04 correction note above stays as history: it records the geometry the 90/30 form replaced, not the current form.
2026-11-21 (tool-developer, Refs #748): the pair bodies now carry the ledger-walk task section (rule R20) - the production path appends it, first pass or final pass by chain_seq, so the pair no longer depends on the planner appending the text by hand.

## 13. The perception layer (scout)

The day work set is no longer defined by the static regulars
alone. Under the owner direction of 2026-10-31, a perception
layer sits in front of production - scout units walk the game
interface first, record what is actually available to do, and
the pool is then diffed and filled from that observation. The
full design - the traversal checklist, the observed items
schema, the diff rules, the tool design and the phased roadmap -
is [perception-driven queue](perception-driven-queue.md). This
section fixes the queue-level contract.

- **Scout unit type.** The regular is `scout` (the post-reset
  full pass, daily-reset cadence anchored at the trade-day reset
  (absolute 02:00 UTC, about 18:00 PST in winter, 19:00 PDT in summer)) and `scout-midday` (the midday pass, daily-reset cadence
  anchored at 07:00 local, the middle of the reset day). Both
  name the activity `perception-scout`. Scout units are windowed
  work - priority 2; the production priority table carries
  their entries since the Phase 2 change (SYNC_PRIORITY and the
  SYNC_EST_MINUTES seeds of 10 minutes in `_tools_/queue.py`). A
  scout unit observes and records only - it never claims,
  fights, dispatches or buys. The work it finds belongs to the
  owning regular own unit.
- **Chain splitting.** One pass is one homogeneous chain of
  scout units, split by surface group - scout-base, scout-events,
  scout-store, scout-alliance - because a full traversal does not
  fit the 15 minute unit cap. The chain id is `scout-<reset
  date>` for the post-reset pass and `scout-mid-<reset date>`
  for the midday pass; the units run in order inside the pass
  window, and a unit that cannot finish its group closes partial
  with the unwalked surfaces named and a successor enqueued for
  the remainder. The regulars schema cannot express the split -
  cadence stages one unit per regular per window - so the staged
  unit is the chain head, and the executor extends the chain
  from it under the chain rules of section 2.
- **The observation output.** Every scout unit appends its
  surface sections to the day observation file,
  `_records_/<local date>/perception-scout/observation.md` - one
  file per reset day, append-only inside the day, carrying the
  day counters in its frontmatter and the observed items in the
  schema the perception document defines. The zero sweep of
  section 12 reads this file alongside the ledger, so observed
  items are swept by the same standard as modelled lines.
- **Result contract.** A scout unit result must reference the
  observed items it produced - `evidence` names the day
  observation file, `stats` carries surfaces_walked,
  items_observed, red_dots_seen, red_dots_explained,
  unexplained_red_dots and unknown_items, and `follow_up` names
  the units the diff enqueued or raised, or the unknowns
  awaiting exploration. A pass that closes with unexplained red
  dots closes partial - the zero unexplained red dots standard
  of the perception document is a closing condition, not a
  report nicety.
- **Dynamic production.** Units created from an observation are
  ordinary units - they pass the same enqueue validation, obey
  the (regular, planned_for) invariant where the planner
  produces them, and carry their source observation in their
  window text when the diff creates them. Unknown items enter as
  priority 2 exploration units and are governed by rule R5 from
  their first day. The diff itself is a program since Phase 2 -
  `_tools_/scout_diff.py` reads the day observation file, diffs it
  against the regulars, the `_activities_` roster with its
  candidate register, the ledger and the pool, and produces the
  enqueue plan, the candidate filings and the coverage report
  (dry run by default; `--apply` enqueues through this tool,
  only against an explicitly named pool root).
- **Scheduling is trigger-based (owner refinement 2026-10-31).**
  Fixed time slots are not the primary production mechanism.
  The regulars are repositioned as a capability profile library
  - each profile carries its entry point, rules, red lines,
  verification read, trigger conditions, deadline shape,
  cooldown and expected duration (perception document section
  5). A unit is produced when an observation fires one of the
  profile triggers - claimable now, deadline approaching, about
  to fill, state rotation, preparation opened, quota behind
  pace, or the floor check - and is ordered by the priority
  formula of the perception document (deadline pressure times
  value over expected duration, gated by dependencies and
  cooldowns) mapped onto the priority classes of section 4. The
  clock keeps two jobs only - the ticker cadence as the
  perception heartbeat, and the game hard deadlines (the trade-day reset,
  absolute 02:00 UTC, Arms Race phase windows, the rule R3 quota
  checkpoints). The planner of section 7 evolves accordingly -
  from staging one unit per (regular, time slot) to consuming
  observations plus profile trigger conditions and producing
  units when triggers fire; slot staging remains only as the
  floor check that guarantees no profile goes unobserved past
  its cadence. That evolution lands with the Phase 2 diff tool;
  until then the executor applies the trigger rules by hand from
  the observation file, and the section 7 planner keeps staging
  the floor.
- **Perception points are a floor, not a ceiling.** The two
  anchored scout passes (post-reset and midday) are the
  guaranteed minimum perception of a day. A full pass also
  fires on a detected state change, and partitioned perception
  of the volatile surface groups rolls with every ticker
  heartbeat, appending to the same day observation file - so a
  trigger is seen when it fires, not at the next anchor.
- **New task discovery (perception document section 6).** Every
  scout traversal roster-matches the labels it meets; an
  unmatched label is filed the same session as a provisional
  candidate profile under `_activities_`, and system mail and
  update notices are discovery signals in their own right (the
  Crystal Shop was announced by the maintenance mail of
  2026-10-21 before any pass found it). Candidates move
  candidate, exploring, then active or rejected with the reason
  kept. Exploration units learn a candidate read-only first -
  entry, mechanism, rewards, cost, cycle, deadline, scoring -
  and anything touching a price, diamonds, a red line or an
  unclear rule stays learn-only and is named to the owner in
  that day round summary. A candidate whose mechanism is clear
  and inside the free and safe envelope is completed as a
  profile with trigger conditions and turns active - from then
  on the trigger scheduler produces its execution units with no
  per-item owner approval. Every full pass closes with the
  `unmatched_labels` roster-out list as part of its coverage
  report, printed even when empty.
- **Learning and knowledge hardening (perception document
  section 10).** Every task - a discovered candidate, and a
  known task whose executions keep failing - carries a learning
  loop beside its execution loop: the task's own interface read
  in full with values marked measured or untested, web research
  cross-checked across at least two independent sources with
  disagreements resolved in favour of the in-game read and
  recorded, and the result hardened into the `_activities_`
  profile under a proficiency state (proficient only when the
  key fields - mechanism, cost, rewards, deadline shape - carry
  measured or dual-source support; a profile still learning
  makes its units learn first). An exploration unit closes not
  on having visited the surface but on the profile fields being
  complete enough to turn the candidate active or explicitly
  rejected. The first retrospective hardening target is
  radar-tasks, named in the perception document.

## 14. Retro review mechanism

**The repository is the single source of truth (owner rule,
2026-10-31).** Everything this game line knows - its knowledge,
mechanisms, measurements, reviews and reflections - lives in
this repository and nowhere else. Chat and Slack carry
summaries and pointers only, never the sole copy of anything
load-bearing. A finding that exists only in a conversation does
not exist.

### Per-unit measurement

Every unit already closes with a structured result (section
5). The retro mechanism fixes the `result.stats` keys every
task type must fill, so outcomes are comparable across units
and days -

| Key | Meaning |
|---|---|
| `target` | the quantity this unit set out to reach - a count, a quota, a threshold |
| `achieved` | the quantity actually reached, read live in the same unit (rule R1) |
| `resources_gained` | what the unit gained, itemised by resource type as displayed |
| `points` | score gained, for scoring types (duel, Arms Race, radar) |
| `costs` | what the unit spent - its duration, stamina, items consumed |
| `verified` | whether the closing figures are same-unit live reads - yes or no |
| `blocker_category` | when the unit did not reach its target, the miss audit root cause class - a window closure, b crowding out, c tap method, d inference over live read, e repeated blocker, f missing precondition, g true red-line miss, h by-design partial, i owner-named without escalation |

`duration_seconds`, `attempts` and the `claimed` list are
already core result fields and are not repeated in stats. A
unit that closes without its required stats keys is counted as
unverified in the retro aggregation, exactly as a unit whose
`verified` reads no - producing the numbers is part of the
work, not paperwork after it.

### Aggregation - the retro_report.py specification

Aggregation is specified here and implemented as
`_tools_/retro_report.py` (landed 2026-11-01). The tool
aggregates by task type, per day and over a rolling window -

```text
retro_report.py [--days 7] [--end YYYY-MM-DD] [--root DIR]
                [--out-dir DIR] [--format text|json]
```

`--root` is the repository root (default - the repository the
tool lives in); the pool is read at `<root>/_queue_` and the
appendix written to `<root>/_records_/retro` unless
`--out-dir` says otherwise. A unit belongs to the local date
of its `result.finished_at` in the queue timezone, falling
back to `started_at`, `planned_for`, and the date in its file
name. A unit file with no result is resolved against its day
INDEX in `_records_` and counted with status unknown and no
invented figures; a file that cannot be parsed is listed
under `parse_errors`, never silently skipped. The required
keys are `target`, `achieved`, `resources_gained`, `costs`
and `verified`, plus `blocker_category` whenever the unit
fell short of its target or closed partial, failed or
skipped-needs-owner; `points` is aggregated whenever present
but is not a required key, since it applies to scoring types
only and the pool carries no authoritative list of them.

- execution count, and the done, partial and
  skipped-needs-owner distribution;
- target attainment - achieved over target, summed and per
  unit;
- output per minute - resources gained and points, divided by
  execution minutes;
- total duration and median duration;
- the top repeated blockers, by `blocker_category` and by the
  named blocker;
- the unverified closing count - `verified` no, plus the units
  missing required stats keys.

Its only data sources are inside the repository - the unit
results in `_queue_/done` and the execution records in
`_records_`. Its only outputs are inside the repository, in
the standing cross-day series at `_records_/retro/` beside
the date folders, registered here as its convention - one
daily retro file per local date at `_records_/retro/<date>.md`
and the rolling metrics file at `_records_/retro/rolling-7d.md`,
both written by the retro pass, and the tool's metrics
appendix for the window ending on a date at
`_records_/retro/<date>-data.json` (canonical) with the same
numbers rendered as tables at `_records_/retro/<date>-data.md`
for the retro file to cite. The retro files are derived
artifacts: they are regenerated from the unit results, which
remain the immutable source (C1), and a regenerated appendix
states the pool state it was derived from - the scanned unit
count and a hash over the scanned units. Re-running the tool
over the same window and the same pool overwrites the
appendix with identical content; it never appends a copy.
The tool was validated on a fixture pool in /tmp - units with
complete stats, legacy stats missing the required keys, a
result-less unit resolved through its day INDEX, a file with
no frontmatter, and a unit outside the window - with the
aggregates asserted against hand-computed figures and a
second run byte-identical to the first.

### The daily rolling retro

Once a day, timed with the post-reset perception round, a
retro pass looks back over the past 7 days. Per task type it
reads the trends and names the largest loss points - where
target attainment leaks, where a blocker repeats, where time
goes without output. It produces improvement actions of two
kinds -

- **Execution knowledge** - what the game taught, written back
  into the corresponding `_activities_` profile with its
  version raised, under the hardening protocol of the
  perception document (section 10).
- **Meta knowledge** - what the system taught about itself -
  revisions to the scheduling triggers, the priority formula,
  the queue rules of section 11 or this design, proposed as
  document changes with their changelog entries.

Every improvement action carries its verification method and
the next-day recheck item that will prove or close it, written
into that day's retro file. An action not closed by its recheck
rolls into the next day's retro list - open actions are a
standing list, never a one-day note. The retro's headline
findings join the round summary as pointers to the retro file;
the file is the record, the summary is the pointer.

The retro itself, and every other standing activity of the
loop, is an execution and leaves its own record under the
[ops execution records](ops-execution-records.md) standard -
the retro measures the loop from those records, not from
session traces.

### System evaluation metrics

This section measures the work; the companion specification
[evaluation metrics](evaluation-metrics.md) measures the system
that does the work - execution efficiency per task type,
perception completeness and discovery generalisation, retro
effectiveness (including the recurrence rate of closed
improvements), the measured impact of the tool developer and
the knowledge organiser, and loop health, including the queue
depth and oldest unit age the 2026-10-31 loop review found
missing. The daily retro computes its core set, the weekly
comparison reads the trend, and threshold breaches are named
the day they are computed. Its computation extends
`_tools_/retro_report.py` as a `system_metrics` object in the
same data appendix, filed in the tool-developer backlog in the
specification's own terms.

Pushes follow the two-tier policy of
[push and PR policy](push-and-pr-policy.md): the records,
queue state and logs this design produces are tier 1 and push
directly to main, while changes to this design, the tools and
the activity profiles are tier 2 and land by pull request, with
the retro's loop-health check auditing that no tier-2 change
reached main unreviewed.

## Changelog

- 0.37.0, 2026-11-22 - section 11 gains rule R26 (reaped-marker reasons, issue #826): `sync` reports `completion_markers_reaped_by_reason` in its JSON, splitting every reaped completion marker into done-landed, aged-out and invalid, and the ticker's sync section quotes the aged-out subset as lost, so a lost closing is named as lost in the run record that reaped it instead of folding into the bare reaped count; the aged-out warning moves to stderr, so stdout stays one parseable JSON object even when markers are lost.
- 0.36.0, 2026-11-22 - section 11 gains rule R25 (claim-before-read gate, issue #737): `queue.py read` records that a pass read the newest queue-ticker record into a shared live-pool receipt, and `claim` refuses until the receipt names the newest record, carries its sha256, names the claiming executor and is at most 120 minutes old, so the standing route change (re-read the newest queue-ticker record before any claim) is enforced by the tool instead of the pass's pre-step prose; with no queue-ticker record in the tree the claim proceeds.

- 0.35.0, 2026-11-22 - section 11 gains rule R24 (stale scout chains, issue #818): `enqueue` refuses a scout chain successor after the chain's reset day ended and `next` skips units whose scout chain day is past, so a Nov-20 chain stops minting on Nov-22 instead of seeding units that write observations to the wrong day's file; the day end comes from the chain id's trailing date against the roster's 02:00 UTC reset (post-reset chains end at the following local date's reset, midday chains at their own date's reset), and zombie, sweep and discovery chains are untouched.

- 0.34.0, 2026-11-22 - section 11 gains rule R23 (missed-VIP-days count, issue #742): the count comes from the pool via new `_tools_/vip_missed.py`, keyed on the unit-id slot date with only the 1800 slot defining a day, and a day is missed when its 1800 unit expired/failed or closed done/partial with claimed_count 0; the ticker's hand count of seven vs the ruled eight is the live instance (the Nov 13 unit's finished_at fell on Nov 15).
- 0.33.0, 2026-11-22 - section 11 gains rule R22 (slot coverage, issue #743): every scheduled ticker slot leaves a record or a missed-fire marker; `_tools_/slot_coverage.py check` reports the recordless past-window slots on the :04/:34 grid and `mark` writes a marker, refusing a slot a record already covers; coverage is read from the record title, never the file name alone, so a late-starting pass serves the slot its title states.
- 0.32.0, 2026-11-22 - section 3 specifies the `_queue_/completed/` completion markers (issue #726): the marker's purpose (issue #438), its four fields, the validity rule, the readers that treat a marker like a local done record, the live-only status, and the sync reaping rule (168 hours, lost closings reported per issue #563). No tool change: `queue.py` already implements all of it; the design document never mentioned the directory.
- 0.31.0, 2026-11-21 - section 12 synced to the [120, 60] sweep geometry (PR #614, Refs #606; renumbered from 0.23.0, issue #739): the pair stages at 120 and 60 minutes before the reset instant (16:00 and 17:00 PST in winter, 17:00 and 18:00 PDT in summer), not 90 and 30. The entry was first labeled 0.23.0 and collided with the R15 entry (PR #715) that already claims 0.23.0; this change renumbers it to the next free version and bumps the frontmatter from its stale 0.17.0 to 0.31.0.
- 0.30.0, 2026-11-21 - section 4 states the VIP expiry rule explicitly (issue #733): a VIP unit staged for a reset opens that reset day and expires at the next reset, so expires_at is planned_for + 24h; the 2026-11-19T02:00:00Z expiry on vip-2026-11-17-1800 is correct and the ticker-2034 flag is refuted. No tool change: the daily-reset branch already computes planned_utc + 1 day.
- 0.29.0, 2026-11-21 - section 11 gains rule R21 (worktree-create base check, issue #709): `pass_worktree.py create` with an explicit `--base` reuses an existing branch only when its tip is the base and refuses a stale branch, exit 2, naming both tips, so a pass never decides from a stale main it did not ask for; without `--base` the checkout-as-is semantics stand.
- 0.28.0, 2026-11-21 - section 11 gains rule R20 (sweep ledger-walk task text, issue #748): the production path appends the standing ledger-walk task section to each pre-reset sweep pair body (first/final pass by chain_seq), so a staged pair carries its walk instructions instead of the generic body; slot and reset times come from the unit's own fields and the ledger line count is read live from the ledger.
- 0.27.0, 2026-11-21 - section 11 gains rule R19 (already_present counts only genuine dedupe hits, issue #744): `plan` and `sweep` report a refused window (expired, duplicate chain step, stale roster) under its own skip list instead of counting it as already present, so already_present equals the units the pool actually holds for the staged windows; the roster-freshness refusal now carries the refused window's unit id so callers can classify it.
- 0.26.0, 2026-11-21 - section 11 gains rule R18 (chain event-end guard, issue #745): `enqueue` refuses a chain successor when the chain's latest recorded `event_ends_at` is past, so a dead event's chain stops minting instead of seeding units for it; no reading recorded means no signal and the mint proceeds as before.
- 0.25.0, 2026-11-21 - section 11 gains rule R17 (doomed-probe zombie preference, issue #746): `next --probe` hands out a queued zombie chain unit ahead of the overlay steering and the normal pick, so a probe pass burns the re-minted chain unit instead of a scout unit; with no zombie unit queued, actionable and inside budget, the probe falls through to the normal pick.
- 0.24.0, 2026-11-21 - section 11 gains rule R16 (enqueue chain-seq reconciliation, issue #750): `enqueue` takes the next chain seq from the highest seq named by the live pool, its completion markers, or the given root's snapshot pool, so a finished seq the live pool forgot is never re-minted. 0.23.0 is now claimed by the merged R15 change (PR #715); the competing R15 branch PR #751 stands superseded, and the geometry fold (PR #761) still claims 0.23.0 per issue #739 and must renumber on rebase, so this change takes the next free number.
- 0.23.0, 2026-11-21 - section 11 gains rule R15 (expired-window and chain-step dedupe, issue #712): the production path refuses a window whose computed expiry is already past and a reset-anchored slot whose chain step the pool already holds at another slot, so plan no longer stages a stillborn zero-sweep unit for yesterday's slot or a second sweep pair at the new geometry beside the old one; both refusals are recorded and reported by plan and sweep.
- 0.22.0, 2026-11-12 - section 11 gains rule R14 (live-pool reap/expire, issue #705): `sync`, `plan` and `reap` resolve the given root through live_pool_root before reaping expired claims, expiring stale inbox units and dropping stale inbox copies, so a worktree-root run expires the live pool instead of the snapshot; the pool-integrity guard in sync now covers the live pool.
- 0.21.0, 2026-11-12 - section 11 gains rule R13 (tool-identity evidence, issue #694): `queue.py version` prints this copy's identity - resolved path, sha256, git HEAD and currency against main - so a pass record cites it and a stale-tool handout is diagnosable from the record alone; the command only reports and never refuses.
- 0.20.0, 2026-11-12 - section 11 gains rule R12 (live-pool handout, issue #694): `next` resolves the given root through the live pool before listing candidates, so a worktree-root `next` reads the live inbox instead of the snapshot, and `claim` claims the live-pool copy into the pass root, so a unit handed out from the live pool is claimable even when the snapshot never held it.
- 0.19.0, 2026-11-12 - section 11 gains rule R11 (worktree-location guard, issue #429): the decision commands refuse when this copy of queue.py - or the pool it would decide on - sits under the system temp directory, so a pass whose worktree was created under /tmp fails loudly at its first decision instead of losing its records to the runtime's /tmp sweep mid-pass; pass_worktree.py (PR #432) already refuses /tmp targets at creation, and this guard covers passes that never call it.
- 0.18.0, 2026-11-12 - section 11 gains rule R10 (tool-currency guard, issue #694): the decision commands refuse when this copy of queue.py differs from main's _tools_/queue.py, so a pass can no longer decide from a stale main-tree checkout; the worktree-tool rule is now enforced by the tool, not just documented.
- 0.17.0, 2026-11-12 - section 11 gains rule R9 (control-lock pause, issue #689): a unit that meets the outcome_unknown control lock closes failed naming blocker_overlay=control-lock, queue.py records a pool-level blocker that pauses next until it ages out after 4 hours or a closing that sent input lifts it, so a locked night burns no failed units.
- 0.16.0, 2026-11-07 - the four 19:00 mentions flagged as follow-up on #147 in 0.15.0 are rewritten to the absolute reset instant 02:00 UTC (about 18:00 PST in winter, 19:00 PDT in summer): VIP expiry (section 4), the scout anchor and the deadline list (section 13), and the quota checkpoints (rule R3). The dated 19:00 mentions in sections 1 and 9 stay: both describe the PDT era, when the reset was 19:00 local.
- 0.14.0, 2026-11-01 - section 14 gains a cross-reference to
  the ops execution records standard: the loop's own
  activities are executions and record themselves in the
  repository, and the retro measures them from those records.
- 0.13.0, 2026-11-01 - a cross-reference to the new push and
  PR policy: the queue's own outputs are tier-1 direct pushes,
  and changes to the design and tools are tier-2 pull requests
  under the audit of section 14's loop-health check.
- 0.12.0, 2026-11-01 - section 14 gains a cross-reference to
  the new evaluation metrics specification - the system-level
  companion that measures execution efficiency, perception,
  discovery, retro effectiveness and the impact of the tool
  developer and the knowledge organiser, with its computation
  extending _tools_/retro_report.py.
- 0.11.0, 2026-11-01 - the aggregation of section 14 is
  implemented as `_tools_/retro_report.py` - per regular, per
  day and rolling window aggregates over the done pool, the
  records INDEX fallback for result-less units, parse errors
  listed rather than skipped, no-data regulars stated, and
  the metrics appendix landed at
  `_records_/retro/<date>-data.json` with its Markdown
  rendering, byte-identical on a re-run over an unchanged
  pool; fixture validated in /tmp against hand-computed
  figures.
- 0.10.0, 2026-11-01 - Phase 2 of the perception layer landed
  in section 13 - `_tools_/scout_diff.py` implemented (dry run by
  default, `--apply` only against an explicitly named pool
  root, scratch-pool validated), the scout and scout-midday
  production priorities and estimate seeds recorded as landed
  in `_tools_/queue.py`, and the learning and knowledge hardening
  protocol of the perception document (its section 10)
  referenced, with radar-tasks as the first retrospective
  hardening target. Section 14 added under the owner direction
  of 2026-10-31 - the retro review mechanism: the repository as
  the single source of truth for this game line, the required
  per-unit result stats keys (target, achieved,
  resources_gained, points, costs, verified, blocker_category
  in the miss audit classes), the aggregation specification
  for a later `_tools_/retro_report.py` writing only into
  `_records_/retro/`, and the daily rolling retro whose
  improvement actions split into execution knowledge and meta
  knowledge, each carrying a verification method and a next-day
  recheck.
- 0.9.0, 2026-11-01 - section 13 extended under the owner
  refinement of 2026-10-31 - scheduling is trigger-based rather
  than fixed-slot, the regulars repositioned as a capability
  profile library, the planner evolution from slot staging to
  consuming observations plus profile triggers, perception
  points as a floor under rolling and change-triggered passes,
  and the new task discovery protocol with its candidate state
  machine and unmatched labels coverage; the perception-driven
  queue design rises to version 1.1.0 alongside.
- 0.8.0, 2026-11-01 - section 13 added under the owner direction
  of 2026-10-31 for perception-driven daily tasks - the scout
  unit type, its chain splitting, the observation output and its
  result contract, referencing the new perception-driven queue
  design document.
- 0.7.0, 2026-11-01 - sections 11 and 12 added under the owner
  instruction of 2026-10-31 to reflect and fix the miss audit -
  execution discipline rules R1 to R8, the daily collection
  ledger reference, and the pre-reset zero sweep with its manual
  enqueue practice and pending planner interface.
- 0.6.1, 2026-10-28 - implemented version, as written at the
  queue cutover.
