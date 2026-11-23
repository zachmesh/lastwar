---
title: 3. The fixes, and where each one landed part 1
created: 2026-11-23T08:36:59Z
modified: 2026-11-23T08:36:59Z
version: 0.1.0
sequence: 4
description: Queue discipline rules R1 to R8 are written into the task unit queue design, section 11,
---
## 3. The fixes, and where each one landed

Queue discipline rules R1 to R8 are written into the
[task unit queue design](task-unit-queue-design.md), section 11,
version 0.7.0. The collection fixes live in the new
[daily collection ledger](daily-collection-ledger.md) and in the
activity metadata named below.

| Audit cause | Fix | Landed in |
| --- | --- | --- |
| D - inference instead of a live read, 6 units | R1 - a unit closes only on a same-unit live read. A hidden or blocked counter closes the unit as unverified and auto-enqueues a named re-read. Arithmetic, presumed, by-result and ranking-row figures are banned as closing counts | task-unit-queue-design.md section 11; alliance-donations INDEX closing rule |
| C - tap method failed, no pivot, 19 units | R2 - two no-change taps end the method. The executor re-grounds the point fresh, observes twice, and switches variant inside the same unit - measured centre, long-press, or a different entry path | task-unit-queue-design.md section 11 |
| E - same blocker, no escalation, 42 units | R2 - the second same-cause partial must change method. The third writes the blocker into the activity metadata, changes the entry route before any further unit of that type runs, and is named in that day round summary. A fourth identical partial is a process failure, not a result | task-unit-queue-design.md section 11 |
| A and F - quota gaps found at the deadline, slots and preconditions unread | R3 - quota types (trucks dispatch 5 and plunder 4, donations 30) carry two checkpoints per cycle, six hours and two hours before the cycle end. A checkpoint reads the counter live; a shortfall raises the next unit of that type to priority 1 | task-unit-queue-design.md section 11; alliance-donations INDEX scheduling rule |
| A and G - Arms Race phases judged at the end, 4 true misses | R4 - the phase is evaluated at its start. The first unit inside a phase reads the score and every scoring path; a phase with no path inside the red lines is reported to the owner as skipped-needs-owner early in the phase, never discovered at its end | task-unit-queue-design.md section 11 |
| A - gaps deferred across a window boundary, 6 units | R6 - no gap may be deferred across a window boundary inside the last 60 minutes of the window. The unit finishes inside itself or enqueues a priority 1 successor expiring at the window close, named in its summary | task-unit-queue-design.md section 11 |
| B - a subtask starved inside its own unit, 6 units | R7 - a subtask deferred twice in one day is promoted to the first action of the next unit of that type, or to a unit of its own | task-unit-queue-design.md section 11 |
