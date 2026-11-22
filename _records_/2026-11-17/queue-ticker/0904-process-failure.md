---
title: Queue ticker process failure - game window lost, seventh consecutive occurrence
created: 2026-11-17T17:15:00Z
executor: ticker-0904
unit: harvest-2026-11-17-0603
regular: harvest
status: process-failure
---

# Queue ticker 2026-11-17 09:04-09:15 PT (ticker-0904) - PROCESS FAILURE

One unit was claimed and closed failed; no game work was executed.
This pass hit the fullscreen-Space window-loss blocker for the
seventh consecutive ticker pass, so under rule R2 it is recorded
as a process failure, not as another routine failed unit. Token
held 09:04-09:15 PT, released at pass end.

## Probe - three fresh sessions, blocker unchanged

- Mac mini ONLINE per device.list (last_seen 2026-11-17T15:30:49Z,
  07:30:49 PT - the same reading as ticker-0804 and ticker-0834;
  it did not move during this pass, so no new contact evidence
  either way). environment.describe confirms LastWar IS in
  running_apps (com.lastwar.ios), alongside Google Chrome
  (Recharge Center - LASTWAR window), ChatGPT and Finder.
  Accessibility and screen recording permissions are granted.
- Session cc-19: computer.control open_app "LastWar" returned
  outcome_unknown (action E8B9B7BB-0CA8-4C61-A5D1-E3203CEE6FD6);
  the launch was not repeated. computer.observe then failed
  observation_unavailable; activate "LastWar" failed with
  ax_windows_empty. list_windows returns the same 10 windows as
  ticker-0534, ticker-0722, ticker-0804 and ticker-0834 - no
  LastWar entry.
- Session cc-20: open_app "LastWar" again returned
  outcome_unknown (action D104AF14-6D16-45E5-B63F-5C4CA4D7E2C5);
  re-listing windows still shows the same 10 windows, no LastWar.
- Session cc-21: list_windows once more, same 10 windows, no
  LastWar entry. The game window is still lost in the
  unobservable fullscreen Space; the control channel cannot bind
  any window - activating even an ordinary Finder window refuses
  with geometry_mismatch, as in ticker-0722. The green zoom
  button was NOT clicked (standing lesson from ticker-0333 - it
  moves the window to the unobservable fullscreen Space). The
  Mission Control pivot was NOT retried - ticker-0443 already
  tried it and failed.
- Difference from ticker-0722/0804/0834: this pass claimed
  harvest-2026-11-17-0603 before probing (queue.py next picked
  it as the earliest-expiry unit), then closed it failed with
  the blocker as the summary. The unit's result stats carry
  only attempts=3 - the required resource-collection stats keys
  (target, achieved, resources_gained, costs, verified,
  blocker_category) are missing, so the closing counts as
  unverified in the retro aggregation. The tracker was left
  untouched, so the regular stays due and the next tick
  re-produces it.

## R2 accounting - seventh consecutive occurrence

- 1st: ticker-0333, harvest-2026-11-17-0203, 03:33 PT (green zoom
  click moved the window to a native fullscreen Space).
- 2nd: ticker-0443, radar-2026-11-17-0203, 04:43 PT.
- 3rd: ticker-0534, help-2026-11-17-0230, 06:06 PT (channel
  blindness widened to every window).
- 4th: ticker-0722, probe only, 07:22 PT.
- 5th: ticker-0804, probe only, 08:04 PT.
- 6th: ticker-0834, probe only, 08:34 PT.
- 7th: this pass, 09:04 PT probe, harvest unit claimed and
  closed failed.
- The owner was already told after the 2nd and after the 3rd
  occurrence that he must exit fullscreen or restart the game
  at the Mac; as of 09:15 PT there is no evidence he has done
  so. No game unit has executed successfully since ticker-0214
  gifts at 02:14 PT (176 Regular + 67 Premium claimed) - about
  seven hours of routine (mail, help, gifts, harvest, VIP,
  donations, trucks, training) now missed.
- Standing route change (ticker-0534, R2): NO game unit runs
  until the window is recovered. The next unit in line is the
  re-produced harvest regular; the next tick will hit the same
  blocker unless the Mac window is recovered first.

## Sync and pool

- Sync: reaped 0, expired 0, due 22, produced 0, already queued
  22 (mail, help, gifts, harvest, vip, passes, daily-missions,
  secrets, treasures, radar, survivors, trucks, train, training,
  donations, events, arms-race, star-ceremony, duel-score, scout,
  scout-midday). Branch reconcile warning: fetch of
  records/2026-11-17 failed (no remote ref), reconcile skipped
  (issue #446).
- Stats: inbox 77, claimed 0, done 2308; newest finished
  2026-11-17T14:15:19Z (about 150 minutes before the stats read).
- Zombie chain stays closed (event ended; last live check
  2026-11-15 found no Zombie Invasion tab; most recent done
  zombie unit zombie-invasion-zombie-2026-11-10-037 finished
  2026-11-15T02:35:26Z failed, cleared false). No seeding.

## Own PRs first

- VPS SSH still Permission denied (publickey), about 116.4 hours
  into the break (IONOS console route chosen 2026-11-14 17:37 PT
  still not complete). The VPS gh check could not run.
- Public PR list re-read 2026-11-17T17:08Z via browser fetch of
  github.com/zachmesh/lastwar/pulls: exactly three open PRs -
  #711 (knowledge), #708 (records 2026-11-12), #425 (feat
  tools) - none owned by this job, no PR for records/2026-11-17
  exists. List unchanged since the ticker-0804 check. No
  question addressed to this job, nothing to fix.

## Owed work

- Tooling Issue for the repeated failure mode "game window lost
  in fullscreen Space, control channel blind" (class tooling) -
  filing owed at VPS recovery; gh unreachable while VPS SSH is
  down. Same owed item as ticker-0443, ticker-0534, ticker-0722,
  ticker-0804 and ticker-0834.
- Blocker write into a shared entry-route note (recording-rules
  Device access or queue design section 11, R2) - tier 2, cannot
  ride this tier-1 records commit; owed to the retro / the
  tooling issue above.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-0904-1117-delivery, UNPUSHED, push pending VPS
  recovery. No PR opened for records/2026-11-17.
