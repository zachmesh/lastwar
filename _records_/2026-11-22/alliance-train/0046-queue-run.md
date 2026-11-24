---
title: Alliance train check 0046
created: 2026-11-24T00:47:00Z
modified: 2026-11-24T00:47:00Z
version: 1.0.0
description: Unit train-2026-11-23-1630 - no train in preparation at 00:46Z (no Boarding closes banner, no locomotive icon); nothing boarded, nothing pressed
status: partial
grounded_in:
  - source: cu_bridge run 20261124T004601Z-22444e, final report read by the operator, 2026-11-24T00:46Z to 00:46Z
  - source: unit brief train-2026-11-23-1630 and the alliance-train rule digest
---

# Alliance train check 0046

Rows in [0046-queue-run.csv](0046-queue-run.csv). Claimed 00:46:01Z; no different-device dialog.

- **Banner.** No 'Boarding closes in' banner in any frame (rule 1: close partial, no panning).
- **Left column.** No locomotive icon; ledger line 19 stays unreadable (the station panel is not reachable).
- **Not done.** Nothing boarded, no ticket spent; waits only.
- **Run.** One run, 6 steps, 5 actions, 0.065376 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 00:46:43Z.
