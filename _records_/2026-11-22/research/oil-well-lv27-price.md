---
title: Oil Well cost table, corrected after the Lv.26 to 27 press
created: 2026-11-26T05:30:00-08:00
modified: 2026-11-26T06:10:00-08:00
level: L0
version: 1.2.0
description: Corrected cost table for the Oil Well upgrades after the Lv.26 to 27 press showed coin and food charged, with the earlier previews carried as partial and the rows for the next levels
status: unverified
grounded_in:
  - source: _records_/2026-11-22/building-queues/0808-queue-run.csv and the Oil Well previews of 2026-11-24 for Lv.20 to 24, iron rows only
  - source: _knowledge_/growth-plan/building-power-gains-L25-31.csv, oil-well to 27, and _records_/2026-11-22/building-queues/1311-queue-run.md
---

# Oil Well cost table, corrected

**This note's first version was wrong.** It said Lv.26 to 27 costs iron only. The press at 13:31:34Z charged **iron 56.1M, food 18.7M and coin 11.9M** (stock deltas), exactly the guide table at 0.85. Effective time was 60.6 h (2d 12:37:36, original 5d 08:49:52), a factor of 2.125, and the real timer 26 s after the press read 54.09 h: the flat 6h32 (23,520 s) cut applied at every build start; the expected power +10,600 awaits the completion.

**Why the earlier reading failed.** Only the Lv.20 to 21 preview was dragged to the end of the cost list; the others show the rows visible without a drag. "No food row" in a list that was not dragged is not evidence. A Drill Ground preview of 11-24 had already recorded that coin was charged though no coin row showed.

| Oil Well preview | Rows seen | Status |
|---|---|---|
| Lv.20 to 21 | iron 8.5M, no food, coin or oil after scrolling; yet food fell 2.9M and coin 1.9M at the press | partial: the panel did not list charged rows |
| Lv.21 to 22 | iron 11.9M, "none scrolled" | partial |
| Lv.22 to 23 | iron 14.4M, scroll not stated | partial |
| Lv.23 to 24 | iron 17.8M, scroll not stated; food fell 6.0M and coin 3.9M within 80 s | partial: probably charged rows |
| Lv.26 to 27 | rows below iron hidden; charged iron, food, coin | cost known from deltas |

The hypothesis that Oil Well levels beyond Lv.21 cost iron only (H116) is refuted at Lv.27.

**Rows for the next levels** (table at 0.85; effective time at 2.125):

| To level | Food | Coin | Iron | Power | Days |
|---|---|---|---|---|---|
| 28 | 26.4M | 17.0M | 78.2M | +12,600 | 3.53 |
| 29 | 36.5M | 23.8M | 110.5M | +14,900 | 4.61 |
| 30 | 51.0M | 33.1M | 153.0M | +17,500 | 5.98 |

**Rule:** price every build from the table's three columns first; drag the cost list until every row is seen, and treat a missing row as unseen, not absent.

**The stock deltas gave it away earlier.** At three presses food was 0.33 to 0.34 of the iron cost and coin 0.21 to 0.22 (Lv.21: 8.5 / 2.9 / 1.9; Lv.24: 17.8 / 6.0 / 3.9; Lv.27: 56.1 / 18.7 / 11.9), the table's own ratio; the earlier records called the food and coin falls unexplained. So even a dragged panel may not list every charged row: the table prices all three, the preview only confirms the rows it shows.

