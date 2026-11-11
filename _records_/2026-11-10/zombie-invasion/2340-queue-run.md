---
title: Zombie invasion queue run 2340
created: 2026-11-10T23:40:00-08:00
modified: 2026-11-10T23:40:00-08:00
version: 1.0.0
description: Zombie invasion unit zombie-invasion-zombie-2026-11-10-003, Glacieradon wave, server maintenance blocked the first half of the unit, 1 Lv.10 kill and its LOOT row claimed for 268,000 coins
status: partial
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-10 23:40-23:53 PST
---

# Zombie invasion queue run 2340

- Unit: zombie-invasion-zombie-2026-11-10-003, executor ticker-2334,
  chain zombie-2026-11-10 seq 3, sessions cc-521 and cc-524.
- Window: 23:40-23:53 PST. Status partial - the wave is still live
  and the chain continues. Successor enqueued to start now.

## Server maintenance ate the first half of the unit

- At entry LastWar showed "Server disconnected. Please restart the
  game." with a Confirm button. A click_element on Confirm produced
  no change; a coordinate tap at 501,545 then exited the app (the
  restart itself, not a crash - the same pattern as the update
  restart below).
- Relaunch showed a SYSTEM ANNOUNCEMENT: "Update complete, please
  restart the game." with Confirm at 502,568. A click_element
  produced no change; a coordinate tap at 502,568 dismissed the
  dialog and the game restarted.
- After the restart a second dialog: "The server is under
  maintenance. Please wait a moment, we'll be back with you
  shortly." with Cancel / Confirm, plus "Login failed. Please retry
  or contact Support" at the bottom. One Confirm tap at 634,568
  retried the login; the game then loaded to the base screen.
  This matches the 2319 donations record, which saw a server banner
  warning of a maintenance shutdown in 7 minutes at its entry -
  the maintenance was announced and the game came back on its own.
- No "active on a different device" dialog appeared at any point.
  Computer session cc-521 dropped once mid-unit (wait returned no
  active session); session cc-524 was started and the game state
  was intact on recovery. No game input was replayed.

## Entry state (base screen, read live about 23:47)

- HUD: food 655.4M, iron 978.5M, coin 109.9M (HUD-rounded), gold
  13.22K, stamina 127. Total Power 149,218,973.

## The event page

- Events icon at 927,131 opened the Events hub. The tab bar read
  The Age of Oil (red 1 badge), Arms Race, Desert Battlefield and
  a partially visible "Zon..." tab at the right edge; tapping it
  at 860,131 opened the Zombie Invasion - Glacieradon page.
- Page read live: event timer 2d 18:12:18 remaining, "Zombies are
  invading! Protect our City! Challenge the fearsome Beast
  Glacieradon!", Store / Ranking / Rewards buttons, Alliance
  Finding / My Findings tabs, boss clue counter 40/40 with
  "Challenge begins in: 1d 18:12:15. Your Timezone: 2026-11-12
  18:00". Alliance Finding lists Lv.80 and Lv.85 Zombie Bosses
  at 546km, 487km, 486km, 506km. "The next wave of Invading
  Zombies will arrive in 00:06:50" at the read (about 23:57).

## The kill

- Search at 379,936 found a Lv.10 Invading Zombies target:
  Guaranteed Reward medal x10, drone data 1.3K, hero EXP 263.0K,
  iron 268.0K, food 268.0K; Potential Reward green crate x1,
  green box x4, gold ticket x1; Suggested Power 670,000; stamina
  cost 10; despawn 11:04:34.
- Crossed-swords at 496,736 opened the deploy panel: Squad 1,
  Unit Count 2,231/2,231, Easy Win, march 00:01:38.
- March at 500,755 dispatched at once. Stamina 127 to 117, March
  Queues 1/4, squad Returning 00:00:57 on the next read and home
  by the LOOT claim.
- squads_parallel 1: only one dispatch was attempted in this unit.
  The maintenance recovery consumed the first half of the unit
  window, leaving no time for a parallel second dispatch - the
  binding limit was the remaining unit time, not the march cap
  of 4. The successor should run parallel dispatches while the
  wave lasts.

## LOOT claim

- Gift badge read 1 at the right end of the March Queues bar
  after the squad's return; the gift box re-grounded fresh on
  the current screenshot at 308,237 opened the LOOT panel.
- One row, read before claiming: Lv.10 Invading Zombies X:471
  Y:355, medal x10, green box x4, iron 268.0K, food 268.0K,
  coin 268.0K, hero EXP 263.0K.
- Claim All (plain blue, no price tag) at 499,765 tapped once;
  panel closed. Coin HUD 109.9M to 110.2M, food 655.4M to
  655.7M, iron 978.5M to 978.7M - each displayed move consistent
  with the single 268,000 row (HUD rounds to 0.1M). Gift badge
  gone after the claim. March Queues 0/4.
- Stamina 117 at close, no refill needed. Store not visited in
  this unit (unit time): the medal balance was not re-read live
  and no Coin Chest redemption was attempted. The Store
  coin-chest identification from unit 001's follow-up stays open
  for the successor.

## Result

- zombies_killed 1 (verified: Victory implied by Returning
  march, stamina 127 to 117, March Queues 1/4 to 0/4, LOOT row
  X:471 Y:355 claimed).
- cleared false: the wave is live, next wave arrives about
  23:57, more targets may appear.
- coin_before 109.9M HUD, coin_after 110.2M HUD,
  coins_collected 268,000 (row read before Claim All).
- medals_before not re-read, medals_after not re-read.
- chests_opened 0. squads_parallel 1 (see above).
- Target: kill wave zombies and claim LOOT; achieved: 1 Lv.10
  kill and its LOOT row claimed. Verified yes (same-unit live
  reads: row coin line, HUD deltas, stamina, queue state).
  Blocker category h (by-design partial - chain continuation).
- Follow-up: successor enqueued to start now (chain rule,
  cleared false). It should run parallel dispatches with
  freshly grounded map taps, visit the Store to identify this
  event's Coin Chest rows by tooltip and re-read the medal
  balance, and check the next wave's targets after 23:57.
