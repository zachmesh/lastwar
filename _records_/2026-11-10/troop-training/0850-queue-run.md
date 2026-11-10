---
title: Troop training queue run 0850
created: 2026-11-10T16:50:00Z
modified: 2026-11-10T16:50:00Z
version: 1.0.0
description: Ticker-0834 training unit, partial - no barracks selected, Drill Ground not re-read, game found on TECH screen by unexplained navigation
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-10 08:47-08:50 PT
---

# 0850 queue run - Troop Training

Executor: ticker-0834. Unit: training-2026-11-10-0603.
Session window about 08:47 to 08:50 America/Los_Angeles.
Computer session cc-424 dropped mid-pass (a full observe
failed with observation_unavailable, no active session);
session cc-426 started to recover, no game state lost,
no different-device dialog.

## What was done

- On re-activating the game window after the session
  restart, the game was found on the TECH screen
  (research category list: Development 84%, Economy
  98%, Hero 68%, Units 77%, Squad 1 Max Level,
  Squad 2 11%, Squad 4 0%, Alliance Duel Max Level,
  Intercity Truck 95%), not on the base screen where
  the previous unit left it. No game input was sent
  by this pass between the base screenshot at 08:46
  and the TECH screenshot at about 08:49 except the
  session restart and the window activate, neither of
  which taps the game. The navigation is unexplained
  and is not attributed to any cause - it may be a
  delayed effect of the earlier back-arrow tap, a
  window-focus artefact, or another session's input.
  Flagged, not asserted.
- Slot-1 timer discrepancy, flagged unverified: the
  research unit in this same pass read slot 1 as
  1d 01:35:27 at 08:46; the TECH screen at about
  08:49 reads slot 1 as 1d 01:51:59. A countdown
  cannot gain 16 minutes over 3 minutes of wall
  time, so one of the two reads is misread. Neither
  figure is claimed as the true timer without a
  re-read; the 1d 01:35:27 coherence argument in the
  0846 research record (matching the 0116 read) is
  now weakened by this second read. Slot 2 reads
  Idle on both screens.
- The back arrow at norm 129,928 was tapped once and
  the base screen returned (Build: Oil Well banner,
  HEROES and WORLD buttons, power 148,058,020,
  iron 939.3M, coin 84.1M read live). The game was
  left on the base screen with nothing selected.
- No barracks tent was tapped in this unit: the
  token lease expired at 08:51:29, inside the
  pass budget, and the unit closed before a new
  grounding route could be tried. The untried routes
  named for the next unit are the full-observe
  accessibility tree with click_element on the tent
  control, and a fullscreen reframe via the green
  zoom button (never Ctrl-Cmd-F or Escape, both
  crash the app). The retired points must not be
  re-tapped: the right-edge tent points (0337) and
  the formation-yard points (0034).

## What was not done

- No barracks was requeued: no barracks state was
  verified live in this unit, and the Drill Ground
  screen was NOT re-read live either. The Drill
  Ground Full toast (39,460 of 39,460, last read
  live 2026-10-31) stays carried forward unverified.
  Carried-forward state (not re-verified): Lv.30
  batch requeued 2026-11-07 about 17:08 (1d 17h)
  was due about 10:22 on 2026-11-09; Lv.27 idle and
  blocked at the 1330 read on 2026-11-09; Lv.24 and
  the fourth barracks not checked. Tracker untouched,
  per the partial rule; the next tick re-produces
  the training regular.
- Quick Dispatch stays untapped: its effect is still
  unverified and it may march troops out, left for an
  owner decision or a learn-first exploration unit.
- R2 process failure: this is the fifth consecutive
  training partial with the same blocker (0039, 1330,
  0034, 0337, this unit), each with a changed method
  and none requeuing a barracks. Per queue rule R2 a
  fourth identical partial is a process failure, not
  a result; the 0337 pass already reported it as one
  and commented the blocker on issue #150. This unit
  adds its evidence comment to #150 as well. The
  next unit must use a new grounding route, not
  another tap on the retired points.

## Figures read live on screen

- Food 612.5M, iron 939.3M, coin 84.1M, power
  148,058,020, diamonds 13.22K at close.
- Build slot in use: Oil Well (0/1), 1/4 hammer icon.
- No login or verification was demanded, and no
  different-device dialog appeared.

## Result statistics

- target 4, achieved 0, resources_gained none, costs
  about 3 minutes play, verified yes, blocker_category e,
  device_takeovers 0
