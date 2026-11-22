---
title: Queue ticker process failure - game window missing, twenty-fourth consecutive occurrence
created: 2026-11-18T01:50:00Z
modified: 2026-11-18T01:50:00Z
version: 1.0.0
description: Queue ticker 2026-11-17 17:34 PT process failure, LastWar has no window on the Mac mini
status: process-failure
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-18T01:35Z
  - source: computer.session cc-49 and cc-50, computer.control list_windows, open_app, activate, computer.observe, connection.health, 2026-11-18T01:35Z to 01:44Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lastwar-probe-1734.json, 2026-11-18T01:45Z
  - source: tools/duel.py --json, 2026-11-18T01:38Z
  - source: GitHub connector list of open pull requests for zachmesh/lastwar, 2026-11-18T01:46Z
  - source: VPS SSH probe, 2026-11-18T01:35Z
---

# Queue ticker 2026-11-17 17:34-17:50 PT (ticker-1734) - PROCESS FAILURE

No unit was executed. This pass hit the windowless-LastWar blocker
for the twenty-fourth consecutive ticker pass. The ticker-0534
standing route change was followed: the newest queue-ticker record
(1704) was re-read BEFORE any claim, no unit was claimed, and the
device token was never taken. (One ordering note, stated plainly:
the pass's `queue.py sync` ran before the 1704 record was re-read;
sync claims nothing and touches no game state, so the route change
was not breached - but the next pass should still re-read the
newest queue-ticker record first, before sync.)

## Probe - two fresh sessions, blocker unchanged

- Mac mini ONLINE per device.list (last_seen 2026-11-18T00:03:35Z,
  UNCHANGED since the 1613 read, about 100 minutes stale at this
  pass; the gateway reconnected at 00:03:35Z, but the window did
  not come back with it). No evidence the owner has done the
  Dock-icon step: the window is still missing.
- environment.describe confirms LastWar IS in running_apps,
  alongside Google Chrome, ChatGPT and Finder. Accessibility and
  screen recording permissions are granted. Display 1920x1080.
