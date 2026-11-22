---
title: Queue ticker process failure - game window missing, fiftieth consecutive occurrence
created: 2026-11-19T01:49:00Z
modified: 2026-11-19T01:49:00Z
version: 1.0.0
description: Queue ticker 2026-11-18 17:34 PT process failure, LastWar has no window on the Mac mini
status: process-failure
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-19T01:44Z
  - source: computer.session cc-104, computer.control list_windows, activate and open_app, computer.observe, environment.describe, 2026-11-19T01:45Z to 01:47Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-1734.json, 2026-11-19T01:48Z
  - source: tools/duel.py --json, 2026-11-19T01:44Z
  - source: _records_/2026-11-18/queue-ticker/1604-process-failure.md read from the live mirror BEFORE sync (route change honored, see below)
  - source: VPS SSH probe, 2026-11-19T01:42Z
  - source: GitHub connector list_pull_requests on zachmesh/lastwar, 2026-11-19T01:44Z
---

# Queue ticker 2026-11-18 17:42 to about 17:49 PT (ticker-1734) - PROCESS FAILURE

No unit was claimed and no game unit executed: the pass hit the
windowless-LastWar blocker for the fiftieth consecutive ticker
pass, by the running count in the records (ticker-1604 at 16:25 PT
was the forty-ninth). This run's trigger_reason was
dependency_probe; the 17:34 tick fired late (pass started 17:42
PT). No batch point passed during this run window, so missed
batches stay 37; next point 19:00 PT.

## The 17:04 slot left no record - ordinal carries a caveat

The 17:04 tick produced no record file, no delivery branch
(no ticker-1704-1118-delivery in local or remote branches) and
no action-log entry for 2026-11-18. The pr-catchall-1739 pass
(17:39-17:47 PT, running alongside this one) independently
confirmed the same gap. The fiftieth ordinal therefore counts
recorded passes only; the 1704 slot stays unaccounted, the same
class of gap as the still-unknown 2204 slot, and the
counting-label contradiction flagged by the knowledge-organization
0032 pass (ticker-2104 and ticker-2134 both recorded as the 31st)
persists for the retro.

## Route change honored - third consecutive honoring pass

This pass re-read the newest queue-ticker record (1604) BEFORE
sync, and honored the ticker-0534 route change: claim no unit
until the window is recovered. No unit was claimed, so no unit
was closed failed on a deviation. This is the third consecutive
honoring pass (1504, 1604, 1734); the route change was already
verified at 1604. The probe itself was still required by the
retry rule and sent no game input.

## Probe - one computer session, blocker unchanged, one new shade

- Mac mini ONLINE per device.list, but its `last_seen` is FROZEN
  at 2026-11-19T00:24:09Z - the same value the 1604 pass read
  about 83 minutes earlier - while all 9 device invokes in this
  pass returned promptly with 0 timeouts. New shade: the gateway
  timestamp is frozen, the channel is NOT stalled. This is not
  the probe v1.1.0 channel-stall form (every invoke timing out);
  no connection.repair was run this pass. No evidence the owner
  has done the Dock-icon step: the window is still missing.
- environment.describe confirms LastWar IS in running_apps,
  alongside Google Chrome, ChatGPT and Finder. Accessibility and
  screen recording permissions are granted. Display 1920x1080.
  `agent_window.available` is false with reason
  `new_tab_in_existing_window`, the twenty-first pass in a row.
