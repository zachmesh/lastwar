---
title: Queue ticker process failure - game window missing, forty-ninth consecutive occurrence
created: 2026-11-19T00:36:00Z
modified: 2026-11-19T00:36:00Z
version: 1.0.0
description: Queue ticker 2026-11-18 16:04 PT process failure, LastWar has no window on the Mac mini
status: process-failure
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-19T00:25Z
  - source: computer.session cc-103, computer.control list_windows, activate and open_app, computer.observe, environment.describe, 2026-11-19T00:28Z to 00:33Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-1604.json, 2026-11-19T00:33Z
  - source: tools/duel.py --json, 2026-11-19T00:28Z
  - source: _records_/2026-11-18/queue-ticker/1504-process-failure.md read from the live mirror BEFORE sync (route change honored, see below)
  - source: VPS SSH probe, 2026-11-19T00:26Z
  - source: GitHub connector list_pull_requests on zachmesh/lastwar, 2026-11-19T00:33Z
---

# Queue ticker 2026-11-18 16:25 to about 16:36 PT (ticker-1604) - PROCESS FAILURE

No unit was claimed and no game unit executed: the pass hit the
windowless-LastWar blocker for the forty-ninth consecutive ticker
pass, by the running count in the records (ticker-1504 at 15:11 PT
was the forty-eighth). This run's trigger_reason was
dependency_probe; the 16:04 tick fired late (pass started 16:25
PT). No batch point passed during this run window, so missed
batches stay 37; next point 19:00 PT.

## Route change VERIFIED - second consecutive honoring pass

This pass re-read the newest queue-ticker record (1504) BEFORE
sync, and honored the ticker-0534 route change: claim no unit
until the window is recovered. No unit was claimed, so no unit
was closed failed on a deviation. This is the second consecutive
honoring pass (1504, 1604) since the 1354 deviation restarted
the watch at zero an eighth time, so the route change now counts
as verified. The probe itself was still required by the retry
rule and sent no game input.

## Probe - one computer session, blocker unchanged

- Mac mini ONLINE per device.list (last_seen 2026-11-19T00:24:09Z,
  about 1 minute before the pass). No evidence the owner has
  done the Dock-icon step: the window is still missing.
- environment.describe confirms LastWar IS in running_apps,
  alongside Google Chrome, ChatGPT and Finder. Accessibility and
  screen recording permissions are granted. Display 1920x1080.
  `agent_window.available` is false with reason
  `new_tab_in_existing_window`, the twentieth pass in a row.
  All 9 device invokes in this pass that completed returned
  promptly; the channel is not stalled. No connection.repair was
  run this pass.
- Session cc-103: list_windows returned 11 windows with no
  LastWar entry; list_windows with app "LastWar" returned 0
  windows; activate LastWar failed ax_windows_empty with
  stale_observation; open_app "LastWar" outcome_unknown
  (action 656750F9-74F8-4F7F-8609-5F32B4C62B71), and a re-list
  after a 20-second wait still showed 11 windows, no LastWar;
  computer.observe observation_unavailable ("No current target
  window can be observed."). The control channel stays wedged
  on the stale LastWar target and cannot bind ANY window,
  confirming ticker-1010's, ticker-1133's, ticker-1248's,
  ticker-1354's and ticker-1504's symptom in the same session.
  The pass stops here on the window, not on the token. Token
  acquired and released 16:33 PT (no other pass held it).
- Methodology note, stated plainly: no game input was sent in
  this pass. No Escape, Return or Control-Command-F was used;
  the green zoom button stays untouched per the standing
  lesson. No Touch ID, no password.
- Probe classification: tools/mac_capture_probe.py v1.2.0 on the
  assembled evidence (/tmp/lw-probe-1604.json) returns
  OFF_SCREEN_WINDOW, high confidence, stop_pass yes. Same label
  as the 0616, 0733, 1010, 1133, 1248, 1354 and 1504 passes. The
  only missing probe steps are the View-menu inspect (Enter/Exit
  Full Screen), unreachable without a bound window, and one
  control observation of a Chrome window. The recovery stays
  the same owner step (issue #284): click the LastWar Dock icon
  once (or run tools/mac_lastwar_front.sh in Terminal), then
  re-probe.

## Own PRs first

- VPS route down (SSH Permission denied, see below), so no fresh
  gh check was possible this pass. The public PR list was
  re-read via the GitHub connector (list_pull_requests,
  2026-11-19T00:33Z): exactly three open PRs - #711
  (knowledge, Owner lastwar-knowledge-organizer, head e3c3dfd0,
  updated 2026-11-12T20:04:57Z), #708 (records 2026-11-12,
  Owner lastwar-pr-integrator, head 2f59c270, updated
  2026-11-12T20:44:37Z), #425 (tooling, Owner
  lastwar-tool-developer, head 4f41cdd6, updated
  2026-11-12T19:29:37Z). Same three as the 0004, 0034, 0134,
  0243, 0353, 0500, 0616, 0733, 0834, 1010, 1133, 1248, 1354
  and 1504 passes, heads and updated_at unchanged since Nov 12
  (so no new comments on any of them). None is owned by this
  job; no open PR for records/2026-11-17 or records/2026-11-18.
  No question addressed to this job, nothing to fix.

