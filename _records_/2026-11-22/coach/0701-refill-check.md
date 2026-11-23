---
title: Independent check of the donation refill datum and the pre-registered test
created: 2026-11-23T15:02:00Z
modified: 2026-11-23T15:02:00Z
version: 1.0.0
description: Coach check of the researcher's refill derivation - arithmetic, the 89 recorded cooldown timers against a 35-minute and a 20-minute grid, and the predictions both hypotheses make for the 17:44Z donations pass, registered before the data
status: done
activity: coach
run_id: coach-2026-11-23-0701
trigger: researcher note donation-refill-check.md
started_at: 2026-11-23T14:57:00Z
finished_at: 2026-11-23T15:02:00Z
duration_seconds: 300
verified: no
grounded_in:
  - source: _records_/2026-11-22/research/donation-refill-check.md
  - source: the alliance-donations records of 2026-10-26 to 2026-11-23, timers listed in donation-timers.csv
---

# Refill check

**Arithmetic holds.** T1 ends 10:17:57.107Z, the 1441 timer 14:57:57.397Z, gap 16,800.29 s. Both ends fall at 57 s past the minute, within 0.3 s: a chance of about 1 percent, so a grid on whole minutes is likely. It does not choose a period: 280 minutes is 8 times 35 and also 14 times 20.

**The recorded timers disagree with 35 minutes.** Of 89 cooldown timers in the donation records since 2026-10-26 ([list](donation-timers.csv)), 85 are 20.0 minutes or less, none lies between 20 and 35, and four read 40.9 to 48.8 (10-31 twice, 11-03 twice). All 48 since 11-04 are 19.6 or less, the highest. On a 35-minute grid, 57 percent of timers fall at or under 20, about 51 of 89; 85 has a chance of 2 in 10^16. A 20-minute period fits the history; today's two timers, 5:10 and 16:59, fit either.

**But 20 minutes fails today's count.** Fourteen refills in 280 minutes would put the 1441 entry count near 15, not 8. So each hypothesis has one conflict: 35 minutes against 89 timers, 20 minutes against one count. The four long timers are unexplained under both. Possible: the period changed on 11-23, or the timer is not the refill clock.

## Pre-registered test ([table](refill-test-prereg.csv))

Registered 15:02Z, before the 17:44Z pass; count = 1 plus grid points passed since 14:57:57.397Z.

| Entry | H35 count, first timer ends | H20 count, first timer ends |
|---|---|---|
| 17:45Z | 5, 17:52:57 | 9, 17:57:57 |
| 17:55Z | 6, 18:27:57 | 9, 17:57:57 |
| 18:30Z | 7, 19:02:57 | 11, 18:37:57 |

Count 5 with an end near 17:52:57 supports 35; count 9 near 17:57:57 supports 20; anything else means no fixed grid. The count at entry separates them by 4, so it needs no second pass.

## The baseline is protected

`donations-pass-2026-11-23-001` is not_before 17:44Z; the next pass is 21:15Z and the next donations unit 00:30Z on 11-24. No queued tap falls before 17:44Z; a hand tap would void the prediction, so none should be made. I count the pass under policy 2532 and log the entry count, tap times and timers.

## Limits

The timer list mixes after-tap and waiting timers, matched by wording; it is a pattern count, not a clean sample.
