---
title: Tool route part 1
created: 2026-11-23T09:02:25Z
modified: 2026-11-23T09:02:25Z
version: 0.1.0
sequence: 15
description: The computation extends _tools_/retro_report.py; it does not become a second tool.
---
## Tool route

The computation extends `_tools_/retro_report.py`; it does not
become a second tool. Reasons - the families that read the done
pool (A, the recurrence half of D, the series E reads) must
share one scan and one unit-date attribution with the retro
aggregation, or the system gets two truths about the same units;
the output contract already exists - one canonical appendix per
window end at `_records_/retro/<date>-data.json` with its
Markdown rendering, its derived-from hash and its
byte-identical re-run - and these metrics ride it as an
additional top-level `system_metrics` object, versioned by the
tool's own version field; and the daily retro already runs the
tool, so no new scheduled step appears. The families that read
outside the pool (B from coverage reports, C from the candidate
register, F from profiles and organiser notes, G from a pool
snapshot) are separate input readers inside the same tool, each
emitting its section or its data-gap independently - a missing
coverage report degrades family B, never the run.

Filed into the tool-developer backlog, in the backlog's own
terms:

