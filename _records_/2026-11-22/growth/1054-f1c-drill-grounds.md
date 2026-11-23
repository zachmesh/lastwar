---
title: Drill Grounds F1c
created: 2026-11-23T11:03:00Z
modified: 2026-11-23T11:03:00Z
version: 1.0.0
description: Continuation of F1b under assignment A-20261123-1054-operator - Building Details and Upgrade previews of the Drill Ground Lv.26, Lv.27 and Lv.30, with the Lv.28 row from F1b; coin is short for every step, the Lv.30 ground needs Headquarters Lv.31
status: done
grounded_in:
  - source: cu_bridge runs 20261123T105505Z-cc809f (Lv.26 and Lv.27) and 20261123T105714Z-34383a (Lv.30), events, final results and the Lv.30 preview frame, 2026-11-23T10:55Z to 10:58Z
  - source: 1047-f1b-drill-ground.md (the Lv.28 row) and coordinator assignment A-20261123-1054-operator
---

# Drill Grounds F1c

Rows in [1054-f1c-drill-grounds.csv](1054-f1c-drill-grounds.csv). Each ground is a red parade field (tap a
soldier); the tag text was read at the tap. Nothing pressed: no Upgrade, Finish Now, Obtain, Construct or
Quick Dispatch. Stock at the reads: food 648.5M, iron 1.0G, coin 14.4M.

| Tag | Details Unit Count | Preview | Unit Count | Power | Coin | Iron or food | Prerequisite | Time original / effective |
|---|---|---|---|---|---|---|---|---|
| Drill Ground Lv.26 | +8035 | Lv.26 to 27 | +7,200 to +7,400 | +21,600 | 59.5M | iron 74.8M met | HQ Lv.27 met | 21d 11:19:25 / 10d 02:30:19 |
| Drill Ground Lv.27 | +8843 | Lv.27 to 28 | +7,400 to +7,600 | +25,600 | 83.3M | iron 102.0M met | HQ Lv.28 met | 30d 01:27:10 / 14d 03:30:26 |
| Drill Ground Lv.28 | +9211 | Lv.28 to 29 | +7,600 to +7,800 | +30,400 | 119.0M | iron 144.5M met | HQ Lv.29 met | 39d 01:53:19 / 18d 09:21:34 |
| Drill Ground Lv.30 | +10080 | Lv.30 to 31 | +8,000 to +8,100 | +37,500 | 178.5M | food 671.5M short | HQ Lv.31 NOT met | 55d 21:10:50 / 26d 07:08:38 |

- **All four grounds have 4 officer slots, all filled.** The Details figure (8035, 8843, 9211, 10080) differs from the
  preview's current figure (7,200, 7,400, 7,600, 8,000) by 835, 1,443, 1,611 and 2,080 (not constant; unexplained, perhaps officer or skill bonus); both are shown as read.
- **Coin is the limit.** 14.4M is under every cost, and the 10M reserve leaves 4.4M spendable; the cheapest step,
  Lv.26 to 27, needs 59.5M coin and 74.8M iron. Power per million coin: Lv.26 363, Lv.27 307, Lv.28 255,
  Lv.30 210, so the lowest ground first. The Lv.30 step also needs Headquarters Lv.31 and food it lacks.
- **Builders.** All four are busy on Training Base to Lv.25 until 2026-11-24T09:20Z, so no ground can start earlier.
- **Camera.** Each tap shifts the view 30 to 85 px; the tag text confirmed each ground at the second tap.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 13 and 9 steps, 0 refused, no `local_input` pause, 0.169154 and
  0.115302 USD, 0.284456 in all (stated cap 0.5).
- Closing state: the base, fresh frame, no panel, token released.
