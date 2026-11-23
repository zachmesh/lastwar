---
title: Cadence
created: 2026-11-23T08:32:53Z
modified: 2026-11-23T08:32:53Z
version: 0.1.0
sequence: 1
description: The hourly cadence of the knowledge organiser with the 2026-11-03 correction of the daily reset boundary
---
## Cadence

Hourly and incremental, as the standing job
`lastwar-knowledge-organizer`, working from a watermark in its
latest record; plus one fuller consolidation sweep of the
ended trade day on the first run after each trade-day
reset (02:00 UTC absolute boundary, about 18:00 PST
now, 19:00 PDT before the DST end). Correction,
2026-11-03 2032: the standing 19:00 local label is
superseded - the 1846 live counters and the PR 249
daily-reset tool fix settle the boundary. This profile
now states the settled boundary; the standing job's
schedule wording still states 19:00 and is an
owner-job definition, so the schedule text itself is
left for the owner or the daily retro, not rewritten
here. Filed as Issue #247; closure belongs to the
daily retro. Feedback order each run: unaddressed integrator review
points on profile PRs first, then the knowledge-organization
backlog entries, then new records since the watermark.
