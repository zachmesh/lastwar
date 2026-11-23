---
title: Tool route
created: 2026-11-23T08:36:55Z
modified: 2026-11-23T08:36:55Z
version: 0.1.0
sequence: 10
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

> IMP tooling - extend _tools_/retro_report.py with the system
> evaluation metrics of
> _conventions_/local-conventions/evaluation-metrics.md. Add a
> top-level system_metrics object to
> _records_/retro/<date>-data.json and its Markdown rendering,
> covering families A to G as specified there - the done pool
> aggregates (adding the attempts distribution and the duration
> p90 to family A in the same change), the scout coverage
> reports, the candidate register in _activities_, the
> improvements backlog, the ops execution records of the loop
> activities, and a pool snapshot for queue depth and oldest
> unit age. Target metric - the
> share of the specification's metrics emitted as figures
> rather than data-gaps in the daily appendix, from its current
> value (family A only, partially) toward the full set.
> Every metric that cannot be computed from repository data is
> emitted as a data-gap entry with its reason, never estimated.
> Re-running over unchanged inputs stays byte-identical.
> Validated on a fixture pool and scratch records in /tmp
> against hand-computed figures before it writes the live
> series.

Landed: PR #30 (merge fe87b043e, 2026-11-01) implemented this
extension as `_tools_/retro_report.py` 1.4.0 - the top-level
`system_metrics` object, the duration p90 and the attempts
distribution in family A, and the remaining data gaps by name.
The "not yet emitted" wording in family A above is superseded
accordingly.

The queue tool's stats validation (the standing tooling backlog
item the loop review calls item b) stays a separate entry -
several metrics above read fields that only its enforcement
makes trustworthy, and the retro names that dependency rather
than merging the two jobs into one unmeasurable lump.

