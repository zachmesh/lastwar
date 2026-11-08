---
title: Zombie invasion queue run
created: 2026-10-31T03:48:00Z
modified: 2026-10-31T03:48:00Z
version: 1.0.0
description: Queue unit zombie-invasion-zombie-2026-10-28-066 execution
status: done
---

# Zombie invasion - 2026-10-30 about 20:43 to 20:48 PDT queue run

Unit: zombie-invasion-zombie-2026-10-28-066, executor
ticker-2034, chain zombie-2026-10-28 seq 66, computer
session cc-577. Status done - not as a kill unit, but
as the chain-closing check: the Zombie Invasion event
has ended, so no kill, loot claim or Store step was
possible, and NO successor unit is enqueued. The chain
ends here, by the design rule that a chain ends only
when its activity ends.

## Entry state

- The game was left on the VIP screen by the vip unit
  in the same pass. Back arrow at 156,945 returned to
  MY PROFILE; the profile X at 854,48 returned to the
  base view. HUD at base entry: coin 171.0M, Total
  Power 146,857,078.
- No "active on a different device" dialog appeared.

## Evidence the event has ended

- Events icon at 932,133 opened the Events hub on the
  Desert Storm Battlefield page.
- The tab bar was dragged to both ends: leftmost tab
  is Arms Race, rightmost tab is Community; the full
  list seen is Arms Race, Desert Storm Battlefield,
  Winter Battlefield, Level Swap, Wanted Boss,
  Community - six tabs, no Zombie Invasion tab.
- Timer arithmetic from the two previous units agrees:
  unit 064 at 13:46 read the event timer at 05:08
  left (ends about 18:54), unit 065 at 17:42 read
  01:16 left (ends about 18:58). The event therefore
  ended at about the 19:00 reset on 2026-10-30, and
  the tab's removal from the hub confirms it.
- No Search was attempted: with no event page there
  is no Search button, no target and no LOOT to claim.
  The gift-box badge on the world map was not read
  as a zombie signal, since the event page is gone.

## Result

- zombies_killed: 0. coins_collected: 0. squads_parallel: 0.
- coin_before and coin_after: 171.0M (HUD, unchanged;
  no zombie coin moved in this unit).
- No medals measured (no Store page exists without the
  event), no Coin Chest redeemed or opened, no stamina
  spent or opened.
- Successor: NONE enqueued, deliberately. The ticker's
  zombie seeding step must not start a fresh chain
  while the event is absent; the activity metadata
  records this close (version 1.22.0).
- No diamonds or money spent, no price tag tapped, no
  player or boss attacked, no assembly or teleport.
- The game was left on the Desert Storm Battlefield
  Events page.
