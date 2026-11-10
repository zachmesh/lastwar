---
title: Radar Tasks Execution 2026-10-30 0220 Queue Run
created: 2026-10-30T09:20:00Z
modified: 2026-10-30T09:20:00Z
level: L0
version: 0.1.0
description: Radar queue unit radar-2026-10-30-0203 on duel Day 5 release posture - free 75 stamina claimed, Quick Execute 5 tasks, two Claim All batches totalling 8 rewards, points 2989 to 2997, special map pins left unattempted
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-30
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
  - source: tools/duel.py readout on 2026-10-30 - duel day 5, Total Mobilization, radar posture release
---

# Radar tasks — execution, 2026-10-30 0220 queue unit

A single task unit, executed by executor ticker-0204 under the
task unit queue. Unit radar-2026-10-30-0203, priority 3.
Session window 02:15 to about 02:20 America/Los_Angeles.
Status — performed in part: ordinary tasks are cleared
and all claimable rewards were claimed, but the special
map pins were not attempted, so the tracker is untouched
and the next tick re-produces this regular.

## What was observed

- Duel posture first (tools/duel.py) — Day 5, Total
  Mobilization, day ends 2026-10-30 19:00 local,
  radar posture release: everything counts, including
  radar claims, and the Day 4 radar stack is to be
  released.
- Entry — the radar screen opened on the first tap of
  the left-column satellite-dish icon, visually
  grounded at centre 53,709 on a fresh screenshot.
- Radar open — Lv.12, points 2,989, stored tasks
  4 of 40, stamina 26, restore bar 100 percent.
  The restore line read "12 Radar Task(s) will be
  restored in 02:34:53". The bottom bar offered
  Quick Execute: "You can complete 5 tasks, requires
  50 Stamina."
- Stamina regain — stamina was short of the 50
  required, so Quick Execute opened the REGAIN
  STAMINA panel instead of failing. Free claim taken
  first: 75 Stamina, Remaining Today 2 of 2 before
  the claim. After the claim the panel read stamina
  102 of 120, free-claim cooldown 03:59:55,
  Remaining Today 1 of 2, fully replenished in
  01:29:46. The paid Buy 100 stamina for 300 rubies
  was never used. Item inventory in the panel:
  10 Stamina items owned 624, 50 Stamina items
  owned 610 (down from 611 before unit 054 opened
  one, consistent with that record).
- Quick Execute — after closing the panel, Quick
  Execute ran at once with no march wait: stamina
  102 to 52, exactly 5 tasks at 10 stamina each.
  The bottom bar then read "6 task rewards can be
  claimed".
- Claim All, first batch — points 2,989 to 2,995
  (plus 6), stored tasks 4 of 40 to 0 of 40. Popup
  rewards: chest items 24, radar tokens 60, Hero
  EXP 10.6M, drone data items 800, iron 2.4M, food
  1.7M, coin 1.1M. Item names other than the
  displayed EXP, iron, food and coin figures are
  as displayed, not independently verified.
- Claim All, second batch — the bottom bar then
  read "2 task rewards can be claimed". Second
  popup: points 2,995 to 2,997 (plus 2), rewards
  chest item 1, radar tokens 10, 5-minute speedups
  6, 1-minute speedups 65, Hero EXP 1.5M, drone
  data items 800, iron 1.2M, food 468.0K, coin
  121.9K. After this claim the bottom bar
  disappeared: no Claim All and no Quick Execute
  offer remained, so ordinary tasks are done.
- Pins, left unattempted — the closing map showed
  five pins: a purple question-mark pin top right,
  a portrait pin left centre, a purple skull pin
  with an axe pin left centre, an orange axe pin
  bottom left and a blue axe pin bottom right. No
  pin was tapped in this unit, following the
  2026-10-29 22:21 unit's pattern and the pin-tap
  caution in the radar metadata (a tap can claim
  a finished task at once with no card). A green
  skull pin with a red dot seen in the pre-claim
  screenshot was absent from the closing map;
  whether it was claimed inside the Claim All
  batches is unverified, so it is not claimed as
  a pin completion here.
- Side effect for Arms Race — the 50 stamina spent
  here would add 5,000 points in the live Drone
  Boost phase at the displayed rate of 100 points
  per stamina (arithmetic only, not a live
  re-read); the arms-race unit for this slot is
  re-produced next tick and will re-read the live
  score then.
- Nothing else spent — no diamonds, no money, no
  speedup items burned, no paid stamina bought.
  No other regular was merged into this unit.
