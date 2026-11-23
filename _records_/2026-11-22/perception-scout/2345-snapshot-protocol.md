---
title: Growth snapshot protocol
created: 2026-11-23T07:50:00Z
modified: 2026-11-23T08:05:00Z
version: 1.1.0
description: Read-only snapshot protocol for Story 868 with routes, fields, stop rules and operator units
status: unverified
grounded_in:
  - source: scout seat reading of repository records for assignment A-20261123-0741-scout
---

# Growth snapshot protocol

Design only, no game input. Sidecars hold the [schemas](2345-snapshot-schemas.csv) and [unit briefs](2345-snapshot-units.csv). Every unit is read-only, at most 8 steps and 10 minutes, grounds each tap fresh and carries no older value.

## Parts and routes

| Part | Route (known means a prior live read) | Fields |
|---|---|---|
| a Power | HUD power figure, Power Details, scroll (known once) | every category |
| b Buildings | hammer panel, tap body, paw Details (known) | builders, levels |
| c Research | flask panel, TECH hub (known) | slots, tree percents |
| d Troops | tent, pistol, TRAIN UNITS; Drill Ground paw (known) | tier counts, cap |
| e Heroes | HEROES, list, detail page (known); stars, skills, weapon, gear, tier (unknown) | per hero |
| f Previews | green arrow Upgrade panel (known) | power, cost, time |

Ten core units, extensions P2, S1, S1b, C1, D1, D1b, A1 and optional O1, O2 are in the sidecar. Run T units and P2 right after the regular training unit. Refresh weekly, P1 also daily.

## Stop rules

- S1 Never press Upgrade, Finish Now, Speed Up, Construct, Research, Train, Hire, Complete, Claim, Quick Dispatch, Promote or Equip.
- S2 Read a diamond or price figure, never tap it.
- S3 Stop at any march, attack, rally, Arena or PvP surface.
- S4 Close any Confirm dialog with Cancel or X.
- S5 Close a preview only by X or left-edge swipe-back, never a low tap (one once hit Upgrade, +14,800 power).
- S6 Two failed taps on one target end the unit as partial.
- S7 No owner name or ID; skip profile and ranking screens.

## What the records already say

- Power Details on 2026-11-08 gave Hero 65.28M, Drone 5.81M, Building 10.29M of 149.85M, so 68.5M is in no record.
- Total Power swung on 2026-11-22: 149.57M at 10:12 PT, 147.97M at 10:59, 150.08M at 19:55, four times the 29-day net.
- A T10 batch of 793 at 1,647 power is 1.31M power for 5.5M iron, about 4 iron a power, against 9,700 for the Builders Hut. The Drill Ground cap (39,460 full on 2026-10-31) may bind, so T2 and F1 read it first. Unverified.
- Building levels conflict (HQ 26 to 30), so none is carried.

## Unknowns

Hero sub-pages, squad panel, Hospital and research node previews have no live read. Tent taps often missed.
