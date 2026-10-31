---
title: Alliance donations queue run 1437
created: 2026-10-31T21:57:00Z
modified: 2026-10-31T21:57:00Z
version: 1.0.0
description: Donations queue unit donations-2026-10-31-1403 - partial, one coin donation to Rallied HP, then the Mac control channel stalled
status: partial
---

# Alliance donations — execution, 2026-10-31 1437 queue unit

Ticker pass ticker-1437. Unit donations-2026-10-31-1403, priority 2,
claimed by ticker-1437. Computer session cc-668 on the owner's Mac mini.

Status — partial: 1 coin donation was made to Rallied HP, and the unit
stopped when the Mac control channel stalled, not when the donation
work was finished. The tracker is untouched; the next tick re-produces
this regular.

## What was done

- Game already open on the Mac mini in the 642x951 window, on the Events
  hub Arms Race Hero Advancement stage (score 41,500, thresholds
  2,000 / 4,000 / 12,000, about 00:19 left at first read). That stage
  belongs to the arms-race unit, not this one, and nothing was claimed
  or changed there. Back arrow returned to base.
- Base to Alliance (right-rail Alliance button, norm 903,689), then to
  Alliance Techs. One mis-tap on the way: the first Alliance Techs tap
  at norm 732,573 opened the Member List instead, so the unit went back
  and re-grounded the tile on its own screenshot — the grounded centre
  norm 691,662 opened Alliance Techs correctly. Do not reuse 732,573
  for this tile.
- Alliance Techs, War tab, at entry: Troop Movement 5/10, Rallied HP
  5/10 (the tile carrying the marker), Rallied Attack 7/10, Rallied
  Defense 7/10, next node 1/10. Tech Donation Today 5150, already above
  the 1000-point ranking-reward gate, so no hand claim exists in this
  flow per the activity metadata.
- Rallied HP panel (grounded centre norm 270,505): Increased Hero HP in
  Rallies for Allies, Tech EXP 1.1M/2.0M, Current +5%, Next Level +6%,
  Donation Reward 50 + 50, Donation Count 13/30 at entry. The coin
  Donate button costs 600 coin; the diamond Donate button (2 diamonds)
  was never tapped.
- One coin donation: the green coin Donate button, grounded centre
  norm 658,762, was tapped once. The next screenshot read Donation
  Count 12/30, confirming exactly one donation landed (600 coin).
  Coin balance at the top stayed 177.1M at HUD rounding.

## Why the unit stopped

- The second coin Donate tap, and every Mac control call after it,
  timed out at the device gateway: click (120 s), computer.observe
  image (120 s), computer.observe compact (120 s), connection.health
  (25 s), connection.repair web (25 s), and one final computer.observe
  compact retry (120 s) all returned node_invoke_timeout. The Mac
  itself still listed as online in device.list, so this is a stalled
  control channel, not a confirmed logout or a different-device dialog
  — no such dialog appeared at any point in this unit.
- Whether the second tap dispatched before the stall is unknown: the
  Donation Count was last verified at 12/30, so this record claims
  only the one confirmed donation. The next unit must re-read the
  count before donating, and must not assume the second tap landed.
- Computer session cc-668 could not be ended cleanly because the
  control channel was already stalling; the session end was not
  attempted again after the unit was completed, to avoid another
  120-second stall past the unit lease. The next pass starts a fresh
  session as usual.
- Chrome stayed frontmost throughout, as in earlier units, but
  background input to the game window worked normally until the
  channel stall — the stall is not the Chrome-foreground blocker
  seen in the 1105, 1145 and 1304 units.

## Remaining work

- Donations remaining on the Rallied HP panel at last verified read:
  12/30, cost 600 coin each, until the coin button greys with its
  timer. Then stop for that run, per the activity metadata.
- No diamonds spent, no money spent, no other task type touched.
  The arms-race stage seen at entry was left exactly as found.
