---
title: Queue Planning Units With No Brief And The Spaced Plunder Scans 2770 2026-11-23
created: 2026-11-23T06:46:00-08:00
modified: 2026-11-23T06:46:00-08:00
level: L0
version: 1.0.0
description: Planner pass for the respawned operator - what the passes unit is, a definition block added to every minted unit that had no brief, a map of each regular to its activity folder, and nine one-scan plunder units spaced 20 minutes apart
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0646-no-brief-and-scans
trigger: coordinator message 14:37Z after the operator respawn
started_at: 2026-11-23T06:38:00-08:00
finished_at: 2026-11-23T06:46:00-08:00
verified: the roster checked against _activities_ for all 25 regulars; the inbox searched for units without a Brief section before and after; word counts under 450; validate exit 0
grounded_in:
  - source: _tools_/regulars.json and _activities_/shop-claims/rule-digest.md
  - source: _records_/2026-11-22/truck-plunder/1405-queue-run.md
---

# Units with no brief and the spaced plunder scans, 2770

## 1. What passes is

`passes` is the roster regular for the shop's weekly and monthly pickups and Free Supply, and its activity is `shop-claims`, defined in `_activities_/shop-claims/` (digest and index), not in a folder named passes. All 25 roster regulars have an activity folder and a rule digest; the confusion is that the regular id often differs from the folder: mail runs mail-rewards, secrets runs secret-missions, trucks runs truck-plunder, harvest runs resource-collection, and so on. The map is [2760-regular-to-activity-map.csv](2760-regular-to-activity-map.csv). No roster entry needs retiring.

## 2. The fix

Thirty-one inbox units, minted by `plan` or `sync`, carried only the default sentence. Each now has a definition block: the regular, its roster line, its activity folder with the digest to read first, the map, the card, and a rule to stop with 'blocked by prerequisite' rather than improvise. The passes units carry the shop-claims rules (free items only, no price button, Renew, Extension or Take All, read each button after a tap, the check-in Go not tapped, no Season hunt). Mail and zero-sweep have a line too. The cause is in the tool: a minted unit gets no definition pointer, so the toolsmith should have `_produce_for_window` write one from the roster; that is outside my scope.

## 3. Plunder scans

The session of 14:05Z made one fight (a UR truck, guard 21.0M against Squad 1 at 25.61M, no troops wounded, 0.61M coin, 0.95M iron and food, UR shards x9) and found no second target in four scans: the list reshuffles on every entry and the session cost 1.11 USD over seven runs. `trucks-plunder-scan-2026-11-23-001` to `-009` each look once, 20 minutes apart from 15:00Z to 17:40Z (windows 30 minutes long), read the Plunder Count first, take only a target by the standing rule, apply the casualty guard before any fight (the Hospital figures sit behind the orange middle button of its tag), and fight at most once. The session unit `-002` opens at 18:00Z.
