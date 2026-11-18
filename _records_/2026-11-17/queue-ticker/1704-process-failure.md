---
title: Queue ticker process failure - game window missing, twenty-third consecutive occurrence
created: 2026-11-18T01:30:00Z
modified: 2026-11-18T01:30:00Z
version: 1.0.0
description: Queue ticker 2026-11-17 17:04 PT process failure, LastWar has no window on the Mac mini
status: process-failure
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-18T01:05Z
  - source: computer.session cc-47 and cc-48, computer.control list_windows, open_app, activate, computer.observe, screen.snap, connection.health, 2026-11-18T01:05Z to 01:20Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lastwar-probe-1704.json, 2026-11-18T01:26Z
  - source: tools/duel.py --json, 2026-11-18T01:20Z
  - source: GitHub connector list of open pull requests for zachmesh/lastwar, 2026-11-18T01:27Z
  - source: VPS SSH probe, 2026-11-18T01:05Z
---

# Queue ticker 2026-11-17 17:04-17:28 PT (ticker-1704) - PROCESS FAILURE

No unit was executed. This pass hit the windowless-LastWar blocker
for the twenty-third consecutive ticker pass. One deviation from the
ticker-0534 standing route change to state plainly: this pass claimed
daily-missions-2026-11-16-1800 and took the device token BEFORE
reading the ticker-1634 record and its route change (no game unit
runs until the window is recovered). The claim is unwound honestly
below - the unit is completed as failed, the tracker is untouched,
the token is released - and the next pass must re-read the latest
queue-ticker record BEFORE claiming anything.

## Probe - two fresh sessions, blocker unchanged

- Mac mini ONLINE per device.list (last_seen 2026-11-18T00:03:35Z,
  UNCHANGED since the 1613 read about 85 minutes earlier; the
  gateway reconnected at 00:03:35Z, but the window did not come
  back with it). No evidence the owner has done the Dock-icon step:
  the window is still missing.
- environment.describe confirms LastWar IS in running_apps,
  alongside Google Chrome, ChatGPT and Finder. Accessibility and
  screen recording permissions are granted. Display 1920x1080.
- Session cc-47: open_app LastWar outcome_unknown (action
  51595AD5-07C8-4109-AC7C-8476368812C9 for "Last War",
  D8297879-3DD7-4A51-8153-767B69AABD8E for "LastWar"); activate
  LastWar brought_to_front false, ax_windows_empty; list_windows
  (all) 10 windows, 0 LastWar; computer.observe
  observation_unavailable ("No current target window can be
  observed. Select an app with computer.control open_app or
  activate, then observe again."); screen.snap the same
  observation_unavailable.
- Session cc-48 (fresh session after ending cc-47): open_app
  LastWar outcome_unknown again (action
  4B7318AE-CEF4-421E-BC85-C3829F796F77); observe still
  observation_unavailable after a 25 second wait and a fresh
  list_windows (still 10 windows, 0 LastWar).
- NEW SHADE persists, third pass in a row - the control channel
  cannot bind ANY window, not just LastWar. activate Finder
  window 28 and activate Chrome window 125 both failed with
  geometry_mismatch (origin_delta=256+ size_delta=256+
  agent_display=false, phase=select). connection.health reports
  both transports connected and healthy (native lastResponse 0s,
  web 5s), so the gateway is fine - the failure is in the
  computer-control window-binding layer. No Touch ID, no
  password, no game input of any kind was sent.
- Probe classification: tools/mac_capture_probe.py on the
  assembled evidence returns OFF_SCREEN_WINDOW, high confidence,
  stop_pass yes (exit 10). The one missing probe step is the
  View-menu inspect (Enter/Exit Full Screen), which cannot be
  read without a bound window. The recovery stays the same owner
  step (issue #284): click the LastWar Dock icon once (or run
  tools/mac_lastwar_front.sh in Terminal), then re-probe.

## The claimed unit - unwound

- daily-missions-2026-11-16-1800 was claimed at 17:10 PT
  (attempts 1 to 2, lease to 17:30 PT) before the route change
  was re-read. It is completed as failed with the blocker
  recorded (stats: target claim completed daily missions and
  activity chests, achieved no game access, window missing,
  verified yes, blocker_category f), evidence this record. The
  tracker is untouched for failed units, and the completion
  marker suppresses re-picks of this unit. The device token was
  acquired at 17:05 PT and released at 17:20 PT.
- Lesson for the next pass, written down so it is not repeated:
  read the newest queue-ticker record in
  _records_/2026-11-17/queue-ticker/ (or the day INDEX tail)
  BEFORE sync/claim, not after. The 1634 record and the day
  INDEX both carried the route change in plain text.

## R2 accounting - twenty-third consecutive occurrence

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
- 23rd: this pass, 17:04 PT (unit claimed before the route
  change was re-read, then completed as failed; token acquired
  then released).
- No game unit has executed since ticker-0214 gifts at 02:14 PT,
  about fifteen hours of routine now missed.

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
  not moved since the 1613 check. No question addressed to this
  job, nothing to fix.

## Sync and seeding

- Sync: reaped 0, expired 0, due 22, produced 0, already queued 21
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

- Duel day 2, Base Expansion, 0.7 hours left at the 17:20 read,
  day ends 18:00 PT Nov 17. UR truck dispatches score (Handbook
  100,000 each) and Legendary secret tasks score (75,000);
  survivor recruitment scores (Handbook). Radar posture: stack
  (complete tasks but do NOT claim, odd-day claim rule). The
  UR-truck window and the scoring survivor intake both stay
  missed while the game window is down, and the day ends in
  about forty minutes. Tonight's pre-reset sweep pair (1630 +
  1730) is staged in the pool; the 1730 sweep fires in minutes
  and will hit the same blocker unless the window recovers
  before then.

## Delivery

- VPS SSH still Permission denied (publickey), probed 01:05Z,
  about 124 hours into the break (outage since about 12:46 PT
  2026-11-12; owner chose the IONOS console route 2026-11-14
  17:37 PT; no fix yet). Push and PR are blocked.
- Delivery PARTIAL: record committed locally on
  ticker-1704-1117-delivery, UNPUSHED, push pending VPS recovery.
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
  through a temporary worktree on ticker-1704-1117-delivery,
  based on ticker-1634-1117-delivery, as in the previous passes.
  The live mirror's _records_/2026-11-17/ tree is untracked
  there, so the delivery branch carries only this job's ticker
  sections of the day INDEX, not the other jobs' sections.

## Owed work

- Tooling Issue for the repeated failure mode "game window lost
  in fullscreen Space, control channel blind" (class tooling) -
  filing owed at VPS recovery; gh unreachable while VPS SSH is
  down. Same owed item as ticker-0443, ticker-0534, ticker-0722,
  ticker-0804, ticker-1204, ticker-1234, ticker-1304, ticker-1334,
  ticker-1404, ticker-1434, ticker-1504, ticker-1534, ticker-1613
  and ticker-1634.
- Blocker write into a shared entry-route note (recording-rules
  Device access or queue design section 11, R2) - tier 2, cannot
  ride this tier-1 records commit; owed to the retro / the
  tooling issue above.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-1704-1117-delivery, UNPUSHED, push pending VPS recovery.
  No PR opened for records/2026-11-17.
