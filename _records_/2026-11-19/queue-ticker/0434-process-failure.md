---
title: Queue ticker process failure - game window missing, sixty-first consecutive occurrence
created: 2026-11-19T12:46:00Z
modified: 2026-11-19T12:46:00Z
version: 1.0.0
description: Queue ticker 2026-11-19 04:34 PT process failure, LastWar has no window on the Mac mini
status: process-failure
grounded_in:
  - source: _records_/2026-11-19/queue-ticker/0331-process-failure.md re-read FIRST, before sync and before any claim (route honored this pass)
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-19T12:40Z
  - source: computer.session cc-124 and cc-125, computer.control list_windows, activate and open_app, environment.describe, connection.health, computer.observe, screen.snap, 2026-11-19T12:41Z to 12:45Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-0434.json, 2026-11-19T12:45Z
  - source: tools/duel.py --json, 2026-11-19T12:41Z
  - source: tools/queue.py sync and stats, 2026-11-19T12:40Z
  - source: VPS SSH probe, 2026-11-19T12:39Z
  - source: GitHub connector list_pull_requests on zachmesh/lastwar, 2026-11-19T12:40Z, corroborated by _records_/2026-11-19/pr-catchall/0339-run.md
---

# Queue ticker 2026-11-19 04:34 to about 04:45 PT (ticker-0434) - PROCESS FAILURE

No game unit executed: the pass hit the windowless-LastWar
blocker for the sixty-first consecutive ticker pass, by the
running count in the records (ticker-0331 at 03:04 PT Nov 19
was the sixtieth; no ticker record exists for the 04:04
slot on Nov 19, so the count advances by this pass alone).
No batch point passed during this run window, so missed
batches stay 40; next point 07:00 PT Nov 19.

## ROUTE HONORED - deviation watch moves off zero

This pass re-read the newest queue-ticker record (0331)
FIRST, before sync and before any claim, and probed the
device before claiming any unit - the ticker-0534 route
change, honored in full. The sync was harmless (reaped 0,
produced 0), NO unit was claimed before the probe, the
token was taken, the device probed, and the token released
with nothing claimed. This is the FIRST honoring pass: the
deviation-watch verification moves from ZERO to ONE
honoring pass. The next pass must keep the same order -
newest queue-ticker record first, then sync, then probe
before any claim.

## No unit claimed - probe before claim honored

- Token held 04:41-04:45 PT by ticker-0434, released after
  the probe with nothing claimed. No unit entered claimed;
  the tracker is untouched.
- Probe classification: tools/mac_capture_probe.py v1.2.0 on
  the assembled evidence (/tmp/lw-probe-0434.json) returns
  OFF_SCREEN_WINDOW, high confidence, stop_pass yes (exit
  10). Same label as 0331 and the passes before it.

## Probe - two computer sessions, blocker unchanged, channel progressed again

- Mac mini ONLINE per device.list, last_seen
  2026-11-19T12:25:42Z - ADVANCED from 10:25:01Z at the 0331
  probe: the channel progressed again at about 12:25Z,
  about 17 minutes before this probe, after the 0331 probe
  ended. connection.health shows both transports healthy,
  lastResponseAgeSeconds 0 (native) and 8 (web), but
  progressAgeSeconds 939/938, down from about 4149 at 0331
  - last progress moved from 10:25Z to about 12:25Z. The
  channel answers promptly (20 device invokes, 0 timeouts)
  and its progress now moves in steps of about two hours,
  not minutes. The frozen-progress shade persists in this
  milder form. No evidence the owner has done the Dock-icon
  step: the window is still missing.
- environment.describe confirms LastWar IS in running_apps,
  alongside Google Chrome, ChatGPT and Finder. Accessibility
  and screen recording permissions are granted. Display
  1920x1080. `agent_window.available` is false with reason
  `new_tab_in_existing_window`.
- Session cc-124: open_app "LastWar" outcome_unknown once;
  list_windows for LastWar returned 0 windows twice; the full
  list_windows returned 11 windows with no LastWar entry;
  activate LastWar failed ax_windows_empty with
  brought_to_front false; computer.observe and screen.snap
  both observation_unavailable (the first observe collided
  with the parallel snap as computer_busy; the serial retry
  returned observation_unavailable cleanly). Three window
  attempts, as the standing authorization requires before a
  pass is recorded access-failed. The pass stops here on the
  window, not on the token.
