---
title: Completion markers ( completed/ ) part 2
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 7
description: Markers are live-only pool state, like the device token and the blockers - _queue_/.gitignore excludes completed/,
---
Markers are live-only pool state, like the device token and the
blockers: `_queue_/.gitignore` excludes `completed/`, so markers are
never committed and never reach the records branches. `sync` reaps a
marker once the unit's done record lands in the local pool - the
delivery caught up - or after 168 hours (7 days,
`COMPLETED_STALE_HOURS`). A valid marker older than 168 hours with
no local done record is reported as lost (issue #563): the delivery
never carried that closing, so the retro can triage the named unit
instead of counting one more bare integer, and the suppression
lapsing makes the gap visible instead of hiding it behind a stale
file. `sync` also splits every reap by reason in its JSON
(`completion_markers_reaped_by_reason`: done-landed, aged-out,
invalid), so the ticker's sync section quotes the aged-out subset
as lost instead of folding it into the bare reaped count
(issue #826).

The two stranded units of issue #726 - `harvest-2026-11-11-1003`
and `zombie-invasion-zombie-2026-11-10-014` - have no full unit file
in the live pool's `done/` and no live marker: their markers lapsed
under the 168-hour rule, so their closings count as lost to the pool
under issue #563. The marker-count discrepancy this surfaced is
tracked by issue #735.

