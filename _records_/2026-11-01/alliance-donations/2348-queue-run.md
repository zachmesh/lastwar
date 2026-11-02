---
title: Queue Run 2348 Alliance Donations Partial Unverified Close
created: 2026-11-02T07:48:00Z
modified: 2026-11-02T07:48:00Z
level: L0
version: 1.0.0
description: Ticker pass ticker-2334 donations unit donated coin donations to Rallied HP from a live-read 11 remaining down to a live-read 1 remaining, then one last donation, final count hidden by a cooldown timer so the close is unverified
status: unverified
grounded_in:
  - source: game screens observed on the owner Mac mini during this pass
---

# 2348 queue run - alliance donations, partial (unverified close)

Session window: 2026-11-01 about 23:35 to 23:48 America/Los_Angeles.
Executor: ticker-2334. Unit: donations-2026-11-01-2203 (regular
donations, activity alliance-donations, priority 2, expires
2026-11-02T06:03:00Z). Status: partial. The tracker is untouched
and a named re-read unit is enqueued for after the cooldown, per
the hard closing rule in the activity metadata: the final count
could not be read live because a cooldown timer hides it.

## Outcome

- Target: Rallied HP, War tab, level 5/10, Current plus 5 percent,
  Next Level plus 6 percent, Tech EXP 1.9M/2.0M, Donation Reward
  plus 20 percent. Coin button cost 600 coin per donation;
  the diamond button (2 diamonds) was never used.
- Donation Count, every figure read live in this unit: 11/30 at
  entry, then 10/30, 9/30, 8/30, 7/30, 6/30 (image-verified;
  the compact OCR misreads 6 as 5), 5/30, 4/30, 3/30, 2/30,
  1/30, one coin tap each. Ten coin donations are confirmed
  by those two live reads at the ends of the chain.
- One last coin donation was then dispatched from the
  live-read 1/30. The button greyed with a 00:05:39 cooldown
  timer (00:05:20 on the closing screenshot), hiding the count
  label. The 0/30 final is therefore NOT claimed as a live
  read: it is the expected result of 1 remaining minus 1
  dispatched tap, but the count itself was not seen after
  that tap. The unit closes unverified on that point, and the
  re-read unit enqueued for about 23:55 local will confirm
  the count.
- Tech Donation Today footer: 800 at entry, 850 after the
  first donation. The footer points are recorded as observed
  only; they are not converted into a count.
- Nothing else spent: no diamonds, no money, no speedup items,
  no stamina items. No other regular was merged into this unit.
  The game was left on the Rallied HP panel with the coin
  button greyed under its cooldown timer.

## Count replenishment observation (knowledge gap, GitHub Issue #160)

- Entry count was 11/30, although the previous donations unit
  (ticker-1934, 19:44) left the same Rallied HP panel at a
  live-read 1/30 plus one dispatched tap. Between about 19:54
  and 23:35 the remaining count rose from 1 (or 0) to 11 with
  no donations unit in between and no record of any other
  donation. The metadata model of a fixed daily 30 that only
  falls does not explain this rise. The count appears to
  replenish over time, roughly 1 per 20 minutes across this
  interval, but the mechanism (rate, cap, timer link) is
  unmeasured. Filed as a GitHub Issue from this record; the
  activity metadata hard closing rule still binds every unit
  until the mechanism is measured.

## Method notes (rule R2)

- Entry: Alliance tile taps at norm 885,660 and 885,673 hit
  above the tile and opened nothing; visual grounding on the
  fresh base screenshot put the Alliance tile at norm
  924,713 (and 935,701 after the relaunch) and that tap
  opened the Alliance menu. Tile centres must be re-grounded
  from the screenshot on every opening, never inherited.
- Alliance Techs tile at norm 686,676 (688,690 after the
  relaunch); Rallied HP node at norm 272,506 (268,515 after
  the relaunch). Coin Donate button at norm 658,761.
- The game app quit mid-unit during a batched tap sequence:
  the first batch click dispatched, the second failed with
  the app exited. The batch click did not land (count stayed
  10/30 and the footer stayed 850). The app was relaunched,
  no different-device dialog appeared, no login or
  verification was demanded, and the panel was re-entered
  and re-read live before donating resumed. Single taps
  were used for the rest of the unit.
- A tap on the coin button surfaced the tooltip "Hold down
  for continuous donations" - the button supports hold to
  donate continuously. Not used in this unit; noted for a
  later unit to test against the live-read closing rule.
- No different-device dialog was seen, no login or
  verification was demanded, and no password or Touch ID
  step was used.

## Red lines

- Coin button only. No diamond button tapped, no purchase, no
  speedup item burned, no building or research started.

## Follow-up

- Re-read unit enqueued for after the cooldown (not before
  about 23:55 local): open the Rallied HP panel and read the
  Donation Count live. If it reads 0/30, the day is done and
  the tracker may be marked done; if it reads 1/30, the last
  tap did not land and one more coin donation is due. If it
  reads above 1/30, the replenishment mechanism is confirmed
  and the count model needs revision.
- Tracker untouched (partial unit).
