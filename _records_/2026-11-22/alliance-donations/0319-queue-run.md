---
title: Alliance donations queue run 0319
created: 2026-11-22T11:20:00Z
modified: 2026-11-22T11:20:00Z
version: 1.0.0
description: Queue unit donations-2026-11-22-0921, ticker-0304 - re-read after the 0113 cooldown, Donation Count 5/30 then 1/30 live, 6 coin donations dispatched, final 0/30 never live-read (cooldown timer hides the count), closed partial
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-22 03:06-03:20 PT
  - source: unit donations-2026-11-22-0921 in _queue_/done
  - source: _activities_/alliance-donations/INDEX.md hard closing rule (live read or unverified)
---

# Alliance donations queue run 0319 (ticker-0304)

Unit donations-2026-11-22-0921, regular donations,
activity alliance-donations, priority 2, est 7 minutes,
not_before 2026-11-22T09:48:00Z (01:48 PT). Executor
ticker-0304. Session window about 03:06 to 03:20 PT.
Computer session cc-88, LastWar window 105986, no
session drop, no other-device dialog. Token held
03:06 to about 03:20 PT.

## Outcome

Partial - this is the re-read unit the 0113 pass
enqueued for after its 00:18:14 cooldown. Donation
Count read live 5/30 at entry, 5 coin donations
dispatched, the coin button then greyed with a
green 00:09:37 cooldown timer hiding the count
label. The cooldown was waited out inside the
unit (about 9 minutes 40 seconds) and the count
re-read live at 1/30 - one refill inside about 10
minutes. One more coin donation dispatched and the
button greyed again with a 00:18:47 timer, the
count label hidden again. The final 0/30 was never
read live in this unit, so per the hard closing
rule the unit closes partial with verified no for
the full 30, the tracker stays untouched, and a
named re-read unit is enqueued for after the new
cooldown (about 11:40 UTC, 03:40 PT). The unit
closed inside the 15 minute cap (about 14 minutes
of execution).

## Entry - network error at login

- At entry the game showed a "Network connection
  error. Please check your connection and try
  logging in again." dialog with Contact and
  Reconnect buttons, over the base view (total
  power 149,417,850, the same account state the
  0113 pass saw).
- A click on the Reconnect OCR element did
  nothing (no change observed); a coordinate tap
  on the button's measured centre (625,567)
  reconnected at once - the dialog cleared and
  the base view returned. Per R2 the failed
  element click was not repeated; the method
  changed to the measured coordinate.
- Base view at re-entry: food 760.8M, iron 1.1G,
  coin 103.9M, stamina 120, badges 17.72K.

## Donations made (live reads only)

- Alliance shield tapped at the fresh measured
  centre (917,726) from the screenshot and opened
  the Alliance menu on the first try. Alliance
  menu live: [AP3x] The Apex, Leader Abyss Apex,
  Power 14,383,191,808, Members 99/100. Alliance
  Star (Event 42) banner read Time Left 14:42:20,
  not entered.
- Alliance Techs, Development tab: Auto Rally Max
  Level, Quick Construction 9/10 carrying the red
  thumbs-up recommended marker, Great Helper Max
  Level, one node below at 2/10. Tech Donation
  Today footer 4450 - alliance-wide, not
  account-attributable, not used as a count.
- Quick Construction panel live: Increased
  Building Speed for Allies, Donation Reward +20%,
  Tech EXP Required 3.6M/8.0M at entry and at
  close, Current +22.5%, Next Level +25%,
  Donation Reward EXP 50 and badge 50 per
  donation. Coin Donate 1000 per donation; diamond
  Donate 2, never used.
- Donation Count live reads: 5/30 at entry. A
  batch of 5 taps on the green coin Donate button
  (649,762) dispatched in about 2.9 seconds; the
  button then greyed with a green 00:09:37 timer
  and no count label. After the wait the count
  re-read live at 1/30 with the button green
  again. A single tap dispatched the last one;
  the button greyed with a green 00:18:47 timer
  and no count label.
- The greyed button with timer is consistent with
  the count reaching 0 - in the 0113 unit the
  button stayed green with a visible count after
  every batch that left a remainder, and greyed
  only on the zeroing batch - but the 0/30 label
  itself was never read live, so the 6 donations
  are recorded as dispatched, not verified.
- Verified spend: 6,000 coin dispatched (6 x
  1000). Panel rates imply Tech EXP +300 and
  badge +300; the Tech EXP panel rounding (3.6M
  to 3.6M) cannot confirm it. Badge count in the
  top bar moved 345.8K to 346.4K across the batch
  of 5 (+600) and to 346.5K after the single tap
  (+100) - per-donation steps that do not match
  50 per donation, so that bar is not used as
  evidence for the donation count, as the 0113
  record already established.

## New observation - the count refills inside 10 minutes

- The count read 1/30 live at 03:18 after the
  button had greyed at about 03:09 (the zeroing
  batch of 5). One count returned inside about 10
  minutes - faster than the roughly 1-per-22-to-33
  minute linear rate implied by the 0113 data
  (6 in about 3 hours 16 minutes; 5 in about 1
  hour 49 minutes). The refill is bursty or
  clock-anchored rather than linear, and a
  "0/30" state is transient: any re-read after a
  cooldown can find a fresh remainder. The
  refill-model issue the 0113 unit filed stays
  open; this unit's data point (0 to 1 in about
  10 minutes) is added to it.
- Cooldown timer lengths observed: 00:09:37 after
  the batch of 5, 00:18:47 after the single tap -
  no relation to batch size.

## Notes

- No diamonds or money spent. No red-line
  contact. The diamond Donate button was never
  tapped.
- The "Hold down for easier continuous donations"
  tooltip appeared after the batch of 5, as in
  the 0113 unit; long-press continuous donation
  remains untested.
