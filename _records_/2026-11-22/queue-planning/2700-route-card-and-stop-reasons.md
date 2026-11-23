---
title: Route Card And Stop Reasons For The Unit Briefs 2700 2026-11-23
created: 2026-11-23T05:40:00-08:00
modified: 2026-11-23T06:20:00-08:00
level: L0
version: 1.4.0
description: The short card the unit briefs point to - the stop reasons, the stats for idle-slot reads and a pointer to the verified route table in the CSV beside it, written against the Coach's top partial causes
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0540-route-card
trigger: coordinator message with Steer A's flip plan and the 56 percent growth partial rate
started_at: 2026-11-23T05:34:00-08:00
finished_at: 2026-11-23T06:20:00-08:00
verified: every route copied from the operator record named in the CSV; none invented
grounded_in:
  - source: _records_/2026-11-22/coach/0501-conformance-report-2.md
  - source: _records_/2026-11-22/queue-planning/2700-routes.csv
---

# Route card and stop reasons, 2700

## Routes

The verified tap routes are in [2700-routes.csv](2700-routes.csv), one row per target with the operator record each came from: the fresh base frame, barracks, hospital, the four Drill Grounds, builders, labs, the Age of Oil tree, trade, the Backpack, alliance donations and hero detail. The safe empty-ground tap is (400,640). Follow a row exactly; if a route fails twice, stop with 'blocked by route'.

## Stop reasons, one phrase each

A unit that cannot do its step stops and writes one of: **blocked by capacity** (for example 'Drill Ground Full', with the building tag text); **blocked by the owner on another device** (a TIPS dialog); **blocked by cost** (the resource and the shortfall); **blocked by prerequisite** (the node or building and what is missing); **blocked by route**; **blocked by window**. It never improvises past a stop reason.

## Stats for idle-slot reads

Reads of building queues, research and troop training close with `--stat slots_idle=<N>`, the TOTAL open slots including the blocked ones, and, for the idle slots that stopped on a full Drill Ground, the subset `--stat slots_blocked_by_capacity=<N> --stat capacity_blocker="Drill Ground Full"`. The blocker text is at most 40 characters, and a count with no blocker named exempts nothing.
