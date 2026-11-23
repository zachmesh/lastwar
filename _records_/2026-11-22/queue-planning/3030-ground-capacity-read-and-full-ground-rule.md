---
title: Queue Planning The Drill Ground Capacity Read And The Full Ground Rule 3030 2026-11-23
created: 2026-11-23T12:15:00-08:00
modified: 2026-11-23T12:15:00-08:00
level: L0
version: 1.0.0
description: Planner pass after a finished troop batch could not be collected while the Drill Ground was full - a read-only capacity unit staged before the builder pick, the capacity line added to the ground units, and the no retry rule in the fills and the training unit
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-1215-ground-capacity
trigger: coordinator message 20:05Z, operator record 1958
started_at: 2026-11-23T12:05:00-08:00
finished_at: 2026-11-23T12:15:00-08:00
verified: the sheet 2540 and the record 2455 read for the measured Unit Count lines; word counts under 450; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/troop-training/1958-queue-run.md (as relayed by the coordinator)
  - source: _records_/2026-11-22/queue-planning/2540-drill-ground-sheet.md and 2455-drill-ground-f1-values.md
---

# The Drill Ground capacity read and the full ground rule, 3030

## What is staged

`building-queues-ground-capacity-read-2026-11-23-001` (priority 1, 20:15Z to 22:15Z, serves PL-08, read only, up to two runs): for each of the four grounds, Lv.26 first, then 28, 30 and 27, it writes the tag text, the Details troop capacity figure and any unit count line, and the Upgrade preview's troop capacity line (current and next, the increase, the power change, the cost and the effective time), with the Details and preview figures written exactly because they disagreed before. It is done when Lv.26 and one more ground are read. It presses nothing that upgrades, trains, collects or speeds up. It exists so that the Strategist has the slots gained per level before the pick at 22:30Z; the starts at 23:21Z come too late for that.

## What is already measured

The previews of 2026-11-23 carry a Unit Count line of +7,200 to +7,400 at Lv.26 to 27, +7,400 to +7,600 at Lv.27 to 28 and +7,600 to +7,800 at Lv.28 to 29: +200 a level, [M] as a preview line. What is not established is whether a ground's +200 joins one shared pool or belongs to that ground alone, which is the Strategist's second question; the read above answers it from the Details figures of all four grounds.

## Changed in the live units

The ground units `building-queues-growth-convert-2026-11-24-001` and `-002` read the troop capacity line (current and next) and the Details figure before each Upgrade. The five fills and the 22:03Z training unit say that a finished batch is never retried while the Drill Ground is Full (toast 'Drill Ground Full: Unable to add more units', measured 19:59:22Z), that such a slot is blocked by capacity and not idle, and that the stats are `slots_blocked_by_capacity=1` with capacity_blocker 'Drill Ground Full'. The speed-up unit `-003` already names the three Drill Ground upgrades and not the Oil Well.

## Not staged

No collect unit for the Lv.30 batch ending 2026-11-24T11:18Z: it would be refused the same way, and the Coach's rule is to stage a unit after its precondition event. That event is a completed ground level, whose time is known only after the starts and the speed-ups; I stage the collect unit then, with a plan item that has a ledger row.
