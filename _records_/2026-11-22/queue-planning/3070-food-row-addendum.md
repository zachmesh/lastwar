---
title: Queue Planning Addendum The Food Row Is Probably Real 3070 2026-11-23
created: 2026-11-23T14:55:00-08:00
modified: 2026-11-23T14:55:00-08:00
level: L0
version: 1.0.0
description: Dated addendum to note 3060 after Steer A's counter-evidence that the Drill Ground upgrades carry a food row - the plan for the food unit, the ground units and the Lv.28 retry
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-1455-food-addendum
trigger: Steer A message 22:41Z
started_at: 2026-11-23T14:42:00-08:00
finished_at: 2026-11-23T14:55:00-08:00
verified: the staged units read back and tested with the tool's forecast_class; word counts under 450; validate exit 0
grounded_in:
  - source: _records_/2026-11-10/alliance-train/0946-queue-run.md (as cited by Steer A, lines 46 to 48)
  - source: _records_/2026-11-22/queue-planning/3060-preconversion-food-and-wave-0203z.md
---

# Addendum to 3060: the food row is probably real, 3070

Note 3060 argued from three previews that showed no food row at the Lv.26 and Lv.28 grounds and called the decision's food figures guide estimates. Steer A points to a measured preview of the Lv.25 to 26 ground on 2026-11-10 that reads iron 56.9M, food 170.0M, a ratio of 3.0, the same as the guide-derived Lv.28 row (food 442M, iron 144.5M, ratio 3.06); my 1054 table has one column 'Iron or food' and may have recorded one of two rows. So the food row is probably real [G, supported by one measured row], and my claim that the food figures were estimates was too strong. Nothing is converted before the starts: the typed Food Chests stay safe unopened.

What is staged: the three ground units (`building-queues-growth-convert-2026-11-24-001`, `-002` and the new `-004`) read every cost row of each preview, scroll to its end, and write each row with its value and whether it was visible without a scroll, as [M], plus 'food row shown' or 'no food row after scrolling'; the food unit `building-queues-growth-preconvert-2026-11-23-003` is aimed at the Lv.28 ground start alone (T is its food row plus the 100M floor, default 542M) and runs between ground 001 and 002 when 001's note shows a food row; `-004` repeats the Lv.28 start after the conversion if `-002` stopped on food, because a stopped unit is consumed and I cannot wake myself to restage. B2 (221M) and B3 (314.5M) need 535.5M against about 660M held, so only the third start can stall.
