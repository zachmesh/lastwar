---
title: Decoration Gallery read D1b
created: 2026-11-23T10:50:00Z
modified: 2026-11-23T10:50:00Z
version: 1.0.0
description: Unit scout-midday-growth-snapshot-2026-11-23-014 - the Decoration Gallery entry was not found in three runs; the orange card bubble opens the Cosmetics, Coupon and Crystal store instead, read-only, nothing bought
status: partial
grounded_in:
  - source: cu_bridge runs 20261123T104131Z-52ba72, 20261123T104303Z-7dbea4 and 20261123T104439Z-1ab817, events, final results and frames, 2026-11-23T10:41Z to 10:46Z
  - source: unit brief scout-midday-growth-snapshot-2026-11-23-014 (Story 868, D1b), decoration-gallery-overview-ur rule digest rule 2, coordinator assignment A-20261123-1040-operator
---

# Decoration Gallery read D1b

Rows in [1040-d1b-decor.csv](../growth/1040-d1b-decor.csv) (schema g_decor, store findings in the notes).

- **Entry not found.** Three tries on the fresh base frame: the left-edge bubble at about (93,339) opened
  nothing (a resource bubble); the left-column vehicle icon (107,580) opened the Trucks screen
  (Your Plunder Count Today 0/4), back arrow closed it; the orange card bubble above the red-roofed
  building (437,296) opens a STORE, not the gallery. Overview figures, tabs, levels and next costs
  stay unread (the last read, 2026-11-09, was UR 18/39, SSR 7/19, SR 4/4, 6,160,413 power).
- **The store behind (437,296).** Four tabs: an unnamed orange-square tab (the Season-token store,
  chip 800: permanent decorations Dominance Sanctuary, Doomsday Castle, Glacial Palace and others),
  Cosmetics (chip 0, two tiles at 4,000), **Coupon Store** (chip **150**, permanent cosmetics 1,500 to
  4,000 coupons) and **Crystal Shop** (chips **4,442 crystals** and **213.2K** of a second item;
  sells Gold Brick, vouchers, Silver Brick, **100 Diamonds** and a 1h Speed-up; restocks on the 1st
  of each month, about 7d 15h left; prices unread). No gallery, book or overview icon.
- **Reading, unverified.** The 4,442 and 213,200 tiles on the Special inventory tab look like the Crystal
  Shop currencies; a diamond line for crystals would be an earned-currency source that the Strategist
  can rank. Nothing was bought, nothing tapped on a tile.
- **Next.** The gallery may sit behind the Heroes or Base customization menu or the left column
  when a different icon set shows; try the Heroes screen and the HQ radial menu in a future unit.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 3 runs, 16 steps, 0 refused, no `local_input` pause:
  0.050629, 0.064022 and 0.119108 USD, 0.233759 in all (stated cap 0.5 each).
- Closing state: the base, fresh frame, no panel open, token released.
