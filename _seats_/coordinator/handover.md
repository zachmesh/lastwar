---
title: Coordinator seat handover
created: 2026-11-22T19:11:00-08:00
modified: 2026-11-26T20:30:00Z
level: L2
version: 0.28.0
description: Stop handover - the game state, the standing rulings, the open owner items and the schedules that existed, for the next harness
status: unverified
grounded_in:
  - source: coordinator ticks _records_/2026-11-22/team-operations/2011-tick.md to 1219-tick.md
  - source: privacy finding _records_/2026-11-22/team-operations/2222-privacy-finding.md
---

# Handover - coordinator (stop at 20:26Z on 2026-11-26)

The owner ordered every goal and schedule in this workspace stopped on DSH (he is moving to another machine and harness). Nine coordinator schedules were deleted; no goal, no running job, no desktop lock, no claimed unit. Nothing is running. Quote `date -u`.

## State of the game (last reads, 18:08Z to 20:04Z)

- Stocks: food 51.1M, iron 647.5M, coin 16.1M, oil 683.3K (gap to 1.2M about 516K), diamonds 10,673; Total Power 152,113,439 at 18:08Z while the first promotion batch (726 troops, Lv.8 to Lv.9) ran; it ended about 20:13Z and its return is uncollected.
- Builds: Oil Well to Lv.27 ends 11-28T08:50Z (30 of 30 helps); grounds end 11-29T15:31Z, 12-03T13:50Z, 12-08T09:25Z. Labs end 11-27T23:20Z and 11-29T12:38Z.
- Barracks tents hold finished batches (Lv.30 67, Lv.24 248, Lv.20 110) waiting for room; the Hospital holds 5,104 completed (tier unread), 1,364 wounded, free room 1,531. The owner's zombie siege runs 01:15Z daily and is never cancelled.
- Trucks 5 of 5 today; plunders 4 of 4. Last harvest collect 16:25Z.

## Standing rulings (details in the sheets and digests)

- Red lines: no real-money or gem spend, no Finish Now, no Arena, rally or PvP, never the Lottery, never a gem-tagged chest, never Claim All on a mail list.
- Floors before any build press: coin 10M, iron 100M, food 30M; price from the table at 0.85 and drag the cost list.
- Helmet bubble (white round) is the help request: press once after a build starts. Promote only, never Finish Now; room is the controlling resource.
- Windows: a macOS consent window is never answered; a Python walking protected folders is found first (the tcc-who tool), then one kill of the window; any other app in front with nobody at the Mac gets the front script once.
- Dialog rule D (a backoff after the different-device dialog) stands until the owner answers.

## Open owner items

The dialog rule A to D; the one Allow click for the cu helper; the Apple Follow Up notice (returned twice); digest lines for the AGENTS file, the upstream roster glob and the leftover test server.

## Schedules that existed (9, names only) and how to restart

Loop tick (15 min), planner ping (4 h), records delivery (2 h), word-budget review (daily), cu quiet window (daily), weekly review, hospital read before the siege, front-log read, evening donations. Recreate with the prompts in the repository history of this file and the sheets named in `_records_/2026-11-22/queue-planning`.
