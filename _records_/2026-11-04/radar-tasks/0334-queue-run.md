---
title: Radar tasks queue run 0334
created: 2026-11-04T11:46:00Z
modified: 2026-11-04T11:46:00Z
status: partial
executor: ticker-0334
unit: radar-2026-11-04-0203
---

# Radar tasks - 0334 queue run

Session window: 2026-11-04 about 03:34 to 03:46 local. Unit
radar-2026-11-04-0203, executor ticker-0334. Status: partial.
Posture: release (live duel.py at entry: duel day 3, Age of
Science, radar posture release; the unit window text reads
"duel day 3 - radar release", matching the live posture).

## Entry and an Esc lesson repeated

- The game was found open on the Alliance Techs donation
  panel (a previous unit's surface, Donation Count 2/30 in
  that frame). Closing the inner panel and the Alliance
  Techs panel worked, but the Alliance panel's back arrow
  did not exit on two taps, and an Esc key press then made
  the app exit outright. Esc on this app is a known crash
  route (AGENTS.md lesson, 2026-10-26) and must not be used
  again: reopening the app from the launcher restored the
  session with no observed state loss (radar points and
  stamina continuity confirmed below).
- Radar entry after relaunch on the first tap at norm
  (53,708), the dish icon with a red badge 6 in the base
  left column, grounded fresh on the current screenshot.
  Entry verified by its own reads: Lv.13, radar points 194,
  stored 3/40, stamina 156, restore line "12 Radar Task(s)
  will be restored in 05:54:30" at entry. Note the stamina
  read 156 exceeds the old 120 cap recorded in the activity
  metadata; it is recorded as read, mechanism unverified,
  not smoothed over.
- Bottom-bar buttons in this window respond at norm
  (500,952), confirmed by the Quick Execute and Claim All
  taps below.

## Pins first (rule R7, from the 2026-11-03 2317 unit)

Five finished-task pins claimed instantly on tap, each
+1 radar point, in this order:

- Green skull pin top centre (428,358): radar item 10,
  blue triangle 225, coin 303.6K. Points 194 to 195,
  stored 3/40 to 2/40.
- Purple axe pin centre (375,430): radar item 10,
  iron 132.0K. Points 195 to 196, stored 2/40 to 1/40.
- Grey skull pin right (735,545): radar item 10, blue
  triangle 183, coin 247.2K. Points 196 to 197,
  stored 1/40 to 0/40.
- Purple skull pin bottom left (265,715): paw print 3,
  radar item 300, iron 975.6K, food 975.6K, coin 622.8K.
  Points 197 to 198.
- Blue axe pin top left (297,375): radar item 10,
  EXP 1.4M, drone item 800, food 727.2K, coin 121.2K.
  Points 198 to 199.

## Doom Elite pin - identified, rally blocked (Issue #268)

- The blue skull pin (552,360) is NOT a finished-task pin.
  It opened the card "Defeat Doom Elite 1 times", rewards
  food 920.4K, iron 920.4K, coin 588.0K, radar item 300
  and a drone item, countdown 07:56:50. This is the
  red-dotted blue skull pin the 2317 unit named as the
  next unit's first action, now identified.
- Go jumped to the world map Doom Elite Lv.1 card:
  suggested power 1,096,500, stamina cost 20, timer about
  24 hours, dialogue "Initiate a rally and call allies
  to attack together." The rally panel showed squad
  25.18M vs 1.09M, Easy Win, Unit Count 2,231/2,231,
  Resistance required 10,250/200, Rally Time 1min
  checked.
- The blue Rally button did not launch on two clicks at
  the grounded point (501,735) and one long-press there:
  no march, no stamina change (still 156), panel stayed
  open. Per rule R2 this is the third no-change attempt
  at that point, so the blocker is filed as Issue #268
  and the next unit must change method before retrying
  (different squad, different rally time, or a fresh
  entry route). The pin was left standing, uncompleted.
  No stamina was spent on it.

## Quick Execute and Claim All

- Re-entering the radar after the rally attempt (dish
  re-grounded fresh at (53,706) on the returned base view;
  one mis-tap on the world-map left column was corrected
  via the BASE button, no game action taken there):
  bottom bar "You can complete 2 tasks, requires 20
  Stamina."
- Quick Execute: 2 tasks, stamina 156 to 136 (-20).
  Bar flipped to Claim All: "6 task rewards can be
  claimed".
- Claim All: 6 rewards, points 199 to 205 (+6, exactly
  the claim count), no TIPS dialog (matching the
  post-rollover units; the duel delta test is still
  owed, no VS panel read was taken in this unit, and no
  duel-points figure is claimed here).
- Claim All popup: radar item 50, EXP 4.7M, blue
  triangle 498, 5-minute speedup 6, 1-minute speedup
  65, iron 1.4M, food 1.4M, coin 1.2M, Lv.1 chest 1.

## Closing state (live reads, same unit)

- Radar Lv.13, radar points 205, stored 0/40, stamina
  136, restore line "Fully restore at 11-5 03:xx local
  time" (time partly obscured by a toast), bottom bar
  with no offer.
- Pin inventory at close (visible frames only, not a
  whole-map census): the Doom Elite blue skull pin still
  standing (blocked, Issue #268); a purple portrait pin
  top right; a purple axe pin bottom centre, identified
  below; other standing pins seen earlier in the unit
  (gold portrait, grey skull top right, [AP3x] portrait,
  blue axe plus pink pin left-mid) were off-frame in the
  closing pan and are NOT claimed as cleared.
- Purple axe pin bottom centre (433,720), tapped in the
  closing minutes: "Rare Farmland", "Allow Troops to
  gather incredibly fast!", food 132.0K, radar item 10,
  countdown 07:52:38. This identifies one of the standing
  axe pins as a gathering pin. It was NOT started in
  this unit: a gathering march near the unit end would
  leave a squad out with its reward unclaimed, so the
  pin is left for the next radar unit to work first via
  Go, the pickaxe step and the radar claim.
- Per the release standard, pins left unattempted or
  uncompleted make this unit partial, never done. The
  Doom Elite rally blocker and the Rare Farmland pin
  become the FIRST actions of the next radar unit, in
  that order, under rule R7.
- No diamonds or money spent, no Buy tapped, no stamina
  item used, no free stamina claim taken (stamina never
  blocked execution), no other activity worked from
  this unit. Base-view harvest bubbles seen on the
  return to base were not touched: they belong to the
  resource-collection unit, not this one.
- Tracker untouched for partial, per the queue rules.

## Totals in this unit

- Rewards claimed: 11 (5 pin claims + 6 Claim All).
  Radar points 194 to 205 (+11, exactly the claim count).
- Tasks executed: 2 via Quick Execute.
- Popup resources summed: radar items 390, EXP 6.1M,
  blue triangles 906, coin 2.4948M, iron 2.5076M,
  food 3.1028M, drone items 800, paw prints 3,
  5-minute speedups 6, 1-minute speedups 65, Lv.1
  chest 1.
- Stamina: 156 to 136 net (-20, Quick Execute only).
- Duel points: NOT read in this unit.
