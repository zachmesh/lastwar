---
title: Queue Planning Restage After The Hold And The Coin Formula 2610 2026-11-23
created: 2026-11-23T04:22:00-08:00
modified: 2026-11-23T04:22:00-08:00
level: L0
version: 1.0.0
description: Planner restage on the coordinator's word after the second-device hold - the lab fill re-timed behind the Secrets claim with both lab slots read first, A1 retired, the optional fills left to expire, and a coin formula replacing fixed chest counts in the builder and lab units
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0422-restage-and-formula
trigger: coordinator GO on the restage after the hold
started_at: 2026-11-23T04:16:00-08:00
finished_at: 2026-11-23T04:22:00-08:00
verified: formula results recomputed for three coin levels; unit files read back; word counts under 450 except the lab unit noted below; validate exit 0
grounded_in:
  - source: coordinator message 12:15Z with the coin formula
  - source: _records_/2026-11-22/growth/1115-rc1-chest-limits.md
---

# Restage after the hold and the coin formula, 2610

## 1. Restage

The lab fill `research-growth-convert-2026-11-23-002` now has window 12:55Z to 13:35Z, after the Secrets claim, which keeps 12:50Z to 13:20Z and ranks first by expiry. Its NODE line stays Special Forces, best power per effective day by preview, with the new first step: read both lab slots first, and if slot 2 is busy (the owner's research or a Special Forces node already running) start nothing and finish the survey read-only. A1 (`scout-midday-growth-snapshot-2026-11-23-017`) is retired unless the Strategist asks for it. The two optional fills (burst 003 and 004) expire on their own.

## 2. Formula

Units read coin first. Builder unit 001: N = ceil((142.8M + 10M - coin now) / 2.4364M) UR chests, which gives 59 from 9.8M, 58 from 12M and 63 from 0.2M; the Total line is checked against the need before Use; stop if N exceeds 87. Builder unit 002: M = ceil((119.0M + 10M - coin now) / 6,000) plain chests, where coin now is the coin after the first two starts (about 19,709 from 10.75M); 6K times the number field is checked before Use; stop if M exceeds 20,862. Lab unit: N = ceil((node coin + 10M - coin now) / 2.4364M), 9 from 9.8M for a 20.1M node, stopping above 28 so the 59 UR kept for tomorrow stay. The 10M floor holds in every case, and tomorrow's path from 9.8M ends at 10.75M.

## 3. Note

Word counts after this edit: lab unit 438, builder units 437 and 441; the longest staged brief is 446. The sheet 2540 funding plan gave fixed counts (59 UR chests, 19,834 plain chests); it now says they are planning figures and the formula governs.
