---
title: Queue Planning Tag Text Rule And Four Grounds 2530 2026-11-23
created: 2026-11-23T02:58:00-08:00
modified: 2026-11-23T02:58:00-08:00
level: L0
version: 1.0.0
description: Planner pass after F1b - the four Drill Grounds in the builder units, the F1 row restored, the F1c unit retired for the operator's continuation, and the coach's tag-text rule written into every building-reading brief and the ledger
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0258-tag-text-and-grounds
trigger: coordinator F1b result, the F1c continuation, and the coach's tag-text rule
started_at: 2026-11-23T02:53:00-08:00
finished_at: 2026-11-23T02:58:00-08:00
verified: unit files read back; word counts under 450; ledger parsed; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/growth/1047-f1b-drill-ground.md
  - source: _records_/2026-11-22/coach/0255-tag-text-check.md
---

# Tag text rule and four grounds, 2530

## 1. F1b and F1c

F1b found four Drill Grounds, parade fields of red soldiers (Lv.26, Lv.28, Lv.30 and Lv.27) and a Tavern Lv.20, so the F1 panel read stands as the Lv.28 ground and the dispute mark is removed, with a note that F1b confirmed the tap identity. The F1c unit I staged before the coordinator's message is retired (expiry past), since the operator runs F1c as a continuation. The two builder units for 2026-11-24T09:20Z now list the four grounds with their coordinates and the pan, take the lowest first (Lv.26, 27, 28, 30), and wait for the F1c previews. The guide estimates imply about 262M coin for the Lv.26, Lv.27 and Lv.28 upgrades, which fits the 281M of read Coin Chests; Lv.30 at about 178.5M does not and waits.

## 2. Tag text

The coach's rule is in 21 units that read a building: the builder, collect and power units, the 13 fills, and the P1, B1, F2, C1, A1 and re-minted D1 reads. Each says to write the tag text (name and level above the building after the tap) beside every number from a building panel, add a tag_text column, and treat a number without it as [G]. The ledger has a `tag_text` column; 6 of its 33 rows carry one, and the rest are guide or hypothesis rows with no building read. The Hospital row records a conflict: operator read 2357 says Hospital Lv.25, the base map 1030 says Hospital Lv.20. The scout's sidecar schemas (`2345-snapshot-schemas.csv`) are not mine to edit: they need a tag_text column from the scout or the scribe.

## 3. Briefs

Adding the line pushed several units over 450 words; I shortened wording until the longest is 447, and the barracks paragraph in the power and collect units is now one shorter paragraph.
