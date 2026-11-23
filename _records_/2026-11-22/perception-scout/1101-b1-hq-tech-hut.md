---
title: Headquarters, Tech Center and Builders Hut read B1
created: 2026-11-23T11:12:00Z
modified: 2026-11-23T11:12:00Z
version: 1.0.0
description: Unit scout-midday-growth-snapshot-2026-11-23-005 - Headquarters Lv.30 read with its Building Details; the Tech Center and the Builders Hut were not found among eight buildings tapped; a tag index of seven other buildings
status: partial
grounded_in:
  - source: cu_bridge run 20261123T110221Z-eec05f, events, final result and frame step-0013, 2026-11-23T11:02:21Z to 11:04:50Z
  - source: unit brief scout-midday-growth-snapshot-2026-11-23-005 (Story 868, B1) and coordinator assignment A-20261123-1101-operator
---

# Headquarters, Tech Center and Builders Hut read B1

Rows in [1101-b1-hq-tech-hut.csv](../growth/1101-b1-hq-tech-hut.csv) (a tag_text column beside every number).
Claimed 11:01:29Z, window end 11:02Z.

- **Headquarters.** Tag text **Headquarters Lv.30**, tapped at (565,405) on the fresh frame. Building Details shows
  no power line, only two hero entries (Adventurer: daily acquisition limit +25, radar task chests +4; Agent:
  hero attack +100, march size +1). The radial menu sat at about Details (468,411), middle (527,459), broom
  (602,459), green arrow (662,411); only Details was pressed.
- **Tech Center and Builders Hut: not found.** No builder count or banked speed-up time was read.
- **Tag index** (the camera drifts 30 to 85 px per tap, later points are approximate): Emergency Center
  **Lv.20** (245,268), Gear Factory **Lv.20** (310,333), Food Warehouse **Lv.24** (385,398), Component
  Factory **Lv.20** (105,385 and 268,420), Training Base **Lv.26** (100,412), Ginkgo Tree **Lv.1** decoration
  (115,188). The red and white building at (437,348) opens the STORE, not a tag.
- **Reading, unverified.** Four Training Base upgrades to Lv.25 are running, so more than one Training Base
  exists. Remaining candidates for the Tech Center and the Builders Hut: the right-hand buildings near the
  clock tower at the upper right and the buildings beyond the left edge.
- **New HUD item.** A "116min" bubble with a survivor icon sits beside the avatar at the lower left; it was not
  read.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 14 steps, 44 actions, 0 refused, no `local_input` pause,
  0.217060 USD (stated cap 0.5; 14 usable turns). HUD unchanged: food 648.5M, iron 1.0G, coin 14.4M, Total Power
  150,211,809. Nothing pressed beyond Details and empty ground.
- Closing state: the base, fresh frame, no panel, token released.
