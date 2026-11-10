---
title: Trucks queue run 0344
created: 2026-11-03T03:44:00-08:00
unit: trucks-2026-11-03-0257
executor: ticker-0334
status: partial
---

# Trucks - 2026-11-03 03:44 local

Unit: trucks-2026-11-03-0257 (regular trucks, activity truck-plunder).
Session: Mac mini Last War window, computer session cc-296.
No "active on a different device" dialog appeared. No diamonds,
no Trade Contracts, no paid button, no plunder, no dispatch.

## Duel posture

- Duel day 2, Base Expansion, from tools/duel.py at unit start.
  UR truck dispatches score (Handbook 100,000 each); trucks go
  UR today, contracts permitting. Radar posture stack.
  Window on the unit: duel day 2 - UR trucks, Mega UR only.

## Entry failure - third distinct route set, all no-change or wrong building

- The 2026-11-02 21:20 unit entered Intercity Trade by tapping
  the station building at norm [491,195]. This unit tried that
  exact tap first: no-change on the live base view, matching
  the 2026-11-02 23:47 unit. That is the second consecutive
  trucks unit for which the old station point does nothing.
- Fresh visual grounding of the base put a station box at
  norm 398-578 x 308-448. Tapping its centre [488,378]
  selected High-temp Furnace Lv.30, not a station. The
  furnace popup was dismissed by tapping empty ground;
  the furnace was not turned on or off and no upgrade
  was touched.
- The base was panned (drag [500,400] to [500,650]), then
  grounding put a station box at norm 545-730 x 105-235.
  Tapping its centre [637,170] selected Wall Lv.26, with
  the same unidentified two-button popup (home icon, up
  arrow) seen in the 23:47 unit. Neither button was tapped;
  the popup was dismissed by tapping empty ground. The
  Wall is not the trade station, and the grounding tool
  mislabels it as one.
- The base was panned again (drag [600,400] to [300,400]),
  then grounding put a station box at norm 280-435 x
  140-260. Tapping its centre [357,200] was no-change.
- The left column was re-grounded fresh and carries no
  trade slot in this set: hammer 2/4, flasks 2/2, green
  face 6.5 degrees C at norm 53,483, light-blue train
  front with a red dot at norm 61,563, white pickup at
  norm 61,643, satellite dish with badge 11 at norm
  62,723, hammer below. Per the 2026-10-30 evening units,
  the train-front icon neither opens trade nor flips
  the set, so it was not tapped in this unit.
- The foreground variant suggested by the 23:47 unit
  (moving the covering Chrome window aside) was not
  attempted: this control channel sends input in the
  background and never brings the game to the front,
  so that variant is not available from here.

## Counters

- Not read live in this unit: the trade screen was never
  entered, so no live counter is asserted here.
- Carried, not re-read, from the 2026-11-02 21:20 unit:
  Trade 4/5, Plunder 4/4, for the trade day ending
  19:00 local 2026-11-03. The 1-dispatch shortfall
  therefore remains unfilled, and the fifth dispatch
  on a UR duel day must still be UR (Mega UR only
  per the unit window). A returned truck may await
  settlement; that is not established in this unit.

## Outcome

- Status: partial, entry failed, dispatch shortfall carried
  forward (not a miss: the trade day runs to 19:00 local
  2026-11-03, and later trucks units keep trying entry).
- Claimed in this unit: none.
- No dispatch, no plunder, no settlement performed.
- Tracker untouched (partial units do not mark the tracker).
- Blocker_category: e (repeated blocker - trade screen
  entry method, third trucks unit in a row with the
  entry route failing or misidentifying buildings).
- GitHub Issue 218 filed in this unit (labels play,
  knowledge) for this repeated failure mode, related
  to Issue 205 on the same grounding-drift pattern
  for the train entry point. The activity metadata
  entry section was NOT edited in this pass; that
  correction belongs to the knowledge organiser via
  the PR flow, not to a tier-1 records commit.
- Next trucks unit: do not re-tap [491,195], [488,378],
  [637,170] or [357,200] blindly. A verified Intercity
  Trade entry route for the current base framing is
  needed first; until Issue 218 is answered, later
  units should spend their budget on finding that
  route rather than repeating these four points.
- Game left on the base screen, panned east from its
  starting framing by the two drags in this unit.
