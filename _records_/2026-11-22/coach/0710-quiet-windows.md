---
title: Quiet windows in the plan triggers and the idle subtraction
created: 2026-11-23T15:10:00Z
modified: 2026-11-23T15:10:00Z
version: 1.0.0
description: Coach record of the four approved cu quiet windows entered as typed plan-trigger rows, the subtraction of their minutes from idle slot time, the revised idle numbers at 15:05Z with the other-device facts, and the missed slot B read
status: done
activity: coach
run_id: coach-2026-11-23-0710
trigger: coordinator relay of Steer A's approval of the cu windows
started_at: 2026-11-23T15:03:00Z
finished_at: 2026-11-23T15:10:00Z
duration_seconds: 420
verified: no
grounded_in:
  - source: coordinator message of 2026-11-23 on the cu windows, approved by Steer A and provisional until the owner answers the cu coordinator
  - source: _records_/2026-11-22/research-queue/1257-age-of-oil-survey.md, 1341-queue-run.csv and 1352-speedup-coin-v.csv
---

# Quiet windows and idle time

**Windows entered** in [plan-triggers.csv](plan-triggers.csv) as type quiet-window, status provisional: QW1 16:10Z to 16:35Z, QW2 17:10Z to 17:25Z, QW3 18:35Z to 18:50Z today, and QW4 08:00Z to 08:25Z daily from 2026-11-24. I built the rows from the coordinator's text; the planner's rows should match, and any difference is theirs to correct.

**Margins to the named triggers**: the donations pass at 17:44Z starts 19 minutes after QW2; builders free 2026-11-24T09:21Z, 56 minutes after QW4; the Food Output V Complete at 2026-11-24T17:30:30Z, 9 h 05 min from the nearest window; the Iron Output V Complete at 2026-11-25T02:39Z, 5 h 21 min. No named trigger falls inside a window.

**Subtraction.** [slot-idle-method.py](slot-idle-method.py) reads [slot-idle-intervals.csv](slot-idle-intervals.csv) and the quiet-window rows, and from now every idle figure I report is net of the minutes inside a window. Tested at 2026-11-24T10:00Z: 80 barracks-minutes subtracted (25, 15, 15 and 25). Today it subtracts 0, because the first window starts at 16:10Z.

## Idle at 15:05Z ([table](slot-idle-now.csv))

| Slots | 24 h | 6 h |
|---|---|---|
| builders | 50.5% | 0.0% |
| labs | 1.8% | 7.3% |
| training | 33.2% | 33.3% |
| all | 33.9% (4,395 of 12,960) | 12.7% |

Labs are revised from 75 to 52 idle minutes: the other device started Food Output V between 12:12Z and 12:51Z, so lab 1's idle time ended there, 29 to 68 minutes after the 11:42:55Z finish; the operator restarted lab 2 in 4 min 19 s.

## What else moved

Total Power rose 205,137 since 07:47Z (+0.14 percent): 7,800 from two Completes and 197,337 unattributed, inside the other-device window (told to the Strategist first). Slot B closed at 15:00Z with no Power Details read in the records; collect-first reads are 0 of 2. New drift: D16 slot B, D17 other-device actions not in the ledger and PL-04 and PL-10 stale, D18 the lab idle bound.
