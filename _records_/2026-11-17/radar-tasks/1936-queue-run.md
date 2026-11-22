---
title: Radar release unit - device control channel unreachable
created: 2026-11-18T03:49:00Z
modified: 2026-11-18T03:49:00Z
version: 1.0.0
description: Queue unit radar-2026-11-17-1803 failed - Mac mini computer-control channel could not bind any window
status: failed
grounded_in:
  - source: live device probes on Zhen's Mac mini, 2026-11-17 19:36-19:49 PST
  - source: tools/duel.py live read, 2026-11-17 19:36 PST
---

# Radar release unit 1936 - access failed

- Executor: ticker-1934
- Unit: radar-2026-11-17-1803 (regular radar, activity radar-tasks)
- Session window: 2026-11-17 19:36-19:49 PST (03:36-03:49 UTC 2026-11-18)
- Status: failed - execution impossible, no game screen was ever reached
- This is the 28th consecutive window-loss occurrence (ticker-1904
  at 19:04 PT was the 27th, same shape, harvest unit completed as
  failed per the 1704 pattern). The NEW SHADE persists an eighth
  pass in a row: the channel cannot bind ANY window, not just the
  game window.
- Posture at entry: duel day 3 (Age of Science), radar_posture release
  per tools/duel.py live read at 19:36 PST - the stack built on day 2
  was due for release today, claims score 10,000 base each. The unit
  file's window label still said "duel day 2 - radar stack"; the live
  duel read governs and the label is stale by one day boundary (day 3
  began 18:00 PST 2026-11-17).
- Nothing claimed, nothing executed, no stamina or items spent.

## What was attempted

Device: Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
connection_state online, last seen 18:01 PST. Last War process
running (pid 11266). Computer-control sessions cc-55, cc-56, cc-57.

1. computer.control activate LastWar - ax_windows_empty, no target
   window bound.
2. computer.control open_app LastWar - outcome_unknown, launch result
   could not be identified; list_windows after it showed no LastWar
   window (10 windows, none for the game).
3. computer.observe mode current - observation_unavailable, no target.
4. screen.snap with no target - observation_unavailable.
5. computer.control activate Finder window 28 - geometry_mismatch
   (origin_delta 256+, size_delta 256+, agent_display=false), failed.
6. computer.control activate Chrome window 125 - same
   geometry_mismatch failure.
7. Fresh session cc-56: open_app LastWar again - outcome_unknown.
8. frontmost_app - "the app in front is the assistant itself".
9. open_app Chrome with URL - refused, two Chrome instances match.
10. computer.control current_target - target bound to LastWar pid
    11266, mode background, has_target true, but still no AX window.
11. inspect_menu Window - stale_observation, no bound window.
12. key control+right (Space switch) - blocked, observation_required,
    input not dispatched.
13. Fresh session cc-57: screen.snap with no target - still
    observation_unavailable.
14. open_app Calculator - outcome_unknown, geometry_mismatch
    (agent_display=false).
15. connection.repair target web - reported healthy, no change.
16. open_app LastWar once more after repair - outcome_unknown again.

Conclusion: the control channel cannot bind or observe ANY window on
the Mac right now, not just the game - every select fails with
geometry_mismatch / agent_display=false, and every observation
demands a target that cannot be bound. The game process is alive
but exposes no accessibility window. This is a channel/display-layer
failure, not a missing authorization and not a game login demand:
no login screen, no verification code and no "active on a different
device" dialog was ever seen. At least 3 attempts were made before
recording this as access-failed, per the standing rule (in fact 16
probe/control attempts across 3 sessions plus a connection repair).

## Pass-level blockers found before game work

- VPS SSH still down: ssh centos@66.179.249.233 returns
  "Permission denied (publickey)" - the 2026-11-12 ~/.ssh loss is
  still unrecovered. Consequence for this pass: OWN PRS FIRST could
  not be done (no gh pr list via VPS), and no push or PR delivery
  is possible. The pass's commits stay on the local records branch
  only; the pass is partial on delivery.
- Zombie Invasion: no seeding. The event ended - the most recent
  done zombie unit (zombie-invasion-zombie-2026-11-10-037,
  ticker-1804, 2026-11-15) verified live that the Glacieradon event
  ended, no Zombie Invasion tab in the Events hub, chain
  zombie-2026-11-10 closed with no successor. No zombie unit was
  enqueued.
- Sync: reaped 0, due 22, produced 0 (all already queued), inbox 66.
  One completion marker reaped (harvest-2026-11-17-1803). Branch
  reconcile skipped: remote records/2026-11-17 does not exist.

## Follow-up

- Route change re-read LATE again (same as ticker-1904): the radar
  unit was claimed and the token taken before the previous record
  (ticker-1904, same failure shape) was re-read; the unit was
  completed as failed per the 1704 pattern instead. The next pass
  should re-read the previous ticker record before claiming any unit.
- The radar stack release (duel day 3) is still owed: the next tick
  re-produces the radar regular, since the tracker was left untouched
  for this failed unit.
- Device control needs the owner or a later run to re-establish: the
  channel binds no window at all, which is wider than a game-window
  problem. If the Mac screen is locked, asleep, or on another Space,
  that state could not be verified from here - every probe that
  could show it failed the same way.
- VPS ~/.ssh recovery (IONOS route chosen by the owner 2026-11-14)
  is still the blocker for all PR/push delivery.
