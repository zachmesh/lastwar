---
title: Alliance donations refill clock
created: 2026-11-23T17:53:50Z
modified: 2026-11-23T21:27:43Z
version: 0.4.0
description: The settled refill rate of the donation count, one per 20 minutes on a fixed clock, with the evidence, the open items and the next prediction
---

# Alliance donations refill clock

Researcher's note `_records_/2026-11-22/research/donation-refill-settled.md` settles digest rule 8: verified, 2026-11-23, on `_records_/2026-11-22/alliance-donations/1745-queue-run.md` and `_records_/2026-11-22/alliance-donations/2115-queue-run.md`, two passes scored on predictions registered before data.

## The rule

"The count is a pool refilling one per 20 minutes on a fixed clock (grid :17:57, :37:57, :57:57 on 2026-11-23), cap 30, so 3 an hour. A spent pool's grey timer ends on that grid. A pass's entry count is 1 + floor((entry time - last timer end) / 20 min), less counts used elsewhere. Each pass logs entry time and count, every tap time, and the first timer with its read time." Re-anchor on each pass's own timer end.

## The evidence

Timer ends 10:17:57.107Z, 14:57:57.397Z and 17:57:57Z lie 14 and 9 periods apart. Pass 001 predicted 9, read 9; pass 002 predicted 10, read 10, its first timer ends 21:17:57.08 and 21:17:57.5, within 0.4 s of the grid.

## The formula as the Coach checks it

predicted = max(0, min(30, 1 + floor((entry - anchor) / 20 min) - taps since the anchor)). The anchor is the last timer end read in a pass that spent the pool; the taps are witnessed taps since; an entry before the anchor gives 0. At 30 the cap hides the answer (10 hours without a pass loses refills): keep the gap under about 9 hours.

## Limits

- The grid is anchored on 2026-11-23 only: each pass re-anchors on its own timer end. Pass 003 (entry 00:30Z predicts 10, 11 at 00:40Z) is the first test across a UTC day boundary.
- A shortfall is counts used elsewhere (the owner's phone closed the 14:39Z deficit of 6, `_records_/2026-11-22/coach/refill-pass-log.csv`): log it elsewhere, flag it only above 6 with no owner activity; only a count above the prediction flags the model.
- The four long timers of 10-31 and 11-03 are unverifiable: a historical oddity, no part of the rule.
