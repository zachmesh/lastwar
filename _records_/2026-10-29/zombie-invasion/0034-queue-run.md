---
title: Zombie Invasion Execution 2026-10-29 0034 Queue Run
created: 2026-10-29T07:46:00Z
modified: 2026-10-29T07:46:00Z
level: L0
version: 1.0.0
description: Zombie-invasion chain unit 031 - partial, two Lv.10 kills claimed in-unit for 536,000 coins, one 10-stamina item opened to fund the second kill, squads did not overlap so squads_parallel is 1, chain continues, successor starts now
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-29
  - source: owner task unit queue design of 2026-10-28
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization, the task unit queue ticker with its 15 minute unit cap and Zombie Invasion continuation chains
  - source: owner instruction of 2026-10-28 - collect the event coins from the task collection icon and maximize coin, dispatch squads in parallel
  - source: owner reminder of 2026-10-28 - open the stamina resource items held in the inventory and use them
  - source: owner decision of 2026-10-28 - redeem event medals for Coin Chests in the event Store and open owned Coin Chests
---

# Zombie Invasion — execution, 2026-10-29 0034 queue unit 031

A single task unit, executed by executor ticker-0034 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-031,
chain zombie-2026-10-28, chain sequence 31, priority 4.
Session window about 00:34 to 00:46 America/Los_Angeles.
Status — partial; the chain continues while the event is
available and a fresh wave is running, so the tracker is
left untouched. Both squads dispatched in this unit were
resolved and claimed inside it.

## What was observed

- Open — a deploy panel was already open on the world map
  (left over, source unknown): Squad 25.05M Vs 670.00K,
  Easy Win, March 00:00:52, stamina cost 10, stamina 18.
  The March tap at the grounded point 499,750 answered
  with the toast "The target location has changed. Please
  try again." and charged no stamina, the same failure
  unit 006 and unit 030 recorded: a stale panel's target
  has moved. No different-device dialog appeared.
- Events page — opened from the world map via 942,152,
  landing directly on the Zombie Invasion tab. At the open
  the page read 1 day 18:24:09 left, next wave in 00:05:28,
  so a new wave was due at about 00:42.
- Kill 1, Squad 1 — Search at the grounded centre 375,943
  found a Lv.10 Invading Zombies card (Suggested Power
  670,000, Guaranteed Reward medal x10, hero EXP 263.0K,
  iron 268.0K, food 268.0K). Crossed swords at 500,753,
  March at 499,750: March Queues 1 of 4, Go X:885 Y:994,
  stamina 18 to 8.
- Stamina inventory, CHECKED before concluding anything
  about refill — Inventory Special tab, found by dragging
  the grid up (a scroll gesture did not move it): a
  lightning-bolt item labelled 50 with count 614, and a
  lightning-bolt item labelled 10 with count 612. The
  Resources red-gem "10 Diamonds" items are NOT stamina
  and were not touched. Two taps at the wrong grid point
  (y 700, below the row) changed nothing; visual grounding
  placed the 10 item at 407,570, and that tap selected it
  ("10 Stamina - Use this item to gain Stamina").
- Stamina refill — one 10 Stamina item opened (Use tap at
  511,953, toast "Commander, you've acquired 10 Stamina",
  count 612 to 611). Base HUD stamina then read 19 (8 plus
  10 plus about 1 regenerated). No diamond spent, no
  speedup burned. The 50-stamina x614 stock was untouched.
- Kill 2, Squad 2 — a batched sequence (Events, Search,
  crossed swords, March) dispatched the second squad to
  X:874 Y:976: March Queues 1 of 4 at the read, stamina
  19 to 9. Squad 1 had already returned by this dispatch,
  so the two squads did NOT overlap: squads_parallel is
  1, verified by the 1 of 4 readings, not 2. The refill
  hunt consumed the overlap window; see the follow-up.
- Returns and LOOT claims — Squad 1's row was claimed
  first (gift box at the right end of the March Queues
  bar, grounded tap 318,242; LOOT panel held Lv.10 X:885
  Y:994; plain blue Claim All at 499,765). HUD after that
  claim: coin 77.7M (from 77.5M), food 201.4M (from
  201.1M), iron 387.8M (from 387.5M). The computer session
  dropped once during the Squad 2 wait (cc-203 ended,
  cc-204 opened); each reopening found the Last War
  window 78525 with state intact. Squad 2 returned at
  about 00:44 (March Queues 0 of 4, gift badge 1); its row
  (Lv.10 X:874 Y:976) was claimed the same way. HUD after
  the second claim: coin 78.0M, food 201.6M, iron 388.1M
  — each up about 268,000 at HUD rounding, confirming the
  claim. Exact coin panel readings were not available
  this unit: the HUD rounds to 0.1M, so no exact
  coin_before or coin_after is asserted here;
  coins_collected 536,000 is exact from the two LOOT
  rows at 268,000 each.
- Stamina and medals — stamina 10 at the close (9 after
  kill 2 plus about 1 regenerated), not exhausted.
  Medals were not re-read in the Store this unit:
  medals_before 900 carried from unit 030's derived
  balance (no other zombie unit ran between 030 and 031),
  medals_after 920 derived (900 plus 20 from the two
  claimed rows).
- Coin chests, NOT redeemed or opened in this unit — the
  unit window was spent on the stale panel, the two
  dispatches, the stamina refill and the two claims, so
  no Store visit was made. The 4 owned Coin Chest (SSR)
  are still unlocated in inventory (unit 014 finding,
  still open), 3,248,640 coins pending, plus a new
  redemption the successor can make from the 920 derived
  balance under the maximize-coin decision.
- Totals — zombies_killed 2 claimed in-unit (X:885 Y:994
  and X:874 Y:976), coins_collected 536,000,
  coin_before HUD 77.5M, coin_after HUD 78.0M,
  medals_before 900 carried, medals_after 920 derived,
  chests_opened 0, squads_parallel 1 verified,
  tasks_badge 2, cleared false (Search found targets at
  once twice, and the new wave arrived at about 00:42
  during this unit; the successor starts now).
  Nothing bought with diamonds or money, no speedup item
  burned, no rally started, no ally panel action taken.

## Follow-up for the successor

- Stamina is 10 at the close: with the fresh wave running,
  open a stamina item BEFORE the first dispatch when the
  balance is below 20, so the second squad can be
  dispatched while the first is still out and the two
  squads genuinely overlap. Stamina is NOT exhausted:
  50-stamina x614 and 10-stamina x611 remain in the
  Inventory Special tab (grid row grounded at 407,570
  for the 10 item; a scroll gesture does not move this
  grid, drag it up instead).
- Read medals_before from the Store header (920 derived
  expected before any new kill rows), never from the old
  derived chain alone. With that balance, redeeming Coin
  Chest (SSR) for 160 medals remains authorized under the
  maximize-coin decision, and the 4 owned chests still
  need locating in inventory and opening (3,248,640
  coins pending).
- A deploy panel left open at unit start may be stale: a
  "target location has changed" toast means no stamina
  was charged; re-Search at once. Check the deploy
  panel's Vs line before March, and never march an
  "Unlikely to Win" rally target.
- Claim LOOT rows in the same unit that dispatched them,
  from the kill-area map position via the grounded
  318,242 gift-box tap, before any BASE or WORLD tap
  that recentres the map.
