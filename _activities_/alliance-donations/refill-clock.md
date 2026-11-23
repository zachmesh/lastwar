---
title: Alliance donations refill clock
created: 2026-11-23T17:53:50Z
modified: 2026-11-23T17:53:50Z
version: 0.1.0
description: The settled refill rate of the donation count, one per 20 minutes on a fixed clock, with the evidence, the open items and the next prediction
---

# Alliance donations refill clock

The Researcher's note `_records_/2026-11-22/research/donation-refill-settled.md` settles digest rule 8: status tested, 2026-11-23, on `_records_/2026-11-22/alliance-donations/1745-queue-run.md` and `_records_/2026-11-22/alliance-donations/1441-queue-run.md`. Back to the [rule digest](rule-digest.md).

## The rule

"The count is a pool refilling one per 20 minutes on a fixed clock (grid :17:57, :37:57, :57:57 on 2026-11-23), cap 30, so 3 an hour. A spent pool's grey timer ends on that grid. A pass's entry count is 1 + floor((entry time - last timer end) / 20 min), less counts used elsewhere. Each pass logs entry time and count, every tap time, and the first timer with its read time." Re-anchor on each pass's own timer end.

## The evidence

Three timer ends: 10:17:57.107Z (T1), 14:57:57.397Z (1441) and 17:57:57Z (1745, three reads within 0.3 s). The gaps are 16,800.29 s (14 x 1,200) and 10,800 s (9 x 1,200). The 17:45:43.410Z entry read 9/30, which is 1 + floor(10,006 s / 1,200) as pre-registered; the 35-minute hypothesis predicted 5. The period is fixed: both gaps are whole multiples of it, so only divisors of 1,200 s fit, and the timers (up to 19.58 minutes in 85 of 89 history timers) exclude every shorter divisor. Each end lies within 0.3 s of the grid.

## Still open [G]

The 14:39Z entry count read 8 against 14 (the phone or partial accrual; the 17:45Z count matched exactly). The four long timers of 10-31 and 11-03, 40.9 to 48.8 minutes, belong to an earlier regime.

## Next prediction

Pass 002 at 21:15Z: count 10, first timer ends 21:17:57 within 3 s; an entry after 21:17:57 gives 11 and 21:37:57. Cost [D]: 72 taps a day at 1,000 coin is 72K coin, about 0.3 to 0.5 percent of the 16M to 26M daily coin income.
