---
title: Survivor intake queue run 0144
created: 2026-11-11T09:44:00Z
modified: 2026-11-11T09:44:00Z
version: 1.0.0
description: Ticker-0135 survivors unit, radar exit blocker broken with fresh-grounded Home button, gate line verified with 2 survivors, intake unverified after taps, partial
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-11 01:42-01:44 PT
---

# Survivor intake queue run 0144 (ticker-0135)

Unit: survivors-2026-11-10-2203. Status: partial.
Activity: survivor-intake.

## Radar exit blocker - BROKEN (R2 changed method)

- The game was left on the radar screen by this pass's radar
  unit (0141). The 2055 survivors unit (2118) had failed the
  exit five times - Home at norm (915,915), Back at (78,915),
  Home at (911,915), Back exact at (78,917), Home lower at
  (911,936) - all no-change.
- Changed method this unit: the Home button was re-grounded
  fresh from a current screenshot (visual grounding on the
  closing radar frame): centre norm (916,953), i.e. the
  button's lower centre rather than the (911-915,915-936)
  band the 2055 unit probed. Move, wait 1 second, click,
  wait 3 seconds - the base screen appeared on the first
  attempt. The exit non-response is therefore NOT a session
  input failure: background clicks reach the window (the
  radar cycle proved that all pass), and the corner buttons
  need their exact measured centre - the 2055 attempts were
  all a few points too high.
- Lesson for the next unit: never reuse (915,915) or
  (911,936) for the radar Home button; ground it fresh and
  tap its measured centre, about norm y 953 in the 642x951
  window.

## Gate line - verified, then cleared after taps (intake unverified)

- Base screen at entry to the gate check: food 666.0M, iron
  988.7M, coin 117.4M (up from 111.8M at the radar entry -
  the radar claims landed), stamina 23.
- The front gate (walled entrance, "Zombies" sign, left side
  of the base) was verified live: TWO survivors stood in
  front of it, each with a "?" bubble, figures confirmed in
  a 3x crop of the gate area. Gate line verified - the first
  survivors unit in weeks to reach a verified line.
- Tap 1: the right-hand survivor figure, norm (135,694)
  (crop-grounded). The tap opened a second window (641363);
  when the unit tried to activate it, it had already closed
  (target_closed). No card or dialog text was read.
- Tap 2: the left-hand survivor figure, norm (78,708)
  (crop-grounded). Visual change in the survivor region, no
  dialog read.
- Closing screenshot: NO "?" bubbles remain at the gate and
  no survivor figures stand there. The line reads clear.
- What is NOT established: whether either tap recruited or
  took in a survivor. No New Survivor Incoming card was read,
  no name, role or trait was seen, no Recruit button was
  tapped. Dialog-type survivors speak a line and walk in on
  a tap, so the bubbles clearing is consistent with two
  walk-ins - but it is equally consistent with the taps
  having dismissed something unread. Per R1 the intake is
  therefore UNVERIFIED: 0 recruits claimed, 0 verified.
- Quick Dispatch did NOT run: with no verified intake there
  is nothing confirmed to post, and the pass budget was out
  (token expiry 01:48). The R7 starved subtask carries on.

## Method correction for the next survivors unit

- One tap, one read. Tap a single survivor figure, then
  screenshot and READ before any second tap: if a card
  opens, record the name/role/trait and tap Recruit; if a
  dialog line opens, read the line, then tap through and
  watch the figure walk in. Never tap a second survivor
  before the first one's outcome is read - the blind
  double-tap is what left this unit unverified.
- If a tap opens a transient window that closes before it
  can be activated, screenshot the main window immediately
  instead of chasing the closed window.

## Closing reads (live, in this unit)

- Base screen: food 666.0M, iron 988.7M, coin 117.4M,
  stamina 23, power 149,218,973. Wall Lv.26 at the gate.
- Gate line at close: no "?" bubbles, no waiting figures -
  reads clear, intake unverified.
- The game was left on the base screen.

## Outcome

Partial. The radar-exit blocker that stranded four survivors
units today is broken (fresh-grounded Home at norm
(916,953), first try), and the gate line was verified with 2
waiting survivors - but the intake itself is unverified
(no card read, no Recruit tapped) and Quick Dispatch did not
run, so the unit's target is not met. The tracker is left
untouched, so the next tick re-produces the survivors
regular. No diamonds or money spent, no priced button tapped,
no other activity's rewards touched.

## Result stats

- target take in every waiting survivor at the front gate,
  then run Quick Dispatch
- achieved 0 recruits verified, 0 dispatched; gate line
  verified with 2 survivors, then read clear after taps,
  intake unverified
- resources_gained none
- points 0
- costs about 3 minutes, no items spent
- verified no
- blocker_category e
- survivors_recruited 0, quick_dispatch_runs 0,
  gate_line_verified yes, gate_line_count_at_entry 2,
  gate_line_clear_at_close yes, intake_verified no,
  radar_exit_attempts 1, radar_exit_successes 1,
  radar_exit_point 916,953, device_takeovers 0
