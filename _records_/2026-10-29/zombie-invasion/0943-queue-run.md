---
title: Zombie Invasion Execution 2026-10-29 0955 Queue Run
created: 2026-10-29T16:48:00Z
unit: zombie-invasion-zombie-2026-10-28-044
executor: ticker-0934
status: partial
---

# Zombie Invasion - execution, 2026-10-29 0943 queue unit 044

A single task unit, executed by executor ticker-0934 under the
task unit queue. Unit zombie-invasion-zombie-2026-10-28-044,
chain zombie-2026-10-28, chain sequence 44, priority 4.
Session window about 09:43 to 09:48 America/Los_Angeles.
Status - partial; the chain continues while the event is
available and zombies remain nearby, so the tracker is
left untouched. The one kill dispatched in this unit was
resolved and claimed inside it, and the march queue
was empty at the close.

## What was observed

- Open - the game was on the base screen, no
  different-device dialog at any point. Computer
  sessions dropped three times mid-pass (cc-258,
  cc-259, then cc-260) and were replaced without
  loss, the same timeout pattern earlier units
  recovered from.
- Event page - Zombie Invasion live with 1 day
  09:15:31 left, next wave in 00:56:53 at first
  sight. Search at normalized 275,925 found a
  Lv.10 Invading Zombies target beside the home
  base (Guaranteed Reward medal x10, book 1.3K,
  hero EXP 263.0K, iron 268.0K, food 268.0K;
  Suggested Power 670,000, stamina cost 10,
  despawn about 11:56:36).
- Deploy - the crossed-swords button's effective
  point is lower than first tapped: a tap at
  498,699 did nothing, the grounded point
  498,728 opened the panel. Squad 1, 25.05M Vs
  670.00K, Easy Win, Unit Count 2,231 of 2,231,
  march time 00:00:03, stamina 53 with cost 10.
- Kill 1, Squad 1 - March at the grounded
  500,755 dispatched. The control channel then
  reported the target app exited or restarted;
  re-activating LastWar showed the world map with
  March Queues 0/4 and the gift badge at 1, so
  the march had resolved and the squad had
  returned during the restart - state intact,
  stamina 43 at the close, confirming 10 spent.
  No second squad was dispatched in this unit:
  the 3 second round trip had already finished
  by the time the app was re-activated, and the
  pass budget was ending, so no parallel attempt
  could be staged. squads_parallel is 1 for
  that stated reason, not a march cap (the
  queue cap remains 4).
- Claim - the grounded gift tap 317,233 opened
  the LOOT panel with exactly one row, Lv.10
  Invading Zombies. Claim All at 498,760, blue
  button with no price tag. The row's coin line
  was not read before the claim; coins_collected
  268,000 is the established Lv.10 row value,
  corroborated by the HUD after the claim: coins
  105.0M to 105.3M and iron 414.7M to 414.9M,
  each up about one 268.0K row.
- Coin totals - coin_before is HUD-rounded
  105.0M at this unit's start (no exact panel
  figure was read); coin_after is HUD-rounded
  105.3M after the claim. Both figures are
  labelled so; coins_collected is the row value
  above, HUD-corroborated.
- Stamina - 53 at the deploy panel, 43 at the
  close. No refill was needed and no conclusion
  about exhausted refills was required, so the
  backpack stamina inventory was not re-read
  this unit.
- Medals - medals_before 2920 is unit 043's
  derived medals_after carried forward, not a
  fresh live read; medals_after 2930 is derived
  (2920 plus this unit's 10). The Store was not
  re-opened this unit, so the Coin Chest (SSR)
  redemption stays deferred, as in unit 043, and
  no owned chest was opened - their backpack
  location is still unknown.
- Cleared - false. Search found a target on
  demand in a live wave, and the event still has
  over a day left. Successor unit 045 enqueued
  to start now.

## Result statistics

- zombies_killed: 1
- cleared: false
- coin_before: 105.0M HUD rounded
- coin_after: 105.3M HUD rounded
- coins_collected: 268000
- medals_before: 2920 derived
- medals_after: 2930 derived
- chests_opened: 0
- squads_parallel: 1
- tasks_badge: 1
- stamina_end: 43
