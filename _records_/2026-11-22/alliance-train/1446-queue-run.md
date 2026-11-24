---
title: Alliance train check 1446
created: 2026-11-24T14:46:22Z
modified: 2026-11-24T14:46:22Z
version: 1.0.0
description: Unit train-2026-11-24-0630 - no train in preparation at 14:46Z (no Boarding closes banner); the tram icon (107,580) has NO badge, so it was not tapped and the station's next conductor countdown was not read; nothing boarded; drags 0
status: partial
grounded_in:
  - source: cu_bridge run 20261124T144604Z-b78398, final report read by the operator, 2026-11-24T14:46Z to 14:47Z
  - source: unit brief train-2026-11-24-0630 and the alliance-train rule digest
---

# Alliance train check 1446

Rows in [1446-queue-run.csv](1446-queue-run.csv). Claimed 14:46:03Z; no different-device dialog.

- **Banner.** No 'Boarding closes in' banner in any frame; the tram icon has no badge: **no badge**, not tapped.
- **Not done.** The station's next conductor countdown was not read (it needs the tram tap, forbidden without a badge); nothing boarded; drags 0.
- **Run.** One run, 6 steps, 5 actions, 0.068977 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 14:46:45Z.
