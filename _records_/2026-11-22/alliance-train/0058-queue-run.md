---
title: Train countdown skipped, tram icon absent 0058
created: 2026-11-25T00:59:01Z
modified: 2026-11-25T00:59:01Z
version: 1.0.0
description: Unit train-2026-11-24-1630 (front at the start 00:58:49Z LastWar) - the tram icon at (107,580) was NOT DRAWN in all four frames (00:58:58.6Z to 00:59:16.8Z, only ground and buildings there): the station countdown needs the icon DRAWN with no badge, so it was skipped and nothing was tapped; no train banner and no locomotive icon; pickup none, radar dish none; hammer 4/4, flask 2/2; drags 0
status: done
grounded_in:
  - source: cu_bridge run 20261125T005850Z-dc7cee, final report read by the operator, 2026-11-25T00:58Z to 00:59Z
  - source: unit brief train-2026-11-24-1630 and the alliance-train rule digest
---

# Train countdown skipped, tram icon absent 0058

Rows in [0058-queue-run.csv](0058-queue-run.csv). Claimed 00:58:49Z; no different-device dialog.

- **Tram icon.** NOT DRAWN in four frames over 18 s: the Station Platform pan is not available; the countdown skipped.
- **Other.** No train banner or locomotive icon; nothing pressed; drags 0.
- **Run.** One run, 5 steps, 0 actions, 0.067637 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 00:59:26Z.
