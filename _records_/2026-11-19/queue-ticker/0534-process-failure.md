---
title: Queue ticker process failure - game window missing, sixty-second consecutive occurrence
created: 2026-11-19T14:15:00Z
modified: 2026-11-19T14:15:00Z
version: 1.0.0
description: Queue ticker 2026-11-19 05:34 PT process failure, LastWar has no window on the Mac mini
status: process-failure
grounded_in:
  - source: _records_/2026-11-19/queue-ticker/0434-process-failure.md re-read AFTER the pass (route deviation - see below)
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-19T13:58Z
  - source: computer.session cc-126 and cc-127, computer.control list_windows, activate and open_app, environment.describe, computer.observe, screen.snap, 2026-11-19T13:59Z to 14:09Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-0534.json, 2026-11-19T14:12Z
  - source: tools/duel.py --json, 2026-11-19T14:03Z
  - source: tools/queue.py sync, stats, claim, complete and token-release, 2026-11-19T13:52Z to 14:02Z
  - source: VPS SSH probe, 2026-11-19T13:54Z
  - source: browser.open re-read of the public PR list on zachmesh/lastwar, 2026-11-19T13:54Z
---

# Queue ticker 2026-11-19 05:34 to about 06:15 PT (ticker-0534) - PROCESS FAILURE

One game unit claimed and failed; no game input executed. The
pass hit the windowless-LastWar blocker for the sixty-second
consecutive ticker pass, by the running count in the records
(ticker-0434 at 04:34 PT Nov 19 was the sixty-first; no ticker
record exists for the 05:04 slot on Nov 19, so the count
advances by this pass alone). No batch point passed during
this run window, so missed batches stay 40; next point
07:00 PT Nov 19.

## ROUTE DEVIATION - this pass did NOT honor the 0434 route

This pass did NOT re-read the newest queue-ticker record
(0434) FIRST, before sync and before any claim, and it did
NOT probe the device before claiming a unit. The order actually
run was: AGENTS.md, recording rules and queue design re-read,
then sync, then the PR-list re-read, then token-acquire, then
the harvest unit was claimed, and only then was the device
probed. The 0434 record was read only after the unit had
already failed. The deviation-watch verification therefore
does NOT advance: it stays at ONE honoring pass (0434, the
first). The next pass must keep the honoring order - newest
queue-ticker record first, then sync, then probe before any
claim.

Consequence of the deviation, stated plainly: the harvest
unit harvest-2026-11-19-0203 was claimed before the blocker
was known, spent its first attempt (1 of 3) and closed
failed. The shared completion marker suppresses re-picks of
that unit; the tracker is untouched (failed units leave it
alone), so the harvest regular stays due and the next tick
re-produces it as a fresh unit - which will fail the same way
unless the next pass probes before claiming. This is exactly
the repeat-failure loop the route change exists to stop.

Count correction: the completed unit's summary says "60th
consecutive window loss". That figure was taken from the stale
ticker-0215 count and understates by two. The correct count
is sixty-second (0434 was sixty-first). The unit file is
append-only and is not rewritten; this record is the
correction.

## Unit claimed and failed - harvest-2026-11-19-0203

- Token held 05:52-06:09 PT by ticker-0534 (acquired
  13:52:27Z, released 14:02Z after the completion). Unit
  claimed 13:55:13Z, lease to 14:15:13Z; completed failed
  14:01:23Z, duration 370 seconds.
- Summary as recorded: "Mac mini online but LastWar window
  still absent (60th consecutive window loss); no game input,
  nothing claimed" - see the count correction above.
- Evidence: _records_/2026-11-19/resource-collection/0534-queue-run.md
  (the short unit record; this file is the full process
  record). Stats: target "collect ready resource bubbles
  and Armed Truck loot", achieved "no game input; window
  unreachable", resources_gained none, costs "about 14
  minutes device time, no stamina or items", verified yes,
  blocker_category f.
- No game input was sent in this pass. No Escape, Return or
  Control-Command-F was used; the green zoom button stays
  untouched per the standing lesson. No Touch ID, no password.

## Probe - two computer sessions, blocker unchanged

- Mac mini ONLINE per device.list, last_seen
  2026-11-19T12:25:42Z - UNCHANGED since the 0434 probe: the
  channel has not progressed since about 12:25Z. connection.health
  was NOT called this pass, so no fresh progressAgeSeconds
  reading exists; that is a gap against the 0434 probe, stated
  here rather than filled from stale numbers.
- environment.describe confirms LastWar IS in running_apps
  (com.lastwar.ios), alongside Google Chrome, ChatGPT and
  Finder. Accessibility and screen recording permissions are
  granted. Display 1920x1080. `agent_window.available` is
  false with reason `new_tab_in_existing_window`.
