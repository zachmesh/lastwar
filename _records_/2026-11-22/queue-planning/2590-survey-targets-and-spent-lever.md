---
title: Queue Planning Survey Targets And The Spent Drill Ground Lever 2590 2026-11-23
created: 2026-11-23T04:10:00-08:00
modified: 2026-11-23T04:10:00-08:00
level: L0
version: 1.0.0
description: Planner pass on the Researcher's provenance note - the survey branch of the idle lab unit now names the Development tail and the DRILL, GROUND, UNIT and CAPACITY tags, the Extra Barracks and Extra Drill Ground levers are closed in the ledger, and the provenance tags are refined
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0410-survey-targets
trigger: Researcher note drill-expansion-source and its two pointers
started_at: 2026-11-23T04:08:00-08:00
finished_at: 2026-11-23T04:10:00-08:00
verified: the repo searched for the Extra Drill Ground and 61M mentions; unit read back; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/research/drill-expansion-source.md
  - source: _records_/2026-11-22/research-queue/1144-queue-run.md
---

# Survey targets and the spent lever, 2590

## 1. Survey

The survey branch of `research-growth-convert-2026-11-23-002` now opens the Development tail first (Infirmary, Barracks and Focused Training IV, Efficient Healing, Survival Skills), then Units, Economy and Hero, and reads every tag containing DRILL, GROUND, UNIT or CAPACITY with effect, coin, iron, food, effective time and power gain. If none exists it says so, and the lever is ground levels only. It still acts only on a NODE line from the Strategist.

## 2. Spent lever

Four Drill Grounds exist (Lv.26, 27, 28 and 30, scout record 1047), so the Extra Drill Ground research, which the Researcher says the fourth ground needed, is spent; Extra Barracks reads MAX in the 1144 read. The ledger row for Extra Barracks and the capacity-table row are closed with those sources. My tables carry no row for Extra Drill Ground at 61M coin and 700 Valor, so the strike belongs to the Strategist's plan files.

## 3. Tags

The name Drill Ground Expansion is [S3] as a name (three guide pages: the Cpt Hedgehog Development calculator, the LootBar research guide, the Vault pre-season page), and [G] on this account for its effect, its levels (five or ten) and its cost. A node name does not give its effect: Barracks Expansion reads Number of Trainees and Infirmary Expansion reads Hospital Capacity. My earlier tag, "web calculators only", is replaced by this one.
