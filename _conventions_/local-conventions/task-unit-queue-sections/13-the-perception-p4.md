---
title: 13. The perception layer (scout) part 4
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 46
description: Scheduling is trigger-based (owner refinement 2026-10-31).
---
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
