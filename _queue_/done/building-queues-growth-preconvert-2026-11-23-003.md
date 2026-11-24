---
unit: building-queues-growth-preconvert-2026-11-23-003
regular: building-queues
activity: building-queues
segment: 1
priority: 1
created_at: 2026-11-23T22:32:18Z
expires_at: 2026-11-24T01:25:00Z
planned_for:
not_before: 2026-11-23T22:35:00Z
window: fallback food chest conversion dispatched only by name after a ground start stops on a food row
est_minutes: 10
serves: PL-14
chain_id: growth-preconvert-2026-11-23
chain_seq: 3
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T23:33:12Z
lease_until: 2026-11-23T23:53:12Z
result:
  status: done
  started_at: 2026-11-23T23:33:12Z
  finished_at: 2026-11-23T23:36:42Z
  duration_seconds: 210
  executor: operator
  summary: 101 Food Chest (UR) used once at 23:35:44.748Z: food 136.0M to 546.1M against the target 542M; the builder timers are a flat 6h 32m 00s under the preview times on all three upgrades
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/2333-queue-run.md and 2333-queue-run.csv; run 20261123T233428Z-44beec
  follow_up: food 546.1M for the Lv.28 ground; read the Lv.28 preview's food row exactly; the 6h 32m flat reduction cause is open
  stats:
    target: food T = 542M from the typed UR Food Chests
    achieved: food 546.1M
    resources_gained: food +410.1M from 101 chests
    points: 0
    costs: none spent; model 0.320677 USD
    verified: yes
    run_id: 20261123T233428Z-44beec
    run_steps: 24
    actions_done: 61
    actions_refused: 0
    cost_usd: 0.320677
    device_takeovers: 0
    food_before: 136.0M
    food_after: 546.1M
    chests_used: 101
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

## Brief (planner, FOOD chests for the Lv.28 ground start (B4), runs after the second ground start)

serves: PL-14

DISPATCH ONLY WHEN NAMED, between `building-queues-growth-convert-2026-11-24-001` (starts 1 and 2) and `-002`, when 001's note shows 'food row shown' on a ground preview (the 11-10 preview of Lv.25 to 26 read food 170.0M against iron 56.9M, a ratio of 3.0, so the Lv.28 row, about 442M, is probably real), or after `-002` stopped on food. If 001 shows no food row after scrolling, do not run. Decision `_records_/2026-11-22/strategy/dec-20261123-08.md`. It ends within 15 minutes of the claim. No Upgrade, no Complete.

Food T = the food row of the Lv.28 preview plus the 100M floor (default 542M = 442M + 100M); food NOW is read after the first two starts, so N is large (about 103).

HAZARD: the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: tap the intended tile first, confirm its name in a frame, never Use with another tile selected.

1. Read food now (the HUD or the Resources panel; tag text). Inventory, Resources tab: select the typed Food Chest UR; read its food value from the item panel (about 4.06M, about 103 owned). N = min(owned, ceil((T - food now) / that value)). Read the field AND the Total line in a frame before Use; Use once. Read food again.
2. Still below T after all the chests: STOP and record the shortfall. Write food before and after, and the last tap's UTC time.
Tag text beside every number; none means [G].
Cost cap, stated: 0.40 USD.
