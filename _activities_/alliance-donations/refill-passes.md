---
title: Alliance donations refill passes
created: 2026-11-24T02:14:19Z
modified: 2026-11-24T02:14:19Z
version: 0.1.0
description: The dated passes and reads that test the donation refill clock, one line each, kept apart from the rule so the rule article stays short
---

# Alliance donations refill passes

Dated evidence for the [refill clock](refill-clock.md) (digest rule 8, verified 2026-11-23). Records are in `_records_/2026-11-22/alliance-donations/`; the Coach's log is `_records_/2026-11-22/coach/refill-pass-log.csv`.

- 2026-11-23, pass 001 (`1745-queue-run.md`): predicted 9, read 9; the 35-minute hypothesis predicted 5.
- 2026-11-23, pass 002 (`2115-queue-run.md`): predicted 10, read 10; the first timer ends 21:17:57.08 and 21:17:57.5, within 0.4 s of the grid.
- 2026-11-24, pass 003 (`0030-queue-run.md`): predicted 10, read 10; the timer ends 00:37:57.170Z. Its day-boundary claim was withdrawn: the game reset is 02:00Z, not 00:00Z.
- 2026-11-24, the 02:00Z daily reset does not touch the count or the grid: read 4 at 01:48Z (`0148-queue-run.md`), 5 at 02:03Z (`0203-queue-run.md`), as predicted without a reset; a reset to 0, a restarted grid and a refill to 30 are all rejected.
- Timer ends 10:17:57.107Z, 14:57:57.397Z and 17:57:57Z lie 14 and 9 periods apart, and timers up to 19.58 minutes exclude shorter divisors.
