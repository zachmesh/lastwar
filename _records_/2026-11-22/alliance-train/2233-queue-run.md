---
title: Alliance train check 2233
created: 2026-11-23T22:36:00Z
modified: 2026-11-23T22:36:00Z
version: 1.0.0
description: Unit train-2026-11-23-1430 - no train in preparation at 22:33Z (no Boarding closes banner, no locomotive icon); nothing boarded, nothing pressed
status: partial
grounded_in:
  - source: cu_bridge run 20261123T223305Z-677d0e, final report read by the operator, 2026-11-23T22:33Z to 22:34Z
  - source: unit brief train-2026-11-23-1430 and the alliance-train rule digest
---

# Alliance train check 2233

Rows in [2233-queue-run.csv](2233-queue-run.csv). Claimed 22:33:05Z; no different-device dialog.

- **Banner.** No 'Boarding closes in' banner in any frame (rule 1: close partial, no panning).
- **Left column.** No locomotive icon; the radar dish shows a red 1 (the leftover reward from 2208).
- **Not done.** Nothing boarded, no ticket spent; waits only.
- **Run.** One run, 6 steps, 5 actions, 0.066412 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 22:33:55Z.
