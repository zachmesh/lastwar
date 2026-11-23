---
title: Drill Ground re-read F1b
created: 2026-11-23T10:57:00Z
modified: 2026-11-23T10:57:00Z
version: 1.0.0
description: Unit scout-midday-growth-snapshot-2026-11-23-024 - four Drill Grounds read (Lv.26, Lv.28, Lv.30, Lv.27) as parade fields; the Lv.28 ground exists and its Lv.29 upgrade costs 119.0M coin, 144.5M iron, 18d 09:21:34, +200 Unit Count per level
status: done
grounded_in:
  - source: cu_bridge runs 20261123T104804Z-ddd02d (a Tavern tapped, nothing pressed) and 20261123T105007Z-a1ecef, events, final result and frames step-0007 and step-0010, 2026-11-23T10:48Z to 10:52Z
  - source: unit brief scout-midday-growth-snapshot-2026-11-23-024 (F1b) and coordinator assignment A-20261123-1047-operator
---

# Drill Ground re-read F1b

Rows in [1047-f1b-drill-ground.csv](1047-f1b-drill-ground.csv). The base map put two Drill Grounds off-screen; there
are **four**, and each is a **parade field of red soldiers** (tap a soldier in the middle of the field), not
the orange-roofed building inside (a Tavern Lv.20) or the purple crystal building.

| Field (panned frame after the drag) | Tag | Approx. fresh-frame point |
|---|---|---|
| 1, upper | Drill Ground **Lv.26** | 705,690 |
| 2, left | Drill Ground **Lv.28** | 580,800 |
| 3, lower middle | Drill Ground **Lv.30** | 770,940 |
| 4, right | Drill Ground **Lv.27** | 975,845 |

- **Lv.28 exists.** Field 2, in the red parade at the bottom right of the fresh frame (about 580,800, plus or
  minus 60 px: the camera shifts about 30 to 85 px per tap). So the F1 panel read earlier was this ground, and the
  base map's "no Lv.28" was wrong: the two grounds it tapped were Lv.30 and Lv.27.
- **Building Details, Lv.28:** Unit Count **+9211**, four officer slots all filled; a Quick Dispatch button
  (not touched).
- **Upgrade preview, Lv.28 to 29, nothing pressed:** Unit Count +7,600 to **+7,800**, Power 165,800 to
  196,200 (**+30,400**), coin **14.4M of 119.0M** (red, short), iron 1.0G of **144.5M** (met), prerequisite
  Lv.29 Headquarters (met), original time 39d 01:53:19, **effective 18d 09:21:34**, Hero EXP 29.0M shown under the
  title. Finish Now (220,437 diamonds), Upgrade and Obtain were present and never pressed.
- **Reading.** The upgrade is blocked by coin (needs 104.6M more) and takes a builder for 18 days; the
  builders free on 2026-11-24T09:20Z. Fields 1, 3 and 4 were tagged, not opened.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 6 + 13 steps, 0 refused, no `local_input` pause,
  0.073656 and 0.177608 USD, 0.251264 in all (stated cap 0.5 per run).
- Closing state: the base, fresh frame, no panel, token released.
