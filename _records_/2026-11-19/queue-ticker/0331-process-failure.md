---
title: Queue ticker process failure - game window missing, sixtieth consecutive occurrence
created: 2026-11-19T11:36:00Z
modified: 2026-11-19T11:36:00Z
version: 1.0.0
description: Queue ticker 2026-11-19 03:04 PT process failure, LastWar has no window on the Mac mini
status: process-failure
grounded_in:
  - source: _records_/2026-11-19/queue-ticker/0215-process-failure.md read AFTER sync (ordering deviation, stated in the record)
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-19T11:34Z
  - source: computer.session cc-123, computer.control list_windows, activate and open_app, environment.describe, connection.health, computer.observe, screen.snap, 2026-11-19T11:34Z to 11:35Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-0331.json, 2026-11-19T11:35Z
  - source: tools/duel.py --json, 2026-11-19T11:34Z
  - source: tools/queue.py sync and stats, 2026-11-19T11:32Z
  - source: VPS SSH probe, 2026-11-19T11:32Z
  - source: GitHub connector list_pull_requests on zachmesh/lastwar, 2026-11-19T11:33Z
---

# Queue ticker 2026-11-19 03:04 to about 03:47 PT (ticker-0331) - PROCESS FAILURE

No game unit executed: the pass hit the windowless-LastWar
blocker for the sixtieth consecutive ticker pass, by the
running count in the records (ticker-0215 at 02:04 PT Nov 19
was the fifty-ninth; no ticker record exists for the 02:34
slot on Nov 19, so the count advances by this pass alone).
The 03:00 PT batch point passed during this run window (PR
708 still open with unchanged head per the pr-catchall 0239
read), so missed batches rise 39 to 40; next point 07:00 PT
Nov 19.

## ORDERING DEVIATION, stated plainly

This pass ran sync BEFORE re-reading the newest queue-ticker
record (0215), against the ticker-0534 route change (re-read
the newest queue-ticker record FIRST, before sync and before
any claim) - the same deviation as 0215 and the passes it
lists. The sync itself was harmless (reaped 0, produced 0),
and unlike 0215 this pass claimed NO unit before probing:
the probe-before-claim half of the route WAS honored, the
token was taken, the device probed, and the token released
with nothing claimed. Even so, this is NOT a honoring pass:
the deviation-watch verification stays at ZERO honoring
passes. The next pass must re-read the newest queue-ticker
record FIRST, before sync and before any claim, and probe
the device before claiming any unit.

## No unit claimed - probe before claim honored

- Token held 03:33-03:35 PT by ticker-0331, released after
  the probe with nothing claimed. No unit entered claimed;
  the tracker is untouched.
- Probe classification: tools/mac_capture_probe.py v1.2.0 on
  the assembled evidence (/tmp/lw-probe-0331.json) returns
  OFF_SCREEN_WINDOW, high confidence, stop_pass yes (exit
  10). Same label as 0215 and the twelve passes before it.

## Probe - one computer session, blocker unchanged, channel progressed once since 0215

- Mac mini ONLINE per device.list, last_seen
  2026-11-19T10:25:01Z - ADVANCED from 08:26:23Z at the 0215
  probe: the channel made progress once at about 10:25Z
  (after the 0215 probe ended), then went idle again; at
  probe time the timestamp is about 70 minutes old.
  connection.health shows both transports healthy,
  lastResponseAgeSeconds 0 (native) and 5 (web), but
  progressAgeSeconds about 4149/4147, down from about
  6940-6944 at 0215 - the last progress event moved from
  08:26Z to 10:25Z. The channel answers promptly (15 device
  invokes, 0 timeouts) but has made no progress since
  10:25Z. The frozen-progress shade persists in this milder
  form: the timestamp moves in steps of hours, not minutes,
  while the transports answer. No evidence the owner has
  done the Dock-icon step: the window is still missing.
- environment.describe confirms LastWar IS in running_apps,
  alongside Google Chrome, ChatGPT and Finder. Accessibility
  and screen recording permissions are granted. Display
  1920x1080. `agent_window.available` is false with reason
  `new_tab_in_existing_window`.
- Session cc-123: open_app "LastWar" outcome_unknown once;
  list_windows for LastWar returned 0 windows twice; the full
  list_windows returned 11 windows with no LastWar entry;
  activate LastWar failed ax_windows_empty with
  brought_to_front false; computer.observe and screen.snap
  both observation_unavailable. Three window attempts, as
  the standing authorization requires before a pass is
  recorded access-failed. The pass stops here on the window,
  not on the token.
