---
title: How it is done - dispatching part 2
created: 2026-11-23T07:16:21Z
modified: 2026-11-23T07:16:21Z
version: 0.1.0
sequence: 8
description: Mega Mode dispatch (UR days), observed end to end 2026-11-10 (0248 unit, Issue 565) - on
---
- Mega Mode dispatch (UR days), observed end to end 2026-11-10 (0248 unit, Issue #565): on the Your Truck tab the Mega Mode button opens two tabs. Mega Refresh lists the four slot rolls with rarity and journey time (0248 rolls: No.1 R 04:08:02, No.2 N 03:40:04, No.3 N 03:48:04, No.4 N 04:26:21 - none UR, so all four needed refreshes). A first refresh costs 3 Trade Contracts per truck (dialog-confirmed before spending); a re-refresh of an already-refreshed truck costs 1 (inferred from the button readings 9/158, 6/149, 3/149, 1/146). The 0248 unit spent 12 contracts in total (stock 158 to 146) and all four rerolled UR (No.1 04:37:27, No.2 04:16:08, No.4 03:42:29, No.3 03:53:44). The "Refresh all to Reindeer Sleigh Ride" checkbox was left unchecked; what it does is unobserved. Mega Dispatch shows preassigned escorts (Squad 1 25.20M, Squad 3 20.37M, Squad 2 19.08M, Squad 4 16.54M); Select All, Dispatch Selected, Confirm ("about to dispatch 4") dispatches all four at once - "All current trade trucks have been dispatched. Time for a coffee break!", Today's Dispatches 4/5, Trade Count 4/5. Expected duel score 4 times 300,000 = 1,200,000 (CORRECTED 2026-11-10 0337: the Duel screen reads Dispatch UR Trade Truck +300,000 live, superseding the 100,000 Handbook rate in tools/duel_schedule.json; the duel-score unit verifies the personal total live). Mega Mode does NOT convert a held roll to UR (0821 finding stands); it refreshes the slots until UR lands, then dispatches them as a batch.
- Let's Go dispatches. Journeys observed ran about 4 to just under 5
  hours. Rewards land when the truck arrives.

