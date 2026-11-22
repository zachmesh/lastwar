---
title: Queue ticker radar run - game window lost, thirty-fifth consecutive occurrence
created: 2026-11-18T08:14:00Z
executor: ticker-0004
unit: radar-2026-11-17-2203
regular: radar
status: failed
---

# Queue ticker 2026-11-18 00:04-00:14 PT (ticker-0004) - FAILED

Unit radar-2026-11-17-2203 (radar-tasks) claimed 00:07:49 PT
and completed FAILED. No game screen was reached, no radar
task was claimed, nothing was spent. This is the thirty-fifth
consecutive ticker pass lost to the same blocker: the game
window is lost in a native fullscreen Space and the control
channel cannot bind any window (ticker-2334 at 23:34 PT was
the thirty-fourth). No game unit has executed successfully
since ticker-0214 gifts at 02:14 PT Nov 17 - about twenty-two
hours of routine (mail, help, gifts, harvest, VIP, donations,
trucks, training) now missed, and the duel day 3 radar release
this unit was meant to run stays unexecuted.

## Ordering deviation, stated plainly

This pass breached the standing route change (ticker-0534,
refined by ticker-2334): the newest queue-ticker record
(2334-process-failure) was re-read only AFTER the unit was
claimed and the device probe was run. The 2334 record
explicitly warned the next pass to re-read first, before sync,
and to claim no unit. This pass ran `queue.py sync` first,
then `next` and `claim`, and only then read the 2304 and 2334
records. The claim should not have happened. The probe itself
was still required by the device-access retry rule (at least
3 attempts before recording access-failed) and sent no game
input, so nothing was executed on an unread state beyond the
claim; the unit is consumed as failed, the tracker is
untouched, and the next tick re-produces radar. The next pass
must re-read the newest queue-ticker record FIRST, before sync
and before any claim.

## Probe - three fresh sessions, blocker unchanged

- Mac mini ONLINE per device.list (last_seen 2026-11-18T08:02:34Z,
  seconds before the probe) - the Mac is back after the Nov 12
  outage. connection.health: native and web transports
  connected, healthy (lastResponseAgeSeconds 0 and 10,
  progressAgeSeconds 419 and 420 - no longer stuck in the
  thousands as in the 2134 pass). environment.describe
  confirms LastWar IS in running_apps, alongside Google Chrome
  (Recharge Center - LASTWAR window), ChatGPT and Finder.
  Accessibility and screen recording permissions are granted.
  Display 1920x1080. `agent_window.available` is false with
  reason `new_tab_in_existing_window`, the sixth pass in a row.
- Session cc-66: computer.control open_app "LastWar" returned
  outcome_unknown; list_windows for LastWar returned 0;
  computer.observe failed observation_unavailable.
- Session cc-67 (fresh session): screen.snap failed
  observation_unavailable (display capture also fails - the
  NEW SHADE persists); list_windows (all) returned 11 windows
  (Typeless, 2x ChatGPT, Calendar, 2x Finder, 3x Chrome,
  BlueBubbles, Calculator), no LastWar entry; open_app
  "LastWar" outcome_unknown a second time; list_windows for
  LastWar still 0.
- Session cc-68 (fresh session): frontmost_app reports the app
  in front is the assistant itself, which cannot be viewed or
  controlled; open_app "LastWar" outcome_unknown a third time;
  activate LastWar without window_id returned
  ax_windows_empty - "the selected app has no bound window".
  No input was dispatched to the game in this pass. No Escape,
  Return or Control-Command-F was used; the green zoom button
  stays untouched per the standing lesson.
- The owner was already told after the 2nd and after the 3rd
  occurrence that he must exit fullscreen or restart the game
  at the Mac; as of 00:14 PT there is no evidence he has done
  so. Recovery stays the owner step (issue #284): click the
  LastWar Dock icon once (or run tools/mac_lastwar_front.sh
  in Terminal), then re-probe. The remaining inbox units were
  left for the next tick; the next tick will hit the same
  blocker unless the Mac window is recovered first.

## Unit result

- status failed, duration_seconds 349 (claim 08:07:49Z to
  complete 08:13:38Z). stats: target 1, achieved 0,
  resources_gained none, costs duration_about_5min,
  verified no, blocker_category e (repeated blocker). The
  tracker was left untouched (failed units do not move it).
  The radar 2203 slot is consumed as failed; later radar
  slots remain in inbox. Token held 00:07-00:13 PT, released.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 3, Age of Science, 17.8 hours left at the 00:12
  read, day ends 18:00 PT Nov 18. Radar posture: RELEASE -
  claims score again today, release the stack built on Day 2.
  This unit was the release-day radar unit; its failure leaves
  the day-3 radar release unexecuted. Research completions,
  valor badges and drone component chests also score today
  and are all missed while the window is down.

## Sync and pool

- Sync: reaped 0, expired 0, due 22, produced 0, already queued
  22 (mail, help, gifts, harvest, vip, passes, daily-missions,
  secrets, treasures, radar, survivors, trucks, train,
  training, donations, events, arms-race, star-ceremony,
  duel-score, scout, scout-midday). Branch reconcile warning:
  fetch of records/2026-11-18 failed (no remote ref),
  reconcile skipped (issue #446).
- Stats at sync: inbox 72, claimed 0, done 2382. Stalled
  priority-1: vip-2026-11-17-1800 (17.1h).
- Zombie chain stays closed (event ended 2026-10-30; last live
  check 2026-11-15 found no Zombie Invasion tab). No seeding.
- Tonight's pre-reset sweep pair: the 17:30/18:30 units for the
  Nov 17 reset already EXPIRED UNEXECUTED at 18:04:42 local
  (fourth consecutive missed night, Nov 14-17); the Nov 18
  pair is not yet staged (the 17:00-hour planner run owns it).

## Own PRs first

- VPS SSH still Permission denied (publickey), about 131.5 hours
  into the break (IONOS console route chosen 2026-11-14 17:37 PT
  still not complete). The VPS gh check could not run.
- Public PR list re-read 2026-11-18T08:06Z via the authenticated
  GitHub connector: exactly three open PRs - #711 (knowledge,
  Owner lastwar-knowledge-organizer, head e3c3dfd0), #708
  (records 2026-11-12, Owner lastwar-pr-integrator, head
  2f59c270), #425 (tools log gate, Owner lastwar-tool-developer,
  head 4f41cdd6) - heads and updated_at unchanged since Nov 12.
  None owned by this job, no PR for records/2026-11-17 or
  records/2026-11-18 exists. No question addressed to this job,
  nothing to fix.

## Owed work

- Tooling Issue for the repeated failure mode "game window lost
  in fullscreen Space, control channel blind" (class tooling) -
  filing owed at VPS recovery; gh unreachable while VPS SSH is
  down. Same owed item as ticker-0443, ticker-0534, ticker-0722,
  ticker-0804, ticker-1034, ticker-1104, ticker-2304 and
  ticker-2334.
- Blocker write into a shared entry-route note (recording-rules
  Device access or queue design section 11, R2) - tier 2, cannot
  ride this tier-1 records commit; owed to the retro / the
  tooling issue above.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-0004-1118-delivery, UNPUSHED, push pending VPS
  recovery. No PR opened for records/2026-11-18.
