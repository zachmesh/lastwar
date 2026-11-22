---
title: Queue ticker process failure - game window missing, twentieth consecutive occurrence
created: 2026-11-17T23:54:00Z
modified: 2026-11-17T23:54:00Z
version: 1.0.0
description: Queue ticker 2026-11-17 15:34 PT process failure, LastWar has no window on the Mac mini
status: process-failure
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-17T23:35Z
  - source: computer.session cc-41, cc-42, cc-43, computer.control list_windows, list_apps, open_app, activate, screen.snap, 2026-11-17T23:36Z to 23:49Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lastwar-probe-1534.json, 2026-11-17T23:51Z
  - source: tools/duel.py --json, 2026-11-17T23:49Z
  - source: GitHub connector list_pull_requests for zachmesh/lastwar, 2026-11-17T23:36Z
  - source: VPS SSH probe, 2026-11-17T23:34Z
---

# Queue ticker 2026-11-17 15:34-15:55 PT (ticker-1534) - PROCESS FAILURE

No unit was executed. This pass hit the windowless-LastWar blocker
for the twentieth consecutive ticker pass, so under rule R2 and the
ticker-0534 standing route change (no game unit runs until the
window is recovered) it is recorded as a process failure, not as
another routine failed unit. Token held 15:37-15:55 PT, released
at pass end.

## Probe - three fresh sessions, blocker unchanged

- Mac mini ONLINE per device.list (last_seen 2026-11-17T22:09:58Z,
  UNCHANGED since the ticker-1434 probe - now about 100 minutes
  stale at this pass's check). The stamp moved once, at 22:09:58Z,
  after the ticker-1404 pass ran connection.repair: the gateway
  reconnected then, but the window did not come back, and the
  stamp has not moved again since. No evidence the owner has
  done the Dock-icon step.
- environment.describe confirms LastWar IS in running_apps,
  alongside Google Chrome, ChatGPT and Finder. Accessibility and
  screen recording permissions are granted. Display 1920x1080.
- Session cc-41: open_app LastWar twice, outcome_unknown both
  times; activate LastWar brought_to_front false,
  ax_windows_empty; list_windows 0 LastWar windows; screen.snap
  observation_unavailable. Session cc-42: open_app again
  outcome_unknown, observe still unavailable. Session cc-43:
  activate Finder fails with geometry_mismatch and
  agent_display=false while target_bundle_id stays
  com.lastwar.ios; frontmost_app reports the assistant itself;
  current_target binds LastWar pid 11266, mode background,
  has_target true - yet list_apps (twice, 30 seconds apart)
  lists 7 apps with NO LastWar entry at all, and describe
  LastWar is observation_unavailable. A Ctrl+Right Space-switch
  key is refused (observation_required, no window bound), so no
  input of any kind could be sent. The process is alive but
  presents no window to the window server. No Touch ID, no
  password, no game input of any kind was sent.
- Probe classification: tools/mac_capture_probe.py on the
  assembled evidence returns OFF_SCREEN_WINDOW, high confidence,
  stop_pass yes (exit 10). The documented recovery is the same
  owner step as issue #284 - click the LastWar Dock icon once
  (or run tools/mac_lastwar_front.sh in Terminal) - then
  re-probe. No background control route unblocks a windowless
  app: open_app returns outcome_unknown, activate needs a
  window, set_window_frame needs an observation, Space keys do
  not switch Spaces in the background.
- Claim-and-release note: this pass claimed
  daily-missions-2026-11-16-1800 at 15:37 PT (token-acquire then
  next returned it) BEFORE the 1504 record and the ticker-0534
  route change were read at about 15:48 PT. Once the standing
  route was found, the unit was released back to inbox with
  tools/queue.py release (not completed as failed), so no failed
  unit was recorded and the tracker is untouched - the probe-only
  pattern the 1504 pass restored is preserved. The claim itself
  is the deviation to avoid next time: read the latest
  queue-ticker record before claiming when the window is known
  down.

## R2 accounting - twentieth consecutive occurrence

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
- 19th: ticker-1504, probe only, 15:04 PT (returned to the
  probe-only pattern).
- 20th: this pass, 15:34 PT probe, unit claimed then released,
  no failed unit recorded.
- No game unit has executed since ticker-0214 gifts at 02:14 PT,
  about thirteen and a half hours of routine now missed.

## Own PRs first

- VPS route down (SSH Permission denied, see below), so the check
  ran through the authenticated GitHub connector
  (list_pull_requests, zachmesh/lastwar, open).
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
  scout-midday). Branch reconcile skipped with a warning: fetch
  of records/2026-11-17 failed (remote ref missing), issue #446.
  Inbox holds 72 units; no unit was executed.
- Zombie seeding no-op: the Zombie Invasion event ended
  2026-10-30 (unit 066 found no Zombie Invasion tab), the chain
  zombie-2026-10-28 stays closed, and no zombie-invasion unit
  sits in inbox or claimed. No fresh chain is seeded until a
  Zombie Invasion tab is seen live in the Events hub again.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 2, Base Expansion, 2.2 hours left at the 15:49 read,
  day ends 18:00 PT Nov 17. UR truck dispatches score (Handbook
  100,000 each) and Legendary secret tasks score (75,000);
  survivor recruitment scores (Handbook). Radar posture: stack
  (complete tasks but do NOT claim, odd-day claim rule). The
  UR-truck window and the scoring survivor intake both stay
  missed while the game window is down.

## Delivery

- VPS SSH still Permission denied (publickey), probed 23:34Z,
  about 122.8 hours into the break (outage since about 12:46 PT
  2026-11-12; owner chose the IONOS console route 2026-11-14
  17:37 PT; no fix yet). Push and PR are blocked.
- Delivery PARTIAL: record committed locally on
  ticker-1534-1117-delivery, UNPUSHED, push pending VPS recovery.
  No PR opened for records/2026-11-17. No Slack sync. Chat
  report owed per the ticker rule (previous pass also
  access-failed); this pass's final message carries it.

## Standing git status anomaly in the live mirror (persists)

- `git status` in the live mirror still reports a large changed
  set (modified activity files, deleted inbox unit files, deleted
  tools/*.py entries that exist on disk) while the queue tools
  run against the files on disk. The live tree sits on branch
  work/ops-execution-records, another job's in-flight state; no
  commit was attempted from this tree. The delivery commit goes
  through a temporary worktree on ticker-1534-1117-delivery,
  based on ticker-1504-1117-delivery, as in the previous passes.

## Owed work

- Tooling Issue for the repeated failure mode "game window lost
  in fullscreen Space, control channel blind" (class tooling) -
  filing owed at VPS recovery; gh unreachable while VPS SSH is
  down. Same owed item as ticker-0443, ticker-0534, ticker-0722,
  ticker-0804, ticker-1204, ticker-1234, ticker-1304, ticker-1334,
  ticker-1404, ticker-1434 and ticker-1504.
- Blocker write into a shared entry-route note (recording-rules
  Device access or queue design section 11, R2) - tier 2, cannot
  ride this tier-1 records commit; owed to the retro / the
  tooling issue above.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-1534-1117-delivery, UNPUSHED, push pending VPS recovery.
  No PR opened for records/2026-11-17.