## Sync and seeding

- Sync: reaped 0, expired 0, due 22, produced 0, already queued
  22 (mail, help, gifts, harvest, vip, passes, daily-missions,
  secrets, treasures, radar, survivors, trucks, train, training,
  donations, events, arms-race, star-ceremony, duel-score,
  scout, scout-midday). Pool: inbox 78, claimed 0, done 2450.
  Stats: newest executed closing 2026-11-18T19:42:37Z (11:42
  PT), stale over 3 hours without an executed closing.
- Zombie seeding: none. The most recent done zombie unit (037,
  chain zombie-2026-11-10, finished 2026-11-15T02:35Z) closed
  the chain because the Glacieradon event had ended - no Zombie
  Invasion tab in the Events hub - and the activity metadata
  forbids seeding a fresh chain until a Zombie tab is seen live
  again. No zombie unit sits in inbox or claimed, and none was
  enqueued.
- Duel day 3 Age of Science ends 18:00 PT (about 1.4 hours left
  at this pass's close); radar posture RELEASE; day-3 scoring
  (research completions, valor badges, drone component chests,
  radar release) all missed again. No game unit since
  ticker-0214 gifts 02:14 PT Nov 17, about thirty-eight and a
  third hours missed.
- Tonight's pre-reset sweep pair is present in inbox
  (zero-sweep-2026-11-18-1630, not_before 16:30 PT, and
  -1730, not_before 17:30 PT; both expire 18:00 PT per their
  files). The first sweep becomes actionable inside this pass's
  window, but no window exists to run it; unless the window
  returns before 18:00 PT, tonight is the fifth consecutive
  missed pre-reset night.

## VPS and delivery

- VPS SSH still Permission denied (publickey) at 16:26 PT,
  about 147.8 hours into the outage (since 2026-11-12 about
  12:47 PT); the owner-selected IONOS console recovery
  (2026-11-14 17:37 PT) still not landed about 4 days later.
  The bundle push attempt failed on the same error (see the
  action log entry).
- Record committed locally only on ticker-1604-1118-delivery
  (based on ticker-1504-1118-delivery, so the pushed chain stays
  linear), UNPUSHED, push pending VPS recovery. No PR for
  records/2026-11-18 exists. A mirror copy of this record and
  its INDEX section live in the local checkout only.

## Notes for the retro

- The counting-label contradiction the knowledge-organization
  0032 pass flagged persists for the retro: ticker-2104 and
  ticker-2134 both recorded as the 31st, and the 2204 slot is
  still unknown. The 1432 pass additionally flagged a
  discrepancy between three honoring passes per the 1232
  carry-forward and two per the 1248/1240/1340/1504 records;
  this pass resolves the honoring count at two consecutive
  (1504, 1604) and verifies the route change - the carry-forward
  figure stays flagged, not adopted.
