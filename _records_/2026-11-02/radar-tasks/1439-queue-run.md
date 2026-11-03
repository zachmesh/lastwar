---
title: Radar release unit 1439
created: 2026-11-02T22:39:00Z
modified: 2026-11-02T22:39:00Z
version: 1.0.0
description: Ticker unit radar-2026-11-02-1403, radar screen never entered, entry blocker second consecutive unit, no tasks executed or claimed
status: partial
---

# Radar tasks - release day unit, partial (entry not reached)

- Unit: radar-2026-11-02-1403, executor ticker-1412.
  Session window about 14:27 to 14:39 America/Los_Angeles.
  Duel day 1, Radar Training, release posture confirmed by
  tools/duel.py (radar_posture release, day ends 19:00,
  4.5 hours left) before the unit started, but the radar
  screen was never entered, so this unit is partial and
  the tracker is untouched.
- Entry state: the game was left by this pass donations
  unit with the base camera panned onto the Drill Ground
  cluster (Drill Ground Lv.25, three floating round
  buttons at the bottom right). The left icon column
  with the radar dish is not visible in this framing.
  This is the second consecutive radar unit with this
  entry blocker, after 1026 the same day.
- Changed method per rule R2 (the 1026 unit burned its
  budget on a grounding timeout): instead of grounding
  the dish, this unit tried to restore the base view
  through the building panel. Tapping the Drill Ground
  area at (810,778) opened the DRILL GROUND panel
  (Unit Count 39460 of 39460, In Base Lv.7 x701, Lv.8
  x1332, Lv.10 x37.4K, Outside no units outside). No
  Promote button was tapped and nothing was spent.
- Panel close failure, two no-change taps, method
  retired in this unit: the panel X at (799,203) and
  again at (802,200) produced no change. The control
  channel noted background clicks do not reach some
  controls and suggested click_element with a visible
  label or the keyboard instead; neither was tried in
  this unit, and Esc was not used (standing rule: Esc
  has crashed this app before). The game is left safe
  with the DRILL GROUND panel open, no purchase, no
  dispatch, no march, no pin tapped, no other
  activity's rewards claimed.
- Handover for the next radar unit: the panel must be
  closed first (candidates: foreground the LastWar
  window and re-tap the X, click_element, or relaunch
  the app to restore the base overview), then restore
  the full base view, then ground the dish fresh from
  that screenshot (the 0636 unit working point was norm
  53,708; the profile measured point is 62,727) and
  verify the radar screen (Lv.13, stored count,
  stamina) before any work. Release posture still
  applies: execute and claim everything stored, then
  scan the map pins to a closing read each. The 0636
  unit pin inventory (two standing orange arrow pins,
  classes unknown) is still open. If the next radar
  unit also fails on entry, it is the third consecutive
  unit with this blocker and must write the blocker
  into the radar-tasks activity metadata per rule R2.
- Cross-unit note: the donations camera pan strands the
  next unit. A donations unit that pans the camera
  should restore the base framing before it closes, or
  the following unit inherits a panned view with no
  icon column.
- Red lines: nothing spent, no Buy tapped, no map pin
  tapped, no other activity's rewards claimed.
- Result stats: target unverified, achieved 0, verified
  no, blocker_category c (entry-route: base camera
  panned onto Drill Ground with no icon column, and
  the Drill Ground panel X unresponsive to background
  clicks; second consecutive radar unit with this
  blocker).
