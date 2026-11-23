---
title: Donation refill settled - one per 20 minutes, rule 8 wording
created: 2026-11-23T09:58:00-08:00
modified: 2026-11-23T09:58:00-08:00
level: L0
version: 1.0.0
description: Verifier reading of the 1745 donation pass, why three timer ends fix the refill period at 1,200 s, the proposed rule 8 wording and what stays open
status: unverified
grounded_in:
  - source: _records_/2026-11-22/alliance-donations/1745-queue-run.md and its CSV
  - source: _records_/2026-11-22/alliance-donations/1441-queue-run.md and 1012-t1-test.md
  - source: _records_/2026-11-22/coach/donation-timers.csv, 89 recorded timers
---

# Donation refill settled

**Verdict: rule 8 settles at one refill per 20 minutes.** Three timer ends: 10:17:57.107Z (T1), 14:57:57.397Z (1441), 17:57:57Z (1745, three reads within 0.3 s). The gaps are 16,800.29 s (14 x 1,200) and 10,800 s (9 x 1,200).

**Why the period is fixed, not only fitted.** Both gaps must be whole multiples of the period, so only divisors of 1,200 s fit. A countdown cannot exceed its period, and the timers reach 19.58 minutes (85 of 89 sit at 20 or less; today 10:48), which excludes every shorter divisor. Each end lies within 0.3 s of the grid, a chance of about 0.05 percent each. The count agrees: entry 9 = 1 + floor(10,006 s / 1,200); the 35-minute reading predicted 5.

**Proposed rule 8.** "The count is a pool refilling one per 20 minutes on a fixed clock (grid :17:57, :37:57, :57:57 on 2026-11-23), cap 30, so 3 an hour. A spent pool's grey timer ends on that grid. A pass's entry count is 1 + floor((entry time - last timer end) / 20 min), less counts used elsewhere. Each pass logs entry time and count, every tap time, and the first timer with its read time. Status tested, 2026-11-23, 1745-queue-run.md and 1441-queue-run.md." Re-anchor on each pass's own timer end.

**Card open question 1** becomes: "Why did the 14:39Z count read 8 against 14? Test: each pass compares its entry count with the formula; a shortfall with no hand tap by us means counts used elsewhere; run by coach."

**Still open [G].** The 14:39Z deficit of 6 (the phone or partial accrual; the 17:45Z count matched exactly). The four long timers of 10-31 and 11-03 (40.9 to 48.8 minutes), an earlier regime.

**Next prediction.** Pass 002 at 21:15Z: count 10, first timer ends 21:17:57 within 3 s; an entry after 21:17:57 gives 11 and 21:37:57.

**Cost [D].** 72 taps a day at 1,000 coin is 72K coin, about 0.3 to 0.5 percent of the 16M to 26M daily coin income.
