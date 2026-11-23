---
title: Box and chest read 0054
created: 2026-11-23T09:08:00Z
modified: 2026-11-23T09:08:00Z
version: 1.0.0
description: Growth continuation A-20261123-0850-operator, owner-approved single openings of a Mystery Supply Box, a Resource Choice Chest SR and a Coin Chest SR - the box pays a chest, not diamonds, the coin chain yields 101.52K coin per SR
status: run-partial
grounded_in:
  - source: cu_bridge runs 20261123T085415Z-a931ca, 20261123T085537Z-03abd4, 20261123T085801Z-8c0ad3, 20261123T085926Z-26c528, 20261123T090147Z-f47251 and 20261123T090417Z-43ecdf, events, final results and frames, 2026-11-23T08:54Z to 09:05Z
  - source: coordinator safeguards in the A-20261123-0850 addendum, Steer A decision 2425
---

# Box and chest read 0054

- Rows in [0054-box-chest-read.csv](0054-box-chest-read.csv); each opening is also in the
  [ledger](ledger.csv). Six runs on `claude-gateway/claude-sonnet-5-5`, 30 steps in all,
  refused 0, cost 0.080141, 0.061714, 0.047979, 0.078953, 0.043391 (paused, stopped) and
  0.082132 USD, total 0.394310 against a stated 0.4 cap per part. Part A, the Universal
  Shard counts and Gear names, is not done.
- **Safeguard used:** each Use ran in its own run after a frame check that the number
  field read exactly 1. The box defaults to its full count (366), so its slider was
  dragged to the minimum first; the choice chest and coin chest defaulted to 1.
- **Mystery Supply Box x1** at 08:55:43Z: one tile, a blue-silver chest with yellow
  chevrons x1, name not shown (a Resource Choice Chest, rarity unknown). **No diamonds, no
  Universal UR Shards.** Box 366 to 365, diamonds 11,136 unchanged. After the open the
  slider returned to the full count, so each later Use must reset the quantity.
- **Resource Choice Chest (SR) x1** at 08:59:41Z: a popup with three tiles (iron, food,
  coin chest), Coin chosen, Use pressed once. It yields **a Coin Chest (SR) x1 as an
  item**, not coins. Coin Chest (SR) count 122 to 123.
- **Coin Chest (SR) x1** at 09:04:32Z: Coins 101.5K. Count 123 to 122, coin 9.6M to 9.7M
  on the HUD, Total Power 150,211,809 unchanged.
- **Reading:** an SR choice chest is worth 101.52K coin, two steps. At that rate the
  1,523 SR chests give about 155M coin, and each box pays one more choice chest (about 365
  more). The UR choice chests give 2.43M each.
- **Interruption:** local pointer input paused run 20261123T090147Z-f47251 after 3 steps
  with no Use pressed; I stopped it and restarted. Other seats' test jobs were running on
  the Mac. The Resources tab selects the 5,000 Diamonds tile by default with Use active.
- Closing state: the base, no panel.
- Follow-up: Part A names (Universal Shard counts, Gear tab, Bond Badges, Guidebooks,
  Training Certificates, Black Market currency), and the rarity of the box's chest.
