---
title: 7. The planner - a 12 hour horizon
created: 2026-11-23T08:37:05Z
modified: 2026-11-23T08:37:05Z
version: 0.1.0
sequence: 12
description: Production has two layers (owner direction 2026-10-28).
---
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

