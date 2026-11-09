---
title: Zombie Invasion Execution 2026-10-28 0435 Queue Run
created: 2026-10-28T11:52:00Z
modified: 2026-10-28T11:52:00Z
level: L0
version: 0.1.0
description: Zombie-invasion chain unit 006 - caught the 1142Z wave, one Lv.10 kill verified by its LOOT row at X980 Y925, Claim All collected 268000 coins exactly (coin 35488573 to 35756573), two further marches failed with the target location has changed toast so parallel dispatch could not be achieved, a fourth march was in flight at the unit cap and is handed to unit 007
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-28
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization, the task unit queue ticker with its 15 minute unit cap and Zombie Invasion continuation chains
  - source: owner instruction of 2026-10-28 - dispatch multiple teams in parallel during zombie invasion and collect the event coins from the task collection icon
  - source: owner decision of 2026-10-28 - maximize coin, redeem medals for Coin Chests in the event Store and open owned Coin Chests
---

# Zombie Invasion — execution, 2026-10-28 04:35 queue unit 006

A single task unit, executed by executor ticker-0434 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-006,
chain zombie-2026-10-28, chain sequence 6, priority 4. Session
window 04:35 to about 04:50 America/Los_Angeles. The unit was
seeded by this tick because unit 005 had finished without a
successor in the pool; the regular inbox units are all staged
for 06:03 and later, so this zombie unit was the only due work.

## What was observed

- Event live throughout - the Zombie Invasion page read 2 days
  14 hours 23 minutes remaining at the open, the next-wave
  countdown about 5 minutes. The wave arrived on schedule
  (countdown reset to about 58 minutes at 04:43) and Search
  found Lv.10 Invading Zombies targets again.
- Coin before - 35,488,573 exact, held from unit 005's closing
  panel read; no coin-moving action preceded this unit's own
  claim. Diamonds 653 throughout.
- Kill 1 (verified) - Search, Squad 1 (25.05M against
  670,000, Easy Win, 30 second march), stamina 109 to about
  99 on the march. The kill registered as the single row in
  the LOOT panel - Lv.10 Invading Zombies, X980 Y925,
  stamina -10, medal x10, box x4, iron 268.0K, food 268.0K,
  coin 268.0K, EXP 263.0K.
- Collection - the LOOT gift icon at the right end of the
  March Queues bar carried badge 1 (tasks_badge 1). Its
  Claim All is plain blue with no price tag; tapped once.
  Coin panel after - Owned 35,756,573 exactly. Coins
  collected 268,000, matching the row's coin line to the
  unit. Medal balance 70 before (Store read at the open);
  the claimed row pays medal x10, so medals_after 80 by the
  row evidence (no second Store read inside the cap).
- Parallel dispatch - attempted, not achieved, and the
  blocker is now named. Two further marches (Squad 2 on the
  second target, then a batched Squad 1 / Squad 2 sequence
  on the third) each failed at the March tap with the toast
  "The target location has changed. Please try again." -
  no stamina was charged on the failed marches (stamina
  read 100 after them, March Queues 0 of 4). Targets from
  Search appear to move or be taken within tens of seconds
  in this wave, so a slow dispatch loses them; the march
  queue cap itself is still unmeasured because a second
  squad never got marching. squads_parallel 1.
- Squad 2 recon - its deploy panel reads 20.92M power,
  five Lv.150 heroes, Unit Count 2,175 of 2,175, march
  57 seconds on the second target; the versus line read
  Unknown / Evenly Matched against the same Lv.10 card
  that Squad 1 read as 670,000 / Easy Win - recorded as
  seen, not explained.
- In flight at the cap - a fourth batched attempt (Events,
  Search, attack, March with Squad 1) dispatched cleanly
  with no failure toast, march timer about 00:01:22 toward
  about X905 Y465. Its outcome is NOT counted here - unit
  007 must check the LOOT badge and March Queues first and
  count the kill there if its row appears.
- Store and chests - medal balance 70 at the open is below
  the confirmed Coin Chest (SR) price of 160, so no
  redemption; the 2 owned Coin Chest (SR) were not located
  or opened in this unit and stay a follow-up. chests_opened
  0. Stamina spent 10 on the verified kill (plus 10 charged
  on the in-flight march, to be settled by unit 007). No
  refill used, nothing bought, no diamond spent.
- cleared is false - the new wave is live and targets
  remain; the successor unit was enqueued to start now.
  The session dropped once during the wave wait and was
  reopened (session cc-51) with all state intact; no
  different-device dialog appeared.
