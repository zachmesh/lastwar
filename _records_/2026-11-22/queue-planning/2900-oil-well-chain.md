---
title: Oil Well Level 20 To 30 Builder Chain 2900 2026-11-23
created: 2026-11-23T08:10:00-08:00
modified: 2026-11-23T10:30:00-08:00
level: L0
version: 1.1.0
description: The facts, route, per level procedure and earliest finish schedule for the builder B1 chain that raises the Oil Well from level 20 to 30 from 2026-11-23T23:21Z, as units staged one per level
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

## Facts [M] from the operator record

Tag 'Oil Well Lv.20', about (1090,340) on the restored fresh frame, at the north-east wall beside the grey tanks. Route: WORLD then BASE, drag (400,580) to (150,830), drag (660,470) to (390,620), tap the pumpjack near (572,740). Preview 'Lv.20 to 21' (green arrow only): output 1,200 to 1,260 an hour, power 23,200 to 27,400 (+4,200), storage (Max Production Time) 10:40:00 to 10:48:00, cost iron 8.5M only (1.0G held; no coin, food or oil), prerequisites Lv.30 Headquarters and Lv.1 Unlock Oil Well both green, original time 19:50:38, the Upgrade button clock (the effective time) 09:20:18, Finish Now 456 diamonds (never). The old figure for Lv.1 to 30 (iron 638M, food 213M, coin 137M) does not apply: it is Lv.20 to 30, ten levels, iron only, about 100M iron and four to six days of ONE builder. One building is upgraded by one builder at a time, so the other builders need other buildings.

## Procedure per level

At each finish: press Complete on the Oil Well entry in the hammer panel (never Speed Up or Finish Now; power registers only on Complete), go to the well by the route, read the tag (stop if it is not the expected level), open the Upgrade preview, write iron cost, output, power, storage, the Upgrade button clock and the original time, keep iron above the 150M floor, press Upgrade once, read the timer to the second and write the finish time in UTC. The coordinator sets the trigger for the next level from that time. A chain unit claimed before its upgrade finishes releases itself unrun (`queue.py release`) and writes the time left.

## Earliest finish schedule (lower bound: every level takes at least 9 h 20 min 18 s, and later levels take longer)

| Level | Start at or after (Z) | Earliest finish (Z) |
|---|---|---|
| 20 to 21 | 11-23 23:21 | 11-24 08:41 |
| 21 to 22 | 11-24 08:41 | 11-24 18:01 |
| 22 to 23 | 11-24 18:01 | 11-25 03:21 |
| 23 to 24 | 11-25 03:21 | 11-25 12:42 |
| 24 to 25 | 11-25 12:42 | 11-25 22:02 |
| 25 to 26 | 11-25 22:02 | 11-26 07:22 |
| 26 to 27 | 11-26 07:22 | 11-26 16:43 |
| 27 to 28 | 11-26 16:43 | 11-27 02:03 |
| 28 to 29 | 11-27 02:03 | 11-27 11:23 |
| 29 to 30 | 11-27 11:23 | 11-27 20:44 |

CORRECTED 2026-11-23 18:13Z: the four builders are free at 23:20Z TODAY (the Training Base timers read 05:13:04 to 05:13:15 at 18:07Z), not 2026-11-24T09:20Z, so the whole chain starts 10 hours earlier than first written. The first finish, 08:41Z, falls 16 minutes after the daily quiet window 08:00Z to 08:25Z; no earliest finish falls inside it, but real finishes are later than these lower bounds, so a finish that lands in a window moves to the nearest edge or takes a one-line exception if the builder would idle more than 15 minutes.
