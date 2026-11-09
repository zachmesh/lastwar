---
title: Donations queue run 2034
created: 2026-11-09T04:41:00Z
modified: 2026-11-09T04:41:00Z
version: 1.0.0
description: Alliance tech coin donations, Quick Construction, unverified close on cooldown timer
status: partial
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-08 20:34-20:41 PT
---

# Donations queue run 2034 (ticker-2004)

Unit: donations-2026-11-08-1803. Status: partial (unverified close).
Activity: alliance-donations. Target technology: Quick Construction
(Development tab, recommended marker), 8/10, +20% toward +22.5%.

## What happened

- Entry: the game was left on the Season "THE AGE OF OIL" tech tree
  by a previous session. Closed the UNLOCK OIL WELL panel untouched
  (no Research, no Finish Now) and returned to the base with the
  back arrow. No research started, no speedup used.
- Alliance entry route (rule R2 third-unit fix, 2026-11-02): the
  Alliance shield icon was re-grounded fresh on this screenshot
  at (930,708) and tapped once. The Alliance menu opened first
  try - the 2026-11-02 entry blocker (three units panning to the
  Drill Ground cluster) did NOT recur on this route. Members
  96/100, [AP3x] The Apex.
- Alliance Techs, Development tab: Auto Rally Max Level, Quick
  Construction 8/10 with the recommended thumbs-up marker, Great
  Helper Max Level, one 2/10 node below. Tech Donation Today
  footer read 6900 at entry.
- Donation panel (Quick Construction): Donation Count read live
  17/30 at entry. Coin Donate 900 (green) used; diamond Donate
  (2, yellow) never touched. Donation Reward per donation:
  50 tech EXP + 50 badge, panel-stated.
- Donations made, all live-read: 1 tap, count 17/30 to 16/30;
  batch of 8 taps, count 16/30 to 8/30 (all 8 landed). Second
  batch of 8 taps: the coin button greyed mid-batch and the
  count label was replaced by a cooldown timer, 00:18:14 at
  first sight, 00:18:02 on the closing screenshot. How many of
  the second batch's 8 taps landed before the cooldown bit is
  unknown - no arithmetic closing figure is claimed.
- Re-read attempt (hard closing rule): closed and reopened the
  panel path; the Tech Donation Today footer now reads 1800,
  down from 6900 at entry. A footer that falls while donations
  are made cannot be a closing count for donations made, and
  its semantics are not understood (see the knowledge gap note
  below). The top-bar badge moved 316.9K to 318.8K (+1900),
  which also does not reconcile with 50 badge per donation.
  Neither figure is used as a closing count.
- Confirmed donations this unit: 9 (live count 17 to 8).
  Coin spent on confirmed donations: 9 x 900 = 8,100.
  Remaining Donation Count: unreadable (hidden by the timer).

## Close

- Closes UNVERIFIED under the hard closing rule of
  _activities_/alliance-donations (2026-10-31 fix, rule R1):
  no live Donation Count read at close, so no closing count
  is stated. The regulars tracker is left untouched.
- A named re-read unit is enqueued for after the cooldown
  (timer 00:18:02 at about 20:44 PT, cooldown ends about
  21:02 PT): donations re-read, not-before 2026-11-09T05:05:00Z.
  The next scheduled donations unit (22:03 slot) is also in
  the pool and will re-read the count.
- Knowledge gap filed as a GitHub Issue (class: knowledge):
  the Tech Donation Today footer fell 6900 to 1800 while
  coin donations were being made, so its semantics are unknown
  and it must never be used as a donations closing count until
  understood. The badge top-bar delta (+1900) is likewise
  unreconciled.

## Red lines

- No diamonds or money spent. Diamond Donate button never
  tapped. No research started, no Finish Now, no speedup.
- No other unit's work touched.
