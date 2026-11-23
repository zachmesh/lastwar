---
title: Growth orders and first findings - 2026-11-22 23:57 PT
created: 2026-11-22T23:57:00-08:00
modified: 2026-11-23T08:05:00Z
level: L3
version: 0.1.0
description: What was ordered for the growth Epic after the owner's four-flat-weeks verdict, the evidence the first reports added, and the state of the first read-then-fill run
status: in-progress
activity: team-operations
run_id: team-operations-2026-11-22-2357-growth-orders
trigger: Steer A messages 07:40Z, 07:45Z and 07:55Z; reports from planner, scout and researcher
started_at: 2026-11-22T23:35:00-08:00
finished_at:
duration_seconds:
verified: figures recomputed from the records (T10 793 x 1,647 = 1,306,071; barracks-day 599,782; Hut 2,400 per builder-day); Drill Ground evidence counted in the troop-training articles (82 'Full', 98 mention, 8 'unlocated', 26 '39,460')
---

# Growth orders and first findings

## Orders

- Decision record `2350-growth-start-rule-decision.md` (owner-delegated): resource-only starts of builds, research and training, 3x rule, reserves (food 100M, iron 150M, coin 10M, diamonds untouched), read first, fill only idle slots, measure again.
- Operator: first read-then-fill assignment (builders, labs, training; three runs) at 07:43:47Z, addendum with floors and priorities. Planner: the scout's read-only units (power breakdown, Drill Ground, upgrade previews, troops, buildings, research, heroes) and a recurring read-then-fill unit every 30 minutes from 08:15Z. Scribe: `_knowledge_/growth-plan/` (no snapshots folder: raw readings stay in records), playbook dated note, three digest Errata. Coach: restart the daily snapshots and count misses.

## What the reports added

- The binding limit is capacity, not stock: "Drill Ground Full" blocks training since 2026-10-31; a Lv.30 barracks trains T10 (+1,306,071 per batch of 793) and a Lv.24 one only T8. Troops are about 0.12 power per food or iron against 0.00008 for the Hut.
- Researcher: 32 claims, 10 tested, 18 sourced, 4 guesses; the hypothesis that builders sit idle is contradicted today (all four busy until 2026-11-24T09:20Z, started on the other device); Base Expansion day pays 30 duel points per building power point (a Hut finish is about 525,000 points).
- Scout: only one Power Details reading exists (2026-11-08: Hero 65.28M, Drone 5.81M, Building 10.29M of 149.85M), so 68.5M of power is in no record; building levels conflict across records.
- Measurement: net power is noisy (a 2,486,382 drop on 2026-11-09); a gross ledger of collections must precede ranking.

## State

Coin is 9.6M, under its 10M floor, so no coin-costing start is allowed yet. The code branch landed as PR 873 (`839bad3f`); the records branch follows. First start of something: not yet.

## Erratum 2026-11-23 08:05Z (measurement)

The figure 2,486,382 is **derived**, not a recorded measurement: my subtraction of two recorded readings, 149,217,331 (2026-11-09 07:45, many records) and 146,730,949 (2026-11-09 17:53, radar record 1754). The 11-10 building-queues record (`run-20261110-0112-p1`) documents "a fall of about 2.47M", flagged with no cause, three consecutive reads at the lower level. The issue 482 step is 641,100 (2026-11-08, a disconnect and relaunch). Cause **unverified**; an uncollected-troop-batch artifact is plausible and untested. Treat the 29-day change as uncertain by a few million; the fixed-state read (collect every finished batch first, then read) is mandatory.
