---
title: Survivor intake queue run 0941
created: 2026-11-11T17:51:00Z
modified: 2026-11-11T17:51:00Z
version: 1.0.0
description: Ticker-0936 survivors unit - one gate survivor processed, question bubble cleared, figure walked in, no recruit card, gate clear as observed, partial
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-11 09:41-09:50 PT
---

# Survivor intake queue run 0941 (ticker-0936)

Unit: survivors-2026-11-11-0603. Status: partial.
Activity: survivor-intake.

## Gate line - one survivor processed, no card read

- At entry the base screen showed ONE question-mark bubble at the
  front gate, left side, above a small figure. Grounded fresh:
  bubble norm (114,650), figure norm (109,688), gate sign norm
  (190,637). Entry HUD: food 680.8M, iron 1.0G, coin 127.8M,
  diamonds 6,317, total power 149,218,973.
- Tapped the figure (the reliable target per the activity
  metadata), move, wait 1 second, then exact click
  (snap_to_control false). The tap dispatched; the receipt
  reported no change observed, so the state was re-read from
  fresh screenshots instead of trusting the receipt.
- After the tap the "?" bubble was GONE on two post-tap
  screenshots (09:44 and 09:47), and the figure was gone from
  the gate. A zoomed crop of the gate before the tap shows a
  human survivor figure (light hair, white shirt, dark shorts)
  standing under the bubble in front of the Zombies-signed
  gate; the after crop shows the same spot empty except for a
  small green marker, unresolved (possibly a plant behind the
  figure, or a processed marker - not verified). Two
  blue-capped figures walk the road above the gate in the
  post-tap views.
- No New Survivor Incoming card, no dialog line, no name, role
  or trait was ever read on screen. No smiley-face bubble was
  observed at the gate after the tap (the processed-state
  marker the 1644 done required), so the intake is recorded
  as processed but unverified in detail: 1 survivor processed
  by the "?"-cleared sequence on two screenshots, 0 recruits
  identified. No further "?" bubbles are visible at the gate
  in the closing view: gate line clear as observed.
- Quick Dispatch did NOT run: no recruit card appeared, so no
  building post is known to have been created, and per the
  1644 refinement Quick Dispatch applies after an intake with
  posts, not after a dialog-type survivor. This matches the
  0520 unit's decision the same morning. The standing R7
  Quick Dispatch debt from the 0834 intake (2026-11-10) is
  unchanged by this unit - that intake likewise showed no
  card, so there is still no verified recruit with a post to
  dispatch.

## Note on the 0520 unit

- The 0520 unit this morning (ticker-0504) tapped nearly the
  same gate point (figure norm 127,688) and found a red panda
  pet marker remaining. This unit's before-crop proves the
  figure under this bubble was a human survivor, not the pet:
  the pet marker sits elsewhere at the gate. The two units
  are therefore different intakes at the same gate spot, not
  a repeat tap on the same figure. The 0520 follow-up asked
  for a zoomed crop of the gate before any tap; this unit
  cropped after the tap but from the pre-tap screenshot, so
  the identification still rests on pre-tap evidence.

## Session

- One computer-session drop mid-unit (cc-588 closed, cc-589
  restarted); the game window was re-selected and the base
  screen re-read live after the restart, no action lost.
- The visual-grounding re-check call timed out once at 180
  seconds with no result; the gate state was verified from
  the screenshots and crops read directly instead.
- No different-device dialog, no login or verification
  demanded, no diamonds or money spent, no paid button
  tapped. No other activity's rewards touched.

## Outcome

Partial, unverified in detail. 1 survivor processed (figure
gone, "?" cleared on two screenshots), 0 recruits identified,
gate line clear as observed. Quick Dispatch did not run (no
verified post). The tracker is left untouched, so the next
tick re-produces the survivors regular and the work resumes
as a fresh unit.

## Result stats

- target 1, achieved 1, resources_gained none, costs about 10
  minutes, verified yes, blocker_category h, survivors_recruited
  0, survivors_verified 0, survivors_processed 1,
  bubbles_seen 1, bubbles_remaining 0, quick_dispatch_run no,
  entry_attempts 1, device_takeovers 0
