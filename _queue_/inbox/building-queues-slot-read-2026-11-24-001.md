---
unit: building-queues-slot-read-2026-11-24-001
regular: building-queues
activity: building-queues
segment: 1
priority: 2
created_at: 2026-11-23T13:35:06Z
expires_at: 2026-11-24T04:30:00Z
planned_for:
not_before: 2026-11-24T02:10:00Z
window: builders read tonight idle slots blocker named
est_minutes: 8
serves: PL-08
chain_id: slot-read-2026-11-24
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-08

## Brief (planner, builders read tonight, conformance alarm, Steer A flip plan)

serves: PL-08

Refresh the builder read. Open the hammer icon: for each of the four builders write its tag text or task (building and level), its time left to the second, and whether it is busy or idle; the four Training Base upgrades end at 2026-11-24T09:20Z. `slots_idle` is the TOTAL idle builders. Write the UTC time of the read.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`; follow it (the safe tap is the bare spot (310,660), not (400,640) after a camera shift; never WORLD with a menu open low). If a slot is idle and the cause is the full Drill Ground, write exactly 'blocked by capacity: Drill Ground Full' with the building's tag text (name and level above it after the tap) and record it in the closing `queue.py complete` line as `--stat slots_blocked_by_capacity=<N> --stat capacity_blocker="Drill Ground Full"` (the blocker text at most 40 characters; a count with no blocker named exempts nothing; the count is capped at the open slots); `--stat slots_idle=<N>` is the TOTAL number of open slots, INCLUDING the blocked ones; the blocked count is a subset of it (the tool subtracts it). A TIPS dialog about another device: STOP and report, never Confirm. Read only: never Upgrade, Research, Train, Collect, Promote, Speed Up or Finish Now. Tag text beside every number; none means [G]. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No chain successor.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
