---
title: First retrospective hardening target - radar-tasks
created: 2026-11-23T09:03:33Z
modified: 2026-11-23T09:03:33Z
version: 0.1.0
sequence: 36
description: The first profile named for retrospective hardening under this protocol is radar-tasks.
---
### First retrospective hardening target - radar-tasks

The first profile named for retrospective hardening under this
protocol is radar-tasks. Its failure history in the audited
days is specific: on a stack day a radar unit never entered the
radar screen at all (the rotating base entry icon pointed at
the wrong target and the pass closed without the screen); on
the release day the map pins - the subtask rule R7 now protects
- went untapped while claims were worked; and the special pin
tasks that Quick Execute does not cover were left without a
closing read. The hardening goal is a complete radar profile:
the task types and their refresh, the exact coverage of Quick
Execute and its exceptions, the handling of each pin task type,
the stack and release scoring rules, and the inventory cap
management that keeps stored tasks refreshing. The completion
standard is not this document's say-so - later execution units
verify the profile field by field against the game, under the
feedback loop above, and the profile rises to proficient only
when the key fields carry measured or dual-source support.

Execution results under this protocol are also the data of the
retro review mechanism (task unit queue design, section 14) -
what units measured, gained and were blocked by is aggregated
there, and its execution-knowledge actions land back here as
profile hardening. The aggregation tool of that mechanism,
`_tools_/retro_report.py`, is implemented (2026-11-01) to the
section 14 specification and writes its metrics appendix into
`_records_/retro/`.

