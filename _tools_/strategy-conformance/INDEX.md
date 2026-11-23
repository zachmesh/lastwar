---
title: Strategy Conformance
created: 2026-11-23T08:48:32Z
modified: 2026-11-23T17:05:46Z
version: 1.2.0
description: strategy_conformance.py, the read-only counts-only watchdog that checks the strategy reaches the queue, with its tests
---

# Strategy conformance

`strategy_conformance.py` turns Steer A's prototype into a tool: does the strategy reach the queue and the game? It reads the
queue folders and each unit's frontmatter, prints counts only (no unit text, no unit ids), and writes nothing.

`python3 _tools_/strategy-conformance/strategy_conformance.py [--hours 12] [--plan CSV] [--format text|json]`; exit 0 conforming,
1 an alarm, 2 the queue cannot be read. Alarms, each threshold a flag: no execution in 45 minutes; a builder, lab or queue slot
idle over 30 minutes (from the latest building-queues, research-queue or troop-training read; the planner's `slots_blocked_capacity` is
subtracted from the idle count and printed beside it, with the blocker text); coverage serving a ranked item
under 60 percent, in units and in unit-hours; growth partial rate over 35 percent; a top plan item not started two hours after
its trigger. A ranked item is a plan item id in `serves` with a row in the newest forecast ledger, the check `queue.py validate` uses; an exempt word, an id with no row and other wording ("snapshot (Story 868)") are not, and are counted apart; with no ledger an id counts by shape and the output says so. The plan file is a CSV
`rank,item,trigger_at,serves` kept by the strategist; without one that check says it was skipped.

Tests (`test_conformance.py`, 40) cover each alarm just under and over its threshold, the ranked rule, the window, counts-only
output, a byte-identical tree afterwards, exit codes and a run on this repository. Run: `python3 -m unittest discover -s _tools_/strategy-conformance`.
