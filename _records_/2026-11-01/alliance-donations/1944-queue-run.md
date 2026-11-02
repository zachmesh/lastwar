---
title: Queue Run 1944 Alliance Donations Partial Unverified Close
created: 2026-11-02T03:55:00Z
modified: 2026-11-02T03:55:00Z
level: L0
version: 1.0.0
description: Ticker pass ticker-1934 donations unit donated coin donations to Rallied HP from 8 remaining to a live-read 1 remaining, then one last donation, final count hidden by a cooldown timer so the close is unverified
status: unverified
grounded_in:
  - source: game screens observed on the owner Mac mini during this pass
---

# 1944 queue run - alliance donations, partial (unverified close)

Session window: 2026-11-01 about 19:44 to 19:54 America/Los_Angeles.
Executor: ticker-1934. Unit: donations-2026-11-01-1803 (regular
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
- Donation Count, every figure read live in this unit: 8/30 at
  entry, 7/30 after the first coin tap, 6/30 after the second
  (image-verified; the compact OCR misread 6 as 5), then a
  batch of 6 coin taps dispatched in 2.4 seconds. The coin
  button then greyed with a 00:04:56 cooldown timer, hiding
  the count label.
- Cooldown waited out inside the unit: the panel was re-opened
  after the timer read 00:02:11, waited a further 140 seconds,
  and the count reappeared as a live-read 1/30. That proves
  7 coin donations landed in this unit (8 down to 1); the
  sixth batch tap hit the already-greyed button and did not
  land. No arithmetic final is claimed for the batch itself:
  the 7 is fixed by the two live reads, 8/30 and 1/30.
- One last coin donation was then dispatched from the
  live-read 1/30. The button greyed again, this time with a
  00:18:42 timer, hiding the count label once more. The
  0/30 final is therefore NOT claimed as a live read: it is
  the expected result of 1 remaining minus 1 dispatched tap,
  but the count itself was not seen after that tap. The unit
  closes unverified on that point, and the re-read unit
  enqueued for about 20:15 local will confirm the count.
- Tech Donation Today footer: 0 at entry, 750 after the first
  donation phase. The footer points are recorded as observed
  only; they are not converted into a count, because the
  metadata carries two different per-donation figures (50 and
  60) and 750 does not divide by the 7 live-counted donations
  under either figure, so the footer cannot close the count.
- Nothing else spent: no diamonds, no money, no speedup items,
  no stamina items. No other regular was merged into this unit.
  The game was left on the Rallied HP panel with the coin
  button greyed under its 00:18:42 timer.

## Method notes (rule R2)

- Entry: the first Alliance tile tap at norm 902,831 and the
  second at norm 903,800 both opened Mail, not the Alliance
  menu; visual grounding on the base screenshot put the
  Alliance tile at norm 930,705 and the Mail tile at
  norm 930,785, and the 930,705 tap opened the Alliance menu.
  Tile centres must be re-grounded from the screenshot on
  every opening, never inherited.
- The Alliance Techs tap at norm 700,631 landed on Members
  (row boundary); the OCR-grounded Techs label row at
  norm 700,679 opened Alliance Techs. The Members detour was
  exited with the back arrow, and the Rallied HP node at
  norm 300,480 opened its donation panel.
- The Alliance menu back arrow failed twice at norm 97,946
  with no change (background clicks do not reach that
  control); the method was abandoned per R2 and the game
  was left on the Alliance menu, which the next session
  resumed from without loss. No Esc key was used.
- One stale-observation retry: a click refused as target
  exited or restarted dispatched nothing; re-selecting the
  same LastWar window and clicking with a fresh observation
  id succeeded, so no donation was lost or doubled by it.
- No different-device dialog was seen, no login or verification
  was demanded, and no password or Touch ID step was used.

## Red lines

- Coin button only. No diamond button tapped, no purchase, no
  speedup item burned, no building or research started.

## Follow-up

- Re-read unit enqueued for after the 00:18:42 cooldown
  (not before about 20:15 local): open the Rallied HP panel
  and read the Donation Count live. If it reads 0/30, the
  day is done and the tracker may be marked done; if it
  reads 1/30, the last tap did not land and one more coin
  donation is due.
- Tracker untouched (partial unit).
