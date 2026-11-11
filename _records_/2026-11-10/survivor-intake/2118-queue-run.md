---
title: Survivor intake queue run 2118
created: 2026-11-11T05:18:00Z
modified: 2026-11-11T05:18:00Z
version: 1.0.0
description: Ticker-2055 survivors unit, radar exit buttons unresponsive, gate line unverified, partial
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-10 21:10-21:18 PT
---

# Survivor intake queue run 2118 (ticker-2055)

Unit: survivors-2026-11-10-1803. Status: partial.
Activity: survivor-intake.

## What happened - exit blocked, gate never reached

- The game was left on the radar screen by the previous unit of
  this pass (ticker-2055 radar release, points 375, stored
  13/40, stamina 41 at close). This unit had to return to the
  base screen first to reach the front gate.
- The radar screen's exit buttons did not respond to background
  clicks, four attempts, three variants (R2 - method exhausted
  inside this unit):
  1. Home button, norm (915,915), snap click - no change
     (restore line display toggled on).
  2. Back arrow, norm (78,915), snap click - no change.
  3. Home button, norm (911,915), snap click - no change.
  4. Back arrow, norm (78,917), exact input
     (snap_to_control false), 3 second wait - no change.
  5. Home button lower area, norm (911,936), snap click -
     no change.
- The in-game canvas buttons on the same screen DID respond
  earlier in this pass (dish entry, Claim All x4, Quick
  Execute x3), so background input reaches the window - the
  non-response is specific to the radar screen's back/home
  corner buttons in this session. The other LastWar window
  (508052) was checked and shows the same radar screen.
- No keyboard keys were used (Return and Esc quit or crash
  this app). No other exit route was attempted: the pass
  budget was nearly out and any further route would have left
  no time for the gate check itself.
- The gate line was therefore never reached and never verified
  in this unit: no survivor figure seen, no question-mark
  bubbles seen, no recruit taken in, Quick Dispatch did not
  run (nothing taken in, so nothing to post - R7 starved
  subtask carries on).

## Standing blocker - fourth identical partial

- This is the fourth survivors unit today to close on the gate
  line not being found or verified (0321, 1224, 1615, now
  2118), on top of the 22 of 22 partials of the queue era
  2026-10-28 to 2026-10-31 recorded in the activity metadata.
  Under queue rule R2 the fourth identical partial is a
  process failure, not a result, and is reported to the owner
  as one (see the pass summary). The 1615 unit's proposed
  changed method - pan to the bottom-right corner gate by the
  red-roofed structure instead of re-probing the same wall -
  was NOT tried, because the unit never got out of the radar
  screen; it stays the first action for the next survivors
  unit, which must first solve the radar exit (or enter from
  a base-screen state left by another unit).
- The exit-button non-response is a new, separate blocker
  recorded here for the first time: earlier radar units
  exited the screen and later units ran other activities, so
  the exit worked in past sessions. Whether this is a
  session-specific input quirk or a radar-screen change is
  unverified - the next unit that finds itself on the radar
  screen must test the exit buttons first and report.

## Closing reads (live, in this unit)

- Radar points 375, stored 13/40, stamina 41 (regen +1 from
  40 during the unit), restore "12 Radar Task(s) will be
  restored in 02:26:37" at close.
- The game was left on the radar screen with a Quick Execute
  offer pending ("complete 2 tasks, requires 20 Stamina").
  The next radar unit (radar-2026-11-10-2203 in inbox) will
  find the radar already open, with 2 executable tasks, 15
  pins inventoried in the 2107 record, and the exit to test.

## Outcome

Partial. No survivor was verified, recruited or dispatched.
The tracker is left untouched, so the next tick re-produces
the survivors regular. No diamonds or money spent, no priced
button tapped, no other activity's rewards touched.

## Result stats

- target take in every waiting survivor at the front gate,
  then run Quick Dispatch
- achieved 0 recruited, 0 dispatched; gate line not verified,
  radar exit blocked
- resources_gained none
- points 0
- costs about 8 minutes, no items spent
- verified no
- blocker_category e
- survivors_recruited 0, quick_dispatch_runs 0,
  gate_line_verified no, radar_exit_attempts 5,
  radar_exit_successes 0
