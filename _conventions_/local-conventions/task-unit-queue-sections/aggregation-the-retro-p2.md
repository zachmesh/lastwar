---
title: Aggregation - the retro_report.py specification part 2
created: 2026-11-23T08:37:05Z
modified: 2026-11-23T08:37:05Z
version: 0.1.0
sequence: 38
description: Its only data sources are inside the repository - the unit results in _queue_/done and the
---
Its only data sources are inside the repository - the unit
results in `_queue_/done` and the execution records in
`_records_`. Its only outputs are inside the repository, in
the standing cross-day series at `_records_/retro/` beside
the date folders, registered here as its convention - one
daily retro file per local date at `_records_/retro/<date>.md`
and the rolling metrics file at `_records_/retro/rolling-7d.md`,
both written by the retro pass, and the tool's metrics
appendix for the window ending on a date at
`_records_/retro/<date>-data.json` (canonical) with the same
numbers rendered as tables at `_records_/retro/<date>-data.md`
for the retro file to cite. The retro files are derived
artifacts: they are regenerated from the unit results, which
remain the immutable source (C1), and a regenerated appendix
states the pool state it was derived from - the scanned unit
count and a hash over the scanned units. Re-running the tool
over the same window and the same pool overwrites the
appendix with identical content; it never appends a copy.
The tool was validated on a fixture pool in /tmp - units with
complete stats, legacy stats missing the required keys, a
result-less unit resolved through its day INDEX, a file with
no frontmatter, and a unit outside the window - with the
aggregates asserted against hand-computed figures and a
second run byte-identical to the first.