- Session cc-49: open_app LastWar outcome_unknown (action
  781F12A3-6462-4621-BAB6-9BF23D2F064D); activate LastWar
  brought_to_front false, ax_windows_empty; list_windows (all)
  10 windows, 0 LastWar; computer.observe observation_unavailable
  ("No current target window can be observed. Select an app with
  computer.control open_app or activate, then observe again.")
  after one computer_busy retry.
- Session cc-50 (fresh session after ending cc-49): open_app
  "Last War" open_failed (no installed app matching that name,
  action 8A08080C-61C7-4755-AC70-EC720575B7D3 - the app is
  "LastWar", bundle com.lastwar.ios); list_windows again 10
  windows, 0 LastWar.
- NEW SHADE persists, fourth pass in a row - the control channel
  cannot bind ANY window, not just LastWar. Activate Chrome
  window 125 failed with geometry_mismatch (origin_delta=256+
  size_delta=256+ agent_display=false, phase=select).
  connection.health reports both transports connected and healthy
  (native lastResponse 0s, web 1s), so the gateway is fine - the
  failure is in the computer-control window-binding layer. No
  Touch ID, no password, no game input of any kind was sent.
- Probe classification: tools/mac_capture_probe.py on the
  assembled evidence returns OFF_SCREEN_WINDOW, high confidence,
  stop_pass yes (exit 10). The one missing probe step is the
  View-menu inspect (Enter/Exit Full Screen), which cannot be
  read without a bound window. The recovery stays the same owner
  step (issue #284): click the LastWar Dock icon once (or run
  tools/mac_lastwar_front.sh in Terminal), then re-probe.

## R2 accounting - twenty-fourth consecutive occurrence

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
- 20th: ticker-1534, probe only, 15:34 PT (unit claimed then
  released, no failed unit recorded).
- 21st: ticker-1613, probe only, 16:13 PT (token never taken).
- 22nd: ticker-1634, probe only, 16:34 PT (token acquired then
  released unused).
- 23rd: ticker-1704, probe only, 17:04 PT (unit claimed before
  the route change was re-read, then completed as failed;
  token acquired then released).
- 24th: this pass, 17:34 PT (probe only; route change re-read
  first, no unit claimed, token never taken).
- No game unit has executed since ticker-0214 gifts at 02:14 PT,
  about fifteen and a half hours of routine now missed.

## Own PRs first

- VPS route down (SSH Permission denied, see below), so the check
  ran through the GitHub connector (open pull requests,
  zachmesh/lastwar).
- Open PRs: #711 (knowledge, Owner lastwar-knowledge-organizer),
  #708 (records 2026-11-12, Owner lastwar-pr-integrator), #425
  (tooling, Owner lastwar-tool-developer). Heads and updated_at
  unchanged since Nov 12 (#708 2026-11-12T20:44:37Z, #711
  2026-11-12T20:04:57Z, #425 2026-11-12T19:29:37Z). None is
  owned by this job; no open PR for records/2026-11-17.
- No new comment can exist without moving updated_at, which has
  not moved since the 1704 check. No question addressed to this
  job, nothing to fix.

## Sync and seeding

- Sync: reaped 0, expired 0, due 22, produced 0, already queued 22
  (mail, help, gifts, harvest, vip, passes, daily-missions,
  secrets, treasures, radar, survivors, trucks, train, training,
  donations, events, arms-race, star-ceremony, duel-score, scout,
  scout-midday). One completion marker reaped
  (daily-missions-2026-11-16-1800, the unit the 1704 pass
  completed as failed). Branch reconcile skipped with a warning:
  fetch of records/2026-11-17 failed (remote ref missing),
  issue #446. Inbox holds 76 units; no unit was executed.
- Zombie seeding no-op: the Zombie Invasion event ended - the
  most recent done zombie unit (zombie-invasion-zombie-2026-11-10-037,
  finished 2026-11-15T02:35:26Z, status failed) found no Zombie
  Invasion tab in the Events hub and closed chain
  zombie-2026-11-10 with no successor. No fresh chain is seeded
  until a Zombie Invasion tab is seen live in the Events hub again.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 2, Base Expansion, 0.4 hours left at the 17:38 read,
  day ends 18:00 PT Nov 17. UR truck dispatches score (Handbook
  100,000 each) and Legendary secret tasks score (75,000);
  survivor recruitment scores (Handbook). Radar posture: stack
  (complete tasks but do NOT claim, odd-day claim rule). The
  UR-truck window and the scoring survivor intake both stay
  missed while the game window is down, and the day ends in
  about twenty minutes. Tonight's pre-reset sweep pair (1630 +
  1730) is staged in the pool; the 1730 sweep fires about now
  and will hit the same blocker unless the window recovers
  before then.

## Delivery

- VPS SSH still Permission denied (publickey), probed 01:35Z,
  about 125 hours into the break (outage since about 12:46 PT
  2026-11-12; owner chose the IONOS console route 2026-11-14
  17:37 PT; no fix yet). Push and PR are blocked.
- Delivery PARTIAL: record committed locally on
  ticker-1734-1117-delivery, UNPUSHED, push pending VPS recovery.
  No PR opened for records/2026-11-17. No Slack sync. Chat
  report owed per the ticker rule (previous pass also
  access-failed); this pass's final message carries it.

## Standing git status anomaly in the live mirror (persists)

- `git status` in the live mirror still reports a large changed
  set (modified activity files, deleted inbox unit files, deleted
  tools entries that exist on disk) while the queue tools run
  against the files on disk. The live tree sits on branch
  work/ops-execution-records, another job's in-flight state; no
  commit was attempted from this tree. The delivery commit goes
  through a temporary worktree on ticker-1734-1117-delivery,
  based on ticker-1704-1117-delivery, as in the previous passes.
  The live mirror's _records_/2026-11-17/ tree is untracked
  there, so the delivery branch carries only this job's ticker
  sections of the day INDEX, not the other jobs' sections.

## Owed work

- Tooling Issue for the repeated failure mode "game window lost
  in fullscreen Space, control channel blind" (class tooling) -
  filing owed at VPS recovery; gh unreachable while VPS SSH is
  down. Same owed item as ticker-0443, ticker-0534, ticker-0722,
  ticker-0804, ticker-1204, ticker-1234, ticker-1304, ticker-1334,
  ticker-1404, ticker-1434, ticker-1504, ticker-1534, ticker-1613,
  ticker-1634 and ticker-1704.
- Blocker write into a shared entry-route note (recording-rules
  Device access or queue design section 11, R2) - tier 2, cannot
  ride this tier-1 records commit; owed to the retro / the
  tooling issue above.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-1734-1117-delivery, UNPUSHED, push pending VPS recovery.
  No PR opened for records/2026-11-17.
