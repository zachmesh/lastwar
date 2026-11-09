---
title: Alliance Gifts Queue Run
created: 2026-11-04T22:04:00-08:00
modified: 2026-11-04T22:04:00-08:00
version: 1.0.0
description: Gifts unit gifts-2026-11-04-1830 executed by ticker-2204
status: failed
grounded_in:
  - source: Mac mini device channel responses on 2026-11-04 about 22:04 to 22:15 local
---

# Alliance gifts 2026-11-04, ticker-2204

Unit gifts-2026-11-04-1830, failed. No gift screen was ever read
and no gift was claimed: the Mac screen-capture channel failed on
every attempt, so no game input was dispatched.

## Attempts

- Mac mini 1c817413-83e2-0545-cb90-36d5e096a6bd online;
  LastWar window running fullscreen 1920x1080 (pid 59735),
  Google Chrome frontmost.
- Computer session cc-490: computer.control list_windows
  succeeded and listed the LastWar window, so the control
  channel itself was reachable; the capture stream was not.
  computer.control activate LastWar selected the window for
  background input but captured no observation, error
  "Failed to start stream due to audio/video capture
  failure"; computer.observe (compact) failed with the same
  error; computer.control describe LastWar failed with the
  same error.
- computer.control open_app LastWar returned outcome_unknown
  (launch result unverifiable, not repeated, per the command
  guidance); the window was already known running and no
  restart was intended.
- Computer session cc-491 (fresh, after ending cc-490):
  activate LastWar again captured no observation with the
  same error. connection.health reported both transports
  healthy (native and web connected), so the failure is in
  the screen-capture stream, not the connection. A final
  computer.observe (compact) failed with the same error.
- Total capture attempts: 5 across 2 sessions, all failing
  with the identical audio/video capture error. This meets
  and exceeds the standing at-least-3-attempts retry rule.
- No blind taps were dispatched: without an observation, any
  tap could land on the wrong control, so the unit stops here
  under the check-first rule. No different-device dialog was
  observed (no screen was ever captured) and no device
  takeover was needed.

## Repeated failure mode

- This is the same blocker already filed as GitHub Issue
  #284 (label tooling, still open at this pass). The
  ticker-2134 pass was the previous ticker pass known to
  have failed identically; this pass is the next ticker pass
  after 2134 and does not assert an exact consecutive count
  beyond that. This pass commented on #284 instead of filing
  a duplicate. Until the Mac screen-recording stream
  recovers, further ticker passes will fail their first unit
  the same way; the inbox held 69 units at this pass.
- This is a device capture failure, not an authorization
  failure: the standing owner authorization is intact, the
  device is online, and the app is running.

## Other pass steps

- Own PRs checked first: open records PR 293 (2026-11-04,
  post-1931 merge, awaiting the 2300 batch) names Owner
  lastwar-pr-integrator, not this job; it is MERGEABLE with
  no comments, so nothing was owed before game work. Older
  open records PRs 265 (2026-11-02), 256 (2026-11-03) and
  187 (2026-11-01) likewise name the integrator; their
  action-log conflicts belong to the integrator, not to this
  ticker pass, and were not attempted inside this pass's
  budget.
- Sync: reaped 0, expired 1, produced nothing new, 21
  regulars already queued.
- No zombie seeding: zombie chain zombie-2026-10-28 closed
  with unit 066 on 2026-10-30 (event ended about the 19:00
  reset 2026-10-30, no Zombie tab in the Events hub), and
  the activity metadata forbids seeding a fresh chain until
  a Zombie Invasion tab is seen live again.
- Tracker untouched: a failed unit does not mark the
  regular, so the next tick re-produces the gifts unit.
- Pass stopped after this unit: with no observation channel,
  a second unit would fail identically and burn the pass
  budget, so the remaining inbox units were left queued.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs were delivered through a temporary
  worktree onto the records/2026-11-04 branch, leaving that
  state undisturbed.

## Outcome

Failed. No gift checked or claimed, no diamonds, money,
speedups or other spending. No alliance diplomacy, no
assembly, no teleport.

## Result stats

- target 0, achieved 0, resources_gained none, costs 0,
  verified no, blocker_category f, device_takeovers 0,
  capture_attempts 5, regular_claimed 0, premium_claimed 0,
  issue 284
