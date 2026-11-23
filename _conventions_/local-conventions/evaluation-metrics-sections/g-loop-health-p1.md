---
title: G. Loop health part 1
created: 2026-11-23T09:02:25Z
modified: 2026-11-23T09:02:25Z
version: 0.1.0
sequence: 12
description: Daily snapshot at the retro, from the records the loop itself leaves.
---
## G. Loop health

Daily snapshot at the retro, from the records the loop itself
leaves. Sources - the queue run records under `_records_/<date>/`,
the ops execution records of the loop activities under the
[ops execution records](ops-execution-records.md) standard,
the retro files under `_records_/retro/`, the improvements
backlog, and the pool itself through `_tools_/queue.py stats`
and the unit frontmatter. The git log is cross-check only.

- **Standing job run rate** - for each standing job, runs that
  left their execution record over runs expected: ticker passes
  (queue run records against the 30 minute cadence), planner
  cycles (units produced and the planner log - the one job
  still proxied, below), the daily retro (its dated file and
  its execution record), the organiser and the tool developer
  and the PR integrator (their execution records, no-op runs
  included - a recorded no-op is a run, an absent record is a
  miss). Each job's rate is reported separately; an average
  across jobs would hide exactly the failure this family
  exists to see.
- **Backlog depth and oldest open age** - open entries in the
  improvements backlog, and the age in days of the oldest.
- **Queue depth and oldest unit age** - units waiting in inbox
  and claimed at snapshot time, and the age of the oldest
  waiting unit from its `created_at`, with any unit past its
  `expires_at` still unexecuted counted and named. These two
  are the capacity metrics the 2026-10-31 loop review found
  missing (its open link 4); the snapshot is persisted into the
  retro data output so the series is historical, not a number
  that evaporates when the pool drains.

