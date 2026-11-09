---
title: Zombie Invasion queue unit 049
created: 2026-10-30T00:54:00Z
modified: 2026-10-30T00:54:00Z
version: 1.0.0
description: Queue unit zombie-invasion-zombie-2026-10-28-049 execution
status: done
---

# Zombie Invasion - 2026-10-29 17:54 PDT queue run

Unit: zombie-invasion-zombie-2026-10-28-049, executor ticker-1739.
Chain zombie-2026-10-28, successor to unit 048.

## What was done

- Events page verified by title before Search: Zombie Invasion,
  1d 01:17:52 left at first read, next wave in about 00:39:18.
  The tab bar shifts between openings, as unit 048 warned.
- Coordinate corrections, recorded for the next unit: the Search
  button's grounded point is 358,941, not 358,901 (a tap at
  901 hit the countdown text above the button and did
  nothing); the target card's crossed-swords button is at
  499,753, not 467,836 (a tap at 836 closed the card, the
  same failure unit 008 recorded); the deploy panel's March
  button is at 500,759.
- Kill 1 - Squad 1, 25.05M vs 670.00K, Easy Win, Unit Count
  2,231/2,231, stamina 79 at the panel (80 after regeneration
  at the March read). Dispatched by a batched sequence
  (Events, Search, crossed-swords, no screenshot read in
  between), then March at the grounded point. The march
  timer read 00:00:08, a very short round trip.
- Kill 2 - Squad 2, target X:985 Y:963, dispatched by a
  second batched sequence (Events, Search, crossed-swords,
  squad-2 tab 397,920, March 500,759) immediately after
  Squad 1's March. Stamina 80 to 60 across the two marches
  proves both marches were charged, 10 each.
- squads_parallel is 1, sequential, not a march cap of 4:
  when the second batch landed, March Queues read 1/4 with
  only Squad 2 outbound, and the gift badge already read 1
  for Squad 1's row, so Squad 1 had fully returned during
  the navigation for Squad 2. This is the same short-round-
  trip limit unit 043 recorded: with 8-second-class marches,
  the first squad returns before the second dispatch lands.
- Loot - after both squads returned (March Queues 0/4),
  the gift badge read 2. The LOOT panel held exactly two
  rows, both Lv.10 Invading Zombies, each coin 268.0K,
  medal x10, iron 268.0K, food 268.0K, EXP 263.0K:
  X:985 Y:963 (Squad 2) and X:982 Y:952 (Squad 1).
  Claim All (plain blue, no price tag) claimed both
  in-unit. The badge cleared, and the coin HUD moved
  109.0M to 109.5M, iron 240.3M to 240.9M, food 424.8M
  to 425.4M, all consistent with 536,000 coins and
  536,000 each of iron and food from the two rows.
- Unit 048 missing row re-check: unit 048's Squad 2 row
  (X:980 Y:844) did NOT appear in this unit's panel.
  The two rows claimed here are this unit's own two
  marches, so the 048 row is confirmed lost, not deferred.
- Session note: the computer-use session cc-347 dropped
  mid-unit (an observe call returned observation_unavailable
  with no session open); session cc-351 was started and
  LastWar re-selected, with no game state lost - both
  squads were home and the badge read 2 on re-entry.
- Stamina - never binding this unit (79/80 to 60 across
  two marches). No stamina item was opened and no backpack
  stamina inventory count was needed, since no refill
  source was exhausted.
- Store - NOT visited this unit. The unit cap was reached
  as the loot was claimed, so the medal balance was not
  re-measured live, and no derived medal total is reported
  here (only plus 20 medals by row evidence). The SSR row
  re-check and the Buy-step retry from unit 047 stay
  deferred to the next unit.

## Result statistics

- zombies_killed: 2
- loot_rows_claimed: 2
- loot_rows_missing: 0 in this unit (unit 048's missing row
  confirmed lost, counted in unit 048, not here)
- cleared: false (wave live, Search found targets on
  demand, event page read 1d 01:17 left)
- coin_before: 109.0M HUD rounded
- coin_after: 109.5M HUD rounded
- coins_collected: 536000
- medals_earned: 20 (from the claimed rows; Store balance
  not re-measured this unit, so no medals_before or
  medals_after total is stated)
- chests_opened: 0
- chests_redeemed: 0
- squads_parallel: 1 (sequential - short round trips, not
  a march cap of 4)
- tasks_badge: 2
- stamina_start: 79
- stamina_end: 60

## Red lines

No diamonds or money spent, no price tag or paid button
tapped, no speedup burned, no assembly, no teleport, no
player attacked.
