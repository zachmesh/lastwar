---
title: Queue Run 1034 Alliance Donations Re-read
created: 2026-11-08T18:35:00Z
modified: 2026-11-08T18:35:00Z
level: L0
version: 1.0.0
description: Donations unit donations-2026-11-08-1621, re-read after cooldown, partial - three verified coin donations 4/30 to 1/30 on Quick Construction, stopped at the live-read 1/30 floor per the changed route
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-08 about 10:24-10:34 America/Los_Angeles
---

# 1034 queue run - alliance donations re-read (donations-2026-11-08-1621)

- Unit: donations-2026-11-08-1621, executor ticker-1017.
  Status: partial - three coin donations landed, each verified
  by a live count re-read, 4/30 to 1/30 on Quick Construction.
  The unit stops at the live-read 1/30 and does NOT tap from
  1/30 on Quick Construction, per the changed route from the
  0920 unit (three consecutive units proved taps from 1/30
  on this node do not land). The day is not done: 1 remains,
  and the 1/30 tap is the known blocker. Tracker untouched;
  the re-read is the newly enqueued donations-2026-11-08-1832
  (not-before 11:05 local). No duplicate re-read unit is
  enqueued.
- Session: computer session cc-108 on the owner Mac mini
  (1c817413-83e2-0545-cb90-36d5e096a6bd). No device-access
  error, no different-device dialog, no login demanded.
  One transient screen-capture failure (screen_failed,
  "App identity or privacy changed during capture") on
  the first observe after tap 1; the immediate retry
  succeeded. A single transient, not the persistent
  Issue 284 form.
- Entry route: game found on the base screen. Alliance
  button tapped at the fresh grounded centre (937,722),
  Alliance Techs tile at (674,678), Development tab,
  Quick Construction 8/10 carrying the recommended
  marker, node tapped at its grounded centre (285,523).
  All three points measured fresh on this unit's
  screenshots, none carried. Base resources at entry:
  food 487.0M, iron 809.6M, coin 12.3M, badge 303.1K,
  diamonds 4,397, stamina 120.

## What was read and done, live in this unit

- Quick Construction panel (Development tab, 8/10,
  "Increased Building Speed for Allies", Donation
  Reward +20%, Tech EXP Required 1.4M/6.0M, Current
  +20%, Next Level +22.5%, Donation Reward EXP 50 +
  badge 50): Donation Count read live at entry:
  **4/30**. This is replenishment, not a fresh day -
  the 0920 unit closed at a live-read 1/30 about
  09:20, so the count rose 1 to 4 over about 69
  minutes, about 1 per 23 minutes as a two-endpoint
  estimate only, NOT a measured rate. The green coin
  Donate 900 button was live, not greyed. Tech
  Donation Today read 4800 at entry, up 100 from the
  0920 entry read of 4700, observed only.
- Tap 1 (green Donate 900, grounded centre 648,761,
  single tap): count re-read live **3/30**, badge
  303.1K to 303.2K, button still green, no timer.
  Landed.
- Tap 2 (same point, single tap): count re-read live
  **2/30**, badge 303.2K to 303.3K, button still
  green, no timer. Landed.
- Tap 3 (same point, single tap): count re-read live
  **1/30**, badge 303.3K to 303.4K, button still
  green, no timer. Landed. The "Hold down for easier
  continuous donations" tooltip appeared after this
  tap; hold-to-donate was NOT used (untested as a
  closing method).
- Stopped here. No tap was dispatched from 1/30.
  Three coin donations landed in this unit, 2,700
  coin spent (900 each). Tech EXP stayed 1.4M/6.0M
  in display rounding (+150 EXP is invisible at 0.1M
  rounding and is not claimed as a landing check);
  the count steps are the landing proof. Coin HUD
  stayed 12.3M in display rounding. Footer at close
  not re-read (panel left open); entry footer 4800
  recorded only.

## Findings

- Taps land fine at counts 4, 3 and 2 on Quick
  Construction, and fail only at count 1 - the
  fourth confirmation of the 1/30 stickiness in
  this chain (0920 third consecutive partial, this
  unit the fourth unit in the sequence to meet it,
  though this unit donated down to it rather than
  failing on it). The blocker is unchanged: the
  final donation of the day does not land from
  Quick Construction by single tap.
- The War-tab branch of the changed route (try
  Rallied Attack / Rallied Defense for the 1/30
  tap) is still untested - this unit's token lease
  ended before it could be attempted. It stays open
  for the re-read unit or a later unit with budget.
- Weekly settlement countdown, read live twice:
  "This week's donations will be settled soon:
  07:32:28" at entry, 07:30:11 at close. It counts
  down to about 18:04 local, near the trade-day
  reset. Observed only; whether the weekly
  settlement resets the Donation Count is unmeasured.
- Replenishment continues at about 1 per 20 to 23
  minutes by two-endpoint estimates (1 to 4 here,
  1 to 2 at 1523, 1 to 4 at 1346). No mechanism is
  asserted; Issue 160 still owns the measurement.

## Follow-up

- Re-read owed to the newly enqueued
  donations-2026-11-08-1832 (not-before 11:05
  local, window carries this unit's state): it reads
  the Donation Count live and applies the changed
  route - tap only if the count has replenished
  above 1, or try the War-tab node for the 1/30 tap.
  The already-queued donations-2026-11-08-1003 slot
  unit may run first; it carries no window context,
  so its executor reads this record and Issue 450.
- Measurement added to Issue 450 (comment from this
  unit): 4/30 entry after replenishment, three
  verified landings 4 to 1, no timer after taps from
  2 or above, War-tab branch still untested, weekly
  settlement countdown 07:32:28 at entry. No new
  issue is filed from this unit.
- Tracker untouched (partial unit, day not done).
- No diamonds spent, no purchase tapped, no red line
  crossed. Coins spent: 2,700 (3 x 900).
