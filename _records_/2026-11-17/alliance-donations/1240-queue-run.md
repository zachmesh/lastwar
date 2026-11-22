---
title: Donations 2026-11-17 ticker-1234 failed, LastWar window missing
created: 2026-11-17T20:44:00Z
modified: 2026-11-17T20:44:00Z
version: 1.0.0
description: Donations unit donations-2026-11-17-1003 failed, LastWar has no window on the Mac mini
status: failed
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-17T20:37Z
  - source: computer.session cc-33, computer.control list_windows, open_app and activate, 2026-11-17T20:39Z to 20:43Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lastwar-probe-1234.json, 2026-11-17T20:43Z
  - source: tools/duel.py --json, 2026-11-17T20:39Z
  - source: unauthenticated GitHub REST API reads of zachmesh/lastwar open PRs, 2026-11-17T20:37Z
  - source: VPS SSH probe, 2026-11-17T20:35Z
---

# Donations 2026-11-17 ticker-1234 failed, LastWar window missing

- Executor: ticker-1234
- Unit: donations-2026-11-17-1003, regular donations, activity alliance-donations, priority 2, est 7 minutes
- Session window: 12:38-12:44 local, token held 12:38-12:44 local

## What happened

- The Mac mini (Zhen's Mac mini, 1c817413-83e2-0545-cb90-36d5e096a6bd)
  reports online in device.list, but its last_seen is UNCHANGED at
  2026-11-17T20:02:14Z - now about 41 minutes stale at the time of
  this pass's check, the same stamp the ticker-1204 pass read at
  20:04Z. The stamp moved once between the 1134 close and the 1204
  probe and has not moved since; the 1204 pass ran after the move
  and still found no window, so the move is NOT evidence the
  window was recovered.
- The game window is still gone. `list_windows` with app LastWar
  returns 0 windows, twice (before and after the relaunch attempt),
  across 12:39-12:43 PT. The app process is bound
  (target_bundle_id com.lastwar.ios) but windowless - the same
  worsened form first seen in the 1204 pass, a step beyond the
  issue #284 off-screen window (there the window existed on an
  inactive Space); here there is no window at all to bring forward.
- Recovery attempts, all inside session cc-33 (3 attempts, per the
  standing rule):
  list_windows (0 windows); open_app LastWar (outcome_unknown,
  no window after the check that followed); activate LastWar
  (brought_to_front false, ax_windows_empty). No Touch ID, no
  password, no game input of any kind was sent.
- Probe classification: tools/mac_capture_probe.py on the
  assembled evidence returns OFF_SCREEN_WINDOW, high confidence,
  stop_pass yes (exit 10). The documented recovery is the same
  owner step as issue #284 - click the LastWar Dock icon once
  (or run tools/mac_lastwar_front.sh in Terminal) - then
  re-probe. No background control route unblocks a windowless
  app: open_app returns outcome_unknown, activate needs a
  window, set_window_frame needs an observation.
- No donation work was executed, nothing claimed, nothing spent.
  The tracker is untouched. The pass stopped after this unit
  rather than cascading failed units - the blocker is systemic
  and every further unit would fail identically. This is the
  fourteenth consecutive ticker occurrence of the window loss
  (ticker-1204 survivors failed the same way about 30 minutes
  earlier); no game unit has executed since ticker-0214 gifts
  at 02:14 PT, about ten and a half hours of routine now missed.

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
  scout-midday); completion marker reaped: survivors-2026-11-17-1003.
  Branch reconcile skipped with a warning: fetch of
  records/2026-11-17 failed (remote ref missing), issue #446.
- Zombie seeding no-op: the Zombie Invasion event ended
  2026-10-30 (unit 066 found no Zombie Invasion tab), the chain
  zombie-2026-10-28 stays closed, and no zombie-invasion unit
  sits in inbox or claimed. No fresh chain is seeded until a
  Zombie Invasion tab is seen live in the Events hub again.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 2, Base Expansion, 5.3 hours left at the 12:39 read, day
  ends 18:00 PT Nov 17. UR truck dispatches score (Handbook
  100,000 each) and Legendary secret tasks score (75,000);
  survivor recruitment scores (Handbook). Radar posture: stack
  (complete tasks but do NOT claim, odd-day claim rule). The
  UR-truck window and the scoring survivor intake both stay
  missed while the game window is down.

## Delivery

- VPS SSH still Permission denied (publickey), probed 20:35Z,
  about 119.8 hours into the break (outage since about 12:46 PT
  2026-11-12; owner chose the IONOS console route 2026-11-14
  17:37 PT; no fix yet). Push and PR are blocked.
- Delivery PARTIAL: record committed locally on
  ticker-1234-1117-delivery, UNPUSHED, push pending VPS recovery.
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
  ticker-1234-1117-delivery, based on ticker-1204-1117-delivery,
  as in the previous passes.
