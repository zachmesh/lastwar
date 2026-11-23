---
title: Queue Planning Builder Units Under Decision 2603 2550 2026-11-23
created: 2026-11-23T03:05:00-08:00
modified: 2026-11-23T03:05:00-08:00
level: L0
version: 1.0.0
description: Planner pass after the first-builder decision - the two builder units for 2026-11-24T09:20Z rewritten to start three Drill Ground steps with the F1c numbers, a shared reference sheet, the ledger updated with measured previews, and the finding that the per-level slot gain is not constant
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0305-builder-units-2603
trigger: coordinator message with decision 2603 and the F1c numbers
started_at: 2026-11-23T03:00:00-08:00
finished_at: 2026-11-23T03:05:00-08:00
verified: figures read from the F1c record and recomputed; unit files read back; word counts 323 and 390; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/team-operations/2603-first-builder-decision.md
  - source: _records_/2026-11-22/growth/1054-f1c-drill-grounds.md
---

# Builder units under decision 2603, 2550

## 1. Units

`building-queues-growth-convert-2026-11-24-001` (from 09:22Z, expiring 09:50Z): read the builders, then on the first idle builder the Lv.26 ground (59.5M coin from Coin Chests), on the next the Lv.27 ground (83.3M), each with a bounded speed-up after its preview. `-002` (expiring 10:20Z): skip any ground already upgrading, the third step on the Lv.28 ground (119.0M from plain Resource Chests in bulk, never Resource Choice Chests, stop without spending if no bulk selector), then the fourth builder by the Strategist's ranking with the Builders Hut Lv.25 to 26 as the default if coin allows. Both start only on idle builders, carry the tag-text rule, and point at one shared sheet, [2540](2540-drill-ground-sheet.md), for tap points, the pan, the measured previews, the coin plan and the hazards. The briefs are 323 and 390 words.

## 2. Numbers

Measured by F1c: Lv.26 to 27 costs 59.5M coin and 74.8M iron in 10d 02:30:19 for +21,600; Lv.27 to 28 costs 83.3M and 102.0M in 14d 03:30:26 for +25,600; Lv.28 to 29 costs 119.0M and 144.5M in 18d 09:21:34 for +30,400. Together 261.8M coin and 321.3M iron. The Coin Chests cover the first two with 138M of the 281M read left, above the 50M emergency reserve.

## 3. A finding

The Unit Count change is +200 on the three lower steps and only +100 on Lv.30 to 31 (+8,000 to +8,100), so the claim of +200 slots a level is not constant; that step is also out, needing Headquarters Lv.31. The ledger row now says 100 slots, 0.56 per million coin. The Details figure and the preview's current figure also differ by 835 to 2,080 and are not explained.

## 4. Open

The Strategist's veto window runs to 20:00Z today. A bulk selector for plain Resource Chests is assumed, not seen; the unit stops without spending if it is absent.
