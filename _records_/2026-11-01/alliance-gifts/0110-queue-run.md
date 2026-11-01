---
title: Alliance gifts queue run 0110
created: 2026-11-01T08:10:00Z
modified: 2026-11-01T08:10:00Z
version: 1.0.0
description: Alliance gifts unit gifts-2026-10-31-2230 executed by ticker-0104
status: performed
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-01
---

# Alliance gifts — execution, 2026-11-01 0110 queue unit

A single task unit, executed by executor ticker-0104 under
the task unit queue. Unit gifts-2026-10-31-2230, priority 3.
Session window about 01:04 to 01:10 America/Los_Angeles.
Status — performed: both tabs claimed, tracker marked done.
No other regular was merged into this unit.

## Own PR first

Before game work, this pass resolved the conflict on
records PR 24 (records/2026-11-01, opened by ticker-0034):
merged current main into the branch in a separate worktree
and reconciled _records_/retro/improvements.md frontmatter
to version 1.1.1, keeping both the main IMP-20261101-01
through IMP-20261101-05 entries and the branch
IMP-20261031-09 implemented status (PR 23). Post-merge
diff of that file vs main is that single status line.
Pushed as 06f1a587 and replied on PR 24 for the
integrator to re-check mergeability.

## What was done

- Computer session cc-732. No different-device dialog
  appeared, no login or verification was demanded.
  Chrome stayed frontmost for part of the unit and every
  grounded tap still reached the game.
- Alliance panel: Alliance at norm 933,735 opened the
  panel at once. Alliance Gifts carried a red dot; its
  grounded button (visual-grounding point 315,606)
  opened the gifts screen. Gift Level 28, progress
  177,052,730 of 206,300,000 at entry.
- Regular tab: Claim All badge 47 at first read. The
  grounded Regular Claim All point (500,935) opened
  the CONGRATULATIONS dialog reading "A total of 47
  Regular Alliance Gifts were claimed this time".
  Progress then read 177,053,200. Dismissed by a tap
  below the dialog at norm 500,850 (a first dismiss
  attempt returned outcome unknown with the dialog
  still up; the second tap at the same point closed
  it). Second sweep: no Claim All badge remained on
  the Regular tab.
- Premium tab: tapped at norm 694,269. The Premium
  Claim All point was re-grounded on this unit's own
  screenshot (754,944); the "Hide your name on Gifts"
  checkbox was left unchecked and untouched. Badge
  read 5, dialog read 6 Premium gifts — one gift
  arrived between the badge read and the tap.
  Progress then read 177,054,650. Dismissed by a tap
  below the dialog at norm 500,850.
- Premium, second sweep: badge 2, two new SSR gifts
  from Janet ^ (Premium Glitter Coin Pack) that
  arrived during the unit. A second Claim All at
  the same point claimed 2 more, dialog confirmed.
- Verification: the Premium list rows read Claimed,
  the Claim All badge was gone, and Gift Level
  progress closed at 177,055,050 of 206,300,000.
- The game was left on the Alliance Gifts Premium
  list. Nothing else spent — no diamonds, no money,
  no speedup items burned, no building or research
  started, no Alliance Store purchase, no Assemble.
- Zombie Invasion seeding was not done: the event
  ended 2026-10-30 about 19:00 and the Events hub
  has no Zombie page, so no zombie unit was seeded.

## Result statistics

- regular_claimed: 47
- premium_claimed: 8

## Close

- Next gifts unit: use Alliance at norm 933,735,
  Alliance Gifts at norm 315,606, Regular Claim All
  at norm 500,935, Premium Claim All at norm
  754,944 — the two tabs' buttons are not in the
  same place, so ground each tab's button separately.
  Expect new gifts to keep arriving during the unit;
  two sweeps clear a tab, and chasing further
  arrivals is not required.
