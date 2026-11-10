---
title: Alliance Donations Queue Run
created: 2026-11-05T08:34:00-08:00
modified: 2026-11-05T08:39:00-08:00
version: 1.0.0
description: Donations unit donations-2026-11-03-1241 executed by ticker-0834, failed on Mac screen capture failure, thirty-ninth consecutive pass with this blocker
status: failed
grounded_in:
  - source: Mac mini device channel responses on 2026-11-05 about 08:36 to 08:39 local
---

# Alliance donations 2026-11-05, ticker-0834

Unit donations-2026-11-03-1241, failed. No Alliance Techs screen
was ever read and no game input was dispatched: the Mac
screen-capture channel failed on every attempt, so the live
Donation Count, the coin button state, and any claimable
donation reward are all unread.

## The unit itself was already superseded

This unit was enqueued by ticker-0434 on 2026-11-03 as a re-read
after its 00:19:35 cooldown timer (started about 04:41 local
2026-11-03), to confirm the Donation Count state. The 0521
re-read unit already answered that question on 2026-11-03: it
read Donation Count 1/30 live after the timer, proving tap 6
did not land. The 11-03 reset day is over, so this unit's
original question no longer has a live answer to read even on
a working screen. It lingered in the inbox because it carries
no expires_at; the sync's expiry path never reaped it. Noted
for queue hygiene, not filed as a new issue: the stale-unit
shape is already visible in the stats (28 inbox units, several
from 11-03/11-04).

## Attempts

- Mac mini 1c817413-83e2-0545-cb90-36d5e096a6bd online;
  LastWar (com.lastwar.ios, pid 59735) running, window
  1920x1080 at (0,0), window_id 160366, Google Chrome
  frontmost.
- Computer session cc-537: computer.control open_app
  LastWar returned outcome_unknown (launch unverified,
  not replayed). computer.observe (compact) then
  succeeded on the Chrome window (60 elements, active
  tab "[cu] Coordinator — DeepSeek Harness"), so the
  capture channel works for on-screen windows.
- computer.control activate LastWar (twice, second with
  window_id 160366) selected the window for background
  input but captured no observation, error "Failed to
  start stream due to audio/video capture failure",
  window_on_screen false, brought_to_front false.
  computer.observe (compact) failed with the same error
  twice; computer.observe (image view, last resort)
  failed with the same error once.
- Fail-fast probe _tools_/mac_capture_probe.py 1.0.0
  classifies this evidence OFF_SCREEN_WINDOW (high
  confidence), stop_pass yes, exit 10: the LastWar
  window sits on an inactive Space and the capture
  stream cannot start because it is the pixel stream
  of an off-screen window. The View-menu inspect step
  could not run (gated on a fresh observation of the
  window, which is exactly what fails).
- Total capture attempts: 3 computer.observe failures
  and 2 activate calls returning the same stream error,
  plus one open_app outcome_unknown. This meets the
  standing at-least-3-attempts retry rule.
- No blind taps were dispatched: without an observation,
  any tap could land on the wrong control, so the unit
  stops here under the check-first rule. No
  different-device dialog was observed (no screen was ever
  captured) and no device takeover was needed.

## Outcome

- Status failed, blocker category e (repeated blocker,
  Issue 284). This is the thirty-ninth consecutive
  ticker pass with this blocker (thirty-eighth was
  ticker-0804, donations unit donations-2026-11-05-0603).
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
  pass (merge commit 5bacb79ca). Zombie Invasion was
  not seeded: the event ended at about the 2026-10-30
  19:00 reset and the activity metadata forbids seeding
  until a Zombie Invasion tab is seen live in the Events
  hub again.
