---
title: Strategy Conformance
created: 2026-11-23T08:48:32Z
modified: 2026-11-26T16:08:36Z
version: 1.8.0
description: strategy_conformance.py, the read-only counts-only watchdog that checks the strategy reaches the queue, with its tests
---

# Strategy conformance

`strategy_conformance.py`: does the strategy reach the queue and the game? It reads the queue folders and each unit's frontmatter,
prints counts only and writes nothing (but `--accept-exempt-list`, below).

`python3 _tools_/strategy-conformance/strategy_conformance.py [--hours 12] [--since TIME] [--plan CSV] [--exempt-list CSV] [--format text|json]`;
exit 0 conforming, 1 an alarm, 2 the queue cannot be read. Alarms, each threshold a flag: no execution in 45 minutes; an idle builder, lab or queue
slot over 30 minutes (`slots_blocked_capacity` is subtracted); the share of unit-hours serving a ranked item under 60 percent; growth partial rate over
35 percent; a top plan item not started two hours after its trigger; an exempt-list error. A ranked item is a plan item id in `serves` with a row in the
newest forecast ledger (`queue.py validate`'s check); with no ledger an id counts by shape, said in the output. The plan file is a CSV
`rank,item,trigger_at,serves`.

Coverage prints the rolling window (context) and since the roster remap landed (the verdict), each with the units serving nothing and their hours. Hours
decide, units are the trend; percentages print to one decimal, the alarm compares unrounded. The cutover is `--since`, else
`_tools_/state/strategy-cutover.json`, else git (the remap's merge).

The exempt list (`serves-exempt-list.csv`, the Strategist's, newest in a `strategy` folder; the parser `exempt_list.py` is the Toolsmith's): every roster
regular is `plan`, `income` or `exempt`, no id outside the roster unless its optional `kind` is `oneoff` (a test or probe, held to its review date), ledger rows for PL ids; any error alarms. The baseline is never re-based silently:
a changed line needs a newer `decided_utc`; only `--accept-exempt-list` records it. DEFINITION B prints beside A: hours of plan and income regulars over
hours without the exempt ones; it never decides the alarm.

Tests (`test_conformance.py` 58, `test_exempt_list.py`): `python3 -m unittest discover -s _tools_/strategy-conformance`.
