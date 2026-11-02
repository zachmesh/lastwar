---
title: Task Unit Queue Design
created: 2026-10-28T10:22:00Z
modified: 2026-11-01T07:58:31Z
version: 0.14.1
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
sweep pair is that regular (`zero-sweep`, slots 17:30 and 18:30,
expiry 19:00, chain `pre-reset-sweep-<local date>`, priority 1,
`est_minutes` 15, activity `daily-activities`); `sync` never
stages it, because the tracker carries no per-slot done state
and plan owns its production. Before this interface landed the
pair was enqueued manually with `_tools_/queue.py enqueue`
(the pair for the 2026-11-01 reset, chain
pre-reset-sweep-2026-11-01, units 001 and 002, was enqueued this
way). A reset with no sweep pair staged is itself reported in
the round summary.

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
  full pass, daily-reset cadence anchored at the 19:00 local
  reset) and `scout-midday` (the midday pass, daily-reset cadence
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
  perception heartbeat, and the game hard deadlines (the 19:00
  reset, Arms Race phase windows, the rule R3 quota
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
