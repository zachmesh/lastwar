---
title: Alliance Donations Queue Run
created: 2026-11-05T04:05:00-08:00
modified: 2026-11-05T04:10:00-08:00
version: 1.0.0
description: Donations unit donations-2026-11-05-0203 executed by ticker-0404, failed on Mac screen capture failure, thirty-first consecutive pass with this blocker
status: failed
grounded_in:
  - source: Mac mini device channel responses on 2026-11-05 about 04:05 to 04:10 local
---

# Alliance donations 2026-11-05, ticker-0404

Unit donations-2026-11-05-0203, failed. No Alliance Techs screen
was ever read and no donation was made: the Mac screen-capture
channel failed on every attempt, so no game input was dispatched.
On a working screen this unit would have opened Alliance Techs
and donated with the coin button until the daily count was used
up or the button greyed on its cooldown, then closed on a live
Donation Count read.

## Attempts

- Mac mini 1c817413-83e2-0545-cb90-36d5e096a6bd online;
  connection health reports both native and web transports
  connected; LastWar (com.lastwar.ios) window 160366 selected.
- Computer session cc-516: computer.control activate LastWar
  selected the window for background input but captured no
  observation, error "Failed to start stream due to audio/video
  capture failure", window_on_screen false,
  brought_to_front false, frontmost app Google Chrome;
  computer.observe (compact) failed twice with the same error.
- Computer session cc-517 (fresh, after ending cc-516):
  computer.control activate LastWar again reported
  window_on_screen false, brought_to_front false;
  computer.observe (compact) failed with the same error;
  computer.observe (image) failed with the same error.
- Total capture attempts: 4 observe calls across 2 sessions,
  plus 2 activate calls reporting the same capture error.
  This meets the standing at-least-3-attempts retry rule.
- No blind taps were dispatched: without an observation, any
  tap could land on the wrong control, so the unit stops here
  under the check-first rule. No different-device dialog was
  observed (no screen was ever captured) and no device
  takeover was needed.

## Probe classification

- The fail-fast probe _tools_/mac_capture_probe.py 1.0.0
  classifies this evidence OFF_SCREEN_WINDOW (high
  confidence), stop_pass yes. Evidence file kept at
  /tmp/ticker-0404-probe-evidence.json.
- The View-menu inspect step could not run this pass: it is
  gated on a fresh observation of the LastWar window, which
  is exactly what the capture failure prevents. The
  classification stands on the activate evidence alone, as
  the probe tool allows (on_screen false plus
  brought_to_front false is high confidence).
- Recovery is one owner step on the Mac mini: click the
  LastWar Dock icon once (or run _tools_/mac_lastwar_front.sh
  in Terminal), then re-probe and expect window_on_screen
  true. Never use Control-Command-F or Escape on this app.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue
  #284 (label tooling, still open at this pass). The
  ticker-0334 pass was the thirtieth consecutive ticker
  pass to fail identically (arms-race unit, finished about
  03:38 local); this pass is the thirty-first. This pass
  commented on #284 instead of filing a duplicate.
- This is a device capture failure, not an authorization
  failure: the standing owner authorization is intact, the
  device is online, and the app is running.

## Other pass steps

- Own PRs checked first: the live records PR for today, PR
  310 (records/2026-11-05, ticker-0304), is open with no
  comments and no reviews, so there is nothing to address.
  The other open records PRs (309, 301, 265, 256) belong to
  the integrator, not to this job.
- Sync: reaped 0, expired 0, due 21, produced nothing new,
  21 regulars already queued.
- No zombie seeding: no zombie-invasion unit in inbox or
  claimed; the chain zombie-2026-10-28 closed with unit 066
  on 2026-10-30 (event ended about the 19:00 reset
  2026-10-30, no Zombie tab in the Events hub), and the
  activity metadata forbids seeding a fresh chain until a
  Zombie Invasion tab is seen live again.
- Tracker untouched: a failed unit does not mark the
  regular, so the next tick re-produces the donations unit.
- Pass stopped after this unit: with no observation channel,
  a second unit would fail identically and burn the pass
  budget, so the remaining inbox units were left queued.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through the
  ticker-0004-1105-delivery worktree onto the
  records/2026-11-05 branch, leaving that state undisturbed.

## Outcome

Failed. No donation made, no diamonds, money, speedups or
other spending. No alliance diplomacy, no assembly, no
teleport.

## Result stats

- target donate the daily coin count until used up, achieved 0,
  resources_gained none, costs 5 minutes, no game input,
  0 stamina, verified no, blocker_category e (repeated
  blocker), capture_attempts 4, sessions cc-516 cc-517,
  diagnosis OFF_SCREEN_WINDOW, issue 284
