---
title: Donation refill - what the 14:57:57Z datum shows and a sharper test
created: 2026-11-23T07:02:00-08:00
modified: 2026-11-23T07:02:00-08:00
level: L0
version: 1.0.0
description: Verifier check of the 35-minute refill datum from the 1441 donations run, its limits, the conflict with older timers and the predictions that would confirm or refute it
status: unverified
grounded_in:
  - source: _records_/2026-11-22/alliance-donations/1441-queue-run.md and its CSV
  - source: _records_/2026-11-22/alliance-donations/1012-t1-test.md and 1432-t2-test.md
  - source: timers in _records_/2026-11-22/alliance-donations/0319-queue-run.md and _records_/2026-11-11/alliance-donations/0434-queue-run.md
---

# Donation refill check

**Arithmetic holds.** T1 timer 10:12:47.107Z + 5:10 ends 10:17:57.107Z; the 1441 timer read 14:40:58.397Z at 16:59 ends 14:57:57.397Z; gap 16,800.29 s; entry count 8 gives 2,100 s a refill. No donation tap lies between: T2 was read-only and no donation record sits between 1012 and 1441.

**What it is not yet.** A derivation, not a confirmation. Any pair of gap and entry count yields a period, and the count fits by construction. It assumes the count was 1 after the first timer and that refills sit on a fixed clock. A later count cannot confirm it alone: periods from 2,000 to 2,200 s give the same count at many hours.

**Conflict.** Timers read right after a refill were 18:47 (11-22 0319) and 18:58 (11-11 0434): about 19 minutes on those days, and 11-04 shows 9 counts in 2h55m. 10-31 read 48:50, longer than 35. The period has varied, so the old 20 was not only a guess and 35 may not be constant [G].

**Sharp test, no extra runs.** The 2,100 s grid from 14:57:57Z: 15:32:57, 16:07:57, 16:42:57, 17:17:57, 17:52:57, 18:27:57, 19:02:57. Predict entry count = 1 + grid points passed (17:45Z gives 5, 17:55Z 6, 18:30Z 7), and the next last-tap timer must end on a grid point within 3 s; a chance match is 0.5 percent. Log entry time and count, last tap time, timer and read time; per pass T = (timer end - previous timer end) / entry count. Two passes that agree within 1 percent settle rule 8.

**Optional tail, 17:44 to 17:48Z start.** The first timer is then under 9 minutes: wait it out, read the count (predict 1/30), tap once more, read the second timer: about 34:30 if T is 35 minutes, about 19 minutes if the old rate returned. Cost: one tap, 1,000 coin, 8 minutes.

**Schedule.** A pass near 17:45Z is safe under either rate; counts only accumulate, the cap is 30.

**T2 side note.** The coin cost fits 100 x (level + 1) at levels 1, 2, 5, 7 (T1, T2) and 8, 9 (earlier records): six levels, no mismatch.
