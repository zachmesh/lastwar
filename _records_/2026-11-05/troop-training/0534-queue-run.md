---
title: Troop Training Queue Run
created: 2026-11-05T05:34:00-08:00
modified: 2026-11-05T05:45:00-08:00
version: 1.0.0
description: Training unit training-2026-11-05-0203 executed by ticker-0534, failed on Mac screen capture failure, thirty-fourth consecutive pass with this blocker
status: failed
grounded_in:
  - source: Mac mini device channel responses on 2026-11-05 about 05:34 to 05:45 local
---

# Troop training 2026-11-05, ticker-0534

Unit training-2026-11-05-0203, failed. No barracks screen was ever
read and no training was requeued or claimed: the Mac
screen-capture channel failed on every attempt, so no game
input was dispatched. On a working screen this unit would have
checked the four barracks and requeued any idle batch, and would
have read the Drill Ground screen live first under the standing
third-strike blocker note (Drill Ground Full, 39,460 of 39,460).

## Attempts

- Mac mini 1c817413-83e2-0545-cb90-36d5e096a6bd online;
  LastWar (com.lastwar.ios, pid 59735) running, window
  2560x1440 at (0,360), window_id 160366; Google Chrome
  frontmost at session start, Keychain Access frontmost at
  the close of the probe.
- Computer session cc-522: computer.control activate LastWar
  selected the window for background input but captured no
  observation, error "Failed to start stream due to audio/video
  capture failure", window_on_screen false,
  brought_to_front false; computer.observe (compact) failed
  three times with the same error (a 10 second wait between
  attempts 1 and 2 changed nothing); computer.control open_app
  LastWar returned outcome_unknown with no verifiable launch
  result and the window still listed under the same pid.
- Control observation of a Chrome window in the same session
  (cc-522) succeeded with a full accessibility tree (the
  Coordinator harness tab), so the capture channel works for
  on-screen windows and the fault is specific to the LastWar
  window stream.
- This meets the standing at-least-3-attempts retry rule.
  No blind taps were dispatched: without an observation, any
  tap could land on the wrong control, so the unit stops here
  under the check-first rule. No different-device dialog was
  observed (no screen was ever captured) and no device
  takeover was needed.

## Probe classification

- Probe _tools_/mac_capture_probe.py 1.0.0 run on this pass's
  evidence (evidence file /tmp/ticker-0534-probe-evidence.json):
  diagnosis OFF_SCREEN_WINDOW, high confidence, stop_pass yes,
  exit 10. The LastWar window sits on an inactive Space, so its
  pixel stream cannot start. Recovery is one owner step on the
  Mac mini: click the LastWar Dock icon once (or run
  _tools_/mac_lastwar_front.sh in Terminal), then re-probe.
- This is the thirty-fourth consecutive ticker pass with this
  blocker (Issue 284), counting the ticker-0504 pass at about
  05:12 local as the thirty-third. The inbox still holds 70
  units; nothing was executed in this pass.

## Tracker

- Tracker untouched: a failed unit leaves the regular due, so
  the next tick re-produces training.
