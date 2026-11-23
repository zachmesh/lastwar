---
title: Coin Output V speed-up and Iron Output V start
created: 2026-11-23T14:10:00Z
modified: 2026-11-23T14:10:00Z
version: 1.0.0
description: Unit research-speedup-coin-v-2026-11-23-001 - seven UR Coin Chests converted, Coin Output V sped up with tech items and completed (+3,900 power), Iron Output V started with a 1d 12:37:59 timer; research speed M is 3.678
status: done
grounded_in:
  - source: cu_bridge runs 20261123T135214Z-6e7e2b (conversion), 20261123T135454Z-845eea (speed-up, Complete), 20261123T140004Z-ea602f (Iron Output V; frames step-0005 and step-0006), 2026-11-23T13:52Z to 14:02Z
  - source: unit research-speedup-coin-v-2026-11-23-001, decision OD-22 and Steer A's three conditions relayed by the coordinator at 13:51Z
---

# Coin Output V speed-up and Iron Output V start

Rows in [1352-speedup-coin-v.csv](1352-speedup-coin-v.csv); three ledger rows (13:55Z, 13:56Z, 14:00Z). Claimed 13:52:14Z; no different-device dialog in any no-click first frame.

- **1 Conversion.** Tag "Coin Chest (UR)", number field **7**, Total 17.05M read in a frame, one Use: coin 529.2K to **17.5M**, UR chests 87 to 80.
- **2 Speed-up, tech items only.** The Speed Up dialog for Coin Output V (1d 01:03:46 left) lists Instant Speed-up and Finish Now (never pressed) and the Research Speed-up items 8h, 1h, 5m. Presses: 8h x3
  (17:03:26, 09:03:18, 01:03:09 left; own 8 to 5), 1h x1 (00:03:01; own 126 to 125), 5m x1: a TIPS "would exceed 00:02:06, excess items returned by mail" took one Confirm (no price) and the research
  completed; about **1,505 minutes** of 11,400.
- **3 Complete** at 13:56:35Z: POWER **+3,900**, Total Power 150,413,046 to **150,416,946**.
- **3 Preview, Iron Output V 0/10** (The Age of Oil): next level +2.50%; iron 1.0G of 1.8M, coin 17.5M of 5.6M, food 654.7M of 1.8M, **no oil cost**; prerequisites Lv.30 Any Tech Center and Lv.1 Unlock Oil Well met.
  Original Time **5d 14:45:00 = 485,100 s**; the Research button 1d 16:50:00 (147,000 s); the Finish Now clock 1d 12:38:00.
- **4 Start** at 14:00:54Z: Research once, timer **1d 12:37:59 = 131,879 s**, so **M = 485,100 / 131,879 = 3.678** (not the 3.30 of the button); coin 11.9M, food 652.8M. Ends about 2026-11-25T02:39Z.
  The real duration equals the Finish Now clock, not the Research button (unexplained 11 percent difference).
- **Queue now:** Food Output V 1d 03:28:28 and Iron Output V 1d 12:37:29, both labs busy. **Not read:** Oil Output I (base 679,140 s), Fast Builder V, Research Enhancement V panels.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 13 + 13 + 12 steps (plus a stopped 12-step run, 0.144455 USD), 0 refused, no `local_input` pause; 0.154838, 0.191604, 0.171974 USD; 0.662871 in all.
- Closing state: the base, no panel, token held for the next unit.
