---
title: Zombie invasion queue run
created: 2026-10-30T07:44:00Z
modified: 2026-10-30T07:44:00Z
version: 1.0.0
description: Queue unit zombie-invasion-zombie-2026-10-28-052 execution
status: done
---

# Zombie invasion - 2026-10-30 00:34 to 00:44 PDT queue run

Unit: zombie-invasion-zombie-2026-10-28-052, executor
ticker-0034, chain zombie-2026-10-28 seq 52, computer
session cc-419.

## Four Lv.10 kills at the march-queue cap, loot claimed in-unit

- Events page verified by title Zombie Invasion on first
  opening (event timer 18:24:07 left, next wave in
  00:05:35 at entry). No tab-bar navigation was needed
  on any dispatch in this unit - Events reopened
  directly on the Zombie Invasion page each time.
- Four batched dispatches (Search 358,941, crossed-swords
  499,753, March 500,759, no screenshot reads in
  between), each verified by March Queues count and
  stamina drop:
  - Kill 1: X:887 Y:926, March Queues 1/4, stamina
    56 to 46.
  - Kill 2: X:877 Y:910, March Queues 2/4, stamina
    46 to 36.
  - Kill 3: X:874 Y:915, March Queues 3/4, stamina
    36 to 26.
  - Kill 4: X:892 Y:880, March Queues 4/4, stamina
    26 to 16.
  squads_parallel is therefore 4, the march-queue cap -
  the first time this chain has run all four squads at
  once. Stamina closed at 17 after regen, so no stamina
  item was opened and no backpack stamina inventory
  check was needed; stamina never bound this unit.
- All four squads verified Returning before the loot
  claim. The gift-box badge read 4, and the LOOT panel
  held exactly this unit's 4 rows, each coin 268.0K,
  medal x10, iron 268.0K, food 268.0K, hero EXP 263.0K:
  X:892 Y:880, X:874 Y:915, X:877 Y:910, X:887 Y:926.
  Claim All (plain blue, no price tag) tapped in-unit;
  panel closed, badge cleared, 1,072,000 coins collected
  by row lines.
- Coin HUD read 122.5M at base entry and 123.6M after
  the claim, consistent with plus 1,072,000 (food
  264.4M to 265.5M and iron 448.1M to 449.2M moved by
  the same four rows). No exact coin-panel reading was
  taken, so no exact coin_before/coin_after is reported.

## Store redemption breakthrough - SSR Coin Chest redeemed

- Store header read live at 3370 medals before any
  redemption - a live-measured balance, not a derived
  total.
- The 160-medal Coin Chest (SSR) row was found again
  after scrolling the Store list (Limit 98), resolving
  unit 047's missing-row question: the row exists and
  its position shifts with scroll, so a first-screen
  scan alone misses it. Its tooltip read Coin Chest
  (SSR), Owned 4, yield 812.16K coins at Base Lv.30.
  The 480-medal Limit 20 row (Coin Chest (UR) per
  unit 047) was also visible on the same screen.
- Redeem input route, new evidence: a 1-second
  long-press on Redeem did nothing this time (unit 047's
  long-press had opened the dialog), while a plain
  single click on Redeem opened the BUY ITEMS dialog
  at once - Coin Chest (SSR) x1, Unit Price 160,
  Total Price 160. A plain single click on Buy then
  succeeded, where unit 047's Buy step had failed by
  single tap, long-press and double-click in background
  input. The Buy-step bottleneck from unit 047 is
  therefore broken in this session by plain single
  clicks; input-route behaviour varies between
  sessions, so the next redemption should still verify
  balance and Owned count rather than assume success.
- Redemption verified live: CONGRATULATIONS banner with
  Coin Chest x1, medal balance 3370 to 3210 (minus
  exactly 160), SSR row Limit 98 to 97. No diamonds
  and no money spent - a medal-denominated redemption
  under the owner's 2026-10-28 maximize-coin decision.
- Owned Coin Chest (SSR) count after the redemption
  was not re-read in a tooltip (it read Owned 4 before
  the redemption); the location of the owned chests in
  the inventory is still unknown, so no chest was
  opened in this unit - that item stays open for the
  successor.

## Outcome

Done (unit work completed inside the cap): 4 kills at
squads_parallel 4, loot 1,072,000 coins claimed
in-unit, 1 SSR Coin Chest redeemed for 160 medals
(medals 3370 to 3210 live-measured). Nearby zombies
not cleared - a fresh wave arrived during the unit
(next-wave countdown 00:59:34 at Store close), so
cleared is false and the successor starts now.
