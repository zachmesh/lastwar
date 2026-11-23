---
title: Age of Oil grey nodes
created: 2026-11-23T14:20:00Z
modified: 2026-11-23T14:20:00Z
version: 1.0.0
description: Read-only panels of Oil Output I, Fast Builder V, Research Enhancement V, Parts Workshop and Base Expansion in THE AGE OF OIL tree, reached through the HQ preview's Base Expansion Research button while both labs are busy; times in seconds against base 485,100 and 686,340
status: done
grounded_in:
  - source: cu_bridge runs 20261123T140817Z-59ec41 and 20261123T141055Z-1b7caf, events and final results, 2026-11-23T14:08Z to 14:13Z
  - source: coordinator assignment of 14:00Z (grey nodes, Finish Now clock beside the Research button) and record 1352
---

# Age of Oil grey nodes

Rows in [1410-age-of-oil-grey-nodes.csv](1410-age-of-oil-grey-nodes.csv). No different-device dialog in either no-click first frame; nothing pressed on any node (every Research and Finish Now button was greyed).

- **Route that works with both labs busy:** HQ (tag "Headquarters Lv.30") green arrow, the red cost row "Lv.1 Base Expansion", its blue **Research** button: it opens THE AGE OF OIL tree (no dialog, nothing starts).
- **Oil Output I** 0/10 (+1.00% oil well output): needs Lv.1 Food Output V (red, running), Lv.1 Iron Output V (red, running), Lv.1 Coin Output V (green); iron 3.3M; base **686,340 s**, Finish Now clock 2d 04:58:00 (190,680 s),
  Research button 2d 09:10:00 (205,800 s). **Fast Builder V** and **Research Enhancement V** (0/10, +2.50% construction and research speed per level) need Lv.10 Oil Output I (red); iron 3.3M, **coin 10.0M**, food 3.3M, the same three times.
- **Parts Workshop** 0/1: coin 28.7M, iron 9.5M, base 22d 07:37:00, button 6d 18:18:29; needs Training Cost I and Healing Cost II (red). **Base Expansion** 0/1 (cap to 35): coin **174.1M**, iron 58.0M, food 58.0M, base 55d 12:47:00,
  button 16d 19:52:25, Finish Now 315,154 diamonds; needs **Lv.10 Oil Output III** (red).
- **Research speed arithmetic.** Button times give M about 3.30 to 3.34 on every node; the Finish Now clock gives 3.599 (Oil Output I) and 3.678 (Iron Output V, whose started timer matched it). The same
  slope 3.42 fits both Age of Oil node pairs with an offset: the effective time is not a pure divisor (unverified; the analyst should fit it).
- **Oil:** no oil cost on any node panel; the counter reads 647.0K. **Not seen:** the lower cost rows of Oil Output I, the Tech Center's own level (panels only say "Lv.30 Any Tech Center").
- **Run.** `claude-gateway/claude-sonnet-5-5`, 10 + 17 steps, 0 refused, no `local_input` pause, 0.159148 and 0.230852 USD (0.390000 in all). HUD unchanged (coin 11.9M, Total Power 150,416,946).
- Closing state: the base, no panel, token released.
