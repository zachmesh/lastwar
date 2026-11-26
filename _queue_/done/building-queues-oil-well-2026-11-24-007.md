---
unit: building-queues-oil-well-2026-11-24-007
regular: building-queues
activity: building-queues
segment: 1
priority: 1
created_at: 2026-11-23T16:00:31Z
expires_at: 2026-11-27T02:00:00Z
planned_for:
not_before: 2026-11-26T07:35:50Z
window: oil well level 26 to 27 builder b1 chain complete the previous level and start this one
est_minutes: 12
serves: PL-17
chain_id: oil-well-2026-11-24
chain_seq: 7
attempts: 1
max_attempts: 8
claimed_by: operator
claimed_at: 2026-11-26T13:28:09Z
lease_until: 2026-11-26T13:48:09Z
result:
  status: done
  started_at: 2026-11-26T13:28:09Z
  finished_at: 2026-11-26T13:40:08Z
  duration_seconds: 719
  executor: operator
  summary: Oil Well Lv.26 to 27 started (Upgrade once at 13:31:34.0Z; ends 2026-11-28T19:37:10Z; effective 2d 12:37:36, original 5d 08:49:52, speed factor 2.125); the preview's coin and food cost rows were hidden because the cost list was not dragged: iron -56.1M, food -18.7M, coin -11.9M (coin now 4.0M, below the 10M floor: a floor breach disclosed and booked); the help icon look: no hand or Help above the well or the Drill Grounds, nothing pressed; the tram icon shows a red dot from 13:33:54.8Z (not entered); drags 7. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/1328-queue-run.md and 1328-queue-run.csv; run 20261126T132809Z-138826
  state_change: yes
  follow_up: coin 4.0M (below the 10M floor); from now on drag every preview's cost list until all rows are visible; the trade entry (tram red dot)
  stats:
    target: start the Oil Well Lv.26 to 27 once with the floors held
    achieved: upgrade started; coin floor breached
    resources_gained: iron -56.1M, food -18.7M, coin -11.9M
    points: 0
    costs: none spent; model 0.735317 USD
    verified: yes
    run_id: 20261126T132809Z-138826
    run_steps: 56
    actions_done: 26
    actions_refused: 0
    cost_usd: 0.735317
    device_takeovers: 0
    claims: 1
    oil_well_end_utc: 2026-11-28T19:37:10Z
    speed_factor: 2.125
    coin_after: 4.0M
    floor_breach: coin
    tram_badge: red dot
    drags_tried: 7
    rules_used: 1,2
  stats_missing: []
  stats_warnings: []
---

# building-queues

Definition `_activities_/building-queues/`; routes `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.

## Brief (planner, builder B1: Oil Well Lv.26 to 27, PL-17)

Dispatched by name. FIRST read the Oil Well entry in the hammer panel: the queue row 'Lv.N upgrade in progress' names the level being upgraded FROM: a row 'Lv.26 upgrade in progress' or a tag 'Oil Well Lv.27' means another hand started it: do NOT release: close a verified nothing-to-do with a `state_read:` line. Go to the well by the route in the sheet: the oil-barrel bubble over it is a COLLECT, never tap it, tap the building below it. Read the tag ('Oil Well Lv.26'; stop and report if it differs) and open the Upgrade preview ('Lv.26 to 27'): write coin, iron, food, oil, the effective time (the Upgrade button clock), the original time and the power gained, with the stocks in the SAME frame. Press Upgrade ONCE, ONLY if every stock stays at or above coin 10M, iron 100M and food 30M after the cost and no diamond price shows; a shortfall may be covered ONLY by the typed fixed chests per sheet `2542-drill-ground-preconvert-rules.md` (never choice chests); if they do not cover it: DO NOT press, write the preview and STOP. After the press read the timer to the second; write the effective time, the SPEED FACTOR (original over effective) and the panel's end time in UTC.
HELP ICON LOOK (Steer A 12:36Z), RIGHT AFTER THE PRESS: a 6x crop of the bubbles above the Oil Well and, after ONE pan from blank ground (about 175 px), above the upgrading Drill Ground: WRITE EACH BUBBLE'S GLYPH BY DESCRIPTION (hand, hammer, figure) AND ANY COUNT. A bubble with a HAND or the text 'Help' and no count or 'requested': PRESS IT ONCE, then read that build's end time to the second before, at +1 and at +10 minutes, with any help count. No hand: press nothing. NEVER the green up arrow, NEVER Speed Up or Finish Now.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the Upgrade pressed or a verified nothing-to-do (`--state-change no`, a `state_read:` line); else PARTIAL.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.90 USD.
