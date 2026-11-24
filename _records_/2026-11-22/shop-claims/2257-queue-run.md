---
title: Passes weekly tab read 2257
created: 2026-11-23T23:00:00Z
modified: 2026-11-23T23:00:00Z
version: 1.0.0
description: Unit passes-2026-11-23-1457 - Weekly Pass tab read twice: Free Supply Claimed, both pass cards Already claimed today (Remaining 6d 3:02:14), nothing claimable, nothing tapped but the tab
status: done
grounded_in:
  - source: cu_bridge run 20261123T225708Z-2b1541, final report read by the operator, 2026-11-23T22:57Z to 22:58Z
  - source: unit brief passes-2026-11-23-1457 and the shop-claims rule digest
---

# Passes weekly tab read 2257

Rows in [2257-queue-run.csv](2257-queue-run.csv). Claimed 22:57:08Z; no different-device dialog.

- **Free Supply.** Claimed (earlier).
- **Pass cards.** Both: Remaining 6d 3:02:14 (ends 2026-11-30 02:00Z), each 'Already claimed today' beside Renew $4.99, with a Renew All $19.99 banner; unchanged on the re-read.
- **Claim.** No green Claim anywhere: nothing claimed. The next Daily Pickup falls after the 02:00Z reset.
- **Taps.** The cart, the Weekly Pass tab and the back arrow; only the in-game shop opened.
- **Run.** One run, 8 steps, 10 actions, 0.102039 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 22:58:23Z.
