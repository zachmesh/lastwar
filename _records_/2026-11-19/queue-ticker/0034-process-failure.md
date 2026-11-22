---
title: Queue ticker process failure - game window missing, fifty-eighth consecutive occurrence
created: 2026-11-19T09:06:00Z
modified: 2026-11-19T09:06:00Z
version: 1.0.0
description: Queue ticker 2026-11-19 00:34 PT process failure, LastWar has no window on the Mac mini
status: process-failure
grounded_in:
  - source: _records_/2026-11-18/queue-ticker/2345-process-failure.md read AFTER sync (ordering deviation, stated in the record)
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-19T08:56Z
  - source: computer.session cc-118, cc-119, cc-120, cc-121, computer.control list_windows, activate and open_app, environment.describe, connection.health, 2026-11-19T08:57Z to 09:04Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-0034.json, 2026-11-19T09:04Z
  - source: tools/duel.py --json, 2026-11-19T08:59Z
  - source: tools/queue.py sync and stats, 2026-11-19T08:54Z
  - source: VPS SSH probe, 2026-11-19T08:53Z
  - source: unauthenticated GitHub REST open-PR list on zachmesh/lastwar, 2026-11-19T08:56Z
---

# Queue ticker 2026-11-19 00:34 to about 01:06 PT (ticker-0034) - PROCESS FAILURE

No game unit executed: the pass hit the windowless-LastWar
blocker for the fifty-eighth consecutive ticker pass, by the
running count in the records (ticker-2345 at 23:45 PT Nov 18
was the fifty-seventh; no ticker record exists for the 00:04
slot on Nov 19, so the count advances by this pass alone). No
batch point passed during this run window, so missed batches
stay 39; next point 03:00 PT Nov 19.

## ORDERING DEVIATION, stated plainly

This pass ran sync BEFORE re-reading the newest queue-ticker
record (2345), against the ticker-0534 route change (re-read
the newest queue-ticker record FIRST, before sync and before
any claim) - the same deviation as 0004, 0134, 0243, 0353,
0500, 0733, 0834 and 1010. The sync produced nothing and no
unit was claimed, so it cost nothing this time, but it is NOT
a honoring pass: the 2345 pass was honoring pass number one
since the watch restarted, and this pass breaks the streak,
so the deviation-watch verification restarts at ZERO honoring
passes. The claim rule itself held in substance - no unit was
claimed at all, because the probe came first and the window
was absent. The next pass must re-read the newest queue-ticker
record FIRST, before sync and before any claim.

## Probe - four computer sessions, blocker unchanged, channel progressing

- Mac mini ONLINE per device.list, last_seen
  2026-11-19T08:26:23Z - ADVANCED again: the same timestamp
  the 2345 pass read as frozen at 06:24:14Z has moved about
  two hours. It is about 30 minutes old at probe time, not
  frozen. connection.health shows both transports healthy,
  lastResponseAgeSeconds 0 (native) and 9 (web),
  progressAgeSeconds about 1826-1830 on both, down from about
  4995 at 2345 - the transports are progressing again. All 15
  device invokes in this pass returned promptly with 0
  timeouts. No evidence the owner has done the Dock-icon step:
  the window is still missing.
- environment.describe confirms LastWar IS in running_apps,
  alongside Google Chrome, ChatGPT and Finder. Accessibility
  and screen recording permissions are granted. Display
  1920x1080. `agent_window.available` is false with reason
  `new_tab_in_existing_window`.
- Session cc-118: open_app "LastWar" outcome_unknown;
  list_windows returned 11 windows with no LastWar entry;
  activate LastWar failed ax_windows_empty with
  stale_observation; observe observation_unavailable.
  Session cc-119 (fresh): open_app "LastWar"
  outcome_unknown again; list_windows still 11 windows, no
  LastWar. Session cc-120 (fresh): open_app "LastWar"
  outcome_unknown a third time; list_windows still 11
  windows, no LastWar. Three attempts, as the standing
  authorization requires before a pass is recorded
  access-failed. Session cc-121 (fresh, Chrome control
  observation for the probe checklist): activate Google
  Chrome failed geometry_mismatch, agent_display=false,
  stale_observation - the control channel is wedged on the
  stale LastWar target, so no window at all can be bound,
  the same shade as 1010, 0034 and 0134. The pass stops here
  on the window, not on the token.
- Methodology note, stated plainly: no game input was sent in
  this pass. No Escape, Return or Control-Command-F was used;
  the green zoom button stays untouched per the standing
  lesson. No Touch ID, no password.
