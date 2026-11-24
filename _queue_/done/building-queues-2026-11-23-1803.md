---
unit: building-queues-2026-11-23-1803
regular: building-queues
activity: building-queues
segment: 1
priority: 3
created_at: 2026-11-23T22:33:38Z
expires_at: 2026-11-24T06:03:00Z
planned_for: 2026-11-24T02:03:00Z
not_before: 2026-11-24T02:03:00Z
window:
est_minutes: 2
serves: PL-08
chain_id:
chain_seq:
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-24T02:05:48Z
lease_until: 2026-11-24T02:25:48Z
result:
  status: done
  started_at: 2026-11-24T02:05:48Z
  finished_at: 2026-11-24T02:09:48Z
  duration_seconds: 240
  executor: operator
  summary: The 1,647,000 Total Power fall is 1,000 wounded T10 troops: Hospital Severely Wounded 1,364 of 7,999 (364 before), Completed 5,306, free room 1,329; March Queues 0/3 so no squad is out; the Zombie Siege search ran and is on cooldown to 2026-11-26
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/0205-queue-run.md and 0205-queue-run.csv; run 20261124T020548Z-59c33e
  follow_up: the 1,000 wounded return as power only after healing (not pressed); the Strategist decides; the Hospital also holds 5,306 uncollectable completed troops (Drill Ground Full)
  stats:
    target: read the Hospital, the Zombie Siege page, the Drill Ground and the Total Power
    achieved: Hospital and Zombie Siege read, H-B confirmed
    resources_gained: none
    points: 0
    costs: none spent; model 0.262521 USD
    verified: yes
    run_id: 20261124T020548Z-59c33e
    run_steps: 19
    actions_done: 61
    actions_refused: 0
    cost_usd: 0.262521
    device_takeovers: 0
    wounded_before: 364
    wounded_now: 1364
    completed: 5306
    free_room: 1329
    total_power: 148769946
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, the 02:03Z wave specifics)

Idle-slot read: close with `--stat slots_idle=<N>`, the TOTAL open slots including the blocked ones, and for slots blocked by a full Drill Ground `--stat slots_blocked_by_capacity=<N> --stat capacity_blocker="Drill Ground Full"` (blocker at most 40 characters); a finished batch is never retried while the Drill Ground is Full. Read only: never Train, Collect, Upgrade or Research here. The builder starts of 23:20Z are the ground and Oil Well units: this read presses nothing.

Safe tap: the bare spot (310,660), not (400,640) after a camera shift (WORLD then BASE first).
HOSPITAL AND TROOPS (Total Power fell 60,939, then about 1,000 T10 troops, 1,647,000; cause [G] the Zombie Siege or a squad sent out): read the Hospital (tent E about (678,510), tag Hospital Lv.25): 'Severely Wounded Units' (Lv.10 was 364) and 'Completed', free room = 7,999 minus both (2,329 at 16:22Z); then ONE Drill Ground (Lv.26, about (705,690)): its troop line and OUTSIDE count, and any march or squad list (read only). Wounded = 364 + N (401 and free room 2,292 for 37; 1,364 and 1,329 for 1,000); dead = 364 unchanged and in-base troops lower; away = 364 unchanged and Outside higher. Write Total Power and the Lv.10 count to the second. Never Collect, Heal, Speed Up, send or recall; never touch the Zombie Siege schedule.
