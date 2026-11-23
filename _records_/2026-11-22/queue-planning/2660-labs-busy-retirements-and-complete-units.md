---
title: Queue Planning Labs Busy Retirements And The Two Complete Units 2660 2026-11-23
created: 2026-11-23T05:04:00-08:00
modified: 2026-11-23T05:04:00-08:00
level: L0
version: 1.0.0
description: Planner pass after both labs were found busy with Age of Oil nodes started on the other device - the moot units retired, the oil and survey units adapted, and two Complete units staged for 2026-11-24 with the next Base Expansion nodes
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0504-labs-busy
trigger: coordinator message 13:01Z with the 1257 survey record
started_at: 2026-11-23T04:57:00-08:00
finished_at: 2026-11-23T05:04:00-08:00
verified: unit states read before each edit; word counts under 450; pool simulated before the retirements; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/research-queue/1257-age-of-oil-survey.md (as relayed by the coordinator)
  - source: coordinator message 13:01Z, schedule-22e92ed7 and schedule-de14b612
---

# Labs busy, retirements and the two Complete units, 2660

## 1. Retired

Both labs are busy with Age of Oil path nodes started on the other device: slot 1 Food Output V to about 2026-11-24T17:29:58Z, slot 2 Coin Output V to about 14:59:10Z; Defense Training VIII is no longer queued. Retired by setting the expiry past: `research-food-output-v-start-2026-11-23-001` and its fallback `-002` (which I had staged minutes earlier), `research-growth-convert-2026-11-23-002`, and `research-complete-2026-11-26-001` (the Defense Training completion). The 14:03Z Special Forces idea is moot.

## 2. Adapted and kept

`research-age-of-oil-survey-2026-11-23-001` was claimed before the first edit and is blocked: with both labs busy the flask opens only the Research Queue list. The follow-up `-002` now reads the two queue rows by tag text (level, Time Left to the second, UTC time) and the oil counter first, and the Coin Output V panel only if a panel opens. The oil units, the HQ 31 reads and the Drill Ground units stand; the Tech Center and centers read the operator now runs overlaps my HQ 31 buildings read `scout-midday-growth-snapshot-2026-11-23-033`, which I retire when that record lands.

## 3. The Complete units

`research-complete-2026-11-24-001` (14:59:30Z to 16:30Z): Complete Coin Output V in lab 2 at about 14:59:10Z, then Research Enhancement V. `research-complete-2026-11-24-002` (17:30:10Z to 19:00Z): Complete Food Output V in lab 1 at about 17:29:58Z, then Iron Output V. Each reads both labs first, reads Total Power before and after, checks the prerequisite and the oil, converts only the coin it lacks by the formula (stop above 40 UR chests, tile name confirmed against the 5,000 Diamonds tile), starts the node once, and applies OD-19 speed-ups (tech items first, up to 30 percent of the general stock a week, 100,000 general minutes kept until M is read, never Finish Now, stop on an oil-bound level). They pair with the coordinator's triggers at 14:59:40Z and 17:30:30Z. Nothing past these two nodes is staged; Oil Output I level 1 waits for the three Output V nodes and 60K oil.
