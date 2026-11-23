---
title: Growth charter evidence
created: 2026-11-23T08:05:06Z
modified: 2026-11-23T08:23:27Z
level: L1
version: 0.2.0
description: What the measured numbers say and why troop training stalled, copied from the charter draft with its erratum and corrections
status: unverified
grounded_in:
  - source: coordinator charter draft v0.4.0 _records_/2026-11-22/team-operations/2340-growth-charter-draft.md
  - source: records _records_/2026-11-22/growth/2344-fill-run.md, _records_/2026-11-22/growth/2357-troop-read.md and _records_/2026-11-22/coach/2358-fall-analysis.md
---
# Growth charter evidence

Verbatim from the coordinator's draft v0.4.0, with its own erratum.

## What the numbers say

Total Power rose 13,466 a day over 29 days (+0.26 percent). A Builders Hut upgrade gives 2,400 power per builder-day (four builders about 9,600 a day). 200M in 90 days needs 554,665 a day (41x). **Troops are the measured lever:** a 666-troop T8 batch gave +707,958 power (1,063 each) for 2.9M food and 2.9M iron in 1 day 4 hours, about 600,000 power per barracks-day, 250x a builder-day. A Lv.30 barracks trains T10: 793 per batch at +1,647 each for 5.5M food and 5.5M iron (+1,306,071, record 2026-10-31 0304); a Lv.24 one only T8.

## Why troops stalled: capacity, not resources

Training is blocked since 2026-10-31 by the toast "Drill Ground Full" (82 troop-training articles; 39,460 of 39,460); the building was "unlocated" in 8 articles; the promote arrow "did nothing" once. At 5.5M per T10 batch, stock pays for about 100 batches above the floors.

## Erratum 2026-11-23 08:05Z (measurement)

The figure 2,486,382 is **derived**, not a recorded measurement: my subtraction of two recorded readings, 149,217,331 (2026-11-09 07:45, many records) and 146,730,949 (2026-11-09 17:53, radar record 1754). The 11-10 building-queues record (`run-20261110-0112-p1`) documents "a fall of about 2.47M", flagged with no cause, three consecutive reads at the lower level. The issue 482 step is 641,100 (2026-11-08, a disconnect and relaunch). Cause **unverified**; an uncollected-troop-batch artifact is plausible and untested. Treat the 29-day change as uncertain by a few million; the fixed-state read (collect every finished batch first, then read) is mandatory.

## Errata

The original text above stays (C2); the newer record governs.

- "capacity, not resources" and the 2,486,382 erratum: the coach finds 146,730,949 a digit artifact (7 records read 146,736,949); the confirmed drop is 2,480,382, exactly 1,506 T10 units, reversed by recorded collections on 2026-11-10 (`_records_/2026-11-22/coach/2358-fall-analysis.md`). Strategy v2.0 adds 5,306 healed troops, 8.74M [D] ([where we are](strategy-where-we-are.md)).
- "39,460 of 39,460 at last read" and "unlocated in 8 articles": a Drill Ground Lv.30 panel was read on 2026-10-31 07:04 (`_records_/2026-10-31/troop-training/0704-queue-run.md`), not re-read, and a Lv.28 on 2026-11-23; the toast did not reproduce in two units on 2026-11-22 (`_activities_/troop-training/changelog-section-p1.md`) and reproduced on 2026-11-23 (`_records_/2026-11-22/growth/2344-fill-run.md`, `_records_/2026-11-22/growth/2357-troop-read.md`).

## Changelog

- 0.2.0, 2026-11-23 - Draft erratum added; Errata corrected (39,460 was read on 2026-10-31) for the coach analysis and v2.0.
