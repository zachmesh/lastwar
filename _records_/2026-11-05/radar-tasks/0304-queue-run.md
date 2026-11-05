---
title: Radar Tasks Queue Run
created: 2026-11-05T03:04:00-08:00
modified: 2026-11-05T03:12:00-08:00
version: 1.0.0
description: Radar unit radar-2026-11-05-0203 executed by ticker-0304, failed on Mac screen capture failure, twenty-ninth consecutive pass with this blocker
status: failed
grounded_in:
  - source: Mac mini device channel responses on 2026-11-05 about 03:04 to 03:12 local
---

# Radar tasks 2026-11-05, ticker-0304

Unit radar-2026-11-05-0203, failed. No radar screen was ever
read and no task was executed or claimed: the Mac
screen-capture channel failed on every attempt, so no game
input was dispatched. This was a stack-day unit (duel day 4):
on a working screen it would have run Quick Execute batches
and recorded the pin inventory without claiming anything.

## Attempts

- Mac mini 1c817413-83e2-0545-cb90-36d5e096a6bd online;
  LastWar (com.lastwar.ios, pid 59735) running, window
  1920x1080 at (0,0), Google Chrome frontmost.
- Computer session cc-512: computer.control activate LastWar
  selected the window for background input but captured no
  observation, error "Failed to start stream due to audio/video
  capture failure", window_on_screen false,
  brought_to_front false; computer.observe (compact) failed
  with the same error; computer.observe (image) failed with
  the same error; computer.control open_app LastWar returned
  outcome_unknown. connection.health reported both transports
  healthy (native and web connected), so the failure is in
  the screen-capture stream, not the connection.
- Computer session cc-513 (fresh, after ending cc-512):
  computer.control activate LastWar again reported
  window_on_screen false, brought_to_front false;
  computer.observe (compact) failed with the same error;
  screen.snap failed with the same error.
- Computer control list_windows with app LastWar confirms
  the window exists: 1 window, 1920x1080 at (0,0),
  window_id 160366, pid 59735.
- Control observation of a Chrome window in the same
  session (cc-513) succeeds with a full accessibility tree
  (Gmail inbox), so the capture channel works for on-screen
  windows and the fault is specific to the LastWar window
  stream.
- Total capture attempts: 4 across 2 sessions, all failing
  with the identical audio/video capture error. This meets
  the standing at-least-3-attempts retry rule.
- No blind taps were dispatched: without an observation, any
  tap could land on the wrong control, so the unit stops here
  under the check-first rule. No different-device dialog was
  observed (no screen was ever captured) and no device
  takeover was needed.

## Probe classification

- First pass to run the fail-fast probe landed by PR 307:
  _tools_/mac_capture_probe.py 1.0.0 on the evidence above
  classifies OFF_SCREEN_WINDOW (high confidence),
  stop_pass yes. Evidence file kept at
  /tmp/ticker-0304-probe-evidence.json.
- The View-menu inspect step could not run this pass: it is
  gated on a fresh observation of the LastWar window, which
  is exactly what the capture failure prevents. The
  classification stands on the activate evidence alone, as
  the probe tool allows (on_screen false plus
  brought_to_front false is high confidence).

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue
  #284 (label tooling, still open at this pass). The
  ticker-0234 pass was the twenty-eighth consecutive ticker
  pass to fail identically (scout unit, finished about
  02:38 local); this pass is the twenty-ninth. This pass
  commented on #284 instead of filing a duplicate.
- This is a device capture failure, not an authorization
  failure: the standing owner authorization is intact, the
  device is online, and the app is running.

## Other pass steps

- Own PRs checked first: the live records PR for today, PR
  304 (records/2026-11-05, ticker-0004), was CONFLICTING
  after the 0300 batch pass merged PR 187 into main
  (merge commit 2071992b). Per the integrator's note on the
  PR, this pass resolved the conflict on the branch side:
  merged main 2071992b into records/2026-11-05 as
  6d65fd817, resolving _logs_/repo-actions/action-log.jsonl
  as a union of both sides' appends (854 entries: branch
  853 plus main-only 1, the pr-integration 2026-11-02-1500
  run), also splitting fused double-entry lines and dropping
  a blank line that pre-existed in both versions; the
  merge-base's 796 entries are all preserved. Pushed via
  the bundle route and verified with git ls-remote
  (remote records/2026-11-05 at 6d65fd817); commented the
  resolution on PR 304. The 0300 batch pass then merged PR
  304 into main (merge commit efc6de7387) and opened PR 309
  for the 2026-11-01 merge line; the records/2026-11-05
  branch continues and this pass's outputs ride on it.
- Sync: reaped 0, expired 5 (events, passes, secrets,
  treasures, trucks 2026-11-04-2257), produced nothing new,
  21 regulars already queued.
- No zombie seeding: no zombie-invasion unit in inbox or
  claimed; the chain zombie-2026-10-28 closed with unit 066
  on 2026-10-30 (event ended about the 19:00 reset
  2026-10-30, no Zombie tab in the Events hub), and the
  activity metadata forbids seeding a fresh chain until a
  Zombie Invasion tab is seen live again.
- Tracker untouched: a failed unit does not mark the
  regular, so the next tick re-produces the radar unit.
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

Failed. No radar task executed or claimed, no diamonds, money,
speedups or other spending. No alliance diplomacy, no
assembly, no teleport.

## Result stats

- target execute stack-day radar tasks, achieved 0,
  resources_gained none, costs 3 minutes, no game input,
  0 stamina, verified no, blocker_category e (repeated
  blocker), capture_attempts 4, sessions cc-512 cc-513,
  diagnosis OFF_SCREEN_WINDOW, issue 284
