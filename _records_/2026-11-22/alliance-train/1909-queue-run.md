---
title: Alliance train check 1909
created: 2026-11-23T19:11:00Z
modified: 2026-11-23T19:11:00Z
version: 1.0.0
description: Unit train-2026-11-23-1030 - no train in preparation at 19:10Z (no Boarding closes banner, no locomotive icon); nothing boarded, nothing pressed
status: partial
grounded_in:
  - source: cu_bridge run 20261123T190935Z-0daef2, final report read by the operator, 2026-11-23T19:09Z to 19:10Z
  - source: unit brief train-2026-11-23-1030 and the alliance-train rule digest
---

# Alliance train check 1909

Rows in [1909-queue-run.csv](1909-queue-run.csv). Claimed 19:09:35Z; no different-device dialog.

- **Banner.** No 'Boarding closes in' banner in four looks.
- **Left column.** No locomotive icon, so no train is in preparation (rule 1: close partial, no panning).
- **Not done.** Nothing boarded, no ticket spent; the arrival mail is read by the mail unit.
- **Run.** One run, 6 steps, 5 actions, 0.074431 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 19:10:51Z.
