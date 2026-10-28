---
title: Zombie Invasion Execution 2026-10-28 1317 Queue Run
created: 2026-10-28T20:17:00Z
modified: 2026-10-28T20:17:00Z
level: L0
version: 1.0.0
description: Zombie-invasion chain unit 017 - partial, one Squad 1 march dispatched and verified to X951 Y765, second parallel dispatch blocked when Search returned a Lv.95 rally-class Zombie Boss that was correctly not engaged, march still in flight at the unit cap so no kill or LOOT claim verified in this unit, cleared false, successor starts now
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-28
  - source: owner task unit queue design of 2026-10-28
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization, the task unit queue ticker with its 15 minute unit cap and Zombie Invasion continuation chains
  - source: owner instruction of 2026-10-28 - collect the event coins from the task collection icon and maximize coin, dispatch squads in parallel
  - source: owner decision of 2026-10-28 - redeem event medals for Coin Chests in the event Store and open owned Coin Chests
---

# Zombie Invasion — execution, 2026-10-28 1317 queue unit 017

A single task unit, executed by executor ticker-1304 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-017,
chain zombie-2026-10-28, chain sequence 17, priority 4.
Session window about 13:05 to 13:17 America/Los_Angeles.
Status — partial; one march was dispatched and verified, but
it was still in flight at the unit cap, so no kill, LOOT
claim or coin collection was verified inside this unit, and
the chain continues via its successor starting now.

## What was observed

- Open — coin detail panel read exactly 51,194,936 owned,
  identical to unit 016's closing read, so no intervening
  change. Stamina 120 at the open, diamonds 658 in the top
  bar. No different-device dialog appeared in this unit.
- Event page — Events opened and the Zombie Invasion tab
  was verified by its title on sight before any Search tap
  (per the unit 011 tab-shift lesson). The page read 2 days
  05:52:12 left and The next wave of invading Zombies will
  arrive in 00:33:26, so the current wave still had about
  half an hour to run at that read.
- Coordinate correction — the crossed-swords button on the
  target card sits at normalized y about 712, not 662:
  taps at 495,662 and 500,657 only animated the button
  area and never opened the deploy panel, while the tap
  at 500,712 opened it at once. The button's press
  animation region read 468,700 to 531,725. Successors
  should tap crossed-swords at about 500,712. The Search
  button dispatches at normalized y 925, as unit 012
  measured.
- Dispatch 1, verified — Search found an unstacked Lv.10
  Invading Zombies target (Guaranteed Reward medal x10,
  book 1.3K, hero EXP 263.0K, iron 268.0K, food 268.0K;
  Suggested Power 670,000, stamina cost 10). The deploy
  panel read Squad 1 25.05M against 670,000, Easy Win,
  march time 00:03:06. March tapped, panel closed, and
  the world map then read March Queues 1 of 4, Go X:951
  Y:765, 00:02:53 remaining, stamina 120 to 110. One
  10-cost march, verified dispatched.
- Parallel attempt, correctly not engaged — a second
  Events-Search cycle (stamina 110, queue 1 of 4, so
  neither stamina nor the queue cap bound it) returned
  not a nearby Lv.10 but a Lv.95 Zombie Boss card:
  Rally Initiator Rewards, Discoverer's Reward, Found by
  [AP3x]blackdragonkalameet, Suggested Power 37,500,000,
  stamina cost 20, timer 01:17:35. That is a rally-class
  boss target, not a nearby Invading Zombies sweep
  target, and Squad 2 (20.92M per unit 006) sits below
  its suggested power, so no rally was started and no
  squad marched on it. The card was closed untouched.
  squads_parallel is therefore 1 in this unit, for this
  stated reason — a Search result of the wrong target
  class — not a march-queue cap and not stamina.
- Control session — the first computer session (cc-103)
  dropped mid-unit with an unavailable-evidence error on
  a wait step; a fresh session (cc-109) reopened, the
  LastWar window reactivated, and the march was still
  verified 1 of 4 there. No input was lost to the drop:
  the dispatched march is server-side and unchanged.
- LOOT badge — no gift badge was visible on the March
  Queues bar while the squad was out (consistent with
  unit 012's note), and no blind tap was made on it.
  The successor should read the badge once the squad
  returns; unit 013's handover lesson applies — a march
  left in flight may or may not leave a LOOT row, so
  check, never assume.
- Coin chests — not pursued in this unit: the 3 owned
  Coin Chest (SSR) are still unlocated in inventory
  (unit 014 finding), and no medal balance was re-read
  (medals carried at 40 from unit 015, unverified here).
  No redemption and no opening were attempted.
- Totals — zombies_killed 0 verified in-unit (one march
  in flight, kill not yet observed), coins_collected 0,
  coin_before 51,194,936, coin_after 51,194,936 carried
  (no coin-moving action after the verified open read),
  medals_before 40 carried, medals_after 40 carried,
  chests_opened 0, squads_parallel 1 (see the boss reason
  above), cleared false (a live target class remains and
  the wave had about 30 minutes to run). Nothing bought,
  no diamonds or money spent, no speedup or stamina item
  burned; the only stamina spend was the one verified
  10-cost march.

## Follow-up for the successor

- First check the March Queues bar and the LOOT badge:
  Squad 1 to X951 Y765 should have returned by the next
  tick; claim its LOOT row (expected 268,000 per the
  later-wave Lv.10 row rate) and re-read the exact coin
  panel before and after.
- Then re-run Search: if it again returns a Lv.95 boss
  instead of a nearby Lv.10, the current wave's nearby
  supply may be exhausted ahead of the next wave (about
  13:45 by the 00:33:26 read at 13:12), in which case
  record that and wait for the wave rather than engaging
  a rally boss.
- The crossed-swords tap is now pinned at about 500,712;
  the deploy panel's March button sits at about 440,783
  for Squad 1.
