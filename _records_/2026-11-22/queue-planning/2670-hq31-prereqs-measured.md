---
title: Queue Planning HQ 31 Prerequisites Measured And The Reads Retired 2670 2026-11-23
created: 2026-11-23T05:11:00-08:00
modified: 2026-11-23T05:11:00-08:00
level: L0
version: 1.0.0
description: Planner pass after the HQ 31 prerequisite read - all five building gates are met and only the Base Expansion research is unmet, so the two HQ 31 read units are retired, builder B2 is dropped, and the tomorrow builder units wait for the Strategist's pick
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0511-hq31-measured
trigger: coordinator message 13:13Z with the HQ 31 prerequisite read
started_at: 2026-11-23T05:09:00-08:00
finished_at: 2026-11-23T05:11:00-08:00
verified: the unit states read before the edit; validate exit 0
grounded_in:
  - source: operator runs 20261123T130521Z-e29a2e and -7636b4 as relayed by the coordinator, record 1308-hq31-prereq-read
---

# HQ 31 prerequisites measured, 2670

## 1. Retired

`scout-midday-growth-snapshot-2026-11-23-033` (the HQ 31 prerequisite buildings read) and `-032` (the HQ 31 preview and prerequisite lines) were unclaimed; both have their expiry set past. The operator's measured read replaces them: tag 'Headquarters Lv.30', preview 'Lv.30 to 31', nothing pressed.

## 2. What the read changes for the queue

All three building gates (any Tech Center at Lv.30, the Barracks at Lv.30, any Tank, Missile Vehicle or Aircraft Center at Lv.30) show green checks, so builder B2, the HQ 31 prerequisite buildings, is empty and dropped. The only unmet row is the research node Lv.1 Base Expansion. The unmet resource rows are oil 647,039 of 1.2M, food 653.9M of 1.3G, coin 55,963 of 433.5M and iron 1.0G of 1.3G; the HQ 31 upgrade is 111d 18:21:40 original and 52d 14:17:16 effective, so its speed-ups would come from the construction stock and it is the last builder job after Base Expansion.

## 3. Still open

Tomorrow's builders at 2026-11-24T09:20Z are B1 the Oil Well Lv.1 to Lv.30 and three slots for the Strategist's pick between the Drill Ground ladder (Lv.26 to 27 for 59.5M coin, Lv.27 to 28 for 83.3M, Lv.28 to 29 for 119.0M) and the Builders Hut, due by 08:00Z. The three builder units staged for 2026-11-24 still describe the Drill Ground plan, so they are rewritten once that one-line decision file exists, keeping the coin formulas and dropping the fixed 59-chest reserve; the Oil Well read and the first collection are in `harvest-oil-well-2026-11-23-001`.
