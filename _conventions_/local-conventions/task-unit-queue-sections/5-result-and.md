---
title: 5. Result and result statistics
created: 2026-11-23T08:37:05Z
modified: 2026-11-23T08:37:05Z
version: 0.1.0
sequence: 8
description: On completion the executor writes a result mapping into the same frontmatter (via _tools_/queue.py complete) and
---
## 5. Result and result statistics

On completion the executor writes a `result` mapping into the same
frontmatter (via `_tools_/queue.py complete`) and the unit moves to
`done`. A completed unit therefore carries its whole life in one
structured document - task, claim, result and statistics.

```yaml
result:
  status: done            # done, partial, failed, skipped-needs-owner
  started_at: 2026-10-28T10:30:00Z
  finished_at: 2026-10-28T10:34:00Z
  duration_seconds: 240
  executor: executor-1
  summary: Claimed the Daily Freebie and the login points
  claimed: [daily-freebie, login-200]
  claimed_count: 2
  evidence: _records_/2026-10-28/vip-rewards/1030-queue-run.md
  follow_up: none
  stats:
    points_gained: 200
```

Core result fields are fixed (status, times, duration, executor,
claimed list and count, evidence, follow-up). The `stats` mapping is
open - each activity defines its own keys in its `_activities_`
metadata (points gained, chests claimed, donations made, trucks
dispatched), and executors pass them as key values at completion.

**Learned estimates** - owner direction 2026-10-28. A task type's
typical execution time is estimated from the pool itself - the
median `duration_seconds` of its completed units, in minutes rounded
up and clamped to the cap, once at least 3 completed samples exist;
the static production defaults apply before that. `sync` stamps
each new unit with the current learned estimate, and the stats
report shows it next to the sample count, so a type whose typical
time creeps toward the 15 minute cap is visible and gets split at
intake instead of silently overrunning.
Because the keys are structured, `_tools_/queue.py stats` aggregates
reliably across the whole pool - counts by state and by regular,
result status totals, duration averages and maxima, units finished
after their expiry, units expired while waiting, and claims past
their lease - in text, YAML or JSON.

The matching `_records_` execution file is still written as today
(C1 append-only audit); the unit references it under `evidence`.

