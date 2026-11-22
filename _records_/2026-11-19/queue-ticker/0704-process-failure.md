---
title: Queue ticker process failure - game window missing, sixty-third consecutive occurrence
created: 2026-11-19T15:28:00Z
modified: 2026-11-19T15:28:00Z
version: 1.0.0
description: Queue ticker 2026-11-19 07:04 PT process failure, LastWar has no window on the Mac mini
status: process-failure
grounded_in:
  - source: _records_/2026-11-19/queue-ticker/0534-process-failure.md re-read BEFORE the probe and before any claim or token (route partially honored - see below)
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-19T15:19Z
  - source: connection.health and environment.describe on the same device, 2026-11-19T15:19Z
  - source: computer sessions cc-128, cc-129 and cc-130, computer.control list_windows, activate and open_app, computer.observe, 2026-11-19T15:20Z to 15:25Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-0704.json, 2026-11-19T15:25Z
  - source: tools/duel.py --json, 2026-11-19T15:25Z
  - source: tools/queue.py sync and stats, 2026-11-19T15:17Z
  - source: GitHub connector list_pull_requests on zachmesh/lastwar, 2026-11-19T15:19Z
  - source: VPS SSH probe, 2026-11-19T15:26Z
---

# Queue ticker 2026-11-19 07:04 to about 07:30 PT (ticker-0704) - PROCESS FAILURE

No unit claimed, no token taken, no game input executed. The
pass hit the windowless-LastWar blocker for the sixty-third
consecutive ticker pass, by the running count in the records
(ticker-0534 at 05:34 PT Nov 19 was the sixty-second; no ticker
record exists for the 06:04 slot on Nov 19, so the count
advances by this pass alone). No batch point passed during
this run window, so missed batches stay 40; the 07:00 point
passed during the queue-planning 0640 run's window and awaits
the integrator's 07:00-batch pass.

## Route - partially honored, material protection held

The newest queue-ticker record (0534) was read BEFORE the
probe and before any claim or token - so no unit was spent
on a known blocker, which is what the route change exists
to prevent. But it was NOT read first: sync and stats ran
before the read, the same ordering slip as the 0534 pass's
first half. The sync cost nothing (reaped 0, expired 0,
produced 0), and the material part of the route - probe
before any claim, no token before the probe - held in full:
this pass claimed nothing, took no token, and has nothing
to release. The deviation-watch therefore does NOT advance:
it stays at ONE honoring pass (0434, the first, which read
the record before sync). The next pass must keep the full
honoring order - newest queue-ticker record first, then
sync, then probe before any claim.

## Probe - three computer sessions, blocker unchanged

- Mac mini ONLINE per device.list, last_seen
  2026-11-19T12:25:42Z - UNCHANGED since the 0434 probe:
  the channel has not progressed since about 12:25Z.
  connection.health WAS called this pass (closing the 0534
  gap): both transports healthy, lastResponseAgeSeconds 0
  (native) and 3 (web), progressAgeSeconds 10567 on both -
  about 2.9 hours frozen, matching the stale last_seen.
  Fresh responses on a channel whose progress has not
  advanced since 12:25Z.
- environment.describe confirms LastWar IS in running_apps
  (com.lastwar.ios), alongside Google Chrome, ChatGPT and
  Finder. Accessibility and screen recording permissions are
  granted. Display 1920x1080. `agent_window.available` is
  false with reason `new_tab_in_existing_window`.
- Session cc-128: list_windows with app LastWar returned 0
  windows; activate "LastWar" failed ax_windows_empty with
  brought_to_front false; open_app "LastWar"
  outcome_unknown; observe and screen observation both
  observation_unavailable; list_windows (all) returned 11
  windows with no LastWar entry; activate "Google Chrome"
  failed geometry_mismatch (origin_delta=256+,
  size_delta=256+, agent_display=false).
- Session cc-129 (fresh session, reopened per the retry
  rule): list_windows LastWar again 0; activate again
  ax_windows_empty; open_app again outcome_unknown; observe
  again observation_unavailable; activate "Finder" failed
  geometry_mismatch - the same failure 0534 measured for
  Chrome windows, so the "no window selectable on the agent
  display" widening now covers Finder as well as Chrome and
  LastWar.
- Session cc-130 (third attempt, per the retry rule):
  list_windows LastWar 0; activate ax_windows_empty,
  brought_to_front false. Identical failure, third time.
- 26 device invokes in total, all answered promptly, 0
  timeouts, 0 node_offline. (The evidence file records
  invoke_responses 21, carried from the 0534 estimate - the
  actual count this pass is 26; the classification does not
  depend on it.)
- Probe classification: tools/mac_capture_probe.py v1.2.0 on
  the assembled evidence (/tmp/lw-probe-0704.json) returns
  OFF_SCREEN_WINDOW, high confidence, stop_pass yes (exit
  10). Same label as 0534 and the passes before it. One
  missing probe step: the View-menu inspect, not runnable
  without a selected window.
