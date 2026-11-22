---
title: Queue ticker process failure - game window lost, fifth consecutive occurrence
created: 2026-11-17T16:13:00Z
executor: ticker-0804
unit: none claimed
regular: none
status: process-failure
---

# Queue ticker 2026-11-17 08:04-08:14 PT (ticker-0804) - PROCESS FAILURE

No unit was claimed and no unit was executed. This pass hit the
fullscreen-Space window-loss blocker for the fifth consecutive
ticker pass, so under rule R2 it is recorded as a process failure,
not as another routine failed unit. Token held 08:05-08:14 PT,
released at pass end.

## Probe - one fresh session, blocker unchanged

- Mac mini ONLINE per device.list (last_seen 2026-11-17T15:30:49Z,
  about 35 minutes before the probe). environment.describe
  confirms LastWar IS in running_apps, alongside Google Chrome
  (Recharge Center - LASTWAR window), ChatGPT and Finder.
  Accessibility and screen recording permissions are granted.
- Session cc-17: computer.control list_windows returns the same
  10 windows as ticker-0534 and ticker-0722 - no LastWar entry.
  The game window is still lost in the unobservable fullscreen
  Space; the control channel cannot see it. No further probe
  steps were repeated: screen.snap (observation_unavailable),
  Finder activate (geometry_mismatch) and open_app LastWar
  (outcome_unknown) were already tried identically in
  ticker-0722 and ticker-0534, and the green zoom button stays
  untouched per the standing lesson from ticker-0333.
- The owner was already told after the 2nd and after the 3rd
  occurrence that he must exit fullscreen or restart the game
  at the Mac; as of 08:14 PT there is no evidence he has done
  so. No game unit has executed successfully since ticker-0214
  gifts at 02:14 PT (176 Regular + 67 Premium claimed) - about
  six hours of routine (mail, help, gifts, harvest, VIP,
  donations, trucks, training) now missed.

## R2 accounting - fifth consecutive occurrence

- 1st: ticker-0333, harvest-2026-11-17-0203, 03:33 PT (green zoom
  click moved the window to a native fullscreen Space).
- 2nd: ticker-0443, radar-2026-11-17-0203, 04:43 PT.
- 3rd: ticker-0534, help-2026-11-17-0230, 06:06 PT (channel
  blindness widened to every window).
- 4th: ticker-0722, probe only, 07:22 PT.
- 5th: this pass, 08:04 PT probe, no unit claimed.
- Standing route change (ticker-0534, R2): NO game unit runs
  until the window is recovered. The next unit in line,
  harvest-2026-11-17-0603, was left in inbox unclaimed; the
  next tick will hit the same blocker unless the Mac window
  is recovered first.

## Sync and pool

- Sync: reaped 0, expired 0, due 22, produced 0, already queued
  22 (mail, help, gifts, harvest, vip, passes, daily-missions,
  secrets, treasures, radar, survivors, trucks, train, training,
  donations, events, arms-race, star-ceremony, duel-score, scout,
  scout-midday). Branch reconcile warning: fetch of
  records/2026-11-17 failed (no remote ref), reconcile skipped
  (issue #446).
- Stats: inbox 77, claimed 0, done 2308; newest finished
  2026-11-17T14:15:19Z (about 109 minutes before the stats read).
- Zombie chain stays closed (event ended; last live check
  2026-11-15 found no Zombie Invasion tab; most recent done
  zombie unit zombie-invasion-zombie-2026-11-10-037 finished
  2026-11-15T02:35:26Z failed, cleared false). No seeding.

## Own PRs first

- VPS SSH still Permission denied (publickey), about 115.5 hours
  into the break (IONOS console route chosen 2026-11-14 17:37 PT
  still not complete). The VPS gh check could not run.
- Public PR list re-read 2026-11-17T16:07Z via browser fetch of
  github.com/zachmesh/lastwar/pulls: exactly three open PRs -
  #711 (knowledge), #708 (records 2026-11-12), #425 (feat
  tools) - none owned by this job, no PR for records/2026-11-17
  exists. No question addressed to this job, nothing to fix.

## Owed work

- Tooling Issue for the repeated failure mode "game window lost
  in fullscreen Space, control channel blind" (class tooling) -
  filing owed at VPS recovery; gh unreachable while VPS SSH is
  down. Same owed item as ticker-0443, ticker-0534 and
  ticker-0722.
- Blocker write into a shared entry-route note (recording-rules
  Device access or queue design section 11, R2) - tier 2, cannot
  ride this tier-1 records commit; owed to the retro / the
  tooling issue above.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-0804-1117-delivery, UNPUSHED, push pending VPS
  recovery. No PR opened for records/2026-11-17.
