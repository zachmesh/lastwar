---
title: Zombie Invasion Execution 2026-10-28 1629 Queue Run
created: 2026-10-28T23:29:00Z
modified: 2026-10-28T23:29:00Z
level: L0
version: 1.0.0
description: Zombie-invasion chain unit 020 - partial, two squads dispatched in parallel, Squad 1 kill claimed for 268,000 coins, Squad 2 still in flight at the unit cap, successor starts now
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-28
  - source: owner task unit queue design of 2026-10-28
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization, the task unit queue ticker with its 15 minute unit cap and Zombie Invasion continuation chains
  - source: owner instruction of 2026-10-28 - collect the event coins from the task collection icon and maximize coin, dispatch squads in parallel
  - source: owner decision of 2026-10-28 - redeem event medals for Coin Chests in the event Store and open owned Coin Chests
---

# Zombie Invasion — execution, 2026-10-28 1629 queue unit 020

A single task unit, executed by executor ticker-1604 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-020,
chain zombie-2026-10-28, chain sequence 20, priority 4.
Session window about 16:16 to 16:29 America/Los_Angeles.
Status — partial; Squad 2 was still in flight at the unit
cap, so its kill and LOOT row are left to the successor
and the tracker is left untouched.

## What was observed

- Open — base screen, coin HUD 53.6M, Total Power
  149,351,992, stamina 120 at the deploy panel. No
  different-device dialog appeared.
- Event page — Events opened and the Zombie Invasion tab
  was verified by its title on sight before any Search tap.
  The page read 2 days 02:41:52 left and The next wave of
  invading Zombies will arrive in 00:23:07.
- Dispatch 1, Squad 1 — Search found a Lv.10 Invading
  Zombies target: Guaranteed Reward medal x10, book 1.3K,
  hero EXP 263.0K, iron 268.0K, food 268.0K, Suggested Power
  670,000, stamina cost 10, despawn timer 11:22:40. The
  crossed-swords button sits at about 500,712 in this
  control system (a tap at 498,694 only animated it).
  Deploy panel: Squad 1 25.05M against 670,000, Easy Win,
  march time 00:03:09, stamina 120, cost minus 10.
  March button lesson, re-confirmed — taps at 467,726
  and 498,704 left the panel open with stamina unchanged
  (the same failure unit 019 hit), while the tap at
  440,783 dispatched at once, as unit 017 recorded.
  Verified after dispatch: March Queues 1 of 4, Go
  X:794 Y:956, 00:02:41 remaining, stamina 120 to 110.
- Dispatch 2, Squad 2, parallel — a batched
  Events-Search-crossed-swords-squad-2-tab-March sequence
  (Search 327,931; crossed 500,712; squad-2 tab 397,920;
  March 440,783) put Squad 2 on a distinct Lv.10 target
  while Squad 1 was still out. Verified: March Queues
  2 of 4, Squad 1 Go X:794 Y:956 00:01:38, Squad 2 Go
  X:800 Y:768 00:04:27, stamina 110 to 100. squads_parallel
  2 in this unit — the march queue cap of 4 was not the
  binding limit; the unit cap was.
- Kill and LOOT claim, Squad 1 — after about a minute
  Squad 1 read Returning 00:03:08 and the March Queues
  bar carried a gift box with a red badge 1 (at about
  317,233). Tapping it opened the LOOT panel with exactly
  one row: Lv.10 Invading Zombies X:794 Y:956, medal x10,
  crate x4, iron 268.0K, food 268.0K, coin 268.0K, hero
  EXP 263.0K. The plain blue Claim All button (no price
  tag) was tapped and the panel closed. HUD after the
  claim: coin 53.6M to 53.8M, food 162.4M to 162.7M, iron
  348.7M to 349.0M — all consistent with the 268.0K row.
  The LOOT badge cleared.
- Exact coin — the coin detail panel read exactly
  53,871,536 owned after the claim. No coin-moving action
  preceded the claim in this unit (kills pay nothing
  directly), so coin_before is 53,871,536 minus 268,000
  equals 53,603,536, matching the 53.6M HUD at the open.
- Stamina and medals — stamina 120 at the open, 100 after
  the two 10-cost marches, 101 at the coin panel read
  (regeneration). Medals carried at 50 from unit 019;
  the claimed row paid medal x10, so medals_after is 60
  in this unit, with Squad 2's medal still unclaimed.
- Coin chests — not pursued in this unit: the 3 owned Coin
  Chest (SSR) are still unlocated in inventory (unit 014
  finding), and no Store redemption was attempted; the
  medal balance of 60 is still below a further 160-medal
  redemption in any case.
- Totals — zombies_killed 1 verified in-unit (Squad 1's
  X:794 Y:956 target; Squad 2's X:800 Y:768 target not
  yet resolved), coins_collected 268,000, coin_before
  53,603,536, coin_after 53,871,536, medals_before 50
  carried, medals_after 60, chests_opened 0,
  squads_parallel 2, cleared false (Squad 2 still out,
  the wave still running, next wave about 23 minutes out
  at the event page read). Nothing bought, no diamonds
  or money spent, no speedup item burned, no stamina
  resource item opened (stamina never bound this unit).

## Follow-up for the successor

- First check the March Queues bar and the LOOT badge:
  Squad 2 to X:800 Y:768 should have returned or be
  returning by the next tick; claim its LOOT row
  (expected 268,000 per the later-wave Lv.10 row rate)
  and re-read the exact coin panel before and after.
- Then re-run Search for the next parallel pair; the
  March button coordinate 440,783 and the crossed-swords
  coordinate 500,712 are the pinned values for this
  control system.
- Do not engage any Lv.95 rally-class Zombie Boss
  returned by Search; only nearby Lv.10 Invading Zombies
  targets are in scope for this chain.
