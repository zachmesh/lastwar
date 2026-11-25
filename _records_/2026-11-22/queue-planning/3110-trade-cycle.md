---
title: Trade Cycle Settle Dispatch And Plunder On One Badge 3110 2026-11-24
created: 2026-11-24T02:25:00-08:00
modified: 2026-11-24T06:45:00-08:00
level: L0
version: 1.7.0
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

At every tram badge (N = the Your Truck tab badge: free slots or returned trucks; 11-25: 3 empty slots, Others' tab 4). The badge can be a STALE DOT: on 11-24 with a returned truck waiting it was dark (18:20:31Z) and, a second time, the icon was not drawn at all (18:50:40Z), then read 1 about 8 to 9 seconds after a WORLD then BASE (n=2). At NO badge on the FIRST read: WORLD then BASE (one tap each on the standing corner button, no icon), then read ONCE: lit: enter; still dark: close 'badge absent: no tap' with the frame. Also read the WORLD frame (the dot may show there, about 3 s after the WORLD tap) and write the icon's state at every read: absent, bare or badge N. A bare icon only pans the camera: never tapped. The Coordinator re-dispatches a dark close 15 minutes later, 3 tries at most.

## 0 Hospital first (units that plunder)

BEFORE the tram tap, read the Hospital Lv.25 figures behind its tag's orange middle button: free room = 7,999 minus wounded minus 'Completed'. Under 1,000: skip the plunder step and write 'blocked by capacity: hospital room'.

## 1 Open and settle

Write the tram icon's (107,580) badge state with the UTC time; with a badge ONE tap opens INTERCITY TRADE on Others' Trucks. Write BOTH tab badges at entry. Tap the Your Truck tab (479,942): four slots, three usable. A returned truck settles when its Truck Details open; claim Reward Recovery at the red dot; write its rewards.

## 2 Dispatch, rule 2

Up to the unit's number, into each empty slot's green plus ((298,450), (362,450), (426,450)); at most 3 out, 5 a day. SR or above as rolled: Let's Go ONCE. Below SR: the free dice refresh once, then Trade Contract refreshes, each after reading the price line (the contract count and 1): up to TEN per slot and 60 a day; stock floor 80 (below 120 each further refresh needs a one-line reason); any diamond or other price: STOP; after ten take the best roll; no Mega Mode. Per dispatch: frame, quality, arrival, contracts.

## 3 Plunder

On the Others' Trucks tab: Stop after a fight wounding over 50. Read the count; stop at 4 of 4. The list has 'out trucks from your Warzone' ticked; refresh only if Free. Target: a gold (UR) or purple (SSR) truck with a UR 500-badge stack in either half, guard under Squad 1 (25.61M), arrival over 30 minutes. Quick Plunder once, Battle once, per fight. Record per fight: shards won, item shares, troops wounded, the count ('Your Plunder Count Today' decides), Total Power. Never Collect, Heal, Recover or Speed Up, and never History unless the unit names sheet 3150.

## 4 Close

The blue back arrow (109,941), then re-read the Hospital free room, the badge state and the trade count. Another app, alert or dialog: stop, name `lsappinfo front`; TIPS Cancel only.
