---
unit: building-queues-oil-well-2026-11-24-010
regular: building-queues
activity: building-queues
segment: 1
priority: 9
created_at: 2026-11-23T16:00:34Z
expires_at: 2026-12-07T00:21:43Z
planned_for:
not_before: 2026-12-06T04:21:43Z
window: oil well level 29 to 30 builder b1 chain complete the previous level and start this one
est_minutes: 8
serves: PL-17
chain_id: oil-well-2026-11-24
chain_seq: 10
attempts: 0
max_attempts: 8
claimed_by:
claimed_at:
lease_until:
---

# building-queues

Definition `_activities_/building-queues/`; routes `_records_/2026-11-22/queue-planning/2700-route-card-and-stop-reasons.md`.

## Brief (planner, builder B1: Oil Well Lv.29 to 30, PL-17)

FIRST read the Oil Well entry in the hammer panel: the queue row 'Lv.N upgrade in progress' names the level being upgraded FROM: a row 'Lv.29 upgrade in progress' or a tag 'Oil Well Lv.30' means another hand started it: do NOT release: close a verified nothing-to-do with a `state_read:` line. If the Lv.28 job still has more than 5 minutes left, write the time and RELEASE this unit unrun. If finished: the well completes by TAPPING THE WRAPPED GIFT BOX on the building (never Speed Up or Finish Now). Go to the well by the route in the sheet: the oil-barrel bubble over it is a COLLECT, never tap it, tap the building below it. Read the tag ('Oil Well Lv.29'; stop and report if it differs) and open the Upgrade preview ('Lv.29 to 30'). DRAG THE COST LIST until EVERY row is visible (iron, food, coin, oil), then write every cost row, the effective time, the original time and the power gained, with the stocks in the SAME frame. Press Upgrade ONCE, ONLY if every stock stays at or above coin 10M, iron 100M and food 30M after the cost, checked against ALL rows AND the table's expected cost at 0.85 (Lv.29 to 30: iron 153.0M, food 51.0M, coin 33.1M; a charged row can hide even after a drag: 2541), and no diamond price shows; a shortfall may be covered ONLY by the typed fixed chests per sheet `2542-drill-ground-preconvert-rules.md` (never choice chests); if they do not cover it: DO NOT press, write the preview and STOP. After the press read the timer to the second; write the effective time, the SPEED FACTOR and the panel's end time in UTC. NEVER the green up arrow, NEVER Speed Up or Finish Now. If any cost row was NOT seen: DO NOT press, write what was seen and STOP.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the Upgrade pressed or a verified nothing-to-do (`--state-change no`, a `state_read:` line); else PARTIAL.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 0.60 USD.
