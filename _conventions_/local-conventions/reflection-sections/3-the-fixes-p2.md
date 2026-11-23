---
title: 3. The fixes, and where each one landed part 2
created: 2026-11-23T09:01:51Z
modified: 2026-11-23T09:01:51Z
version: 0.1.0
sequence: 5
description: A and G - Arms Race phases judged at the end, 4 true misses R4 -
---
| A and G - Arms Race phases judged at the end, 4 true misses | R4 - the phase is evaluated at its start. The first unit inside a phase reads the score and every scoring path; a phase with no path inside the red lines is reported to the owner as skipped-needs-owner early in the phase, never discovered at its end | task-unit-queue-design.md section 11 |
| A - gaps deferred across a window boundary, 6 units | R6 - no gap may be deferred across a window boundary inside the last 60 minutes of the window. The unit finishes inside itself or enqueues a priority 1 successor expiring at the window close, named in its summary | task-unit-queue-design.md section 11 |
| B - a subtask starved inside its own unit, 6 units | R7 - a subtask deferred twice in one day is promoted to the first action of the next unit of that type, or to a unit of its own | task-unit-queue-design.md section 11 |
| H - by-design partials counted as failure noise, 11 units | R8 - chain continuation and stack posture get their own label in reporting, split from misses, so the daily miss count only counts units that failed their own objective | task-unit-queue-design.md section 11 |
| I - owner-named task with no escalation, crystal, 6 days, 0 units | R5 - an owner-named task incomplete after 24 hours rises to priority 1 and is named in every round summary until it closes. Crystal itself is now modelled and queued - see section 4 | task-unit-queue-design.md section 11; _activities_/crystal-shop/INDEX.md; queue unit crystal-shop-2026-11-01-0503 |
