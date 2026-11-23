---
title: Category baseline, misses and resources - 2026-11-23Z
created: 2026-11-23T07:54:00Z
modified: 2026-11-23T07:54:00Z
version: 1.0.0
description: Coach record after the operator's first exact power breakdown - gain per day by category against the 2026-11-08 reading, recorded versus unattributed gain, the first post-restart miss count and the resource deltas
status: done
activity: coach
run_id: coach-2026-11-22-2354
trigger: coordinator confirmation of slots A and B with the growth folder now open
started_at: 2026-11-23T07:51:00Z
finished_at: 2026-11-23T07:54:00Z
duration_seconds: 180
verified: no
grounded_in:
  - source: _records_/2026-11-22/growth/2344-power-breakdown.csv and 2344-fill-run.md
  - source: _records_/2026-11-08/resource-collection/0958-queue-run.md
  - source: _tools_/state/resources.jsonl rows 14 and 15
---

# Category baseline

Second breakdown, 2026-11-22 23:47 PT, against the first, 2026-11-08 09:58 PT: 14.576 days ([categories](power-by-category.csv)). Net +361,456, or +24,799 a day, against 13,466 over 29 days.

| Category | Change | Per day | Recorded in ledger | Unattributed |
|---|---|---|---|---|
| Hero | +959,061 | +65,799 | +8,219 | +950,842 |
| Drone | +33,387 | +2,291 | 0 | +33,387 |
| Building | -543,250 | -37,271 | +21,600 | -564,850 |
| Unit plus Tech | -87,742 | -6,020 | +1,298,143 | -1,385,885 |
| Total | +361,456 | +24,799 | +1,327,962 | -966,506 |

- Recorded gains run 91,108 a day, 97 percent troop batches, and net 3.7 times less: about 66,309 a day leaves unattributed.
- Hero rose 959,061 with one recorded level (+8,219). The rest is unattributed, possibly other-device play; unverified.
- Troop and tech batches recorded +1,298,143 yet the line fell 87,742, so about 1.39M was lost with no record. Cause unverified; wounded or lost troops is a hypothesis.
- The Buildings line fell 557,600. With Unit plus Tech it sums to -645,342, within 4,242 of the 11-08 step-down of 641,100 (issue 482): consistent, not proof.
- Survivor and Unit plus Tech for 11-08 are derived by subtraction. One pair is one interval, not a series.

## Misses

Post-restart reads in `_records_/2026-11-22/growth/`: 1 (2344, 07:47Z). Builders 4 of 4 and labs 2 of 2 busy. The Lv.24 barracks is idle, blocked by Drill Ground Full; a fourth tent looks idle, untried. Startable misses: 0; blocked: 1 ([log](misses-log.csv)). Per the record no builder frees until 2026-11-24T09:20Z, so the Drill Ground Lv.28 start, which would lift the cap, waits about 25 hours.

## Resources

Coin 33.9M to 9.6M in 25.88 days (-0.94M a day); food +507.6M; iron about +676M, rounded. Coin cause unverified ([deltas](resource-deltas.csv)).

## Slots

A (02:00Z to 04:00Z) and B (13:00Z to 15:00Z) confirmed. The 07:47Z read is outside both. Next report 12:00Z.
