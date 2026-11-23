---
title: Donations units counted by the tracker policy
created: 2026-11-23T10:36:00Z
modified: 2026-11-23T10:36:00Z
version: 1.0.0
description: Coach count of the alliance-donations units in the 24 hours to 10:33Z under the coordinator's tracker policy - done, partial, failed, uncalibrated - and the day totals of witnessed landed taps
status: done
activity: coach
run_id: coach-2026-11-23-0236
trigger: coordinator decision 2532 on the donations tracker policy
started_at: 2026-11-23T10:32:00Z
finished_at: 2026-11-23T10:36:00Z
duration_seconds: 240
verified: no
grounded_in:
  - source: _records_/2026-11-22/team-operations/2532-donations-tracker-policy.md and research/donation-close-ruling.md
  - source: the alliance-donations records and queue units listed in donations-units-new-rule.csv
---

# Donations count, policy 2532

Rule applied: done when the unit closes with the count spent (green to grey with a timer, witness read) or finds it spent; partial when it stops before; failed when the panel is not reached; an entry at 1/30 closes flagged uncalibrated. A tap is witnessed when the live count fell by exactly the taps taken, or on the last tap green to grey with a timer and the Tech EXP or badge witness up 0.1K. Rows: [units](donations-units-new-rule.csv). Times are Mac UTC; record file names mix Pacific and UTC, so each row's time comes from its text.

## Last 24 hours, to 10:33Z

| Unit | Taps logged | Taps witnessed | New status |
|---|---|---|---|
| 0921 | 6 | 0 | partial |
| 1119 | 0 | 0 | uncalibrated |
| 1146 | 4 | 0 | partial |
| 0203 | 3 | 3 | done |
| 1003 | 14 | 14 | partial |
| 1803 | 0 | 0 | failed |
| 0709 | 2 | 2 | partial |
| 0711, two passes | 8 | 8 | partial |
| T1 test, a continuation | 1 | 1 | done, flagged uncalibrated |

**Queue units: 8.** Done 1, partial 5, failed 1, uncalibrated 1. The records closed all eight partial, so the done rate moves from 0 of 8 to 1 of 8. The T1 test is not a queue unit.

**Witnessed landed taps: 28** of 38 logged. By Mac UTC day: 2026-11-22, 41 witnessed of 57 logged (it includes the 0114 unit, 24 witnessed by batch count reads, outside the 24 hours); 2026-11-23 to 10:33Z, 11 of 11.

## Where witnesses are missing

- Burst taps without a count read: units 0921 and 1146 logged 10 taps and witnessed none. In 1146 the badge rose 0.3K over a burst of 3, which supports but does not witness it.
- The 0114 unit's last batch of 6 and its final count were not witnessed.
- Fix for the operator: one tap per read, or a count read after each batch, and the Tech EXP or badge before and after the last tap.

## Limits

The unit 0711 passes (records 1002 and 1010) are one unit; its record called the second pass done under the old floor rule, and under this rule it stopped at 1/30. Refill timing is not measured here; the planner's rule 8 log owns it.
