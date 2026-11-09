---
title: Events queue run 0359
created: 2026-11-02T11:59:00Z
modified: 2026-11-02T11:59:00Z
version: 1.0.0
description: Events unit events-2026-11-02-0257 executed by ticker-0334, partial
status: partial
grounded_in:
  - source: game screens observed on the owner Mac mini during this unit
---

# Events queue run 0359

Unit: events-2026-11-02-0257. Executor: ticker-0334.
Session window: about 03:52 to 03:59 America/Los_Angeles.
Status: partial. The hub sweep was cut short by an app crash
(see below) at the pass budget end; the tracker is untouched
and the next tick re-produces this regular.

## What was done

- Events hub opened from the base right rail. It landed on the
  current Arms Race phase page, Hero Advancement, Contest
  Segment Lv.29-30, read live: account score 40,500, rank
  #2110 [AP3x]Bears Lair, phase countdown 02:08:44 falling.
  Point chest thresholds 2,000, 4,000 and 12,000 are all
  passed at this score. The top-left cumulative chest reads
  6/2.
- The 2,000 point chest was tapped: it opened only a reward
  preview popup ("Valued: 2,360" - Skill Medal 200, Arms Race
  Badge 1, Coin Chest (SR) 4, Food Chest (SR) 4, Iron Chest
  (SR) 4, 5m Speed-up 8) with no Claim button visible. A
  preview-only tap is consistent with that chest already
  having been claimed by an earlier arms-race unit, but the
  claimed state was not verified before the crash below, so
  no chest state is asserted here. The 4,000 and 12,000
  chests and the cumulative chest were not tapped.
- No grinding was done; Arms Race point work belongs to the
  arms-race unit. No paid button was tapped: no Legendary
  Take All, no Battle Pass unlock, no Level Swap.

## App crash, self-inflicted, recovered

- To close the chest preview popup, an Escape key was sent.
  LastWar quit immediately after the key reached it. This is
  the known rule recorded in the workspace notes - never use
  Esc (or Ctrl-Cmd-F) on this app, it crashes it. The Escape
  key must not be used on LastWar again.
- Recovery: the app was relaunched and came back directly to
  the base screen (power 149,196,915, no login demand, no
  "active on a different device" dialog). Nothing was lost
  beyond this unit's unfinished sweep.

## Not done in this unit

- The 4,000 and 12,000 point chests, the cumulative chest,
  and the remaining hub tabs (Desert Battlefield, Wanted
  Boss, Community and further right tabs) were not swept.
  The next tick's events unit resumes the sweep; the
  arms-race unit owns any unclaimed Arms Race chest.
