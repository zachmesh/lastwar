---
title: Zombie Invasion queue unit 048
created: 2026-10-30T00:31:00Z
modified: 2026-10-30T00:31:00Z
version: 1.0.0
description: Queue unit zombie-invasion-zombie-2026-10-28-048 execution
status: done
---

# Zombie Invasion - 2026-10-29 17:31 PDT queue run

Unit: zombie-invasion-zombie-2026-10-28-048, executor ticker-1704.
Chain zombie-2026-10-28, successor to unit 047.

## What was done

- Events page, Zombie Invasion tab verified by title before
  Search (the tab bar shifts between openings - a batched
  sequence that assumed the earlier tab position landed on
  the Desert Storm Battlefield tab instead; no Confirm or
  entry button was tapped there, nothing spent, and the run
  recovered by clicking the partially visible Zombie tab at
  the right edge of the bar).
- Kill 1 - Squad 1, 25.05M vs 670.00K, Easy Win, Unit Count
  2,231/2,231, march 83 seconds, target X:906 Y:936.
  Stamina 84 to 74 on march. March Queues verified 1/4.
- Kill 2 - Squad 2, 20.92M vs 670.00K, Easy Win, Unit Count
  2,175/2,175, march 115 seconds, target X:980 Y:844.
  The deploy panel defaulted to Squad 1 (returning); the
  Squad 2 tab was tapped first, then March. Stamina 75
  (with regeneration) to 65 on march.
- Parallel attempt - a batched second dispatch inside Squad
  1's outbound window failed for the tab-shift reason above,
  and the verified stepwise second dispatch finished only
  after Squad 1 had already returned, so the March Queues
  bar read 1/4 at the second March, not 2/4.
  squads_parallel is therefore 1, sequential, not a march
  cap of 4.
- Loot - after both squads returned (March Queues 0/4),
  the gift badge read 1, not 2. The LOOT panel held exactly
  one row: Lv.10 Invading Zombies, X:906 Y:936 (Squad 1's
  target), coin 268.0K, medal x10, iron 268.0K, food
  268.0K, EXP 263.0K. Claim All (plain blue, no price tag)
  claimed it in-unit. The badge cleared and the coin HUD
  moved 108.7M to 109.0M.
- Missing row - Squad 2's kill (X:980 Y:844) produced no
  LOOT row in this unit's panel, although its march was
  verified out (1/4, stamina charged) and both squads were
  home (0/4) before the panel was opened. This is a second
  handover-style loss after unit 009's: a completed march
  whose row never materialized. The successor unit must
  re-check the gift badge - if the row appears late, claim
  it then; if not, it is lost, not deferred.
- Stamina - never binding this unit (84 to 65 across two
  marches, 76 at close with regeneration). No stamina item
  was opened and no backpack stamina inventory count was
  needed, since no refill source was exhausted.
- Store - NOT visited this unit. The unit ran past its
  15 minute cap (two sequential dispatches plus two full
  march round trips) and the pass budget was already over
  when the loot was claimed. The medal balance was not
  re-measured live, so no derived medal total is reported
  here. The Coin Chest (SSR) row re-check and the Buy-step
  retry from unit 047 stay deferred to the next unit.

## Result statistics

- zombies_killed: 2 (two marches completed and returned;
  only 1 LOOT row materialized)
- loot_rows_claimed: 1
- loot_rows_missing: 1 (Squad 2, X:980 Y:844)
- cleared: false (wave live, Search found targets on
  demand, event page read 1d 01:37 left)
- coin_before: 108.7M HUD rounded
- coin_after: 109.0M HUD rounded
- coins_collected: 268000
- medals_earned: 10 (from the claimed row; Store balance
  not re-measured this unit, so no medals_before or
  medals_after total is stated)
- chests_opened: 0
- chests_redeemed: 0
- squads_parallel: 1 (sequential - second dispatch
  finished after Squad 1 returned)
- tasks_badge: 1
- stamina_start: 84
- stamina_end: 76

## Red lines

No diamonds or money spent, no price tag or paid button
tapped, no speedup burned, no assembly, no teleport, no
player attacked.
