---
title: Strategy 1 - where we are
created: 2026-11-23T08:19:08Z
modified: 2026-11-23T08:23:27Z
level: L1
version: 0.1.0
description: The measured power split, the troops waiting in the hospital and the coin behaviour of the account
status: unverified
grounded_in:
  - source: Steer A growth strategy v2.0 (2026-11-23 09:40Z), snapshot sha256 2137b1c5a923, copied verbatim from source lines 3 to 5
  - source: coordinator order of 2026-11-23 (v2.0 supersedes v1.1 to v1.5) and decision record _records_/2026-11-22/team-operations/2401-growth-strategy-decision.md
---
# Strategy 1 - where we are

1. WHERE WE ARE (all [M] unless tagged)

 Total Power 150.2M = Hero 44.1% (66.24M), Troops 42.3% (63.51M), Buildings 6.5%, Drone 3.9%, Tech 3.2%. HQ 30: hero level cap 150, reached [S3]. Troops are nearly all T10 (1,609 average of 1,647 per troop [D]). Research gives about +15K a level. HQ 31 and the Age of Oil path cost about 2.3B coin: not a lever [S1]. Coin income is 16M to 26M a day, spent by the owner by hand in bursts of about 100M and 118M [M]. Food 732M and iron 1.1G are in surplus; diamonds are never spent.

 THE HIDDEN FACT: 5,306 troops are healed and waiting in the hospital, NOT in Total Power: 5,306 x 1,647 = 8.74M, 5.8% of power. "Collect" is blocked by "Drill Ground Full" (39,460 of 39,460) [M]. The 2026-11-09 fall of 1,506 T10 (2,480,382) was the same mechanism, reversed by the collections of 11-10 [M, cause unverified]. Wounded troops count zero until collected; with the Drill Ground full they cannot come back.

## Sources

- Power split: `_records_/2026-11-22/growth/2344-power-breakdown.csv`. Healed troops, Collect blocked, Total Power unchanged at 150,211,809: `_records_/2026-11-22/growth/2357-troop-read.md` and [train](train.md). The 2026-11-09 fall of 2,480,382, 1,506 T10 units (654 + 407 + 445 units x 1,647), reversed by recorded collections on 2026-11-10: `_records_/2026-11-22/coach/2358-fall-analysis.md` [M, cause unverified]. Coin: [coin-history.csv](coin-history.csv).

## Errata

The original text above stays (C2); the newer record governs.

- "(39,460 of 39,460)": read on a Drill Ground Lv.30 panel on 2026-10-31 07:04 (`_records_/2026-10-31/troop-training/0704-queue-run.md`) and not re-read; the 2026-11-23 Building Details read a Drill Ground Lv.28 with Unit Count +9211 (`_records_/2026-11-22/growth/2344-fill-run.md`), possibly another building; step P1 reads how many exist.
- "Troops are nearly all T10": the Train panel on 2026-11-23 lists Lv.7 1,116, Lv.8 2,141, Lv.9 1,878 and Lv.10 35.1K, Lv.6 cut off (`_records_/2026-11-22/growth/2357-troop-read.md`), about 87 percent T10 by count over those four tiers; the 1,609 average [D] depends on the unread tier mix.
- "Food 732M and iron 1.1G": the HUD read of 2026-11-23 07:48Z is food 638.0M and iron 1.0G (`_records_/2026-11-22/growth/2344-fill-run.md`), still above the floors.

## Changelog

- 0.1.0, 2026-11-23 - Landed from strategy v2.0, replacing the v1.5 pages.
