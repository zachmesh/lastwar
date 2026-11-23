---
title: 13. The perception layer (scout) part 2
created: 2026-11-23T08:37:05Z
modified: 2026-11-23T08:37:05Z
version: 0.1.0
sequence: 33
description: Result contract.
---
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
