---
title: Research queue read 1808
created: 2026-11-23T18:10:00Z
modified: 2026-11-23T18:10:00Z
version: 1.0.0
description: Unit research-2026-11-23-1003 - both labs busy, Food Output V 23:21:14 left and Iron Output V 1d 08:30:15 left, ending about 2026-11-24T17:29:55Z and 2026-11-25T02:38:56Z; 0 idle; nothing pressed
status: done
grounded_in:
  - source: cu_bridge run 20261123T180824Z-d43adb, final report and observation timestamps read by the operator, 2026-11-23T18:08Z to 18:09Z
  - source: unit brief research-2026-11-23-1003 and the 1656 record
---

# Research queue read

Rows in [1808-queue-run.csv](1808-queue-run.csv). Claimed 18:08:23Z; no different-device dialog; nothing pressed in the panel.

- **Lab 1.** Food Output V (Lv.0 upgrade), Time Left **23:21:14** at 18:08:40.679Z: ends about **2026-11-24T17:29:55Z**.
- **Lab 2.** Iron Output V (Lv.0 upgrade), Time Left **1d 08:30:15**: ends about **2026-11-25T02:38:56Z**.
- **Idle.** 0 of 2 labs (`slots_idle=0`), none showing Complete; no capacity blocker.
- **Finish Now clock.** Not read: each lab shows a blue Speed Up button, and the clock sits behind a node panel that this read did not open. The 1656 read (16:56Z) agrees to the second with these ends.
- **Run.** One run, 6 steps, 9 actions, 0.075034 USD, cap 0.4; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, panel closed with its X; token released 18:09:05Z.
