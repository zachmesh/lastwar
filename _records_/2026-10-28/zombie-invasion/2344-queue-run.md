---
title: Zombie Invasion Execution 2026-10-28 2344 Queue Run
created: 2026-10-29T06:44:00Z
modified: 2026-10-29T06:53:00Z
level: L0
version: 1.0.0
description: Zombie-invasion chain unit 030 - partial, two Lv.10 kills in parallel claimed for 536,000 coins, one rally-class target passed over, one moved target missed, chain continues, successor starts now
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-28
  - source: owner task unit queue design of 2026-10-28
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization, the task unit queue ticker with its 15 minute unit cap and Zombie Invasion continuation chains
  - source: owner instruction of 2026-10-28 - collect the event coins from the task collection icon and maximize coin, dispatch squads in parallel
  - source: owner reminder of 2026-10-28 - open the stamina resource items held in the inventory and use them
  - source: owner decision of 2026-10-28 - redeem event medals for Coin Chests in the event Store and open owned Coin Chests
---

# Zombie Invasion — execution, 2026-10-28 2344 queue unit 030

A single task unit, executed by executor ticker-2334 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-030,
chain zombie-2026-10-28, chain sequence 30, priority 4.
Session window about 23:44 to 23:53 America/Los_Angeles.
Status — partial; the chain continues while the event is
available and the wave is still running, so the tracker is
left untouched. Both squads dispatched in this unit were
resolved and claimed inside it.

## What was observed

- Open — the game was already on the base interior screen
  (left over from the secrets and treasures units), coin HUD
  76.9M, Total Power 149,351,992, stamina 29 at the deploy
  read (28 on the base HUD, 29 in the deploy panel after
  about 1 regenerated). No different-device dialog appeared.
  The computer session dropped twice during the unit
  (cc-197 ended, cc-200 opened); each reopening found the
  Last War window 78525 with state intact. The game window
  was moved from (79,30) to (800,30) during the secrets
  unit; size unchanged 642 by 951.
- Events page — opened from the base via 942,152, first
  landing on the Community tab; the left-edge tab ending
  in "sion" was tapped at the grounded point 145,128 to
  reach Zombie Invasion. At the open the page read
  1 day 19:13:21 left, next wave in 00:54:40, so the current
  wave was running.
- First Search, rally-class target passed over — a batched
  sequence (Events, Search, attack, March) opened a deploy
  panel reading Squad 25.05M Vs 36.00M, "Unlikely to Win",
  Rally Time options and a Rally button, with a 20 stamina
  cost shown. That is a rally-class target, not a Lv.10
  sweep target, so no march was sent and no rally was
  started; the panel was closed by tapping the map above
  it. No stamina was charged.
- Second Search, Lv.10 card verified — Search at the
  grounded centre 375,943 found a Lv.10 Invading Zombies
  card: Guaranteed Reward medal x10, book 1.3K, hero EXP
  263.0K, iron 268.0K, food 268.0K; Potential Reward crate
  x1, box x4, ticket x1; Suggested Power 670,000; stamina
  cost 10; despawn 11:53:00. The crossed-swords button at
  the grounded point 500,753 opened the deploy panel:
  Squad 1, 25.05M Vs 670.00K, Easy Win, Unit Count
  2,231 of 2,231, stamina 29.
- Moved target missed — the March tap at the grounded
  point 499,750 answered with the toast "The target
  location has changed. Please try again." and charged
  no stamina, the same failure unit 006 recorded: Search
  targets in a fresh wave move or are taken within tens
  of seconds, so a dispatch that pauses to read screens
  loses its target.
- Kill 1, Squad 1 — a batched sequence (Events, Search,
  attack, March, no screenshot reads in between)
  dispatched Squad 1 at once: March Queues 1 of 4, Go
  X:959 Y:942, stamina 29 to 19.
- Kill 2, Squad 2, parallel — immediately after, the same
  batched sequence dispatched Squad 2 to X:962 Y:973:
  March Queues 2 of 4 was observed, with Squad 1 already
  Returning (00:00:31) and Squad 2 still going out.
  squads_parallel is therefore 2, verified by the 2 of 4
  reading, not merely by two dispatches. Stamina 19 to 9.
- Returns and LOOT claim — after the wait, March Queues
  read 0 of 4 with both squads back, and the gift box at
  the right end of the March Queues bar carried a red
  badge 2. The grounded tap 318,242 opened the LOOT
  panel. It held exactly two rows, both from this unit:
  Lv.10 X:962 Y:973 and Lv.10 X:959 Y:942, each medal
  x10, crate x4, iron 268.0K, food 268.0K, coin 268.0K,
  hero EXP 263.0K. The plain blue Claim All button (no
  price tag) at 499,765 was tapped; the panel closed and
  the gift badge cleared.
- Claim verification — HUD after the claim: coin 77.5M
  (from 76.9M), food 201.1M (from 200.6M), iron 387.5M
  (from 387.0M) — each up about 536,000 at HUD rounding,
  confirming the claim. Exact coin panel readings were
  not available this unit: the HUD rounds to 0.1M, and
  the carried exact balance from unit 029 (75,035,886)
  is stale because intervening truck, gift and mail
  activity moved the coin balance by about 1.9M since
  then, so no exact coin_before or coin_after is asserted
  here; coins_collected 536,000 is exact from the two
  LOOT rows.
- Stamina and medals — stamina 9 at the close, not
  exhausted, and no refill was needed inside this unit.
  Medals were not re-read in the Store this unit:
  medals_before 880 carried from unit 029's derived
  balance (no other zombie unit ran between 029 and
  030), medals_after 900 derived (880 plus 20 from the
  two claimed rows).
- Coin chests, NOT redeemed or opened in this unit —
  the unit window was spent on the rally-class pass-over,
  the moved target, and the two parallel dispatches, so
  no Store visit was made. The 4 owned Coin Chest (SSR)
  are still unlocated in inventory (unit 014 finding,
  still open), 3,248,640 coins pending, plus a new
  redemption the successor can make from the 900 derived
  balance under the maximize-coin decision.
- Totals — zombies_killed 2 claimed in-unit (X:959 Y:942
  and X:962 Y:973), coins_collected 536,000,
  coin_before HUD 76.9M, coin_after HUD 77.5M,
  medals_before 880 carried, medals_after 900 derived,
  chests_opened 0, squads_parallel 2 verified,
  tasks_badge 2, cleared false (the wave was still
  running, next wave about 53 minutes out, and Search
  found targets at once twice; the successor starts now).
  Nothing bought with diamonds or money, no speedup item
  burned, no rally started, no ally panel action taken.

## Follow-up for the successor

- Stamina is 9 at the close: open a stamina item from the
  Inventory Special tab before the next dispatch (unit
  029: 50-stamina x612, 10-stamina x612 after its use;
  do not mistake the Resources red-gem "10 Diamonds"
  items for stamina). Stamina is NOT exhausted.
- Read medals_before from the Store header (900 derived
  expected before any new kill rows), never from the old
  derived chain alone. With that balance, redeeming Coin
  Chest (SSR) for 160 medals remains authorized under the
  maximize-coin decision, and the 4 owned chests still
  need locating in inventory and opening (3,248,640
  coins pending).
- The first Search of this unit found a rally-class
  36.00M target: check the deploy panel's Vs line before
  March, and never march an "Unlikely to Win" rally
  target. A "target location has changed" toast means
  no stamina was charged; re-Search at once, batched.
- Claim LOOT rows in the same unit that dispatched them,
  from the kill-area map position via the grounded
  318,242 gift-box tap, before any BASE or WORLD tap
  that recentres the map.
