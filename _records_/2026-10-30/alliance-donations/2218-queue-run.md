---
title: Alliance Donations Execution 2026-10-30 2218 Queue Run
created: 2026-10-31T05:18:00Z
modified: 2026-10-31T05:18:00Z
level: L0
version: 0.1.0
description: Donations queue unit donations-2026-10-30-2203 - target Rallied HP 5/10, Donation Count 10/30 at entry, coin Donate button unresponsive across nine taps and three input routes, no donation made, tracker untouched
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-30
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
---

# Alliance donations — execution, 2026-10-30 2218 queue unit

A single task unit, executed by executor ticker-2204 under the
task unit queue. Unit donations-2026-10-30-2203, priority 2.
Session window about 22:11 to 22:18 America/Los_Angeles.
Computer sessions cc-580 then cc-582.
Status — partial: the target panel was read but no donation
landed, so the tracker is untouched and the next tick
re-produces this regular.

## What was observed

- Entry — base screen coin HUD 171.0M. Alliance button at
  norm 928,705 opened the Alliance panel; Alliance Techs
  tile at norm 717,678 opened ALLIANCE TECHS on the War
  tab (Troop Movement 5/10, Rallied HP 5/10, Rallied
  Attack 7/10, Rallied Defense 7/10, next node 1/10).
  Tech Donation Today footer read 0 at entry, a new
  day after the 19:00 reset.
- Target — Rallied HP 5/10, the node carrying the
  recommended marker on the War tab, same target as
  the 1850 unit. Panel: Increased Hero HP in Rallies
  for Allies, Current +5%, Next Level +6%, Donation
  Reward +20%, Tech EXP 779.9K/2.0M, Donation Reward
  50 + 50 as displayed. Coin Donate 600 per donation;
  the diamond Donate button (2 diamonds) was never
  touched.
- Donation Count — 10/30 at entry, and still 10/30
  at the close. No coin was spent and Tech EXP did
  not move.
- Unresponsive button — the green coin Donate button
  did not register a donation across nine taps in
  three input routes: single taps at norm 636,671
  (which landed above the button, cursor at about
  pixel 407,613), 636,699 (cursor confirmed on the
  button), 580,699 and 690,699; a 1-second long-press
  batch (move, mouse down, wait, mouse up); and a
  double-click at 636,699. A title-bar fronting tap
  plus a retried tap, a full computer session restart
  (cc-580 ended, cc-582 started, LastWar re-selected,
  panel state intact), and closing and reopening the
  panel all left the count at 10/30. Other controls
  in the same sessions responded normally (panel
  open and close, tab and tile taps), so this is a
  button-specific unresponsiveness, not a dead
  session. The next unit must try a different input
  route for this button.
- Nothing else spent — no diamonds, no money, no
  speedup items, no stamina items. No other regular
  was merged into this unit. The game was left on
  the Rallied HP donation panel. No login or
  verification was demanded, and no different-device
  dialog appeared.

## Result statistics

- donations_made: 0
- coin_spent: 0
- donation_count_before: 10
- donation_count_after: 10
- tech_donation_today_entry: 0
- target: Rallied HP
