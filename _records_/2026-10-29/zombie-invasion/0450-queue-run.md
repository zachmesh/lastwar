---
title: Zombie Invasion Execution 2026-10-29 0450 Queue Run
created: 2026-10-29T12:05:00Z
modified: 2026-10-29T12:05:00Z
level: L0
version: 1.0.0
description: Zombie-invasion chain unit 041 - partial, one 50-stamina item opened, two Lv.10 kills claimed in-unit for 536,000 coins, squads_parallel 2 verified, back-arrow point corrected by grounding, chain continues, successor starts now
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-29
  - source: owner task unit queue design of 2026-10-28
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization, the task unit queue ticker with its 15 minute unit cap and Zombie Invasion continuation chains
  - source: owner instruction of 2026-10-28 - collect the event coins from the task collection icon and maximize coin, dispatch squads in parallel
  - source: owner reminder of 2026-10-28 - open the stamina resource items held in the inventory and use them
  - source: owner decision of 2026-10-28 - redeem event medals for Coin Chests in the event Store and open owned Coin Chests
---

# Zombie Invasion — execution, 2026-10-29 0450 queue unit 041

A single task unit, executed by executor ticker-0434 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-041,
chain zombie-2026-10-28, chain sequence 41, priority 4.
Session window about 04:50 to 05:02 America/Los_Angeles.
Status — partial; the chain continues while the event is
available and zombies remain nearby, so the tracker is
left untouched. Both squads dispatched in this unit were
resolved and claimed inside it, and the march queue was
empty at the close.

## What was observed

- Open — the game was on the world map (left over from
  unit 040), coin HUD 98.4M, Total Power 149,351,992,
  stamina 14 carried from unit 040. No
  different-device dialog appeared. Computer session
  cc-233 (replacing timed-out cc-229) stayed up for
  the whole unit.
- Stamina refill BEFORE the first dispatch — Inventory
  Special tab, grid dragged up: the 50 Stamina item
  at the grounded point 406,651 was selected (detail
  read "50 Stamina - Use this item to gain
  Stamina") and Use was tapped. The refill is
  confirmed by the deploy read below (stamina 64),
  not by a re-read count: inventory 50-stamina is
  therefore 609 derived (610 minus 1), 10-stamina
  x621 unchanged.
- Back-arrow point corrected — the Inventory back
  arrow's grounded point is 60,940, and a tap there
  exited to the world map at once. The unit 039
  taps at 59,983 and 60,980 had landed below the
  button — the same systematic offset seen with the
  crossed-swords button (screenshot-pixel estimates
  read low against grounded points). Ground the
  button; do not reuse the 983 estimate.
- Kill 1, Squad 1 — Events stayed on the Zombie
  Invasion tab; Search at 375,925 found a Lv.10
  card (Suggested Power 670,000); the
  crossed-swords tap at 500,765 on the
  identical-layout card opened the deploy panel
  (Squad 1, 25.05M Vs 670.00K, Easy Win, Unit Count
  2,231 of 2,231, stamina 64 — refill confirmed);
  March dispatched it: March Queues 1 of 4, about
  21 seconds out, stamina 64 to 54.
- Kill 2, Squad 2, parallel — the batched sequence
  (Events, Search, crossed-swords at 500,765)
  opened the deploy panel, which had auto-selected
  Squad 2 (Unit Count 2,175, Easy Win); March
  dispatched it: March Queues 2 of 4 verified,
  stamina 54 to 44.
- LOOT claim — after a 30 second wait the gift
  badge read 2 and the queue read 1 of 4 (one
  squad Returning). The grounded tap 318,222
  opened the LOOT panel with exactly two rows:
  Lv.10 X:994 Y:978 and Lv.10 X:984 Y:977, each
  medal x10, box x4, iron 268.0K, food 268.0K,
  coin 268.0K, hero EXP 263.0K. The plain blue
  Claim All button (no price tag) at 499,765 was
  tapped; the panel closed and the gift badge
  cleared. Claim verification — HUD after the
  claim: coin 99.0M (from 98.4M), food 220.4M
  (from 219.8M), iron 406.6M (from 406.1M) — each
  up about 536,000 at HUD rounding, confirming
  the claim. Exact coin panel readings were not
  available this unit: the HUD rounds to 0.1M, so
  no exact coin_before or coin_after is asserted
  here; coins_collected is exact from the LOOT
  rows.
- Stamina and medals — stamina 45 at the close
  (64 minus 20 plus about 1 regenerated), not
  exhausted, and no further refill was needed.
  Inventory stamina after the unit is 50-stamina
  x609 derived and 10-stamina x621. Medals were
  not re-read in the Store this unit: medals_before
  1200 carried from unit 040's derived balance (no
  other zombie unit ran between 040 and 041),
  medals_after 1220 derived (1200 plus 20 from
  the two claimed rows).
- Coin chests, NOT redeemed or opened in this unit —
  the unit window was spent on the refill and the
  two dispatches and claims, so no Store visit was
  made. The 4 owned Coin Chest (SSR) are still
  unlocated in inventory (unit 014 finding, still
  open), 3,248,640 coins pending, plus a new
  redemption the successor can make from the 1220
  derived balance under the maximize-coin decision.
- Totals — zombies_killed 2 claimed in-unit (X:984
  Y:977 and X:994 Y:978), coins_collected 536,000,
  coin_before HUD 98.4M, coin_after HUD 99.0M,
  medals_before 1200 carried, medals_after 1220
  derived, chests_opened 0, squads_parallel 2
  verified by the 2 of 4 queue reading, tasks_badge
  2, cleared false (Search found targets at once
  twice and the wave was still running; the
  successor starts now, and the queue was empty at
  the close). Nothing bought with diamonds or
  money, no speedup item burned, no rally started,
  no teleport used, no ally panel action taken.

## Follow-up for the successor

- Stamina is 45 at the close with 50-stamina x609
  derived and 10-stamina x621 in inventory:
  stamina is NOT exhausted; a further refill is
  not needed for the next two-squad round, but
  one 50-stamina item covers a four-squad round.
- Read medals_before from the Store header (1220
  derived expected before any new kill rows), never
  from the old derived chain alone. With that balance,
  redeeming Coin Chest (SSR) for 160 medals remains
  authorized under the maximize-coin decision, and
  the 4 owned chests still need locating in inventory
  and opening (3,248,640 coins pending).
- Ground the crossed-swords button per card before
  tapping it (765 on both cards this unit), and
  ground the Inventory back arrow (60,940) rather
  than estimating it from the screenshot.
- Claim LOOT rows in the same unit that dispatched
  them, from the kill-area map position via the
  grounded gift-box tap, before any BASE or WORLD
  tap that recentres the map.
