---
title: Queue ticker process failure - game window missing, fifty-first consecutive occurrence
created: 2026-11-19T02:22:00Z
modified: 2026-11-19T02:22:00Z
version: 1.0.0
description: Queue ticker 2026-11-18 18:04 PT process failure, LastWar has no window on the Mac mini
status: process-failure
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-19T02:05Z
  - source: computer.session cc-105, cc-106, cc-107, computer.control list_windows, activate and open_app, computer.observe, environment.describe, 2026-11-19T02:09Z to 02:21Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-1804.json, 2026-11-19T02:21Z
  - source: tools/duel.py --json, 2026-11-19T02:18Z
  - source: _records_/2026-11-18/queue-ticker/1734-process-failure.md read from the live mirror AFTER sync and claim (route change missed before acting, see below)
  - source: VPS SSH probe, 2026-11-19T02:05Z
  - source: GitHub connector list_pull_requests on zachmesh/lastwar, 2026-11-19T02:21Z
---

# Queue ticker 2026-11-18 18:04 to about 18:23 PT (ticker-1804) - PROCESS FAILURE

No game unit executed: the pass hit the windowless-LastWar
blocker for the fifty-first consecutive ticker pass, by the
running count in the records (ticker-1734 at 17:42 PT was the
fiftieth). The 18:00 reset passed during this run window, so
the pre-reset sweep pair expired and duel day 3 closed. No
batch point passed during this run window, so missed batches
stay 37; next point 19:00 PT.

## Deviation - unit claimed before the route change was re-read, then released

This pass did NOT re-read the newest queue-ticker record before
sync and claim: it ran sync, token-acquire and `next`, and
claimed gifts-2026-11-18-1430 before reading the 1734 record
and its ticker-0534 route change (claim no unit until the
window is recovered). The claim was caught before any game
input and corrected in the same pass: `queue.py release`
returned gifts-2026-11-18-1430 to inbox un-executed, claim
fields cleared, attempts 1 of 3. No unit was closed failed on
the deviation. The deviation restarts the route-change
honoring watch at zero - the 1504, 1604, 1734 streak of three
consecutive honoring passes is broken, and the next pass that
honors restarts the count at one. The standing fix is to read
the newest queue-ticker record FIRST, before sync, in every
pass.

## Probe - three computer sessions, blocker unchanged, channel wedged on every window

- Mac mini ONLINE per device.list, but its `last_seen` is still
  FROZEN at 2026-11-19T00:24:09Z - the same value the 1604 and
  1734 passes read, now about 2 hours stale - while all 24
  device invokes in this pass returned promptly with 0
  timeouts. The gateway timestamp is frozen, the channel is
  NOT stalled. This is not the probe v1.1.0 channel-stall form
  (every invoke timing out); no connection.repair was run this
  pass. No evidence the owner has done the Dock-icon step: the
  window is still missing.
- environment.describe confirms LastWar IS in running_apps,
  alongside Google Chrome, ChatGPT and Finder. Accessibility and
  screen recording permissions are granted. Display 1920x1080.
  `agent_window.available` is false with reason
  `new_tab_in_existing_window`, the twenty-second pass in a row.
- Session cc-105: open_app "LastWar" outcome_unknown (action
  400CB8C3-82C1-4A76-BE04-25658030AC86); observe
  observation_unavailable; activate LastWar failed
  ax_windows_empty with stale_observation; list_windows
  returned 11 windows with no LastWar entry; screen.snap
  observation_unavailable; activate Finder window 28 failed
  geometry_mismatch (origin_delta 256+, size_delta 256+,
  agent_display false); open_app "Finder" failed with the same
  geometry_mismatch; menu Quit LastWar refused for want of a
  fresh observation. Session cc-106 (fresh): open_app
  "LastWar" outcome_unknown again (action
  685B9E5D-B380-4A8C-8EAE-631D0A13DEAE); activate LastWar again
  ax_windows_empty; environment.describe refresh and a fresh
  list_windows still showed 11 windows, no LastWar. Session
  cc-107: list_windows with app "LastWar" returned 0 windows;
  open_app "Google Chrome" refused (two running instances);
  activate Chrome window 125 failed geometry_mismatch, the
  same error as Finder - the control channel cannot bind ANY
  window right now, not just LastWar. The pass stops here on
  the window, not on the token. Token held 18:09-18:22 PT,
  released.
- Methodology note, stated plainly: no game input was sent in
  this pass. No Escape, Return or Control-Command-F was used;
  the green zoom button stays untouched per the standing
  lesson. No Touch ID, no password.
