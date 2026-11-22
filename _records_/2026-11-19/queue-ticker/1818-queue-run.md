---
title: Queue ticker run failure - game window missing, seventy-sixth consecutive occurrence
created: 2026-11-20T02:33:00Z
modified: 2026-11-20T02:33:00Z
version: 1.0.0
description: Queue ticker 2026-11-19 18:18 PT run failure, LastWar has no window on the Mac mini
status: run-failure
grounded_in:
  - source: _records_/2026-11-19/queue-ticker/1740-queue-run.md read during the run (route NOT honored - see below)
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-20T02:21Z
  - source: computer session cc-148, computer.control list_windows, activate and open_app, computer.observe, screen.snap, 2026-11-20T02:22Z to 02:29Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-1818.json, 2026-11-20T02:30Z
  - source: tools/queue.py sync, token-acquire, next, claim, release and token-release, 2026-11-20T02:19Z to 02:31Z
  - source: GitHub connector open-PR read on zachmesh/lastwar, 2026-11-20T02:32Z
  - source: VPS SSH probe, 2026-11-20T02:19Z
---

# Queue ticker 2026-11-19 18:18 to about 18:35 PT (ticker-1818) - FAILED

No unit executed, nothing read or claimed. No screen entered.
The blocker is the seventy-sixth consecutive window-loss
occurrence by chain arithmetic (ticker-1740 at 17:40 PT Nov 19
was the seventy-fifth; no ticker record exists for any slot
between 17:40 and 18:18 on Nov 19, so the count advances by
this pass alone; the counting basis is retro-owned - chain
arithmetic here, process-failure-record basis elsewhere).

## Route - NOT honored, deviation owned, mitigated

This pass repeated the token-before-probe ordering slip AND the
claim-before-probe slip: queue sync, token-acquire, `next` and
claim all ran before the newest queue-ticker record (1740) was
read and before the device probe. The material cost differs
from 1704: the claimed unit (help-2026-11-19-1430) was NOT
completed as failed - it was returned to inbox with
`queue.py release`, so no unit was burned as failed and no
attempt was lost beyond the claim itself (attempts 1 of 3,
claim stamps cleared, tracker untouched). The deviation-watch
of fully-honoring passes therefore stays at THREE (0434, 1347,
1404); this pass joins 1704 as not honoring, with release as
the mitigation. The next pass must read the newest
queue-ticker record first, then sync, then probe, then token
and claim only if the probe passes.

## Sync and seeding

- Sync: due 23, produced 0, already_queued all 23 (mail, help,
  gifts, harvest, vip, passes, daily-missions, secrets,
  treasures, radar, survivors, trucks, train, training,
  donations, events, arms-race, ghost-ops, star-ceremony,
  duel-score, scout, scout-midday), reaped 0, expired 9.
  The 9 expired unexecuted at 02:19:25Z in this pass's sync:
  arms-race, donations, harvest, radar, survivors and training
  2026-11-19-1403, scout-2026-11-18-1800, and both pre-reset
  sweep units zero-sweep-2026-11-19-1630 and -1730 (chain
  pre-reset-sweep-2026-11-19) - tonight's sweep is therefore
  fully missed; the 19:00 reset is about 25 minutes after this
  pass ends. Branch reconcile warning: fetch of
  records/2026-11-19 failed (remote ref missing, issue #446),
  reconcile skipped.
- Zombie seeding skipped: the event ended at about the 19:00
  reset on 2026-10-30; chain zombie-2026-10-28 is closed; no
  zombie unit sits in inbox or claimed; do not seed until a
  Zombie Invasion tab is seen live again.

## Own PRs first

- VPS route blocked: ssh to centos@66.179.249.233 returned
  Permission denied (publickey) at about 02:19Z, about 173.7
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
  ticker-1740 read about 40 minutes earlier, so no new comment
  or review can have landed. None is owned by this job, and no
  open PR exists for records/2026-11-19. No new question or
  numbered fix point is addressed to this job.

## Probe - one computer session, blocker unchanged

- Mac mini ONLINE per device.list, last_seen
  2026-11-20T01:57:56Z (about 24 minutes stale at probe time).
  environment.describe confirms LastWar IS in running_apps.
  Accessibility and screen recording permissions are granted.
  Display 1920x1080. `agent_window.available` is false with
  reason `new_tab_in_existing_window`.
- Session cc-148: list_windows returned 11 windows and 0
  LastWar windows, three times; activate "LastWar" failed
  ax_windows_empty with brought_to_front false, twice;
  open_app "LastWar" outcome_unknown, twice; observe
  observation_unavailable; screen.snap
  observation_unavailable. All device invokes answered
  promptly, 0 timeouts, 0 node_offline.
- Probe classification: tools/mac_capture_probe.py v1.2.0 on
  the assembled evidence (/tmp/lw-probe-1818.json) returns
  OFF_SCREEN_WINDOW, high confidence, stop_pass yes (exit
  10). Same label as 1536, 1645, 1704 and 1740.
- Detail vs 1740: identical - window enumeration works (a
  full 11-window list, three times), LastWar exposes no window
  and no listed window was bound this pass (no Finder binding
  attempt was made, unlike 1740). Recovery still stands as the
  one owner step on the Mac mini: click the LastWar Dock icon
  once (or run _tools_/mac_lastwar_front.sh in Terminal), then
  re-probe.

## Unit

- help-2026-11-19-1430 claimed before the probe (attempts 1
  of 3, lease to 02:40:42Z), released back to inbox
  unexecuted after the probe classified stop_pass yes; the
  unit stays available for a later pass. No other unit was
  claimed or completed. Tracker untouched.

## Standing counts

- No game unit since ticker-0214 gifts Nov 17 02:14 PT
  (about 64 hours missed). Seventh consecutive missed VIP day
  (vip-2026-11-19-1800 sits in inbox, unplayable while the
  window is gone; the reset is about 25 minutes away).
  Tonight's pre-reset sweep pair expired unexecuted in this
  pass's sync - the sweep night is missed, and the sweep-night
  count discrepancy stays carried as retro flag (k) from the
  1732 record; this run adopts neither figure. Duel day 4
  Train Heroes ended 18:00 PT Nov 19, unreachable.
- Missed batches stay 42 (next point 19:00 PT). Contradiction
  with MEMORY.md 43 carried as retro flag (i).
- VPS SSH still Permission denied (publickey), about 173.7
  hours into the outage; delivery blocked, commit left on
  local records/2026-11-19, no PR. This pass is partial.
