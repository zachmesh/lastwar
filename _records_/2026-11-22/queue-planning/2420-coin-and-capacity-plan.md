---
title: Queue Planning Coin Supply Capacity First And Guard Bypass Log 2420 2026-11-23
created: 2026-11-23T00:15:00-08:00
modified: 2026-11-23T00:15:00-08:00
level: L0
version: 1.0.0
description: Planner pass for the coin plan and strategy v2.0 - coin supply and sink tables, capacity sources ranked by slots per million coin, briefs rebuilt under the commit gate, seven scout units and a collect unit staged under the bounded stale-tool bypass, with every bypass use logged
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0015-coin-and-capacity
trigger: coordinator coin plan and strategy v2.0 messages, option B authorization
started_at: 2026-11-23T00:06:00-08:00
finished_at: 2026-11-23T00:15:00-08:00
verified: word counts of every staged unit measured before and after; the pick order simulated at three instants; ledger and capacity CSVs parsed; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/growth/2357-troop-read.md, the operator's hospital and tier census
  - source: _records_/2026-11-22/queue-planning/2410-coin-supply.csv, 2410-coin-sinks-ranked.csv, 2420-capacity-sources.csv, 2400-candidate-ledger-template.csv
  - source: _tools_/queue.py refuse_if_tool_stale
---

# Coin and capacity plan, 2420

## 1. Capacity is the gate

The operator's tier census (Lv.7 1,116, Lv.8 2,141, Lv.9 1,878, Lv.10 35.1K) totals 40,235 against a Drill Ground cap of 39,460 read on 2026-10-31, and 35.1K at 1,647 plus the lower tiers lands near the 63.51M unit power. So the cap appears to count every troop owned (inference). Waiting troops are 5,306 healed plus the 793 and 726 batches in training, 6,825 in all, which at +200 slots a level is about 34 levels. [Capacity sources](2420-capacity-sources.csv), by slots per million coin on the strategy and guide costs: Drill Ground L21 18.2, L22 13.3, L23 11.1, L24 8.7, L25 5.1, L26 3.7, L27 2.9. Drill Ground Expansion and the Extra node are unread. The ledger gains `slots_gained` and `slots_per_million_coin`. Promotion needs no slots, and the T8 and T9 tiers alone would add 1.80M if it works.

## 2. Coin supply

[Supply](2410-coin-supply.csv): HUD coin 9.6M, plus the convertible total (pending the operator's inventory CSV), plus the campaign at about 16M to 26M a day between bursts. [Sinks](2410-coin-sinks-ranked.csv) rank by power per million coin; gear levels and hero skills have no queue and wait for the previews. No conversion-and-spend unit is minted yet, because C1 and the inventory CSV have not landed. Hero levers are never converted. The first free lab and builder are reserved for the coordinator's capacity pick, and fills start nothing in them.

## 3. Order and briefs

F1 moved into the early group: P2, T2, F1, S1 run in that order, then the first fill; the Secrets claim leads at 08:50Z. S1 duplicates the direct inventory read and will probably expire; S1b should take the universal count from the inventory CSV. All staged briefs are now under the gate. Before, then after, in words: power A 682 to      338, power B 676 to      336, P2 626 to 430, A1 552 to 389, 13 fills 538 to 383; 16 snapshot briefs were shortened to one pointer line. Fills now carry hospital first, Complete, the coin hold and no conversion.

## 4. Stale-tool bypass log (`LASTWAR_QUEUE_ALLOW_STALE_TOOL=1`, authorized to the merge or 09:15Z)

Eight uses, all `enqueue`: seven snapshot units 08:08:25Z to 08:08:28Z (chain seq 011 to 017), then one collect unit at about 08:09Z. No `next`, `sync`, `plan` or `sweep`. Before the authorization two enqueues were refused (08:04Z and 08:06Z) and one `next` at 08:06Z ran without the flag only because the fetch failed. I stop using the flag at the merge notice or 09:15Z by the Mac clock. Steer A's time labels run about an hour ahead of this Mac, so every window here uses the Mac's UTC.
