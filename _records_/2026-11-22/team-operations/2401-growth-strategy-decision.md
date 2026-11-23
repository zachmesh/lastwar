---
title: Decision - the growth strategy v1.1 is the working plan - 2026-11-23 08:20Z
created: 2026-11-23T00:01:00-08:00
modified: 2026-11-23T08:10:00Z
level: L3
version: 0.1.0
description: The owner asked for a researched growth strategy; v1.1 is adopted as the unverified working plan, with reserves, a coin correction and a read-first sequence
status: done
activity: team-operations
run_id: team-operations-2026-11-23-0801-growth-strategy
trigger: Steer A message 08:20Z with the strategy v1.1
started_at: 2026-11-23T00:01:00-08:00
finished_at: 2026-11-23T00:05:00-08:00
verified: strategy read in full; coin and power-breakdown figures checked against _tools_/state/resources.jsonl and the growth fill-run record 2344
---

# Decision: strategy v1.1 is the working plan

## Owner's words (2026-11-23, relayed)

"Comprehensively research the best growth plan ... you may reserve some resources, do not spend them all, but clearly and carefully prioritize for growth." Then: should the team establish a strategy from this research. Answer: yes; the coordinator lands and executes it.

## Adopted

Strategy v1.1 (Steer A, 08:15Z; status unverified, evidence tags kept) lands as small articles under `_knowledge_/growth-plan/` (Charter and Strategy pages). Levers in order: troop promotion plus Drill Ground capacity; exclusive weapons; fill every idle slot by power per coin and slot-day; a coin campaign; drone, decorations, Wall of Honor, gear levels; medals and EXP in scoring windows; the long line to Season 3. HQ 31 and the Age of Oil path are not funded. Reserves: food 100M, iron 150M, coin 10M, diamonds untouched, duel-day reservation; the rest under the 3x rule. Unchanged: no purchase, diamond spend, speed-up, PvP, diplomacy or ally exchange.

## Corrections from our own measurements

- **Coin: 35.3M at 04:03Z, 9.6M by 07:48Z.** See the erratum below: the 35M figure was real; about 26M was spent within hours, likely on the owner's four Training Base upgrades. Every coin-costing start waits for the coin campaign or an explicit exception.
- **The power split is now measured** (Power Details, 150,211,809): Hero 66.24M, Unit 63.51M, Building 9.75M, Drone 5.84M, Tech 4.87M. Units and heroes are 86 percent; buildings and research together 10 percent.
- **Today nothing is startable:** builders 4 of 4 busy until 2026-11-24T09:20Z, both labs busy (one free about 11:43Z), training blocked by Drill Ground Full (Drill Ground Lv.28).

## Sequence

Read first (the snapshot gates everything); two fixed-state power reads a day; fill idle slots; find and read the Drill Ground and the promote panel; every action logs exact Total Power before and after. Provisional goal: 5x today's pace within two weeks; a real target after the snapshot (review 2026-11-30).

## Erratum 2026-11-23 08:10Z (coin, corrected by Steer A's source)

The roughly 35M coin was a real reading: the observation run `20261123T040311Z-e26691` (HUD "35.3M", 04:03Z) and the operator's survivors record at about 04:05Z. `resources.jsonl` only had 33.9M from 2026-10-28, which is why I called the 35M stale. The operator's HUD read at 07:36Z to 07:48Z shows 9.6M: about 26M was spent in roughly three hours after the 04:24Z builder check found all four builders idle and then busy on Lv.25 Training Base upgrades; very likely the owner on the other device (unverified). My earlier "24M left in four weeks" is withdrawn. Coin is the gate; until the owner says how to split it, no coin-costly build or research starts.
