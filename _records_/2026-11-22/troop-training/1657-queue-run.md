---
title: Troop training idle-slot read 1657
created: 2026-11-23T17:02:00Z
modified: 2026-11-23T17:02:00Z
version: 1.0.0
description: Unit training-2026-11-23-0603 - Barracks Lv.24 and Lv.20 idle and blocked by capacity (Drill Ground Full), Lv.27 and Lv.30 training (batches of 726 and 793); read-only
status: done
grounded_in:
  - source: cu_bridge run 20261123T165728Z-6ce66d (no final report: step cap; messages read from its event log) and the cleanup run 20261123T170020Z-9d0187, 2026-11-23T16:57Z to 17:00Z
  - source: unit brief training-2026-11-23-0603 and the 1344 read
---

# Troop training idle-slot read

Rows in [1657-queue-run.csv](1657-queue-run.csv). Claimed 16:57:28Z; no different-device dialog.

- **Idle and blocked.** Barracks Lv.24 and Lv.20: the pistol raised 'Drill Ground Full: Unable to add more units.' (blocked by capacity: Drill Ground Full; tags Barracks Lv.24 and Lv.20). Stats: `slots_idle=2`, `slots_blocked_by_capacity=2`, `capacity_blocker="Drill Ground Full"`.
- **Training.** Barracks Lv.27: Lv.9 batch of 726, 02:57:18 left at 16:59:20Z (ends about 19:56:38Z). Barracks Lv.30: Lv.10 batch of 793, 18:18:41 left at 16:59:53Z (ends about 2026-11-24T11:18:34Z). Both match the 13:44Z read.
- **Run shape.** 15 steps were not enough: the final report turn never ran, so the read comes from the model's per-step messages in the event log; the close of the Lv.30 panel was recorded but not executed, so a 5-step cleanup run closed it (X at 611,281) at 17:00Z. Speed Up never pressed.
- **Runs.** 0.208690 and 0.060967 USD (0.269657 in all), cap 0.5 each; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel, no building selected; token released 17:00:49Z.
