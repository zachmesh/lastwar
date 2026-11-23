---
title: Queue Planning The Builder Start Gap And The Pre-Conversion Unit 3040 2026-11-23
created: 2026-11-23T12:50:00-08:00
modified: 2026-11-23T12:50:00-08:00
level: L0
version: 1.0.0
description: Planner pass for Steer A's rule that the operator is idle from 23:10Z so the 300 second counter has run out at 23:20:12Z - one pre-conversion unit that ends by 23:09Z, the builder units claimable at 23:20:15Z, the units that fall in the gap moved, and a simulation of the pool under the slower throughput
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-1250-builder-gap
trigger: coordinator message 20:26Z (Steer A's rule)
started_at: 2026-11-23T12:27:00-08:00
finished_at: 2026-11-23T12:50:00-08:00
verified: the inbox searched for units opening, closing or ranking inside 23:09Z to 23:21Z; the pool simulated with the tool's own pick_key at 5.5 and 3.8 units an hour; word counts under 450; validate exit 0
grounded_in:
  - source: coordinator message 20:26Z
  - source: _tools_/queue.py pick_key and _actionable
---

# The builder start gap and the pre-conversion unit, 3040

## Staged

`building-queues-growth-preconvert-2026-11-23-001` (priority 1, est 15, serves PL-14) opens at 22:40Z, can be claimed until 22:55Z and ends by 23:09Z: it converts the UR Coin Chests (N from the live coin) and then the plain Resource Chests to the coin total T, default 271.8M for the three Drill Ground starts (59.5M, 83.3M, 119.0M, plus the 10M floor). It starts nothing and completes nothing. T is edited here when the Strategist's pick lands, and the coordinator does not dispatch before that. The tool caps a unit at 15 minutes, so a first split into two units was rejected for a better reason: two units back to back need the 300 second idle wait between them and the second would have expired unclaimed. The builder units `building-queues-oil-well-2026-11-24-001` and the ground units `-001` and `-002` open at 23:20:15Z so they are claimable at the 23:20:20Z dispatch; the conversion text left the ground units, which only check coin and stop on a shortfall.

## The gap

Moved: `scout-midday-2026-11-23-0612` (window 22:55Z to 23:35Z, which would have been the first pick at 23:20:20Z because its expiry is earlier than the Oil Well unit's) to 00:30Z to 01:30Z, and the five fills (fill 001 had 23:10Z to 23:21Z) to 00:25Z to 01:40Z, after the builder units. The 22:30Z and 22:57Z groups have windows of four hours, so they are claimable throughout: the pool cannot keep the operator out of 23:10Z to 23:20Z, and the coordinator's dispatch has to.

## Simulated

With the tool's own ranking from 20:31Z to 23:09Z, no unit expires unrun at either 5.5 or 3.8 units an hour (13 and 10 units run); the pre-conversion unit is picked at 22:47Z and 22:53Z, so at the slow rate the margin to the 22:55Z claim deadline is two minutes and the 23:09Z end is tight: dispatch it by name at 22:40Z. At 23:20:20Z the first picks are the Oil Well unit, then the two ground units.

## Open

If the operator's own last click resets the idle counter, each separate run waits 300 seconds: the four builders are then started at about 23:20:30Z, 23:36Z and 23:52Z, not together. That makes the order of the starts matter; whether the Drill Ground Lv.26 should go first is decided with the Strategist's pick.
