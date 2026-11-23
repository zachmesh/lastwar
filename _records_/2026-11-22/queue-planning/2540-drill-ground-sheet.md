---
title: Drill Ground Reference Sheet For The 09:20Z Builder Units 2540 2026-11-23
created: 2026-11-23T03:04:00-08:00
modified: 2026-11-23T04:24:00-08:00
level: L0
version: 1.4.0
description: The reference the builder units for 2026-11-24T09:20Z point at - the four Drill Grounds with tap points and the pan, the measured upgrade previews with their tag texts, the funding plan and the hazards; the conversion procedure and speed-up use are on sheet 2541
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0304-drill-ground-sheet
trigger: coordinator decision 2603 and the F1c previews
started_at: 2026-11-23T03:02:00-08:00
finished_at: 2026-11-23T03:04:00-08:00
verified: every figure copied from _records_/2026-11-22/growth/1054-f1c-drill-grounds.md and the decision 2603; sums recomputed
grounded_in:
  - source: _records_/2026-11-22/growth/1115-rc1-chest-limits.md
  - source: _records_/2026-11-22/growth/1054-f1c-drill-grounds.md
  - source: _records_/2026-11-22/growth/1047-f1b-drill-ground.md
  - source: _records_/2026-11-22/team-operations/2603-first-builder-decision.md
---

# Drill Ground sheet, 2540

## Where

Four parade fields of red soldiers; tap a soldier in the middle and read the tag. Fresh frame: Lv.26 about (705,690), Lv.28 about (580,800), Lv.30 about (770,940), Lv.27 about (975,845) off-screen right. Pan with a drag from (540,700) to (290,450); the fresh frame is the panned frame plus (250,250), give or take 60 px. The orange-roofed building is a Tavern. Each tap shifts the view 30 to 85 px.

## Measured previews [M], tag text from the F1c read

| Tag text | Step | Coin | Iron | Effective time | Power | Unit Count |
|---|---|---|---|---|---|---|
| Drill Ground Lv.26 | 26 to 27 | 59.5M | 74.8M | 10d 02:30:19 | +21,600 | +7,200 to +7,400 |
| Drill Ground Lv.27 | 27 to 28 | 83.3M | 102.0M | 14d 03:30:26 | +25,600 | +7,400 to +7,600 |
| Drill Ground Lv.28 | 28 to 29 | 119.0M | 144.5M | 18d 09:21:34 | +30,400 | +7,600 to +7,800 |
| Drill Ground Lv.30 | 30 to 31 | 178.5M | food 671.5M short | 26d 07:08:38 | +37,500 | out: needs Headquarters Lv.31 |

The three steps cost 261.8M coin and 321.3M iron.

## Funding plan [D], from the RC1 limits [M]

Keeps the coin in the base at the buffer and the 50M fixed-chest reserve. (a) Grounds 1 and 2, 59.5M + 83.3M = 142.8M: ONE Use of N UR Coin Chests, N = ceil((142.8M + 10M - coin now) / 2.4364M), which is 59 from 9.8M, 58 from 12M and 63 from 0.2M (59 x 2.4364M = 143.75M); stop if N would exceed 87. (b) Ground 3, 119.0M: ONE Use of M plain Resource Chests choosing the 6K COIN option, M = ceil((119.0M + 10M - coin now) / 6,000), about 19,709 from 10.75M (19,834 is the planning figure at the 15M baseline); stop if M would exceed 20,862. The slider is about 80 chests per pixel, so read the number field after the drag and accept 19,700 to 20,000; a miss of 1M coin is fine; the default 20,862 would be 125.2M, also acceptable if the drag fails, but say so. (c) After all three starts coin should read about 15M (floor 10M); fixed chests left: UR 28, SSR 71, SR 122, about 138M; the Builders Hut (guide about 22M coin) from SSR chests if the Strategist ranks it.

## Hazards

Never Upgrade on a builder running the owner's queue. Close a menu with an empty-ground tap such as (200,610); never tap WORLD at (660,940) with a menu open low, because the green Upgrade arrow can sit there. Never press Obtain.
