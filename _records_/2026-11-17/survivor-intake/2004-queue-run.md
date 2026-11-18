---
title: Survivor intake unit - device control channel unreachable
created: 2026-11-18T04:12:00Z
modified: 2026-11-18T04:12:00Z
version: 1.0.0
description: Queue unit survivors-2026-11-17-1803 failed - Mac mini computer-control channel could not bind any window
status: failed
grounded_in:
  - source: live device probes on Zhen's Mac mini, 2026-11-17 20:04-20:13 PST
  - source: _records_/2026-11-17/radar-tasks/1936-queue-run.md (ticker-1934, same failure shape 15 minutes earlier)
---

# Survivor intake unit 2004 - access failed

- Executor: ticker-2004
- Unit: survivors-2026-11-17-1803 (regular survivors, activity survivor-intake)
- Session window: 2026-11-17 20:04-20:13 PST (04:04-04:13 UTC 2026-11-18)
- Status: failed - execution impossible, no game screen was ever reached
- This is the 29th consecutive window-loss occurrence (ticker-1934
  at 19:36 PT was the 28th, same shape, radar unit completed as
  failed per the 1704 pattern). The NEW SHADE persists a ninth
  pass in a row: the channel cannot bind ANY window, not just the
  game window.
- The survivor line at the front gate was never observed; no
  survivor recruited, no Quick Dispatch run. Nothing claimed,
  nothing executed, no stamina or items spent. The tracker was
  left untouched, so the next tick re-produces the survivors
  regular.

## What was attempted

Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
connection_state online, last seen 04:04:22Z. Last War process
running. Computer-control session cc-58.

1. computer.control open_app LastWar - outcome_unknown, launch
   result could not be identified; did not repeat the launch.
2. computer.observe mode full - observation_unavailable, no target.
3. environment.describe - LastWar listed among running apps; no
   LastWar window in the window list (11 windows enumerated, none
   for the game); display 1920x1080.
4. computer.control activate LastWar - ax_windows_empty, no target
   window bound.
5. computer.control list_windows - 11 windows, none for LastWar.
6. screen.snap with no target - observation_unavailable.
7. computer.control activate Google Chrome window 125 -
   geometry_mismatch (origin_delta 256+, size_delta 256+,
   agent_display=false), input not dispatched.

Conclusion: the control channel cannot bind or observe ANY window
on the Mac right now, not just the game - every select fails with
geometry_mismatch / agent_display=false, and every observation
demands a target that cannot be bound. The game process is alive
but exposes no accessibility window. This is a channel/display-layer
failure, not a missing authorization and not a game login demand:
no login screen, no verification code and no "active on a different
device" dialog was ever seen. At least 3 attempts were made before
recording this as access-failed, per the standing rule (7 probes
in this pass, on top of the 16 probes of ticker-1934 fifteen
minutes earlier). No further input route was retried: the identical
method has now failed 29 consecutive times, and repeating it
unchanged would be a process failure under queue rule R2, not
diligence.

## Pass-level blockers found before game work

- VPS SSH still down: ssh centos@66.179.249.233 returns
  "Permission denied (publickey)" - the 2026-11-12 ~/.ssh loss is
  still unrecovered. Consequence for this pass: OWN PRS FIRST could
  not be done (no gh pr list via VPS), and no push or PR delivery
  is possible. The pass's commits stay on the local records branch
  only; the pass is partial on delivery. Freshest available PR
  state is the pr-catchall 1939 pass (18 minutes before this run):
  open PRs #711, #708, #425 unchanged, nothing adoptable, no
  adoption, fix, reply or hand-off owed by this job.
- Zombie Invasion: no seeding. The event ended - the most recent
  done zombie unit (zombie-invasion-zombie-2026-11-10-037,
  ticker-1804, 2026-11-15) verified live that the Glacieradon event
  ended, no Zombie Invasion tab in the Events hub, chain
  zombie-2026-11-10 closed with no successor. No zombie unit was
  enqueued.
- Sync: reaped 0, expired 0, due 22, produced 0 (all already
  queued), inbox 71. One completion marker reaped
  (radar-2026-11-17-1803). Branch reconcile skipped: remote
  records/2026-11-17 does not exist.
- Route change re-read LATE again (same as ticker-1934): the
  survivors unit was claimed and the token taken before the
  previous ticker record (1936-queue-run.md, same failure shape)
  was re-read; the unit was completed as failed per the 1704
  pattern instead. The next pass should re-read the previous
  ticker record before claiming any unit.

## Follow-up

- The survivors intake is still owed: the next tick re-produces
  the survivors regular, since the tracker was left untouched
  for this failed unit.
- Device control needs the owner or a later run to re-establish:
  the channel binds no window at all, which is wider than a
  game-window problem. If the Mac screen is locked, asleep, or on
  another Space, that state could not be verified from here -
  every probe that could show it failed the same way.
- VPS ~/.ssh recovery (IONOS route chosen by the owner 2026-11-14)
  is still the blocker for all PR/push delivery.
