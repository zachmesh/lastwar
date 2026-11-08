---
title: Alliance Donations Execution 2026-10-31 0220 Queue Run
created: 2026-10-31T09:20:00Z
modified: 2026-10-31T09:20:00Z
level: L0
version: 0.1.0
description: Donations queue unit donations-2026-10-31-0203 - target Rallied HP 5/10, 22 coin donations made at 600 coin each, count 22/30 to 1/30 verified step by step, final tap moved Tech EXP and greyed the button on a 00:48:50 timer
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-31
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
---

# Alliance donations — execution, 2026-10-31 0220 queue unit

A single task unit, executed by executor ticker-0204 under the
task unit queue. Unit donations-2026-10-31-0203, priority 2.
Session window about 02:12 to 02:20 America/Los_Angeles.
Computer sessions cc-596, cc-597 and cc-598 (sessions
dropped twice mid-unit and were restarted with no game
state lost, as in earlier units).
Status — partial: 22 coin donations landed, but the final
count label is hidden under the button timer, so the
tracker is untouched and the next tick re-produces this
regular to verify the count at 0.

## What was observed

- Entry — base screen coin HUD 171.0M. Alliance button
  at norm 928,705 opened the Alliance panel; Alliance
  Techs tile at norm 717,678 opened ALLIANCE TECHS on
  the War tab (Troop Movement 5/10, Rallied HP 5/10,
  Rallied Attack 7/10, Rallied Defense 7/10, next node
  1/10). Tech Donation Today footer read 0 at entry.
- Target — Rallied HP 5/10, the node carrying the
  recommended marker on the War tab, same target as
  the 2026-10-30 1850 and 2218 units. Panel: Increased
  Hero HP in Rallies for Allies, Current +5%, Next
  Level +6%, Donation Reward +20%, Tech EXP
  817.6K/2.0M at entry, Donation Reward 50 + 50 as
  displayed. Coin Donate 600 per donation; the
  diamond Donate button (2 diamonds) was never
  touched.
- Grounded button point — the green coin Donate
  button grounds at norm 660,765 by visual grounding.
  This explains the 2026-10-30 2218 unit's failure:
  its taps at norm 636,699 and nearby landed above
  the button. The next unit should reuse 660,765,
  not 699.
- Donations made — 22 in total, verified by the
  Donation Count label at each step: 22/30 at entry,
  21/30 after the first grounded tap, 16/30 after a
  batch of 5, 8/30 after a batch of 8, 1/30 after a
  batch of 8 of which 7 landed (the eighth hit the
  burst cooldown). Tech EXP moved 817.6K to 820.1K
  across the unit (0.1K display rounding, so the
  count label, not the EXP delta, is the donation
  evidence). Coin spent: 22 times 600 = 13,200.
- Cooldowns — after the 8/30 to 1/30 batch the coin
  button greyed with a 00:01:24 timer (the burst
  limit of the 2026-10-26 note); the unit waited
  it out and the count reappeared at 1/30. The
  final tap moved Tech EXP 819.8K to 820.1K and
  greyed the button again, this time with a
  00:48:50 timer and the count label hidden, so
  the final 0/30 reading is arithmetic (22 minus
  22), not a directly read label — hence partial,
  not done. The next unit should re-read the
  count once the timer clears.
- Navigation note — the game opened on the Arms
  Race phase page (left by the 0211 arms-race
  unit). The back arrow at norm 159,938 returned
  to the base view. A first Alliance tap at norm
  875,672 missed the button and panned the base
  camera into the zoomed interior state; a tap
  on an empty road tile at norm 500,450 restored
  the exterior view, and the recorded Alliance
  point 928,705 then opened the panel. The game
  was left on the Rallied HP panel.
- Nothing else spent — no diamonds, no money, no
  speedup or stamina items, no research or
  building started. No other regular was merged
  into this unit. No login or verification was
  demanded, and no different-device dialog
  appeared.
