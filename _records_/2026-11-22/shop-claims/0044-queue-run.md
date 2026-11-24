---
title: Passes weekly tab read 0044
created: 2026-11-24T00:46:00Z
modified: 2026-11-24T00:46:00Z
version: 1.0.0
description: Unit passes-2026-11-23-1630 - Weekly Pass tab read twice: Free Supply Claimed, both pass cards Already claimed today (Remaining 6d 1:14:50), nothing claimable, nothing tapped but the tab
status: done
grounded_in:
  - source: cu_bridge run 20261124T004452Z-0e14bf, final report read by the operator, 2026-11-24T00:44Z to 00:45Z
  - source: unit brief passes-2026-11-23-1630 and the shop-claims rule digest
---

# Passes weekly tab read 0044

Rows in [0044-queue-run.csv](0044-queue-run.csv). Claimed 00:44:51Z; no different-device dialog.

- **Free Supply.** Claimed (earlier).
- **Pass cards.** Both: Remaining 6d 1:14:50 (ends 2026-11-30 02:00Z), each 'Already claimed today' beside Renew $4.99; unchanged on the re-read.
- **Claim.** No green Claim anywhere: nothing claimed; ledger lines 7, 10 and 11 stay at zero.
- **Taps.** The cart, the Weekly Pass tab and the back arrow; only the in-game shop opened.
- **Run.** One run, 7 steps, 9 actions, 0.090598 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 00:45:49Z.
