---
title: Arms Race queue run 1633
created: 2026-11-08T00:48:00Z
modified: 2026-11-08T00:48:00Z
level: L0
version: 1.0.0
description: Ticker-1633 arms-race unit, Base Building phase at 0 points with the target unreachable inside the red lines, recorded as skipped-needs-owner per queue rule R4
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-07
---

# 1633 queue run - Arms Race

Executor: ticker-1633. Unit: arms-race-2026-11-07-1403.
Session window about 16:35 to 16:48 America/Los_Angeles.
Mac mini online; Last War window 788x1083, screen capture working
after the 1204 pass capture failure (Issue 282).

## Not performed - target missed inside the red lines

- Phase read live twice (16:37 and 16:46): Base Building,
  Contest Segment Lv.29-30, score 0, timer 01:22:22 then
  01:20:37 left in the phase, chest thresholds 6,250 /
  12,500 / 30,000, account rank #2110 [AP3x]Bears Lair,
  segment rank 12, 0 points.
- Scoring paths, all read live: Increase Building Power by
  1pt pays +1, Use 1-min Construction Speed-up pays +10,
  Buy Packs containing Diamonds pays +30 per diamond.
- Building queue read live: Lv.29 Aircraft Center upgrade in
  progress, Time Left 4d 19:47:25; Lv.26 Drill Ground upgrade
  in progress, Time Left 1d 16:25:35; two slots Idle. No
  building completion lands inside the phase window (ends
  about 18:00 local).
- The only remaining scoring paths are the banned ones:
  burning Construction Speed-ups and buying diamond packs.
  Both sit inside the red lines, so the top chest threshold
  of 30,000 is unreachable in this phase. No chest was
  earned, nothing was claimed.
- Completion sweep, per the owner correction of 2026-10-26:
  the Arms Race page was re-read before leaving the Events
  screen. Cumulative counter chest reads 0/2, not claimable
  and not bouncing. No bouncing chest and no red dot on the
  Arms Race tab or page. The ranking-row chest opens a
  contents preview only while the phase is live. Arms Race
  is complete for this phase with nothing outstanding.
- Status: skipped-needs-owner under queue rule R4 - a phase
  whose paths all sit inside the red lines, reported early
  in the phase. Tracker marked skipped for arms-race with
  this reason. The already-staged 1803 unit for the next
  phase is unaffected. Tooling gap found in this pass and
  filed as Issue #407: tools/regulars.py uses date.today()
  in the container UTC timezone, so this unit's first skip
  landed in tools/state/2026-11-08.json and was moved to
  2026-11-07 by hand with --date; the bogus 2026-11-08 file
  was deleted.

## Live reads in this unit

- Base screen: food 440.8M, iron 768.9M, coins 33.0M,
  25.0M, 922.2K, diamonds 3,436, power 147,749,175,
  stamina 120, level 30.
- Events hub tab bar shows Arms Race, Desert Battlefield,
  Winter Battlefield - no Zombie Invasion tab, consistent
  with the event having ended at about the 19:00 reset on
  2026-10-30. No fresh zombie chain was seeded.
- Duel VS timer 01:22:54 at entry; Season II, 8d 01:22:55.
