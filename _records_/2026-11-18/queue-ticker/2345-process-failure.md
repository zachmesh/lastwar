---
title: Queue ticker process failure - game window missing, fifty-seventh consecutive occurrence
created: 2026-11-19T07:55:00Z
modified: 2026-11-19T07:55:00Z
version: 1.0.0
description: Queue ticker 2026-11-18 23:45 PT process failure, LastWar has no window on the Mac mini
status: process-failure
grounded_in:
  - source: _records_/2026-11-18/queue-ticker/2233-process-failure.md read FIRST, before sync (ticker-0534 route change honored)
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-19T07:47Z
  - source: computer.session cc-115, cc-116, cc-117, computer.control list_windows, activate and open_app, environment.describe, connection.health, 2026-11-19T07:47Z to 07:54Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-2345.json, 2026-11-19T07:54Z
  - source: tools/duel.py --json, 2026-11-19T07:48Z
  - source: tools/queue.py sync and stats, 2026-11-19T07:46Z
  - source: VPS SSH probe, 2026-11-19T07:47Z
  - source: unauthenticated GitHub REST open-PR list on zachmesh/lastwar, 2026-11-19T07:46Z
---

# Queue ticker 2026-11-18 23:45 to about 23:58 PT (ticker-2345) - PROCESS FAILURE

No game unit executed: the pass hit the windowless-LastWar
blocker for the fifty-seventh consecutive ticker pass, by the
running count in the records (ticker-2233 at 22:33 PT was the
fifty-sixth; no ticker record exists for the 23:03 or 23:33
slots, so the count advances by this pass alone). No batch
point passed during this run window, so missed batches stay 39;
next point 03:00 PT Nov 19.

## Route change honored - no claim this pass

This pass read the newest queue-ticker record (2233) FIRST,
before sync, per the ticker-0534 route change (claim no unit
until the window is recovered). No unit was claimed, no unit
was completed, no token was acquired - there is nothing to
play, so the device token was never taken and there is nothing
to release. The 2233 deviation (mail-1830 claimed before the
record was re-read, then released un-executed) does not recur
here; the honoring watch restarts at one.

## Probe - three computer sessions, blocker unchanged, channel live

- Mac mini ONLINE per device.list, last_seen 2026-11-19T06:24:14Z
  - STALE again: the same timestamp the 2233 pass read as fresh
  at 06:28Z has not advanced by 07:47Z, about 83 minutes frozen.
  NEW shade against 2233: the gateway progress timestamp froze
  again while the transports answer promptly. connection.health
  shows both transports healthy, lastResponseAgeSeconds 0 (native)
  and 4 (web), progressAgeSeconds about 4995 on both. All 12
  device invokes in this pass returned promptly with 0 timeouts.
  This is not the probe v1.1.0 channel-stall form; no
  connection.repair was run this pass. No evidence the owner has
  done the Dock-icon step: the window is still missing.
- environment.describe confirms LastWar IS in running_apps,
  alongside Google Chrome, ChatGPT and Finder. Accessibility and
  screen recording permissions are granted. Display 1920x1080.
  `agent_window.available` is false with reason
  `new_tab_in_existing_window`.
- Session cc-115: open_app "LastWar" outcome_unknown; activate
  LastWar failed ax_windows_empty with stale_observation;
  list_windows returned 11 windows with no LastWar entry.
  Session cc-116 (fresh): open_app "LastWar" outcome_unknown
  again; list_windows still 11 windows, no LastWar. Session
  cc-117 (fresh): open_app "LastWar" outcome_unknown a third
  time; list_windows still 11 windows, no LastWar. Three
  attempts, as the standing authorization requires before a
  pass is recorded access-failed. The pass stops here on the
  window, not on the token.
- Methodology note, stated plainly: no game input was sent in
  this pass. No Escape, Return or Control-Command-F was used;
  the green zoom button stays untouched per the standing
  lesson. No Touch ID, no password.
- Probe classification: tools/mac_capture_probe.py v1.2.0 on the
  assembled evidence (/tmp/lw-probe-2345.json) returns
  OFF_SCREEN_WINDOW, high confidence, stop_pass yes. Same label
  as the 0616, 0733, 1010, 1133, 1248, 1354, 1504, 1604, 1734,
  1804 and 2233 passes. The only missing probe steps are the
  View-menu inspect (Enter/Exit Full Screen), unreachable
  without a bound window, and one control observation of a
  Chrome window. The recovery stays the same owner step (issue
  #284): click the LastWar Dock icon once (or run
  tools/mac_lastwar_front.sh in Terminal), then re-probe.

