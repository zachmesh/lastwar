---
title: Queue Run 0808 Alliance Donations Re-read
created: 2026-11-08T16:26:00Z
modified: 2026-11-08T16:26:00Z
level: L0
version: 1.0.0
description: Donations unit donations-2026-11-08-1523, re-read after cooldown, partial - one donation verified live, second tap no-landing by the count-unchanged rule, third tap unverified behind a 17m33s timer
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-08 about 08:08-08:24 America/Los_Angeles
---

# 0808 queue run - alliance donations re-read (donations-2026-11-08-1523)

- Unit: donations-2026-11-08-1523, executor ticker-0804.
  Status: partial - one coin donation verified live by the
  Donation Count; a second tap produced the grey button
  plus a badge move but the count was unchanged (1/30)
  after its timer cleared, so it did not land by the
  count-unchanged rule; a third tap sits behind a
  00:17:33 timer and is unverified. The unit closes
  unverified per the hard closing rule in the
  alliance-donations metadata (rule R1). Tracker
  untouched; a named re-read unit is enqueued for after
  the cooldown (not-before 2026-11-08T16:40:00Z).
- Session: computer sessions cc-97 and cc-98 on the owner
  Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd).
  Session cc-97 dropped during the cooldown wait
  (observe returned observation_unavailable); cc-98 was
  started and LastWar re-selected with no game state
  lost. No device-access error, no different-device
  dialog, no login demanded.
- Entry route: the Alliance shield icon was tapped at its
  fresh measured centre on the live screenshot (937,727
  normalized) - the menu opened first try, no Drill
  Ground detour. The R2-changed route holds. The game
  was found on the EVENTS screen (Winter Battlefield);
  the back arrow was re-grounded (first tap at y 893
  landed above the button and did nothing; second tap
  at the measured centre 181,938 returned to base).

## What was read and done, live in this unit

- Base screen: food 478.8M, iron 802.1M, coin 6.9M,
  diamonds 4,397, total power 149,850,353. Alliance
  button (right column) tapped at its fresh measured
  centre.
- Alliance menu: [AP3x] The Apex, Overall Rating 5.0,
  Leader Abyss Apex, Power 13,259,135,070, Members
  95/100, Language English. Tiles: Alliance Wars, Help
  (red dot), Alliance Gifts (red dot), Members, Alliance
  Store, Alliance Techs. Alliance Star (Event 40),
  Time Left 09:39:44.
- ALLIANCE TECHS, Development tab: Auto Rally Max Level,
  Quick Construction 8/10 (recommended marker), Great
  Helper Max Level, one node below at 2/10 (partially
  visible). Footer at entry: Tech Donation Today 4400.
- Quick Construction panel (recommended node): "Increased
  Building Speed for Allies", Donation Reward +20%, Tech
  EXP Required 1.4M/6.0M, Current +20%, Next Level
  +22.5%, Donation Reward EXP 50 + badge 50. Donate
  buttons: yellow Donate 2 diamonds (never used) and
  green Donate 900 coins. "This week's donations will be
  settled soon: 09:47:54" at entry.
- Donation Count read live at entry: **2/30** (remaining).
  This is NOT the 0/30 the 0704 unit's arithmetic implied:
  the 0704 unit left the count at 1/30 (about 07:24) and
  this unit read 2/30 (about 08:11) - the count rose by
  1 in about 47 minutes, consistent with the slow
  replenishment rate in Issue 450 (about 1 per 27
  minutes from the 0546 to 0704 reads).
- First tap (green Donate 900): VERIFIED landed - the
  count read **1/30** live on the next screenshot, and
  the HUD badge moved 302.6K to 302.7K. Button stayed
  green and live.
- Second tap (green Donate 900): the coin button greyed
  immediately with a **00:04:19** cooldown timer and the
  badge moved to 302.8K, but after the timer expired
  (about 4.5 minutes waited inside the unit) the count
  read **1/30** again - the tap did NOT land, by the
  same count-unchanged signature as the 0704 unit's
  fourth tap. The badge move alone is not landing
  evidence.
- Third tap (at 1/30, button green and active): the coin
  button greyed again with a **00:17:33** timer and the
  badge moved to 302.9K, and a "Hold down for easier
  Continuous donations" tooltip appeared. The count is
  hidden behind this timer, which outruns the unit's
  remaining budget, so whether this tap landed is
  UNVERIFIED. No arithmetic final is claimed as the
  closing count.
- Footer re-read live at close (panel closed back to the
  tree screen): Tech Donation Today **4600** (entry
  4400, delta +200). The delta does not reconcile with
  50 points per coin donation over this unit's one
  verified donation, so the footer is NOT used as a
  count proxy - it is recorded only as an observed
  figure. The 0704 unit saw +350 for three verified
  donations; this unit saw +200 for one verified
  donation. The footer moves independently of verified
  donations.

## Findings

- The burst cap is reached after as few as one verified
  donation in a burst: this unit's second tap (and the
  0704 unit's fourth tap) greyed the button without
  landing, while the count stayed above zero. The
  grey-plus-badge signature is confirmed NOT to be
  landing evidence in a second unit.
- Cooldown timers grow inside a burst: 00:04:19 after
  this unit's second tap, 00:17:33 after the third
  (0704 saw 00:05:07 then 00:19:33). The timer is a
  burst cooldown, not a refill timer: after the
  00:04:19 timer cleared the count was unchanged
  (1/30), so no refill arrived with the timer.
- Count replenishment is slow: 1/30 (0704 close, about
  07:24) to 2/30 (this unit entry, about 08:11), about
  1 per 47 minutes, in line with the 0546 to 0704 rate
  of about 1 per 27 minutes. A 0/30 read is therefore
  not a stable day-done state; more donations become
  available later in the day. See Issue 450.
- New UI note: tapping the coin Donate button shows a
  "Hold down for easier Continuous donations" tooltip -
  holding the button may donate continuously. Not tried
  in this unit; the next unit may try a hold if the
  button is live and the count is above zero.

## Follow-up

- Re-read unit enqueued, not-before 2026-11-08T16:40:00Z
  (after the 00:17:33 cooldown): it reads the Donation
  Count live and, if it still shows 1 remaining,
  donates once more; if 0, the day is done and the
  tracker is marked.
- Issue 450 commented with this unit's measurements
  (replenishment rate, burst-cap taps, growing timers,
  footer mismatch).
- Tracker untouched (partial/unverified unit).
- No diamonds spent, no purchase tapped, no red line
  crossed. Coins spent: 900 verified (one donation);
  the third tap's 900 is unverified.
