---
title: Troop training read 1810
created: 2026-11-23T18:14:00Z
modified: 2026-11-23T18:14:00Z
version: 1.0.0
description: Unit training-2026-11-23-1003 - Barracks Lv.24 and Lv.20 idle and blocked by capacity (Drill Ground Full), Lv.27 batch of 726 ends about 19:56Z, Lv.30 batch of 793 about 11:18Z tomorrow; read-only, no Train
status: done
grounded_in:
  - source: cu_bridge runs 20261123T180930Z-44390f (route failed) and 20261123T181026Z-54b987 (the read), final reports read by the operator, 2026-11-23T18:09Z to 18:13Z
  - source: unit brief training-2026-11-23-1003 and the 1657 record
---

# Troop training read

Rows in [1810-queue-run.csv](1810-queue-run.csv). Claimed 18:09:30Z; no different-device dialog; no Train, Speed Up or slider touched.

- **Route.** The first run's tap at (626,584) selected the Hospital Lv.25 because the camera had shifted; after WORLD then BASE the second run found all four tags (the four tents sit lower and further left on a shifted frame).
- **Idle and blocked.** Barracks Lv.24 and Lv.20: the pistol raised 'Drill Ground Full: Unable to add more units.' (blocked by capacity: Drill Ground Full). Stats: `slots_idle=2`, `slots_blocked_by_capacity=2`, `capacity_blocker="Drill Ground Full"`.
- **Training.** Barracks Lv.27: Lv.9 batch of 726, 01:44:32 left (ends about 19:56:50Z). Barracks Lv.30: Lv.10 batch of 793, 17:05:50 left (ends about 2026-11-24T11:18:30Z). Both match 1657.
- **Runs.** 0.067772 and 0.200548 USD (0.268320 in all), cap 0.5 each; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no menu or panel; token released 18:13:06Z.
