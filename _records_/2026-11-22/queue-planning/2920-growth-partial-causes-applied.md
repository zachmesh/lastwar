---
title: Queue Planning The Coach's Three Growth Partial Causes Applied 2920 2026-11-23
created: 2026-11-23T08:30:00-08:00
modified: 2026-11-23T08:30:00-08:00
level: L0
version: 1.0.0
description: Planner pass applying the Coach's three causes of the 54 percent growth partial rate - locate-and-record units for the buildings still unlocated, a primary target and optional extras in the store reads, and the rule that a fill finding no idle slot closes DONE
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0830-partial-causes
trigger: Coach message 0813 (growth-partial-causes)
started_at: 2026-11-23T08:00:00-08:00
finished_at: 2026-11-23T08:30:00-08:00
verified: the tag index and the Coach's causes file read; the inbox searched; word counts under 450; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/coach/0813-growth-partial-causes.md and growth-partial-causes.csv
  - source: _records_/2026-11-22/growth/tag-index.csv
---

# The Coach's three causes applied, 2920

## 1. Targets not located

The tag index (28 rows) still holds the Builders Hut as 'not found' and the Tech Center as unlocated (at least Lv.30 by the HQ 31 green check); the Decoration Gallery is not in it and plan item PL-15 describes it as a screen reached by the Heroes screen, the HQ radial menu or Base customization. `scout-midday-locate-2026-11-23-001` (Tech Center), `-002` (Builders Hut) and `-003` (Decoration Gallery), 16:40Z to 03:30Z, priority 3, each do one job with no reading: find it, read the tag text (or the screen title) and write its position or route as a row in the tag index; not found after eight pans closes 'blocked by route' with the frames covered, so the next unit starts from them. The Oil Well, located today by two pans, is the model. The tent identity cause (the Hospital) is a stale index row: it reads Lv.20 there while the plunder runs read Hospital Lv.25 twice; the row needs a dated update from the operator or scribe.

## 2. Over-scoped reads

The five store reads (`scout-midday-growth-snapshot-2026-11-23-027` to `-031`) now open with a PRIMARY target that completes the unit (weapons 1 to 3, weapons 4 to 6, the UR roster, hero panels 4 to 6, panels 7 to 9) and mark the Backpack counts and the first three hero panels as optional extras whose absence does not make the unit partial.

## 3. Precondition absent or nothing to do

The five 11-24 fills now close DONE ('nothing to fill', slots_idle 0) when every slot is read and none is idle, as policy 2532 does for donations, and their stale builder lines now name the Oil Well chain. No promote unit is staged: it waits for its precondition event (an idle barracks with Drill Ground room), which does not exist before the new grounds finish; the Lv.27 batch collect unit at 19:58Z is the nearest event unit.
