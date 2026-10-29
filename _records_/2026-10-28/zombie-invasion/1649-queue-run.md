---
title: Zombie Invasion Execution 2026-10-28 1649 Queue Run
created: 2026-10-28T23:49:00Z
modified: 2026-10-28T23:49:00Z
level: L0
version: 1.0.0
description: Zombie-invasion chain unit 021 - partial, handover kill and one new parallel kill claimed for 536,000 coins, Squad 1 still returning at the unit cap, successor starts now
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-28
  - source: owner task unit queue design of 2026-10-28
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization, the task unit queue ticker with its 15 minute unit cap and Zombie Invasion continuation chains
  - source: owner instruction of 2026-10-28 - collect the event coins from the task collection icon and maximize coin, dispatch squads in parallel
  - source: owner decision of 2026-10-28 - redeem event medals for Coin Chests in the event Store and open owned Coin Chests
---

# Zombie Invasion — execution, 2026-10-28 1649 queue unit 021

A single task unit, executed by executor ticker-1636 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-021,
chain zombie-2026-10-28, chain sequence 21, priority 4.
Session window about 16:37 to 16:49 America/Los_Angeles.
Status — partial; Squad 1 was still returning at the unit
cap, so its kill and LOOT row are left to the successor
and the tracker is left untouched.

## What was observed

- Open — base screen, coin HUD 53.8M, Total Power
  149,351,992, stamina 103 at the top-left lightning icon.
  No different-device dialog appeared. The first computer
  session (cc-138) closed during a 3 minute wait for a
  march return; a fresh session (cc-140) was opened and
  the Last War window re-selected with state intact.
- Handover kill claimed first — March Queues 0/4 with a
  gift box carrying a red badge 1 at about 317,233, the
  unit 020 Squad 2 return. Tapping it opened the LOOT
  panel with exactly one row: Lv.10 Invading Zombies
  X:800 Y:768, medal x10, crate x4, iron 268.0K, food
  268.0K, coin 268.0K, hero EXP 263.0K. The plain blue
  Claim All button (no price tag) was tapped and the
  panel closed. HUD after: coin 54.1M, food 162.9M,
  iron 349.3M — all consistent with the 268.0K row.
- Dispatch 1, Squad 1 — Events opened (tap note: from
  the world map an Events tap at 903,158 lands on the
  base interior, and the Events panel opens from there
  at 942,152; from the base interior 942,152 opens it
  directly). The Zombie Invasion tab was verified by its
  title on sight before any Search tap. The page read
  2 days 02:19:37 left and the next wave in 00:00:52.
  Search found a Lv.10 Invading Zombies target:
  Guaranteed Reward medal x10, book 1.3K, hero EXP
  263.0K, iron 268.0K, food 268.0K, Suggested Power
  670,000, stamina cost 10, despawn timer 11:00:25.
  Crossed-swords at 500,712 opened the deploy panel
  (Squad 1, Easy Win, march 00:04:2x); March at 440,783
  dispatched at once. Verified: March Queues 1/4,
  Go X:800 Y:755, 00:04:15 remaining, stamina 103 to 93.
- Dispatch 2, Squad 2, parallel — a batched
  Events-Search-crossed-swords-squad-2-tab-March sequence
  (Search 327,931; crossed 500,712; squad-2 tab 397,920;
  March 440,783) ran while Squad 1 was still out. The
  second march was a short home-cluster run: by the
  next screenshot March Queues read 1/4 again, stamina
  93 to 84, and the gift box at 317,233 carried a new
  red badge 1. Tapping it opened the LOOT panel with
  exactly one row: Lv.10 Invading Zombies X:994 Y:953,
  medal x10, crate x4, iron 268.0K, food 268.0K,
  coin 268.0K, hero EXP 263.0K. The plain blue Claim
  All button (no price tag) was tapped. HUD after:
  coin 54.4M, food 163.2M, iron 349.5M. squads_parallel
  2 in this unit — Squad 2 marched and returned while
  Squad 1 was still out; the march queue cap of 4 was
  not the binding limit.
- Squad 1 still out at the cap — after a 3 minute wait
  the bar read Go X:800 Y:755, 00:01:15 remaining, and
  at the closing screenshot Returning 00:01:22. Its
  kill and LOOT row (expected 268,000 per the
  later-wave Lv.10 row rate) are left to the successor.
- Exact coin — coin_after of unit 020 was exactly
  53,871,536. No coin-moving action preceded the two
  claims in this unit (kills pay nothing directly), so
  coin_before is 53,871,536 and coin_after is
  53,871,536 plus 536,000 equals 54,407,536, matching
  the 54.4M HUD at the close. The exact panel was not
  re-read this unit; the figures are derived as unit
  020 derived its coin_before, and the HUD confirms
  both steps.
- Stamina and medals — stamina 103 at the open, 93
  after the Squad 1 march, 84 after the Squad 2 march
  (one point of regeneration in between). Medals
  carried at 60 from unit 020; the two claimed rows
  paid medal x10 each, so medals_after is 80 in this
  unit, with Squad 1's medal still unclaimed.
- Coin chests — not pursued in this unit: the 3 owned
  Coin Chest (SSR) are still unlocated in inventory
  (unit 014 finding), and the medal balance of 80 is
  still below a further 160-medal Store redemption in
  any case.
- Totals — zombies_killed 2 claimed in-unit (the unit
  020 handover X:800 Y:768 and the new Squad 2 kill
  X:994 Y:953; Squad 1's X:800 Y:755 target not yet
  resolved), coins_collected 536,000, coin_before
  53,871,536, coin_after 54,407,536, medals_before 60
  carried, medals_after 80, chests_opened 0,
  squads_parallel 2, cleared false (Squad 1 still
  returning, the next wave arriving). Nothing bought,
  no diamonds or money spent, no speedup item burned,
  no stamina resource item opened (stamina never bound
  this unit).

## Follow-up for the successor

- First check the March Queues bar and the LOOT badge:
  Squad 1 to X:800 Y:755 should have returned by the
  next tick; claim its LOOT row (expected 268,000)
  and re-read the exact coin panel before and after.
- Then re-run Search for the next parallel pair; the
  March button coordinate 440,783 and the crossed-swords
  coordinate 500,712 are the pinned values for this
  control system, and the Events panel opens from the
  base interior at 942,152.
- Do not engage any Lv.95 rally-class Zombie Boss
  returned by Search; only nearby Lv.10 Invading Zombies
  targets are in scope for this chain.
