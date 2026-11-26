---
title: Oil Well help request: no help control on the row 1110
created: 2026-11-26T11:10:48Z
modified: 2026-11-26T11:10:48Z
version: 1.0.0
description: Unit building-queues-oil-well-help-2026-11-25-001 (H118 help request on the Oil Well Lv.25 job; version 1.0.366(908); front LastWar at the start 11:10:03Z; the different-device dialog never on screen; a first attempt at 11:08:36Z met a cu-integrator gate run (DESKTOP BUSY) and waited read-only until the lock read free at 11:09:57Z; the earlier record of the Oil Well unit holds no help request) - the hammer COUNTER (108,218) tapped once at 11:10:16.2Z: the BUILDING QUEUE panel opened: row 1 'Lv.25 Oil Well upgrade in progress' Time Left 01:59:34 at 11:10:22.9Z and 01:59:27 at 11:10:29.5Z (the END about 2026-11-26T13:09:56.5Z), its only control a blue Speed Up button; NO help count ('n of 30') drawn, no hand glyph, no Help or Request Help button and no 'help requested' mark on the Oil Well row (nor on any row); row 2 Lv.27 Drill Ground 3d 04:20:32, row 3 Lv.27 Drill Ground 13d 20:13:49 (the new upgrade, ends about 2026-12-10T07:24:19Z), row 4 Lv.28 Drill Ground 7d 02:39:44; the builders 4/4; THE GESTURE NOT MADE: the unit allows the row's own Help control only; none exists on the row in this version (the same finding as the earlier help test of 05:25Z): the test is not run: no timer to re-read after 60 s; Speed Up, Finish Now and every other row never pressed; the panel closed by its X (612,237) at 11:10:35.7Z; the base; HUD: food 47.4M, iron 681.5M, coin 13.5M, diamonds 10,673; drags 0
status: partial
grounded_in:
  - source: cu_bridge run 20261126T111005Z-a6be62, final report read by the operator, 2026-11-26T11:10Z to 11:11Z
  - source: unit brief building-queues-oil-well-help-2026-11-25-001 and the building-queues rule digest
---

# Oil Well help request: no help control on the row 1110

Rows in [1110-queue-run.csv](1110-queue-run.csv). Claimed 11:10:04Z; no different-device dialog.

- **Oil Well row** (11:10:29.5Z): Lv.25, Time Left 01:59:27: **ends about 13:09:56.5Z**; no timer change to compare (no gesture).
- **No help control.** The row carries only a Speed Up button; no 'n of 30' count, no hand glyph, no Help button: the gesture could not be made (as at 05:25Z).
- **Not pressed:** Speed Up, Finish Now, any other row; the dialog never showed; drags 0.
- **Run.** One run, 8 steps, 2 actions, 0.092186 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 11:10:58Z.
