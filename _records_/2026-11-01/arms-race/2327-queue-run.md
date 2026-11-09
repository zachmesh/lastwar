---
title: Queue Run 2327 Arms Race Unit Progression Partial
created: 2026-11-01T23:27:00-08:00
modified: 2026-11-01T23:27:00-08:00
version: 1.0.0
description: Ticker unit arms-race-2026-11-01-2203 read Unit Progression at 0, tier-3 gap 75000, one barracks judged Lv.10 locked and busy, sweep clean, nothing claimed
status: unverified
grounded_in:
  - source: game screens observed on the owner Mac mini during this pass
---

# 2327 queue run - arms race, partial

Session window: 2026-11-01 about 23:16 to 23:27 America/Los_Angeles.
Executor: ticker-2304. Unit: arms-race-2026-11-01-2203 (regular
arms-race, activity arms-race, priority 2, expires 2026-11-02T10:03:00Z).
Status: partial. The live phase and score were read twice, the
scoring paths were judged live as far as the unit cap allowed, and
the completion sweep was done, but the tier-3 target stands
unreached, so the tracker is untouched and the next tick
re-produces this regular.

## Outcome

- Live phase, read at entry and again at the sweep: Unit
  Progression, Contest Segment Lv.29-30, time left 02:40:31 at
  entry and 02:38:22 at the sweep. Score 0 on both reads.
- Chest thresholds: 15,000, 30,000 and 75,000. Tier-3 gap: the
  full 75,000 points. No point chest earned (score 0 below the
  first threshold), nothing claimed.
- Scoring table, read live: Train a Lv.10 unit pays plus 31,
  Use 1-min Training Speed-up pays plus 10, Buy Packs
  containing Diamonds pays plus 30 per diamond. The speedup
  and pack paths are red lines and were not used.
- Training path judged by live read, in part: the Train a
  Lv.10 unit row arrow opened a TRAIN UNITS panel for one
  barracks. That barracks trains up to Lv.8 only (Lv.9 and
  Lv.10 shown locked), its slider stood at 666 units at
  Lv.8, and its Train button carried a batch timer of
  1d 04:20:26, so it is busy and cannot queue Lv.10 units.
  No Train was tapped and no Finish Now was tapped. The
  other three barracks were NOT checked inside this unit's
  cap, so the training path is judged blocked at one
  barracks, not settled for the account.
- Completion sweep at the close, on the Arms Race page: no
  bouncing chest and no reward red dot. The cumulative
  counter chest at top left reads 0/2, static, no bounce,
  and was not tapped. The ranking row reads #2110
  [AP3x]Bears Lair with score 0, matching the phase score
  on this read; its chest is preview-only per precedent
  and was not tapped. Nothing was claimed. The game was
  left on the Arms Race page.
- Own PRs first: no open PR exists on zachmesh/lastwar at
  this pass's start (VPS gh pr list returned empty; the
  records/2026-11-01 PR 142 noted by the 19:34 unit has
  evidently been merged in the 23:00 batch), so nothing
  addressed to this job and no PR action was owed before
  the game work.
- Zombie seeding: not done. The zombie-invasion activity
  INDEX records chain close at unit 066: the event ended
  at about the 19:00 reset on 2026-10-30, so no chain unit
  was seeded, per the standing do-not-seed rule.

## Method notes

- The Events tab bar shifted between openings again: the
  first two taps on the partially visible Arms Race tab
  did nothing, backing out to base and re-entering still
  landed on Wanted Boss, and a rightward drag of the tab
  bar revealed the Arms Race tab fully, after which a tap
  on its OCR-grounded centre switched the page. On the
  sweep return the same drag switched straight to the
  Arms Race page. Tab positions must be re-grounded from
  OCR on every opening, never inherited.
- One stale-observation retry: a tab tap sent with an
  image observation id was refused, and the same tap
  re-sent with the latest receipt observation id
  succeeded, so no game state was lost.
- The radar unit of this same pass launched a Doom Walker
  rally (March Queues 1 of 4, marching at the arms-race
  unit's entry); that rally belongs to the radar unit and
  its result falls to the next radar unit, not to this
  arms-race unit.

## Follow-up

- Next arms-race unit must check the other three barracks
  for an idle Lv.30 barracks that can queue Lv.10 units
  (2,420 units score 75,000 at plus 31 each, before any
  batch-size cap), before concluding the training path
  is blocked for this phase. If such a barracks is idle,
  queue just enough Lv.10 units to reach 75,000 and claim
  all three chests in that unit.
- Tracker untouched for partial, per the queue rules.
  Nothing claimed.

## Red lines

- No diamonds or money spent, no speedup item burned, no
  building or research started, no stage swapped, no
  chest tapped that was not earned.
