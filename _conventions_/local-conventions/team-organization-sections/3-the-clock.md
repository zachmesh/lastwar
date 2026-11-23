---
title: 3. The clock and 4 more
created: 2026-11-23T07:02:07Z
modified: 2026-11-23T07:02:07Z
version: 0.1.0
sequence: 6
description: Time Owner Act
---
## 3. The clock

| Time | Owner | Act |
|---|---|---|
| every 15 min | coordinator | one tick: read, assign, verify, record |
| every 2 h | scout | one perception pass |
| 16:00 and 17:00 | scout/planner | pre-reset sweep pair (roster `[120, 60]`) |
| hourly | planner | pool hygiene and staging |
| 18:20 | coach | daily retro and dashboard |
| Sunday 18:30 | coach/coordinator | weekly improvement review |
| on assignment | operator/toolsmith/scribe | the bounded unit |

The coordinator's schedule is the only recurring schedule. Delegated
sessions cannot create their own schedules, so the coordinator wakes
them with `session-relay send` and collects the reply. A seat that is
idle is not a stopped loop.

## 4. Assignment and reply contract

Coordinator to seat:

```
ASSIGNMENT <id>
Question: <one sentence>
Evidence expected: <artifact path or measurement>
Completion condition: <what makes it done>
Deadline: <local time or tick>
Write scope: <paths>
Cap: <minutes, steps, cost>
```

Seat to coordinator:

```
STATUS: done | partial | blocked | no-op
ARTIFACT: <repository path or none>
MEASUREMENT: <the number the assignment asked for>
NEXT: <one bounded next action or none>
```

A reply without an artifact or a measurement is `partial`, not
`done`. Chat text alone never closes an assignment.

## 5. Work priority

1. **Incident** - the game is down, the control lock stands, the queue
   is corrupt, or a session is gone. The coordinator handles it before
   any play.
2. **Owner request** - an explicit owner instruction.
3. **P1 window** - a pre-reset sweep or a unit whose deadline is
   close.
4. **L1 play** - the next queued unit.
5. **L2 discovery** - perception and research.
6. **L3 improvement** - tools, knowledge and meta-work.

The queue is the only task list. Do not create a second list in chat
or in a seat folder.

## 6. Measurement and review

The coach owns the daily dashboard and the retro. The three families
are fixed in [evaluation metrics](evaluation-metrics.md) and extended
by [continuous play](continuous-play-team.md) section 2.

- **Daily** - L1 done rate, unverified, duration, attempts; L2 ledger
  coverage and red dots; L3 open/closed and recurrence.
- **Weekly** - compare the week with the previous one; name one
  meta-change; review one seat per day in rotation.
- **A metric without a source** is a data gap, never zero.
- **Association is not causation.** A tool landing is reported with
  the before/after windows and the game-change confounders named.

## 7. Failure playbooks

