---
title: Queue ticker process failure - game window missing, fifty-ninth consecutive occurrence
created: 2026-11-19T10:31:00Z
modified: 2026-11-19T10:31:00Z
version: 1.0.0
description: Queue ticker 2026-11-19 02:04 PT process failure, LastWar has no window on the Mac mini
status: process-failure
grounded_in:
  - source: _records_/2026-11-19/queue-ticker/0034-process-failure.md read AFTER sync and AFTER the mail unit was claimed (ordering deviation, stated in the record)
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-19T10:15Z
  - source: computer.session cc-122, computer.control list_windows, activate and open_app, environment.describe, connection.health, 2026-11-19T10:15Z to 10:23Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-0215.json, 2026-11-19T10:31Z
  - source: tools/duel.py --json, 2026-11-19T10:24Z
  - source: tools/queue.py sync and stats, 2026-11-19T10:16Z
  - source: VPS SSH probe, 2026-11-19T10:15Z
  - source: GitHub connector list_pull_requests on zachmesh/lastwar, 2026-11-19T10:17Z
---

# Queue ticker 2026-11-19 02:04 to about 02:31 PT (ticker-0215) - PROCESS FAILURE

No game unit executed: the pass hit the windowless-LastWar
blocker for the fifty-ninth consecutive ticker pass, by the
running count in the records (ticker-0034 at 00:34 PT Nov 19
was the fifty-eighth; no ticker record exists for the 01:04
or 01:34 slots on Nov 19, so the count advances by this pass
alone). No batch point passed during this run window, so
missed batches stay 39; next point 03:00 PT Nov 19.

## ORDERING DEVIATION, stated plainly

This pass ran sync BEFORE re-reading the newest queue-ticker
record (0034), against the ticker-0534 route change (re-read
the newest queue-ticker record FIRST, before sync and before
any claim) - the same deviation as 0034 and the passes it
lists. It also claimed the mail unit BEFORE probing the
device, where 0034's route probes first and claims nothing
when the window is absent. The claim is closed properly
below (failed, no stranded claim, tracker untouched), so the
deviation cost one failed unit record instead of a clean
no-claim pass, but it is NOT a honoring pass: the
deviation-watch verification stays at ZERO honoring passes.
The next pass must re-read the newest queue-ticker record
FIRST, before sync and before any claim, and probe the device
before claiming any unit.

## The claimed unit - mail-2026-11-18-2230, failed

- Claimed 02:15 PT by ticker-0215 (lease to 02:39 PT) from
  the queue pick (earliest expiry). Token held 02:15-02:24
  PT, released after the probe.
- Completed as failed: Mac mini online but LastWar exposes
  no window, so no mail screen was ever reached, no game
  input sent, nothing claimed. Evidence is this record.
  Tracker untouched (failed units do not move it); the mail
  regular stays due and the next tick re-produces it.
- Result stats: target claim-mail-rewards, achieved 0,
  resources_gained none, costs probe-only, verified no,
  blocker_category a (window closure).

## Probe - one computer session, blocker unchanged, channel answering but not progressing

- Mac mini ONLINE per device.list, last_seen
  2026-11-19T08:26:23Z - UNCHANGED since the 0034 read: the
  same timestamp, now about 117 minutes old at probe time.
  connection.health shows both transports healthy,
  lastResponseAgeSeconds 0 (native) and 1 (web), but
  progressAgeSeconds about 6940-6944 on both, up from about
  1826-1830 at 0034 - the last progress event was about
  08:26Z, the same moment as last_seen. The channel answers
  promptly (19 device invokes, 0 timeouts) but has made no
  progress since 08:26:23Z. The frozen-last_seen shade is
  back in this milder form: the timestamp does not move
  while the transports answer. No evidence the owner has
  done the Dock-icon step: the window is still missing.
- environment.describe confirms LastWar IS in running_apps,
  alongside Google Chrome, ChatGPT and Finder. Accessibility
  and screen recording permissions are granted. Display
  1920x1080. `agent_window.available` is false with reason
  `new_tab_in_existing_window`.
- Session cc-122: open_app "LastWar" outcome_unknown twice;
  list_windows for LastWar returned 0 windows three times;
  the full list_windows returned 11 windows with no LastWar
  entry; activate LastWar failed ax_windows_empty with
  brought_to_front false; computer.observe and screen.snap
  both observation_unavailable. Three window attempts, as
  the standing authorization requires before a pass is
  recorded access-failed. The pass stops here on the window,
  not on the token.
- Methodology note, stated plainly: no game input was sent in
  this pass. No Escape, Return or Control-Command-F was used;
  the green zoom button stays untouched per the standing
  lesson. No Touch ID, no password.
