---
title: Oil Well Level 20 To 30 Builder Chain 2900 2026-11-23
created: 2026-11-23T08:10:00-08:00
modified: 2026-11-23T18:50:00-08:00
level: L0
version: 1.5.0
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

Tag 'Oil Well Lv.20', about (1090,340) on the restored fresh frame at the north-east wall beside the grey tanks. Route: WORLD then BASE, drag (400,580) to (150,830), drag (660,470) to (390,620), tap the pumpjack near (572,740); drag ONCE per frame and check the frame after each drag (a double drag cost two runs). The job is Lv.20 to 30: ten levels, iron only, about 100M iron, ONE builder.

## The flat reduction [M]

Every build measured so far ended 23,520 s (6 h 32 min) before its preview, to within 2 s, five times (three Drill Ground builds, two Oil Well): Lv.21 started 23:29:34.8Z, preview 09:20:18, ended 02:17:53Z; Lv.22 started 02:25:21.9Z, preview 12:08:24, panel 05:35:48, ends 08:01:45.8Z. A flat grant, cause unknown; research differs by 15,120 s from its button. Each next level's real end is its own preview effective time minus 23,520 s, read at the start.

## Hand-off rule

At each real finish the coordinator dispatches the next unit BY NAME. A finished well completes by TAPPING THE WRAPPED GIFT BOX on the building (no Complete button in the panel; Total Power registers then). Then: the route, the tag (stop if the level is wrong), the Upgrade preview, iron above the 150M floor, Upgrade once, and write the preview's effective time, the panel's end time in UTC and their difference in seconds. The planner re-times the NEXT unit from that real end. A unit claimed before its upgrade ends releases itself unrun and the release keeps the attempt, so each carries max_attempts 8 and priority 9 until it is due. Lv.21 cost 7.48 idle builder minutes (the gift box, two lost runs).

## Schedule

[2900-oil-well-chain.csv](2900-oil-well-chain.csv) holds each level's expected start and end, unit and window. Lv.21 and Lv.22 are measured; later ends are Decision 08's durations minus 23,520 s [G]. Lv.22 ends 08:01:46Z, 1.8 minutes inside the quiet window 08:00Z to 08:25Z, so the next hand-off opens at 08:25:30Z and finishes before 09:45Z (23 idle minutes, about 280 power-equivalent, accepted).
