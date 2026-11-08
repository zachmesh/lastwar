---
title: Queue Run 1238 Alliance Donations Re-read and War-tab 1/30 Test
created: 2026-11-08T20:38:00Z
modified: 2026-11-08T20:38:00Z
level: L0
version: 1.0.0
description: Donations unit donations-2026-11-08-1832, partial - six verified coin donations on Quick Construction 7/30 to 1/30, then the War-tab 1/30 test on Rallied Attack, two taps 2/30 to 1/30, final tap greyed behind a 00:18:42 timer, closing 0/30 unverified
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-08 about 12:30-12:38 America/Los_Angeles
---

# 1238 queue run - alliance donations re-read and War-tab 1/30 test (donations-2026-11-08-1832)

- Unit: donations-2026-11-08-1832, executor ticker-1223.
  Status: partial - eight coin donations dispatched, seven verified
  by live count steps, the eighth (the War-tab 1/30 test tap)
  dispatched behind a 00:18:42 cooldown timer that hides the
  count, so the closing 0/30 is NOT a live read. The unit closes
  unverified on that point per the hard closing rule. Tracker
  untouched; the re-read is the newly enqueued
  donations-2026-11-08-2038 (not-before 13:03 local).
- Session: computer session cc-119 on the owner Mac mini
  (1c817413-83e2-0545-cb90-36d5e096a6bd). No device-access
  error, no different-device dialog, no login demanded.
  No screen-capture failure. One control-channel advisory
  (background clicks may not reach some controls) after tap
  2 on Quick Construction; the live count step 6/30 to 5/30
  in the same observation proves that tap landed, so the
  advisory is not treated as a failure.
- Entry route: game found on the base screen. Alliance
  button tapped at the fresh grounded centre (936,721),
  Alliance Techs tile at (673,682), Development tab,
  Quick Construction 8/10 carrying the recommended
  marker, node tapped at its grounded centre (284,522).
  All points measured fresh on this unit's screenshots,
  none carried. Base resources at entry: food 489.5M,
  iron 811.9M, coin 12.3M, badge 303.4K, diamonds 4,397,
  stamina 120, Total Power 149,850,353.

## What was read and done, live in this unit

- Quick Construction panel (Development tab, 8/10,
  "Increased Building Speed for Allies", Donation
  Reward +20%, Tech EXP Required 1.5M/6.0M, Current
  +20%, Next Level +22.5%, Donation Reward EXP 50 +
  badge 50): Donation Count read live at entry:
  **7/30**. This is replenishment - the 1034 unit closed
  at a live-read 1/30 about 10:34, so the count rose 1 to
  7 over about 2 hours, about 1 per 20 minutes as a
  two-endpoint estimate only, NOT a measured rate. The
  green coin Donate 900 button was live, not greyed.
  Tech Donation Today read 5300 at tree entry, up 500
  from the 1034 entry read of 4800, observed only.
- Tap 1 (green Donate 900, grounded centre 647,777,
  single tap): count re-read live **6/30**, badge
  303.4K to 303.5K, button still green, no timer.
  Landed.
- Tap 2 (same point, single tap): count re-read live
  **5/30**, button still green, no timer. Landed. The
  badge HUD was covered by a scrolling announcement
  banner on the re-read screenshot and is not claimed.
- Tap 3 (same point, single tap): count re-read live
  **4/30** by OCR, badge 303.7K, button still green,
  no timer. The "Hold down for easier continuous
  donations" tooltip appeared; hold-to-donate was NOT
  used (untested as a closing method). Landed.
- Tap 4 (same point, single tap): count re-read live
  **3/30** by OCR, button still green, no timer.
  Landed.
- Tap 5 (same point, single tap): count re-read live
  **2/30** by OCR, button still green, no timer.
  Landed.
- Tap 6 (same point, single tap): count re-read live
  **1/30** by OCR, button still green, no timer.
  Landed. Six coin donations on Quick Construction,
  5,400 coin spent (900 each). Badge HUD 304.1K at
  the 1/30 screenshot, observed only.
- Stopped tapping on Quick Construction at the
  live-read 1/30, per the changed route. No tap was
  dispatched from 1/30 on this node.

## The War-tab 1/30 test (Rallied Attack)

