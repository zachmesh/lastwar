---
title: Inventory read 0009
created: 2026-11-23T08:25:00Z
modified: 2026-11-23T08:25:00Z
version: 1.0.0
description: Growth continuation A-20261123-0810-operator, read-only Backpack read - about 2.38 billion coin is obtainable from coin chests and resource choice chests, the Overlord items were not located
status: run-partial
grounded_in:
  - source: cu_bridge runs 20261123T080903Z-9d4ced, 20261123T081103Z-f88d9c, 20261123T081250Z-cd7ecd, 20261123T081431Z-738a31, 20261123T081554Z-2c5f5f and 20261123T081833Z-97ebf3, events, final results and frames, 2026-11-23T08:09Z to 08:19Z
  - source: frames saved as _tools_/state/cu_inventory_resources_0016.png and cu_inventory_choice_0014.png (untracked)
  - source: coordinator assignment A-20261123-0810-operator and its addendum
---

# Inventory read 0009

- Rows in [0009-inventory-read.csv](0009-inventory-read.csv). Six runs on
  `claude-gateway/claude-sonnet-5-5`, 6, 7, 7, 7, 7 and 3 steps, refused 0, cost 0.529608
  USD in all, about 10 minutes. The last run stopped at its cost cap. Read only: tiles
  were selected, never used; no Use, Open, Convert or Buy.
- **Method:** a tapped tile shows its name and description under the grid; with quantity
  1 the Total line is the amount one item gives. A grid drag must start inside the grid.
- **Coin-convertible, in order of size:**
  - Resource Choice Chest UR 552: choose a Food, Iron or Coin Chest (UR), coin 2.43M each.
  - Resource Choice Chest SSR 587 (812.16K each) and SR 1,523 (101.52K each), same wording.
  - Resource Chest 20,753: choose 10K food, 10K iron or 6K coin.
  - Coin Chest UR 87, SSR 71, SR 122: 2.43M, 812.16K, 101.52K each, read.
  - Coin items 6.0K x174 and 600 x5,713, from tile labels.
- **Total coin obtainable: 2,383,161,480 (2.38G).** Read by description 405,976,800
  (coin chests 281,458,800, Resource Chest 124,518,000). Inferred from the matching Coin
  Chest 1,972,712,880 (the choice chests). Label only 4,471,800. The choice popup was
  never opened, so a two-step conversion (chest, then open) is assumed. Amounts follow
  the Base Level. Coin now 9.6M.
- **Other resources, read:** iron chests 4.06M (UR, x275), 1.35M (SSR, x1,428), 169.20K
  (SR, x7,981); Food Chest UR x169 at 4.06M; many food, iron and oil items.
- **Hero levers, left alone:** Mystery Supply Box x299 (Universal UR Shards and 5,000
  Diamonds), Skill Medal x9,521, hero chests, blueprints, exclusive weapons.
- **Red lines, left alone:** about 277,990 diamonds sit in item form (only the 5,000 size
  was read), and general speed-ups total about 352,000 minutes.
- **Not found:** Bond Badges, Guidebooks, Training Certificates and a Black Market
  currency: most Heroes, Gear and Special tiles have no name read yet. Needs one more run
  of about 0.1 USD.
- Snapshot taken. Red lines held: nothing used, nothing converted.