- Chrome control observation, the step 0215 left unattempted:
  attempted and blocked on ambiguity, not on the channel -
  open_app "Google Chrome" failed action_failed because two
  running Chrome instances match, and activate with a
  window_id is rejected (activate requires app name). No
  Chrome window was selected, so no Chrome observation was
  recorded; chrome_observes_ok stays null in the evidence.
  The channel fault is still separated from the window fault
  by the 0215 evidence (invokes answer promptly); the
  missing Chrome observation does not change the label.
- Methodology note, stated plainly: no game input was sent in
  this pass. No Escape, Return or Control-Command-F was used;
  the green zoom button stays untouched per the standing
  lesson. No Touch ID, no password.
- The recovery stays the same owner step (issue #284): click
  the LastWar Dock icon once (or run
  tools/mac_lastwar_front.sh in Terminal), then re-probe.

## Own PRs first

- VPS route down (SSH Permission denied, see below), so no gh
  check was possible this pass. The open PR list was re-read
  via the authenticated GitHub connector
  (2026-11-19T11:33Z): exactly three open PRs - #711
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
  pr-catchall 0239 read (03:23 PT) in the same day INDEX.

## Sync and seeding

- Sync: reaped 0, expired 0, due 23, produced 0, already
  queued 22 (mail, help, gifts, harvest, vip, passes,
  daily-missions, secrets, treasures, radar, survivors,
  trucks, train, training, donations, events, arms-race,
  ghost-ops, star-ceremony, duel-score, scout, scout-midday),
  completion marker reaped for mail-2026-11-18-2230. Branch
  reconcile skipped with a warning: fetch of
  records/2026-11-19 failed (remote ref missing), issue #446.
  Pool at the 11:32Z stats read: inbox 73, claimed 0, done
  2496, upcoming 41. Newest executed closing
  2026-11-19T10:26:38Z (the 0215 mail failed unit), about 66
  minutes before this pass. Stalled priority-1:
  vip-2026-11-18-1800 (about 21.5h).
- Zombie seeding: none. The most recent done zombie unit (037,
  chain zombie-2026-11-10, finished 2026-11-15T02:35Z) closed
  the chain because the Glacieradon event had ended - no Zombie
  Invasion tab in the Events hub - and the activity metadata
  forbids seeding a fresh chain until a Zombie tab is seen live
  again. No zombie unit sits in inbox or claimed, and none was
  enqueued.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 4, Train Heroes, 14.4 hours left at the 03:34 read,
  day ends 18:00 PT Nov 19. Day 3 Age of Science is now
  definitively closed with its scoring (research completions,
  valor badges, drone component chests, radar release) all
  missed. Day 4 is a hero day: hero EXP, shards, skill medals
  and recruitment tickets score, and the owner spends those
  consumables; radar posture is STACK - complete but do not
  claim. None of it is reachable while the window is down. No
  game unit has executed since ticker-0214 gifts at 02:14 PT
  Nov 17, about forty-nine and a half hours of routine now
  missed. Sixth consecutive VIP day already lost at the 19:00
  reset Nov 18; the seventh game day is now running and
  unreachable. Fifth consecutive missed pre-reset sweep night
  (the Nov 18 pair expired unexecuted).

## Delivery

- VPS SSH still Permission denied (publickey), probed 03:32 PT,
  about 158.8 hours into the break (outage since about 12:47 PT
  2026-11-12; owner chose the IONOS console route 2026-11-14
  17:37 PT, about 106 hours ago; no fix yet). Push and PR are
  blocked.
- Delivery PARTIAL: record committed locally on
  ticker-0331-1119-delivery, UNPUSHED, push pending VPS
  recovery. No PR opened for records/2026-11-19. No Slack sync.
  Chat report owed per the ticker rule (previous pass also
  access-failed); this pass's final message carries it.
- Missed batches rise 39 to 40 (next point 07:00 PT Nov 19).

## Standing git status anomaly in the live mirror (persists)

- `git status` in the live mirror still reports a large changed
  set (modified activity files, deleted inbox unit files,
  deleted tools entries that exist on disk) while the queue
  tools run against the files on disk. The live tree sits on
  branch work/ops-execution-records, another job's in-flight
  state; no commit was attempted from this tree. The delivery
  commit goes through a temporary worktree on
  ticker-0331-1119-delivery (created from main), as the 0215
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
  This pass adds one new observation beyond the 0215 record:
  the gateway last_seen timestamp HAS advanced since 0215
  (08:26:23Z to 10:25:01Z) and progressAgeSeconds fell from
  about 6940 to about 4149, so the channel progressed once at
  about 10:25Z and then went idle again - the frozen-progress
  shade persists, but it now moves in steps of hours rather
  than standing at one timestamp all day.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-0331-1119-delivery, UNPUSHED, push pending VPS
  recovery. No PR opened for records/2026-11-19.
