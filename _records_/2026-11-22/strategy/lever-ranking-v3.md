---
title: Lever ranking for strategy v3.0 draft
created: 2026-11-23T09:02:00Z
modified: 2026-11-24T04:26:00Z
version: 0.4.0
level: L3
description: The merged capacity and materials ranking by power per scarce unit, with the evidence tag and the read that would change each rank
status: unverified
grounded_in:
  - source: _records_/2026-11-22/strategy/lever-ranking-v3.csv, 12 rows
  - source: Steer A wave-2 reports, the operator records 1047 and 0030, and the inventory read
---

# Lever ranking v3.0 draft

Rows in [the sidecar](lever-ranking-v3.csv). Draft: the 12:30Z version waits for the previews. Rank is the owner's order first, then power per scarce unit.

## What changed at 12:45Z

The owner ordered Base Expansion as the strategy's priority, so "HQ 31 and the Age of Oil path are off" is retired. The earlier ranking by power per unit stays for the short line, and the long line sits above it by order, not by arithmetic ([decision 03](dec-20261123-03.md)).

## Top five

1. **Base Expansion line** (owner order). Path nodes +411K power [S1] and HQ 31 +63,700 [M] with Hero Level Cap 155; oil binds, ETA 2027-01-08 to 01-23 ([ETA note](0510-base-expansion-eta.md)); it carries the 3rd Tech Center, Fast Builder V and Research Enhancement V.
2. **Drill Ground levels,** the only reachable room (ramp base case: each level releases 200 finished troops, 35.7K, 25.6K and 19.9K a builder-day on the first three, about 1,042 troops waiting, then training): 8,189 troops (10.2M to 13.3M power) wait behind it; +200 slots a level, three started at 23:20Z, the first done 12-03 19:20Z ([room levers](0670-room-levers.md)).
3. **Unit Count extras:** 5,969 slots of unread source; a read-only unit decides if they can be raised.
4. **Hero Tier 5 stars** for Lucius and Schuyler: 120 of 680 shards close the gaps, +0.3M to +1.0M [G]; weapon steps wait for the Murphy test (0640).
5. **Promotion, +2.75M,** when the panel opens.

## Forecast, 30 days

Base +1.8M; with promotion +4.5M; with three ground levels filled +1.1M more: upper bound near +5.6M (3.7 percent) [G]. Base Expansion adds no power by itself in 30 days beyond node gains (+3.9K or more each).

## Retired by evidence

The Extra Drill Ground and new-ground lever (rank 1 on 11-23 08:00Z) is retired: all four grounds exist (F-006 and F-007 are scored misses; decision 01 v1.2).

## Last

Gear stars and hero levels stay off until previews. Truck plunder (decision 04) is a food and coin supplement, ranked fifth after the first fight cost no troops (n=1).
