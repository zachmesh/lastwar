---
title: Zombie Invasion Execution 2026-10-28 1254 Queue Run
created: 2026-10-28T19:54:00Z
modified: 2026-10-28T19:54:00Z
level: L0
version: 1.0.0
description: Zombie-invasion chain unit 016 - partial, no march dispatched: Search found a Lv.10 target stacked with a player base, and the crossed-swords tap only cycled a Choose-a-target popup instead of opening the deploy panel, so no squad marched, coins unchanged, cleared false, successor starts now
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-28
  - source: owner task unit queue design of 2026-10-28
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization, the task unit queue ticker with its 15 minute unit cap and Zombie Invasion continuation chains
  - source: owner instruction of 2026-10-28 - collect the event coins from the task collection icon and maximize coin, dispatch squads in parallel
  - source: owner decision of 2026-10-28 - redeem event medals for Coin Chests in the event Store and open owned Coin Chests
---

# Zombie Invasion — execution, 2026-10-28 1254 queue unit 016

A single task unit, executed by executor ticker-1234 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-016,
chain zombie-2026-10-28, chain sequence 16, priority 4.
Session window 12:46 to about 12:54 America/Los_Angeles.
Status — partial; no march was dispatched in this unit, and
the chain continues via its successor starting now.

## What was observed

- Open — coin detail panel read exactly 51,194,936 owned,
  against unit 015's closing 51,203,336 — a decrease of 8,400
  between 09:34 and 12:47 that this unit did not cause (no
  coin-moving action by this unit preceded the read; the
  difference is intervening routine spending, not zombie
  play). Stamina 120 at the open, so stamina was not a
  constraint and no stamina item was opened or needed.
  Diamonds 653 in the top bar. No different-device dialog
  appeared in this unit.
- Event page — Events opened and the Zombie Invasion tab was
  verified by its title on sight before any Search tap (per
  the unit 011 tab-shift lesson). The page read 2 days
  06:10:25 left and The next wave of invading Zombies will
  arrive in 00:51:39, so a fresh wave was about 52 minutes
  out at that read — but the wave was not exhausted: Search
  found a target (see below).
- Target found — Search jumped to the world map and opened a
  Lv.10 Invading Zombies card: Guaranteed Reward medal x10,
  book 1.3K, hero EXP 263.0K, iron 268.0K, food 268.0K;
  Suggested Power 670,000, stamina cost 10, timer
  1h49:41 falling to 1h48:12 across the unit (despawn
  countdown, not march time). The target sits stacked with
  a player base (#2110 [W77] in the stack list).
- Dispatch blocked by the stack — tapping the crossed-swords
  button at norm (498,647) opened a Choose a target popup
  listing #2110 [W77] and Lv.10 Invading Zombies, instead of
  the deploy panel. Tapping the Lv.10 row returned to the
  target card, and tapping crossed-swords again reopened
  the same popup — a loop, twice observed. No squad tab and
  no March button were ever reached, so no march was
  dispatched and no stamina was spent. This is a target
  stacking problem, not a march-queue cap and not a stamina
  problem.
- LOOT badge — not read in this unit: the world-map March
  Queues bar was not located in the closing map views, and
  no blind tap was made on it. The successor should read
  the badge before dispatching.
- Coin chests — not pursued in this unit: the 3 owned Coin
  Chest (SSR) are still unlocated in inventory (unit 014
  finding), and no medal balance was re-read (medals
  carried at 40 from unit 015, unverified here). No
  redemption and no opening were attempted.
- Totals — zombies_killed 0, coins_collected 0,
  coin_before 51,194,936, coin_after 51,194,936 (no
  coin-moving action after the verified read), medals_before
  40 carried, medals_after 40 carried, chests_opened 0,
  squads_parallel 0 (no dispatch was possible for the
  stacked-target reason above, not a game cap),
  cleared false (a live target exists nearby). Nothing
  bought, no diamonds or money spent, no speedup or stamina
  item burned.

## Follow-up for the successor

- Re-run Search from the Events page: a fresh Search may
  land on a different, unstacked Lv.10 target, which the
  batched Events-Search-crossed-swords-March sequence
  handles cleanly. If the same stacked target returns, try
  tapping the helicopter target on the map directly, or
  zooming the map to separate the stack, before falling
  back to waiting for the next wave.
- Read the LOOT badge and the March Queues bar first, then
  dispatch in parallel to the 4-squad cap where the game
  allows it.