## Own PRs first

- VPS route down (SSH Permission denied, see below), so no gh
  check was possible this pass. The public PR list was re-read
  via the unauthenticated GitHub REST API
  (2026-11-19T07:46Z): exactly three open PRs - #711
  (knowledge, Owner lastwar-knowledge-organizer, head e3c3dfd0,
  updated 2026-11-12T20:04:57Z), #708 (records 2026-11-12,
  Owner lastwar-pr-integrator, head 2f59c270, updated
  2026-11-12T20:44:37Z), #425 (tooling, Owner
  lastwar-tool-developer, head 4f41cdd6, updated
  2026-11-12T19:29:37Z). Same three as every pass since Nov 12,
  heads and updated_at unchanged since Nov 12 (so no new
  comments on any of them). None is owned by this job; no open
  PR for records/2026-11-18. No question addressed to this job,
  nothing to fix.

## Sync and seeding

- Sync: reaped 0, expired 5, due 22, produced 0, already queued
  22 (mail, help, gifts, harvest, vip, passes, daily-missions,
  secrets, treasures, radar, survivors, trucks, train, training,
  donations, events, arms-race, star-ceremony, duel-score,
  scout, scout-midday). Branch reconcile skipped with a warning:
  fetch of records/2026-11-18 failed (remote ref missing),
  issue #446. Pool at the 07:47Z stats read:
  inbox 69, claimed 0, done 2489, upcoming 48. No unit claimed,
  no unit completed.
- Zombie seeding: none. The most recent done zombie unit (037,
  chain zombie-2026-11-10, finished 2026-11-15T02:35Z) closed
  the chain because the Glacieradon event had ended - no Zombie
  Invasion tab in the Events hub - and the activity metadata
  forbids seeding a fresh chain until a Zombie tab is seen live
  again. No zombie unit sits in inbox or claimed, and none was
  enqueued.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 4, Train Heroes, 18.2 hours left at the 23:48 read,
  day ends 18:00 PT Nov 19. Day 3 Age of Science is now
  definitively closed with its scoring (research completions,
  valor badges, drone component chests, radar release) all
  missed. Day 4 is a hero day: hero EXP, shards, skill medals
  and recruitment tickets score, and the owner spends those
  consumables; radar posture is STACK - complete but do not
  claim. None of it is reachable while the window is down. No
  game unit has executed since ticker-0214 gifts at 02:14 PT
  Nov 17, about forty-five and a half hours of routine now
  missed. Sixth consecutive VIP day already lost at the 19:00
  reset; the seventh game day is now running and unreachable.
  Fifth consecutive missed pre-reset sweep night.

## Delivery

- VPS SSH still Permission denied (publickey), probed 23:47 PT,
  about 155 hours into the break (outage since about 12:47 PT
  2026-11-12; owner chose the IONOS console route 2026-11-14
  17:37 PT, about 102 hours ago; no fix yet). Push and PR are
  blocked.
- Delivery PARTIAL: record committed locally on
  ticker-2345-1118-delivery, UNPUSHED, push pending VPS
  recovery. No PR opened for records/2026-11-18. No Slack sync.
  Chat report owed per the ticker rule (previous pass also
  access-failed); this pass's final message carries it.
- The 23:00 batch point passed during the 2239 catch-all window;
  missed batches stay 39 (next point 03:00 PT Nov 19).

## Standing git status anomaly in the live mirror (persists)

- `git status` in the live mirror still reports a large changed
  set (modified activity files, deleted inbox unit files,
  deleted tools entries that exist on disk) while the queue
  tools run against the files on disk. The live tree sits on
  branch work/ops-execution-records, another job's in-flight
  state; no commit was attempted from this tree. The delivery
  commit goes through a temporary worktree on records/2026-11-18,
  as the 2233 pass did. The live mirror's _records_/2026-11-18/
  tree is untracked there, so the delivery branch carries only
  this job's ticker sections of the day INDEX, not the other
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
  This pass adds one new observation beyond the 2233 record:
  the gateway last_seen timestamp is FROZEN again at
  06:24:14Z (about 83 minutes stale at probe time) although
  connection.health reports both transports healthy with
  lastResponseAgeSeconds 0-4s - the frozen-progress shade has
  returned on a live channel, so a fresh last_seen no longer
  proves the gateway is progressing.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-2345-1118-delivery, UNPUSHED, push pending VPS
  recovery. No PR opened for records/2026-11-18.
