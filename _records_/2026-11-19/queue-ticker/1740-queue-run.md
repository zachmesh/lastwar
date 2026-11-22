---
title: Queue ticker run failure - game window missing, seventy-fifth consecutive occurrence
created: 2026-11-20T01:49:00Z
modified: 2026-11-20T01:49:00Z
version: 1.0.0
description: Queue ticker 2026-11-19 17:40 PT run failure, LastWar has no window on the Mac mini
status: run-failure
grounded_in:
  - source: _records_/2026-11-19/queue-ticker/1704-queue-run.md read during the run (route partially honored - see below)
  - source: _records_/2026-11-19/INDEX.md tail (knowledge-organization-1732, queue-planning-1640) read during the run
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-20T01:40Z
  - source: connection.health and environment.describe on the same device, 2026-11-20T01:41Z and 01:47Z
  - source: computer session cc-147, computer.control list_windows, activate and open_app, computer.observe, 2026-11-20T01:42Z to 01:48Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-1740.json, 2026-11-20T01:48Z
  - source: tools/queue.py sync, token-acquire and token-release, 2026-11-20T01:40Z to 01:49Z
  - source: GitHub connector open-PR read on zachmesh/lastwar, 2026-11-20T01:43Z
  - source: VPS SSH probe, 2026-11-20T01:41Z
---

# Queue ticker 2026-11-19 17:40 to about 17:50 PT (ticker-1740) - FAILED

No unit claimed, no unit completed. No screen entered, nothing
read or claimed. The blocker is the seventy-fifth consecutive
window-loss occurrence by chain arithmetic (ticker-1704 at 17:04 PT
Nov 19 was the seventy-fourth; no ticker record exists for any slot
between 17:04 and 17:40 on Nov 19, so the count advances by this
pass alone; the counting basis is retro-owned - chain arithmetic
here, process-failure-record basis elsewhere).

## Route - PARTIALLY honored, deviation owned

This pass repeated the token-before-probe ordering slip: queue sync
and token-acquire ran before the newest queue-ticker record (1704)
was read and before the device probe. The material part was honored
this time - the probe ran before any claim, `next` was never called,
and NO unit was claimed, so no unit attempt was burned (the stale
vip-2026-11-18-1800 unit stays in inbox at attempts 2 of 3). The
deviation-watch of fully-honoring passes therefore stays at THREE
(0434, 1347, 1404); this pass joins 1645 as partially honoring
(probe before claim, record-first and probe-before-token not). The
next pass must read the newest queue-ticker record first, then sync,
then probe, then token and claim only if the probe passes.

## Sync and seeding

- Sync: due 23, produced 0, already_queued all 23 (mail, help,
  gifts, harvest, vip, passes, daily-missions, secrets, treasures,
  radar, survivors, trucks, train, training, donations, events,
  arms-race, ghost-ops, star-ceremony, duel-score, scout,
  scout-midday), reaped 0, expired 0. Completion markers reaped:
  vip-2026-11-18-1800. Branch reconcile warning: fetch of
  records/2026-11-19 failed (remote ref missing, issue #446),
  reconcile skipped.
- Zombie seeding skipped: the event ended; chain
  zombie-2026-11-10 was closed by unit 037 on 2026-11-14 (no
  Zombie Invasion tab in the Events hub); no zombie unit sits in
  inbox or claimed; do not seed until the tab is seen live again.

## Own PRs first

- VPS route blocked: ssh to centos@66.179.249.233 returned
  Permission denied (publickey) at about 01:41Z, about 172 hours
  into the outage. The VPS gh CLI check could not run.
- Fallback via the GitHub connector (read-only open-PR list on
  zachmesh/lastwar): exactly three open PRs, all unchanged since
  2026-11-12 - #711 knowledge fold (Owner
  lastwar-knowledge-organizer, head e3c3dfd0, updated
  2026-11-12T20:04:57Z), #708 records 2026-11-12 (Owner
  lastwar-pr-integrator, head 2f59c270, updated
  2026-11-12T20:44:37Z), #425 tools log gate (Owner
  lastwar-tool-developer, head 4f41cdd6, updated
  2026-11-12T19:29:37Z). Updated timestamps identical to the
  ticker-1704 read about 35 minutes earlier, so no new comment
  or review can have landed. None is owned by this job, and no
  open PR exists for records/2026-11-19. No new question or
  numbered fix point is addressed to this job.

## Probe - one computer session, blocker unchanged

- Mac mini ONLINE per device.list, last_seen
  2026-11-20T00:16:13Z (16:16:13 PST, about 84 minutes stale at
  probe time). connection.health: both transports healthy,
  lastResponseAgeSeconds 0 (native) and 8 (web),
  progressAgeSeconds 5404 on native (about 90 minutes frozen)
  and 3260 on web (about 54 minutes). The native channel has
  not progressed since about 16:16 PT, the same anchor as 1645
  and 1704; the age grew only because the clock moved.
- environment.describe confirms LastWar IS in running_apps.
  Accessibility and screen recording permissions are granted.
  Display 1920x1080. `agent_window.available` is false with
  reason `new_tab_in_existing_window`.
- Session cc-147: list_windows returned 11 windows and 0
  LastWar windows; activate "LastWar" failed ax_windows_empty
  with brought_to_front false; open_app "LastWar"
  outcome_unknown; list_windows again 11 windows, still 0
  LastWar; activate "Finder" (window 28) failed
  geometry_mismatch (origin_delta 256+, size_delta 256+,
  agent_display false) with the session still pinned to target
  bundle com.lastwar.ios; observe observation_unavailable.
- 11 device invokes in total, all answered promptly, 0
  timeouts, 0 node_offline.
- Probe classification: tools/mac_capture_probe.py v1.2.0 on
  the assembled evidence (/tmp/lw-probe-1740.json) returns
  OFF_SCREEN_WINDOW, high confidence, stop_pass yes (exit
  10). Same label as 1536, 1645 and 1704.
- Detail vs 1704: window enumeration itself works this pass
  (a full 11-window list, twice), so the failure is narrower
  than "no windows at all" - LastWar exposes no window and no
  listed window can be bound (geometry_mismatch on the Finder
  window). The window-selection layer is still the failing
  layer, not just the LastWar window. Recovery still stands as
  the one owner step on the Mac mini: click the LastWar Dock
  icon once (or run _tools_/mac_lastwar_front.sh in Terminal),
  then re-probe.

## Unit

- None claimed, none completed. `next` was never called, so the
  queue-pick observation from 1645/1704 (the stale
  vip-2026-11-18-1800 unit being handed out while the game is
  unreachable) was not re-tested this pass; the unit stays in
  inbox at attempts 2 of 3, expiring 2026-11-20T02:00:00Z
  (19:00 PT Nov 19). Tracker untouched.

## Standing counts

- No game unit since ticker-0214 gifts Nov 17 02:14 PT
  (about 63.5 hours missed). Seventh consecutive missed VIP day.
  Tonight's pre-reset sweep pair (chain
  pre-reset-sweep-2026-11-19, 2 pending) still sits in inbox;
  it misses unless the window recovers before the 19:00 reset
  (about 70 minutes away at pass end). Sweep-night count
  discrepancy carried as retro flag (k) from the 1732 record -
  this run adopts neither figure. Duel day 4 Train Heroes runs
  to 18:00 PT Nov 19, unreachable.
- Missed batches stay 42 (next point 19:00 PT). Contradiction
  with MEMORY.md 43 carried as retro flag (i).
- VPS SSH still Permission denied (publickey), about 172
  hours into the outage; delivery blocked, commit left on
  local records/2026-11-19, no PR. This pass is partial.
