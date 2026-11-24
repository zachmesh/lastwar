---
unit: building-queues-slot-read-2026-11-24-001
regular: building-queues
activity: building-queues
segment: 1
priority: 2
created_at: 2026-11-23T13:35:06Z
expires_at: 2026-11-24T04:30:00Z
planned_for:
not_before: 2026-11-24T02:30:00Z
window: builders read tonight idle slots blocker named
est_minutes: 8
serves: PL-08
chain_id: slot-read-2026-11-24
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T04:07:04Z
lease_until: 2026-11-24T04:27:04Z
result:
  status: done
  started_at: 2026-11-24T04:07:04Z
  finished_at: 2026-11-24T04:09:41Z
  duration_seconds: 157
  executor: operator
  summary: All four builders busy (the three Drill Grounds and the Oil Well Lv.22, ends as predicted); Hospital unchanged at 1,364 wounded, 5,306 completed, free room 1,329; Total Power 150,046,960; nothing pressed
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/0407-queue-run.md and 0407-queue-run.csv; run 20261124T040704Z-f89a5f
  follow_up: the Oil Well ends 08:01:45Z inside the quiet window; the first free builder after it is the Lv.26 ground at 2026-11-26T21:10:36Z
  stats:
    target: read the four builders and the Hospital
    achieved: four builders and Hospital read
    resources_gained: none
    points: 0
    costs: none spent; model 0.171658 USD
    verified: yes
    run_id: 20261124T040704Z-f89a5f
    run_steps: 14
    actions_done: 13
    actions_refused: 0
    cost_usd: 0.171658
    device_takeovers: 0
    slots_idle: 0
    wounded: 1364
    completed: 5306
    free_room: 1329
    total_power: 150046960
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-08

## Brief (planner, builders read tonight, conformance alarm, Steer A flip plan)

serves: PL-08

Refresh the builder read. Open the hammer icon: for each of the four builders write its tag text or task (building and level), its time left to the second, and whether it is busy or idle; the four builders were freed at 23:20Z on 2026-11-23 and restarted: read what each now builds and its time left. `slots_idle` is the TOTAL idle builders. Write the UTC time of the read.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`; follow it (the safe tap is the bare spot (310,660), not (400,640) after a camera shift; never WORLD with a menu open low). If a slot is idle and the cause is the full Drill Ground, write exactly 'blocked by capacity: Drill Ground Full' with the building's tag text (name and level above it after the tap) and record it in the closing `queue.py complete` line as `--stat slots_blocked_by_capacity=<N> --stat capacity_blocker="Drill Ground Full"` (the blocker text at most 40 characters; a count with no blocker named exempts nothing; the count is capped at the open slots); `--stat slots_idle=<N>` is the TOTAL number of open slots, INCLUDING the blocked ones; the blocked count is a subset of it (the tool subtracts it). A TIPS dialog about another device: STOP and report, never Confirm. Read only: never Upgrade, Research, Train, Collect, Promote, Speed Up or Finish Now. Tag text beside every number; none means [G]. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No chain successor.
HOSPITAL AND TROOPS: as in `building-queues-2026-11-23-1803` (Hospital Severely Wounded Lv.10 against 364, Completed, free room; one Drill Ground's troop line and OUTSIDE count; any march list; read only); write Total Power and the Lv.10 count to the second.
HOSPITAL (measured 02:05Z to 02:09Z, record 0205: Severely Wounded 1,364 of 7,999, Completed 5,306, free room 1,329, Total Power 148,769,946; the Zombie Siege ended, cooldown to 11-26): read the Hospital (tent E about (678,510), tag Hospital Lv.25): 'Severely Wounded Units' and 'Completed', free room = 7,999 minus both. Write the figures, the free room, the change since 02:05Z (healing or new casualties) and Total Power. Never Collect, Heal or Speed Up.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
