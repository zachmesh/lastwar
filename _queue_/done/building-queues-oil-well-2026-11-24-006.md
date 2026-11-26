---
unit: building-queues-oil-well-2026-11-24-006
regular: building-queues
activity: building-queues
segment: 1
priority: 9
created_at: 2026-11-23T16:00:30Z
expires_at: 2026-11-26T19:09:41Z
planned_for:
not_before: 2026-11-26T07:09:41Z
window: oil well level 25 to 26 builder b1 chain complete the previous level and start this one
est_minutes: 12
serves: PL-17
chain_id: oil-well-2026-11-24
chain_seq: 6
attempts: 1
max_attempts: 8
claimed_by: operator
claimed_at: 2026-11-26T13:12:01Z
lease_until: 2026-11-26T13:32:01Z
result:
  status: partial
  started_at: 2026-11-26T13:12:01Z
  finished_at: 2026-11-26T13:19:11Z
  duration_seconds: 430
  executor: operator
  summary: Oil Well: the finished Lv.25 job (ended 13:09:56Z, no hammer row, one builder idle) completed by tapping the wrapped gift box (13:17:34.5Z): OIL WELL LEVEL UP (Power 51,500 to 60,800, oil 1,500 to 1,560 an hour, Total Power +9,300 to 151,689,455); the tag then reads Oil Well Lv.26, not Lv.25, so the unit's step is already done: stopped without a preview or Upgrade (the next upgrade is Lv.26 to 27); an unintended Collect on the oil-barrel bubble (oil 585.7K to 587.0K) disclosed; drags 3. state_change: yes
  claimed: []
  claimed_count: 0
  evidence: _records_/2026-11-22/building-queues/1311-queue-run.md and 1311-queue-run.csv; run 20261126T131725Z-7e537b
  state_change: yes
  follow_up: a Lv.26 to 27 hand-off unit (one builder idle); the help icon look waits for an Upgrade
  stats:
    target: complete the well and press Lv.25 to 26 once
    achieved: well completed; the tag reads Lv.26: no Upgrade
    resources_gained: none
    points: 0
    costs: none spent; model 0.501095 USD
    verified: yes
    run_id: 20261126T131725Z-7e537b
    run_steps: 38
    actions_done: 13
    actions_refused: 0
    cost_usd: 0.501095
    device_takeovers: 0
    claims: 1
    total_power_before: 151680155
    total_power_after: 151689455
    tag: Oil Well Lv.26
    blocker_category: tag differs: the well is already Lv.26; the next upgrade Lv.26 to 27 is not this unit
    tram_badge: not read
    drags_tried: 3
    rules_used: 1,2
  stats_missing: []
  stats_warnings: [blocker_category not in enum a-i]
---

# building-queues

Oil Well hand-off, builder B1. Definition `_activities_/building-queues/` (its `rule-digest.md` first); routes `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.

## Brief (planner, builder B1: Oil Well Lv.25 to 26, PL-17)

Route: `_records_/2026-11-22/queue-planning/2900-oil-well-chain.md`. Starts at the Oil Well finish, dispatched by name. FIRST read the Oil Well entry in the hammer panel (hammer opens nothing: routes table, never a fourth tap): if it reads 'Oil Well Lv.26' (another hand started it) do NOT release: close a verified nothing-to-do with a `state_read:` line (the panel, its timer); if the Lv.25 job still has more than 5 minutes left, write the time and RELEASE this unit unrun. If finished: the well completes by TAPPING THE WRAPPED GIFT BOX on the building (no Complete button; never Speed Up or Finish Now); Total Power before and after. Go to the well by the route in the sheet, read the tag ('Oil Well Lv.25'; stop and report if it differs), open the Upgrade preview ('Lv.25 to 26') and write iron cost, the Upgrade button clock (effective time) and the original time; keep iron above the 150M floor; press Upgrade ONCE; read the timer to the second; write the effective time, the SPEED FACTOR (original over effective), the panel's end time in UTC. HELP ICON LOOK (Steer A 12:36Z), RIGHT AFTER THE UPGRADE PRESS: take a 6x crop of the area above the Oil Well and, after ONE pan from blank ground (about 175 px, one message, back by WORLD then BASE), above the upgrading Drill Ground, and WRITE EACH BUBBLE'S GLYPH BY DESCRIPTION (a hand, a hammer, a figure, a number) AND ANY COUNT. A bubble with a HAND or the text 'Help' that shows no count or 'requested': PRESS IT ONCE (the bubble rule is lifted for this press only); read that build's end time to the second before, at +1 and at +10 minutes, with any help count. No hand: press nothing. NEVER the green up arrow (the upgrade shortcut), NEVER Speed Up.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the Upgrade pressed or a verified nothing-to-do (`--state-change no`, a `state_read:` line); else PARTIAL.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.90 USD.
