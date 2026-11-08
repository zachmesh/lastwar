---
title: Zombie Invasion Execution 2026-10-28 2145 Queue Run
created: 2026-10-29T04:45:00Z
modified: 2026-10-29T04:45:00Z
level: L0
version: 1.0.0
description: Zombie-invasion chain unit 029 - partial, two Lv.10 kills claimed for 536,000 coins, stamina item opened, chain continues, successor starts now
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-28
  - source: owner task unit queue design of 2026-10-28
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization, the task unit queue ticker with its 15 minute unit cap and Zombie Invasion continuation chains
  - source: owner instruction of 2026-10-28 - collect the event coins from the task collection icon and maximize coin, dispatch squads in parallel
  - source: owner reminder of 2026-10-28 - open the stamina resource items held in the inventory and use them
  - source: owner decision of 2026-10-28 - redeem event medals for Coin Chests in the event Store and open owned Coin Chests
---

# Zombie Invasion — execution, 2026-10-28 2145 queue unit 029

A single task unit, executed by executor ticker-2134 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-029,
chain zombie-2026-10-28, chain sequence 29, priority 4.
Session window about 21:34 to 21:45 America/Los_Angeles.
Status — partial; the chain continues while the event is
available and the new wave is still running, so the tracker
is left untouched. Both squads dispatched in this unit were
resolved and claimed inside it.

## What was observed

- Open — the game was already on the base interior screen,
  coin HUD 74.4M, Total Power 149,351,992, stamina 12.
  No different-device dialog appeared. The computer session
  dropped once during a 90 second wave wait (cc-183 ended,
  cc-184 opened); each reopening found the Last War
  window 78525 with state intact.
- Stamina inventory, CHECKED as the successor follow-up
  required — Inventory Resources tab shows coal, diamonds,
  food, iron and coin items and no stamina item; one
  Resources item was tapped to verify and read "10
  Diamonds" (count 23), which is NOT stamina and was NOT
  used. The Special tab holds the stamina items, found by
  scrolling: a lightning-bolt item labelled 50 with count
  612, and a lightning-bolt item labelled 10 with count
  613. Recorded here so the next unit goes straight to
  Special: 50-stamina x612, 10-stamina x613 at this
  unit's check.
- Stamina refill — one 10 Stamina item opened (Use tap,
  toast "you've acquired 10 Stamina", count 613 to 612).
  Base HUD stamina then read 23 (12 plus 10 plus about 1
  regenerated). No diamond spent, no speedup burned.
- Events page — opened from the base interior via
  942,152, landing directly on the Zombie Invasion tab
  (title verified on sight). At the open the page read
  1 day 21:20:09 left, next wave in 00:01:26.
- Old wave exhausted — the first Search answered
  "Monsters not found nearby. Try again later." After a
  90 second wait the new wave's Search found a Lv.10
  Invading Zombies target at once (Suggested Power
  670,000, stamina cost 10, Guaranteed Reward medal x10,
  book 1.3K, hero EXP 263.0K, iron 268.0K, food 268.0K).
- Kill 1, Squad 1 — crossed swords at 500,712, March at
  the grounded point 502,744. March Queues read 1/4.
  The target was a home-cluster pile: the squad was
  already Returning (00:00:04) on the next screenshot,
  with a Defeat banner on the target. Stamina 23 to 13.
- Kill 2, Squad 2 — immediately after, a batched
  sequence (Events, Search, crossed swords, March)
  dispatched the second squad to X:982 Y:964, March
  Queues 1/4 at the read (Squad 1 already back).
  Stamina 13 to 4. By elimination Squad 1's kill is the
  X:987 Y:950 LOOT row below. squads_parallel is
  recorded as 1, not 2: no 2/4 reading was ever
  observed, because the home-cluster marches resolve in
  seconds and Squad 1 was already on its return leg
  before Squad 2's Search sequence finished. This is a
  march-duration limit on these targets, not the queue
  cap of 4 and not stamina (23 stamina covered two
  marches).
- Returns and LOOT claim — after the wait, March
  Queues read 0/4 with both squads back, and the gift
  box at the right end of the March Queues bar
  carried a red badge 2. The pinned tap 317,233
  opened the LOOT panel from the kill-area map
  position. It held exactly two rows, both from this
  unit: Lv.10 X:982 Y:964 (medal x10, crate x1, iron
  268.0K, food 268.0K, coin 268.0K, hero EXP 263.0K)
  and Lv.10 X:987 Y:950 (medal x10, crate x4, same
  268.0K lines). The plain blue Claim All button
  (no price tag) at 499,765 was tapped; the panel
  closed and the gift badge cleared.
- Claim verification — HUD after the claim: coin
  75.0M (from 74.4M), food 196.1M (from 195.6M),
  iron 377.8M (from 377.2M) — each up about
  536,000 at HUD rounding, confirming the claim.
  Coin_before 74,499,886 carried from unit 028,
  coin_after 75,035,886 derived (74,499,886 plus
  536,000).
- Stamina and medals — stamina 4 at the close.
  Medals carried at 860 from unit 028's derived
  balance; the two claimed rows paid medal x10 each,
  so medals_after is 880 derived (the Store balance
  was not re-read this unit).
- Coin chests, NOT redeemed or opened in this unit
  — the unit window was spent on the stamina search
  and the wave wait, so no Store visit was made. The
  4 owned Coin Chest (SSR) are still unlocated in
  inventory (unit 014 finding, still open),
  3,248,640 coins pending, plus a new redemption
  the successor can make from the 880 derived
  balance under the maximize-coin decision.
- Totals — zombies_killed 2 claimed in-unit (X:987
  Y:950 and X:982 Y:964), coins_collected 536,000,
  coin_before 74,499,886 carried, coin_after
  75,035,886 derived, medals_before 860 carried,
  medals_after 880 derived, chests_opened 0,
  squads_parallel 1 for the march-duration reason
  above, tasks_badge 2, cleared false (the new wave
  had just arrived and Search found targets at once
  twice; the successor starts now). Nothing bought
  with diamonds or money, no speedup item burned, no
  rally started, no ally panel action taken.

## Follow-up for the successor

- Stamina items live in the Inventory Special tab, not
  Resources: 50-stamina x612, 10-stamina x612 after
  this unit's use. Open from Special directly; do not
  mistake the Resources red-gem "10 Diamonds" items
  for stamina.
- Read medals_before from the Store header (880
  derived expected before any new kill rows), never
  from the old derived chain alone. With that
  balance, redeeming Coin Chest (SSR) for 160 medals
  remains authorized under the maximize-coin
  decision, and the 4 owned chests still need
  locating in inventory and opening (3,248,640
  coins pending).
- Claim LOOT rows in the same unit that dispatched
  them, from the kill-area map position via the
  pinned 317,233 gift-box tap, before any BASE or
  WORLD tap that recentres the map.
