---
title: Strategy Conformance
created: 2026-11-23T08:48:32Z
modified: 2026-11-23T17:22:29Z
version: 1.3.0
description: strategy_conformance.py, the read-only counts-only watchdog that checks the strategy reaches the queue, with its tests
---

# Strategy conformance

`strategy_conformance.py`: does the strategy reach the queue and the game? It reads the queue folders and each unit's frontmatter,
prints counts only (no unit text or ids), and writes nothing.

`python3 _tools_/strategy-conformance/strategy_conformance.py [--hours 12] [--since TIME] [--plan CSV] [--format text|json]`; exit 0 conforming,
1 an alarm, 2 the queue cannot be read. Alarms, each threshold a flag: no execution in 45 minutes; a builder, lab or queue slot
idle over 30 minutes (latest building-queues, research-queue or troop-training read; the planner's `slots_blocked_capacity` is
subtracted and printed beside it); coverage serving a ranked item
under 60 percent, in units and in unit-hours; growth partial rate over 35 percent; a top plan item not started two hours after
its trigger. A ranked item is a plan item id in `serves` with a row in the newest forecast ledger, the check `queue.py validate` uses; an exempt word, an id with no row and other wording ("snapshot (Story 868)") are not, and are counted apart; with no ledger an id counts by shape, said in the output. The plan file is a CSV
`rank,item,trigger_at,serves` kept by the strategist; without one that check says it was skipped.

Coverage prints two lines: the rolling window (context) and since the roster remap landed (the verdict, which the alarm and the Coach
quote), each with the units serving nothing and their hours. The cutover is `--since TIME`, else
`_tools_/state/strategy-cutover.json` (`{"since": "ISO UTC"}`), else the first-parent git commit that introduced a plan item id as a roster
serves (the remap's merge); with none, the rolling figure is the verdict, said in the output. The JSON carries both.

Tests (`test_conformance.py`, 51) cover each alarm at its threshold, the ranked rule, the cutover, counts-only output, a byte-identical
tree afterwards and exit codes. Run: `python3 -m unittest discover -s _tools_/strategy-conformance`.
