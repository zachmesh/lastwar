---
title: Alliance donations closing standard
created: 2026-11-23T10:32:26Z
modified: 2026-11-23T10:32:26Z
version: 0.1.0
description: The Researcher's rulings of 2026-11-23 on what closes a donations unit and what a grey Donate means, verbatim, behind digest rules 4 and 6
---

# Alliance donations closing standard

Researcher rulings of 2026-11-23, status tested, on the records `_records_/2026-11-22/alliance-donations/1012-t1-test.md` and `_records_/2026-11-22/alliance-donations/0319-queue-run.md`; the full note is `_records_/2026-11-22/research/donation-close-ruling.md`. The [rule digest](rule-digest.md) rules 4 and 6 and the card's R2 point here.

## What closes a unit (digest rule 6)

"A count figure needs a live read in the same unit. After the last tap the count is hidden by design; close as count spent when the live count before that tap was 1/30, the Donate turned from green to grey with a timer, and a witness that can move rose 0.1K. Write the timer and the UTC time. Never write a count after the last tap, derive one by arithmetic, or take one from the footer."

No re-read unit is owed for the last donation; cadence follows the refill log of rule 8. An entry at 1/30 has no calibration tap: close it flagged uncalibrated.

## What a greyed tap means (digest rule 4)

"Verify each tap by the live count falling by one. For the last count the text becomes a grey timer: the tap landed when the green Donate turned grey with a timer; Tech EXP or the badge item rising 0.1K corroborates, and the 0.1M EXP bar at Quick Construction is blind. A witness that stays put is blind or unread, not an eaten tap. Do not wait out the timer to judge a tap: the count after it read 1/30 for witnessed and unwitnessed taps alike."

The clause "unlanded until re-read after its timer" came from the 2026-11-08 units, whose re-read a refill also produces; those records stand, the rule goes.
