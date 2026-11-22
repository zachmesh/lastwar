---
title: Queue ticker run failure - game window missing, seventy-fourth consecutive occurrence
created: 2026-11-20T01:16:00Z
modified: 2026-11-20T01:16:00Z
version: 1.0.0
description: Queue ticker 2026-11-19 17:04 PT run failure, LastWar has no window on the Mac mini
status: run-failure
grounded_in:
  - source: _records_/2026-11-19/queue-ticker/1645-queue-run.md re-read during the run (route partially honored - see below)
  - source: _records_/2026-11-19/INDEX.md tail (pr-catchall-1539, pr-integration-1630, knowledge-organization-1632) re-read during the run
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-20T01:06Z
  - source: connection.health and environment.describe on the same device, 2026-11-20T01:07Z and 01:11Z
  - source: computer sessions cc-145 and cc-146, computer.control list_windows, activate and open_app, computer.observe, screen.snap, 2026-11-20T01:08Z to 01:15Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-1704.json, 2026-11-20T01:16Z
  - source: tools/queue.py sync, token-acquire, next, claim, complete and token-release, 2026-11-20T01:04Z to 01:17Z
  - source: GitHub connector open-PR read on zachmesh/lastwar, 2026-11-20T01:17Z
  - source: VPS SSH probe, 2026-11-20T01:05Z
---

# Queue ticker 2026-11-19 17:04 to about 17:24 PT (ticker-1704) - FAILED

One unit claimed and completed as failed. No screen entered, nothing
read or claimed. The blocker is the seventy-fourth consecutive
window-loss occurrence by chain arithmetic (ticker-1645 at 16:45 PT
Nov 19 was the seventy-third; no ticker record exists for any slot
between 16:45 and 17:04 on Nov 19, so the count advances by this
pass alone; the counting basis is retro-owned - chain arithmetic
here, process-failure-record basis elsewhere).

## Route - NOT honored, deviation owned

This pass repeated the claim-before-probe ordering slip: queue sync,
token-acquire, `next` and the claim of vip-2026-11-18-1800 all ran
before the newest queue-ticker record (1645) was read and before
the device probe. The 1645 record was only read after the probe
failed, when the unit was already claimed. The deviation-watch of
fully-honoring passes therefore stays at THREE (0434, 1347, 1404);
this pass joins 1536 as a worked example of the claim-before-probe
cost - one unit attempt burned on a known blocker. The next pass
must keep the full honoring order - newest queue-ticker record
first, then sync, then probe, then token and claim only if the
probe passes.

## Sync and seeding

- Sync: due 23, produced 0, already_queued all 23 (mail, help,
  gifts, harvest, vip, passes, daily-missions, secrets, treasures,
  radar, survivors, trucks, train, training, donations, events,
  arms-race, ghost-ops, star-ceremony, duel-score, scout,
  scout-midday), reaped 0, expired 0. Branch reconcile warning:
  fetch of records/2026-11-19 failed (remote ref missing, issue
  #446), reconcile skipped.
- Zombie seeding skipped: the event ended; chain
  zombie-2026-11-10 was closed by unit 037 on 2026-11-14 (no
  Zombie Invasion tab in the Events hub); no zombie unit sits in
  inbox or claimed; do not seed until the tab is seen live again.

## Own PRs first

- VPS route blocked: ssh to centos@66.179.249.233 returned
  Permission denied (publickey) at about 01:05Z, about 172 hours
  into the outage. The VPS gh CLI check could not run.
- Fallback via the GitHub connector (read-only open-PR list on
  zachmesh/lastwar): exactly three open PRs, all unchanged since
  2026-11-12 - #711 knowledge fold (Owner
  lastwar-knowledge-organizer, head e3c3dfd0, updated
  2026-11-12T20:04:57Z), #708 records 2026-11-12 (Owner
  lastwar-pr-integrator, head 2f59c270, updated
  2026-11-12T20:44:37Z), #425 tools log gate (Owner
  lastwar-tool-developer, head 4f41cdd6, updated
  2026-11-12T19:29:37Z). None is owned by this job, and no open
  PR exists for records/2026-11-19. No new question or numbered
  fix point is addressed to this job.

## Probe - two computer sessions, blocker unchanged

- Mac mini ONLINE per device.list, last_seen
  2026-11-20T00:16:13Z (16:16:13 PST). connection.health: both
  transports healthy, lastResponseAgeSeconds 0 (native) and 0
  (web), progressAgeSeconds 3056 on native (about 51 minutes
  frozen) and 912 on web (about 15 minutes). The native channel
  has not progressed since about 16:12 PT, same anchor as 1645.
- environment.describe confirms LastWar IS in running_apps.
  Accessibility and screen recording permissions are granted.
  Display 1920x1080. `agent_window.available` is false with
  reason `new_tab_in_existing_window`.
- Session cc-145: list_windows returned 0 LastWar windows;
  activate "LastWar" failed ax_windows_empty with
  brought_to_front false; open_app "LastWar" outcome_unknown;
  observe observation_unavailable; list_windows again 0;
  screen.snap observation_unavailable; activate "LastWar"
  again ax_windows_empty after a 20 second wait. Activate
  "Finder" (window 28) failed geometry_mismatch
  (origin_delta 256+, size_delta 256+, agent_display false)
  with the session still pinned to target bundle
  com.lastwar.ios.
- Session cc-146 (fresh session after ending cc-145, third
  window-acquire attempt per the retry rule): activate
  "LastWar" ax_windows_empty again; activate "Finder" again
  geometry_mismatch, session still pinned to
  com.lastwar.ios.
- 15 device invokes in total, all answered promptly, 0
  timeouts, 0 node_offline.
- Probe classification: tools/mac_capture_probe.py v1.2.0 on
  the assembled evidence (/tmp/lw-probe-1704.json) returns
  OFF_SCREEN_WINDOW, high confidence, stop_pass yes (exit
  10). Same label as 1536 and 1645.
- NEW detail vs 1645: not only the LastWar window is
  unbindable - even a Finder window could not be bound in
  either session (geometry_mismatch both times, session
  pinned to com.lastwar.ios). The window-selection layer
  itself is failing, not just the LastWar window. Recovery
  still stands as the one owner step on the Mac mini: click
  the LastWar Dock icon once (or run
  _tools_/mac_lastwar_front.sh in Terminal), then re-probe.

## Unit

- vip-2026-11-18-1800 claimed before the probe and completed
  as failed; the regulars tracker is untouched (failed units
  leave it alone). Attempts now 2 of 3. This is the same stale
  Nov 18 18:00 VIP unit `next` handed out to 1645
  (planned_for 2026-11-19T02:00:00Z, expires
  2026-11-20T02:00:00Z, today 19:00 PT): `next` keeps
  handing out this stale unit while the game is unreachable.
  Queue-pick observation for the retro, no issue filed while
  the VPS gh route is down.

## Standing counts

- No game unit since ticker-0214 gifts Nov 17 02:14 PT
  (about 63 hours missed). Seventh consecutive missed VIP day.
  Tonight's pre-reset sweep pair (chain
  pre-reset-sweep-2026-11-19, 2 pending) still sits in inbox;
  it becomes the fifth consecutive missed sweep night unless
  the window recovers before the 19:00 reset. Duel day 4
  Train Heroes runs to 18:00 PT Nov 19, unreachable.
- Missed batches stay 42 (next point 19:00 PT).
- VPS SSH still Permission denied (publickey), about 172
  hours into the outage; delivery blocked, commit left on
  local records/2026-11-19, no PR. This pass is partial.
