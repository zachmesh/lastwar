---
unit: training-slot-read-barracks-2026-11-24-001
regular: training
activity: troop-training
segment: 1
priority: 2
created_at: 2026-11-23T13:35:27Z
expires_at: 2026-11-23T12:00:00Z
planned_for:
not_before: 2026-11-24T02:30:00Z
window: barracks read tonight idle queues blocked by capacity named
est_minutes: 10
serves: PL-09
chain_id: slot-read-barracks-2026-11-24
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-24T04:07:34Z
  duration_seconds: 
  executor:
  summary: retired by the planner: the four barracks were read at 03:51Z (record 0351) and the unit ends at 04:40Z; the finished-batch lesson now lives in the roster training unit and the route card
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# training

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-09

## Brief (planner, barracks read tonight, conformance alarm, Steer A flip plan)

serves: PL-09

Refresh the troop-training read, one barracks per fresh frame: Lv.27, Lv.30, Lv.24 and Lv.20 by the tap points on the card. For each write the tag text, then busy (batch, tier and count, time left to the second) or idle. For an idle barracks open the pistol (the middle button under the tag), read the Train panel without pressing Train: the slider maximum and any 'Drill Ground Full' text, then close it with its X. The Lv.24 barracks was idle and capacity-blocked in the Coach's read. `slots_idle` is the TOTAL idle queues including the ones blocked by a full Drill Ground; `slots_blocked_by_capacity` counts the blocked ones as a subset. Read the soldier icon count and cap if it shows.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`; follow it (the safe tap is the bare spot (310,660), not (400,640) after a camera shift; never WORLD with a menu open low). If a slot is idle and the cause is the full Drill Ground, write exactly 'blocked by capacity: Drill Ground Full' with the building's tag text (name and level above it after the tap) and record it in the closing `queue.py complete` line as `--stat slots_blocked_by_capacity=<N> --stat capacity_blocker="Drill Ground Full"` (the blocker text at most 40 characters; a count with no blocker named exempts nothing; the count is capped at the open slots); `--stat slots_idle=<N>` is the TOTAL number of open slots, INCLUDING the blocked ones; the blocked count is a subset of it (the tool subtracts it). A TIPS dialog about another device: STOP and report, never Confirm. Read only: never Upgrade, Research, Train, Collect, Promote, Speed Up or Finish Now. Tag text beside every number; none means [G]. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No chain successor.
Barracks read (the Coach's audit, adopted by Steer A): one barracks per fresh frame; record the READY BUBBLE over each tent (a portrait = a finished batch waiting, a clock = training, none = empty) and press the pistol ONCE per barracks whenever room could exist: a finished batch collects (toast 'Training complete: N Lv.X units are ready'). The toast 'Drill Ground Full' is IDENTICAL for an empty queue and a finished batch behind room 0, so classify each barracks as EMPTY QUEUE, FINISHED BATCH WAITING (with its size) or BLOCKED BY THE TOAST recorded in THIS read; write the split in the note. Close with `--stat slots_idle=<N>` and, for slots blocked by a full Drill Ground, `--stat slots_blocked_by_capacity=<N> --stat capacity_blocker="Drill Ground Full"`. Never Train, Heal, Hospital Collect, speed up or buy here.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
