---
unit: building-queues-growth-preconvert-2026-11-23-002
regular: building-queues
activity: building-queues
segment: 1
priority: 1
created_at: 2026-11-23T20:27:58Z
expires_at: 2026-11-23T12:00:00Z
planned_for:
not_before: 2026-11-23T22:40:00Z
window: pre convert 2 of 2 plain resource chests ends by 2309z
est_minutes: 10
serves: PL-14
chain_id: growth-preconvert-2026-11-23
chain_seq: 2
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
result:
  status: expired
  started_at:
  finished_at: 2026-11-23T20:29:11Z
  duration_seconds: 
  executor:
  summary: merged into building-queues-growth-preconvert-2026-11-23-001: two units back to back would need a 300 s idle wait between them and the second would expire unclaimed
  claimed: []
  claimed_count: 0
  evidence: 
  follow_up: none
  stats:
  stats_missing: [target, achieved, resources_gained, costs, verified]
  stats_warnings: []
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-14

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, PRE-CONVERSION 2 of 2: the plain Resource Chests, before the 23:20Z builder starts, PL-14)

serves: PL-14

Why: the four builders free at 23:20:12Z and the operator is idle from 23:10Z (the 300 s rule), so the coin must be ready first. THIS UNIT ENDS BY 23:09Z: if it cannot, stop and record. Press NO Upgrade and NO Complete here. COIN TOTAL T TO REACH = 271.8M (the default plan: Drill Ground Lv.26 59.5M, Lv.27 83.3M, Lv.28 119.0M, plus the 10M floor); the planner edits T when the Strategist's pick lands, and the coordinator does not dispatch before that.

HAZARD: the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: tap the intended tile first, confirm its name in a frame, never Use with another tile selected.

1. Read coin (after unit 001 of this pair). Inventory, Resources tab: select the plain Resource Chest (20,862 owned; the field defaults to the FULL stock). M = ceil((T - coin now) / 6,000). Drag the handle (about 80 chests per pixel) until the field reads M or just above; read it in a frame; 6K times the field at least T - coin now; M above 20,862: STOP. Use once and choose ONLY the 6K Coins option; anything else or a cost: stop. Never Resource Choice Chests. Read coin, the chests left and the UTC time of the tap.

Tag text beside every number; none means [G]. Rules: `_records_/2026-11-22/queue-planning/2430-conversion-rules.md`.
Cost cap, stated: 0.40 USD.
