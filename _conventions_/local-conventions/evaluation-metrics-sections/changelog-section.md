---
title: Changelog
created: 2026-11-23T09:02:25Z
modified: 2026-11-23T09:02:25Z
version: 0.1.0
sequence: 17
description: 1.1.2, 2026-11-05 - family A corrected - duration p90 and the attempts distribution are emitted today
---
## Changelog

- 1.1.2, 2026-11-05 - family A corrected: duration p90 and the
  attempts distribution are emitted today by
  `_tools_/retro_report.py` 1.4.0 (PR #30), not "not yet emitted"
  as the 1.0.0 text said; the tool-route extension is marked
  landed (same PR). Attempts read from the unit's top-level
  `attempts` field, `result.attempts` a fallback only (Issue
  #316, filed by the tool-development 0647 run, assigned to
  lastwar-knowledge-organizer by the tool-development 0732 run).
- 1.1.0, 2026-11-01 - families D to G re-sourced onto the ops
  execution records of the
  [ops execution records](ops-execution-records.md) standard:
  the retro's, tool developer's, organiser's and integrator's
  own runs are now measured from their structured execution
  records under `_records_/<date>/<ops-activity>/`, and commit
  and PR traces are demoted to cross-check only. The
  data-gap statements move accordingly - run metrics exist
  from 2026-10-31 (period 0 reconstructed), entry-state
  metrics still wait on the improvements backlog, and the
  planner remains proxied until its log migrates in. The
  tool-route backlog text is aligned (ops execution records
  among its readers).
- 1.0.0, 2026-10-31 - first version, under the owner direction
  of 2026-10-31 to create evaluation metrics for the system
  itself and monitor them - seven families (execution
  efficiency, perception completeness, generalisation and
  discovery, retro effectiveness, tool developer impact,
  knowledge organiser impact, loop health), the monitoring
  cadence and first threshold set, and the tool route extending
  _tools_/retro_report.py, filed into the tool-developer backlog.
