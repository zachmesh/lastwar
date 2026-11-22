---
title: Queue ticker process failure - game window missing, fifteenth consecutive occurrence
created: 2026-11-17T21:22:00Z
modified: 2026-11-17T21:22:00Z
version: 1.0.0
description: Queue ticker 2026-11-17 13:04 PT process failure, LastWar has no window on the Mac mini
status: process-failure
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-17T21:06Z
  - source: computer.session cc-34, computer.control list_windows, open_app and activate, 2026-11-17T21:06Z to 21:13Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lastwar-probe-1304.json, 2026-11-17T21:18Z
  - source: tools/duel.py --json, 2026-11-17T21:10Z
  - source: unauthenticated GitHub REST API reads of zachmesh/lastwar open PRs, 2026-11-17T21:05Z
  - source: VPS SSH probe, 2026-11-17T21:05Z
---

# Queue ticker 2026-11-17 13:04-13:22 PT (ticker-1304) - PROCESS FAILURE

No unit was claimed and no unit was executed. This pass hit the
windowless-LastWar blocker for the fifteenth consecutive ticker
pass, so under rule R2 and the ticker-0534 standing route change
(no game unit runs until the window is recovered) it is recorded
as a process failure, not as another routine failed unit. Token
held 13:04-13:21 PT, released at pass end.

## Probe - one fresh session, blocker unchanged

- Mac mini ONLINE per device.list (last_seen 2026-11-17T20:02:14Z,
  UNCHANGED since the ticker-1204 probe - now about 76 minutes
  stale at this pass's check, the same stamp ticker-1234 read
  at 20:04Z). The stamp has not moved since 20:02Z; no evidence
  the owner has done the Dock-icon step.
- environment.describe confirms LastWar IS in running_apps,
  alongside Google Chrome, ChatGPT and Finder. Accessibility and
  screen recording permissions are granted. Display 1920x1080.
- Session cc-34: computer.control list_windows returns 0 windows
  for LastWar (target_bundle_id com.lastwar.ios), twice (before
  and after the relaunch attempt). open_app LastWar returns
  outcome_unknown. activate LastWar returns brought_to_front
  false, ax_windows_empty. Three attempts, per the standing rule.
  No Touch ID, no password, no game input of any kind was sent.
- Probe classification: tools/mac_capture_probe.py on the
  assembled evidence returns OFF_SCREEN_WINDOW, high confidence,
  stop_pass yes (exit 10). The documented recovery is the same
  owner step as issue #284 - click the LastWar Dock icon once
  (or run tools/mac_lastwar_front.sh in Terminal) - then
  re-probe. No background control route unblocks a windowless
  app: open_app returns outcome_unknown, activate needs a
  window, set_window_frame needs an observation.
- No game unit was executed, nothing claimed, nothing spent.
  The tracker is untouched. The pass stopped after the probe
  rather than claiming a unit to fail identically - the blocker
  is systemic and every further unit would fail the same way.
  This is the fifteenth consecutive ticker occurrence of the
  window loss; no game unit has executed since ticker-0214
  gifts at 02:14 PT, about eleven hours of routine now missed.

## R2 accounting - fifteenth consecutive occurrence

- 1st: ticker-0333, harvest-2026-11-17-0203, 03:33 PT (green zoom
  click moved the window to a native fullscreen Space).
- 2nd: ticker-0443, radar-2026-11-17-0203, 04:43 PT.
- 3rd: ticker-0534, help-2026-11-17-0230, 06:06 PT (standing
  route change: NO game unit runs until the window is
  recovered).
- 4th: ticker-0722, probe only, 07:22 PT.
- 5th: ticker-0804, probe only, 08:04 PT.
- 6th-12th: ticker-0834, 0904, 0934, 1004, 1034, 1104, 1134.
- 13th: ticker-1204, survivors-2026-11-17-1003, 12:04 PT
  (unit claimed and failed).
- 14th: ticker-1234, donations-2026-11-17-1003, 12:38 PT
  (unit claimed and failed).
- 15th: this pass, 13:04 PT probe, no unit claimed.
- The 1234 pass's choice to claim a unit added a fourteenth
  failed unit without new information; this pass returns to
  the 0804 probe-only pattern, which the route change prescribes.

## Own PRs first

- VPS route down (SSH Permission denied, see below), so the check
  ran through the unauthenticated public GitHub REST API for
  zachmesh/lastwar (open PR list), 21:05Z.
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
  scout-midday); completion marker reaped: donations-2026-11-17-1003.
  Branch reconcile skipped with a warning: fetch of
  records/2026-11-17 failed (remote ref missing), issue #446.
- Zombie seeding no-op: the Zombie Invasion event ended
  2026-10-30 (unit 066 found no Zombie Invasion tab), the chain
  zombie-2026-10-28 stays closed, and no zombie-invasion unit
  sits in inbox or claimed. No fresh chain is seeded until a
  Zombie Invasion tab is seen live in the Events hub again.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 2, Base Expansion, 4.8 hours left at the 13:10 read, day
  ends 18:00 PT Nov 17. UR truck dispatches score (Handbook
  100,000 each) and Legendary secret tasks score (75,000);
  survivor recruitment scores (Handbook). Radar posture: stack
  (complete tasks but do NOT claim, odd-day claim rule). The
  UR-truck window and the scoring survivor intake both stay
  missed while the game window is down.

## Delivery

- VPS SSH still Permission denied (publickey), probed 21:05Z,
  about 120.3 hours into the break (outage since about 12:46 PT
  2026-11-12; owner chose the IONOS console route 2026-11-14
  17:37 PT; no fix yet). Push and PR are blocked.
- Delivery PARTIAL: record committed locally on
  ticker-1304-1117-delivery, UNPUSHED, push pending VPS recovery.
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
  ticker-1304-1117-delivery, based on ticker-1234-1117-delivery,
  as in the previous passes.

## Owed work

- Tooling Issue for the repeated failure mode "game window lost
  in fullscreen Space, control channel blind" (class tooling) -
  filing owed at VPS recovery; gh unreachable while VPS SSH is
  down. Same owed item as ticker-0443, ticker-0534, ticker-0722,
  ticker-0804, ticker-1204 and ticker-1234.
- Blocker write into a shared entry-route note (recording-rules
  Device access or queue design section 11, R2) - tier 2, cannot
  ride this tier-1 records commit; owed to the retro / the
  tooling issue above.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-1304-1117-delivery, UNPUSHED, push pending VPS
  recovery. No PR opened for records/2026-11-17.
