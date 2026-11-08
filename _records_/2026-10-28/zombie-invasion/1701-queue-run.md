---
title: Zombie Invasion Execution 2026-10-28 1701 Queue Run
created: 2026-10-29T00:01:00Z
modified: 2026-10-29T00:01:00Z
level: L0
version: 1.0.0
description: Zombie-invasion chain unit 022 - partial, handover kill plus a new parallel pair claimed for 804,000 coins, chain continues, successor starts now
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-28
  - source: owner task unit queue design of 2026-10-28
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization, the task unit queue ticker with its 15 minute unit cap and Zombie Invasion continuation chains
  - source: owner instruction of 2026-10-28 - collect the event coins from the task collection icon and maximize coin, dispatch squads in parallel
  - source: owner decision of 2026-10-28 - redeem event medals for Coin Chests in the event Store and open owned Coin Chests
---

# Zombie Invasion — execution, 2026-10-28 1701 queue unit 022

A single task unit, executed by executor ticker-1636 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-022,
chain zombie-2026-10-28, chain sequence 22, priority 4.
Session window about 16:50 to 17:01 America/Los_Angeles.
Status — partial; the chain continues while the event is
available, so the successor starts now and the tracker is
left untouched. All squads dispatched in this unit were
resolved and claimed inside it.

## What was observed

- Open — base screen, coin HUD 54.4M, Total Power
  149,351,992, stamina 85 at the top-left lightning icon.
  No different-device dialog appeared. The computer
  session closed twice during waits for march returns
  (cc-140, then cc-141 opened); each reopening found
  the Last War window with state intact.
- Handover kill claimed first — March Queues 0/4 with a
  gift box carrying a red badge 1 at about 317,233, the
  unit 021 Squad 1 return. Tapping it opened the LOOT
  panel with exactly one row: Lv.10 Invading Zombies
  X:800 Y:755, medal x10, crate x4, iron 268.0K, food
  268.0K, coin 268.0K, hero EXP 263.0K. The plain blue
  Claim All button (no price tag) was tapped and the
  panel closed.
- Dispatch 1, Squad 1 — Events opened (tap note: from
  the world map an Events tap at 903,158 lands on the
  base interior, and the Events panel opens from there
  at 942,152). The Zombie Invasion tab was verified by
  its title on sight before any Search tap; the page
  read 2 days 02:07:58 left. A batched Search, crossed
  swords, March sequence (Search 327,931; crossed
  500,712; March 440,783) dispatched Squad 1. Verified:
  March Queues 1/4, Go X:999 Y:897 (the earlier OCR
  read of X:499 was a misread of the same entry).
- Dispatch 2, Squad 2, parallel — Events reopened and
  the Zombie Invasion tab verified again, then a
  batched Search, crossed-swords, squad-2-tab, March
  sequence (Search 327,931; crossed 500,712; squad-2
  tab 397,920; March 440,783) put Squad 2 out while
  Squad 1 was still marching. Verified: March Queues
  2/4, Go X:999 Y:897 00:00:06 and Go X:959 Y:896
  00:00:57, stamina 85 to 66 (two 10-cost marches plus
  one point of regeneration). squads_parallel 2 in
  this unit; the march queue cap of 4 was not the
  binding limit.
- Both kills claimed — after a 2 minute 30 second wait
  March Queues read 0/4 and the gift box carried a new
  badge. The LOOT panel held exactly two rows: Lv.10
  Invading Zombies X:959 Y:896 (medal x10, crate x1,
  iron 268.0K, food 268.0K, coin 268.0K, hero EXP
  263.0K) and Lv.10 Invading Zombies X:999 Y:897
  (medal x10, crate x4, same 268.0K coin line). The
  plain blue Claim All button (no price tag) was
  tapped for both rows at once. HUD after: coin 55.2M,
  food 164.0M, iron 350.3M — all consistent with the
  804,000 claimed in this unit (the post-claim OCR
  first misread the coin HUD as 54.6M; the fresh
  screenshot reads 55.2M and confirms the claim).
- Exact coin — coin_before is 54,407,536 (unit 021
  coin_after; no coin-moving action in between, kills
  pay nothing directly). coin_after is 54,407,536
  plus 804,000 equals 55,211,536, matching the 55.2M
  HUD at the close. The figures are derived as unit
  020 derived its coin_before; the HUD confirms both
  steps.
- Stamina and medals — stamina 85 at the open, 66
  after the two 10-cost marches. Medals carried at 80
  from unit 021; the three claimed rows paid medal
  x10 each, so medals_after is 110 in this unit.
- Coin chests — not pursued in this unit: the 3 owned
  Coin Chest (SSR) are still unlocated in inventory
  (unit 014 finding), and the medal balance of 110 is
  still below a further 160-medal Store redemption in
  any case.
- Totals — zombies_killed 3 claimed in-unit (the unit
  021 handover X:800 Y:755 and the new pair X:959
  Y:896 and X:999 Y:897), coins_collected 804,000,
  coin_before 54,407,536, coin_after 55,211,536,
  medals_before 80 carried, medals_after 110,
  chests_opened 0, squads_parallel 2, cleared false
  (the wave is still running; no exhaust check was
  made, so the successor starts now). Nothing bought,
  no diamonds or money spent, no speedup item burned,
  no stamina resource item opened (stamina never bound
  this unit).

## Follow-up for the successor

- Re-run Search for the next parallel pair; the March
  button coordinate 440,783 and the crossed-swords
  coordinate 500,712 are the pinned values for this
  control system, and the Events panel opens from the
  base interior at 942,152.
- Do not engage any Lv.95 rally-class Zombie Boss
  returned by Search; only nearby Lv.10 Invading Zombies
  targets are in scope for this chain.
