---
unit: trucks-settle-2026-11-23-001
regular: trucks
activity: truck-plunder
segment: 3
priority: 2
created_at: 2026-11-23T13:45:21Z
expires_at: 2026-11-23T16:00:00Z
planned_for:
not_before: 2026-11-23T14:20:00Z
window: own trade trucks settle and re dispatch no plunder contract floor 200
est_minutes: 10
serves: upkeep
chain_id: settle-2026-11-23
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-23T15:38:22Z
lease_until: 2026-11-23T15:58:22Z
result:
  status: done
  started_at: 2026-11-23T15:38:22Z
  finished_at: 2026-11-23T15:40:45Z
  duration_seconds: 143
  executor: operator
  summary: Three returned own trucks settled by one tap on slot 1 (truck 1 UR: iron 2.2M, food 2.2M, coin 1.4M, 500-badge shard x3, four 5m speed-up tiles, chest, gold bar; trucks 2 and 3 not read separately); HUD food 655.1M to 662.7M, coin 13.4M to 18.3M; Today's Trade Count 5/5 so no dispatch; Reward Recovery without a red dot not pressed; no plunder, no diamond
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/truck-plunder/1538-queue-run.md and 1538-queue-run.csv; run 20261123T153837Z-6003f6
  follow_up: next own-trucks settle at 00:30Z; the trade day resets 02:00Z; per-truck rarity and cargo of the second and third truck were not read
  stats:
    target: settle returned own trucks, claim Reward Recovery at a red dot, re-dispatch only if the count allows
    achieved: 3 trucks settled, no red dot on Recover, count 5/5 so no dispatch
    resources_gained: food 7.6M; coin 4.9M; truck 1 also 500-badge shard x3 and speed-up tiles
    points: 0
    costs: none spent; model 0.14502 USD
    verified: yes
    run_id: 20261123T153837Z-6003f6
    run_steps: 10
    actions_done: 25
    actions_refused: 0
    cost_usd: 0.14502
    device_takeovers: 0
    rules_used: 4,5
    rule_failed: none
    rule_gap: none
  stats_missing: []
  stats_warnings: []
---

# trucks

Produced by _tools_/queue.py. The executor reads the activity metadata and the standing rules before acting.

Serves: upkeep

## Brief (planner, own trade trucks settle and re-dispatch, no plunder, coordinator 13:44Z)

serves: upkeep

Own trucks only. The trade trucks came home from 13:34Z (the UR truck about 13:45Z, the last about 14:18Z) and there is no own-trucks settle unit until 00:30Z. Open Intercity Trade by the left-column vehicle icon (entry as in `_records_/2026-11-22/truck-plunder/0953-queue-run.md`). Settle every returned truck by opening its Truck Details, claim Reward Recovery at the red dot, read Today's Trade Count, then dispatch to fill the slots by the truck-plunder profile's standing rules (`_activities_/truck-plunder/rule-digest.md`, rules 2 to 6): SR or above as rolled; on a UR duel day only UR, in Mega Mode; below SR take the one Free refresh, then Trade Contract refreshes.

CONTRACT FLOOR: 200 Trade Contracts must remain; 266 were held at the last read, each refresh costs 1, so at most about 66 refreshes. Read the contract count before every refresh and stop at 200. Never a diamond refresh or any price in diamonds or money; no speed-up.

No Plunder of other players' trucks in this unit; the plunder sessions are separate units. A TIPS dialog about another device: STOP and report, never Confirm. Close menus with the bare spot (310,660) (not (400,640) after a camera shift); never WORLD with a menu open low. Write per truck its rarity, cargo and the dispatch time to the second. Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`. No chain successor.
Cost cap, stated: 0.60 USD (the harness stops near 0.36 of it).
