---
title: Shop tabs read 1629
created: 2026-11-23T16:32:00Z
modified: 2026-11-23T16:32:00Z
version: 1.0.0
description: Unit passes-shop-tabs-read-2026-11-23-001 - the shop tab row read in full, the G tab is the Gold Brick Mall purchase page and a Hot Sale Packs tab exists as the last tab, showing Packs sold out; nothing tapped but tabs, no other app opened
status: done
grounded_in:
  - source: cu_bridge run 20261123T162933Z-9a1415, final report and the foreground check read by the operator, 2026-11-23T16:29Z to 16:31Z
  - source: unit brief passes-shop-tabs-read-2026-11-23-001, the run 1457 record and the shop-claims rule digest
---

# Shop tabs read

Rows in [1629-queue-run.csv](1629-queue-run.csv). Claimed 16:29:29Z; Steer A's standing rule met by the coordinator's exit plan (16:29Z); no different-device dialog.

- **Tab row** after one sideways drag: Official Event, Weekly Deal, Super Monthly Pass, Weekly Pass, Diamond, **Gold Brick Mall**, **Hot Sale Packs**; no tag text on any tab; nothing sits beyond the last.
- **The G tab is the Gold Brick Mall**, a purchase page titled 'Gold Brick Mall - Extra 5% Bonus': gold brick packs with Free Gift bonuses at $4.99, $9.99, $499.9 and $999.9, no timers and no Claim, Claimed or Already claimed text. Only its title and first four cards were read; two more exist below the fold (not scrolled).
- **Hot Sale Packs exists** (the 1457 read missed it, cut off by the right edge) and shows only 'Packs sold out': no cards, timers or prices. The rule digest's 'no Hot Sale Packs tab' is stale; the free pack is not on offer now.
- **Official Event** first frame still carries the 'Visit the Last War Store' banner with a blue Go button: not tapped.
- **Taps.** The cart icon, two tabs, one tab-row drag and the shop back arrow; no price button, Renew, Extension, Take All, Get Now, Buy or Claim; the foreground stayed LastWar through the run (polled every 9 s).
- **Run.** One run, 7 steps, 11 actions, 0.084851 USD, cap 0.5; 0 refused.
- **Closing state.** The base, no panel; food 664.1M, iron 1.0G, coin 19.1M, gems 11,113 and Total Power 150,416,946, all unchanged; token released 16:30:35Z.
