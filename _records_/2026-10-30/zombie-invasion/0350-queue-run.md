---
title: Zombie invasion queue run
created: 2026-10-30T10:50:00Z
modified: 2026-10-30T10:50:00Z
version: 1.0.0
description: Queue unit zombie-invasion-zombie-2026-10-28-055 execution
status: done
---

# Zombie invasion - 2026-10-30 about 03:41 to 03:50 PDT queue run

Unit: zombie-invasion-zombie-2026-10-28-055, executor
ticker-0334, chain zombie-2026-10-28 seq 55, computer
sessions cc-439 then cc-440 (cc-439 dropped before the
zombie unit; cc-440 re-selected LastWar, no game state
lost).

## Two Lv.10 kills, sequential, loot claimed in-unit

- Events page verified by title Zombie Invasion on
  opening (event timer 15:17:58 left, next wave in
  00:39:27 at entry). Coin HUD 133.6M at entry.
- First dispatch, batched sequence failed silently -
  a batched sequence (Events, Search with a 2 second
  pause after Search, crossed-swords, March) left
  stamina unchanged and no march queue, the same
  class of silent batch failure as unit 053. The
  map was left centred on X:985 Y:947 with no card
  open.
- First kill, single-step dispatch - Events reopened
  directly on the Zombie Invasion page, Search found
  a Lv.10 Invading Zombies card (Guaranteed medal
  x10, EXP 263.0K, iron 268.0K, food 268.0K, stamina
  cost 10, despawn 11:58:52), crossed-swords at
  499,736 opened the deploy panel (Squad 1, 25.05M
  Vs 670.00K, Easy Win, Unit Count 2,231 of 2,231,
  march 00:00:06, stamina 69 in the panel), March at
  498,766 dispatched at once. Verified: March
  Queues 1/4, Go X:985 Y:951, stamina 69 to 59.
- Parallel attempt, wrong card, aborted untouched -
  an immediate batched second dispatch landed on a
  Lv.95 Zombie Boss card (Found by [AP3x]MesutCLK
  Apex, Suggested Power 37,500,000, stamina cost
  20, despawn 00:47:46) instead of an Invading
  Zombies target, the same tab-shift class as units
  011 and 048. The rally-flag button on that card
  was NOT tapped, no boss march was sent, stamina
  stayed 59, and the card was closed by tapping
  blank map. No boss, rally or other task type was
  touched.
- Second kill, single-step dispatch - Events
  reopened on the Zombie Invasion page, Search found
  a second Lv.10 card (despawn 11:57:06), swords and
  March as above (Squad 1 again, auto-selected after
  its return). Verified: March Queues 1/4, Go
  X:982 Y:951, stamina 59 to 49.
- squads_parallel is therefore 1, sequential, not
  the march-queue cap of 4: both round trips were
  about 6 seconds out plus return, so the first
  squad was home before the second dispatch landed,
  as in units 049 and 053. The parallel attempt
  failed on the wrong-card batch, not on a cap.
- LOOT claim - after the second return the gift
  badge read 2. The grounded tap at 332,250 opened
  the LOOT panel with exactly this unit's 2 rows,
  each coin 268.0K, medal x10, iron 268.0K, food
  268.0K, hero EXP 263.0K: X:982 Y:951 and
  X:985 Y:951. Claim All (plain blue, no price tag)
  at 499,765 tapped in-unit; panel closed, badge
  cleared, 536,000 coins collected by row lines.
  Claim verification - HUD after the claim: coin
  134.1M (from 133.6M), food 271.3M (from 270.8M),
  iron 463.4M (from 462.8M), consistent with plus
  536,000 at HUD rounding. No exact coin-panel
  reading was taken, so no exact coin_before or
  coin_after is reported.

## Store redemption - SSR Coin Chest redeemed, live-measured

- Store header read live at 3670 medals after the
  claims and before any redemption. That is 560
  above unit 054's 3110 close, reconciled here
  rather than left as drift: plus 20 from this
  unit's 2 kills, plus 540 from the Zombie Invasion
  Intel Reward batch claimed in the 03:14 mail unit.
  No derived medal total is reported beyond that
  reconciliation.
- The 160-medal Coin Chest (SSR) row was found after
  scrolling (Limit 96, as unit 054 left it). Its
  tooltip read Coin Chest (SSR), Owned 6, yield
  812.16K coins at Base Lv.30. A first Redeem tap
  at the grounded point 741,492 did nothing - it
  closed the tooltip instead of opening the dialog,
  a new instance of the Redeem bottleneck. A second
  plain single click at the same point opened the
  BUY ITEMS dialog at once (Coin Chest (SSR) x1,
  Unit Price 160, Total Price 160).
- Buy at the visually grounded centre 497,677
  succeeded at once (not the 640 top-edge point
  unit 054 warned against).
- Redemption verified live: CONGRATULATIONS banner
  with Coin Chest x1, medal balance 3670 to 3510
  (minus exactly 160), SSR row Limit 96 to 95.
  No diamonds and no money spent - a
  medal-denominated redemption under the owner's
  2026-10-28 maximize-coin decision.
- Owned Coin Chest (SSR) count after the redemption
  was not re-read in a tooltip, and the location of
  the owned chests in the inventory is still unknown,
  so no chest was opened in this unit - that item
  stays open for the successor, as in units 048, 049,
  052, 053 and 054. The Store panel was still open
  at the unit close; that is harmless - the
  successor reopens Events directly.

## Outcome

Done (unit work completed inside the cap): 2 kills at
squads_parallel 1 (sequential, short round trips),
loot 536,000 coins claimed in-unit, 1 SSR Coin Chest
redeemed for 160 medals (medals 3670 to 3510
live-measured). Nearby zombies not cleared - Search
found targets twice in this wave and the next-wave
countdown read about 54 minutes at the Store close,
so cleared is false and the successor starts now.
Stamina 49 at close; stamina inventory was not
re-checked because stamina never bound (49 left, no
refill needed), so no 1 hour delay applies.
