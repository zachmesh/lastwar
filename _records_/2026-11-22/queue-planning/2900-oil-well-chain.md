---
title: Oil Well Level 20 To 30 Builder Chain 2900 2026-11-23
created: 2026-11-23T08:10:00-08:00
modified: 2026-11-26T04:50:00Z
level: L0
version: 1.11.0
description: The facts, route, hand-off rule and current schedule pointer for the builder B1 chain that raises the Oil Well from level 20 to 30, with the per level table in a CSV beside it
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0810-oil-well-chain
trigger: coordinator message 16:00Z with the Oil Well found at level 20
started_at: 2026-11-23T07:58:00-08:00
finished_at: 2026-11-23T08:10:00-08:00
verified: preview numbers copied from the operator record 1553-oil-well-found as relayed; the schedule computed by script from the first level's effective time; none of it read by me on screen
grounded_in:
  - source: _records_/2026-11-22/resource-collection/1553-oil-well-found.md (as relayed by the coordinator at 16:00Z)
---

# Oil Well level 20 to 30 chain, 2900

## Facts [M]

Tag 'Oil Well Lv.20', about (1090,340) on the restored fresh frame at the north-east wall. Route: WORLD then BASE, drag (400,580) to (150,830), drag (660,470) to (390,620), tap the pumpjack near (572,740); drag ONCE per frame and check the frame after each drag (a double drag cost two runs). The job is Lv.20 to 30: ten levels, iron only, about 100M iron, ONE builder.

## The flat reduction [M]

Every build measured so far ended 23,520 s (6 h 32 min) before its preview, to within 2 s, seven times (three Drill Ground builds, four Oil Well; the per-level times are in the CSV). A flat grant, cause unknown; research differs by 15,120 s from its button. Each next level's real end is its own preview effective time minus 23,520 s, read at the start.

## Hand-off rule

At each real finish the coordinator dispatches the next unit BY NAME. A finished well completes by TAPPING THE WRAPPED GIFT BOX on the building (no Complete button in the panel; Total Power registers then). Then: the route, the tag (stop if the level is wrong), the Upgrade preview, iron above the 150M floor, Upgrade once, and write the preview's effective time, the panel's end time in UTC and their difference in seconds. The planner re-times the NEXT unit from that real end. A unit claimed before its upgrade ends releases itself unrun and the release keeps the attempt, so each carries max_attempts 8 and priority 9 until it is due.

## Schedule

[2900-oil-well-chain.csv](2900-oil-well-chain.csv) is the start log: each level's start, end, unit, window, `speed_factor` and `last_game_restart_utc`. Lv.21 to Lv.24 are measured: Lv.23 ended 17:27:27Z, Lv.24 started 17:31:42Z and REALLY ENDS 2026-11-25T07:11:20Z. CORRECTED 2026-11-26T13:23Z: the builders row 'Lv.N upgrade in progress' names the level upgraded FROM. The job read at 04:41Z (Time Left 08:28:12) was Lv.25 to 26: it ended 13:09:56.4Z and was completed 13:17:34.5Z (tag Oil Well Lv.26, +9,300 power, oil 1,500 to 1,560 an hour); -006 stopped. -007 (Lv.26 to 27, priority 1) is live for the idle builder; Lv.27 to 30 were shifted by 32:59:51, expiries 20 h after the floors; the planner re-times from each real end. The hand-off unit opens 2 minutes before a real end; no opening in the quiet window 08:00Z to 08:25Z.


## HQ 31 start unit, pre-steps (not staged)

Steer A, 2026-11-24 16:52Z: oil is the binding resource of the HQ 31 path (gate 1.2M; 687K held; the well 1,536 an hour). The HQ 31 start unit's pre-steps include 'use all oil items' (the barrels and the depot's 6.0K items): a typed Use, verified to add its label to the HUD, used just in time (when the counter would be short for the start, or the stack is large). The Backpack oil stock is unread (Resources row 4 cut off). The unit starts only when all gates are met (oil, food, coin, iron, a free builder).
