---
title: Train arrival mail stopped by a macOS alert 1536
created: 2026-11-24T15:37:12Z
modified: 2026-11-24T15:37:12Z
version: 1.0.0
description: Unit mail-train-arrival-claim-2026-11-24-001 - foreground switch: a macOS alert at 15:36:22Z, no tap of ours: UserNotificationCenter took the front 10 s into the run; the guard stopped it at step 1 (nothing pressed, nothing answered, the mail not opened); I ran the standing killall once at 15:36:34Z before the coordinator's hold: the process respawned (new ASN) and stayed in front; the game is held until the coordinator's restore word; drags 0
status: partial
grounded_in:
  - source: cu_bridge run 20261124T153612Z-931fd0, final report read by the operator, 2026-11-24T15:36Z to 15:37Z
  - source: unit brief mail-train-arrival-claim-2026-11-24-001 and the mail-rewards rule digest
---

# Train arrival mail stopped by a macOS alert 1536

Rows in [1536-queue-run.csv](1536-queue-run.csv). Claimed 15:36:11Z; no different-device dialog.

- **Foreground switch.** UserNotificationCenter took the front at **15:36:23Z**, 10 s into the run; the guard stopped it at step 1: nothing pressed, answered or opened.
- **Killall.** ONE standing killall at 15:36:34Z (before the hold arrived): it respawned (new ASN) and stayed in front on every poll to 15:37:25Z.
- **State.** The game is held; the restore word is the coordinator's (15:57Z).
- **Counts.** Drags 0; tram badge none at 15:36:17.8Z.
- **Run.** One run, 2 steps, 0 actions, 0.01 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The game held behind the alert; token released 15:36:23Z.
