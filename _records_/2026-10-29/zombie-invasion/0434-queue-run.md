---
title: Zombie Invasion Execution 2026-10-29 0434 Queue Run
created: 2026-10-29T11:47:00Z
modified: 2026-10-29T11:47:00Z
level: L0
version: 1.0.0
description: Zombie-invasion chain unit 039 - partial, four Lv.10 kills claimed in-unit for 1,072,000 coins, one 50-stamina item opened, one app crash on Esc with clean relaunch, chain continues, successor starts now
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-29
  - source: owner task unit queue design of 2026-10-28
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization, the task unit queue ticker with its 15 minute unit cap and Zombie Invasion continuation chains
  - source: owner instruction of 2026-10-28 - collect the event coins from the task collection icon and maximize coin, dispatch squads in parallel
  - source: owner reminder of 2026-10-28 - open the stamina resource items held in the inventory and use them
  - source: owner decision of 2026-10-28 - redeem event medals for Coin Chests in the event Store and open owned Coin Chests
---

# Zombie Invasion — execution, 2026-10-29 0434 queue unit 039

A single task unit, executed by executor ticker-0434 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-039,
chain zombie-2026-10-28, chain sequence 39, priority 4.
Session window about 04:34 to 04:46 America/Los_Angeles.
Status — partial; the chain continues while the event is
available and zombies remain nearby, so the tracker is
left untouched. All four squads dispatched in this unit
were resolved and claimed inside it, and the march queue
was empty at the close.

## What was observed

- Open — the game was already on the base interior screen,
  coin HUD 96.8M, Total Power 149,351,992, stamina about
  22 at the first deploy read (18 carried from unit 038
  plus regeneration). No different-device dialog appeared.
  The computer session stayed up for the whole unit
  (cc-229); the game itself quit once mid-unit (see
  below) and was relaunched cleanly with state intact.
- Event page — opened from the base via 942,152 and
  landed directly on the Zombie Invasion tab: 1 day
  14:24:36 left, next wave in 00:05:58, so a new wave
  was due about 04:42 and the event is live.
- First Search, fixed-point batch missed — Search at
  375,925 found a Lv.10 card (Suggested Power 670,000),
  but the batched attack tap at 500,750 and March tap
  at 499,750 missed: the crossed-swords button on that
  card sat at 502,598 (grounded), not 750, because the
  card sits higher when its target is farther up the
  map. The taps ended on the base interior under a
  MISSING ITEMS dialog (Advanced Teleporter Owned: 0,
  with Buy buttons for the VIP Store, Alliance Shop and
  Diamond Store). NO Buy button was tapped and nothing
  was bought or teleported; the dialog was closed with
  its X at 846,155. Lesson carried forward: the
  crossed-swords point moves with the card (598, 721,
  732 and 770 all seen this unit) — ground it per card,
  never reuse a fixed point blindly.
- Kill 1, Squad 1 — the same target was re-tapped on
  the map at 450,405, its card re-verified (Lv.10,
  stamina cost 10, despawn 11:04:31, medal x10, iron
  268.0K, food 268.0K), the grounded crossed-swords
  tap at 502,598 opened the deploy panel (Squad 1,
  25.05M Vs 670.00K, Easy Win, Unit Count 2,231 of
  2,231, March 00:02:41, stamina 22), and March at
  499,750 dispatched it: March Queues 1 of 4, Go
  X:829 Y:999.
- Kill 2, Squad 2, parallel — Events, Search, then the
  card grounded and the crossed-swords tap at 500,770
  opened the deploy panel, which had auto-selected
  Squad 2 (Unit Count 2,175, Easy Win, matching unit
  024). March dispatched it: March Queues 2 of 4
  verified, Go X:811 Y:883, stamina 22 to 2.
