---
title: Drone and Wall of Honor read D1
created: 2026-11-23T10:22:00Z
modified: 2026-11-23T10:22:00Z
version: 1.0.0
description: Unit scout-midday-growth-snapshot-2026-11-23-023 - read-only look at the Drone Center and the Wall of Honor; Tactical Drone Lv.134 power 5,840,675, Drone Center Lv.1, Wall of Honor not found, three drone tabs unread
status: partial
grounded_in:
  - source: cu_bridge run 20261123T101753Z-e9a1c6, events, final result and frame step-0008, 2026-11-23T10:17:53Z to 10:19:20Z
  - source: unit brief scout-midday-growth-snapshot-2026-11-23-023 (Story 868, D1 re-minted) and coordinator assignment A-20261123-1017-operator
---

# Drone and Wall of Honor read D1

Rows in [1017-d1-drone-wall.csv](../growth/1017-d1-drone-wall.csv) (schema g_drone_wall).

- **Framing.** The camera was still panned to the train station; WORLD then BASE (bottom right,
  both at about 660,940) restored the full base, nothing touched on the World map.
- **Drone Center.** Name tag **Lv.1** (a Chip Lab Lv.20 and a Wall Lv.26 were tapped by mistake
  on the way; their menus were closed, nothing pressed). The plane icon in the radial menu opens
  the **Tactical Drone** screen.
- **Drone screen, Attributes tab.** Drone **Lv.134**, level bar 0/1,681,200, screen power
  **5,840,675**. Health +2,671,634 to +2,673,501, Attack +60,910 to +60,955, Defense +11,182
  to +11,191, one 5-star skill. A resource line reads **2.88M/93.40K** beside a blue data icon
  (label unread; probably Battle Data against a Data Training cost, unverified), above the green
  **Data Training** button with a red dot, not pressed. Tabs: Attributes, Component, Combat
  Boost, Skill Chip, plus Upgrade Preview and Skin.
- **Unread (owed to D1b).** Drone Parts stock, the Battle Data label, skill chip stock, the
  Combat Boost tier and the next-level cost.
- **Wall of Honor: not found.** No orange medal icon on the base; the trophy bubble in the middle is
  off limits (red line list); a Wall Lv.26 tap opened a repair menu. Try a Tank, Aircraft or
  Missile Center tab next.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 10 steps, 18 actions, 0 refused, no `local_input`
  pause, 0.146503 USD (stated cap 0.6; 12 usable turns for the framing restore, the unit's own
  budget is 8 steps). Nothing spent or pressed beyond taps on building bodies and menus.
- Closing state: the base, no panel open, token released.
