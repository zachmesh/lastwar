---
title: The refill test scored - H20 holds, H35 rejected
created: 2026-11-23T18:00:00Z
modified: 2026-11-23T18:08:00Z
version: 1.0.1
description: Coach scoring of the donations pass of 17:45Z against the predictions registered at 15:02Z, the policy 2532 count of the pass and of unit 1441, the day totals, and the predictions registered for pass 002
status: done
activity: coach
run_id: coach-2026-11-23-0953
trigger: coordinator message of 17:52Z on the refill test
started_at: 2026-11-23T17:50:00Z
finished_at: 2026-11-23T18:00:00Z
duration_seconds: 600
verified: no
grounded_in:
  - source: _records_/2026-11-22/alliance-donations/1745-queue-run.md and its CSV; 1441-queue-run.md and its CSV
  - source: refill-test-prereg.csv, registered 15:02Z with the scoring rule agreed with the researcher
---

# The refill test scored

## Against the pre-registration

| Test | H35 predicted | H20 predicted | Observed |
|---|---|---|---|
| Primary: first timer end | 17:52:57.397 | 17:57:57.397 | 17:57:57.063, .286 and 56.966 from three reads |
| Secondary: entry count at 17:45:43Z | 5 | 9 | 9 |

H20's end is 0.11 to 0.43 s from its grid point; H35 is 300 s off. A match inside 0.5 s has a chance of 0.08 percent on a 1,200 s grid (0.5 percent at the 3 s criterion I registered). **H20 is confirmed on both tests, H35 rejected.** The count matched with no consumption between the 14:40:53Z zeroing tap and 17:45Z: nine grid points passed, nine counts.

**Still open.** The 14:39Z entry count was 8; the grid from the 10:12:44Z zeroing tap gives 14 (10:17:57 to 14:37:57), a shortfall of 6 used elsewhere or never accrued; the operator's "fits 20 minutes too" is loose. The four timers of 40.9 to 48.8 minutes (10-31, 11-03) remain unexplained.

## Policy 2532 counts

- **Pass 001, 17:45Z:** entry 9/30, nine taps. Taps 1 to 8 witnessed by the count falling one by one. Tap 9 went green to grey with a timer (00:10:48) whose end lies 0.11 s from the grid: witnessed under the researcher's amended close rule (the grid is the witness; a 0.1K rise is no longer required). DONE.
- **Unit 1441, 14:39Z:** entry 8/30, eight taps witnessed, the last green to grey with timer 00:16:59 and the badge up 98.8K to 99.7K. DONE.
- **Day totals of witnessed landed taps.** UTC day 11-23 to 17:52Z: 28 of 28 logged (11 before, 8, 9); rolling 24 hours: 42. The amended rule applies from 11-23 on; the units of 11-22 keep their old status, since the grid phase is anchored only on 11-23.

## Pass 002, registered 18:00Z before the data ([table](refill-test-prereg-2.csv))

Entry count = 1 plus floor((entry - 17:57:57.397Z) / 20 min): 21:15Z gives 10, 21:20Z and 21:30Z give 11, 22:00Z gives 13, 00:30Z gives 20. The primary test is the first timer end after the last tap, read within a minute, landing on a grid point (:17:57, :37:57, :57:57) within 1 s. A lower count means counts used elsewhere, not a refutation. The operator keeps logging the first timer with its read time to the second; reading the badge or Tech EXP in the same frame corroborates and costs no step.
