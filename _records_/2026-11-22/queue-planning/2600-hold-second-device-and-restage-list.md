---
title: Queue Planning Hold For A Second Device And The Restage List 2600 2026-11-23
created: 2026-11-23T04:18:00-08:00
modified: 2026-11-23T04:18:00-08:00
level: L0
version: 1.0.0
description: Planner note during the coordinator's hold for a second logged-in device - no unit is changed, the units that will expire unrun are listed for restaging, and the coin plan is re-checked against the lower coin baseline
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0418-hold-restage-list
trigger: coordinator message, hold for a second device logged in since about 12:11Z
started_at: 2026-11-23T04:16:00-08:00
finished_at: 2026-11-23T04:18:00-08:00
verified: unit file modification times read; the pool read for windows closing before 13:20Z; coin arithmetic recomputed
grounded_in:
  - source: _tools_/queue.py pick_key and unit frontmatter
  - source: coordinator message 12:15Z (coin 9.8M at 12:12:50Z, 14.4M at 12:01Z)
---

# Hold and restage list, 2600

## 1. Hold

The coordinator stood the operator down at about 12:15Z because a second device is logged in (TIPS dialog since about 12:11Z). I change no unit, window or expiry for 30 minutes. My last unit-file edits were at 12:15:09Z (the 2026-11-26 lab completion unit), 12:15:22Z (the lab backup unit) and 12:15:33Z (builder unit 002), before the hold reached me.

## 2. Units that close during the hold

If the operator stays stood down they expire unrun: `fill-burst-2026-11-23-003` (12:20Z), `fill-burst-2026-11-23-004` (12:35Z), `research-growth-convert-2026-11-23-002` (12:48Z), the A1 snapshot `scout-midday-growth-snapshot-2026-11-23-017` (12:50Z) and the 4-hour Secrets claim `secrets-2026-11-23-0944` (13:20Z; the claim is the top priority and tasks left unclaimed can be plundered). To restage on the coordinator's word: the Secrets claim first, then the lab fill (the Strategist's pick waits and a lab slot may now hold the owner's research), then A1 if still wanted. The fills are optional reads.

## 3. Coin baseline

Coin read 9.8M at 12:12:50Z, down from 14.4M at 12:01Z, not by our units. Every coin figure of mine that starts from 14.4M or 9.6M needs re-baselining at the next read. Tomorrow's plan reads coin live, but the margin is thin: from 9.8M the path is 9.8M, +143.75M, -142.8M, +119.0M, -119.0M, ending at 10.75M, 0.75M above the 10M floor. A further fall before 09:20Z would put the third step below the floor, so the units must read coin first and say so.
