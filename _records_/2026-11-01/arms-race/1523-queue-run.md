---
title: Queue Run 1523 Arms Race Tech Research Partial
created: 2026-11-01T23:23:00Z
modified: 2026-11-01T23:23:00Z
level: L0
version: 1.0.0
description: Ticker pass ticker-1504 arms-race unit read Tech Research at 0, tier-3 unreachable inside red lines, research timers prove no in-window completion
status: unverified
grounded_in:
  - source: game screens observed on the owner Mac mini during this pass
---

# 1523 queue run - arms race, partial

Session window: 2026-11-01 about 15:06 to 15:23 America/Los_Angeles.
Executor: ticker-1504. Unit: arms-race-2026-11-01-1403 (regular
arms-race, activity arms-race, priority 2, expires 2026-11-02T02:03:00Z).
Status: partial. The live phase and score were read twice, every
scoring path was judged live, and the completion sweep was done, but
the tier-3 target stands unreached inside the red lines, so the
tracker is untouched and the next tick re-produces this regular.

## Outcome

- Live phase, read at entry and again at the sweep: Tech Research,
  Contest Segment Lv.29-30, time left 02:45:25 at entry and 02:37:12
  at the sweep. Score 0 both reads.
- Chest thresholds: 6,250, 12,500 and 30,000. Tier-3 gap: 30,000
  points. No point chest earned (score 0 below the first
  threshold), nothing claimed.
- Scoring table, read live: Increase Tech Power by 1pt pays plus 1,
  Use 1-min Research Speed-up pays plus 10, Buy Packs containing
  Diamonds pays plus 30 per diamond. The speedup and pack paths
  are red lines and were not used.
- Tech Power path judged by live read, not by assumption: the
  research queue, opened from the base screen queue icons (flask
  icon, 2/2), holds Lv.1 Precision Targeting II with Time Left
  4d 16:36:32 and Lv.9 Morale upgrade in progress with Time Left
  1d 19:08:09, read twice across two computer sessions. No
  research completes inside this phase window (which ends about
  17:57 local), so the only legal path cannot score here. This
  is the same shape as the 2026-10-26 Tech Research miss, with
  the timers now measured instead of carried over.
- Completion sweep at the close, on the Arms Race page: no
  bouncing chest and no reward red dot. The cumulative counter
  chest at top left reads 1 of 2 with a partial bar and no
  bounce. The ranking row still shows the previous phase figure
  (#2110 [AP3x]Bears Lair, 6,000); per precedent that row is
  not used as the phase score, and its chest is preview-only
  with no claim and was not tapped. Nothing was claimed.

## Method notes (rule R2)

- The Arms Race tab bar position shifted between openings: the
  first two taps at norm 92,128 and 111,128 did nothing, and the
  OCR-grounded tab centre at norm 187,128 switched the page.
  Tab positions must be re-grounded from OCR on every opening,
  never inherited.
- The scoring-row arrow method ended after two no-change taps:
  a tap on the Increase Tech Power arrow at norm 849,550 and a
  tap on the row text at norm 450,548 both produced no change,
  so that method was abandoned inside this unit and the
  research queue was reached instead through the base queue
  icons, a different entry path.
- The Events page back arrow was first mis-measured at norm
  63,924 (that point hit a small round icon); the grounded
  back square at norm 190,962 returned to the base.
- The computer-use session dropped three times mid-unit
  (observation_unavailable); sessions cc-50, cc-51 and cc-54
  were started in turn and the game state was intact at each
  recovery, so no game state was lost. The unit ran about 17
  minutes against the 15 minute cap because of the three
  session recoveries; no scoring action was started late to
  compensate.
- No different-device dialog was seen, no login or verification
  was demanded, and no password or Touch ID step was used.

## Red lines

- No diamonds or money spent, no speedup item burned (neither
  Speed Up button in the research queue was tapped), no
  research or building started, no stage swapped, no chest
  tapped that was not earned. The research panel was closed
  with its X at norm 806,338.

## Follow-up

- The measured research timers settle this phase: no research
  completes before the phase ends, so later units of this phase
  need only re-read the score and the sweep, not re-judge the
  Tech Power path or re-open the research queue identically.
- The tier-3 shortfall for this Tech Research phase is a miss
  inside the red lines, recorded here at the phase start (first
  unit inside the phase), not discovered in the phase last
  minutes.
- Tracker untouched (partial unit). Nothing claimed.
