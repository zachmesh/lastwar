---
title: Trucks queue run 0248
created: 2026-11-10T10:48:00Z
modified: 2026-11-10T10:48:00Z
version: 1.0.0
description: Ticker pass ticker-0234 trucks unit - 4 UR trucks dispatched by Mega Mode, 1 plunder won
status: unverified
---

# Trucks - ticker-0234, 02:36 to 02:48 PST

Unit trucks-2026-11-09-2257, executor ticker-0234. Status partial.
Duel day 2, Base Expansion - UR truck dispatches score 100,000 each
(Handbook rate, from tools/duel.py). Window: duel day 2, UR trucks,
Mega UR only.

## Counters, read live on the trade screen

- Entry: Today's Trade Count 0/5, Your Plunder Count Today 0/4.
  Yard empty, no returned truck to settle.
- Close: Today's Trade Count 4/5, Your Plunder Count Today 1/4.
  Both read live in this unit.

## Dispatch - Mega Mode, first execution of the standing UR-day rule

- Entry: base-screen left column, blue truck-front icon with red
  badge 4, grounded at norm 52,569. Trade screen opened on
  Others' Trucks; Your Truck tab showed 4 empty slots and the
  Mega Mode button.
- Mega Mode has two tabs: Mega Refresh and Mega Dispatch. Mega
  Refresh listed the four slot rolls: No.1 R 04:08:02, No.2 N
  03:40:04, No.3 N 03:48:04, No.4 N 04:26:21. None was UR, so
  all four needed refreshes before a UR-only dispatch.
- Mega Refresh cost, dialog-confirmed before spending: 3 Trade
  Contracts per truck on its first refresh (9 for the 3-truck
  batch, 3 for No.3 alone). A re-refresh of an already-refreshed
  truck costs 1 - inferred from the button reading 1/146 for
  No.3 after its refresh, consistent with the four readings
  9/158, 6/149, 3/149, 1/146; the 6/149 reading was first
  misread as 2/149. Total spent 12 Trade Contracts, stock
  158 to 146. No diamonds spent.
- Batch 1 (No.1, No.2, No.4 selected): all rerolled UR - No.1
  04:37:27, No.2 04:16:08, No.4 03:42:29. Batch 2 (No.3 alone):
  UR 03:53:44. The "Refresh all to Reindeer Sleigh Ride"
  checkbox was left unchecked; what it does is unobserved.
- Mega Dispatch tab: escorts Squad 1 25.20M, Squad 3 20.37M,
  Squad 2 19.08M, Squad 4 16.54M. Select All, Dispatch Selected,
  Confirm ("about to dispatch 4") - "All current trade trucks
  have been dispatched. Time for a coffee break!", Today's
  Dispatches 4/5, Trade Count 4/5. Four gold UR trucks visible
  on the road on the Your Truck view.
- Expected duel score: 4 times 100,000 = 400,000, Handbook
  rate, not a live read - the duel-score unit verifies it live.

## Plunder

- Attempt 1: [BROT]TPM01, UR, Lv.30, guard 11.2M, cargo with
  three UR shard stacks (100 x1 at positions 1, 2, 6). Quick
  Plunder opened battle prep (25.20M vs 11.25M); the Battle tap
  showed the toast "The target has disappeared" and a second
  tap did nothing. Backed out; the truck was gone from the
  road. No plunder counted.
- Attempt 2: [STCL]De Stenenman, UR, Lv.30, guard 24.6M (prep
  screen 24.69M), two 500 x3 UR shard stacks at right-side
  cargo positions 5 and 6, arrives in 01:49. Quick Plunder,
  Battle (25.20M vs 24.69M), Mission Completed. Yield, read
  live on the rewards screen: iron 951.8K, food 951.8K, coin
  607.5K, 5m speedups x10 in four stacks (5, 2, 2, 1), UR
  shard 500 x3 plus Extra x3 (6 total), one blue chest x1.
  Plunder Count 1/4 after Return.

## Notes for the next trucks unit

- Dispatch 1 of 5 still open: all four slots are out until the
  trucks return (03:42 to 04:37 dispatches, plus the return
  leg), so the 5th dispatch is a second wave, not available
  now. Plunder 3 of 4 still open.
- Reward Recovery (Recover button, bottom left of the trade
  screen) still carries a red dot - not checked in this unit.
- One Return tap missed because pixel coordinates were passed
  where the control expects normalized 0-1000 coordinates;
  re-grounded at norm 662,893 and it worked. Coordinates for
  computer.control are always normalized.
- Mid-unit transient, about 02:51 during the No.3 refresh
  confirm: an observe call failed "target app exited or
  restarted", but LastWar was still running (pid 1908) and the
  refresh dialog was still up. No different-device dialog was
  seen in this unit; kick count 0.
- Mega Mode mechanics are now observed end to end for the
  first time; the activity metadata still lists Mega dispatch
  as an open question. A knowledge issue is filed from this
  record so the metadata update is not lost.

## Result stats

- target: dispatch 5, plunder 4
- achieved: dispatch 4, plunder 1
- resources_gained: iron 951.8K, food 951.8K, coin 607.5K,
  UR shards 500 x6, 5m speedups x10, blue chest x1
- points: 400000 (expected duel points, Handbook rate,
  pending live verification by the duel-score unit)
- costs: 12 Trade Contracts, about 12 minutes
- verified: yes (counters and rewards read live in-unit)
- blocker_category: h (by-design partial - the 15 minute
  unit cap closed the quota mid-way; dispatch 4/5, plunder
  1/4, remainder resumes in the next trucks unit)
