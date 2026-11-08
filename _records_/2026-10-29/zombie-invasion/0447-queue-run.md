---
title: Zombie Invasion Execution 2026-10-29 0447 Queue Run
created: 2026-10-29T12:02:00Z
modified: 2026-10-29T12:02:00Z
level: L0
version: 1.0.0
description: Zombie-invasion chain unit 040 - partial, two Lv.10 kills claimed in-unit for 536,000 coins, squads_parallel 2 verified, one transient control-channel loss and one computer-session timeout recovered, chain continues, successor starts now
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-29
  - source: owner task unit queue design of 2026-10-28
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization, the task unit queue ticker with its 15 minute unit cap and Zombie Invasion continuation chains
  - source: owner instruction of 2026-10-28 - collect the event coins from the task collection icon and maximize coin, dispatch squads in parallel
  - source: owner reminder of 2026-10-28 - open the stamina resource items held in the inventory and use them
  - source: owner decision of 2026-10-28 - redeem event medals for Coin Chests in the event Store and open owned Coin Chests
---

# Zombie Invasion — execution, 2026-10-29 0447 queue unit 040

A single task unit, executed by executor ticker-0434 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-040,
chain zombie-2026-10-28, chain sequence 40, priority 4.
Session window about 04:47 to 05:00 America/Los_Angeles.
Status — partial; the chain continues while the event is
available and zombies remain nearby, so the tracker is
left untouched. Both squads dispatched in this unit were
resolved and claimed inside it, and the march queue was
empty at the close.

## What was observed

- Open — the game was on the world map (left over from
  unit 039), coin HUD 97.9M, Total Power 149,351,992,
  stamina 33 carried from unit 039 (plus 1 regenerated,
  34 at the first deploy read). No different-device
  dialog appeared. The computer session cc-229 timed
  out mid-unit and was replaced by cc-233; the game
  window 98425 stayed up throughout.
- Events page — opened from the map via 942,152 and
  landed on the Zombie Invasion tab (title verified
  before Search, per the unit 039 lesson).
- Kill 1, Squad 1 — Search at 375,925 found a Lv.10
  card (Suggested Power 670,000); the grounded
  crossed-swords tap at 500,765 opened the deploy
  panel (Squad 1, 2,231 of 2,231, Easy Win); a first
  March tap failed in the control channel (target app
  reported exited, input not dispatched — the window
  was in fact still up under the same pid, so this
  was a transient channel loss, not a crash); after
  re-activating, the deploy panel was still open
  (Squad 1, 25.05M Vs 670.00K, Easy Win, March
  00:00:20, stamina 34) and March at 499,750
  dispatched it: March Queues 1 of 4, Go X:989
  Y:974, about 10 seconds out.
- Kill 2, Squad 2, parallel — Events, Search, then
  the crossed-swords tap at 500,765 on an
  identical-layout card opened the deploy panel,
  which had auto-selected Squad 2 (Unit Count
  2,175, Easy Win). March dispatched it: March
  Queues 2 of 4 verified, Go X:985 Y:975,
  stamina 34 to 14.
- LOOT claim — after a 30 second wait the computer
  session cc-229 had timed out; session cc-233 was
  started and the window re-activated, showing
  March Queues 0 of 4 (both squads home) and a gift
  badge 2. The grounded tap 318,222 opened the
  LOOT panel with exactly two rows: Lv.10 X:985
  Y:975 and Lv.10 X:989 Y:974, each medal x10,
  iron 268.0K, food 268.0K, coin 268.0K, hero EXP
  263.0K. The plain blue Claim All button (no price
  tag) at 499,765 was tapped; the panel closed and
  the gift badge cleared. Claim verification — HUD
  after the claim: coin 98.4M (from 97.9M), food
  219.8M (from 219.3M), iron 406.1M (from 405.5M) —
  each up about 536,000 at HUD rounding, confirming
  the claim. Exact coin panel readings were not
  available this unit: the HUD rounds to 0.1M, so no
  exact coin_before or coin_after is asserted here;
  coins_collected is exact from the LOOT rows.
- Stamina and medals — stamina 14 at the close,
  not exhausted, and no refill was needed inside
  this unit. Inventory stamina after the unit is
  50-stamina x610 and 10-stamina x621 (unchanged
  from unit 039). Medals were not re-read in the
  Store this unit: medals_before 1180 carried from
  unit 039's derived balance (no other zombie unit
  ran between 039 and 040), medals_after 1200
  derived (1180 plus 20 from the two claimed rows).
- Coin chests, NOT redeemed or opened in this unit —
  the unit window was spent on the two dispatches,
  the channel-loss recovery, the session restart
  and the claim, so no Store visit was made. The 4
  owned Coin Chest (SSR) are still unlocated in
  inventory (unit 014 finding, still open),
  3,248,640 coins pending, plus a new redemption
  the successor can make from the 1200 derived
  balance under the maximize-coin decision.
- Totals — zombies_killed 2 claimed in-unit (X:989
  Y:974 and X:985 Y:975), coins_collected 536,000,
  coin_before HUD 97.9M, coin_after HUD 98.4M,
  medals_before 1180 carried, medals_after 1200
  derived, chests_opened 0, squads_parallel 2
  verified by the 2 of 4 queue reading, tasks_badge
  2, cleared false (Search found targets at once
  twice and the wave was still running; the
  successor starts now, and the queue was empty at
  the close). Nothing bought with diamonds or
  money, no speedup item burned, no rally started,
  no teleport used, no ally panel action taken.

## Follow-up for the successor

- Stamina is 14 at the close with 50-stamina x610
  and 10-stamina x621 in inventory: open one
  50-stamina item before the first dispatch of the
  next round (33 to 14 covers only one more
  two-squad round without a refill).
- Read medals_before from the Store header (1200
  derived expected before any new kill rows), never
  from the old derived chain alone. With that balance,
  redeeming Coin Chest (SSR) for 160 medals remains
  authorized under the maximize-coin decision, and
  the 4 owned chests still need locating in inventory
  and opening (3,248,640 coins pending).
- Ground the crossed-swords button per card before
  tapping it (765 on both cards this unit).
- If a March tap reports the target app exited but
  the window is still listed under the same pid,
  re-activate and re-check the panel instead of
  assuming a crash — the tap was not dispatched.
- Computer sessions time out after roughly half an
  hour: if observe reports no session, start a new
  one and re-activate the game window; LOOT rows
  survive the gap.
- Claim LOOT rows in the same unit that dispatched
  them, from the kill-area map position via the
  grounded gift-box tap, before any BASE or WORLD
  tap that recentres the map.