- Probe classification: tools/mac_capture_probe.py v1.2.0 on
  the assembled evidence (/tmp/lw-probe-0034.json) returns
  OFF_SCREEN_WINDOW, high confidence, stop_pass yes (exit
  10). Same label as 0616, 0733, 1010, 1133, 1248, 1354,
  1504, 1604, 1734, 1804, 2233 and 2345. The only missing
  probe step is the View-menu inspect (Enter/Exit Full
  Screen), unreachable without a bound window. The recovery
  stays the same owner step (issue #284): click the LastWar
  Dock icon once (or run tools/mac_lastwar_front.sh in
  Terminal), then re-probe.
- Token held 00:54-01:05 PT, released unused; no unit
  claimed.

## Own PRs first

- VPS route down (SSH Permission denied, see below), so no gh
  check was possible this pass. The public PR list was re-read
  via the unauthenticated GitHub REST API
  (2026-11-19T08:56Z): exactly three open PRs - #711
  (knowledge, Owner lastwar-knowledge-organizer, head e3c3dfd0,
  updated 2026-11-12T20:04:57Z), #708 (records 2026-11-12,
  Owner lastwar-pr-integrator, head 2f59c270, updated
  2026-11-12T20:44:37Z), #425 (tooling, Owner
  lastwar-tool-developer, head 4f41cdd6, updated
  2026-11-12T19:29:37Z). Same three as every pass since Nov 12,
  heads and updated_at unchanged since Nov 12 (so no new
  comments on any of them). None is owned by this job; no open
  PR for records/2026-11-18 or records/2026-11-19. No question
  addressed to this job, nothing to fix.

## Sync and seeding

- Sync: reaped 0, expired 0, due 23, produced 0, already queued
  23 (mail, help, gifts, harvest, vip, passes, daily-missions,
  secrets, treasures, radar, survivors, trucks, train, training,
  donations, events, arms-race, ghost-ops, star-ceremony,
  duel-score, scout, scout-midday). Branch reconcile skipped
  with a warning: fetch of records/2026-11-19 failed (remote
  ref missing), issue #446. Pool at the 08:54Z stats read:
  inbox 74, claimed 0, done 2489. No unit claimed, no unit
  completed. Stalled priority-1: vip-2026-11-18-1800 (18.6h).
- Zombie seeding: none. The most recent done zombie unit (037,
  chain zombie-2026-11-10, finished 2026-11-15T02:35Z) closed
  the chain because the Glacieradon event had ended - no Zombie
  Invasion tab in the Events hub - and the activity metadata
  forbids seeding a fresh chain until a Zombie tab is seen live
  again. No zombie unit sits in inbox or claimed, and none was
  enqueued.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 4, Train Heroes, 17.0 hours left at the 00:59 read,
  day ends 18:00 PT Nov 19. Day 3 Age of Science is now
  definitively closed with its scoring (research completions,
  valor badges, drone component chests, radar release) all
  missed. Day 4 is a hero day: hero EXP, shards, skill medals
  and recruitment tickets score, and the owner spends those
  consumables; radar posture is STACK - complete but do not
  claim. None of it is reachable while the window is down. No
  game unit has executed since ticker-0214 gifts at 02:14 PT
  Nov 17, about forty-six and three-quarter hours of routine
  now missed. Sixth consecutive VIP day already lost at the
  19:00 reset; the seventh game day is now running and
  unreachable. Fifth consecutive missed pre-reset sweep night
  (the Nov 18 pair expired unexecuted).

## Delivery

- VPS SSH still Permission denied (publickey), probed 00:53 PT,
  about 156 hours into the break (outage since about 12:47 PT
  2026-11-12; owner chose the IONOS console route 2026-11-14
  17:37 PT, about 103 hours ago; no fix yet). Push and PR are
  blocked.
- Delivery PARTIAL: record committed locally on
  ticker-0034-1119-delivery, UNPUSHED, push pending VPS
  recovery. No PR opened for records/2026-11-19. No Slack sync.
  Chat report owed per the ticker rule (previous pass also
  access-failed); this pass's final message carries it.
- Missed batches stay 39 (next point 03:00 PT Nov 19).

## Standing git status anomaly in the live mirror (persists)

- `git status` in the live mirror still reports a large changed
  set (modified activity files, deleted inbox unit files,
  deleted tools entries that exist on disk) while the queue
  tools run against the files on disk. The live tree sits on
  branch work/ops-execution-records, another job's in-flight
  state; no commit was attempted from this tree. The delivery
  commit goes through a temporary worktree on records/2026-11-19
  (created from main on first use today), as the 2345 pass did
  for 2026-11-18. The live mirror's _records_/2026-11-19/
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
  This pass adds one new observation beyond the 2345 record:
  the gateway last_seen timestamp has ADVANCED again
  (06:24:14Z frozen at 2345, now 08:26:23Z) and
  progressAgeSeconds fell from about 4995 to about 1830, so
  the frozen-progress shade is gone for now - the channel is
  progressing while the window stays absent, which separates
  the channel from the window fault more cleanly than the
  2345 read did.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-0034-1119-delivery, UNPUSHED, push pending VPS
  recovery. No PR opened for records/2026-11-19.
