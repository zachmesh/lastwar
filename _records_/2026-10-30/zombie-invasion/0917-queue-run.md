---
title: Zombie invasion queue run
created: 2026-10-30T16:17:00Z
modified: 2026-10-30T16:17:00Z
version: 1.0.0
description: Queue unit zombie-invasion-zombie-2026-10-28-062 execution
status: partial
---

# Zombie invasion - 2026-10-30 about 09:05 to 09:17 PDT queue run

Unit: zombie-invasion-zombie-2026-10-28-062, executor
ticker-0904, chain zombie-2026-10-28 seq 62, computer
sessions cc-469 and cc-470 (cc-469 dropped during a
visual-grounding call that timed out, cc-470 recovered
with the target card still open and no state lost, as
in earlier units).
Status partial: two kills, the in-unit loot claim and
one SSR Coin Chest redemption are complete, but the
chain is not exhausted, so the work continues in
successor unit 063. No tracker change is made for a
partial unit.

## Entry state

- Base screen at entry: coin HUD 143.6M, stamina 58.
  Event page: Zombie Invasion timer 09:53:36 left,
  next wave in 00:35:07, so the current wave was
  still open. No "active on a different device"
  dialog appeared.
- Grounded windowed points reused or corrected in
  this unit: Events icon 935,138; Search 441,940;
  crossed-swords 499,753; March 500,759; gift box
  311,252 on this map view; Claim All 499,765;
  Store button 818,195; SSR Redeem 740,415 at this
  scroll position; Buy centre 499,689.

## Two Lv.10 kills, sequential, loot claimed in-unit

- Kill 1: Lv.10 Invading Zombies, X:979 Y:961,
  Squad 1 (Easy Win, 13 second march, Unit Count
  2,231), stamina 58 to 49, March Queues 1 of 4
  verified on screenshot with 00:00:04 outbound
  left.
- Kill 2 (parallel attempt): batched Search with a
  2 second pause, crossed-swords, then March
  dispatched a second Lv.10 target, X:977 Y:955,
  stamina 49 to 39, March Queues 1 of 4 with
  00:00:09 outbound. Squad 1 was already home
  when the second deploy panel opened (short
  round trip, as in units 043, 049, 058, 059 and
  061), so squads_parallel is 1, not the march
  cap of 4.
- After a 40 second wait both squads were home
  (March Queues bar gone, stamina 40 with
  regeneration). Gift box at 311,252 opened LOOT
  at once. The panel held exactly the two rows:
  X:977 Y:955 and X:979 Y:961, each coin 268.0K,
  iron 268.0K, food 268.0K, medal 10, EXP 263.0K.
- Both rows claimed in-unit via the plain blue
  Claim All at 499,765 (no price tag). Total
  coins_collected 536,000. Coin HUD moved 143.6M
  to 144.1M, consistent with 536,000 plus HUD
  rounding. No stamina item opened; stamina
  never bound this unit.
- squads_parallel 1, for the short-round-trip
  reason above. Stamina 58 to 40 net (20 spent
  on marches, 2 regained).

## Store redemption breakthrough

- Store button correction: taps at 609,221 to
  625,220 that units 057 and 058 recorded as
  unresponsive are not the Store button on this
  layout. The Store button on the Zombie
  Invasion event page is at 818,195 (cart icon,
  top right of the event panel); a single tap
  there opened the Store at once. The next unit
  should use 818,195, not the 609 to 625 points.
- Store header read live at 4050 medals after
  the kills and loot claim. The medal balance
  before the kills was not measured live in this
  unit, so no derived before total is reported;
  the rows evidence plus 20 medals earned.
- The 160-medal Coin Chest (SSR) row was found
  after scrolling (Limit 94, as unit 060's
  tooltip check left it). Its Redeem at 740,415
  opened the BUY ITEMS dialog naming Coin Chest
  (SSR), Unit Price 160, Total Price 160; a
  single tap on Buy at the grounded centre
  499,689 succeeded with a CONGRATULATIONS
  banner.
- Verified live after the redemption: balance
  4050 to 3890, SSR row Limit 94 to 93. One SSR
  Coin Chest redeemed, 812.16K coins of pending
  value by the tooltip yield.
- No Coin Chest was opened in this unit; the
  owned chests' inventory location is still
  unknown, and that item stays open for the
  successor.

## Close

- Cleared is false: both Searches found a target
  at once, the next wave was still 00:24:55 away
  at Store close, and the event timer read
  09:42:58. Successor unit 063 is enqueued to
  start now in the same chain, for the next tick.
- No diamonds or money spent, no price tag tapped
  except the free Claim All, no speedup burned, no
  assembly or teleport.
