---
title: Growth snapshot protocol living rules
created: 2026-11-23T10:58:57Z
modified: 2026-11-23T10:58:57Z
version: 0.1.0
description: The rules added to the growth snapshot protocol after it was recorded, starting with the tag text of every building read
---

# Growth snapshot protocol living rules

The snapshot protocol of 2026-11-22 (routes, fields, stop rules R1 to R7) is the record `_records_/2026-11-22/perception-scout/2345-snapshot-protocol.md`. A record is never edited, so the rules added after it live here. Back to the [rule digest](rule-digest.md).

## T1 Tag text with every building read

Every read of a building records the tag text it was read from, the name and level shown above the building after the tap, next to every number taken from its panel. A number with no tag text is [G], a guess to test (the strategy's evidence tags, `_knowledge_/growth-plan/strategy-source.md`).

Status tested, 2026-11-23. The coach proposed it and the coordinator accepted it on Steer A's proposal.

## Why: two tap-identity errors in one day

- The upper-right tent was read as Barracks Lv.20 by one run and as Hospital Lv.20 by the next, and the difference was left unresolved (`_records_/2026-11-22/perception-scout/0022-queue-run.md`).
- The base map showed two Drill Grounds and no Lv.28; the F1b re-read found four parade fields, a Lv.28 ground among them, and a Tavern inside the compound (`_records_/2026-11-22/growth/1047-f1b-drill-ground.md`).

## Check and carriers

The coach counts it as check (g) in each conformance report: the share of building-read rows that carry their tag text. Baseline 26 of 67 rows, 39 percent, over 12 growth CSVs; six files carry none: the inventory, the stocks, two stores reads, the drone wall and the decoration read (`_records_/2026-11-22/coach/0255-tag-text-check.md`).

The planner writes the rule into the unit briefs for every building read and the operator records the tag text in each row. The rule is in the digests of perception-scout, building-queues, troop-training, upgrade-builders-hut-to, resource-collection and decoration-gallery-overview-ur.
