---
title: Alliance donations closing standard
created: 2026-11-23T10:32:26Z
modified: 2026-11-23T17:56:31Z
version: 0.2.0
description: The Researcher's rulings of 2026-11-23 on what closes a donations unit and what a grey Donate means, verbatim, behind digest rules 4 and 6
---

# Alliance donations closing standard

Researcher rulings of 2026-11-23, tested, amended the same day (`_records_/2026-11-22/research/donation-close-amendment.md`). Records `_records_/2026-11-22/alliance-donations/1012-t1-test.md` and `_records_/2026-11-22/alliance-donations/1745-queue-run.md`.

## What closes a unit (digest rule 6)

"A count figure needs a live read in the same unit. After the last tap the count is hidden by design; close as count spent when the live count before that tap was 1/30, the Donate turned from green to grey with a timer, and the timer end lies on the 20-minute refill grid within 3 s. A rise of the badge item or Tech EXP by 0.1K corroborates and is read when it is in the same frame; it is not required, since the 0.1M EXP bar at Quick Construction cannot move. Write the timer, its read time and the UTC time of the last tap. If the end is off the grid or unread, close unverified unless a witness rose. Never write a count after the last tap, derive one by arithmetic, or take one from the footer."

No re-read unit is owed for the last donation; cadence follows rule 8. An off-grid end means a regime change or a misread: re-anchor on it.

## What a greyed tap means (digest rule 4)

"Verify each tap by the live count falling by one. For the last count the text becomes a grey timer: the tap landed when the green Donate turned grey with a timer; the timer end on the refill grid within 3 s confirms it; Tech EXP or the badge item rising 0.1K corroborates, and the 0.1M EXP bar at Quick Construction is blind. A witness that stays put is blind or unread, not an eaten tap. Do not wait out the timer to judge a tap: the count after it read 1/30 for witnessed and unwitnessed taps alike."