- Chrome observation, the step 0331 left blocked on
  ambiguity: attempted in TWO forms this pass, both failed
  on geometry, not on ambiguity - activate with window_id
  125 (the "Recharge Center - LASTWAR" Chrome window) and
  activate by app name "Google Chrome" both failed
  geometry_mismatch (origin_delta=256+, size_delta=256+,
  agent_display=false), and the follow-up observe returned
  observation_unavailable. chrome_observes_ok is therefore
  measured FALSE this pass, not null: the control layer
  cannot select ANY window on the agent display, not only
  the LastWar window. The probe classification is unchanged
  (OFF_SCREEN_WINDOW, high confidence - on_screen false
  plus brought_to_front false decides it before the Chrome
  branch), but the fault picture widens: no window is
  selectable, so the recovery is still the owner step and
  no background route exists.
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
  (2026-11-19T12:40Z): exactly three open PRs - #711
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
  pr-catchall 0339 read (04:25-04:31 PT) in the same day INDEX.

## Sync and seeding

- Sync: reaped 0, expired 0, due 23, produced 0, already
  queued 22 (mail, help, gifts, harvest, vip, passes,
  daily-missions, secrets, treasures, radar, survivors,
  trucks, train, training, donations, events, arms-race,
  ghost-ops, star-ceremony, duel-score, scout, scout-midday).
  Branch reconcile skipped with a warning: fetch of
  records/2026-11-19 failed (remote ref missing), issue #446.
  Pool at the 12:40Z stats read: inbox 75, claimed 0, done
  2506, upcoming 53. Newest executed closing
  2026-11-19T10:26:38Z (the 0215 mail failed unit), about 134
  minutes before this pass. Stalled priority-1:
  vip-2026-11-18-1800 (about 22.5h).
- Zombie seeding: none. The most recent done zombie unit (037,
  chain zombie-2026-11-10, finished 2026-11-15T02:35Z) closed
  the chain because the Glacieradon event had ended - no Zombie
  Invasion tab in the Events hub - and the activity metadata
  forbids seeding a fresh chain until a Zombie tab is seen live
  again. No zombie unit sits in inbox or claimed, and none was
  enqueued.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 4, Train Heroes, 13.3 hours left at the 04:41 read,
  day ends 18:00 PT Nov 19. Day 3 Age of Science is now
  definitively closed with its scoring (research completions,
  valor badges, drone component chests, radar release) all
  missed. Day 4 is a hero day: hero EXP, shards, skill medals
  and recruitment tickets score, and the owner spends those
  consumables; radar posture is STACK - complete but do not
  claim. None of it is reachable while the window is down. No
  game unit has executed since ticker-0214 gifts at 02:14 PT
  Nov 17, about fifty and a half hours of routine now
  missed. Sixth consecutive VIP day already lost at the 19:00
  reset Nov 18; the seventh game day is now running and
  unreachable. Fifth consecutive missed pre-reset sweep night
  (the Nov 18 pair expired unexecuted).

## Delivery

- VPS SSH still Permission denied (publickey), probed 04:39 PT,
  about 159.9 hours into the break (outage since about 12:47 PT
  2026-11-12; owner chose the IONOS console route 2026-11-14
  17:37 PT, about 107 hours ago; no fix yet). Push and PR are
  blocked.
- Delivery PARTIAL: record committed locally on
  ticker-0434-1119-delivery, UNPUSHED, push pending VPS
  recovery. No PR opened for records/2026-11-19. No Slack sync.
  Chat report owed per the ticker rule (previous pass also
  access-failed); this pass's final message carries it.
- Missed batches stay 40 (no batch point in this run window;
  next point 07:00 PT Nov 19).

## Standing git status anomaly in the live mirror (persists)

- `git status` in the live mirror still reports a large changed
  set (modified activity files, deleted inbox unit files,
  deleted tools entries that exist on disk) while the queue
  tools run against the files on disk. The live tree sits on
  branch work/ops-execution-records, another job's in-flight
  state; no commit was attempted from this tree. The delivery
  commit goes through a temporary worktree on
  ticker-0434-1119-delivery (created from main), as the 0331
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
  This pass adds one new observation beyond the 0331 record:
  Chrome windows ALSO fail selection now (geometry_mismatch,
  agent_display=false, two activate forms) - the fault is no
  longer only "LastWar has no window" but "no window is
  selectable on the agent display". That observation belongs
  in the owed issue's evidence when it is filed.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-0434-1119-delivery, UNPUSHED, push pending VPS
  recovery. No PR opened for records/2026-11-19.
