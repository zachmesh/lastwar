---
title: Queue ticker process failure - game window missing, twenty-second consecutive occurrence
created: 2026-11-18T00:45:00Z
modified: 2026-11-18T00:45:00Z
version: 1.0.0
description: Queue ticker 2026-11-17 16:34 PT process failure, LastWar has no window on the Mac mini
status: process-failure
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-18T00:35Z
  - source: computer.session cc-46, computer.control list_windows, list_apps, open_app, activate, computer.observe, screen.snap, 2026-11-18T00:35Z to 00:40Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lastwar-probe-1634.json, 2026-11-18T00:40Z
  - source: tools/duel.py --json, 2026-11-18T00:39Z
  - source: GitHub connector list of open pull requests for zachmesh/lastwar, 2026-11-18T00:35Z
  - source: VPS SSH probe, 2026-11-18T00:34Z
---

# Queue ticker 2026-11-17 16:34-16:45 PT (ticker-1634) - PROCESS FAILURE

No unit was executed. This pass hit the windowless-LastWar blocker
for the twenty-second consecutive ticker pass, so under rule R2 and the
ticker-0534 standing route change (no game unit runs until the
window is recovered) it is recorded as a process failure, not as
another routine failed unit. Probe-only pattern preserved: the
ticker-1613 record and its route change were read BEFORE any unit
was claimed, so no unit was claimed, the tracker was untouched, and
no failed unit was recorded. One deviation from the 1613 pattern to
state plainly: the device token WAS acquired at the start of this
pass (ticker-1634, before the 1613 record was read) and was released
unused at the end of the pass - no unit ran under it.

## Probe - one fresh session, blocker unchanged

- Mac mini ONLINE per device.list (last_seen 2026-11-18T00:03:35Z,
  UNCHANGED since the 1613 read about 40 minutes earlier). The
  gateway reconnected at 00:03:35Z, but the window did not come
  back with it. No evidence the owner has done the Dock-icon step:
  the window is still missing.
- environment.describe confirms LastWar IS in running_apps,
  alongside Google Chrome (two instances), ChatGPT and Finder.
  Accessibility and screen recording permissions are granted.
  Display 1920x1080.
- Session cc-46: open_app LastWar outcome_unknown (action
  5FF7F611-64EA-4EB4-8C8B-5A53BEF19886); list_windows (all) 10
  windows, 0 LastWar; activate LastWar brought_to_front false,
  ax_windows_empty; list_apps 7 apps with NO LastWar entry at
  all; computer.observe observation_unavailable ("No current
  target window can be observed. Select an app with
  computer.control open_app or activate, then observe again.");
  screen.snap the same observation_unavailable. No Touch ID, no
  password, no game input of any kind was sent.
- NEW SHADE persists, second pass in a row - the control channel
  cannot bind ANY window, not just LastWar. activate Chrome
  window 125 failed with geometry_mismatch
  (origin_delta=256+ size_delta=256+ agent_display=false,
  phase=select), observe and screen.snap after that still
  observation_unavailable. In the 1534 pass Chrome windows
  observed normally in the same sessions; in 1613 and now in
  1634 the channel's window binding itself is blind.
  list_windows still returns window lists and
  environment.describe still responds, so the channel answers -
  only selection/observation fails. The recovery stays the same
  owner step (issue #284): click the LastWar Dock icon once
  (or run tools/mac_lastwar_front.sh in Terminal), then
  re-probe.
- Probe classification: tools/mac_capture_probe.py on the
  assembled evidence returns OFF_SCREEN_WINDOW, high confidence,
  stop_pass yes (exit 10). The one missing probe step is the
  View-menu inspect (Enter/Exit Full Screen), which cannot be
  read without a bound window. The observe attempt the
  classifier lists as missing was in fact made once this pass
  (computer.observe mode current, observation_unavailable with
  the exact message quoted above); the classifier's list
  reflects the evidence keys supplied, not an unattempted step.

## R2 accounting - twenty-second consecutive occurrence

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
- 22nd: this pass, 16:34 PT probe, no unit claimed, token
  acquired then released unused.
- No game unit has executed since ticker-0214 gifts at 02:14 PT,
  about fourteen and a half hours of routine now missed.

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
- Newest comments checked: #711 carries one comment from
  zachmesh (2026-11-12T19:55:59Z) addressed to the integrator
  and the next knowledge-organizer run about PR #710 merging
  after #711 opened - not addressed to this job. #708 has no
  comments. No question addressed to this job, nothing to fix.
  No new comment can exist without moving updated_at, which
  has not moved since the 1613 check.

## Sync and seeding

- Sync: reaped 0, expired 0, due 22, produced 0, already queued 22
  (mail, help, gifts, harvest, vip, passes, daily-missions,
  secrets, treasures, radar, survivors, trucks, train, training,
  donations, events, arms-race, star-ceremony, duel-score, scout,
  scout-midday). Branch reconcile skipped with a warning: fetch
  of records/2026-11-17 failed (remote ref missing), issue #446.
  Inbox holds 77 units; no unit was executed.
- Zombie seeding no-op: the Zombie Invasion event ended - the
  most recent done zombie unit (zombie-invasion-zombie-2026-11-10-037,
  finished 2026-11-15T02:35:26Z, status failed) found no Zombie
  Invasion tab in the Events hub and closed chain
  zombie-2026-11-10 with no successor. No fresh chain is seeded
  until a Zombie Invasion tab is seen live in the Events hub again.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 2, Base Expansion, 1.3 hours left at the 16:39 read,
  day ends 18:00 PT Nov 17. UR truck dispatches score (Handbook
  100,000 each) and Legendary secret tasks score (75,000);
  survivor recruitment scores (Handbook). Radar posture: stack
  (complete tasks but do NOT claim, odd-day claim rule). The
  UR-truck window and the scoring survivor intake both stay
  missed while the game window is down, and the day ends in
  about an hour and twenty minutes. Tonight's pre-reset sweep
  pair (1630 + 1730) is staged in the pool but cannot execute
  unless the window recovers before 17:30.

## Delivery

- VPS SSH still Permission denied (publickey), probed 00:34Z,
  about 123.5 hours into the break (outage since about 12:46 PT
  2026-11-12; owner chose the IONOS console route 2026-11-14
  17:37 PT; no fix yet). Push and PR are blocked.
- Delivery PARTIAL: record committed locally on
  ticker-1634-1117-delivery, UNPUSHED, push pending VPS recovery.
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
  through a temporary worktree on ticker-1634-1117-delivery,
  based on ticker-1613-1117-delivery, as in the previous passes.
  The live mirror's _records_/2026-11-17/ tree is untracked
  there, so the delivery branch carries only this job's ticker
  sections of the day INDEX, not the other jobs' sections.

## Owed work

- Tooling Issue for the repeated failure mode "game window lost
  in fullscreen Space, control channel blind" (class tooling) -
  filing owed at VPS recovery; gh unreachable while VPS SSH is
  down. Same owed item as ticker-0443, ticker-0534, ticker-0722,
  ticker-0804, ticker-1204, ticker-1234, ticker-1304, ticker-1334,
  ticker-1404, ticker-1434, ticker-1504, ticker-1534 and
  ticker-1613.
- Blocker write into a shared entry-route note (recording-rules
  Device access or queue design section 11, R2) - tier 2, cannot
  ride this tier-1 records commit; owed to the retro / the
  tooling issue above.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-1634-1117-delivery, UNPUSHED, push pending VPS recovery.
  No PR opened for records/2026-11-17.
