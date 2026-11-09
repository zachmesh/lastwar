---
title: Donations queue run 0244
created: 2026-11-08T10:56:00Z
modified: 2026-11-08T10:56:00Z
level: L0
version: 1.0.0
description: Ticker-0244 donations unit, partial and unverified - 5 coin donations landed live (6->1), final tap hidden behind a 00:08:17 timer, count never read at 0
status: unverified
---

# 0244 queue run - Alliance donations

Executor: ticker-0244. Unit: donations-2026-11-08-0618. Session
about 02:44 to 02:55 America/Los_Angeles (computer session cc-78;
no drop, no different-device dialog, no login demand).

## Pool divergence note - read first

This unit was executed under the main-tree copy of
donations-2026-11-08-0618. The records branch already holds the
same unit id in done, closed partial by ticker-0137 at 01:53 PT
(0 donations, blocked by the Star Ceremony overlay; record
0154-queue-run.md). The main-tree pool still carried the unit in
inbox, so this pass re-picked and re-executed an already-closed
unit. The two pool copies have diverged: the branch pool carries
ticker-0137's completion, the main-tree pool did not. The game
work in this record is a separate, later execution - the count
had refilled to 6/30 by 02:44 - and it is recorded here only. It
is NOT merged into the branch's 0618 unit result, which stands
as ticker-0137 wrote it; the branch delivery of this pass
carries this record file, the day INDEX entry, the action log
line and the re-read inbox unit, but not a second 0618 done
file. Pool-divergence issue filed (tooling class) from this
record.

## Performed

- Entry route (rule R2): the Alliance shield was re-grounded
  fresh with the visual-grounding tool on the current
  screenshot - centre (937, 708) in the 763x1050 windowed
  layout. The tap opened the Alliance menu on the first try
  with no camera pan to the Drill Ground - the 11-02 entry
  blocker did not recur. Alliance: [AP3x] The Apex, Leader
  Abyss Apex, power 13,350,333,388, members 96/100, English.
  Red dots on Help and Alliance Gifts tiles, both mapping to
  their own regulars, already queued. The Alliance Star
  (Event 40) banner (Time Left 15:04:19) was left untouched.
- Alliance Techs, Development tab: Auto Rally Max Level,
  Quick Construction 8/10 carrying the recommended marker,
  Great Helper Max Level, one node below at 2/10 (cut off).
  Tech Donation Today read 2350 at entry (above the 1000
  reward threshold).
- Donation panel, Quick Construction (8/10, +20% building
  speed, Tech EXP 1.2M/6.0M, reward EXP 50 + badge 50 per
  donation): Donation Count read live 6/30 at entry.
- Coin donations made in this unit, all on the green coin
  button (900 coin each), diamond button never touched,
  single taps with a live count read after each:
  6/30 -> 5/30 -> 4/30 -> 3/30 -> 2/30 -> 1/30. Five coin
  donations landed on live reads. Coin spent verified 4,500.
- The "Hold down for easier continuous donations" hint
  appeared after the third tap, as in the 2219 and 0043
  units. Single taps were kept throughout; no hold-down
  was used.
- Sixth tap note: after the 1/30 read, one more single tap.
  The control channel warned the tap "showed no change" and
  advised click_element instead, but the live image read
  shows the coin button greyed with a 00:08:17 cooldown
  timer and the count label hidden - the tap dispatched and
  the button entered its cooldown state. No click_element
  retry was made: a retry tap on a greyed button cannot land
  and would only risk a double-spend reading.
- Footer cross-check, observed only: Tech Donation Today read
  2950 at close, up 600 from the 2350 entry read - exactly
  +100 per donation for the 6 dispatched taps, matching the
  0043 unit's +100 per tap. This is recorded as observed
  only, not as a closing figure: the footer is disqualified
  as a count-closing figure per the activity profile, and
  its per-donation value has varied across units.
- Badge counter in the top bar, verbatim reads only: 300.4K
  at entry, 300.5K, 300.6K, 300.7K, 300.8K, 300.9K after
  each of the first five donations, 301.0K after the sixth
  tap - +0.1K per tap throughout. Recorded as observed
  only: the badge step has been inconsistent across units
  (0043 saw +100, +100, then +200), so no per-donation
  rate is inferred from it.

## Not verified - why this unit closes partial

- The Donation Count was never read live at 0/30 in this
  unit, so the day cannot be closed as done (rule R1 /
  hard closing rule in the activity profile). The last tap's
  effect is unconfirmed: the count is either 0/30 (tap
  landed, timer is the exhaustion timer) or still 1/30
  (tap eaten by the grey-out, as the 2219 unit proved
  possible when it waited out a 00:01:27 timer and re-read
  1/30 unchanged).
- The 00:08:17 timer cannot be waited out inside this unit's
  15-minute cap (timer expiry about 03:02 local). A named
  re-read unit is enqueued for after the cooldown
  (not before 03:03 local).
- Count-rise note for Issue #160: the 0043 unit closed at
  about 00:43 with a last live read of 1/30 and an
  unconfirmed final tap; this unit opened at 02:44 to a
  live read of 6/30. That is a rise of +5 over about 121
  minutes (about 1 per 24 minutes) if the 0043 final tap
  did not land, or +6 (about 1 per 20 minutes) if it did.
  Either way it matches the roughly 1 per 20 minutes
  estimate from the 2348 unit, and it is far faster than
  the 1 per 70 minutes two-endpoint estimate in the 0043
  record (which used the 2219 to 0043 pair). The
  replenishment rate remains unmeasured; the mechanism
  measurement per Issue #160 is still owed. Commented on
  #160 from this record.

## Game left safe

- ALLIANCE TECHS closed, Alliance menu closed, back on the
  base screen. No diamond button tapped, no money spent, no
  other task type touched. No Assemble, no teleport, no
  purchase.
