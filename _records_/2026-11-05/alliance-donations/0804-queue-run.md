---
title: Alliance Donations Queue Run
created: 2026-11-05T08:04:00-08:00
modified: 2026-11-05T08:20:00-08:00
version: 1.0.0
description: Donations unit donations-2026-11-05-0603 executed by ticker-0804, failed on Mac screen capture failure, thirty-eighth consecutive pass with this blocker
status: failed
grounded_in:
  - source: Mac mini device channel responses on 2026-11-05 about 08:04 to 08:20 local
---

# Alliance donations 2026-11-05, ticker-0804

Unit donations-2026-11-05-0603, failed. No Alliance Techs screen
was ever read and no game input was dispatched: the Mac
screen-capture channel failed on every attempt, so the live
Donation Count, the coin button state, and any claimable
donation reward are all unread. This was a segment 1 unit
(planned_for 2026-11-05T14:03:00Z, expires 18:03:00Z); on a
working screen it would have read the Donation Count live, made
coin donations to the recommended technology until the button
greyed, and closed only on a live count read under the hard
closing rule of 2026-10-31.

## Attempts

- Mac mini 1c817413-83e2-0545-cb90-36d5e096a6bd online;
  LastWar (com.lastwar.ios, pid 59735) running, window
  1920x1080 at (0,0), window_id 160366, Google Chrome
  frontmost.
- Computer session cc-535: computer.control list_apps
  re-grounded the window fresh in this pass (1 window,
  1920x1080 at (0,0), window_id 160366, pid 59735).
  computer.control activate LastWar selected the window for
  background input but captured no observation, error
  "Failed to start stream due to audio/video capture
  failure", window_on_screen false, brought_to_front
  false; computer.observe (compact) failed with the same
  error twice; computer.control focus was rejected as
  invalid params (needs an element); computer.control
  open_app LastWar returned outcome_unknown; a third
  computer.observe (compact) failed with the same error.
- Computer session cc-536 (fresh, after ending cc-535):
  computer.control activate LastWar failed identically
  (window_on_screen false, brought_to_front false);
  computer.observe (compact) failed with the same error.
- Control check in cc-536: computer.control activate
  Google Chrome then succeeded with a full accessibility
  tree (60 elements, active tab "[cu] Coordinator —
  DeepSeek Harness"), so the capture channel works for
  on-screen windows and the fault is specific to the
  LastWar window stream.
- Fail-fast probe _tools_/mac_capture_probe.py 1.0.0
  (extracted from main to /tmp for this run, since this
  worktree on work/ops-execution-records carries no
  _tools_ folder) classifies this evidence
  OFF_SCREEN_WINDOW (high confidence), stop_pass yes,
  exit 10. The View-menu inspect could not run (gated on
  a fresh observation of the window, which is exactly
  what fails).
- Total capture attempts: 4 computer.observe failures
  and 2 activate calls returning the same stream error,
  across 2 sessions, plus one open_app outcome_unknown.
  This meets the standing at-least-3-attempts retry rule.
- No blind taps were dispatched: without an observation,
  any tap could land on the wrong control, so the unit
  stops here under the check-first rule. No
  different-device dialog was observed (no screen was ever
  captured) and no device takeover was needed.

## Outcome

- Status failed, blocker category e (repeated blocker,
  Issue 284). This is the thirty-eighth consecutive
  ticker pass with this blocker (thirty-seventh was
  ticker-0734, arms-race unit arms-race-2026-11-05-0603).
- No Donation Count read, no donation made, no reward
  claimed. Tracker untouched.
- Recovery still needs the one owner step: click the
  LastWar Dock icon once on the Mac mini (or run
  _tools_/mac_lastwar_front.sh in Terminal), then
  re-probe. The device exposes no shell or terminal
  command to this agent, so the script cannot be run
  from here.
- Issue 284 commented with this pass's failure; no new
  issue filed (same blocker, same issue).
- PR check at pass start: records PR 310 (records/
  2026-11-05, ticker-0304) carries no unanswered
  question for this job - the integrator's conflict note
  was already reconciled branch-side by the ticker-0704
  pass (merge commit 5bacb79ca) and its own records
  commit ac92eea48 pushed and ls-remote verified.
  Zombie Invasion was not seeded: the event ended at
  about the 2026-10-30 19:00 reset and the activity
  metadata forbids seeding until a Zombie Invasion tab
  is seen live in the Events hub again.
