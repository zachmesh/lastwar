---
title: Queue ticker run failure - game window missing, seventy-seventh consecutive occurrence
created: 2026-11-20T03:37:00Z
modified: 2026-11-20T03:37:00Z
version: 1.0.0
description: Queue ticker 2026-11-19 19:26 PT run failure, LastWar has no window on the Mac mini
status: run-failure
grounded_in:
  - source: _records_/2026-11-19/queue-ticker/1740-queue-run.md read during the run (main worktree copy)
  - source: records/2026-11-19 branch queue-ticker/1818-queue-run.md (commit 6d19a8bc20) read during the run - the newest ticker record, lives only on the branch
  - source: _records_/2026-11-19/INDEX.md tail read during the run
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-20T03:27Z to 03:29Z
  - source: connection.health and environment.describe on the same device, 2026-11-20T03:29Z
  - source: computer session cc-149, computer.control list_windows, computer.observe, 2026-11-20T03:30Z to 03:33Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-1926.json, 2026-11-20T03:33Z
  - source: tools/queue.py sync, 2026-11-20T03:26Z
  - source: GitHub connector open-PR read on zachmesh/lastwar, 2026-11-20T03:28Z
  - source: VPS SSH probe, 2026-11-20T03:27Z
---

# Queue ticker 2026-11-19 19:26 to about 19:40 PT (ticker-1926) - FAILED

No unit claimed, no unit completed. No screen entered, nothing
read or claimed. The blocker is the seventy-seventh consecutive
window-loss occurrence by chain arithmetic (ticker-1818 at 18:18 PT
Nov 19 was the seventy-sixth; no ticker record exists for any slot
between 18:18 and 19:26 on Nov 19, so the count advances by this
pass alone; the counting basis is retro-owned - chain arithmetic
here, process-failure-record basis elsewhere).

## Route - PARTIALLY honored, deviation owned

This pass repeated the token-before-probe ordering slip: queue sync
ran before the newest queue-ticker record was read. The material
part was honored - the probe ran before any token or claim, the
token was never acquired, `next` was never called, and NO unit
was claimed, so no unit attempt was burned (vip-2026-11-19-1800
stays in inbox at attempts 0 of 3). The deviation-watch of
fully-honoring passes therefore stays at THREE (0434, 1347, 1404);
this pass joins 1645 and 1740 as partially honoring. The next pass
must read the newest queue-ticker record first - checking BOTH the
main worktree AND the records/2026-11-19 branch, since the 1818
record lives only on the branch - then sync, then probe, then token
and claim only if the probe passes.

## Sync and seeding

- Sync: due 23, produced 0, already_queued all 23 (mail, help,
  gifts, harvest, vip, passes, daily-missions, secrets, treasures,
  radar, survivors, trucks, train, training, donations, events,
  arms-race, ghost-ops, star-ceremony, duel-score, scout,
  scout-midday), reaped 0, expired 5 (events, passes, secrets,
  treasures and trucks-2026-11-19-1457, the 14:57 slot, window
  ended 02:57Z). Branch reconcile warning: fetch of
  records/2026-11-19 failed (remote ref missing, issue #446),
  reconcile skipped.
- Zombie seeding skipped: the event ended at about the 19:00
  reset on 2026-10-30; chain zombie-2026-10-28 is closed and
  chain zombie-2026-11-10 was closed by unit 037 on 2026-11-14
  (no Zombie Invasion tab in the Events hub); no zombie unit
  sits in inbox or claimed; do not seed until the tab is seen
  live again.

## Own PRs first

- VPS route blocked: ssh to centos@66.179.249.233 returned
  Permission denied (publickey) at about 03:27Z, about 174.7
  hours into the outage. The VPS gh CLI check could not run.
- Fallback via the GitHub connector (read-only open-PR list on
  zachmesh/lastwar): exactly three open PRs, all unchanged since
  2026-11-12 - #711 knowledge fold (Owner
  lastwar-knowledge-organizer, head e3c3dfd0, updated
  2026-11-12T20:04:57Z), #708 records 2026-11-12 (Owner
  lastwar-pr-integrator, head 2f59c270, updated
  2026-11-12T20:44:37Z), #425 tools log gate (Owner
  lastwar-tool-developer, head 4f41cdd6, updated
  2026-11-12T19:29:37Z). Updated timestamps identical to the
  ticker-1740 and ticker-1818 reads, so no new comment or review
  can have landed. None is owned by this job, and no open PR
  exists for records/2026-11-19. No new question or numbered fix
  point is addressed to this job. Note: the first connector
  status call failed with an MCP transport TLS error (peer closed
  connection); the retry connected and the list read succeeded.

