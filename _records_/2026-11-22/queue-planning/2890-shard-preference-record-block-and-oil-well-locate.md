---
title: Queue Planning The Shard Preference Record Block And The Oil Well Locate Read 2890 2026-11-23
created: 2026-11-23T08:00:00-08:00
modified: 2026-11-23T08:00:00-08:00
level: L0
version: 1.0.0
description: Planner pass adding Steer A's shard preference and the per-fight record block to the plunder scans and session unit, staging the Oil Well locate read for tomorrow, and correcting the later oil collection units after the first collection could not find the building
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0800-shard-preference-oil-locate
trigger: coordinator message 15:38Z
started_at: 2026-11-23T07:38:00-08:00
finished_at: 2026-11-23T08:00:00-08:00
verified: the scans, the session unit and the oil units read back; the first oil collection's result read in full; word counts under 450; validate exit 0
grounded_in:
  - source: coordinator message 15:38Z (Steer A's approval and additions)
  - source: _queue_/done/harvest-oil-well-2026-11-23-001.md
---

# Shard preference, record block and the Oil Well locate read, 2890

## Plunder

Scans `trucks-plunder-scan-2026-11-23-003` to `-009` (445 words) and the session unit `trucks-plunder-2026-11-23-002` (442 words) now say: PREFER the card showing the MOST shards (fight 1 paid 9 with stacks on the right, fight 2 paid 3 on the left), and record per fight the shards won, for each item the share of the cargo taken (loot over the cargo shown), the card's shard count and the slot numbers of its stacks, with the troops wounded, the count and Total Power. That gives the Strategist's second row a per-half yield, and after about eight fights the owner gets the measured yield per half.

## The Oil Well

`scout-midday-oil-well-locate-2026-11-24-001` (02:05Z to 06:00Z on 2026-11-24, serves PL-17, read only, 425 words) finds the building by panning the base, reads its tag text, position, storage, output and the Lv.N to N+1 preview, and does nothing else; it skips what a record of 2026-11-23 already gives. It is the fallback for today's assignment. The first collection (15:34Z) worked by the top-bar barrel panel (output 1.2K an hour, +3,760 oil) but never located the building, so the two later collection units (due about 23:30Z and 07:30Z) now say to collect by that panel route and no longer say to open the well by its tag. The panel's Details button has an unrecorded effect: under the standing rule it needs Steer A's approval first, so no unit presses it.

## Open

The operator respawn at 16:12Z needs nothing from me. The 22:03Z plan is due: ping me about 19:00Z.
