---
title: Alliance help Help All 0401
created: 2026-11-24T04:05:30Z
modified: 2026-11-24T04:05:30Z
version: 1.0.0
description: Unit help-2026-11-23-1830 - Help All pressed once: the header 'Today's points gained from Alliance Help' went from 0/1,000 to 120/1,000; three ally requests helped (a Lv.27 Oil Well, a Lv.28 Drill Ground and a Lv.21 building), the owner's own Food Output V request stays at 30/30
status: done
grounded_in:
  - source: cu_bridge run 20261124T040058Z-9bcc18, final report read by the operator, 2026-11-24T04:00Z to 04:01Z
  - source: unit brief help-2026-11-23-1830 and the alliance-help rule digest
---

# Alliance help Help All 0401

Rows in [0401-queue-run.csv](0401-queue-run.csv). Claimed 04:00:58Z; no different-device dialog.

- **Before.** Header 0/1,000; the owner's own request (30/30) and three ally requests.
- **Help All.** Once: the three ally rows cleared; the header **0 to 120 of 1,000** (40 points a help).
- **Left.** Only the owner's own Food Output V request (full 30/30).
- **Run.** One run, 7 steps, 15 actions, 0.090507 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 04:01:48Z.
