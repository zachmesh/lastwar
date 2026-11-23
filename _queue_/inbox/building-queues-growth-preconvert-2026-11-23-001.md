---
unit: building-queues-growth-preconvert-2026-11-23-001
regular: building-queues
activity: building-queues
segment: 1
priority: 1
created_at: 2026-11-23T20:27:56Z
expires_at: 2026-11-23T22:55:00Z
planned_for:
not_before: 2026-11-23T22:40:00Z
window: pre convert the coin chests for the builder starts ends by 2309z
est_minutes: 15
serves: PL-14
chain_id: growth-preconvert-2026-11-23
chain_seq: 1
attempts: 0
max_attempts: 3
claimed_by:
claimed_at:
lease_until:
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-14

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, PRE-CONVERSION of coin chests before the 23:20Z builder starts, PL-14)

serves: PL-14

Why: the builders free at 23:20:12Z and the operator is idle from 23:10Z (300 s rule): the coin must be ready first. THIS UNIT ENDS BY 23:09Z: if it cannot, stop and record. No Upgrade, no Complete. COIN TOTAL T TO REACH = 271.8M (the default plan: Drill Ground Lv.26 59.5M, Lv.27 83.3M, Lv.28 119.0M, plus the 10M floor); the planner edits T when the Strategist's pick lands, and the coordinator does not dispatch before that.

HAZARD: the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: tap the intended tile first, confirm its name in a frame, never Use with another tile selected.

1. UR chests: read coin. Inventory, Resources tab: select the Coin Chest UR (87 owned). N = ceil((142.8M + 10M - coin now) / 2.4364M); N of 0 or less: skip. Set the field to N; read the field AND the Total line in a frame; Total at least 142.8M + 10M - coin now; N above 87: STOP. Use once. Read coin.
2. Plain chests: select the plain Resource Chest (20,862 owned; the field defaults to the FULL stock). M = ceil((T - coin now) / 6,000). Drag the handle (about 80 chests per pixel) until the field reads M or just above; read it; 6K times the field at least T - coin now; M above 20,862: STOP. Use once, ONLY the 6K Coins option; anything else or a cost: stop. Never Resource Choice Chests. Read coin.
3. Write coin before and after each Use and the last tap's UTC time.
Cost cap, stated: 0.60 USD.
