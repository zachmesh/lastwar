---
title: Aggregation - the retro_report.py specification part 1
created: 2026-11-23T08:37:05Z
modified: 2026-11-23T08:37:05Z
version: 0.1.0
sequence: 37
description: Aggregation is specified here and implemented as _tools_/retro_report.py (landed 2026-11-01).
---
### Aggregation - the retro_report.py specification

Aggregation is specified here and implemented as
`_tools_/retro_report.py` (landed 2026-11-01). The tool
aggregates by task type, per day and over a rolling window -

```text
retro_report.py [--days 7] [--end YYYY-MM-DD] [--root DIR]
                [--out-dir DIR] [--format text|json]
```

`--root` is the repository root (default - the repository the
tool lives in); the pool is read at `<root>/_queue_` and the
appendix written to `<root>/_records_/retro` unless
`--out-dir` says otherwise. A unit belongs to the local date
of its `result.finished_at` in the queue timezone, falling
back to `started_at`, `planned_for`, and the date in its file
name. A unit file with no result is resolved against its day
INDEX in `_records_` and counted with status unknown and no
invented figures; a file that cannot be parsed is listed
under `parse_errors`, never silently skipped. The required
keys are `target`, `achieved`, `resources_gained`, `costs`
and `verified`, plus `blocker_category` whenever the unit
fell short of its target or closed partial, failed or
skipped-needs-owner; `points` is aggregated whenever present
but is not a required key, since it applies to scoring types
only and the pool carries no authoritative list of them.

- execution count, and the done, partial and
  skipped-needs-owner distribution;
- target attainment - achieved over target, summed and per
  unit;
- output per minute - resources gained and points, divided by
  execution minutes;
- total duration and median duration;
- the top repeated blockers, by `blocker_category` and by the
  named blocker;
- the unverified closing count - `verified` no, plus the units
  missing required stats keys.

