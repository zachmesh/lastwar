---
title: Oil Well Level 20 To 30 Builder Chain 2900 2026-11-23
created: 2026-11-23T08:10:00-08:00
modified: 2026-11-23T16:58:00-08:00
level: L0
version: 1.3.0
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

Tag 'Oil Well Lv.20', about (1090,340) on the restored fresh frame at the north-east wall beside the grey tanks. Route: WORLD then BASE, drag (400,580) to (150,830), drag (660,470) to (390,620), tap the pumpjack near (572,740). The Lv.20 to 21 preview: output 1,200 to 1,260 an hour, power +4,200, iron 8.5M only, original time 19:50:38, effective time 09:20:18, Finish Now 456 diamonds (never). The job is Lv.20 to 30: ten levels, iron only, about 100M iron, ONE builder (one building takes one builder at a time).

## The flat reduction [M]

Every build measured on 2026-11-23 ended 23,520 s (6 h 32 min) before its preview: the Oil Well Lv.21 started 23:29:34.8Z, preview 09:20:18, panel end 2026-11-24T02:17:53Z; the Lv.26 and Lv.27 grounds the same (Steer A, to the second). A flat grant, cause unknown; research differs by 15,120 s from its button. Each next level's real end is its own preview effective time minus 23,520 s, read at the start.

## Hand-off rule

At each real finish the coordinator dispatches the next unit BY NAME. It presses Complete on the Oil Well entry in the hammer panel (never Speed Up or Finish Now), goes to the well by the route, reads the tag (stop if the level is wrong), reads the Upgrade preview, keeps iron above the 150M floor, presses Upgrade once, and writes the preview's effective time, the panel's end time in UTC and their difference in seconds (expected 23,520 s). The planner re-times the NEXT unit from that real end. A unit claimed before its upgrade finishes releases itself unrun; a release keeps the attempt, so each chain unit carries max_attempts 8 and priority 9 until it is due. No unit is claimed by ranking.

## Schedule

[2900-oil-well-chain.csv](2900-oil-well-chain.csv) holds each level's expected start and end, its unit and its window. Only Lv.21 (ends 02:17:53Z) is measured; the later ends are Decision 08's durations minus the flat reduction [G], from 07:53Z on 11-24 for Lv.22 to 11:01Z on 12-13 for Lv.30. Lv.22 is expected six minutes before the daily quiet window 08:00Z to 08:25Z: its Complete and the next Upgrade press finish before 08:00Z or wait for 08:25Z, or the coordinator asks for the one-line exception if the builder would idle over 15 minutes.
