---
title: Zombie invasion queue run
created: 2026-10-30T15:49:00Z
modified: 2026-10-30T15:49:00Z
version: 1.0.0
description: Queue unit zombie-invasion-zombie-2026-10-28-061 execution
status: partial
---

# Zombie invasion - 2026-10-30 about 08:45 to 08:49 PDT queue run

Unit: zombie-invasion-zombie-2026-10-28-061, executor
ticker-0834, chain zombie-2026-10-28 seq 61, computer
sessions cc-467 (continued from unit 060) and cc-468
(cc-467 dropped during a 20 second wait, cc-468
recovered with no state lost, as in earlier units).
Status partial: two kills and the in-unit loot claim
are complete, but the chain is not exhausted and the
Store step was not attempted in this unit, so the
work continues in successor unit 062. No tracker
change is made for a partial unit.

## Entry state

- The game was left on the Zombie Invasion Events
  page by unit 060. Coin HUD at entry 143.0M.
  No "active on a different device" dialog appeared.
- Fresh wave in progress: unit 060's close showed
  the next-wave countdown at 00:57:18, and both
  Searches in this unit found a target at once.

## Two Lv.10 kills, sequential, loot claimed in-unit

- Dispatch method: single-step with a screen read
  between steps. Grounded windowed points reused
  from unit 060: Events icon 935,160; Search
  376,940; crossed-swords 501,753; March 499,774.
- Kill 1: Lv.10 Invading Zombies, X:989 Y:951
  (read from its LOOT row; the march entry was
  garbled in OCR), Squad 1 (25.05M, Easy Win,
  Unit Count 2,231 of 2,231), stamina 73 to 64
  by the Victory screenshot (one point of
  regeneration in between), March Queues 1 of 4.
  The target was a short round trip: the squad
  was already Returning 00:00:02 at the first
  post-march screenshot, under a Victory banner.
- Kill 2: Lv.10, X:991 Y:959, Squad 1 again
  (already home - the short round trip, not the
  march cap of 4, is why this unit ran
  squads_parallel 1, as in units 043, 049, 058
  and 059), stamina 64 to 54, March Queues 1 of 4,
  timer 00:00:01 at the post-march screenshot.
- After a 20 second wait both squads were home
  (March Queues 0 of 4) and the gift badge read 2.
  Gift box at 296,252 on that map view opened
  LOOT at once. The panel held exactly the two
  rows: X:991 Y:959 and X:989 Y:951, each coin
  268.0K, iron 268.0K, food 268.0K, medal 10,
  EXP 263.0K.
- Both rows claimed in-unit via the plain blue
  Claim All at 499,765 (no price tag). Total
  coins_collected 536,000. Coin HUD moved 143.0M
  to 143.6M, food 286.8M to 287.3M, iron 473.2M
  to 473.7M, each consistent with 2 x 268K plus
  HUD rounding.
- squads_parallel 1, for the short-round-trip
  reason above; the parallel attempt was made
  immediately after kill 1, but squad 1 was
  already home when the second deploy panel
  opened. Stamina 73 to 54, 20 spent, no refill
  needed, no stamina item opened.

## Store step not attempted

- The Store redemption from unit 060 was already
  proven unresponsive in this session (single tap,
  1 second long-press and double-click all left
  balance 4010 and Limit 94 unchanged), and this
  unit's pass budget did not leave room for a
  fresh Store attempt plus a re-verification, so
  the SSR redemption and the Owned-count
  discrepancy from unit 060 stay open for unit
  062: re-measure the medal balance live, retry
  Redeem with a different input route, and
  re-verify balance and Limit before assuming
  any exchange.
- No Coin Chest was opened in this unit; the owned
  chests' inventory location is still unknown.

## Close

- Cleared is false: both Searches found a target
  at once, and the event timer read 10:11:55 at
  close. Successor unit 062 is enqueued to start
  now in the same chain, for the next tick.
- No diamonds or money spent, no price tag tapped,
  no speedup burned, no assembly or teleport.