- Closed the Quick Construction panel, tapped the War
  tab, dragged the tree down twice to the Rallied row:
  Troop Movement 5/10 above, Rallied HP 7/10, Rallied
  Attack 7/10, Rallied Defense 7/10, one node 1/10
  below. No recommended marker on the Rallied row; the
  marker sits on Development Quick Construction.
  Rallied HP is 7/10 now, up from 5/10 on 2026-11-01
  and past its upgrade countdown that ran to about
  13:20 local on 2026-11-02.
- Rallied Attack panel (War tab, 7/10, "Increased Hero
  Attack in Rallies for Allies", Tech EXP Required
  23.3K/4.5M, Current +7%, Next Level +8%, Donation
  Reward EXP 50 + badge 50): Donation Count read live
  at entry: **2/30**. The green coin Donate 800 button
  was live, not greyed. Coin cost here is 800, not the
  900 Quick Construction charges.
- Tap 7 (green Donate 800, grounded centre 648,783,
  single tap): count re-read live **1/30**, Tech EXP
  23.3K to 23.5K. Landed.
- Tap 8 (same point, single tap, from the live-read
  1/30 on the War-tab node - THE test): the coin
  Donate button GREYED with a **00:18:42** cooldown
  timer replacing the count label. Tech EXP stepped
  23.5K to 23.6K on the same observation. Two coin
  donations on Rallied Attack, 1,600 coin spent
  (800 each).
- Reading of tap 8: the Tech EXP step (+0.1K display,
  about +150 EXP per donation at this display scale)
  is consistent with a landed donation, and the
  greyed-button-plus-timer shape matches the
  post-final-donation closes of the 2348 and 0259
  units, where the tap had landed. But the count
  itself was NOT seen after tap 8, so under the hard
  closing rule the 0/30 is NOT claimed as a live
  read: this unit closes partial and unverified, and
  the re-read unit decides it. If the re-read finds
  0/30 live, the War-tab route breaks the 1/30
  blocker and the changed route is retired; if it
  finds 1/30, the blocker is node-independent and
  Issue 450 stays open.

## New question - per-node count or global count

- The Rallied Attack panel read 2/30 about four
  minutes after Quick Construction read 1/30 live.
  Two readings are possible: (a) a replenishment tick
  landed in between (+1 in about 4 minutes, much
  faster than the about 1-per-20-minutes two-endpoint
  estimates, which are coarse); (b) the Donation
  Count is per-node, not one global remaining count -
  no unit has ever read two nodes' counts in one pass
  before, so this is untested. The re-read unit
  (donations-2026-11-08-2038) is instructed to read
  BOTH panels after the cooldown: if Quick
  Construction still reads 1/30 while Rallied Attack
  reads 0/30, the count is per-node; if both read
  the same, it is global plus replenishment. Commented
  on Issue 450 with this unit's evidence.

## Other live reads

- Weekly settlement countdown, read live twice:
  "This week's donations will be settled soon:
  05:26:31" on the Quick Construction panel,
  05:21:15 at the Rallied Attack close. It counts
  down to about 18:00 local, near the trade-day
  reset. Observed only; whether the weekly
  settlement resets the Donation Count is unmeasured.
- Tech Donation Today footer: 5300 at tree entry,
  5850 on the War-tab tree, observed only (the
  footer is disqualified as a count-closing figure).

## Follow-up

- Re-read owed to the newly enqueued
  donations-2026-11-08-2038 (not-before 13:03
  local, window carries this unit's state): read the
  Rallied Attack Donation Count live after the
  00:18:42 timer clears, and read the Quick
  Construction count in the same unit for the
  per-node test. No duplicate re-read unit is
  enqueued.
- Measurement added to Issue 450 (comment from this
  unit): seven verified landings 7 to 1 on Quick
  Construction, War-tab 1/30 tap dispatched with a
  00:18:42 timer and a Tech EXP step 23.5K to 23.6K,
  Rallied Attack count 2/30 against Quick
  Construction 1/30 four minutes apart, weekly
  settlement countdown 05:26:31. No new issue is
  filed from this unit; the per-node question rides
  on Issue 450.
- Tracker untouched (partial unit, closing count
  unverified).
- No diamonds spent, no purchase tapped, no red line
  crossed. Coins spent: 7,000 (6 x 900 + 2 x 800).
  Badge HUD 303.4K to 304.3K, observed only.