- Session cc-126: activate "Last War" failed (no running app
  matching that name); activate "LastWar" failed
  ax_windows_empty with brought_to_front false; open_app
  "LastWar" outcome_unknown once; observe and screen.snap
  both observation_unavailable; list_windows returned 11
  windows with no LastWar entry.
- Session cc-127 (fresh session, reopened per the retry
  rule): open_app "LastWar" outcome_unknown again; observe
  observation_unavailable again; environment.describe
  re-confirmed LastWar running but windowless; list_windows
  again 11 windows, no LastWar entry; activate "Finder"
  failed geometry_mismatch (origin_delta=256+,
  size_delta=256+, agent_display=false) - the same failure
  0434 measured for Chrome windows. Corroborated again:
  chrome_observes_ok is FALSE and no window is selectable
  on the agent display, not only the LastWar window. The
  control channel itself answers promptly (21 device invokes,
  0 timeouts, 0 node_offline).
- Probe classification: tools/mac_capture_probe.py v1.2.0 on
  the assembled evidence (/tmp/lw-probe-0534.json) returns
  OFF_SCREEN_WINDOW, high confidence, stop_pass yes (exit
  10). Same label as 0434 and the passes before it.
- The recovery stays the same owner step (issue #284): click
  the LastWar Dock icon once (or run
  tools/mac_lastwar_front.sh in Terminal), then re-probe.

## Own PRs first

- VPS route down (SSH Permission denied, see below), so no gh
  check was possible this pass. The open PR list was re-read
  via browser.open on the public pulls page
  (2026-11-19T13:54Z): exactly three open PRs - #711
  (knowledge: fold ticker-1047 pass into 4 profiles, opened
  Nov 12), #708 (records: 2026-11-12, opened Nov 12), #425
  (feat(tools): pre-delivery log gate, opened Nov 8). Same
  three as every pass since Nov 12. None is owned by this
  job; no open PR for records/2026-11-18 or
  records/2026-11-19; no new question addressed to this job
  visible in the fetched text. Limitation, stated plainly:
  the browser.open fetch renders comment bodies only as
  truncated snippets, so the newest-comment check is
  partial, not the full read the 0434 pass got from the
  GitHub connector. Nothing in the visible text asks this
  job anything or shows a conflict on a records PR.
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
  Pool at the 13:52Z stats read: inbox 76, claimed 0, done
  2506. Newest executed closing 2026-11-19T10:26:38Z (the
  0215 mail failed unit), about 3.4 hours before this pass.
  Stalled priority-1: vip-2026-11-18-1800 (about 23h).
- Zombie seeding: none. The most recent done zombie unit (037,
  chain zombie-2026-11-10, finished 2026-11-15T02:35Z) closed
  the chain because the Glacieradon event had ended - no Zombie
  Invasion tab in the Events hub - and the activity metadata
  forbids seeding a fresh chain until a Zombie tab is seen live
  again. No zombie unit sits in inbox or claimed, and none was
  enqueued.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 4, Train Heroes, 11.9 hours left at the 06:03 read,
  day ends 18:00 PT Nov 19. Day 3 Age of Science is now
  definitively closed with its scoring (research completions,
  valor badges, drone component chests, radar release) all
  missed. Day 4 is a hero day: hero EXP, shards, skill medals
  and recruitment tickets score, and the owner spends those
  consumables; radar posture is STACK - complete but do not
  claim. None of it is reachable while the window is down. No
  game unit has executed since ticker-0214 gifts at 02:14 PT
  Nov 17, about fifty-two hours of routine now missed.
  Seventh consecutive VIP day already lost at the 19:00 reset
  Nov 18 (sixth lost day) with the seventh game day now
  running and unreachable; fifth consecutive missed pre-reset
  sweep night (the Nov 18 pair expired unexecuted).

## Delivery

- VPS SSH still Permission denied (publickey), probed 05:54 PT,
  about 160.9 hours into the break (outage since about 12:47 PT
  2026-11-12; owner chose the IONOS console route 2026-11-14
  17:37 PT, about 108 hours ago; no fix yet). Push and PR are
  blocked.
- Delivery PARTIAL: record committed locally on
  ticker-0534-1119-delivery, UNPUSHED, push pending VPS
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
  ticker-0534-1119-delivery (created from main), as the 0434
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
  This pass adds two observations beyond the 0434 record:
  (a) a Finder activate ALSO fails geometry_mismatch, so the
  "no window selectable on the agent display" widening now
  covers Finder as well as Chrome and LastWar; (b) the
  claim-before-probe deviation consumed a harvest attempt
  (1 of 3) on a unit that could not run - the route change
  exists to prevent exactly this, and the deviation-watch
  honoring count stays at ONE.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-0534-1119-delivery, UNPUSHED, push pending VPS
  recovery. No PR opened for records/2026-11-19.
