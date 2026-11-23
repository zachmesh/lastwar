---
title: Queue Planning Three Fixes Tap Point Chest Counts And The Speed Factor 2680 2026-11-23
created: 2026-11-23T05:22:00-08:00
modified: 2026-11-23T05:22:00-08:00
level: L0
version: 1.0.0
description: Planner pass on the three fixes from the 1308 read - the empty-ground tap point replaced in every unclaimed unit and my sheets, the coin tables re-baselined for the Coin Chests the other device used, and the research speed factor noted
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0522-three-fixes
trigger: coordinator message 13:15Z, operator record 1308
started_at: 2026-11-23T05:15:00-08:00
finished_at: 2026-11-23T05:22:00-08:00
verified: every inbox unit searched for the old point before and after; chest totals recomputed; validate exit 0
grounded_in:
  - source: operator record 1308-hq31-prereq-read as relayed by the coordinator
---

# Three fixes, 2680

## 1. Tap point

The empty-ground tap point (200,610) is a Gold Mine Lv.28 that opens its menu; the safe point is (400,640). Replaced in all 19 unclaimed inbox units that carried it, after a search showed none was claimed, and in my sheet [2540](2540-drill-ground-sheet.md) (now 1.5.0, with a note naming the old point) and in the conversion rules. The sheet [2541](2541-conversion-and-speedup-sheet.md) and the oil sheet 2650 never named it. Left as written because they are records of what was done: the operator's records 1030, 1308 and 0054, the tag index, the run-state file, and three finished units. The scout's units finished before the fix still say (200,610) in their text.

## 2. Coin tables

The other device used the barrels (210K oil), the small coin tiles and 82 SR Coin Chests (122 to 40). The fixed Coin Chests are now UR 87 (211.97M, Total line read), SSR 71 (57.66M) and SR 40 (4.06M), about 273.7M. With the plain Resource Chests at 20,862 (125.17M), the coin I can plan on from reads is about 398.9M, down from 406.0M. `2410-coin-supply.csv` has the new planning row and the new chest row, with the earlier two marked superseded, and the conversion rules and sheet 2540 carry the new counts. Coin on hand was 55,963 at the last read.

## 3. Research speed factor

The tech speed-up items (the blue-disc type) lost 3,960 minutes to the other device, leaving 11,400, and the research speed divisor M is about 2.2, not 4.6, so research is lab-bound again. The two Complete units for 2026-11-24 (14:59:30Z and 17:30:10Z) are unchanged on the coordinator's word; they still say tech stock at least 15,360 minutes and keep the general reserve until M is read, which is now out of date but harmless because they read the panel first.
