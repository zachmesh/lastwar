---
title: Records pull requests - batch cadence part 1
created: 2026-11-23T09:02:35Z
modified: 2026-11-23T09:02:35Z
version: 0.1.0
sequence: 4
description: Owner decision, 2026-11-01 - records PRs are merged in batches every 4 hours, superseding cadence A
---
## Records pull requests - batch cadence

Owner decision, 2026-11-01 - records PRs are merged in
batches every 4 hours, superseding cadence A (the
2026-10-31 at 22:49 PDT decision that the integrator merge
every 15 minutes when new commits exist, so main stayed near
real-time). Rationale, from the same day's running: on
2026-11-01 the integrator merged more than 16 PRs, nearly
all of them routine records merges carrying zero review
value - the merge ceremony cost the loop passes and bought
no scrutiny. Records are append-only trajectories; nothing
in them is improved by being merged sooner.

A batch lands at the first integrator pass at or after each
of 19:00, 23:00, 03:00, 07:00, 11:00 and 15:00
America/Los_Angeles. The boundary set is chosen so a batch
lands right after the 19:00 trade-day reset and the 20:39
daily retro reads a complete trade day in main. Between
batches, main trails the live records by at most 4 hours;
writers and readers that need the live record read the date
branch, exactly as the records flow section above already
provides.

