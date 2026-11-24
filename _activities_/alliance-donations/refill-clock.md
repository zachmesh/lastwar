---
title: Alliance donations refill clock
created: 2026-11-23T17:53:50Z
modified: 2026-11-24T02:14:19Z
version: 0.5.0
description: The settled refill rate of the donation count, one per 20 minutes on a fixed clock, with the evidence, the open items and the next prediction
---

# Alliance donations refill clock

Researcher's note `_records_/2026-11-22/research/donation-refill-settled.md` settles digest rule 8: verified, 2026-11-23. The dated passes are in [refill passes](refill-passes.md).

## The rule

"The count is a pool refilling one per 20 minutes on a fixed clock (grid :17:57, :37:57, :57:57 on 2026-11-23), cap 30, so 3 an hour. A spent pool's grey timer ends on that grid. A pass's entry count is 1 + floor((entry time - last timer end) / 20 min), less counts used elsewhere. Each pass logs entry time and count, every tap time, and the first timer with its read time." Re-anchor on each pass's own timer end.

## The formula as the Coach checks it

predicted = max(0, min(30, 1 + floor((entry - anchor) / 20 min) - taps since the anchor)). The anchor is the last timer end read in a pass that spent the pool; the taps are witnessed taps since; an entry before the anchor gives 0. At 30 the cap hides the answer (10 hours without a pass loses refills): keep the gap under about 9 hours.

## Limits

- The grid was first anchored on 2026-11-23; each pass re-anchors on its own timer end.
- Elsewhere use is unobservable and only lowers the count (the owner's phone closed the 14:39Z deficit of 6, `_records_/2026-11-22/coach/refill-pass-log.csv`): log a shortfall as elsewhere, flag it only above 6 with no owner activity. The clock is refuted only by a count above the prediction or a timer end off the grid.
- The four long timers of 10-31 and 11-03 are unverifiable, a historical oddity. The 4/30 read at 07:41Z on 11-23 is about 26 counts used elsewhere only as a guess [G].
