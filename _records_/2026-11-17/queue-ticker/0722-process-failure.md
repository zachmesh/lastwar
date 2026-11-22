---
title: Queue ticker process failure - game window lost, fourth consecutive occurrence
created: 2026-11-17T15:35:00Z
executor: ticker-0722
unit: none claimed
regular: none
status: process-failure
---

# Queue ticker 2026-11-17 07:22-07:35 PT (ticker-0722) - PROCESS FAILURE

No unit was claimed and no unit was executed. This pass hit the
fullscreen-Space window-loss blocker for the fourth consecutive
ticker pass, so under rule R2 it is recorded as a process failure,
not as another routine failed unit. Token held 07:23-07:33 PT,
released at pass end.

## Probe - three fresh sessions, blocker unchanged

- Mac mini ONLINE per device.list (last_seen 2026-11-17T13:31:32Z,
  unchanged since 05:31 PT - a reconnection stamp, not an activity
  tracker). LastWar IS in running_apps (com.lastwar.ios);
  environment.describe confirms it running alongside a Chrome
  "Recharge Center - LASTWAR" window.
- Session cc-14: computer.control list_windows returns the same
  10 windows as ticker-0534 - no LastWar entry.
- Session cc-15: screen.snap fails observation_unavailable.
  Activating ordinary Finder window 28 refuses with
  geometry_mismatch (origin_delta 256+, size_delta 256+,
  agent_display=false) - the control channel cannot bind ANY
  window, not just the game window. Identical to ticker-0534.
- Session cc-16: open_app "LastWar" returns outcome_unknown;
  re-listing windows still shows the same 10 windows, no LastWar.
  The launch was not repeated, per the result instruction.
- The green zoom button was NOT clicked (standing lesson from
  ticker-0333 - it moves the window to the unobservable
  fullscreen Space). The Mission Control pivot was NOT retried -
  ticker-0443 already tried it and failed.

## R2 accounting - fourth consecutive occurrence

- 1st: ticker-0333, harvest-2026-11-17-0203, 03:33 PT (green zoom
  click moved the window to a native fullscreen Space).
- 2nd: ticker-0443, radar-2026-11-17-0203, 04:43 PT.
- 3rd: ticker-0534, help-2026-11-17-0230, 06:06 PT (channel
  blindness widened to every window).
- 4th: this pass, 07:22 PT probe, no unit claimed.
- The owner was already told after the 2nd and after the 3rd
  occurrence that he must exit fullscreen or restart the game
  at the Mac; as of 07:33 PT there is no evidence he has done
  so. No game unit has executed successfully since ticker-0214
  gifts at 02:14 PT (176 Regular + 67 Premium claimed) - about
  five hours of routine (mail, help, gifts, harvest, VIP,
  donations, trucks, training) now missed.
- Standing route change (ticker-0534, R2): NO game unit runs
  until the window is recovered. The next unit in line,
  harvest-2026-11-17-0603, was left in inbox unclaimed; the
  next tick will hit the same blocker unless the Mac window
  is recovered first.

## Sync and pool

- Sync: reaped 0, expired 1 (scout-midday-2026-11-16-0700, window
  passed before execution), due 22, produced 0, already queued 22
  (mail, help, gifts, harvest, vip, passes, daily-missions,
  secrets, treasures, radar, survivors, trucks, train, training,
  donations, events, arms-race, star-ceremony, duel-score, scout,
  scout-midday); completion markers reaped: help-2026-11-17-0230.
  Branch reconcile warning: fetch of records/2026-11-17 failed
  (no remote ref), reconcile skipped (issue #446).
- Stats: inbox 77, claimed 0, done 2308; newest finished
  2026-11-17T14:15:19Z (67 minutes before the stats read);
  stalled priority-1: vip-2026-11-16-1800, age 25.0h - its
  reset-day window expired at the 19:00 PT reset on Nov 16,
  so that day's VIP freebie is lost.
- Zombie chain stays closed (event ended; last live check
  2026-11-15 found no Zombie Invasion tab; most recent done
  zombie unit zombie-invasion-zombie-2026-11-10-037 finished
  2026-11-15T02:35:26Z failed, cleared false). No seeding.
- Tonight's pre-reset sweep pair (1630 + 1730) is staged, but
  execution depends on the channel recovering before 17:30.

## Own PRs first

- VPS SSH still Permission denied (publickey), about 114.3 hours
  into the break (IONOS console route chosen 2026-11-14 17:37 PT
  still not complete). The VPS gh check could not run.
- Public PR list re-read 2026-11-17T15:25Z: exactly three open
  PRs - #711 (knowledge), #708 (records 2026-11-12), #425 (feat
  tools) - none owned by this job, no PR for records/2026-11-17
  exists. No question addressed to this job, nothing to fix.

## Owed work

- Tooling Issue for the repeated failure mode "game window lost
  in fullscreen Space, control channel blind" (class tooling) -
  filing owed at VPS recovery; gh unreachable while VPS SSH is
  down. Same owed item as ticker-0443 and ticker-0534.
- Blocker write into a shared entry-route note (recording-rules
  Device access or queue design section 11, R2) - tier 2, cannot
  ride this tier-1 records commit; owed to the retro / the
  tooling issue above.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-0722-1117-delivery, UNPUSHED, push pending VPS
  recovery. No PR opened for records/2026-11-17.
- Note: the action-log file carries 5 pre-existing malformed
  lines (59, 106, 374, 380, 381 - extra data after the JSON
  object, or a split entry), found during this pass's JSONL
  validation. They predate this pass; my appended entry (line
  407) parses cleanly. Left untouched here.
