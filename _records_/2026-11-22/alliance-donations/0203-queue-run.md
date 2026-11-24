---
title: Refill reset read B 0203
created: 2026-11-24T02:05:00Z
modified: 2026-11-24T02:05:00Z
version: 1.0.0
description: Unit donations-refill-reset-read-2026-11-24-002 - READ B after the 02:00Z reset: Donation Count 5/30 at 02:03:29.666Z and 02:03:35.265Z, outcome (a) no reset: 4 at READ A plus the 01:57:57 grid point; coin Donate green, no timer; Tech Donation Today 8,550 unchanged; no Donate tap
status: done
grounded_in:
  - source: cu_bridge run 20261124T020301Z-a48379, final report read by the operator, 2026-11-24T02:03Z to 02:04Z
  - source: unit brief donations-refill-reset-read-2026-11-24-002 and the alliance-donations rule digest
---

# Refill reset read B 0203

Rows in [0203-queue-run.csv](0203-queue-run.csv). Claimed 02:03:01Z; no different-device dialog.

- **Count.** **5/30** at **02:03:29.666Z** and again 02:03:35.265Z (inside the 02:03:00Z to 02:09:00Z window), coin Donate green, no timer.
- **Outcome (a), no reset.** 5 = READ A's 4 plus the 01:57:57.4Z grid point: the 02:00:00Z reset did not change the count (not 0 with a timer, not 30); B differs from A, no elsewhere-tap flag.
- **Daily figure.** Tech Donation Today 8,550 did not reset at 02:00Z either.
- **Pressed.** Only the route taps and closes; neither Donate button; nothing spent; the 00:37:57.17Z anchor stays valid.
- **Run.** One run, 10 steps, 9 actions, 0.115782 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The dialog, Techs and Alliance screens closed; the base, no panel; token released 02:04:07Z.
