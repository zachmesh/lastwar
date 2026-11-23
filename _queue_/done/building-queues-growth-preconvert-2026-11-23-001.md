---
unit: building-queues-growth-preconvert-2026-11-23-001
regular: building-queues
activity: building-queues
segment: 1
priority: 1
created_at: 2026-11-23T20:27:56Z
expires_at: 2026-11-23T22:56:00Z
planned_for:
not_before: 2026-11-23T22:35:00Z
window: pre convert coin chests ur then ssr for the builder starts ends by 2309z
est_minutes: 15
serves: PL-14
chain_id: growth-preconvert-2026-11-23
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T22:38:16Z
lease_until: 2026-11-23T22:58:16Z
result:
  status: done
  started_at: 2026-11-23T22:38:16Z
  finished_at: 2026-11-23T22:43:15Z
  duration_seconds: 299
  executor: operator
  summary: 80 Coin Chest (UR) for 194.91M then 62 Coin Chest (SSR) for 50.35M: coin 27.2M to 222.1M to 272.5M, above the target 271.8M; nothing started or completed
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/2238-queue-run.md and 2238-queue-run.csv; run 20261123T224105Z-4b264a
  follow_up: coin 272.5M for the three Drill Ground starts at 23:20Z; 9 SSR coin chests and 79 SR chests remain; the UR and SR counts fell since 11:21Z for an unrecorded reason
  stats:
    target: coin T = 271.8M from the UR then SSR coin chests
    achieved: coin 272.5M
    resources_gained: coin +245.3M from 142 chests
    points: 0
    costs: none spent; model 0.385 USD
    verified: yes
    run_id: 20261123T224105Z-4b264a
    run_steps: 30
    actions_done: 68
    actions_refused: 0
    cost_usd: 0.385
    device_takeovers: 0
    coin_before: 27.2M
    coin_after: 272.5M
    ur_chests_used: 80
    ssr_chests_used: 62
    rules_used: 1
  stats_missing: []
  stats_warnings: []
---

# building-queues

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: PL-14

## Brief (definition pointer, from the roster)

This unit is the regular `building-queues`: Building queues - read the four build queues, record running upgrades and idle slots; read-only, never start builds. Its definition is the activity folder `_activities_/building-queues/` (the folder is named for the activity, not the regular id): read its `rule-digest.md` first, then its `INDEX.md`. The map of every regular to its activity folder is `_records_/2026-11-22/queue-planning/2760-regular-to-activity-map.csv`. If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, PRE-CONVERSION 1 of 2: COIN chests before the 23:20Z builder starts, Decision 08)

serves: PL-14

THIS UNIT ENDS BY 23:09Z: if it cannot, stop and record. No Upgrade, no Complete. Decision `_records_/2026-11-22/strategy/dec-20261123-08.md`: coin total T = 271.8M (the three starts 261.8M plus the 10M floor), from the 87 UR Coin Chests (2.4364M each, 211.4M) and then about 50 SSR Coin Chests (about 0.81M each, 40.6M), the high grades first; the plain Resource Chests are NOT used here.

HAZARD: the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: tap the intended tile first, confirm its name in a frame, never Use with another tile selected.

1. Read coin. Inventory, Resources tab: select the Coin Chest UR. N = min(owned, ceil((T - coin now) / 2.4364M)); read the field AND the Total line in a frame before Use; Use once. Read coin.
2. If coin is still below T: select the Coin Chest SSR; read its coin value from the item panel; N = ceil((T - coin now) / that value), at most the owned count; the field and the Total line in a frame; Use once. Read coin.
3. Still below T after the SSR chests: STOP and record the shortfall; do not use plain Resource Chests. Write coin before and after each Use and the last tap's UTC time.
Cost cap, stated: 0.60 USD.
