---
title: Queue Planning The Oil Well Chain Staged 2910 2026-11-23
created: 2026-11-23T08:20:00-08:00
modified: 2026-11-23T08:20:00-08:00
level: L0
version: 1.0.0
description: Planner pass after the Oil Well was found at level 20 - ten chain units staged for builder B1 from 2026-11-24T09:21Z, the locate unit retired, the fourth builder line of the ground units corrected, and the points that need the Strategist
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0820-oil-well-chain
trigger: coordinator message 16:00Z
started_at: 2026-11-23T07:58:00-08:00
finished_at: 2026-11-23T08:20:00-08:00
verified: the release command's usage read; the inbox searched; word counts under 450; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/queue-planning/2900-oil-well-chain.md
  - source: _records_/2026-11-22/resource-collection/1553-oil-well-found.md (as relayed)
---

# The Oil Well chain staged, 2910

## Staged

`building-queues-oil-well-2026-11-24-001` to `-010` serve PL-17, one per level from Lv.20 to 21 up to Lv.29 to 30. The first (415 words) opens at 09:21:00Z and expires 09:45Z, so it ranks ahead of the ground units; it completes the four finished Training Base entries (skipped if unit 001 of the grounds already did), then starts the well on the first idle builder: iron 8.5M only, no coin, food or oil. The next nine open at the earliest possible finish of the level before (each level takes at least 9 h 20 min 18 s, the first level's effective time; later ones longer) and run 40 hours, because the coordinator dispatches them by name at the real finish. A unit claimed before its upgrade is finished releases itself unrun (`queue.py release --unit`) and writes the time left, so it is not consumed. The sheet [2900](2900-oil-well-chain.md) holds the facts, the route, the procedure and the earliest schedule.

## Corrected and retired

`scout-midday-oil-well-locate-2026-11-24-001` is closed as moot. Ground unit `-002` no longer says the Hut is the fourth builder: the well takes one, so three builders are free for the grounds.

## For the Strategist and the coordinator

One building is upgraded by one builder at a time, so 'all spare builders on the Oil Well' cannot hold: B2 to B4 need other buildings, and the B2 to B4 pick (due 08:00Z) still decides them. The earliest finish of Lv.24 to 25 is 11-26 08:02Z, inside the daily quiet window, so that Complete and the next start move to the nearest edge or take a one-line exception. The chain spends about 100M iron while HQ 31 needs 1.3G iron against 1.0G held and Base Expansion 616M more: an iron budget question.