## Probe - one computer session, blocker unchanged

- Mac mini ONLINE per device.list, last_seen
  2026-11-20T01:57:56Z (17:57:56 PST, about 95 minutes stale at
  probe time). connection.health: both transports healthy,
  lastResponseAgeSeconds 0 (native) and 2 (web),
  progressAgeSeconds 5519 on both (about 92 minutes frozen,
  anchor about 02:00Z, about 18:00 PT). The channel has not
  progressed since about 18:00 PT.
- environment.describe confirms LastWar IS in running_apps.
  Accessibility and screen recording permissions are granted.
  Display 1920x1080. `agent_window.available` is false with
  reason `new_tab_in_existing_window`.
- Session cc-149: list_windows returned 11 windows and 0
  LastWar windows; observe observation_unavailable; session
  ended clean. No activate or open_app attempt this pass - both
  methods failed without change in 1740 and 1818, and repeating
  them would breach the pivot rule (R2).
- 9 device invokes in total: 8 answered promptly, 1 param error
  of this pass's own making (a session_id arg passed to
  computer.control, which does not accept it); 0 timeouts, 0
  node_offline.
- Probe classification: tools/mac_capture_probe.py v1.2.0 on
  the assembled evidence (/tmp/lw-probe-1926.json) returns
  OFF_SCREEN_WINDOW, medium confidence, stop_pass yes (exit
  10). Same label as 1536, 1645, 1704, 1740 and 1818; confidence
  is medium rather than high because this pass skipped the
  View-menu inspect and the Chrome control observation the
  classifier lists as missing probe steps. Recovery still stands
  as the one owner step on the Mac mini: click the LastWar Dock
  icon once (or run _tools_/mac_lastwar_front.sh in Terminal),
  then re-probe.

## Unit

- None claimed, none completed. `next` was never called, so the
  queue-pick observation from 1645/1704 (a stale unit being
  handed out while the game is unreachable) was not re-tested
  this pass. The token was never acquired, so no release was
  owed. Tracker untouched. vip-2026-11-19-1800 stays in inbox
  at attempts 0 of 3, expires_at 2026-11-21T02:00:00Z.

## Standing counts

- No game unit since ticker-0214 gifts Nov 17 02:14 PT
  (about 65.4 hours missed). Seventh consecutive missed VIP day
  (the reset day ending at the 02:00Z boundary Nov 20; the new
  reset day's VIP unit is in inbox, attempts 0, unexecuted).
- Tonight's pre-reset sweep pair expired unexecuted in the
  1818 sync (02:19:25Z); the sweep night is fully missed.
- Missed batches stay 42 per the adopted worker definition
  (next point 23:00 PT Nov 19). The 19:00 batch is due and
  unexecuted: pr-integration-1900 started in-window at 19:01:09
  PT but could not merge records PR 708, VPS unreachable.
  Contradiction with MEMORY.md (43 as of the 15:00 batch, 44
  after the 19:00 batch) carried as retro flag (i); the
  sweep-night count discrepancy carried as retro flag (k);
  neither adopted.
- Duel day 4 Train Heroes ended 18:00 PT Nov 19, unreachable.
- VPS SSH still Permission denied (publickey), about 174.7
  hours into the outage; delivery blocked, commit left on
  local records/2026-11-19, no PR. This pass is partial.

## Time note

- The reset-day boundary is 02:00Z: the sweep windows end
  02:00Z and the VIP unit expires 02:00Z. In winter (PST,
  UTC-8) that is 18:00 PT; the repo's standing "19:00 PT
  reset" label is the PDT-era reading of the same 02:00Z
  instant. Times in this record use PST (UTC-8) unless marked
  Z. The integrator batch points (19:00, 23:00, 03:00, 07:00,
  11:00, 15:00 local) are a separate local-time schedule and
  are unaffected.
