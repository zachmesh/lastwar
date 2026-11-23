---
title: Chest quantity limits RC1
created: 2026-11-23T11:30:00Z
modified: 2026-11-23T11:30:00Z
version: 1.0.0
description: Unit scout-midday-growth-snapshot-2026-11-23-026 - one Use can take the full stock of every chest read (Resource Chest 20,862, Coin Chest UR 87 for 211.97M coins, SR 122 for 12.38M); no typed quantity; nothing used
status: done
grounded_in:
  - source: cu_bridge runs 20261123T111538Z-948aa9, 20261123T111730Z-3c32e0 and 20261123T112025Z-6085b3, frames step-0002, step-0005, step-0009, step-0010, step-0011, 2026-11-23T11:15Z to 11:22Z
  - source: unit brief scout-midday-growth-snapshot-2026-11-23-026 (RC1, Steer A verdict on decision 2603) and coordinator assignment A-20261123-1115-operator
---

# Chest quantity limits RC1

Rows in [1115-rc1-chest-limits.csv](1115-rc1-chest-limits.csv). Nothing was used, opened or typed; Use (about 400,920) was
never pressed; no choice chest was touched beyond selecting its tile.

- **Resource Chest** (tag text "Resource Chest", **20,862** owned, 109 more than the 20,753 of the 0009 read, probably the truck
  chests, unverified): selecting it sets the quantity to the **full stock 20862** with the slider handle at the far right; a tap on the number
  field did nothing (**no typed quantity**); no Total line; buttons minus, plus, Use, Statistics, no batch or use-all text.
  Max per Use is the stock; one choice of 6K coin each would be 125.17M coin (inferred, not tried).
- **Coin Chest (UR)** 87: default 1, with the handle at the far right **87**, Total **211.97M** coins; **no cap below the stock**.
- **Coin Chest (SR)** 122: handle at the far right **122**, Total **12.38M**; no cap. **Coin Chest (SSR)** 71: default 1, slider
  end not measured (inferred 71, 57.66M).
- **Reading.** Every chest read opens its full stock in one Use, so coin for the Lv.28 Drill Ground step (119.0M) is one UR Use
  of 87 chests (211.97M), not many runs; owner and Strategist rank it, the red line on opening chests stands. The Resources tab
  opens with the **5,000 Diamonds x16** tile selected and a live Use, and the Resource Chest default is its full stock: any
  later brief must name the tile and forbid Use.
- **Speed-up tab (not selected).** General: 8h x94, 3h x266, 1h x1,196, 15m x1, 5m x32,394, 1m x24,902 (351,647 minutes, about 244
  days); construction: 8h x10, 1h x26, 5m x28,477, 1m x19,015 (167,760 minutes, about 116.5 days); a blue-disc row
  8h x16, 1h x128 and a cut-off row are unread. Speed-ups stay a red line.
- **Run.** `claude-gateway/claude-sonnet-5-5`, three runs, 5 + 12 + 13 steps, 0 refused, no `local_input` pause, 0.078067, 0.169733 and
  0.183032 USD, 0.430832 in all. The grid drags overshoot; the slider handle drags only change a figure.
- Closing state: the base, no panel, token released.
