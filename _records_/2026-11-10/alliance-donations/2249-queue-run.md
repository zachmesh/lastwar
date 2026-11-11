---
title: Alliance donations queue run 2249
created: 2026-11-11T06:49:00Z
modified: 2026-11-11T06:49:00Z
version: 1.0.0
description: Donations unit donations-2026-11-11-0413, re-read after the ticker-1952 cooldown, 3 coin donations verified live 4 of 30 to 1 of 30, stopped at the 1 of 30 floor per the changed route, partial
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-10 22:43-22:49 PT
---

# Alliance donations queue run 2249 (ticker-2231)

Unit: donations-2026-11-11-0413. Status: partial.
Activity: alliance-donations. Computer session cc-517.

## Entry - map view, fresh label-area point

- The game was left on the world map by the previous pass
  (not the base screen). Resource bar at entry: food
  644.6M, iron 967.7M, coin 106.1M (HUD-rounded), gold
  405.5K, Total Power 149,218,973.
- Alliance entry: the shield label area tapped at the fresh
  measured point (930,721) from the current screenshot -
  opened the Alliance menu on the first try. The (903,787)
  centre in the activity metadata stays withdrawn.
- Alliance menu: [AP3x] The Apex, Leader Abŷss Apex,
  Power 13,803,720,462, Members 96/100, Language English.
  Alliance Techs tile tapped at (686,680) from the current
  screenshot - opened first try.
- Two LastWar windows persist on pid 1908 (489932 at
  642x951, used here; 508052 at 642x919 covers it per the
  activate receipt), but background input to the selected
  window worked on every tap - no recurrence of the 0634
  input-blocked state (Issue #575).

## Donations - 3 verified, stopped at the 1 of 30 floor

- Alliance Techs opened on the Development tab. Quick
  Construction 8/10, Increased Building Speed for Allies,
  Donation Reward +20%, Tech EXP Required 3.0M/6.0M,
  Current +20%, Next Level +22.5%, per-donation reward
  50 EXP + 50 badge. Tech Donation Today 1150, display
  only, never a closing figure (Issue #558).
- Donation Count read live at entry: 4/30. The coin Donate
  button is green at 900 coin per donation; the diamond
  button (Donate 2) was never used.
- Three coin donations, each verified by a live count
  re-read immediately after the tap: 4/30 to 3/30, 3/30
  to 2/30, 2/30 to 1/30. Coin spent 2,700. The Tech EXP
  bar stayed 3.0M/6.0M throughout - at this rounding a
  +50 EXP step per donation is invisible, so the count
  label is the only per-tap verification this unit, as
  in the 2133 unit.
- Stopped at the live-read 1/30 per the changed route:
  no tap from 1/30 on Quick Construction. The button
  stayed green at 1/30 with no cooldown timer shown
  after the third tap - unlike earlier units' grey-outs,
  no timer hid the count this unit.
- Gold rose 405.5K to 405.7K to 405.9K during the unit
  (alliance income, not mine); coin HUD stayed 106.1M
  (the 2,700 spent is below HUD rounding).
- Panel closed cleanly back to the Alliance Techs tree
  before the unit ended.

## Replenishment - another data point for Issue 160

- Ticker-1952 left the count at 1/30 plus one dispatched
  tap behind a 00:14:47 cooldown. This unit entered at
  4/30 after the cooldown, so the count rose by 3 over
  the interval between the two units. Replenishment
  continues to be the standing model (Issue #160); no
  rate is derived from this single interval.
- The War-tab Rallied Attack count was not re-read in
  this unit (unit cap), so the per-node count question
  stays open (Issues #160, #450). The successor re-read
  carries it as its changed-route test.

## Close

- Closing figure: Donation Count 1/30 read live in this
  unit (screenshot-verified). Status partial: the regular
  is not fully done - 1 remains and it replenishes, so
  the tracker stays untouched and a named re-read unit
  is enqueued for after 23:30 PT. The day's 30 is not
  claimed done on arithmetic.
- Successor: donations re-read, not-before 2026-11-11
  07:30:00Z, window "re-read after ticker-2231 1/30
  close; War-tab Rallied Attack count check".
