---
title: Queue Planning Ledger v1.2 Coin Picture And Strategy Deltas 2400 2026-11-23
created: 2026-11-23T00:08:00-08:00
modified: 2026-11-23T00:08:00-08:00
level: L0
version: 1.0.0
description: Planner pass applying strategy v1.3 to v1.5 - candidate ledger v1.2 with coin_cost and power_per_coin, a measured coin history that contradicts a flat 35M, brief edits for v1.4, next actions per lever, and a queue-tool guard that blocks staging the seven new scout units
status: partial
activity: queue-planning
run_id: queue-planning-2026-11-23-0008-ledger-v1-2
trigger: coordinator messages for strategy v1.2 to v1.5
started_at: 2026-11-22T23:57:00-08:00
finished_at: 2026-11-23T00:08:00-08:00
verified: coin readings checked at their lines; per-million figures recomputed in code; unit edits read back; validate exit 0; the guard refusal reproduced twice
grounded_in:
  - source: _records_/2026-11-22/queue-planning/2400-candidate-ledger-template.csv, 27 rows, 15 columns
  - source: 2400-building-guide-rows.csv, 2400-coin-history.csv, 2400-next-actions-per-lever.csv in the same folder
  - source: /tmp/growth-strategy-v1.3.md and v1.4.md, copied rows from /tmp/lw/building-power-gains-L25-31.csv
---

# Ledger v1.2, 2400

## 1. Schema and order

[Ledger](2400-candidate-ledger-template.csv) adds `coin_cost` and `power_per_coin`. I added one category, `drone`, because the strategy ranks drone apart from heroes. Rows follow the v1.5 value order: collect finished batches; the hero block; drone; Drill Ground levels when coin allows; research in idle labs; Oil Well and small buildings. Ten rows are `unread` and cannot be ranked. [Guide rows](2400-building-guide-rows.csv) are copied into the repo (49 rows).

## 2. Coin is bursty, not flat

[Coin history](2400-coin-history.csv), 13 rows, 11 checked at their source lines and 2 as given by the coordinator: 145.7M on 11-12, 27.7M on 11-16, 107.6M on 11-21, 109.2M on 11-22 at about 11:23 PT, 35.3M, then 9.6M. Between spend bursts coin accumulated roughly 16M to 26M a day (derived, times approximate, includes events). Bursts: about 118M gone between 11-12 and 11-16, about 100M on 11-22. So the limiter is the other device's spending, not income, and a level that costs 11M takes under a day of accumulation if nothing is spent. This conflicts with "even L21 is out of reach"; it rests on the owner's split.

## 3. Coin sinks by power per million coin

Guide data, unverified. Drill Ground L21 to L24: at least 14K to 30K (capacity case). L25: 8.9K, L26: 6.5K, L27: 5.0K. Training Base L26: 845. Builders Hut L26: 795 only if the guide's 22M applies; the 11-09 panel listed iron and food only. Barracks L30: 151. Tech Center L30: 143. HQ L30: 130. Troops are near saturation (1,609 per troop, 97.7 percent of T10), so collecting and promotion are a one-off of about 1.3M to 1.5M, and my earlier 600k per barracks-day was the rate while capacity was free.

## 4. Corrections and disclosures

- The 11-09 fall is derived (149,217,331 to 146,730,949 is 2,486,382), cause unverified, probably a collection-state artifact. Wording from now: about 2.47M, cause unverified.
- Edited by hand, all unclaimed: 13 fill briefs (v1.4 Complete rule, builder and lab priority, collect first); the two power units (collect first); time fields of P1, F1 and T1; `serves` lines on 16 units; one line in `_queue_/unit-template.md`. Season Photo is not re-minted until a new season icon, about 2026-12-13.

## 5. Blocker: seven units not staged

`enqueue` and `next` are refused whenever the fetch of origin/main succeeds. Origin carries the older `queue.py`; this checkout holds the serves commits f091ac9d and d9d6a7a6, so the byte comparison fails (issue #694). Reproduced twice; once a failed fetch let `next` through. I did not set the bypass flag. Waiting on the coordinator. Staged when cleared: P2 08:00 to 08:43Z, S1 08:00 to 08:44Z, D1 09:05 to 09:27Z, D1b 09:05 to 10:54Z, S1b 09:05 to 11:09Z, C1 09:05 to 11:14Z, A1 11:45 to 12:50Z.

## 6. Next actions

Three per lever, with unit and check, in [the actions file](2400-next-actions-per-lever.csv): 21 rows over 7 levers.
