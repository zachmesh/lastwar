---
title: Ruling - how a donations unit closes and what a greyed tap means
created: 2026-11-23T02:36:00-08:00
modified: 2026-11-23T02:36:00-08:00
level: L0
version: 1.0.0
description: Researcher rulings on the two tensions after the T1 rewrite - the closing rule for a unit whose last tap hides the count, and the rule that judged a greyed tap by a re-read after its timer
status: unverified
grounded_in:
  - source: _records_/2026-11-22/alliance-donations/1012-t1-test.md, a tap from 1/30 landed, green to grey at +2.9 s, EXP and badge +0.1K
  - source: _records_/2026-11-22/alliance-donations/0319-queue-run.md, green after every batch that left a remainder, grey only on the zeroing batch, timers 9:37 then 18:47
  - source: donation-timer-evidence.csv, eleven taps from 1/30
---

# Ruling

**1. Card R2 and digest 6 (what closes a unit).** Close on evidence of the state you claim. Replace both with: "A count figure needs a live read in the same unit. After the last tap the count is hidden by design; close as count spent when the live count before that tap was 1/30, the Donate turned from green to grey with a timer, and a witness that can move rose 0.1K. Write the timer and the UTC time. Never write a count after the last tap, derive one by arithmetic, or take one from the footer." Status tested, 2026-11-23, `1012-t1-test.md`, `0319-queue-run.md`. No re-read unit is owed for the last donation; cadence follows the refill log of rule 8.

**2. Digest 4 (what a greyed tap means).** Replace with: "Verify each tap by the live count falling by one. For the last count the text becomes a grey timer: the tap landed when the green Donate turned grey with a timer; Tech EXP or the badge item rising 0.1K corroborates, and the 0.1M EXP bar at Quick Construction is blind. A witness that stays put is blind or unread, not an eaten tap. Do not wait out the timer to judge a tap: the count after it read 1/30 for witnessed and unwitnessed taps alike." Same status and records. The clause "unlanded until re-read after its timer" came from the 11-08 units, whose re-read a refill also produces; those records stand, the rule goes.

**Why they fit.** R1 says tap on, rule 4 says how the last tap is known, R2 says what may be claimed. In 0319 the button greyed only on the zeroing tap, never at a count of 2 or more.

**For the scribe.** Failures line "count hidden by timer" becomes "by design after the last tap; close on the witness". Replace open question 2 with: "Does the badge item witness every node? Test: read it before and after a counted tap at Quick Construction and at Rallied Attack; run by operator."

**For the coordinator.** Tracker policy is yours: what a day total means under a refilling pool, and whether a spent-count close is done. An entry of 1/30 has no calibration tap: close it flagged uncalibrated.
