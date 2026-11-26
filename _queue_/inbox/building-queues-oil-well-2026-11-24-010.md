---
unit: building-queues-oil-well-2026-11-24-010
regular: building-queues
activity: building-queues
segment: 1
priority: 9
created_at: 2026-11-23T16:00:34Z
expires_at: 2026-12-05T12:17:14Z
planned_for:
not_before: 2026-12-04T16:17:14Z
window: oil well level 29 to 30 builder b1 chain complete the previous level and start this one
est_minutes: 12
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

Definition `_activities_/building-queues/`.

## Brief (planner, builder B1: Oil Well Lv.29 to 30, PL-17)

Read the Oil Well entry in the hammer panel ('Lv.N upgrade in progress' names the level upgraded FROM): a row 'Lv.29 upgrade in progress' or a tag 'Oil Well Lv.30' means another hand started it: do NOT release: close a verified nothing-to-do (`state_read:`). If the Lv.28 job has over 5 minutes left, write the time and RELEASE unrun. If finished: TAP THE WRAPPED GIFT BOX.
COIN FIRST: open the top-bar coin panel, read Available, tap Collect ONCE, confirm Owned moved, read the HUD coin.
Go to the well by the route in the sheet (the oil-barrel bubble over it is a COLLECT: never tap it, tap the building below). Read the tag ('Oil Well Lv.29'; else stop and report), open the preview ('Lv.29 to 30') and DRAG THE COST LIST until EVERY row is visible: write every row, the effective time, the power gained and the stocks in the SAME frame. Table cost at 0.85: iron 153.0M, food 51.0M, coin 33.1M.
Press Upgrade ONCE, ONLY if after the cost every stock stays at or above coin 10M, iron 100M and food 30M by BOTH the table and ALL rows seen, and no diamond price shows. If a row was NOT seen or a floor would break: use NO chest (zero; never the R5), DO NOT press, write the table's total and the stocks, RELEASE unrun. After the press: the timer to the second, the effective time, the SPEED FACTOR, the end time in UTC.
HELMET (Steer A 14:04Z): right after the press, a 6x crop of the bubbles above the well: a white round bubble with a green helmet: press it ONCE (no other bubble); read the end time to the second before, at +1 and at +10 minutes; a price, gem, Speed Up or Upgrade dialog: close by its X. NEVER the green up arrow, Speed Up or Finish Now.
CLOSE by `_records_/2026-11-22/queue-planning/3170-closing-rule-done-and-partial.md`: DONE for the Upgrade pressed or a verified nothing-to-do (`--state-change no`, a `state_read:` line); else PARTIAL.
FRONT: if `lsappinfo front` is not LastWar: record, run the standing front script, record; still not: stop, release, tell the Coordinator.
May open another app: any banner, Go, Buy, link, web or share button needs Steer A's approval first; if another app opens, STOP and touch nothing.
Cost cap, stated: 1.20 USD.
