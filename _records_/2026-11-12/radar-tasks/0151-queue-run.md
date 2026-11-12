---
title: Radar queue run 0151
created: 2026-11-12T09:53:00Z
modified: 2026-11-12T09:53:00Z
version: 1.0.0
description: Ticker-0134 radar unit - device input blocked, control channel locked with outcome_unknown, no game input possible, unit failed
status: unverified
---

# Radar - ticker-0134, 01:50 to 01:57 PST

Unit radar-2026-11-11-2203, executor ticker-0134. Status
failed: the Mac computer-control channel refused every game
input with outcome_unknown, so no radar work was done and
nothing was claimed. Computer sessions cc-695, cc-696,
cc-697. No device dialog, no login demand, no Touch ID, no
password typed.

## Posture

- tools/duel.py --json at 01:50: duel day 4, theme Train
  Heroes, radar_posture stack. On a stack day radar tasks
  are completed but NOT claimed, and map pins stay untapped.
  Day ends 2026-11-12 18:00 PT, 16.2 hours left.
- The unit file's window text reads "duel day 4 - radar
  stack" - it agrees with the live read this time, so no
  staleness correction is owed.

## What happened

- Token acquired about 01:50; unit claimed about 01:51
  (expires_at 2026-11-12T10:03:00Z, 02:03 PT).
- Input attempt 1 (cc-695): open_app LastWar - outcome_unknown,
  "An earlier action has an unresolved outcome. Stop sending
  input; read-only inspection is allowed. Report the
  uncertainty. A new local user submission is required before
  input can resume." Nothing was dispatched.
- Read-only inspection worked throughout: computer.observe and
  screen.snap returned the live base screen (window 676414,
  642x951 windowed, power 149,218,973, task "Build: Oil Well
  [0/1]").
- Input attempt 2 (cc-696, fresh session): activate Last War
  window 676414 - the same outcome_unknown.
- Input attempt 3 (cc-697, fresh session): exact-pointer click
  on the re-grounded dish candidate at normalized (55,594),
  snap_to_control false - the same outcome_unknown,
  input_dispatched false.
- Input attempt 4 (cc-697): list_windows worked (read-only) -
  two LastWar windows under the same pid 36941: 676414
  (642x951, "Last War") and 680257 (642x919, no title). A
  second click on the dish - the same outcome_unknown.
- connection.health: native and web transports healthy and
  connected, last response 0 to 6 seconds ago, nothing to
  repair. The block sits at the computer-use authorization
  layer, not the transport.
- This is the same lock the ticker-0134 scout pass hit minutes
  earlier and filed as Issue #689 (sessions cc-693 and cc-694,
  same window 676414, same error text). New sessions do not
  clear it; only a local user submission on the Mac can, and
  the owner is asleep, so no local submission is available
  to a detached overnight pass. Per Issue #689 a pass meeting
  this state stops: no further unit was attempted this pass,
  and the zombie-invasion unit 024 stays in inbox for the
  next tick, which will hit the same wall unless the channel
  clears.

## Live reads (read-only)

- Base HUD from the 01:52 screenshot: food 701.5M, iron 1.0G,
  coins 145.7M, diamonds 6,717, power 149,218,973, level 67,
  task "Build: Oil Well [0/1]", VS timer 16:08:21, event
  timers 1d 16:18:21 and 3d 16:08:21.
- Left-column icons: the dish candidate sits at normalized
  (55,594) in this screenshot (blue circular icon with a red
  dot). The rotating slot has moved since the 2105 unit's
  (55,702) grounding, so the next radar unit must re-ground
  from a fresh screenshot before tapping.

## Result stats

- target: radar tasks completed per the stack posture
  (complete, do not claim), stored tasks read
- achieved: 0 tasks - no game input was possible
- resources_gained: none
- points: 0
- costs: about 7 minutes, no items spent
- verified: yes (the input block and the base reads are
  observed on screen, not inferred; no closing figure is
  claimed)
- blocker_category: f (missing precondition - device input
  unavailable; control channel locked, Issue #689)
- follow_up: the next tick retries; if the channel is still
  locked, the next pass records its own access failure per
  Issue #689. The 7 pending rewards from the 2105 unit still
  await the day-5 release unit.
