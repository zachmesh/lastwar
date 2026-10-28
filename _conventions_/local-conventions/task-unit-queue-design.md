---
title: Task Unit Queue Design
created: 2026-10-28T10:22:00Z
modified: 2026-10-28T10:33:00Z
version: 0.3.0
description: Proposal to run the routine as short task units drawn from a file queue instead of long segment runs
status: proposal
grounded_in:
  - source: owner request 2026-10-28 to design a task unit pool with short bounded executions
  - source: run records of 2026-10-27 and 2026-10-28 in _records_
---

# Task unit queue design

Status - proposal for owner review. Nothing in the live routine changes
until the owner approves the migration in section 8.

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
- **Pool** - the `_queue_` type folder with three state subfolders.
  `inbox` holds pending units, `claimed` holds units under execution,
  `done` holds finished units. Moving a file is the state transition.
- **Producer** - a short job that reads the due list from
  `tools/regulars.py` and writes one unit file per due regular into
  `inbox`. It never touches the device.
- **Executor loop** - the main agent's standing job under this
  design. It keeps executing where work is needed - take the device
  token, pick the best unit, run it, write its result, pick the next
  one. The loop is the scheduler; there is no separate batch concept.
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
  standing stop rules (cleared, or the chain budget of 3 hours),
  while higher priority units slip in between its units whenever
  their time arrives.
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
| `window` | execution window constraint, for example an Arms Race phase or a duel posture; empty when none |
| `est_minutes` | producer estimate; enqueue rejects anything above the 15 minute cap |
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
Because the keys are structured, `tools/queue.py stats` aggregates
reliably across the whole pool - counts by state and by regular,
result status totals, duration averages and maxima, units finished
after their expiry, units expired while waiting, and claims past
their lease - in text, YAML or JSON.

The matching `_records_` execution file is still written as today
(C1 append-only audit); the unit references it under `evidence`.

## 6. The executor loop and the 15 minute unit

The loop the main agent runs, indefinitely, while work exists.

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
   atomic in-game action, write the `_records_` file, complete the
   unit with a `partial` result noting the remaining work, and move
   it back to `inbox` - it keeps its `expires_at` and chain
   position, so the loop or a later pass resumes it ahead of fresh
   work.
4. On completion, write the `_records_` file, complete the unit
   (the result section lands in its frontmatter), rename `claimed`
   to `done`, and update the regulars tracker exactly as segment
   runs do today. If the unit belongs to a chain and its result
   stats say the activity is not exhausted, enqueue the next unit
   of the chain - unless the chain's own stop rules end it (for
   Zombie Invasion, nearby zombies cleared, or the 3 hour chain
   budget spent; the budget is carried in the chain units'
   structured fields, not in prose).
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

One honest limit - the loop runs inside agent sessions and
scheduled triggers, not as a literal daemon. In practice the
executor trigger fires frequently and each pass works through
units in this order until the pool's urgent work is drained;
between passes the pool simply waits in `inbox`. The unit cap is
what makes that safe - no pass can be captured by one task for
longer than 15 minutes.

## 7. What stays the same

- The red lines, the kick rule for the different-device dialog, the
  Arms Race just-enough rule and every other standing order bind units
  exactly as they bind segment runs. A unit inherits its regular's
  activity metadata in `_activities_`.
- The regulars tracker stays the cadence source of truth; the pool is
  a work distribution layer over it, not a replacement.
- The round summary for Slack assembles from the `done` units'
  structured result sections, gathered by `tools/queue.py stats`,
  instead of three segment records. The same command doubles as the
  pool health report for the owner.

## 8. Migration

1. **Shadow mode (one day)** - the producer writes units each cycle
   and the reaper runs, but executors do not claim; the segment crons
   keep playing. Compare pool contents against the tracker daily to
   prove the split is faithful.
2. **Pilot** - segment 2 regulars (mail, help, gifts, train,
   star-ceremony, vip) move to executor batches; segments 1 and 3 keep
   their crons.
3. **Full switch** - all regulars move; the three segment crons are
   replaced by the producer plus a frequent executor trigger. The
   segment cron definitions are retired only on the owner's word.

## 9. Questions put to the owner

- Lease length - 20 minutes proposed. Longer is safer against slow
  screens, shorter recovers crashed work faster. **Still open.**
- Ad hoc sessions as units or token-only - **resolved by the owner
  2026-10-28** - they join the pool as continuation chains (section
  2), Zombie Invasion first.
- Batch size - **resolved by the owner 2026-10-28** - there is no
  batch. The cap is per unit (15 minutes) and the executor loop
  re-picks after every unit, which is what lets other tasks ingest
  when their time arrives.
