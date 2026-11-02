---
title: Radar queue run
created: 2026-11-01T19:04:00-08:00
modified: 2026-11-01T19:04:00-08:00
version: 1.0.0
description: Ticker unit radar-2026-11-01-1803, duel day 1 release, 11 tasks executed and 25 rewards claimed, pins left for next unit
status: unverified
---

# Radar queue run, 2026-11-01 about 19:05 to 19:35 local

Unit radar-2026-11-01-1803, executor ticker-1904. Status
partial. Live duel posture from tools/duel.py at entry:
duel day 1, Radar Training, radar posture release, day ends
2026-11-02 19:00 local. The unit window text still read
"duel day 7 - radar stack" (stamped at production before
the 19:00 reset); the live posture governs, so this unit
ran as a release unit, more than 5 minutes after the
19:00 roll, past the dead window named in the duel gate.

## Opening state

- Prior radar unit 1629 (16:29 local) never entered the
  radar screen, so its reads were carried from unit 1122:
  stored 33 of 40, stamina 85, 11 task rewards pending.
  This unit re-read everything live instead of trusting
  the carry.

## What happened in this unit

- Radar entry verified on the first tap at norm 62,727
  (the 2026-10-29 measured dish point): Lv.13, radar
  points 66, stored 19 of 40, stamina 145, restore line
  "Fully restore at 11-2 03:31:43 local time" at entry
  (later reads showed 15:31:43; the hour figure is
  recorded as displayed and is unverified).
- Batch 1: Quick Execute 4 tasks, stamina 145 to 105.
  Bar flipped to Claim All, 10 task rewards. Claim All
  claimed 10, radar points 66 to 76. Rewards: chest
  times 25, radar item 100, EXP 14.1M, drone item 3.2K,
  blue triangle 450, iron 3.9M, food 2.3M, coin 2.0M.
- Batch 2: Quick Execute 3 tasks, stamina 105 to 75,
  stored 9 of 40. Bar flipped to Claim All, 8 task
  rewards. Claim All claimed 8, radar points 76 to 84.
  Rewards: radar item 70, EXP 14.2M, drone item 3.2K,
  speedup 5m times 7, speedup 1m times 85, iron 4.4M,
  food 3.6M, coin 1.3M.
- Batch 3: Quick Execute 4 tasks, stamina 75 to 35,
  stored 1 of 40. Bar flipped to Claim All, 7 task
  rewards. Claim All claimed 7, radar points 84 to 91.
  Rewards: radar item 70, EXP 13.2M, drone item 2.4K,
  iron 3.3M, food 2.4M, coin 1.3M.
- Totals in this unit: 11 tasks executed, 25 rewards
  claimed, radar points 66 to 91, stamina 145 to 35,
  coin claimed across the three popups 2.0M plus 1.3M
  plus 1.3M equals 4.6M (popup figures, not HUD totals).
- No diamonds or money spent, no Buy tapped, no other
  activity worked from this unit. A visual grounding
  call during entry timed out after 3 minutes; entry
  then succeeded on the documented coordinate, so no
  method change was needed.

## Closing state (live reads, same unit)

- Radar Lv.13, radar points 91, stored 0 of 40,
  stamina 35, restore line "12 Radar Task(s) will be
  restored in 02:16:05", fully restore 11-2 15:31:43
  local time as displayed.
- Remaining ordinary work: the bottom bar offers 1
  more task for 10 stamina. Stored reads 0 of 40 while
  a 1-task offer stands, so the offer count and the
  stored count do not move together; the next unit
  must read the bar it is actually shown.
- Pin inventory, untapped in this unit: purple
  question-mark story pin top centre, purple skull pin
  centre, orange axe pin lower left, blue skull pin
  lower centre, plus one alliance portrait pin
  ([AP3x]Black Death) that is not a task. The green
  and blue skull pins with red dots seen at entry are
  gone after the claims. Per the release standard,
  pins left unattempted make this unit partial, never
  done; the next radar unit must work the pins to a
  closing read (completed, claimed, or identified with
  a reason) and run the remaining 1-task offer.
- Duel delta test still owed: the VS panel was not
  opened in this unit, so no duel score before and
  after was read. The 25 claims on a scoring day are
  the batch the delta test should measure against.
- Tracker untouched for partial, per the queue rules.

## Red lines

- No diamonds or money spent, no paid button tapped,
  no map pin tapped, no other activity worked from
  this unit.
