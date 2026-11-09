---
title: Alliance donations queue run 0235
created: 2026-11-03T10:43:00Z
executor: ticker-0234
unit: donations-2026-11-03-0203
status: partial
---

# Alliance donations - 2026-11-03 02:35 local

Unit: donations-2026-11-03-0203 (regular donations,
activity alliance-donations). Session: Mac mini Last War
window, computer session cc-290. Coin button only, no
diamonds, no money, no paid button tapped.

## Entry route - the 2026-11-02 blocker is broken

- The three 2026-11-02 donations units (0621, 1020, 1427)
  failed to open the Alliance menu. This unit used the
  changed route: base framing was already correct on
  entry (not the Drill Ground view), and a single tap at
  the freshly measured Alliance shield centre (910,720)
  on the current screenshot opened the Alliance menu at
  once. Note: the (903,787) centre recorded by the 1427
  unit did not match this screenshot's Alliance position
  (the shield sits higher on this view); re-grounding on
  the current screenshot, not reusing the recorded point,
  is what worked.
- Alliance menu read: [AP3x] The Apex, 94/100 members.
  The Help and Alliance Gifts red dots visible on the
  menu belong to their own units and were left untouched.
- Alliance Techs tile tapped at (709,662): War tab,
  Troop Movement 5/10, Rallied HP 6/10, Rallied Attack
  7/10, Rallied Defense 7/10, next node below 1/10.
  Tech Donation Today 5250 at entry.

## State, read live in this unit

- Rallied Attack panel (the previous target, still 7/10):
  Tech EXP 10.3K/4.5M, Current +7 percent, Next Level
  +8 percent, Donation Reward 50/50, Donation Count
  2/30, coin Donate green at 800 coin, diamond Donate
  untouched at 2 diamonds.

## Donations made - three coin taps, per-tap evidence

- Tap 1 at the green coin Donate centre (709,783):
  Donation Count 2/30 to 1/30, verified by screenshot;
  Tech EXP 10.3K to 10.4K. Donation landed.
- Tap 2 at the same centre: button greyed with a
  00:02:27 cooldown timer, verified by screenshot; the
  timer hid the Donation Count label. Tech EXP stayed
  10.4K (display rounds to 0.1K, so this does not prove
  or disprove a landing). The cooldown was waited out
  inside the unit (100 seconds, then 30 seconds); after
  expiry the panel read Donation Count 1/30 again, live.
  So either tap 2 did not land, or the count
  replenished by 1 across the 2:27 cooldown. This unit
  does not decide between the two; the replenishment
  rule is already tracked as Issue #174 (and #160).
- Tap 3 at the same centre: the control reported no
  visual change on the tap itself, but the next
  screenshot showed Tech EXP 10.4K to 10.5K and the
  coin button greyed with a 00:18:45 cooldown timer.
  A donation landed on this tap (EXP move is the
  evidence). The timer again hides the Donation Count
  label. A tooltip line seen in the tap-3 observation
  reads "Hold down for easier continuous donations" -
  a hold-to-donate route exists and is untested; the
  next unit may try it if single taps stop registering.
- Coin spent by arithmetic only (HUD coin reads 5.9M
  throughout, too coarse to show 800-coin steps):
  3 taps times 800 coin = 2,400 coin. Honor HUD moved
  193.3K to 193.5K across the unit; not claimed as
  this unit's alone.

## Closing state - unverified, by the hard rule

- At close the Donation Count cannot be read live: the
  00:18:45 timer from tap 3 (started about 02:42) runs
  until about 03:01 local, past this unit's budget, and
  the count label is hidden behind it. Per the hard
  closing rule this unit closes partial and unverified,
  not done: no arithmetic final count is claimed.
- Tracker left untouched, following the 0144 precedent.
- Re-read unit donations-2026-11-03-0910 was already
  queued with not_before 02:10 local, which predates
  this unit's 18:45 timer; claiming it before about
  03:02 would find the timer still running and waste
  an attempt. Its not_before was moved to
  2026-11-03T11:02:00Z (03:02 local) and its window
  text updated to the tap-3 00:18:45 timer, so the
  next claimable tick after the cooldown does the
  re-read. No new issue filed: replenishment is
  already Issue #174, commented with this unit's
  cooldown data points.

## Red lines

- No diamonds spent, no paid button tapped, no
  alliance diplomacy, no assembly, no teleport. The
  diamond Donate button was never tapped.