- Probe classification: tools/mac_capture_probe.py v1.2.0 on
  the assembled evidence (/tmp/lw-probe-0215.json) returns
  OFF_SCREEN_WINDOW, high confidence, stop_pass yes (exit
  10). Same label as 0034 and the twelve passes before it.
  The only missing probe steps are the View-menu inspect
  (Enter/Exit Full Screen), unreachable without a bound
  window, and a Chrome control observation, not attempted
  this pass. The recovery stays the same owner step (issue
  #284): click the LastWar Dock icon once (or run
  tools/mac_lastwar_front.sh in Terminal), then re-probe.

## Own PRs first

- VPS route down (SSH Permission denied, see below), so no gh
  check was possible this pass. The open PR list was re-read
  via the authenticated GitHub connector
  (2026-11-19T10:17Z): exactly three open PRs - #711
  (knowledge, Owner lastwar-knowledge-organizer, head e3c3dfd0,
  updated 2026-11-12T20:04:57Z), #708 (records 2026-11-12,
  Owner lastwar-pr-integrator, head 2f59c270, updated
  2026-11-12T20:44:37Z), #425 (tooling, Owner
  lastwar-tool-developer, head 4f41cdd6, updated
  2026-11-12T19:29:37Z). Same three as every pass since Nov 12,
  heads and updated_at unchanged since Nov 12 (so no new
  comments on any of them). None is owned by this job; no open
  PR for records/2026-11-18 or records/2026-11-19. No question
  addressed to this job, nothing to fix. Corroborated by the
  pr-catchall 0139 read (02:18 PT) in the same day INDEX.

## Sync and seeding

- Sync: reaped 0, expired 6 (the 2203 set - training,
  survivors, radar, harvest, donations, arms-race
  2026-11-18-2203, windows passed unexecuted), due 23,
  produced 0, already queued 22 (mail, help, gifts, harvest,
  vip, passes, daily-missions, secrets, treasures, radar,
  survivors, trucks, train, training, donations, events,
  arms-race, ghost-ops, star-ceremony, duel-score, scout,
  scout-midday). Branch reconcile skipped with a warning:
  fetch of records/2026-11-19 failed (remote ref missing),
  issue #446. Pool at the 10:16Z stats read: inbox 68,
  claimed 0, done 2495. Newest executed closing
  2026-11-19T05:25:15Z (survivors-2026-11-18-1803,
  ticker-2104, failed - window loss), about 290 minutes
  before this pass. Stalled priority-1: vip-2026-11-18-1800
  (20.0h).
- Zombie seeding: none. The most recent done zombie unit (037,
  chain zombie-2026-11-10, finished 2026-11-15T02:35Z) closed
  the chain because the Glacieradon event had ended - no Zombie
  Invasion tab in the Events hub - and the activity metadata
  forbids seeding a fresh chain until a Zombie tab is seen live
  again. No zombie unit sits in inbox or claimed, and none was
  enqueued.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 4, Train Heroes, 15.6 hours left at the 02:24 read,
  day ends 18:00 PT Nov 19. Day 3 Age of Science is now
  definitively closed with its scoring (research completions,
  valor badges, drone component chests, radar release) all
  missed. Day 4 is a hero day: hero EXP, shards, skill medals
  and recruitment tickets score, and the owner spends those
  consumables; radar posture is STACK - complete but do not
  claim. None of it is reachable while the window is down. No
  game unit has executed since ticker-0214 gifts at 02:14 PT
  Nov 17, about forty-eight hours of routine now missed.
  Sixth consecutive VIP day already lost at the 19:00 reset
  Nov 18; the seventh game day is now running and
  unreachable. Fifth consecutive missed pre-reset sweep night
  (the Nov 18 pair expired unexecuted).

## Delivery

- VPS SSH still Permission denied (publickey), probed 02:15 PT,
  about 157.8 hours into the break (outage since about 12:47 PT
  2026-11-12; owner chose the IONOS console route 2026-11-14
  17:37 PT, about 105 hours ago; no fix yet). Push and PR are
  blocked.
- Delivery PARTIAL: record committed locally on
  ticker-0215-1119-delivery, UNPUSHED, push pending VPS
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
  commit goes through a temporary worktree on
  ticker-0215-1119-delivery (created from main), as the 0034
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
  This pass adds one new observation beyond the 0034 record:
  the gateway last_seen timestamp has NOT advanced since 0034
  (08:26:23Z, now about 117 minutes old) and progressAgeSeconds
  grew from about 1830 to about 6940, so the frozen-progress
  shade is back while the transports still answer promptly -
  the channel is live but idle since 08:26:23Z, which
  separates the channel from the window fault more cleanly
  than the 2345 read did.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-0215-1119-delivery, UNPUSHED, push pending VPS
  recovery. No PR opened for records/2026-11-19.
