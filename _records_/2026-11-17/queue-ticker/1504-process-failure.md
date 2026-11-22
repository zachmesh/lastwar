---
title: Queue ticker process failure - game window missing, nineteenth consecutive occurrence
created: 2026-11-17T23:12:00Z
modified: 2026-11-17T23:12:00Z
version: 1.0.0
description: Queue ticker 2026-11-17 15:04 PT process failure, LastWar has no window on the Mac mini
status: process-failure
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-17T23:06Z
  - source: computer.session cc-40, computer.control list_windows, open_app and activate, 2026-11-17T23:06Z to 23:09Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lastwar-probe-1504.json, 2026-11-17T23:10Z
  - source: tools/duel.py --json, 2026-11-17T23:08Z
  - source: unauthenticated GitHub REST API reads of zachmesh/lastwar open PRs, 2026-11-17T23:05Z
  - source: VPS SSH probe, 2026-11-17T23:04Z
---

# Queue ticker 2026-11-17 15:04-15:13 PT (ticker-1504) - PROCESS FAILURE

No unit was claimed and no unit was executed. This pass hit the
windowless-LastWar blocker for the nineteenth consecutive ticker
pass, so under rule R2 and the ticker-0534 standing route change
(no game unit runs until the window is recovered) it is recorded
as a process failure, not as another routine failed unit. Token
held 15:06-15:13 PT, released at pass end.

## Probe - one fresh session, blocker unchanged

- Mac mini ONLINE per device.list (last_seen 2026-11-17T22:09:58Z,
  UNCHANGED since the ticker-1434 probe - now about 56 minutes
  stale at this pass's check). The stamp moved once, at 22:09:58Z,
  after the ticker-1404 pass ran connection.repair: the gateway
  reconnected then, but the window did not come back, and the
  stamp has not moved again since. No evidence the owner has
  done the Dock-icon step.
- environment.describe confirms LastWar IS in running_apps,
  alongside Google Chrome, ChatGPT and Finder. Accessibility and
  screen recording permissions are granted. Display 1920x1080.
- Session cc-40: computer.control list_windows returns 0 windows
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
  This is the nineteenth consecutive ticker occurrence of the
  window loss; no game unit has executed since ticker-0214
  gifts at 02:14 PT, about thirteen hours of routine now missed.

## R2 accounting - nineteenth consecutive occurrence

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
- 15th: ticker-1304, probe only, 13:04 PT.
- 16th: ticker-1334, probe only, 13:34 PT.
- 17th: ticker-1404, help-2026-11-17-1030, 14:04 PT (unit
  claimed and failed; ran connection.repair, which moved the
  device last_seen stamp to 22:09:58Z - the gateway
  reconnected, the window stayed missing).
- 18th: ticker-1434, passes-2026-11-17-1057, 14:34 PT (unit
  claimed and failed; confirmed the blocker after the
  last_seen move, no new recovery information).
- 19th: this pass, 15:04 PT probe, no unit claimed.
- The 1404/1434 claim-and-fail deviation added two failed units
  without recovering the window; the only new information it
  produced was that connection.repair refreshes the gateway
  stamp without restoring the window. This pass returns to the
  0804/1304/1334 probe-only pattern, which the route change
  prescribes.

## Own PRs first

- VPS route down (SSH Permission denied, see below), so the check
  ran through the unauthenticated public GitHub REST API for
  zachmesh/lastwar (open PR list, crawled 23:05Z).
- Open PRs: #711 (knowledge, Owner lastwar-knowledge-organizer),
  #708 (records 2026-11-12, Owner lastwar-pr-integrator), #425
  (tooling, Owner lastwar-tool-developer). Heads and updated_at
  unchanged since Nov 12 (#708 2026-11-12T20:44:37Z, #711
  2026-11-12T20:04:57Z, #425 2026-11-12T19:29:37Z). None is
  owned by this job; no open PR for records/2026-11-17. No
  question addressed to this job, nothing to fix.

## Sync and seeding

- Sync: reaped 0, expired 4, due 22, produced 0, already queued 22
  (mail, help, gifts, harvest, vip, passes, daily-missions,
  secrets, treasures, radar, survivors, trucks, train, training,
  donations, events, arms-race, star-ceremony, duel-score, scout,
  scout-midday); completion marker reaped: passes-2026-11-17-1057.
  Branch reconcile skipped with a warning: fetch of
  records/2026-11-17 failed (remote ref missing), issue #446.
- Zombie seeding no-op: the Zombie Invasion event ended
  2026-10-30 (unit 066 found no Zombie Invasion tab), the chain
  zombie-2026-10-28 stays closed, and no zombie-invasion unit
  sits in inbox or claimed. The last zombie unit (037, chain
  zombie-2026-11-10) failed 2026-11-15 with the Glacieradon
  event ended and no tab. No fresh chain is seeded until a
  Zombie Invasion tab is seen live in the Events hub again.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 2, Base Expansion, 2.9 hours left at the 15:08 read, day
  ends 18:00 PT Nov 17. UR truck dispatches score (Handbook
  100,000 each) and Legendary secret tasks score (75,000);
  survivor recruitment scores (Handbook). Radar posture: stack
  (complete tasks but do NOT claim, odd-day claim rule). The
  UR-truck window and the scoring survivor intake both stay
  missed while the game window is down.

## Delivery

- VPS SSH still Permission denied (publickey), probed 23:04Z,
  about 122.4 hours into the break (outage since about 12:46 PT
  2026-11-12; owner chose the IONOS console route 2026-11-14
  17:37 PT; no fix yet). Push and PR are blocked.
- Delivery PARTIAL: record committed locally on
  ticker-1504-1117-delivery, UNPUSHED, push pending VPS recovery.
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
  ticker-1504-1117-delivery, based on ticker-1434-1117-delivery,
  as in the previous passes.

## Owed work

- Tooling Issue for the repeated failure mode "game window lost
  in fullscreen Space, control channel blind" (class tooling) -
  filing owed at VPS recovery; gh unreachable while VPS SSH is
  down. Same owed item as ticker-0443, ticker-0534, ticker-0722,
  ticker-0804, ticker-1204, ticker-1234, ticker-1304, ticker-1334,
  ticker-1404 and ticker-1434.
- Blocker write into a shared entry-route note (recording-rules
  Device access or queue design section 11, R2) - tier 2, cannot
  ride this tier-1 records commit; owed to the retro / the
  tooling issue above.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-1504-1117-delivery, UNPUSHED, push pending VPS recovery.
  No PR opened for records/2026-11-17.
