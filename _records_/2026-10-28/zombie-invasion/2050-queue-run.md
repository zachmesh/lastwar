---
title: Zombie Invasion Execution 2026-10-28 2050 Queue Run
created: 2026-10-29T03:50:00Z
modified: 2026-10-29T03:50:00Z
level: L0
version: 1.0.0
description: Zombie-invasion chain unit 027 - partial, Coin Chest (SSR) redeemed for 160 medals after tooltip identification, medal balance corrected to 1000 before and 840 after, no kill dispatched because the only March attempt hit a moved target, chain continues, successor starts now
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-28
  - source: owner task unit queue design of 2026-10-28
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization, the task unit queue ticker with its 15 minute unit cap and Zombie Invasion continuation chains
  - source: owner instruction of 2026-10-28 - collect the event coins from the task collection icon and maximize coin, dispatch squads in parallel
  - source: owner decision of 2026-10-28 - redeem event medals for Coin Chests in the event Store and open owned Coin Chests
---

# Zombie Invasion — execution, 2026-10-28 2050 queue unit 027

A single task unit, executed by executor ticker-2034 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-027,
chain zombie-2026-10-28, chain sequence 27, priority 4.
Session window about 20:34 to 20:50 America/Los_Angeles.
Status — partial; the unit hit its 15 minute cap with the
Store redemption done but no kill dispatched, so the chain
continues and the tracker is left untouched.

## What was observed

- Open — the game was already on the Zombie Invasion
  Events page, title verified on sight. No
  different-device dialog appeared. Event page read
  1 day 22:23:56 left, next wave in 00:05:13 at the open.
- Coin panel, NOT re-read — coin_before is carried
  from unit 026 (73,963,886 derived); the world-map HUD
  read 73.9M at the close, confirming no intervening
  coin move, and no LOOT claim was made in-unit, so
  coin_after equals coin_before.
- Store, medal balance CORRECTION — the Store header
  read 1000 at the open, not the 170 derived by the
  unit 024 to 026 chain. That derived chain is
  superseded: successors must read the Store header
  as medals_before, never carry the derived figure.
  The header is the medal balance — it fell by exactly
  the redemption price, 1000 to 840, on the purchase
  below.
- Store, chest identification — the two 160-medal rows
  visible at first sight are NOT coin chests: row 4
  (Limit 50) is Iron Chest (SSR, 1.35M iron) and row 5
  (Limit 50) is Food Chest (SSR, 1.35M food), each
  identified by tapping its item icon and reading its
  tooltip. Scrolling the Store list down (drag
  500,700 to 500,350) revealed the Coin Chest row:
  160 medals, Limit 99 at the open, gold-coin item
  icon. Its tooltip reads Coin Chest (SSR), Owned 3,
  812.16K coins at the current Base Level.
- Store, redemption — the BUY ITEMS dialog for that
  row reads Coin Chest (SSR), Unit Price 160, Total
  Price 160, quantity 1, Buy button medal 160. Buy
  was tapped (a medal-denominated redemption covered
  by the owner maximize-coin decision, not a diamond
  or money purchase). CONGRATULATIONS granted the
  chest; the Store header fell to exactly 840, and
  tapping the granted chest read Coin Chest (SSR),
  Owned 4. The Coin Chest row Limit then read 98.
  Total pending coin in owned chests is now
  4 times 812,160, or 3,248,640 coins. The 4 owned
  Coin Chest (SSR) are still unlocated in inventory
  (unit 014 finding, still open).
- Wave reset — during the Store work the next-wave
  countdown ran out and reset to about 00:59:14, so a
  fresh wave was running when hunting began.
- Kill attempt, Squad 1, target moved — Search found
  a Lv.10 Invading Zombies target at once
  (Suggested Power 670,000, stamina cost 10, despawn
  11:58:27, Guaranteed Reward medal x10, book 1.3K,
  hero EXP 263.0K, iron 268.0K, food 268.0K).
  Crossed swords at 500,712 opened the deploy panel
  (Squad 1, 25.05M vs 670,000, Easy Win, Unit Count
  2,231 of 2,231, march 00:00:10, stamina 22 on the
  panel, 23 by the close through regeneration).
- March button lesson — image-estimated March taps
  at 440,640, 452,652, 444,664 and 472,760 all failed
  with no change, and the control channel reported
  background clicks do not reach that control. Two
  Last War windows exist on the Mac (78525 at
  642x951 and 79275 at 642x919, same game state);
  the grounded March point on the 78525 window,
  502,744, dispatched at once. Successors: use the
  grounded point on window 78525, not image
  estimates, and not the 79275 window's coordinates.
  The long button struggle cost the target: the
  dispatched March answered with the toast "The
  target location has changed. Please try again."
  and the panel closed with no squad marching and
  no stamina charged (the moved-target pattern of
  unit 006). No second Search was run — the unit
  cap had been reached.
- Stamina and medals — stamina 22 at the deploy
  panel, 23 at the close, no stamina resource item
  opened (stamina never bound this unit; the failed
  March charged nothing). Medals verified 1000
  before the redemption, 840 after, no kill rows
  claimed, so medals_after is 840.
- Coin chests — 1 redeemed in-unit (see above),
  0 opened (inventory location still unknown).
- Totals — zombies_killed 0 in-unit, coins_collected
  0 in-unit, coin_before 73,963,886 carried,
  coin_after 73,963,886, medals_before 1000 verified,
  medals_after 840 verified, chests_opened 0,
  chests_redeemed 1, squads_parallel 0 (no squad
  marched; the moved target, not a game cap or
  stamina, is the reason), tasks_badge not observed
  (no LOOT rows existed to claim), cleared false
  (the fresh wave is running; Search found a Lv.10
  target at once). Nothing bought with diamonds or
  money, no speedup item burned, no rally started,
  no ally panel action taken.

## Follow-up for the successor

- Re-run Search at once for a fresh Lv.10 target and
  dispatch with the grounded March point 502,744 on
  window 78525, in one prompt sequence — do not spend
  the unit's minutes on image-estimated March taps,
  or the target will move again. Verify the target
  card reads Lv.10 Invading Zombies before the
  crossed-swords tap (500,712); a boss card opens
  the rally panel and must be closed, never rallied.
- Read medals_before from the Store header (840
  expected before any new kill rows), never from the
  old derived chain. The 4 owned Coin Chest (SSR)
  still need locating in inventory and opening
  (3,248,640 coins pending).
- Claim LOOT rows in the same unit that dispatched
  them, from the kill-area map position via the
  pinned 317,233 gift-box tap, before any BASE or
  WORLD tap that recentres the map — unit 025's
  rows show that rows left unclaimed across a
  recentring do not survive to the next unit.
