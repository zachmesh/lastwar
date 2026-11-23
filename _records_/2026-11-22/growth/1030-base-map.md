---
title: Base map
created: 2026-11-23T10:40:00Z
modified: 2026-11-23T10:40:00Z
version: 1.0.0
description: One-time grounding of the barracks tents, the Hospital and the Drill Grounds on the fresh full-base frame (after WORLD then BASE), read-only, with tags, levels and tap points so later training reads start from known positions
status: done
grounded_in:
  - source: cu_bridge runs 20261123T102945Z-d814fb (fresh frame), 20261123T103104Z-6efaca (tents A to C) and 20261123T103402Z-729e81 (tents D, E and the Drill Grounds), frames and events, 2026-11-23T10:29Z to 10:36Z
  - source: coordinator assignment A-20261123-1030-operator
---

# Base map

Rows in [1030-base-map.csv](1030-base-map.csv). Positions are in the 1920x1080 frame of the **fresh base
frame**, restored with the WORLD button (660,940) then the BASE button at the same place; the restored
frames matched each time, so the points repeat.

| Building | Tag | Clock bubble | Tap point (x,y) |
|---|---|---|---|
| tent A | Barracks Lv.27 | yes, (460,530), the batch ending about 19:56Z | 462,585 |
| tent B | Barracks Lv.30 | yes, (529,578) | 530,637 |
| tent C | Barracks Lv.24 | none | 628,562 |
| tent D | Barracks Lv.20 | none | 668,535 |
| tent E | Hospital Lv.20 | none (red-helmet bubble above) | 678,510 |
| Drill Ground, orange | Drill Ground Lv.30 | none | about 740,880, off-screen right |
| Drill Ground, purple crystal | Drill Ground Lv.27 | none | about 855,790, off-screen right |

- **No Drill Ground Lv.28.** The Lv.28 seen near (260,545) is the Farmland. The two Drill Grounds sit past
  the right edge of the fresh frame; only their red soldier parade (bottom right, about 500-715 by 830-980)
  shows. A pan (one drag) showed no third one, only wall and fog at the bottom right edge.
- **Each tap** shows the tag (name and level) above the building and a radial menu (paw, orange
  pistol or tent button, green up arrow), and shifts the camera about 30 px; tapping near the lower
  edge or the Hospital can shift it about 220 px.
- **Hazard.** With a radial menu open low on the screen, the green up arrow (Upgrade) can sit at the
  WORLD button's position. Close a menu with an empty-ground tap such as (200,610), then use WORLD and
  BASE; run 2 avoided the green arrow that way. Press only the pistol for the training read.
- **Training read route.** From the fresh frame tap A, B, C or D, read the tag, then the orange pistol under
  it; restore with WORLD then BASE before the next building.
- **Run.** Three runs on `claude-gateway/claude-sonnet-5-5`: 0.041678, 0.112049 (8 steps, no model report,
  tags read from the frames) and 0.133088 USD, 0.286815 in all, stated cap 0.4 each, 0 refused, no
  `local_input` pause. Nothing pressed in any menu; no Hospital Collect.
- Closing state: the base, fresh frame, no panel, token released.
