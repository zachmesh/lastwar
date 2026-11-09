---
title: Zombie Invasion Execution 2026-10-29 0518 Queue Run
created: 2026-10-29T12:18:00Z
modified: 2026-10-29T12:18:00Z
level: L0
version: 1.0.0
description: Zombie-invasion chain unit 042 - partial, three Lv.10 kills claimed in-unit for 804,000 coins, squads_parallel 2 verified, Store medal balance read live at 2900 conflicting with unit 041 derived 1220, Coin Chest redemption deferred after Store Redeem taps did not respond
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-29
  - source: owner task unit queue design of 2026-10-28
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization, the task unit queue ticker with its 15 minute unit cap and Zombie Invasion continuation chains
  - source: owner instruction of 2026-10-28 - collect the event coins from the task collection icon and maximize coin, dispatch squads in parallel
  - source: owner reminder of 2026-10-28 - open the stamina resource items held in the inventory and use them
  - source: owner decision of 2026-10-28 - redeem event medals for Coin Chests in the event Store and open owned Coin Chests
---

# Zombie Invasion — execution, 2026-10-29 0518 queue unit 042

A single task unit, executed by executor ticker-0504 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-042,
chain zombie-2026-10-28, chain sequence 42, priority 4.
Session window about 05:04 to 05:18 America/Los_Angeles.
Status — partial; the chain continues while the event is
available and zombies remain nearby, so the tracker is
left untouched. All three kills dispatched in this unit
were resolved and claimed inside it, and the march queue
was empty at the close. The Coin Chest redemption is
deferred, not done — see below.

## What was observed

- Open — the game was on the base screen, coin HUD
  99.0M, Total Power 149,351,992, stamina 47 read on
  the first deploy panel. Event page read: Zombie
  Invasion live with 1 day 13:54:33 left, next wave
  in 00:35:53. No different-device dialog appeared.
  Computer session cc-234 dropped mid-unit and was
  replaced by cc-236 without loss, the same timeout
  pattern units 040 and 041 recovered from.
- Kill 1, Squad 1 — Search found a Lv.10 card
  (Suggested Power 670,000, stamina cost 10, medal
  x10, EXP 263.0K, iron 268.0K, food 268.0K). The
  crossed-swords tap at the screenshot-pixel estimate
  498,673 twice failed to open the deploy panel; the
  grounded point 498,758 opened it at once (Squad 1,
  25.05M Vs 670.00K, Easy Win, Unit Count 2,231 of
  2,231). March at the grounded 499,755.
- Failed blind batch, lesson — the second dispatch
  was batched as Search, crossed-swords at 498,758,
  March at 499,755 without a screenshot read. It
  landed on a secret-task tile instead of a zombie:
  the new Search card sat higher, so 498,758 hit the
  tile below the card. The card was closed by tapping
  empty map ground. Rule restated: the target card
  position varies between Searches (crossed-swords
  grounded at 758, then 625, then 733 in this unit),
  so ground the button on each fresh card and never
  batch across a new Search.
- Kill 2, Squad 1 — careful re-dispatch: Events
  re-verified on the Zombie Invasion tab by OCR,
  Search found a Lv.10 card, crossed-swords grounded
  at 500,625, deploy read Squad 1, 25.05M, Easy Win,
  stamina 38, march time 00:00:58. March at the
  grounded 500,757.
- Kill 3, Squad 2, parallel — while Squad 1 was in
  flight, Events re-verified, Search found a Lv.10
  card, crossed-swords grounded at 498,733, and the
  deploy panel had auto-selected Squad 2 (Unit Count
  2,175 of 2,175, Easy Win, stamina 29, march time
  00:01:07), matching unit 024. March at the
  grounded 500,744. The march queue then read 2 of
  4 — squads_parallel 2 verified in one screenshot.
- Claim 1 — gift box at the grounded 322,221 (the
  earlier tap at 320,208 missed high) opened the
  LOOT panel: one row, Lv.10 at X:978 Y:987, coin
  268.0K. Claim All at the grounded 498,752, blue
  button with no price tag. Coin panel read after:
  99,283,332 owned.
- Claim 2 — after both squads returned, gift badge
  2, gift box at the grounded 317,215 opened LOOT
  with two rows, Lv.10 at X:938 Y:992 and Lv.10 at
  X:949 Y:998, coin 268.0K each. Claim All at the
  grounded 498,770. Coin panel read after:
  99,819,332 owned, reconciling exactly — first
  claim plus 536,000 equals the second read, so the
  Owned figure moves only on claims and spending
  while passive income accrues under Collect
  Resources (992,526 to 1,028,113 over the unit).
- Coin totals — coin_before 99,015,332 derived
  (99,283,332 minus the first row's 268,000, no
  spending in between), coin_after 99,819,332 read,
  coins_collected 804,000 across three rows. The
  coin_before figure is derived, not read at unit
  start, and is labelled so.
- Stamina — 47 minus 10, plus 1 regen, minus 10,
  plus 1 regen, minus 10, ending 19. No refill was
  needed: 19 stamina remains, and no unit conclusion
  about exhausted refills was required. Backpack
  stamina item counts were not re-read this unit.
- Medals, conflict flagged — the event Store header
  read live at 2900 medals after the unit's 3 kills.
  Unit 041 recorded medals carried to 1220 derived.
  The two cannot both be balances: either the
  earlier derivation drifted from a stale base, or
  the header counts something else. This unit
  records medals_before 2870 derived (2900 minus
  this unit's 30) and medals_after 2900 read live,
  and flags the 1220 figure as suspect — the next
  unit should re-read the Store header rather than
  trust either derivation.
- Coin Chest redemption deferred — the Store row
  for the gold coin chest reads 160 medals, Limit
  98, matching the Coin Chest (SSR) of unit 014
  (Limit 100, two redeemed since). Its Redeem tap
  at the grounded 740,550 twice produced no change,
  and the control channel advised against clicking
  there again — background clicks do not reach some
  controls. No medals were spent, balance stays
  2900, and the redemption is left for the successor
  unit to attempt, possibly by another route. The
  owned Coin Chest (SSR) count of 4 from unit 041
  was not re-verified this unit, and no owned chest
  was opened — their backpack location is still
  unknown.
- Cleared — false. The wave was still producing
  targets on demand (three Searches, three Lv.10
  cards), and the next wave was about 25 minutes
  out at the close. Successor unit 043 enqueued to
  start now.

## Result statistics

- zombies_killed: 3
- cleared: false
- coin_before: 99015332 (derived, see above)
- coin_after: 99819332 (read)
- coins_collected: 804000
- medals_before: 2870 (derived, see above)
- medals_after: 2900 (read live in the Store)
- chests_opened: 0
- squads_parallel: 2
- tasks_badge: 2
- stamina_end: 19