- Stamina refill BEFORE further dispatch — Inventory
  Special tab, grid dragged up: 50-stamina x611 and
  10-stamina x621 confirmed. The 50 Stamina item at
  405,615 was selected (detail read "50 Stamina -
  Use this item to gain Stamina") and Use moved the
  count 611 to 610. Stamina then read about 52, enough
  for a further round. The 10-stamina count is
  unchanged at 621.
- Back-arrow failure and app crash — the Inventory
  back arrow at 59,983 and 60,980 did not respond to
  background clicks, and an Escape keypress then quit
  the game outright (the known Esc-crash behaviour of
  this iPad app on Mac, already in AGENTS.md — the
  keypress was a mistake and must not be repeated).
  The app was relaunched with open_app into window
  98425 (same 642 by 951 frame at 800,30); all
  server-side state survived — stamina 52, March
  Queues 2 of 4, both squads still out.
- First LOOT claim — on the world map the gift box
  at the right end of the March Queues bar carried a
  red badge 1 (Squad 1 killed, Returning; Squad 2
  still going out). The grounded tap 318,222 opened
  the LOOT panel with exactly two rows (Squad 2 had
  landed by then): Lv.10 X:811 Y:883 and Lv.10
  X:829 Y:999, each medal x10, iron 268.0K, food
  268.0K, coin 268.0K, hero EXP 263.0K. The plain
  blue Claim All button (no price tag) at 499,765
  was tapped; the panel closed and the gift badge
  cleared. Claim verification — HUD after the claim:
  coin 97.4M (from 96.8M), food 218.8M (from
  218.2M), iron 405.0M (from 404.5M) — each up about
  536,000 at HUD rounding, confirming the claim.
  Exact coin panel readings were not available this
  unit: the HUD rounds to 0.1M, so no exact
  coin_before or coin_after is asserted here;
  coins_collected is exact from the LOOT rows.
- Kill 3, Squad 1 reused — Events reopened on the
  Hero Advancement tab after the relaunch (the tab
  bar defaults there on a fresh launch, not to
  Zombie Invasion); the Search tap at 375,925 on
  that page landed on empty bottom area and did
  nothing — no button, no purchase, no stage swap.
  The Zombie tab was then tapped at its grounded
  point 856,124 (an earlier tap at 910,131 had
  missed it, landing off the tab). Search found a
  Lv.10 card; the grounded crossed-swords tap at
  497,721 opened the deploy panel (Squad 1 again,
  home from its short X:990 trip, 2,231 of 2,231,
  Easy Win); March dispatched it: Go X:990 Y:942,
  about 5 seconds out, stamina 53 to 43, March
  Queues 2 of 4 (Squad 2 still Returning).
- Kill 4, Squad 1 reused again — Events stayed on
  the Zombie tab this time; Search found a Lv.10
  card; the grounded crossed-swords tap at 499,732
  opened the deploy panel (Squad 1, home again,
  25.05M Vs 670.00K, Easy Win, 2,231 of 2,231,
  March 00:00:14, stamina 43, Squad 2's tab
  carrying the returning red arrow); March
  dispatched it: Go X:982 Y:966, March Queues 2 of
  4, stamina 43 to 33.
- Second LOOT claim — after a 10 second wait the
  gift badge read 2 and the queue read 1 of 4
  (Squad 1 Returning 00:00:08). The grounded tap
  318,222 opened the LOOT panel with exactly two
  rows: Lv.10 X:982 Y:966 and Lv.10 X:990 Y:942,
  each medal x10, box x4, iron 268.0K, food
  268.0K, coin 268.0K, hero EXP 263.0K. Claim All
  at 499,765 was tapped; the panel closed and the
  badge cleared. Claim verification — HUD after
  the claim: coin 97.9M (from 97.4M), food 219.3M
  (from 218.8M), iron 405.5M (from 405.0M) — each
  up about 536,000 at HUD rounding, confirming
  the claim.
- Stamina and medals — stamina 33 at the close,
  not exhausted, and no further refill was needed.
  Inventory stamina after the unit is 50-stamina
  x610 and 10-stamina x621. Medals were not
  re-read in the Store this unit: medals_before
  1140 carried from unit 038's derived balance (no
  other zombie unit ran between 038 and 039),
  medals_after 1180 derived (1140 plus 40 from
  the four claimed rows).
- Coin chests, NOT redeemed or opened in this unit —
  the unit window was spent on the four dispatches,
  the stamina refill, the crash recovery and the
  two claims, so no Store visit was made. The 4
  owned Coin Chest (SSR) are still unlocated in
  inventory (unit 014 finding, still open),
  3,248,640 coins pending, plus a new redemption
  the successor can make from the 1180 derived
  balance under the maximize-coin decision.
- Totals — zombies_killed 4 claimed in-unit (X:829
  Y:999, X:811 Y:883, X:990 Y:942 and X:982 Y:966),
  coins_collected 1,072,000, coin_before HUD 96.8M,
  coin_after HUD 97.9M, medals_before 1140 carried,
  medals_after 1180 derived, chests_opened 0,
  squads_parallel 2 verified by queue readings
  (Squads 1 and 2 out together at 2 of 4; the
  queue never passed 2 of 4 in this unit because
  the home-cluster marches were seconds long and
  squads came home between dispatches, and the
  refill plus crash recovery broke the dispatch
  run — no game-side cap beyond the known march
  queue cap of 4 was hit), tasks_badge 2 at the
  second claim (1 at the first), cleared false
  (the wave was still running and Search found
  targets at once four times; the successor starts
  now, and the queue was empty at the close).
  Nothing bought with diamonds or money, no
  speedup item burned, no rally started, no
  teleport used, no ally panel action taken. The
  MISSING ITEMS dialog's Buy buttons were not
  touched, and the Hero Advancement page was left
  untouched (its Confirm never tapped, no stage
  swap).

## Follow-up for the successor

- Stamina is 33 at the close with 50-stamina x610
  and 10-stamina x621 in inventory: stamina is NOT
  exhausted, and one 50-stamina item before the
  first dispatch still covers a four-squad round.
- Read medals_before from the Store header (1180
  derived expected before any new kill rows), never
  from the old derived chain alone. With that balance,
  redeeming Coin Chest (SSR) for 160 medals remains
  authorized under the maximize-coin decision, and
  the 4 owned chests still need locating in inventory
  and opening (3,248,640 coins pending).
- Ground the crossed-swords button per card before
  tapping it — its point moves with the card
  (598, 721, 732, 770 seen this unit). A fixed 750
  tap misses on high cards and can surface the
  MISSING ITEMS dialog; close that dialog with its
  X and never touch its Buy buttons.
- After any app relaunch, Events defaults to the
  Hero Advancement tab, not Zombie Invasion — tap
  the Zombie tab at its grounded point (856,124
  this unit) and verify the title before Search.
- Never press Escape in this app — it quits the
  game. Leave the Inventory with its back arrow
  (tap it precisely) or by reopening Events from
  the map; if the back arrow does not respond,
  close and reopen the app rather than pressing
  Escape.
- Claim LOOT rows in the same unit that dispatched
  them, from the kill-area map position via the
  grounded gift-box tap, before any BASE or WORLD
  tap that recentres the map.
