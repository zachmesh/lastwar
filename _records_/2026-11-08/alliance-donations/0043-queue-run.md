---
title: Donations queue run 0043
created: 2026-11-08T08:43:00Z
modified: 2026-11-08T08:43:00Z
level: L0
version: 1.0.0
description: Ticker-0034 donations re-read unit, partial and unverified - 2 coin donations landed live (3->1), final tap hidden behind a 00:16:01 timer, count never read at 0
status: unverified
---

# 0043 queue run - Alliance donations

Executor: ticker-0034. Unit: donations-2026-11-08-0419 (re-read
after the 2018 unit's 00:18:46 cooldown; not-before 20:38 local
2026-11-07). Session about 00:36 to 00:43 America/Los_Angeles
(computer session cc-65; no drop, no different-device dialog,
no login demand).

## Performed

- Entry route (rule R2): the Alliance shield was re-grounded
  fresh with the visual-grounding tool on the current
  screenshot - centre (938, 718) in the 763x1050 windowed
  layout. The tap opened the Alliance menu on the first try
  with no camera pan to the Drill Ground - the 11-02 entry
  blocker did not recur. Alliance: [AP3x] The Apex, Leader
  Abŷss Apex, power 13,350,333,388, members 96/100, English.
  Red dots on Help and Alliance Gifts tiles, both mapping to
  their own regulars, already queued.
- Alliance Techs, Development tab: Auto Rally Max Level,
  Quick Construction 8/10 carrying the recommended marker,
  Great Helper Max Level, one node below at 2/10 (cut off).
  Tech Donation Today read 2050 at entry (above the 1000
  reward threshold).
- Donation panel, Quick Construction (8/10, +20% building
  speed, Tech EXP 1.2M/6.0M, reward EXP 50 + badge 50 per
  donation): Donation Count read live 3/30 at entry.
- Coin donations made in this unit, all on the green coin
  button (900 coin each), diamond button never touched,
  single taps with a live count read after each:
  3/30 -> 2/30, 2/30 -> 1/30. Two coin donations landed on
  live reads. Coin spent verified 1,800.
- Third tap note: after the 1/30 read, one more single tap.
  The control channel warned the tap "showed no change" and
  advised click_element instead, but the live image read
  shows the coin button greyed with a 00:16:01 cooldown
  timer and the count label hidden - the tap dispatched and
  the button entered its cooldown state. The "Hold down for
  easier continuous donations" hint appeared, as it did in
  the 2219 unit after a tap that landed. No click_element
  retry was made: a retry tap on a greyed button cannot land
  and would only risk a double-spend reading.
- Footer cross-check, observed only: Tech Donation Today read
  2350 at close, up 300 from the 2050 entry read - exactly
  +100 per donation for the 3 dispatched taps. This is
  recorded as observed only, not as a closing figure: the
  footer is disqualified as a count-closing figure per the
  activity profile, and its per-donation value has varied
  across units (+50 for one donation in the 2348 unit, +750
  for 8 in the 0545 unit, unchanged across 6 in the 1924
  unit).
- Badge counter in the top bar, verbatim reads only: 300.0K
  at entry, 300.1K after the first donation, 300.2K after
  the second, 300.4K after the third. The last step (+200)
  does not match the first two (+100 each); no per-donation
  rate is inferred, matching the 2219 unit's treatment.

## Not verified - why this unit closes partial

- The Donation Count was never read live at 0/30 in this
  unit, so the day cannot be closed as done (rule R1 /
  hard closing rule in the activity profile). The last tap's
  effect is unconfirmed: the count is either 0/30 (tap
  landed, timer is the exhaustion timer) or still 1/30
  (tap eaten by the grey-out, as the 2219 unit proved
  possible when it waited out a 00:01:27 timer and re-read
  1/30 unchanged).
- The 00:16:01 timer cannot be waited out inside this unit's
  15-minute cap. A named re-read unit is enqueued for after
  the cooldown (not before 00:59 local).
- Count-rise note for Issue #160: the 2219 unit closed at
  22:19 on 2026-11-07 with a last live read of 1/30 and an
  unconfirmed final tap; this unit opened at 00:40 to a live
  read of 3/30. That is a rise of +2 over about 2 hours 21
  minutes (about 1 per 70 minutes if the 2219 final tap
  landed and the count went 0 -> 3, or 1 -> 3 if it did
  not). Either way it is far slower than the roughly 1 per
  20 minutes two-endpoint estimate from the 2348 unit, and
  it matches the 2018 unit's own rise (1/30 at 19:24 to
  2/30 at 20:04). The replenishment rate remains unmeasured;
  the mechanism measurement per Issue #160 is still owed.

## Game left safe

- ALLIANCE TECHS tree open on the Development tab, Quick
  Construction panel closed. No diamond button tapped, no
  money spent, no other task type touched. No Assemble,
  no teleport, no purchase.
