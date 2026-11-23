---
title: Store read ST1
created: 2026-11-23T09:44:00Z
modified: 2026-11-23T09:44:00Z
version: 1.0.0
description: Unit scout-midday-growth-snapshot-2026-11-23-020 - read-only look at the VIP, Honor, Alliance and Campaign stores; Honor 130.1K, Alliance 81,010, Campaign 1,260 stars; three Campaign prices and the Season tab unread
status: partial
grounded_in:
  - source: cu_bridge runs 20261123T093837Z-368305, 20261123T094011Z-2eaf5c and 20261123T094139Z-750ba2, events, final results and frames, 2026-11-23T09:38Z to 09:43Z
  - source: unit brief scout-midday-growth-snapshot-2026-11-23-020 (Story 868, ST1) and coordinator assignment A-20261123-0938-operator
---

# Store read ST1

Rows in [0938-st1-stores.csv](../growth/0938-st1-stores.csv) (schema m_store, 53 rows).

- **Balances.** Honor medals **130.1K** (101.1K earlier), alliance currency **81,010**,
  Campaign stars **1,260**, red gems 11,136 (VIP tab, seen on opening).
- **Honor (monthly, 00:00 on the 1st, 7d 16:19 left).** UR Hero Universal Shard 10/10 at
  3,000; Universal Exclusive Weapon Shard 25/25 at 2,500; Resource Choice Chest (UR) 100/100
  at 4,000; Hero Recruitment Ticket 100/100 at 2,000; Gear Blueprint (UR) 50/50 at 10,000,
  (MR) 2/2 at 30,000; Skill Chip Chest (UR) and Decoration Chest 1/1 at 50,000 each;
  Decor Component 150/150 at 200; Drone Parts and Dielectric Ceramic 100/100 at 800;
  50 Stamina 50/50 at 1,000. Nothing sold out, no red price; rows below Emote: Victory Fest
  may exist.
- **Alliance (weekly, Monday 00:00, 6d 16:20 left).** Mason Shard 30/30 at 1,000; UR Hero
  Universal Shard, Survivor Recruitment Ticket, Violet Shard, Drone Parts and Lv.1 Drone
  Component Chest are SOLD; three tiles in the last row had price and stock cut off.
- **Campaign (weekly, Monday 00:00).** UR Hero Universal Shard 10/10 at 200 stars, Campaign
  Chest (UR) 10/10 at 200, Resource Choice Chest (SSR) 200/200 at 500, Battle Data 100K at
  2,000 and Basic Chip Material x400 at 5,000 (both above the balance); 8 more tiles at 200
  to 1,000. **Prices unread:** Universal Exclusive Weapon Shard 10/10, Skill Chip Chest
  (SSR), Upgrade Ore 1.0K.
- **Tab strip:** VIP, Alliance, Honor, Campaign, Season, Cosmetics, Coupon Store, Crystal
  Shop; Season, Coupon Store and Crystal Shop not read.
- **Why partial.** Run 1 (`20261123T093837Z-368305`, 8 steps) lost turns to a "You're very
  popular!" pop-up on the profile (its Awesome! button tapped once, harmless) and stopped on
  the Alliance tab; run 2 (`20261123T094011Z-2eaf5c`, 7 steps) read Honor in full and closed to
  the base; run 3 (`20261123T094139Z-750ba2`, 10 steps) read Campaign.
- **Cost.** 0.114182, 0.093433 and 0.119137 USD, 0.326752 in all, 25 steps, 0 refused, no
  `local_input` pause; stated cap 0.60 per run (harness stops near 0.216). Nothing bought,
  refreshed or claimed; no tile tapped. No player name or ID was recorded.
- Closing state: the base, no panel open, token released.
