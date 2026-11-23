---
title: Donation refill test pass 1745
created: 2026-11-23T17:51:00Z
modified: 2026-11-23T17:51:00Z
version: 1.0.0
description: Unit donations-pass-2026-11-23-001 - entry count 9/30 at 17:45:43.410Z, nine coin taps, first timer ending 17:57:57 on the 20-minute grid: H20 confirmed, H35 rejected; tail skipped
status: done
grounded_in:
  - source: cu_bridge runs 20261123T174509Z-2a6969 (the pass) and 20261123T174759Z-64c738 (closing panels, a third timer read), event logs with millisecond timestamps read by the operator
  - source: unit brief donations-pass-2026-11-23-001, the Coach's pre-registration refill-test-prereg.csv and policy 2532
---

# Donation refill test pass

Rows in [1745-queue-run.csv](1745-queue-run.csv). Claimed 17:45:03Z; no different-device dialog; no hand tap before the pass.

- **Entry (written first).** Count **9/30** at **17:45:43.410Z**, coin Donate green at 1,000, no timer, node Quick Construction 9/10. Prediction H35: 5; H20: 9.
- **Taps.** Nine witnessed landed coin taps, 17:45:49.893Z to **17:47:04.217Z**, the count falling 9 to 1 one by one; 9,000 coins; the diamond Donate never pressed.
- **First timer.** Grey Donate with **00:10:48** read at 17:47:09.063Z and **00:10:41** at 17:47:16.286Z; a third read **00:09:56** at 17:48:00.966Z (cleanup run, no tap). All three end at **17:57:56.97 to 17:57:57.29Z**, within 0.5 s of 14:57:57.397Z plus 9 x 1,200 s.
- **Verdict.** **H20**: a fixed 20-minute grid, count 9 at entry as predicted, first end 17:57:57. H35 (5 and 17:52:57) is rejected. No refill model mismatch. The 1441 note (one per 35 minutes) does not hold; its entry count 8 at 14:39 fits 20 minutes too.
- **Tail.** Skipped: the first timer was 10:41 (over 10 minutes). Next grid points: 18:17:57 and 18:37:57.
- **Runs.** 0.199609 and 0.081694 USD (0.281303 in all), cap 0.4 and 0.3; 0 refused; foreground stayed LastWar.
- **Closing state.** The dialog, Techs and Alliance screens closed with their X and back arrow; the base, no panel; token released 17:48:44Z.
