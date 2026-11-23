---
unit: building-queues-2026-11-23-0603
regular: building-queues
activity: building-queues
segment: 1
priority: 3
created_at: 2026-11-23T14:14:04Z
expires_at: 2026-11-23T18:03:00Z
planned_for: 2026-11-23T14:03:00Z
not_before:
window:
est_minutes: 3
serves: upkeep
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T16:50:31Z
lease_until: 2026-11-23T17:10:31Z
result:
  status: partial
  started_at: 2026-11-23T16:50:31Z
  finished_at: 2026-11-23T16:56:01Z
  duration_seconds: 330
  executor: operator
  summary: Builders 4/4 and labs 2/2 all busy (0 idle); barracks Lv.24 and Lv.20 tags read but the pistol tap showed no toast or panel, so their idle state was not re-read; the 13:44Z Drill Ground Full read stands unconfirmed
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/1650-queue-run.md and 1650-queue-run.csv; run 20261123T165032Z-127154
  follow_up: re-read the two barracks with a toast capture (the pistol toast vanished within 2 s); builder timers read 06:29:20 probably 16:29:20 (ends 2026-11-24T09:20Z), unverified
  stats:
    target: idle-slot read of builders, labs and barracks
    achieved: builders 0 idle, labs 0 idle, barracks not re-read
    resources_gained: none
    points: 0
    costs: none spent; model 0.239532 USD
    verified: yes
    run_id: 20261123T165032Z-127154
    run_steps: 19
    actions_done: 32
    actions_refused: 0
    cost_usd: 0.239532
    device_takeovers: 0
    slots_idle: 0
    blocker_category: f missing precondition (barracks pistol toast not captured)
    builders_idle: 0
    labs_idle: 0
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, the 14:03Z wave, coordinator 14:13Z)

Idle-slot read: close with `--stat slots_idle=<N>`, the TOTAL open slots including the blocked ones, and for slots blocked by a full Drill Ground `--stat slots_blocked_by_capacity=<N> --stat capacity_blocker="Drill Ground Full"` (blocker at most 40 characters); name the blocker as 'blocked by capacity: Drill Ground Full' with the building tag text. Read only: never Train, Collect, Upgrade or Research here.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `2700-routes.csv`); the safe empty-ground tap is the bare spot (310,660), not (400,640) after a camera shift. A TIPS dialog about another device: STOP, report, never Confirm. Tag text beside every number from a building panel. No purchase, diamond spend or speed-up. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
