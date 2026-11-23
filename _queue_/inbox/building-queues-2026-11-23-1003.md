---
unit: building-queues-2026-11-23-1003
regular: building-queues
activity: building-queues
segment: 1
priority: 3
created_at: 2026-11-23T15:09:37Z
expires_at: 2026-11-23T22:03:00Z
planned_for: 2026-11-23T18:03:00Z
not_before: 2026-11-23T18:03:00Z
window:
est_minutes: 3
serves: PL-08
chain_id:
chain_seq:
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

## Brief (planner, the 18:03Z wave)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (named for the activity, not the regular id): read its `rule-digest.md` first. Map: `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which; never improvise.

Idle-slot read: close with `--stat slots_idle=<N>`, the TOTAL open slots including the blocked ones, and for slots blocked by a full Drill Ground `--stat slots_blocked_by_capacity=<N> --stat capacity_blocker="Drill Ground Full"` (blocker at most 40 characters); name the blocker as 'blocked by capacity: Drill Ground Full' with the building tag text. Read only: never Train, Collect, Upgrade or Research here.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `2700-routes.csv`); the safe empty-ground tap is the bare spot (310,660), not (400,640) after a camera shift. A TIPS dialog about another device: STOP, report, never Confirm. Tag text beside every number from a building panel. No purchase, diamond spend or speed-up. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
