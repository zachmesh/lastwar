---
title: Survivors 2026-11-17 ticker-1204 failed, LastWar window missing
created: 2026-11-17T20:12:00Z
modified: 2026-11-17T20:12:00Z
version: 1.0.0
description: Survivors unit survivors-2026-11-17-1003 failed, LastWar has no window on the Mac mini
status: failed
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-17T20:04Z to 20:06Z
  - source: computer.session cc-31 and cc-32, computer.control list_windows, current_target, activate and open_app, computer.observe, 2026-11-17T20:06Z to 20:11Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lastwar-probe-1211.json, 2026-11-17T20:11Z
  - source: tools/duel.py --json, 2026-11-17T20:11Z
  - source: unauthenticated GitHub REST API reads of zachmesh/lastwar open PRs, 2026-11-17T20:08Z
  - source: VPS SSH probe, 2026-11-17T20:04Z
---

# Survivors 2026-11-17 ticker-1204 failed, LastWar window missing

- Executor: ticker-1204
- Unit: survivors-2026-11-17-1003, regular survivors, activity survivor-intake, priority 3, est 3 minutes
- Session window: 12:04-12:12 local, token held 12:04-12:12 local

## What happened

- The Mac mini (Zhen's Mac mini, 1c817413-83e2-0545-cb90-36d5e096a6bd)
  is back ONLINE - device.list reports online with last_seen
  2026-11-17T20:02:14Z, fresh at the time of the check. This ends
  the offline stretch that froze the previous 24 ticker passes
  (last_seen had been stuck at 2026-11-15T13:19:56Z).
- But the game window is gone. LastWar (pid 11266, bundle
  com.lastwar.ios) is in the running-apps list and is the bound
  computer-control target, yet `list_windows` with app LastWar
  returns 0 windows, repeated three times across 12:06-12:11 PT,
  including 25 seconds after the second launch attempt. The app
  process is alive but windowless - a step beyond the issue #284
  off-screen window (there the window existed on an inactive
  Space); here there is no window at all to bring forward.
- Recovery attempts, all inside sessions cc-31 and cc-32:
  open_app LastWar twice (outcome_unknown both times, no window
  after 8-10 seconds each, then 25 more seconds); activate LastWar
  twice (brought_to_front false, ax_windows_empty); observe
  (observation_unavailable, no target window); a Chrome-window
  probe failed the same way (geometry_mismatch on window 125,
  whose listed geometry is unchanged) and frontmost_app reports
  the assistant itself is in front. No Touch ID, no password, no
  game input of any kind was sent.
- Probe classification: tools/mac_capture_probe.py on the
  assembled evidence returns OFF_SCREEN_WINDOW, high confidence,
  stop_pass yes (exit 10). The documented recovery is the same
  owner step as issue #284 - click the LastWar Dock icon once
  (or run tools/mac_lastwar_front.sh in Terminal) - then
  re-probe. No background control route unblocks a windowless
  app: open_app returns outcome_unknown, activate needs a
  window, set_window_frame needs an observation.
- No survivor work was executed, nothing claimed, nothing spent.
  The tracker is untouched. The pass stopped after this unit
  rather than cascading failed units - the blocker is systemic
  and every further unit would fail identically. This is the
  thirteenth consecutive ticker occurrence of the window loss
  (ticker-1104 harvest and ticker-1134 radar failed the same way
  earlier today); no game unit has executed since ticker-0214
  gifts at 02:14 PT, about ten hours of routine now missed.

## Own PRs first

- VPS route down (SSH Permission denied, see below), so the check
  ran through the unauthenticated public GitHub REST API for
  zachmesh/lastwar (open PR list).
- Open PRs: #711 (knowledge, Owner lastwar-knowledge-organizer),
  #708 (records 2026-11-12, Owner lastwar-pr-integrator), #425
  (tooling, Owner lastwar-tool-developer). Heads and updated_at
  unchanged since Nov 12 (#708 2026-11-12T20:44:37Z, #711
  2026-11-12T20:04:57Z, #425 2026-11-12T19:29:37Z). None is
  owned by this job; no open PR for records/2026-11-17. No
  question addressed to this job, nothing to fix.

## Sync and seeding

- Sync: reaped 0, expired 0, due 22, produced 0, already queued 22
  (mail, help, gifts, harvest, vip, passes, daily-missions,
  secrets, treasures, radar, survivors, trucks, train, training,
  donations, events, arms-race, star-ceremony, duel-score, scout,
  scout-midday); completion marker reaped: radar-2026-11-17-1003.
  Branch reconcile skipped with a warning: fetch of
  records/2026-11-17 failed (remote ref missing), issue #446.
- Zombie seeding no-op: the Zombie Invasion event ended
  2026-10-30 (unit 066 found no Zombie Invasion tab), the chain
  zombie-2026-10-28 stays closed, and no zombie-invasion unit
  sits in inbox or claimed. No fresh chain is seeded until a
  Zombie Invasion tab is seen live in the Events hub again.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 2, Base Expansion, RELEASE posture is not stated -
  theme Base Expansion, 5.8 hours left at the 12:11 read, day
  ends 18:00 PT Nov 17. UR truck dispatches score (Handbook
  100,000 each) and Legendary secret tasks score (75,000);
  survivor recruitment scores (Handbook). Radar posture: stack
  (complete tasks but do NOT claim, odd-day claim rule). The
  UR-truck window and the scoring survivor intake both stay
  missed while the game window is down.

## Delivery

- VPS SSH still Permission denied (publickey), probed 20:04Z,
  about 119.3 hours into the break (outage since about 12:46 PT
  2026-11-12; owner chose the IONOS console route 2026-11-14
  17:37 PT; no fix yet). Push and PR are blocked.
- Delivery PARTIAL: record committed locally on
  ticker-1204-1117-delivery, UNPUSHED, push pending VPS recovery.
  No PR opened for records/2026-11-17. No Slack sync. Chat
  report owed per the ticker rule (previous pass also
  access-failed); this pass's final message carries it.

## Standing git status anomaly in the live mirror (persists)

- `git status` in the live mirror still reports a large changed
  set (modified activity files, deleted inbox unit files) while
  the queue tools run against the files on disk. The live tree
  sits on branch work/ops-execution-records, another job's
  in-flight state; no commit was attempted from this tree. The
  delivery commit goes through a temporary worktree on
  ticker-1204-1117-delivery, based on ticker-1134-1117-delivery,
  as in the previous passes.
