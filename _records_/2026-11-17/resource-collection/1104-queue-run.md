---
title: Queue ticker harvest run - game window lost, eleventh consecutive occurrence
created: 2026-11-17T19:10:00Z
executor: ticker-1104
unit: harvest-2026-11-17-1003
regular: harvest
status: failed
---

# Queue ticker 2026-11-17 11:04-11:11 PT (ticker-1104) - FAILED

Unit harvest-2026-11-17-1003 (resource-collection) claimed
11:05:16 PT and completed FAILED. No game screen was reached,
no resource bubble was collected, nothing was spent. This is
the eleventh consecutive ticker pass lost to the same blocker:
the game window is lost in a native fullscreen Space and the
control channel cannot bind any window. No game unit has
executed successfully since ticker-0214 gifts at 02:14 PT -
about nine hours of routine (mail, help, gifts, harvest, VIP,
donations, trucks, training) now missed.

## Probe - one fresh session, blocker unchanged

- Mac mini ONLINE per device.list (last_seen 2026-11-17T18:40:31Z,
  about 25 minutes before the probe). environment.describe
  confirms LastWar IS in running_apps, alongside Google Chrome
  (Recharge Center - LASTWAR window), ChatGPT and Finder.
  Accessibility and screen recording permissions are granted.
- Session cc-28: computer.control open_app "LastWar" returned
  outcome_unknown twice (E0BDD313, DB5B04BF); activate
  LastWar returned ax_windows_empty; list_windows returned
  the same 10 windows as ticker-0534, ticker-0722, ticker-0804
  and ticker-1034 - no LastWar entry; screen.snap failed
  observation_unavailable.
- R2 pivot, new method, failed at the selection step: activate
  Chrome window 125 returned geometry_mismatch
  (origin_delta 256+, agent_display false), and a bare key
  control-right returned observation_required with no input
  dispatched - the channel cannot bind any window, so the
  Space-switch step could not be sent. No input was dispatched
  to the game in this pass. The green zoom button stays
  untouched per the standing lesson from ticker-0333, and no
  Escape or Control-Command-F was used.
- The owner was already told after the 2nd and after the 3rd
  occurrence that he must exit fullscreen or restart the game
  at the Mac; as of 11:11 PT there is no evidence he has done
  so. Standing route change (ticker-0534, R2) still holds: no
  game unit runs until the window is recovered. The next unit
  in line was left for the next tick; the next tick will hit
  the same blocker unless the Mac window is recovered first.

## Unit result

- status failed, duration_seconds 304 (claim 19:05:16Z to
  complete 19:10:20Z). stats: target 1, achieved 0,
  resources_gained none, verified no, blocker_category e
  (repeated blocker). Correction: the stats costs string was
  written as duration_about_13min against the token hold
  estimate; the measured unit duration is 304 seconds, about
  5 minutes. The tracker was left untouched (failed units do
  not move it); a shared marker suppresses re-picks of this
  unit. The harvest 1003 slot is consumed as failed; later
  harvest slots (1403, 1803, 2203) remain in inbox.

## Sync and pool

- Sync: reaped 0, expired 4, due 22, produced 0, already queued
  21 (mail, help, gifts, harvest, vip, passes, daily-missions,
  secrets, treasures, radar, survivors, trucks, train,
  training, donations, events, arms-race, star-ceremony,
  duel-score, scout, scout-midday). Branch reconcile warning:
  fetch of records/2026-11-17 failed (no remote ref),
  reconcile skipped (issue #446).
- Stats at sync: inbox 72, claimed 0, done 2325.
- Zombie chain stays closed (event ended 2026-10-30; last live
  check 2026-11-15 found no Zombie Invasion tab). No seeding.

## Own PRs first

- VPS SSH still Permission denied (publickey), about 118 hours
  into the break (IONOS console route chosen 2026-11-14 17:37 PT
  still not complete). The VPS gh check could not run.
- Public PR list re-read 2026-11-17T18:46Z via browser fetch of
  github.com/zachmesh/lastwar/pulls: exactly three open PRs -
  #711 (knowledge), #708 (records 2026-11-12), #425 (feat
  tools) - none owned by this job, no PR for records/2026-11-17
  exists. No question addressed to this job, nothing to fix.

## Owed work

- Tooling Issue for the repeated failure mode "game window lost
  in fullscreen Space, control channel blind" (class tooling) -
  filing owed at VPS recovery; gh unreachable while VPS SSH is
  down. Same owed item as ticker-0443, ticker-0534, ticker-0722,
  ticker-0804 and ticker-1034.
- Blocker write into a shared entry-route note (recording-rules
  Device access or queue design section 11, R2) - tier 2, cannot
  ride this tier-1 records commit; owed to the retro / the
  tooling issue above.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-1104-1117-delivery, UNPUSHED, push pending VPS
  recovery. No PR opened for records/2026-11-17.
