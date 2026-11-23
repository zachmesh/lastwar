---
title: Where records live
created: 2026-11-23T08:38:24Z
modified: 2026-11-23T08:38:24Z
version: 0.1.0
sequence: 4
description: One file per run, at _records_/ YYYY-MM-DD/ ops-activity/ HHMM-run.md, where the date and time are the
---
## Where records live

One file per run, at
`_records_/<YYYY-MM-DD>/<ops-activity>/<HHMM>-run.md`, where
the date and time are the run's local finish time, and the run
is appended to that day's `_records_/<date>/INDEX.md` - the
same layout the game executions use. The ops activities with
standing profiles are registered under `_activities_`:

- `retro-review` - the daily retro pass.
- `tool-development` - the tool developer's runs.
- `knowledge-organization` - the knowledge organiser's runs.
- `pr-integration` - the PR integrator's runs.

Derived retro artifacts keep their standing home at
`_records_/retro/` (the retro file, its data appendix, the
rolling file, the improvements backlog); the retro's execution
record is the per-run file above and points at them.

