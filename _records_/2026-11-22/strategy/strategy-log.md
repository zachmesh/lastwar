---
title: Strategy log
created: 2026-11-23T08:47:00Z
modified: 2026-11-23T09:17:00Z
version: 1.0.0
level: L3
description: One line a day on what the strategist changed and why, append only, for the watchdog and the weekly review
status: unverified
grounded_in:
  - source: Steer A design of 2026-11-23 08:44Z for observing the strategist
---

# Strategy log

One line per day, newest last. A correction is a new line.

- 2026-11-23. Centre moved from capacity first to training slots first after the hospital Collect was read as all or nothing (operator read 0030). F1 confirmed the ground cost model (coin 119.0M, iron 144.5M, +200 a level, speed factor 0.4706). Plan of record 0.3 and forecast ledger rows F-001 to F-018 written before any unit runs. Open: Extra Drill Ground node, X of Y, the 19:56Z batch test, the lowest ground.
- 2026-11-23 correction. The hospital Collect label "all or nothing, confirmed" was too strong (Steer A red team 08:46Z): no selector and a toast naming 5,306 are measured, partial-space behaviour is not. H16 is retagged supported and untested; one Collect tap at the first free slots decides it (F-019). The Oil Well is not built yet (task 0 of 1, Unlock Oil Well running), so the 434K oil held comes from elsewhere.
- 2026-11-23 box model. The 08:51Z claim paid 67 Mystery Supply Boxes (stock about 366); earlier claims paid 0, 1 to 15 and one batch of 224, so the rate is a forecast (F-020, about 100 a day), not 67 per claim. One box is a format read; ten boxes give a mean (PL-13). The box shards may be hero shards, not weapon shards (H43).
- 2026-11-23 learning. F-001 missed: the item text ("Universal UR Shards and 5,000 Diamonds") was taken as what a box pays, but one box gave one unnamed chest tile and no shards (operator ledger 08:55:43Z). The shard lever claim for the boxes is withdrawn (H43); they are a chest supply of unknown rarity. A schema change made at 08:58Z touched F-001 after its action ran; the row was restored at 08:59Z. The ledger now has kinds, p_success and value tags.
- 2026-11-23 correction. My 09:00Z line withdrew the box shard lever on one draw; that overreached (Steer A red team round 3). State: distribution unknown, prior low, n = 1. Steer A approved a sample of up to 22 boxes; F-031 and F-032 forecast a rare hit (p 0.45 and 0.30). No hit in 22 would put the rare rate under 10 percent at 90 percent. Opening the rest then loses nothing (H46).
- 2026-11-23 chain. Record 0054: SR Resource Choice Chest to Coin Chest SR to 101.52K coin, two steps, measured (H23 confirmed for SR). Batch 2 go rule fixed before batch 1 returns (H46). The Resources tab defaults to the 5,000 diamonds tile with Use active (H47).
- 2026-11-23 box policy. Box policy v1 written (0117-box-policy-v1). Changes to Steer A's draft: unread tiles are read not never; coin on hand is capped at floor plus 6 hours of spend, the 72-hour figure is a planning horizon (the plunder reason is unproven, H48); Violet's Loot sampled to 22 like the boxes. Food, not coin, is the first resource typed chests must cover.
