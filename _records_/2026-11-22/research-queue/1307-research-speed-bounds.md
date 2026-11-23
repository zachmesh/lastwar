---
title: Research speed multiplier M - bounds from the queue timers - 2026-11-23 13:07Z
created: 2026-11-23T05:07:00-08:00
modified: 2026-11-23T05:14:00-08:00
level: L3
version: 0.1.0
description: A first measured bound on the account's research speed from the Coin Output V and Food Output V timers, using Steer B's frame times and the guide sheet's base time
status: done
activity: research-queue
run_id: research-queue-2026-11-23-1307-speed-bounds
trigger: Steer B's frame forensics at 12:44Z and the operator's survey 1257 (queue rows read at 12:56:50Z)
started_at: 2026-11-23T05:05:00-08:00
finished_at: 2026-11-23T05:12:00-08:00
verified: base time 485,100 s from /tmp/oilres/aoo-sheet.csv (the Last War Tutorial sheet, [G] as a guide value, not read on screen); frame times from Steer B (two screenshots under ~/.computer-use/runs, not in the repository); end times from the operator's queue read
---

# Research speed multiplier M: first bounds

## Inputs

- Guide base time of level 1 of both Output V nodes: 485,100 s (5d 14h 45m) [G]; power on completion 3,900 each [G, equals the measured Complete of Unlock Oil Well].
- Frames (Steer B): at 12:09:04Z lab slot 2 was IDLE and Defense Training VIII ran in slot 1; at 12:11:30Z both labs read busy.
- Queue read at about 12:56:50Z: Coin Output V 1d 02:02:20 left (ends about 2026-11-24T14:59:10Z); Food Output V 1d 04:33:08 left (ends about 17:29:58Z).

## Result [D]

| Node | Effective total | M = base / effective | Natural time of the 879 base days |
|---|---|---|---|
| Coin Output V L1 (slot 2) | 26h47m40s to 26h50m06s | 5.02 to 5.03 | about 175 days |
| Food Output V L1 (slot 1) | 28h33m to 29h18m | 4.60 to 4.72 | about 186 to 191 days |

The two differ by about 0.3 to 0.4: a bonus that applies only at the start (Steer A's analysts: Secretary of Science, VIP) is the likely cause; the plain multiplier is about 4.6 to 4.7.

## Assumptions and unknowns

- The other device used no speed-up item on either node (unknown; the speed-up stock read will show it).
- The guide base time is right for this account (a panel read of an idle node would confirm: a lab idles at 2026-11-24T14:59Z).
- Coin fell about 4.6M at the Coin node's start against a guide cost of 6.2M: the account may carry a research cost reduction (unverified).
