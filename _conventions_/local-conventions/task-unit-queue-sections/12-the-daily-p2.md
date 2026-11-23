---
title: 12. The daily collection ledger and the pre-reset zero sweep part 2
created: 2026-11-23T08:37:05Z
modified: 2026-11-23T08:37:05Z
version: 0.1.0
sequence: 30
description: Generation - the planner interface.
---
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

