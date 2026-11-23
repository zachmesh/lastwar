---
title: Queue Planning The Serves Remap For The Coverage Alarm 2950 2026-11-23
created: 2026-11-23T09:05:00-08:00
modified: 2026-11-23T09:05:00-08:00
level: L0
version: 1.0.0
description: Planner pass answering Steer A's coverage alarm - which plan item each maintenance regular feeds, applied to the live units, the effect measured on the last six hours of executed units, and the trap that a snapshot text counts as ranked only until the forecast flip
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0905-serves-remap
trigger: Steer A message 16:54Z (strategy_conformance coverage 52 percent)
started_at: 2026-11-23T08:56:00-08:00
finished_at: 2026-11-23T09:05:00-08:00
verified: the coverage recomputed from the done folder (44 units in 6 h, 52 percent of units and 71 percent of unit-hours, matching the alarm); every proposed id checked against the forecast ledger; every inbox unit tested with the tool's forecast_class; validate exit 0
grounded_in:
  - source: _tools_/strategy-conformance/strategy_conformance.py (NON_RANKED is upkeep, snapshot, baseline)
  - source: _records_/2026-11-22/queue-planning/2940-regular-serves-map.csv
---

# The serves remap for the coverage alarm, 2950

## What the tool counts

A unit serves a ranked item when its `serves` is anything but exactly upkeep, snapshot or baseline. In the last six hours 44 units ran for 3.23 hours; 52 percent of the units and 71 percent of the hours counted as ranked, matching the alarm. Seven of the ranked ones were scout reads whose serves read 'snapshot (Story 868)', which is not an exact exempt word. At the forecast flip those become plain snapshot and stop counting, so a remap that left the scouts alone would read about 52 and 72 percent again.

## The map

[2940-regular-serves-map.csv](2940-regular-serves-map.csv): secrets and radar to PL-17 (the oil line), trucks to PL-18 (the materials engine), harvest to PL-16 (the iron and food line, alternative PL-14), donations to PL-04 (the research line, alternative PL-16), passes to PL-05 (the weekly cards are drone parts and components: the Strategist must confirm), research to PL-04, building-queues to PL-08, training to PL-09, and the midday scouts to PL-07 (a read serves the plan item it informs; a locate unit serves the item whose reads it anchors). Every id has a ledger row. Kept as upkeep, because I can show no lever: mail, help, gifts, train, duel-score, star-ceremony, arms-race, vip, daily-missions, treasures, survivors, events, ghost-ops and zero-sweep.

## Applied and measured

24 live units were remapped and every unit in the inbox passes the forecast check. With the full map in the roster default as well, the last six hours would read 75 percent of units and 90 percent of unit-hours. The remaining upkeep is 0.34 hours of 3.23, led by mail (three units, 0.14 hours). The roster default is `_tools_/regulars.json`, which I do not edit: the toolsmith changes it from the map, and until then units minted by `plan` and `sync` come back as upkeep and must be remapped. The Strategist confirms each id. A unit serving nothing is a signal to drop it or lower its frequency: the candidates are the 0.34 hours above.
