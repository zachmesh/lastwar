---
title: Zombie invasion queue run
created: 2026-10-30T11:45:00Z
modified: 2026-10-30T11:45:00Z
version: 1.0.0
description: Queue unit zombie-invasion-zombie-2026-10-28-057 execution
status: partial
---

# Zombie invasion - 2026-10-30 about 04:34 to 04:45 PDT queue run

Unit: zombie-invasion-zombie-2026-10-28-057, executor
ticker-0434, chain zombie-2026-10-28 seq 57, computer
sessions cc-445 then cc-446 after a mid-unit session
drop. Status partial: the kills and the in-unit loot
claim are complete, but the Store redemption step was
not executed, so the work continues in successor unit
058. Correction to the unit summary wording: the unit
ran about 11 minutes (claimed 11:34 UTC, completed
11:45 UTC), inside the 15 minute cap; partial here
means the Store step is unexecuted, not that the cap
ran out. No tracker change is made for a partial unit.

## Entry state and focus blocks

- The game was found with the Zombie Invasion Store
  panel still open from unit 056. Store header read
  live at 3530 medals, exactly unit 056's close.
- The first open_app launch returned outcome_unknown;
  observation showed the game already open, so the
  launch was not repeated.
- Two keyboard_focus_unavailable blocks ("user is
  working in another window of this app", frontmost
  app Macky) were cleared by activating LastWar and
  retrying; no input was lost to them.
- The game is in native fullscreen (1920x1080,
  screenshots downsampled to 1280x720), as unit 056
  left it. All coordinates below are normalized
  0 to 1000 in the fullscreen window.

## Two mis-aimed navigations, both corrected

- Search point corrected: two taps at 358,941 hit the
  back arrow, not Search (the back arrow grounds at
  349,950; the real Search button is at 441,940 by
  OCR). Both taps jumped to the map with no target
  card. The "The event has ended" toast seen on the
  map both times belongs to a Lv.10 Marshal's Guard
  notification, not to Zombie Invasion.
- Events icon corrected: a tap at 645,153 opened the
  Halloween Check-In page instead of Events (the
  Events icon grounds at 683,150). All check-in days
  there were already ticked, nothing was claimed,
  and the grounded back arrow at 349,950 returned
  to the map.
- Lesson for the successor: use the grounded points
  (Search 441,940, Events 683,150, back 349,950) and
  verify the page title before the Search tap; never
  re-tap an estimated bottom-bar point.

## Two Lv.10 kills, sequential, loot claimed in-unit

- Coin HUD 134.6M at entry, stamina 39 to 40 by
  regeneration before dispatch.
- First kill - Search found a Lv.10 Invading Zombies
  card (Guaranteed medal x10, EXP 263.0K, iron
  268.0K, food 268.0K, Suggested Power 670,000,
  stamina cost 10). Crossed swords at 499,753
  opened the deploy panel (Easy Win); March at
  500,759 dispatched at once. Verified: March
  Queues 1/4, target X:960 Y:950, 00:00:24 timer,
  stamina 40 to 30.
- Parallel attempt - Events was reopened at once and
  Search found a second Lv.10 card, but squad 1 had
  already returned home by the second dispatch, so
  the queue again read 1/4. Second kill: target
  X:910 Y:965, 00:00:50 timer, stamina 30 to 20.
  squads_parallel is 1 for the same reason as units
  043 and 049: round trips of tens of seconds, not
  the march cap of 4.
- Session drop - session cc-445 closed during the
  wait for squad 2 (observation_unavailable);
  session cc-446 was started, LastWar re-selected,
  and no game state was lost. Squad 2 was Returning
  with 00:00:28 left on recovery.
- LOOT - the gift box grounded at 424,251 on that
  map view opened the LOOT panel with 2 rows:
  X:910 Y:965 and X:960 Y:950, each 268.0K coin
  and medal plus 10. The plain blue Claim All at
  499,765 (no price tag) claimed both rows for
  536,000 coins in-unit. Coin HUD 134.6M to 135.2M
  (HUD-rounded readings, not exact panel values).
  Tasks badge 2 at tap time, matching the 2 rows.
- Stamina closed at 20 with no stamina item opened;
  stamina never bound this unit (kills cost 20
  total). Inventory stamina counts were not
  re-checked because no refill was needed.

## Store step not executed, redemption deferred

- A tap at 645,271 opened Ranking instead of Store
  (Ranking grounds lower than estimated); it was
  closed untouched, nothing spent.
- The Store button grounded twice at 618,222 and
  625,220 produced no change on either attempt; the
  control channel guidance states background clicks
  do not reach some controls and advises against
  repeating the point. No Redeem was tapped, so no
  medals were spent and no chest was redeemed.
- Medal balance after the kills was NOT re-measured
  live in the Store, so no medals_after is reported;
  3530 plus 20 is a derived figure and is not
  claimed as a balance, per the chain rule that only
  Store-measured counts are real. The SSR Coin
  Chest row stood at Limit 95 at unit entry.
- The successor unit must try a different input
  route for the Store button (for example a labelled
  control if one appears) and must re-verify the
  medal balance and the SSR row Limit before
  assuming any exchange happened. Chests opened 0;
  the owned Coin Chests inventory location is
  still unknown.

## Close

- Cleared is false: Search found a Lv.10 target on
  both attempts, and the event page read next wave
  in 00:57:05 near the end of the unit, so zombies
  remain nearby. Successor unit
  zombie-invasion-zombie-2026-10-28-058 was
  enqueued in the same chain to start now.
- No diamonds or money spent, no price tag tapped,
  no red line crossed. The game was left on the
  Zombie Invasion event page.
