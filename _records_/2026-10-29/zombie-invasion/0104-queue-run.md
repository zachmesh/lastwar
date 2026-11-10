---
title: Zombie Invasion Execution 2026-10-29 0104 Queue Run
created: 2026-10-29T08:15:00Z
modified: 2026-10-29T08:15:00Z
level: L0
version: 1.0.0
description: Zombie-invasion chain unit 032 - partial, two Lv.10 kills dispatched in parallel and claimed in-unit for 536,000 coins, one 10-stamina item opened before the first dispatch, squads_parallel 2 verified, chain continues, successor starts now
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-29
  - source: owner task unit queue design of 2026-10-28
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization, the task unit queue ticker with its 15 minute unit cap and Zombie Invasion continuation chains
  - source: owner instruction of 2026-10-28 - collect the event coins from the task collection icon and maximize coin, dispatch squads in parallel
  - source: owner reminder of 2026-10-28 - open the stamina resource items held in the inventory and use them
  - source: owner decision of 2026-10-28 - redeem event medals for Coin Chests in the event Store and open owned Coin Chests
---

# Zombie Invasion — execution, 2026-10-29 0104 queue unit 032

A single task unit, executed by executor ticker-0104 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-032,
chain zombie-2026-10-28, chain sequence 32, priority 4.
Session window about 01:04 to 01:15 America/Los_Angeles.
Status — partial; the chain continues while the event is
available and the wave is still running, so the tracker is
left untouched. Both squads dispatched in this unit were
resolved and claimed inside it.

## What was observed

- Open — the game was already on the base interior screen,
  coin HUD 78.0M, Total Power 149,351,992, stamina 14 on
  the base HUD. No different-device dialog appeared. The
  computer session dropped once during the wait for the
  squads to return (cc-205 ended, cc-207 opened); each
  reopening found the Last War window 78525 with state
  intact.
- Stamina refill BEFORE the first dispatch, per unit 031
  follow-up — Inventory Special tab, grid dragged up:
  50-stamina x614 and 10-stamina x611 confirmed (the
  Resources red-gem "10 Diamonds" items are NOT stamina
  and were not touched). One 10 Stamina item opened
  (selected at the grounded point 407,570, Use tap,
  count 611 to 610). Base HUD stamina then read 22 at
  the target card and 25 in the deploy panel.
- Events page — opened from the base via 942,152,
  landing directly on the Zombie Invasion tab. At the
  open the page read 1 day 17:51:21 left, next wave in
  00:32:40, so the current wave was still running.
- Kill 1, Squad 1 — Search at the grounded centre
  375,943 found a Lv.10 Invading Zombies card:
  Guaranteed Reward medal x10, book 1.3K, hero EXP
  263.0K, iron 268.0K, food 268.0K; Potential Reward
  crate x1, box x4, ticket x1; Suggested Power 670,000;
  stamina cost 10; despawn 11:32:07. The crossed-swords
  button at the grounded point 500,750 opened the
  deploy panel: Squad 1, 25.05M Vs 670.00K, Easy Win,
  Unit Count 2,231 of 2,231, stamina 25. March at
  499,750 dispatched Squad 1 to X:952 Y:980,
  stamina 25 to 15.
- Kill 2, Squad 2, parallel — immediately after, Events
  and Search in one batch found a second Lv.10 card
  (Suggested Power 670,000), and a batched
  crossed-swords plus March dispatched Squad 2 to
  X:934 Y:973. March Queues 2 of 4 was observed, with
  Squad 1 already Returning (00:00:44) and Squad 2
  still going out (00:00:53). squads_parallel is
  therefore 2, verified by the 2 of 4 reading, not
  merely by two dispatches. Stamina 15 to 5.
- Coordinate note — a first tap at 502,676 on the
  crossed-swords button did nothing; visual grounding
  placed the button at 498,749, matching the grounded
  500,750 used by earlier units. The screenshot-pixel
  estimate of the button centre is unreliable in this
  control channel; trust the grounded points.
- Returns and LOOT claim — after the wait, March
  Queues read 0 of 4 with both squads back, and the
  gift box at the right end of the March Queues bar
  carried a red badge 2. The grounded tap 318,242
  opened the LOOT panel. It held exactly two rows,
  both from this unit: Lv.10 X:934 Y:973 and Lv.10
  X:952 Y:980, each medal x10, crate x4, iron 268.0K,
  food 268.0K, coin 268.0K, hero EXP 263.0K. The plain
  blue Claim All button (no price tag) at 499,765 was
  tapped; the panel closed and the gift badge cleared.
- Claim verification — HUD after the claim: coin
  78.5M (from 78.0M), food 202.2M (from 201.6M), iron
  388.6M (from 388.1M) — each up about 536,000 at HUD
  rounding, confirming the claim. Exact coin panel
  readings were not available this unit: the HUD
  rounds to 0.1M, so no exact coin_before or
  coin_after is asserted here; coins_collected
  536,000 is exact from the two LOOT rows at 268,000
  each.
- Stamina and medals — stamina 6 at the close (5 after
  kill 2 plus about 1 regenerated), not exhausted.
  Medals were not re-read in the Store this unit:
  medals_before 920 carried from unit 031's derived
  balance (no other zombie unit ran between 031 and
  032), medals_after 940 derived (920 plus 20 from
  the two claimed rows).
- Coin chests, NOT redeemed or opened in this unit —
  the unit window was spent on the stamina refill, the
  two parallel dispatches and the two claims, so no
  Store visit was made. The 4 owned Coin Chest (SSR)
  are still unlocated in inventory (unit 014 finding,
  still open), 3,248,640 coins pending, plus a new
  redemption the successor can make from the 940
  derived balance under the maximize-coin decision.
- Totals — zombies_killed 2 claimed in-unit (X:952
  Y:980 and X:934 Y:973), coins_collected 536,000,
  coin_before HUD 78.0M, coin_after HUD 78.5M,
  medals_before 920 carried, medals_after 940
  derived, chests_opened 0, squads_parallel 2
  verified, tasks_badge 2, cleared false (the wave
  was still running, next wave about 32 minutes out,
  and Search found targets at once twice; the
  successor starts now). Nothing bought with diamonds
  or money, no speedup item burned, no rally started,
  no ally panel action taken.

## Follow-up for the successor

- Stamina is 6 at the close: open a stamina item from
  the Inventory Special tab BEFORE the first dispatch
  (50-stamina x614 untouched, 10-stamina x610 after
  this unit's use), so the squads can overlap again.
  Stamina is NOT exhausted.
- Read medals_before from the Store header (940 derived
  expected before any new kill rows), never from the old
  derived chain alone. With that balance, redeeming Coin
  Chest (SSR) for 160 medals remains authorized under
  the maximize-coin decision, and the 4 owned chests
  still need locating in inventory and opening
  (3,248,640 coins pending).
- Trust the grounded tap points (crossed swords
  500,750, March 499,750, gift box 318,242, Claim All
  499,765) over screenshot-pixel estimates in this
  control channel.
- Claim LOOT rows in the same unit that dispatched them,
  from the kill-area map position via the grounded
  318,242 gift-box tap, before any BASE or WORLD tap
  that recentres the map.
