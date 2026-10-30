---
title: Zombie invasion queue run
created: 2026-10-30T08:47:00Z
modified: 2026-10-30T08:47:00Z
version: 1.0.0
description: Queue unit zombie-invasion-zombie-2026-10-28-054 execution
status: done
---

# Zombie invasion - 2026-10-30 01:34 to 01:47 PDT queue run

Unit: zombie-invasion-zombie-2026-10-28-054, executor
ticker-0134, chain zombie-2026-10-28 seq 54, computer
sessions cc-423 then cc-424 (cc-423 dropped during a
60 second wait with no session open; cc-424 re-selected
LastWar, no game state lost).

## Four Lv.10 kills at the march-queue cap, loot claimed in-unit

- Events page verified by title Zombie Invasion on first
  opening (event timer 17:21:58 left, next wave in
  00:03:26 at entry). Coin HUD 124.1M at entry.
- Stamina refill BEFORE the first dispatch - stamina
  read 8 at entry, below one 10-cost march. Inventory
  opened with a tap at 900,870 (earlier taps at 875,825
  and 880,840 did not open it). Inventory Special tab,
  grid dragged up: 50-stamina x611 and 10-stamina x624
  confirmed live. One 50 Stamina item opened (selected
  at the visually grounded point 598,455, detail read
  "50 Stamina - Use this item to gain Stamina", Use tap
  at 511,953, toast "you've acquired 50 Stamina").
  Inventory after the refill is 50-stamina x610 derived
  and 10-stamina x624 unchanged. Back arrow at 60,940
  exited to the world map at once.
- First dispatch, stale target - single-step dispatch
  (Search 358,941, crossed-swords 499,753, March
  500,762) opened the deploy panel (Squad 1, 25.05M Vs
  670.00K, Easy Win, Unit Count 2,231 of 2,231, stamina
  59 - refill confirmed), but March answered with the
  toast "The target location has changed. Please try
  again." and charged no stamina, as in units 006, 030
  and 031. Stamina stayed 59, March Queues 0 of 4.
- Batched dispatches, all four at the cap - a batched
  sequence (Events 942,152, Search 358,941 with a
  2 second pause after Search so the jump animation
  produces the card, crossed-swords 499,753, March
  500,762) dispatched four squads in succession, each
  verified by March Queues count and stamina drop:
  - Kill 1: X:913 Y:944, March Queues 1/4, stamina
    59 to 49.
  - Kill 2: X:894 Y:953, March Queues 2/4, stamina
    49 to 39.
  - Kill 3: X:894 Y:934, March Queues 3/4, stamina
    39 to 29.
  - Kill 4: X:862 Y:942, March Queues 4/4, stamina
    29 to 19.
  squads_parallel is therefore 4, the march-queue cap,
  the second cap-4 run in this chain after unit 052.
  The batched sequence with a pause after Search is
  the working dispatch method; the 1.5 second batch
  without a pause in unit 053 failed, and a slow
  single-step dispatch loses a wave-end target to
  the stale-target failure above.
- LOOT claim - after the fourth arrival the gift badge
  read 4 (it had read 3 while two squads were still
  Returning, so a LOOT row is created on arrival, not
  on homecoming). The grounded tap 318,242 opened the
  LOOT panel with exactly this unit's 4 rows, each
  coin 268.0K, medal x10, iron 268.0K, food 268.0K,
  hero EXP 263.0K: X:862 Y:942, X:894 Y:934,
  X:894 Y:953, X:913 Y:944. Claim All (plain blue,
  no price tag) at 499,765 tapped in-unit; panel
  closed, badge cleared, 1,072,000 coins collected
  by row lines. Claim verification - HUD after the
  claim: coin 125.2M (from 124.1M), food 267.1M
  (from 266.0M), iron 450.8M (from 449.7M),
  consistent with plus 1,072,000 at HUD rounding.
  No exact coin-panel reading was taken, so no exact
  coin_before or coin_after is reported. Stamina
  closed at 20 at the claim (19 after the fourth
  march plus regen).

## Store redemption - SSR Coin Chest redeemed, live-measured

- Store header read live at 3270 medals after the
  claims and before any redemption - a live-measured
  balance, not a derived total (unit 052 closed at
  3210; the 3270 live read is 20 above the 3250 a
  simple 3210 plus 40 would give, the same class of
  derived-total drift units 041 to 043 already proved
  wrong, so no derived medal total is reported).
- The 160-medal Coin Chest (SSR) row was found after
  scrolling the Store list (Limit 97, as unit 052
  left it). Its gold-coin chest icon and Limit 97
  match unit 052's row; the BUY ITEMS dialog named
  it Coin Chest (SSR) x1, Unit Price 160, Total
  Price 160, before any Buy tap, confirming the row.
- Redeem input route, new evidence: a plain single
  click on Redeem at the grounded point 741,420
  opened the BUY ITEMS dialog at once, as in unit
  052. A first Buy tap at 500,640 did NOT register
  (dialog stayed open, balance stayed 3270 - that
  point hits the button's top edge); a tap at the
  visually grounded Buy centre 499,689 succeeded.
  The Buy-step bottleneck therefore varies by tap
  point as well as by session - ground the Buy
  centre, never reuse the 640 estimate.
- Redemption verified live: CONGRATULATIONS banner
  with Coin Chest x1, medal balance 3270 to 3110
  (minus exactly 160), SSR row Limit 97 to 96.
  No diamonds and no money spent - a
  medal-denominated redemption under the owner's
  2026-10-28 maximize-coin decision.
- Owned Coin Chest (SSR) count after the redemption
  was not re-read in a tooltip, and the location of
  the owned chests in the inventory is still unknown,
  so no chest was opened in this unit - that item
  stays open for the successor, as in units 048, 049,
  052 and 053. The Store panel was still open at the
  unit close (a tap at 820,135 cleared the banner
  overlay and left the Store list showing Limit 96);
  that is harmless - the successor reopens Events
  directly.

## Outcome

Done (unit work completed inside the cap): 4 kills at
squads_parallel 4, loot 1,072,000 coins claimed
in-unit, 1 SSR Coin Chest redeemed for 160 medals
(medals 3270 to 3110 live-measured). Nearby zombies
not cleared - Search found targets four times in
this wave and a fresh wave arrived during the unit
(next-wave countdown reset to about 57 minutes at
the Store close, event timer 17:16:10), so cleared
is false and the successor starts now. Stamina 20
at close with 50-stamina x610 derived and
10-stamina x624 in inventory; stamina is not
exhausted, so no 1 hour delay applies.
