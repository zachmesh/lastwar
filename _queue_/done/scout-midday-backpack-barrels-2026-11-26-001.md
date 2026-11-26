---
unit: scout-midday-backpack-barrels-2026-11-26-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 1
created_at: 2026-11-26T15:05:17Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T15:12:00Z
window: backpack barrels, all remaining 6.0k oil barrels (steer a 15:04z)
est_minutes: 8
serves: snapshot
chain_id: backpack-barrels-2026-11-26
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T15:13:01Z
lease_until: 2026-11-26T15:33:01Z
result:
  status: done
  started_at: 2026-11-26T15:13:01Z
  finished_at: 2026-11-26T15:15:14Z
  duration_seconds: 133
  executor: operator
  summary: Backpack barrels: the general speed-up counts read without a tap (8h 94, 3h 266, 1h 1,196, 15m 1, 5m 32,858, 1m 25,725: unchanged since 14:44Z); the 6.0K Oil stack of 10 used in one Use at quantity 10: oil 618.2K to 678.2K (+60.0K, exact), the stack empty; fifteen barrels in all; the Backpack closed; the diamond tile and every other tile untouched; drags 3. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1513-queue-run.md and 1513-queue-run.csv; run 20261126T151301Z-e39885
  state_change: yes
  follow_up: the oil stock is 678.2K; the Backpack's selection can move to a live '600 Coins' tile after a Use (never pressed)
  stats:
    target: use all the oil barrels
    achieved: ten barrels used (fifteen in all)
    resources_gained: oil 60.0K
    points: 0
    costs: none spent; model 0.180256 USD
    verified: yes
    run_id: 20261126T151301Z-e39885
    run_steps: 13
    actions_done: 9
    actions_refused: 0
    cost_usd: 0.180256
    device_takeovers: 0
    claims: 1
    barrel_count_before: 10
    barrel_count_after: 0
    oil_rise: 60.0K
    oil_after: 678.2K
    drags_tried: 3
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# scout-midday

Serves: snapshot

## Brief (definition pointer, from the roster)

One-off Backpack barrel Use (not the midday walk); definition `_activities_/perception-scout/`.

Routes and stop reasons: `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md` (routes in `_records_/2026-11-22/queue-planning/2700-routes.csv`). Red lines and snap: `_records_/2026-11-22/team-operations/2350-growth-start-rule-decision.md`.

## Brief (planner, BACKPACK BARRELS, plan reason: oil is the binding resource; Steer A 15:04Z)

serves: snapshot

Open Inventory. HAZARD: the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: NEVER tap that tile, and NEVER press Use while any tile other than the Oil Depot barrel is selected. If the barrel item is not in view, pan from the CENTRE of a gap between tiles (about (274,448)): one message per pan (press, hold 1 s, ONE move of about 175 px, hold 1 s, release, screenshot), at most three pans.
FIRST one frame of the general speed-up counts (8h, 3h, 1h, 15m, 5m, 1m): write each count, no tap on an item (the before and after line for the cause of the 04:41Z shift).
OIL BARRELS (a plain free Use): select the Oil Depot's '6.0K Oil' item by icon and name, write the stack's count N (14 or 10 expected) and read the HUD oil. If N is 10 or fewer: Use ALL N in ONE Use (quantity N); if N is above 10: Use 4 first, then the rest. Read the quantity field before each Use and the HUD oil after it: it must rise by the quantity times 6.0K within one display step (0.1K). A price, a gem or diamond icon on a dialog, a deviation, or a name or quantity that cannot be read: DO NOT press, STOP and write what the dialog said. NEVER a Resource Choice Chest, NEVER any other tile, diamonds or speed-ups.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the Uses read (`--state-change yes`, a `state_read:` line); else PARTIAL.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.40 USD.
