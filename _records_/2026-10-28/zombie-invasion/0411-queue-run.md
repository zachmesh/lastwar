---
title: Zombie Invasion Execution 2026-10-28 0411 Queue Run
created: 2026-10-28T11:21:00Z
modified: 2026-10-28T11:21:00Z
level: L0
version: 0.1.0
description: Zombie-invasion chain unit 005 - wave exhausted (Monsters not found nearby, next wave about 1144Z), no targets to dispatch so parallel play was impossible for lack of targets, Store recon confirmed the Coin Chest (SR) price at 160 medals against a balance of 70, no kills, no collection, no spend
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-28
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization, the task unit queue ticker with its 15 minute unit cap and Zombie Invasion continuation chains
  - source: owner instruction of 2026-10-28 - dispatch multiple teams in parallel during zombie invasion, enforced from unit 005 onward
---

# Zombie Invasion — execution, 2026-10-28 04:11 queue unit 005

A single task unit, executed by executor parallel-exec-005 under
the task unit queue. Unit zombie-invasion-zombie-2026-10-28-005,
chain zombie-2026-10-28, chain sequence 5, priority 4. Session
window 04:11 to about 04:19 America/Los_Angeles. This unit was
dispatched with parallel dispatch as its priority, after units
001 to 004 recorded squads_parallel 1.

## What was observed

- The game stood open on the base with the COIN panel open,
  left by the earlier units. The panel read Owned 35,488,573
  exactly - coin_before 35488573, unchanged from unit 003's
  coin_after. Diamonds 653, stamina 103 at the open.
- The Zombie Invasion event page read 2 days 14 hours 47
  minutes remaining; the next-wave countdown read about 28
  minutes.
- Search answered with the toast "Monsters not found nearby.
  Try again later." - the current wave is exhausted around
  the base. Next wave at about 11:44Z by the countdown read
  at 11:16Z. No target existed to dispatch any squad on, so
  parallel dispatch was impossible in this unit for lack of
  targets - that is not a game cap, and the march queue cap
  remains unmeasured. squads_parallel 0, zombies_killed 0,
  stamina spent 0.
- Event Store recon - medal balance 70. The Coin Chest (SR)
  row reads price 160 medals, Limit 100 - the exact price is
  now confirmed (round 1 read it as about 150). Coin Chest
  (SSR) reads 480 medals, Limit 20, as before. With 70
  medals no chest redemption was possible in this unit.
- The 2 owned Coin Chest (SR) were not opened - they were
  not located inside this unit's window. The Special tab's
  purple gold chest (x5) is a Tactical Master Supply Box, not
  the coin chest; the Resources tab pages reached show coal,
  iron and food boxes only. Locating the chests in the
  inventory is a follow-up for the next unit.
- The LOOT collection icon was not tapped - no kills were
  made and its badge was not read in this unit. Follow-up
  for the next unit, which should also catch the 11:44Z
  wave and finally measure parallel dispatch and the march
  queue cap.
- No coin moved in this unit - no kills, no claim, no
  redemption, no opening. coin_after 35488573 (exact panel
  value held from the unit's opening read; no coin-moving
  action occurred). coins_collected 0. Nothing bought, no
  diamond spent, no item used.

## Input notes

- In fullscreen the event Store panel's close X did not
  respond to synthetic clicks (several attempts, including
  press-and-release). Exiting fullscreen through the View
  menu and clicking the same X in the windowed 642x951 mode
  closed the panel at once. Executors should do panel work
  in windowed mode.
- One mis-aimed click early in the Store visit toggled the
  Store "Exchange Reminder" checkbox off; attempts to
  re-check it did not visibly restore it. That checkbox is
  only a reminder preference - no purchase, no currency, no
  game state depends on it. A later unit can re-check it.
