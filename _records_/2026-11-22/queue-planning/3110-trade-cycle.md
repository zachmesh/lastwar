---
title: Trade Cycle Settle Dispatch And Plunder On One Badge 3110 2026-11-24
created: 2026-11-24T02:25:00-08:00
modified: 2026-11-24T06:45:00-08:00
level: L0
version: 1.3.0
description: The procedure of one trade cycle - at a tram badge, settle the returned trucks, dispatch into the empty slots by rule 2, then plunder within today's count and the OD-20 guards - built from record 1000 and Steer A's ruling of 2026-11-24 10:16Z
status: done
activity: queue-planning
run_id: queue-planning-2026-11-24-0225-trade-cycle
trigger: Steer A message 10:16Z
started_at: 2026-11-24T02:14:00-08:00
finished_at: 2026-11-24T02:25:00-08:00
verified: tap points copied from the operator record 1000 as relayed and read; none of the plunder steps has been run yet
grounded_in:
  - source: _records_/2026-11-22/truck-plunder/1000-queue-run.md
  - source: _activities_/truck-plunder/rule-digest.md
---

# Trade cycle, 3110

## When

At every tram badge (red N = N free slots or returned trucks). NO badge, NO tap (Steer A): the icon then only pans the camera. A unit that finds no badge closes 'badge absent: no tap' with the frame; the Coordinator re-dispatches 15 minutes later, at most 3 tries.

## 0 Hospital first (units that plunder)

BEFORE the tram tap, read the Hospital Lv.25 figures behind its tag's orange middle button: free room = 7,999 minus wounded minus 'Completed'. Under 1,000: do the cycle without the plunder step and write 'blocked by capacity: hospital room'.

## 1 Open and settle

WORLD then BASE; write the tram icon's (107,580) badge state with the UTC time; with a badge ONE tap opens INTERCITY TRADE on Others' Trucks. Tap the Your Truck tab (479,942): four slots, three usable, slot 4 locked. A returned truck settles when its Truck Details open; claim Reward Recovery at the red dot; write each truck's rewards.

## 2 Dispatch, rule 2

Up to the unit's number, into each empty slot's green plus ((298,450), (362,450), (426,450)); at most 3 out at once, 5 a day. SR or above as rolled: Let's Go ONCE. Below SR: the free dice refresh once, then Trade Contract refreshes, each after reading the price line (the contract count and 1): up to TEN per slot and 60 a day over the five dispatches (Steer A 14:30Z); the stock floor is 80 (below 120 each further refresh needs a one-line reason in the unit note); any diamond or other price: STOP; after ten take the best roll as it stands; no Mega Mode (UR duel days only). Per dispatch: frame, quality, arrival, count, contracts used.

## 3 Plunder

Switch to the Others' Trucks tab. Stop after any fight wounding more than 50 troops. Read the count; stop at 4 of 4. The list has the filter 'out trucks from your Warzone' ticked and about 17 rows; refresh only if its button reads Free. Target: a gold (UR) or purple (SSR) truck with a UR 500-badge stack in either half, guard under Squad 1 (25.61M), arrival over 30 minutes; prefer the most shards; the opened card decides. Quick Plunder once, Battle once, per fight, up to the unit's number. Record per fight: shards won, share of each item, the card's shard count, troops wounded, the count ('Your Plunder Count Today' decides, never arithmetic), Total Power. Never Collect, Heal, Recover, History or Speed Up.

## 4 Close

The trade screen stays open across the runs of one unit (no trip to the base between runs); every fight records the guard, quality, cargo and loot. The History read (cycle A only) is done. The blue back arrow (109,941), then read the Hospital free room again; write the badge state and trade count again. Another app, alert or dialog: stop, name `lsappinfo front`; TIPS Cancel only.
