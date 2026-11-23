---
title: Queue Planning F1b Drill Ground Re-read And Attribution 2520 2026-11-23
created: 2026-11-23T02:43:00-08:00
modified: 2026-11-23T02:43:00-08:00
level: L0
version: 1.0.0
description: Planner pass after the base map - the F1b Drill Ground re-read staged, the builder conversion units rewritten to name the grounds by the base map, barracks coordinates added, and the F1 panel's attribution flagged as disputed with the numeric evidence
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0243-f1b-and-attribution
trigger: coordinator instruction after the operator's base map 1030
started_at: 2026-11-23T02:38:00-08:00
finished_at: 2026-11-23T02:43:00-08:00
verified: the F1 panel figures compared with the guide table rows for Drill Ground and Farmland; unit files read back; word counts under 450; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/growth/1030-base-map.md
  - source: _records_/2026-11-22/perception-scout/0035-queue-run.md
  - source: _records_/2026-11-22/queue-planning/2400-building-guide-rows.csv
---

# F1b and the Drill Ground attribution, 2520

## 1. Staged

`scout-midday-growth-snapshot-2026-11-23-024`, priority 1, read-only, 10 minutes, window 10:41Z to 11:30Z, `serves: baseline Drill Ground`. For each of the two Drill Grounds (Lv.30 orange about (740,880), Lv.27 purple crystal about (855,790), both past the right edge, one pan): read the tag, Building Details (Level, Unit Count, officer slots), then the Upgrade preview (coin, iron, time, Unit Count change, prerequisite). Never Upgrade, Finish Now, Speed Up or Obtain. The hazard is written in: close menus with an empty-ground tap, never the WORLD button with a menu open low.

## 2. The attribution

The base map says there is no Drill Ground Lv.28, and that the Lv.28 near (260,545) is the Farmland. But the F1 panel (Lv.28 to 29, power 165,800 to 196,200, original time 39d 01:53, coin 119.0M and iron 144.5M, which are 0.85 of 140M and 170M) matches the guide's Drill Ground Lv.28 to 29 row exactly (+30,400, 39.1 days, 140M, 170M) and not the Farmland's (+14,900, 9.8 days, 28M). So either a Lv.28 ground exists and a base-map tag was misread, or the F1 tap reached a third ground. F1b settles it, and the brief asks it to report any ground reading Lv.28. Until then the F1 row in the ledger and both tables is marked disputed, and my note 2455 calling it measured on a Drill Ground is superseded by this one.

## 3. Units changed

The two builder conversion units (2026-11-24, 400 and 417 words) name the grounds by the base map, drop the unattributed numbers and 49-chest count, and plan from the F1b preview; the lowest level goes first. The collect unit and the two power units carry the barracks coordinates: Lv.27 (462,585), Lv.30 (530,637), Lv.24 (628,562), Lv.20 (668,535). Guide estimates for the grounds the base map names: Lv.27 to 28 about 83.3M coin and 14.2 days (2.40 slots per million coin), Lv.30 to 31 about 178.5M and 26.3 days (1.12), both to be replaced by the F1b numbers.
