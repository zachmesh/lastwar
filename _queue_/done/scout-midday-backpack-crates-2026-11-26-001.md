---
unit: scout-midday-backpack-crates-2026-11-26-001
regular: scout-midday
activity: perception-scout
segment: 2
priority: 2
created_at: 2026-11-26T12:49:56Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T14:10:00Z
window: backpack crate measurement, three crates one use each (coordinator 12:52z)
est_minutes: 12
serves: snapshot
chain_id: backpack-crates-2026-11-26
chain_seq: 1
attempts: 1
max_attempts: 3
claimed_by: operator
claimed_at: 2026-11-26T14:44:16Z
lease_until: 2026-11-26T15:04:16Z
result:
  status: partial
  started_at: 2026-11-26T14:44:16Z
  finished_at: 2026-11-26T14:54:01Z
  duration_seconds: 585
  executor: operator
  summary: Backpack: speed-up stacks read (construction 5m 24,829 and 1m 19,640; general 8h 94 to 1m 25,725); one SR chest each used at quantity 1: Food Chest (SR) 169.20K food, Iron Chest (SR) 169.20K iron, Coin Chest (SR) 101.52K coin (coin 9.2M to 9.3M); one '6.0K Oil' barrel used (stack 15 to 14, oil 587.0K to 593.0K, +6.0K as expected); the other four barrels not used (stopped at the 0.80 cost cap, 0.746 spent); the Backpack left open with the quantity at 4; the diamond tile and choice chests untouched; drags 5. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/perception-scout/1453-queue-run.md and 1453-queue-run.csv; run 20261126T145133Z-d569ef
  state_change: yes
  follow_up: four oil barrels still to use (stack 14, quantity field 4, Total 24.00K, the Backpack open on the Resources tab); coin 9.3M is 0.7M under the 10M floor
  stats:
    target: read the speed-up stacks; use one iron, food and golden crate and up to five oil barrels
    achieved: three chests and one barrel used; four barrels pending
    resources_gained: none
    points: 0
    costs: none spent; model 0.745719 USD
    verified: yes
    run_id: 20261126T145133Z-d569ef
    run_steps: 69
    actions_done: 38
    actions_refused: 0
    cost_usd: 0.745719
    device_takeovers: 0
    claims: 4
    oil_rise: 6.0K
    coin_after: 9.3M
    oil_after: 593.0K
    blocker_category: cost cap reached before the last four barrels
    drags_tried: 5
    rules_used: 1,2
  stats_missing: []
  stats_warnings: [blocker_category not in enum a-i]
---

# scout-midday

Serves: snapshot

## Brief (definition pointer, from the roster)

One-off Backpack crate measurement (not the midday walk); definition `_activities_/perception-scout/`; routes `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.

## Brief (planner, BACKPACK CRATES AND BARRELS, plan reason: dig price and oil gap; Steer A 12:24Z and 12:50Z)

serves: snapshot

Open Inventory. HAZARD: the Resources tab opens with the 5,000 Diamonds x16 tile SELECTED and a live Use: NEVER tap that tile, and NEVER press Use while any tile other than the intended item is selected. If an item is not in view, pan from the CENTRE of a gap between tiles (about (274,448); a margin start moves nothing): one message per pan (press, hold 1 s, ONE move of about 175 px, hold 1 s, release, screenshot), at most three pans.
FIRST one frame of the construction speed-up stacks (8h, 1h, 5m, 1m): write each count, no tap (the BEFORE read). CRATES, IN ORDER: ONE iron crate, ONE food crate, ONE golden crate. For EACH: select by ICON AND NAME and read the name in the panel BEFORE any Use; the quantity defaults to the FULL stock: reduce it to ONE and read the number field; HUD iron, food, coin and oil before and after EACH Use. A name or quantity unreadable, a price or a choice: DO NOT press.
OIL BARRELS (plain free Use), after the crates: select the Oil Depot's '6.0K Oil' item by icon and name and write the stack's count. Use at most FIVE barrels in all, whatever the count. Use ONE barrel first and read the HUD oil before and after: it must rise by 5.9K to 6.1K (the HUD shows 0.1K). If so, Use the other four (one at a time or quantity 4; no price or gem icon): the HUD must then be up 23.9K to 24.1K. If the first Use does NOT raise the HUD: STOP, write what the dialog said, use nothing else.
NEVER a Resource Choice Chest, NEVER more than ONE of a CRATE stack, diamonds, speed-ups or any other tile.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the Uses read (`--state-change yes`, a `state_read:` line); else PARTIAL.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.80 USD.
