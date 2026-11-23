---
title: Research speed of the account - bounds from the queue timers - 2026-11-23 13:16Z
created: 2026-11-23T05:07:00-08:00
modified: 2026-11-23T05:20:00-08:00
level: L3
version: 0.4.0
description: The account's research speed from the Coin Output V and Food Output V timers, first without and then with the speed-up items the other device used; the current bound is a divisor of about 2.2 (plus 121 percent)
status: done
activity: research-queue
run_id: research-queue-2026-11-23-1307-speed-bounds
trigger: Steer B's frame forensics at 12:44Z, the operator's queue read at 12:56:50Z and its Backpack read at 13:11Z
started_at: 2026-11-23T05:05:00-08:00
finished_at: 2026-11-23T05:20:00-08:00
verified: base time 485,100 s from /tmp/oilres/aoo-sheet.csv (a guide sheet, [G]); frame times from Steer B (screenshots under ~/.computer-use/runs, not in the repository); timers and stock from the operator's records 1257 and 1308; the steps are in the sidecar CSV
---

# Research speed: current bound

## Inputs

- Guide base time of level 1 of both Output V nodes: 485,100 s (134.75 h) [G]; completion power 3,900 each [G, equals the measured Complete of Unlock Oil Well].
- Slot 2, Coin Output V: started between 12:09:04Z (slot idle in the operator's frame) and 12:11:30Z (labs 2/2 in a dimmed frame), ends 2026-11-24T14:59:10Z: effective 26h47m40s to 26h50m06s.
- Slot 1, Food Output V: 28h33m08s left at 12:56:50Z, start after 12:09:04Z: effective 28h33m to 29h18m.
- Backpack, 13:11Z against 11:26Z: the tech speed-up items (blue disc, 8h and 1h) fell by 3,960 minutes; general and construction items were not used.

## Current bound [D]

The first reading (divisors 5.02 and 4.6 to 4.7, speed +402 percent) assumed no speed-up was used and is SUPERSEDED (sidecar steps 1 and 2). With 66 hours of speed-ups split between two nodes that share one base time and one multiplier, the only consistent solution is a natural duration of 60.7 to 61.1 hours each (about 34 h of speed-up on Coin, 32 h on Food): divisor M = 2.21 to 2.22, research speed about +121 percent. The 879 base days on two labs take about 398 natural days. Convention: M is the divisor (base over effective); research speed is M minus 1; every ETA names both.

## Stock and assumptions

Remaining: tech 11,400 min (7.9 days), general 351,687 min (244 days), construction 167,895 min. Assumed: all 3,960 minutes went to these two nodes, the guide base holds, no start-only bonus. A clean read (an idle node panel, 2026-11-24T14:59Z) settles it.
