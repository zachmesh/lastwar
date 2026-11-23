---
title: G. Loop health
created: 2026-11-23T08:36:55Z
modified: 2026-11-23T08:36:55Z
version: 0.1.0
sequence: 8
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

Thresholds - the oldest open backlog entry over 7 days is
named. Any expired-but-unexecuted unit is named. A daily job
(retro, organiser) missing its artifact on any day is named the
next day; the ticker shortfall is named when a day's passes fall
under 90 percent of the cadence expectation.

Known defects - the planner's own log lives outside the
repository (in the goal workspace), so its run rate is proxied
by produced units until the log is mirrored in as execution
records - the migration item the ops standard names. The
retro's own run rate has the one-day blind spot the loop
review accepted - a retro that never ran leaves neither file
nor record, and is only visible to the next one. Device
locks and maintenance distort the ticker expectation; the retro
annotates known distortions rather than treating the raw rate
as a verdict.