- The recovery stays the same owner step (issue #284): click
  the LastWar Dock icon once (or run
  tools/mac_lastwar_front.sh in Terminal), then re-probe.
- No game input was sent in this pass. No Escape, Return or
  Control-Command-F was used; the green zoom button stays
  untouched per the standing lesson. No Touch ID, no password.

## Own PRs first

- VPS route down (SSH Permission denied, see below), so no gh
  check was possible this pass. The open PR list was re-read
  via the GitHub connector (list_pull_requests,
  2026-11-19T15:19Z): exactly three open PRs - #711
  (knowledge: fold ticker-1047 pass into 4 profiles, opened
  Nov 12), #708 (records: 2026-11-12, opened Nov 12), #425
  (feat(tools): pre-delivery log gate, opened Nov 8). Heads
  and updated_at byte-identical to every read since Nov 12
  (#711 e3c3dfd0 / 2026-11-12T20:04:57Z, #708 2f59c270 /
  2026-11-12T20:44:37Z, #425 4f41cdd6 /
  2026-11-12T19:29:37Z), so no new comment or review activity
  exists on any of them. None is owned by this job; no open PR
  for records/2026-11-18 or records/2026-11-19; no new
  question addressed to this job. This job's one adopted PR
  137 stays merged.
- PR #708 still awaits the integrator batch; that is the
  integrator's queue, not a question for this job.

## Sync and seeding

- Sync: reaped 0, expired 0, due 23, produced 0, already
  queued 22 (mail, help, gifts, harvest, vip, passes,
  daily-missions, secrets, treasures, radar, survivors,
  trucks, train, training, donations, events, arms-race,
  ghost-ops, star-ceremony, duel-score, scout, scout-midday).
  Branch reconcile skipped with a warning: fetch of
  records/2026-11-19 failed (remote ref missing), issue #446.
  Completion marker reaped: harvest-2026-11-19-0203 (the
  0534 failed unit). Pool at the 15:17Z stats read: inbox 78,
  claimed 0, done 2524 - matching the queue-planning 0640
  numbers exactly. Stalled priority-1: vip-2026-11-18-1800
  (created for the Nov 18 18:00 slot, still unexecuted).
- Zombie seeding: none. The most recent done zombie unit (037,
  chain zombie-2026-11-10, finished 2026-11-15T02:35Z) closed
  the chain because the Glacieradon event had ended - no Zombie
  Invasion tab in the Events hub - and the activity metadata
  forbids seeding a fresh chain until a Zombie tab is seen live
  again. No zombie unit sits in inbox or claimed, and none was
  enqueued.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 4, Train Heroes, 10.6 hours left at the 07:25 read,
  day ends 18:00 PT Nov 19. Day 3 Age of Science is now
  definitively closed with its scoring (research completions,
  valor badges, drone component chests, radar release) all
  missed. Day 4 is a hero day: hero EXP, shards, skill medals
  and recruitment tickets score, and the owner spends those
  consumables; radar posture is STACK - complete but do not
  claim. None of it is reachable while the window is down. No
  game unit has executed since ticker-0214 gifts at 02:14 PT
  Nov 17, about fifty-three hours of routine now missed.
  Seventh consecutive VIP day already lost at the 19:00 reset
  Nov 18 (sixth lost day) with the seventh game day now
  running and unreachable; fifth consecutive missed pre-reset
  sweep night (the Nov 18 pair expired unexecuted). Tonight's
  sweep pair exists in the pool via plan staging (1630 seq 1 +
  1730 seq 2, both expiring 18:00 local).

## Delivery

- VPS SSH still Permission denied (publickey), probed 07:26 PT,
  about 162.6 hours into the break (outage since about 12:47 PT
  2026-11-12; owner chose the IONOS console route 2026-11-14
  17:37 PT, about 109 hours ago; no fix yet). Push and PR are
  blocked.
- Delivery PARTIAL: record committed locally on
  ticker-0704-1119-delivery, UNPUSHED, push pending VPS
  recovery. No PR opened for records/2026-11-19. No Slack sync.
  Chat report owed per the ticker rule (previous pass also
  access-failed); this pass's final message carries it.
- Missed batches stay 40 (no batch point in this run window;
  the 07:00 point awaits the integrator's 07:00-batch pass).
- Live mirror log note: the append to the live tree's
  _logs_/repo-actions/action-log.jsonl landed, but the file
  check reports 5 pre-existing lines that do not parse as
  JSON (lines 59, 106, 374, 380, 381 - concatenated pairs
  and a blank line from the Nov 3 era, the #401/#422 class).
  The delivery-branch copy (from main) checks clean at 1965
  lines, so the committed record is unaffected; the live
  tree's log still needs the gate repair (PR #425) at route
  recovery.

## Standing git status anomaly in the live mirror (persists)

- `git status` in the live mirror still reports a large changed
  set (modified activity files, deleted inbox unit files,
  deleted tools entries that exist on disk) while the queue
  tools run against the files on disk. The live tree sits on
  branch work/ops-execution-records, another job's in-flight
  state; no commit was attempted from this tree. The delivery
  commit goes through a temporary worktree on
  ticker-0704-1119-delivery (created from main), as the 0534
  pass did. The live mirror's _records_/2026-11-19/ tree is
  untracked there, so the delivery branch carries only this
  job's ticker sections of the day INDEX, not the other
  jobs' sections.
- Root cause of the tools/ deletions pinned at 0500: `tools`
  is a symlink to `_tools_` (Nov 8), while git tracks
  `tools/duel.py` and friends as real paths, so git reports
  every tools/ entry as deleted although the files run fine
  through the symlink. Cosmetic only; no repair attempted.

## Owed work

- Tooling Issue for the repeated failure mode "game window lost
  in fullscreen Space, control channel blind" (class tooling) -
  filing owed at VPS recovery; gh unreachable while VPS SSH is
  down. Same owed item as every ticker pass since ticker-0443.
  This pass adds two observations beyond the 0534 record:
  (a) connection.health is now called (closing the 0534 gap) -
  both transports healthy with fresh lastResponseAgeSeconds
  0/3 but progressAgeSeconds 10567, about 2.9 hours frozen,
  matching the stale last_seen; (b) three computer sessions
  all agree on the failure, so the retry rule's three attempts
  are satisfied inside the probe itself with no unit claimed.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-0704-1119-delivery, UNPUSHED, push pending VPS
  recovery. No PR opened for records/2026-11-19.