- Session cc-104: list_windows returned 11 windows with no
  LastWar entry; list_windows with app "LastWar" returned 0
  windows; activate LastWar failed ax_windows_empty with
  stale_observation; open_app "LastWar" outcome_unknown
  (action 39493E86-A3AF-4D1B-B492-74FA0092511B), and a re-list
  after a 20-second wait still showed 0 LastWar windows;
  computer.observe observation_unavailable ("No current target
  window can be observed."). The control channel stays wedged
  on the stale LastWar target and cannot bind ANY window,
  confirming ticker-1010's, ticker-1133's, ticker-1248's,
  ticker-1354's, ticker-1504's and ticker-1604's symptom in the
  same session. The pass stops here on the window, not on the
  token. Token held 17:45-17:47 PT, released.
- Methodology note, stated plainly: no game input was sent in
  this pass. No Escape, Return or Control-Command-F was used;
  the green zoom button stays untouched per the standing
  lesson. No Touch ID, no password.
- Probe classification: tools/mac_capture_probe.py v1.2.0 on the
  assembled evidence (/tmp/lw-probe-1734.json) returns
  OFF_SCREEN_WINDOW, high confidence, stop_pass yes. Same label
  as the 0616, 0733, 1010, 1133, 1248, 1354, 1504 and 1604
  passes. The only missing probe steps are the View-menu inspect
  (Enter/Exit Full Screen), unreachable without a bound window,
  and one control observation of a Chrome window. The recovery
  stays the same owner step (issue #284): click the LastWar Dock
  icon once (or run tools/mac_lastwar_front.sh in Terminal), then
  re-probe.

## Own PRs first

- VPS route down (SSH Permission denied, see below), so no fresh
  gh check was possible this pass. The public PR list was
  re-read via the GitHub connector (list_pull_requests,
  2026-11-19T01:44Z): exactly three open PRs - #711
  (knowledge, Owner lastwar-knowledge-organizer, head e3c3dfd0,
  updated 2026-11-12T20:04:57Z), #708 (records 2026-11-12,
  Owner lastwar-pr-integrator, head 2f59c270, updated
  2026-11-12T20:44:37Z), #425 (tooling, Owner
  lastwar-tool-developer, head 4f41cdd6, updated
  2026-11-12T19:29:37Z). Same three as the 0004, 0034, 0134,
  0243, 0353, 0500, 0616, 0733, 0834, 1010, 1133, 1248, 1354,
  1504 and 1604 passes, heads and updated_at unchanged since
  Nov 12 (so no new comments on any of them). None is owned by
  this job; no open PR for records/2026-11-17 or
  records/2026-11-18. No question addressed to this job, nothing
  to fix.

## Sync and seeding

- Sync: reaped 0, expired 0, due 22, produced 0, already queued
  22 (mail, help, gifts, harvest, vip, passes, daily-missions,
  secrets, treasures, radar, survivors, trucks, train, training,
  donations, events, arms-race, star-ceremony, duel-score,
  scout, scout-midday). Branch reconcile skipped with a warning:
  fetch of records/2026-11-18 failed (remote ref missing),
  issue #446. Pool at the 17:47 read: inbox 78, claimed 0, done
  2450, upcoming 55. Newest executed closing
  2026-11-18T19:42:37Z (11:42 PT), stale over 3 hours without an
  executed closing. No unit claimed, no unit completed.
- Zombie seeding: none. The most recent done zombie unit (037,
  chain zombie-2026-11-10, finished 2026-11-15T02:35Z) closed
  the chain because the Glacieradon event had ended - no Zombie
  Invasion tab in the Events hub - and the activity metadata
  forbids seeding a fresh chain until a Zombie tab is seen live
  again. No zombie unit sits in inbox or claimed, and none was
  enqueued.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 3, Age of Science, 0.3 hours left at the 17:44 read,
  day ends 18:00 PT Nov 18. Research completions land today;
  valor badges are spent only inside today (owner decision);
  drone component chests score only today (owner inventory);
  radar posture: RELEASE - claims score again today, release
  the stack built on Day 2.
- The day-3 scoring (research, valor badges, drone chests, radar
  release) is all missed while the window is down. No game unit
  has executed since ticker-0214 gifts at 02:14 PT Nov 17,
  about thirty-nine and a half hours of routine now missed.
  Tonight's pre-reset sweep pair is present in inbox
  (zero-sweep-2026-11-18-1630 and -1730, both expire 18:00 PT);
  unless the window returns in the next ~11 minutes, tonight is
  the fifth consecutive missed pre-reset night (Nov 14-18).

## Delivery

- VPS SSH still Permission denied (publickey), probed 17:42 PT,
  about 149.0 hours into the break (outage since about 12:47 PT
  2026-11-12; owner chose the IONOS console route 2026-11-14
  17:37 PT, about 96.2 hours ago; no fix yet). Push and PR are
  blocked.
- Delivery PARTIAL: record committed locally on
  ticker-1734-1118-delivery (based on ticker-1604-1118-delivery,
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
  through a temporary worktree on ticker-1734-1118-delivery,
  based on ticker-1604-1118-delivery, as in the previous passes.
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
  This pass adds one new observation beyond the 1604 record:
  device.list last_seen is now frozen (~83 min stale) while
  invokes still return promptly - a gateway-timestamp shade,
  not a channel stall.
- The 1704 slot gap (no record, no branch, no log entry) is a
  second owed item for the retro: the scheduler fired a tick
  that left no trace at all.
- Blocker write into a shared entry-route note (recording-rules
  Device access or queue design section 11, R2) - tier 2, cannot
  ride this tier-1 records commit; owed to the retro / the
  tooling issue above.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-1734-1118-delivery, UNPUSHED, push pending VPS recovery.
  No PR opened for records/2026-11-18.
