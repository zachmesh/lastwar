---
title: Changelog part 7
created: 2026-11-23T09:03:48Z
modified: 2026-11-23T09:03:48Z
version: 0.1.0
sequence: 61
description: 0.14.0, 2026-11-01 - section 14 gains a cross-reference to the ops execution records standard - the
---
- 0.14.0, 2026-11-01 - section 14 gains a cross-reference to
  the ops execution records standard: the loop's own
  activities are executions and record themselves in the
  repository, and the retro measures them from those records.
- 0.13.0, 2026-11-01 - a cross-reference to the new push and
  PR policy: the queue's own outputs are tier-1 direct pushes,
  and changes to the design and tools are tier-2 pull requests
  under the audit of section 14's loop-health check.
- 0.12.0, 2026-11-01 - section 14 gains a cross-reference to
  the new evaluation metrics specification - the system-level
  companion that measures execution efficiency, perception,
  discovery, retro effectiveness and the impact of the tool
  developer and the knowledge organiser, with its computation
  extending _tools_/retro_report.py.
- 0.11.0, 2026-11-01 - the aggregation of section 14 is
  implemented as `_tools_/retro_report.py` - per regular, per
  day and rolling window aggregates over the done pool, the
  records INDEX fallback for result-less units, parse errors
  listed rather than skipped, no-data regulars stated, and
  the metrics appendix landed at
  `_records_/retro/<date>-data.json` with its Markdown
  rendering, byte-identical on a re-run over an unchanged
  pool; fixture validated in /tmp against hand-computed
  figures.
