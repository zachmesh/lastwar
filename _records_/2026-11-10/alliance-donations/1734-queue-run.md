---
title: Alliance donations queue run 1734
created: 2026-11-10T17:34:00-08:00
modified: 2026-11-10T17:34:00-08:00
version: 1.0.0
description: Donations unit donations-2026-11-10-1403, 17 coin donations to Quick Construction, final count unreadable behind cooldown timer, re-read unit enqueued
status: partial
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-10 17:15-17:34 PST
---

# Alliance donations queue run 1734

- Unit: donations-2026-11-10-1403, executor ticker-1704, sessions cc-484 (closed mid-unit, replaced) and cc-486.
- Window: 17:15-17:34 PST.

## Entry-route blocker broken

- The base camera was panned to the map top edge by the arms-race unit's missed hammer tap. Two drags moved it only partly (first drag worked, second barely moved at the map edge); scroll did nothing. Tapping the gold-star building marker at (589, 310) restored the default base framing with all edge icons visible.
- Alliance shield tapped at the fresh measured centre (927, 715) in this 642x951 window opened the Alliance menu at once. Note: the R2 note's (903, 787) does not match this window geometry - the working point here is (927, 715). The 2026-11-02 entry blocker (three failed units) is broken by this route.
- Alliance Techs tile tapped; Development tab shown.

## Live reads

- Tech Donation Today: 7600 at entry, 9300 at close (delta +1700).
- Quick Construction 8/10 (Increased Building Speed for Allies, +20%, Tech EXP 2.9M/6.0M, Next Level +22.5%), recommended marker (red thumbs-up) on its tile.
- Donation Count (remaining) read live: 17/30 at entry, 16/30 after 1 donation, 8/30 after 9 donations.
- Donate buttons: green coin Donate 900, yellow diamond Donate 2 (never used).

## Donations made

- 17 coin donations to Quick Construction in this unit: 1 single tap, then a batch of 8, then a batch of 8. Coin cost 900 each, 15,300 total. Coin HUD stayed 97.8M (rounding).
- After the last batch the green button greyed with a 00:04:21 cooldown timer, and the Donation Count label vanished behind the timer - the exact R1 trap.

## Closing state - unverified

- The final Donation Count was NOT read live (hidden by the timer), so this unit closes partial, not done, per the hard closing rule. The tracker is untouched.
- Corroboration, not a closing figure: footer delta +1700 over exactly 17 taps in this unit. If one donation is worth 100 contribution points, that is exactly 17 donations and the count is 0/30. The per-donation point value is not settled in the records (50 and 60 both appear in older notes), so the footer alone does not close the count.
- Re-read unit enqueued: donations-2026-11-11-0122, priority 2, not_before 2026-11-11T01:40:00Z (after the 00:04:21 cooldown ends about 17:38), to read the Donation Count live and close the day.

## Notes

- Session cc-484 closed on its own mid-unit (observe returned observation_unavailable); session cc-486 was started and LastWar re-selected, no game state lost.
- One batched click set failed once with privacy_unverified and dispatched nothing; a re-observe cleared it and the batch then ran clean.
- Nothing spent except the 15,300 coin in donations. No diamonds, no speedups, no stamina items.
- Oil Well construction timer seen on the base: 1d 09:08:00 remaining - no building completion lands inside the current Arms Race phase (corroborates the arms-race unit's tier-3 shortfall).

## Result

- Status: partial. Target 30 of 30, achieved unverified (17 donations made this unit, final count unreadable). Verified no. Blocker category d (inference over live read refused - the timer hides the count; the unit refuses to close on arithmetic).
- Follow-up: re-read unit donations-2026-11-11-0122 (not_before 01:40Z).
