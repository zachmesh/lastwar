---
title: Queue Run 1342 Arms Race Skipped Needs Owner
created: 2026-11-08T21:42:00Z
modified: 2026-11-08T21:42:00Z
level: L0
version: 1.0.0
description: Arms Race successor arms-race-2026-11-08-2127, Unit Progression phase verdict, score 0, tier-3 unreachable inside the red lines, skipped-needs-owner
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-08 about 13:40-13:42 America/Los_Angeles
---

# 1342 queue run - arms race successor (arms-race-2026-11-08-2127)

- Unit: arms-race-2026-11-08-2127, executor ticker-1317.
  Status: skipped-needs-owner - the Unit Progression
  phase verdict for this slot: score 0, tier-3
  unreachable inside the red lines. Tracker marked
  skipped for this slot.
- Session: computer session cc-126 on the owner Mac mini
  (1c817413-83e2-0545-cb90-36d5e096a6bd). No device-access
  error, no different-device dialog, no login demanded.
  Nothing bought, no speedup used, no building or
  research started, no stage swapped.
- Session window: 13:40-13:42 local, about 2 minutes.

## What was read live

- Phase re-read on the Arms Race page: Unit Progression,
  Contest Segment Lv.29-30, score 0, timer 00:18:49 at
  the read (about 13:41). The timer reads cross-check
  to a phase end about 14:00 local, not 14:03 - the
  1333 unit's "about 14:03" estimate is superseded by
  the two timer reads here and in the 1333 sweep
  (00:34:17 at about 13:26).
- Point chest thresholds 15,000 / 30,000 / 75,000 (ruby
  tags 2,360 / 4,800 / 11,800). No chest earned at
  score 0. Cumulative counter chest at top left reads
  0/2, not full, no bounce. Ranking row #2110
  [AP3x]Bears Lair with score 0, matching the phase
  score; its chest is preview-only per precedent and
  was not tapped.
- Scoring table unchanged from the 1333 read: Train a
  Lv.10 unit +31, Use 1-min Training Speed-up +10 (red
  line), Buy Packs containing Diamonds +30 per diamond
  (red line). Tier-3 gap stands at the full 75,000
  points.

## Why the phase is unreachable

- The only legal scoring path is training Lv.10 units.
  Two barracks were checked live in this pass: the
  Lv.30 barracks holds a Lv.10 batch of 793 with about
  20:47 left (1333 and 1350 units), and a Lv.8-only
  barracks holds a batch with 1d 04:20 left (2026-11-01
  2327 unit). No idle Lv.30 barracks was found, and no
  Lv.10 batch was queued anywhere in this pass, so the
  score stayed 0 from the phase read to this re-read.
- The remaining legal paths are the banned speedup and
  pack spends. No refill was spent for this phase: per
  the 2026-10-31 phase-final miss rule, Free Claim and
  stamina items are opened before a miss is recorded
  only when the gap is closable inside the remaining
  window, and 75,000 points (about 2,420 Lv.10 units)
  cannot close in the 19 minutes left with no idle
  barracks.

## Completion sweep

- On the Arms Race page at close: no bouncing chest and
  no reward red dot. No point chest earned, so nothing
  was claimed and nothing earned was left unclaimed.
  The Events tab bar shows a red badge on Frontline
  Breakthrough - that belongs to the Doomsday event
  page, not to Arms Race, and was left for the events
  regular. The game was left on the base screen.

## Tracker and follow-up

- Tracker marked skipped for this slot (regulars.py
  skip arms-race): Unit Progression tier-3 unreachable,
  score 0, training path blocked, phase ends about
  14:00. The next arms-race unit
  (arms-race-2026-11-08-1403, in inbox) serves the next
  phase; its first unit reads that phase fresh under
  rule R4.
- Result stats: target 75000, achieved 0, verified yes
  for the live 0 read.
