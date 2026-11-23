---
title: Tech Center locate 1801
created: 2026-11-23T18:05:00Z
modified: 2026-11-23T18:05:00Z
version: 1.0.0
description: Unit scout-midday-locate-2026-11-23-001 - first run read four tags (Arena Lv.1, Hospital Lv.25, Drone Center Lv.1, Eternal Pyramid Lv.3) and found no Tech Center; blocked by route, second run not made
status: partial
grounded_in:
  - source: cu_bridge run 20261123T180107Z-2f61d4, final report read by the operator, 2026-11-23T18:01Z to 18:03Z
  - source: unit brief scout-midday-locate-2026-11-23-001 and the tag-index and 1030 base map
---

# Tech Center locate

Rows in [1801-queue-run.csv](1801-queue-run.csv). Claimed 18:01:07Z; no different-device dialog; nothing upgraded, collected or trained.

- **Taps on the fresh frame (no pans).** (575,300) Arena Lv.1; (330,300) no tag; (665,445) Hospital Lv.25; (400,205) Drone Center Lv.1; (250,200) Eternal Pyramid Lv.3. None is a Tech Center.
- **New tag rows.** Arena, Drone Center and Eternal Pyramid were not in the tag index; added to [tag-index.csv](tag-index.csv) with the tap points (approximate: the view shifts a little with each selection).
- **Not covered.** No pan was made (0 of 8): the south, the far left and the north-east beyond the Oil Well remain; the flask research list does not show it either.
- **Result.** Blocked by route: the Tech Center is still unlocated; the next run should start with pans from WORLD then BASE, tapping unlabelled large buildings south and west of the Barracks and the Training Bases.
- **Run.** One run of the two allowed, 11 steps, 28 actions, 0.131713 USD, cap 0.4; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no tag, no panel; token released 18:02:54Z.