- Probe classification: tools/mac_capture_probe.py v1.2.0 on the
  assembled evidence (/tmp/lw-probe-1804.json) returns
  OFF_SCREEN_WINDOW, high confidence, stop_pass yes. Same label
  as the 0616, 0733, 1010, 1133, 1248, 1354, 1504, 1604 and
  1734 passes. The only missing probe steps are the View-menu
  inspect (Enter/Exit Full Screen), unreachable without a bound
  window, and one control observation of a Chrome window. The
  recovery stays the same owner step (issue #284): click the
  LastWar Dock icon once (or run tools/mac_lastwar_front.sh in
  Terminal), then re-probe.

## Own PRs first

- VPS route down (SSH Permission denied, see below), so no fresh
  gh check was possible this pass. The public PR list was
  re-read via the GitHub connector (list_pull_requests,
  2026-11-19T02:21Z): exactly three open PRs - #711
  (knowledge, Owner lastwar-knowledge-organizer, head e3c3dfd0,
  updated 2026-11-12T20:04:57Z), #708 (records 2026-11-12,
  Owner lastwar-pr-integrator, head 2f59c270, updated
  2026-11-12T20:44:37Z), #425 (tooling, Owner
  lastwar-tool-developer, head 4f41cdd6, updated
  2026-11-12T19:29:37Z). Same three as the 0004, 0034, 0134,
  0243, 0353, 0500, 0616, 0733, 0834, 1010, 1133, 1248, 1354,
  1504, 1604 and 1734 passes, heads and updated_at unchanged
  since Nov 12 (so no new comments on any of them). None is
  owned by this job; no open PR for records/2026-11-17 or
  records/2026-11-18. No question addressed to this job,
  nothing to fix.

## Sync and seeding

- Sync: reaped 0, expired 11, due 22, produced 0, already queued
  22 (mail, help, gifts, harvest, vip, passes, daily-missions,
  secrets, treasures, radar, survivors, trucks, train, training,
  donations, events, arms-race, star-ceremony, duel-score,
  scout, scout-midday). Branch reconcile skipped with a warning:
  fetch of records/2026-11-18 failed (remote ref missing),
  issue #446. Pool at the 18:22 read: inbox 67, claimed 0, done
  2461. The 11 expired units include the pre-reset sweep pair
  (zero-sweep-2026-11-18-1630 and -1730) and vip-2026-11-17-1800.
  The sweep pair's 18:00 PT expiry passed during this pass, so
  tonight is the fifth consecutive missed pre-reset night
  (Nov 14-18), now confirmed rather than conditional.
  vip-2026-11-18-1800 stays in inbox (priority 1, expires
  2026-11-20T02:00:00Z) for the next tick. No unit claimed, no
  unit completed.
- Zombie seeding: none. The most recent done zombie unit (037,
  chain zombie-2026-11-10, finished 2026-11-15T02:35Z) closed
  the chain because the Glacieradon event had ended - no Zombie
  Invasion tab in the Events hub - and the activity metadata
  forbids seeding a fresh chain until a Zombie tab is seen live
  again. No zombie unit sits in inbox or claimed, and none was
  enqueued.

## Duel posture (read from tools/duel.py, not from the screen)

- The 18:00 reset rolled the duel to day 4, Train Heroes, 23.7
  hours left at the 18:18 read, day ends 18:00 PT Nov 19. Day 3
  Age of Science is now definitively closed with its scoring
  (research completions, valor badges, drone component chests,
  radar release) all missed. Day 4 is a hero day: hero EXP,
  shards, skill medals and recruitment tickets score, and the
  owner spends those consumables; radar posture is STACK -
  complete but do not claim. None of it is reachable while the
  window is down. No game unit has executed since ticker-0214
  gifts at 02:14 PT Nov 17, about forty hours of routine now
  missed.

## Delivery

- VPS SSH still Permission denied (publickey), probed 18:05 PT,
  about 149.6 hours into the break (outage since about 12:47 PT
  2026-11-12; owner chose the IONOS console route 2026-11-14
  17:37 PT, about 96.8 hours ago; no fix yet). Push and PR are
  blocked.
- Delivery PARTIAL: record committed locally on
  ticker-1804-1118-delivery (based on ticker-1734-1118-delivery,
  so the pushed chain stays linear), UNPUSHED, push pending VPS
  recovery. No PR opened for records/2026-11-18. No Slack sync.
  Chat report owed per the ticker rule (previous pass also
  access-failed); this pass's final message carries it.
- The 19:00 batch point has not passed; missed batches stay 37.

## Standing git status anomaly in the live mirror (persists)

- `git status` in the live mirror still reports a large changed
  set (modified activity files, deleted inbox unit files, deleted
  tools entries that exist on disk) while the queue tools run
  against the files on disk. The live tree sits on branch
  work/ops-execution-records, another job's in-flight state; no
  commit was attempted from this tree. The delivery commit goes
  through a temporary worktree on ticker-1804-1118-delivery,
  based on ticker-1734-1118-delivery, as in the previous passes.
  The live mirror's _records_/2026-11-18/ tree is untracked
  there, so the delivery branch carries only this job's ticker
  sections of the day INDEX, not the other jobs' sections.
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
  This pass adds one new observation beyond the 1734 record:
  two open_app outcome_unknown results in two fresh sessions,
  and the geometry_mismatch binding failure reproduced on a
  second app family (Finder open_app, after Chrome activate).
- The 1704 slot gap (no record, no branch, no log entry) is a
  second owed item for the retro: the scheduler fired a tick
  that left no trace at all.
- Blocker write into a shared entry-route note (recording-rules
  Device access or queue design section 11, R2) - tier 2, cannot
  ride this tier-1 records commit; owed to the retro / the
  tooling issue above.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-1804-1118-delivery, UNPUSHED, push pending VPS recovery.
  No PR opened for records/2026-11-18.
