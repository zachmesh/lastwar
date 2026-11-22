---
title: Alliance donations queue run 0359
created: 2026-11-22T11:59:00Z
modified: 2026-11-22T11:59:00Z
level: L0
version: 1.0.0
description: Queue unit donations-2026-11-22-1119, ticker-0334 - re-read after the 0304 cooldown, Donation Count 1/30 live on both nodes, changed route held, no donation made
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-22 03:46-03:59 PT
  - source: unit donations-2026-11-22-1119 in _queue_/done
  - source: _activities_/alliance-donations/INDEX.md hard closing rule (live read or unverified) and changed route (do not tap from 1/30)
---

# Alliance donations queue run 0359 (ticker-0334)

Unit donations-2026-11-22-1119, regular donations,
activity alliance-donations, priority 2, est 7 minutes,
not_before 2026-11-22T11:40:00Z (03:40 PT). Executor
ticker-0334. Session window about 03:46 to 03:59 PT.
Computer session cc-93, LastWar window 105986, no
session drop, no other-device dialog. Token held
03:37 to 03:59 PT (renewed once near expiry).

## Outcome

Partial - this is the re-read unit the 0304 pass enqueued
for after its 00:18:47 cooldown. Donation Count read live
1/30 on Quick Construction AND 1/30 on Rallied Attack -
the same count on both nodes, supporting a shared/global
remaining count (the 0129 paired-read finding, against
the 2350 split read). Per the standing changed route, no
tap was made from 1/30 on either node, so no donation was
dispatched this unit and the count stays 1/30 live-read.
The tracker stays untouched and a named re-read unit is
enqueued for after the next refill (not_before 12:15 UTC,
04:15 PT). The unit closed inside the 15 minute cap
(about 13 minutes of execution).

## Entry and reads (live reads only)

- Base view at entry: food 760.8M, iron 1.1G, coin 103.9M,
  diamonds 6,436, power 149,417,850, lightning 120,
  hammer 1/4 (red dot), flask 2/2, Events badge 1, VS red
  dot, Build: Oil Well (0/1), WORLD badge 43.
- Alliance shield tapped at the fresh measured label area
  (930,721) from the current screenshot and opened the
  Alliance menu on the first try. Alliance menu live:
  [AP3x] The Apex, Overall Rating 5.0, Leader Abyss Apex,
  Power 14,383,191,808, Members 99/100, Language English.
  Help, Alliance Gifts and Alliance Store carry red dots.
  Alliance Star (Event 42) banner read Time Left 14:06:20,
  not entered.
- Alliance Techs tile tapped at (666,655) from the current
  screenshot, opened on the first try. Development tab
  live: Auto Rally Max Level, Quick Construction 9/10
  carrying the red thumbs-up recommended marker, Great
  Helper Max Level, one node below at 2/10. Tech Donation
  Today footer 5300 at entry and at close (display only,
  disqualified per Issue #558, never a closing figure).
  Top-bar badge item 346.5K, unchanged since the 0304
  close.
- Quick Construction panel live: Increased Building Speed
  for Allies, Donation Reward +20%, Tech EXP Required
  3.6M/8.0M, Current +22.5%, Next Level +25%, Donation
  Reward EXP 50 and badge 50 per donation. Coin Donate
  1000 GREEN with no cooldown timer; diamond Donate 2
  never used. Donation Count read live 1/30.
- War tab: two drags (500,550) to (500,300) scrolled the
  tree; both drags returned outcome_unknown receipts, and
  the screenshots after each verified the scrolls worked,
  so the same method was used twice on verified effect,
  not blindly repeated. Tree read live: Unit Load Capacity
  2/10, Quick Training 1/10, Expert Trainer 2/10, World
  Interception 5/10, Rapid Siege 5/10, Quick Garrison 5/10,
  Troop Movement 5/10, Rallied HP 7/10, Rallied Attack 7/10,
  Rallied Defense 7/10, Expert Nurse below the fold. No
  red-panda recommended badge was seen on the visible
  tiles; the thumbs-up above the Development tab is fixed
  and is not a node marker.
- Rallied Attack panel live: Increased Hero Attack in
  Rallies for Allies, 7/10, Current +7%, Next Level +8%,
  Tech EXP Required read as 25.4K/4.5M by OCR (garbled -
  flagged, not relied on), Donation Count read live 1/30,
  coin Donate button green. No tap was made from this
  1/30 either.

## Refill data point

- The count refilled 0 to 1 between the 0304 unit's last
  tap (about 03:20, button greyed 00:18:47) and this
  unit's live 1/30 read (about 03:52) - about 30 minutes
  for one count. Against the 0304 unit's 0 to 1 in about
  10 minutes, the refill stays bursty or clock-anchored,
  not linear. The refill-model issue the 0113 unit filed
  stays open; this unit's data point (0 to 1 in about 30
  minutes) is added to it.

## Cross-reads for the scout chain

- Blue-building count-up timer: 09:43 at about 03:50 and
  09:44 at about 03:52, read at the right edge behind the
  panels - the +1 per minute count-up is corroborated a
  third time (08:08 at about 02:19 to 09:44 at about 03:52
  is +96 over about 93 minutes). The building identity
  stays open for scout seq 15.
- Right-edge long timer: 14:16:35 at about 03:47. Rocket
  model (zero near the 18:00 reset) predicts about 14:13,
  about 3 to 4 minutes off; green-clock model predicts
  about 13:49, about 27 minutes off. Third datapoint
  favoring the rocket identification.
- Lightning: the scout unit's close OCR read of 114 is
  RESOLVED as an OCR misread of the hammer "1/4" - the
  lightning counter reads 120 in this unit's screenshots
  at entry and at close. No 6-point drop happened.

## Notes

- No diamonds or money spent. No red-line contact. The
  diamond Donate button was never tapped. Coin balance
  unchanged at 103.9M.
- The game was left on the ALLIANCE TECHS War tab (panel
  closed with its X, first try); the next unit navigates
  from there.
