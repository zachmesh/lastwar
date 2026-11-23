---
title: Alliance donations refill clock
created: 2026-11-23T17:53:50Z
modified: 2026-11-23T19:58:10Z
version: 0.3.0
description: The settled refill rate of the donation count, one per 20 minutes on a fixed clock, with the evidence, the open items and the next prediction
---

# Alliance donations refill clock

The Researcher's note `_records_/2026-11-22/research/donation-refill-settled.md` settles digest rule 8: status tested, 2026-11-23, on `_records_/2026-11-22/alliance-donations/1745-queue-run.md` and `_records_/2026-11-22/alliance-donations/1441-queue-run.md`.

## The rule

"The count is a pool refilling one per 20 minutes on a fixed clock (grid :17:57, :37:57, :57:57 on 2026-11-23), cap 30, so 3 an hour. A spent pool's grey timer ends on that grid. A pass's entry count is 1 + floor((entry time - last timer end) / 20 min), less counts used elsewhere. Each pass logs entry time and count, every tap time, and the first timer with its read time." Re-anchor on each pass's own timer end.

## The evidence

Three timer ends (10:17:57.107Z, 14:57:57.397Z, 17:57:57Z) lie 14 and 9 periods apart; the 17:45:43Z entry read 9/30 as pre-registered. Timers up to 19.58 minutes exclude shorter divisors; each end is within 0.3 s of the grid.

## The formula as the Coach checks it, 2026-11-23

predicted = max(0, min(30, 1 + floor((entry - anchor) / 20 min) - taps since the anchor)). The anchor is the last timer end read in a pass that spent the pool; the taps are witnessed taps since, ours included; an entry before the anchor gives 0. At 30 the cap hides the answer (10 hours without a pass loses refills): keep the gap under about 9 hours. A smaller count is counts used elsewhere: the owner donated from the phone between 10:13Z and 14:39Z (the count is shared with the game), so the 14:39Z shortfall of 6 is no model mismatch (`_records_/2026-11-22/coach/refill-pass-log.csv`). Log a later shortfall as elsewhere; flag it only above 6 with no owner activity. Method `_records_/2026-11-22/coach/refill-check-method.py`.

## Still open [G]

The four long timers of 10-31 and 11-03 (40.9 to 48.8 minutes), an earlier regime.

## Next prediction

Pass 002 at 21:15Z: count 10, first timer ends 21:17:57 within 3 s; an entry after 21:17:57 gives 11 and 21:37:57.
