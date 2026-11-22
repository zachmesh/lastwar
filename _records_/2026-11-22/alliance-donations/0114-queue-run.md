---
title: Alliance donations queue run 0114
created: 2026-11-22T09:21:00Z
modified: 2026-11-22T09:21:00Z
version: 1.0.0
description: Queue unit donations-2026-11-21-2203, ticker-0113 - 24 coin donations verified live on Quick Construction, Donation Count 30/30 to 6/30 live, final batch of 6 dispatched but final 0/30 not live-read (cooldown timer hides the count), closed partial with the button greyed on a cooldown timer
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-22 01:14-01:22 PT
  - source: unit donations-2026-11-21-2203 in _queue_/done
  - source: _activities_/alliance-donations/INDEX.md hard closing rule (live read or unverified)
---

# Alliance donations queue run 0114 (ticker-0113)

Unit donations-2026-11-21-2203, regular donations,
activity alliance-donations, priority 2, est 7 minutes,
expires 2026-11-22T10:03:00Z (02:03 PT). Executor
ticker-0113. Session window about 01:14 to 01:22 PT.
Computer session cc-77, LastWar window 105986, no
session drop, no other-device dialog. Token held
01:13 to about 01:22 PT.

## Outcome

Partial - 24 coin donations verified live, Donation
Count 30/30 to 6/30 by live reads. A final batch of
6 was dispatched and the coin button then greyed
with a green 00:18:14 cooldown timer, which hides
the count label, so the final 0/30 was NOT read
live. Per the hard closing rule the unit closes
partial with verified no for the full 30, the
tracker stays untouched, and a named re-read unit
is enqueued for after the cooldown (about 09:48
UTC). The unit closed well inside the 15 minute cap (6 minutes
10 seconds of execution, unit started 09:15:25Z and finished
09:21:35Z), on the button greying with the cooldown timer - no
further donation was possible in this unit.

## Entry route

- Base view at entry was the default framing with
  the full UI present (avatar Lv.30, total power
  149,417,850, right column Events, VS, Alliance,
  Mail, Inventory, HEROES / WORLD bottom bar).
- Alliance shield tapped at the fresh measured
  centre (904,728) and opened the Alliance menu on
  the first try. This is about 40 normalized units
  left of the 2142 unit's (943,719) and about level
  with the metadata's (903,787) in x but higher in
  y - the shield icon sits above its label, and
  the label centre is lower. Entry-route blocker
  from 2026-11-02 is resolved on this framing.
- Alliance menu live: [AP3x] The Apex, Leader
  Abŷss Apex, Power 14,360,841,109, Members
  99/100. Alliance Star (Event 42) banner read
  Time Left 16:33:01, not entered.

## Donations made (live reads only)

- Alliance Techs, Development tab: Auto Rally Max
  Level, Quick Construction 9/10 carrying the red
  thumbs-up recommended marker, Great Helper Max
  Level, one node below at 2/10 (unread, off the
  first screen). Tech Donation Today footer 750 -
  not account-attributable (Issue #558), not used
  as a count.
- Quick Construction panel live: Increased Building
  Speed for Allies, Donation Reward +20%, Tech EXP
  Required 3.5M/8.0M at entry and 3.6M/8.0M at
  close, Current +22.5%, Next Level +25%,
  Donation Reward EXP 50 and badge 50 per
  donation. Coin Donate 1000 per donation; diamond
  Donate 2, never used.
- Donation Count live reads: 30/30 at entry, 27/30
  after batch 1 (3 taps on the green coin Donate
  button), 24/30 after batch 2 (3 taps), 18/30
  after batch 3 (6 taps), 12/30 after batch 4
  (6 taps), 6/30 after batch 5 (6 taps). Batches
  of 6 land cleanly - no missed taps in this unit.
- Final batch 6 (6 taps) dispatched at about
  01:21 PT; the closing screenshot shows the coin
  button greyed with a green 00:18:14 timer above
  Donate and no count label. The greyed button
  with timer is consistent with the count reaching
  0, but the 0/30 itself was never read live, so
  the 6 are recorded as dispatched, not verified.
- Verified spend: 24,000 coin (24 x 1000). If the
  final 6 landed, 30,000 coin. Tech EXP +1200
  verified by the panel rounding (3.5M to 3.6M).
  Badge count in the top bar moved 342.5K to
  345.8K across the unit - the per-batch steps
  (+300, +400, +600, +600, +600) do not match 50
  per donation, so that bar is not used as
  evidence for the donation count.

## New observation - the count regenerates

- Donation Count read 30/30 at entry although the
  previous unit (ticker-2142, 21:44-21:58 PT) left
  it at 24/30 live, in the same reset day (reset
  19:00 PT). Six counts returned within about 3
  hours 16 minutes - roughly one per 33 minutes -
  or the count resets at local midnight, which
  this window also crossed. Either way the
  metadata's flat "30 donations a day, burn them
  down early" model is incomplete: the count
  refills during the day, and a unit that finds
  30/30 late in the day is not seeing a fresh day.
  The quota checkpoints of rule R3 should be read
  against a refilling count, not a fixed daily 30.
  Filed as an issue from this unit (see unit
  result).
- Tooltip seen after batch 1: "Hold down for
  easier continuous donations" - a long-press on
  Donate may donate continuously and could speed
  later units; untested, left for a later unit.

## Notes

- An alliance announcement banner crossed the top
  during batch 4 ("Important: President HawksMav
  appointed ... as Secretary") - game chatter,
  no action taken.
- No diamonds or money spent. No red-line
  contact. The diamond Donate button was never
  tapped.
