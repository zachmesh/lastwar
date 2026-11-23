---
title: Train
created: 2026-11-23T08:05:06Z
modified: 2026-11-23T09:08:31Z
level: L1
version: 0.3.0
description: The measured troop facts, the hospital backlog and the Drill Ground capacity wall, and the reads still owed
status: unverified
grounded_in:
  - source: records _records_/2026-11-22/growth/2357-troop-read.md, _records_/2026-11-22/coach/2358-fall-analysis.md, _records_/2026-10-31/troop-training/0304-queue-run.md, _records_/2026-10-31/troop-training/0704-queue-run.md and _records_/2026-11-10/troop-training/1229-queue-run.md
  - source: _records_/2026-11-22/growth/2344-fill-run.md
  - source: articles _activities_/troop-training/cadence-section.md and _activities_/troop-training/changelog-section-p1.md
---
# Train

Troops count only when collected, so the Drill Ground capacity decides how much troop power the account can bank ([the one idea](strategy-one-idea.md)). Every number names its record.

## Measured facts

- Hospital Lv.25 shows "Completed 5306" with a Collect button; one tap gave the toast "Drill Ground Full: Unable to add 5306 units." and Total Power stayed 150,211,809 (`_records_/2026-11-22/growth/2357-troop-read.md`) [M]. 5,306 x 1,647 = 8,738,982, 5.8 percent of Total Power [D], at the T10 power per troop; their tier is unread. Severely wounded 364 of 7,999.
- The 2026-11-09 fall of 2,480,382 is exactly 1,506 T10 units, reversed by recorded collections on 2026-11-10 (+2,467,024 across five events); cause unverified (`_records_/2026-11-22/coach/2358-fall-analysis.md`).
- Batch gains per tier and the barracks state of 2026-11-23: [train batch facts](train-batch-facts.md).

## The capacity wall

- The toast appeared from 2026-10-31; it did not reproduce in two units on 2026-11-22 (`_activities_/troop-training/changelog-section-p1.md`) and reproduced on 2026-11-23 (`_records_/2026-11-22/growth/2344-fill-run.md`, `_records_/2026-11-22/growth/2357-troop-read.md`).
- A Drill Ground Lv.30 panel read Unit Count 39460/39460, In Base Lv.7 701, Lv.8 1,332, Lv.10 37.4K, no units outside, on 2026-10-31 07:04 (`_records_/2026-10-31/troop-training/0704-queue-run.md`); a Drill Ground Lv.28 read Unit Count +9211 on 2026-11-23 (`_records_/2026-11-22/growth/2344-fill-run.md`). How many exist is unread.
- Whether promotion works with a full Drill Ground is unsettled: a busy barracks shows no Promote and an idle one raises the toast (`_records_/2026-11-22/growth/2357-troop-read.md`).

## Reads owed

The reads that strategy steps P1 to P3 still owe are on [train reads owed](train-reads-owed.md).

## Changelog

- 0.2.0, 2026-11-23 - Hospital backlog and the 2,480,382 fall added with sources; the capacity wall corrected (the 39,460 figure was read on 2026-10-31); links to the v2.0 pages.
- 0.3.0, 2026-11-23 - The reads-owed section and two batch bullets moved verbatim to train-reads-owed.md and train-batch-facts.md (page budget 300 words).
