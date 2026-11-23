---
title: Research speed of the account - bounds from the queue timers - 2026-11-23 13:16Z
created: 2026-11-23T05:07:00-08:00
modified: 2026-11-23T06:09:00-08:00
level: L3
version: 0.5.0
description: The account's research speed - first estimates from the queue timers, superseded by the clean read at the start of Iron Output V - divisor 3.678 (plus 268 percent)
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

## Current bound [M] (measured at 14:00:54Z)

The first readings (divisors 5.0, then 2.2) were estimates and are SUPERSEDED (sidecar steps 1 to 4). The clean read: Iron Output V started with no speed-up and a timer of 131,879 s (equal to the Finish Now clock), against the guide base 485,100 s: DIVISOR 3.678, research speed about +268 percent. The blue Research button of the same panel read 147,000 s (divisor 3.30) and is not the effective time: read the Finish Now clock. The progress-bar estimate (3.5 to 3.7) was right; the 66 hours of tech speed-ups seen gone from the Backpack were mostly NOT on these two nodes (about 20 h were). The 879 base days on two labs take about 239 natural days. Convention: M is the divisor; research speed is M minus 1; every ETA names both.

## Stock and assumptions

Remaining after today's 1,505 tech minutes on Coin Output V: tech 9,895 min (6.9 days), general 351,687 min (244 days), construction 167,895 min. The guide base time of Output V level 1 held (485,100 s). Speed-up stock (251 days) exceeds the natural path (239 days), so oil, not the labs, limits the date if the stock is spent.
