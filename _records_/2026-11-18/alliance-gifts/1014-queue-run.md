---
title: Queue ticker gifts run - game window lost, forty-fourth consecutive occurrence
created: 2026-11-18T18:35:00Z
executor: ticker-1010
unit: gifts-2026-11-18-0630
regular: gifts
status: failed
---

# Queue ticker 2026-11-18 10:14 to about 10:28 PT (ticker-1010) - FAILED

Unit gifts-2026-11-18-0630 (alliance-gifts) claimed 10:14:30 PT
and completed FAILED. No game screen was reached, no gift was
claimed, nothing was spent. This is the forty-fourth
consecutive ticker pass lost to the same blocker: the game
window is lost and the control channel cannot bind any window
(ticker-0834 at 08:34 PT was the forty-third). No game unit
has executed successfully since ticker-0214 gifts at 02:14 PT
Nov 17 - about thirty-two and a quarter hours of routine now
missed. The 11:00 PT batch point has not passed during this
run, so missed batches stay 35.

## Ordering deviation, stated plainly

This pass breached the standing route change (ticker-0534,
refined by ticker-2334): the newest queue-ticker record
(0834-process-failure) was re-read only AFTER the unit was
claimed and the device probe was run. The 0834 record
explicitly warned the next pass to re-read first, before sync,
and to claim no unit. This pass ran `queue.py sync` first,
then `next` and `claim`, and only then read the 0834 record
and the day INDEX. The claim should not have happened. The
probe itself was still required by the device-access retry
rule (at least 3 attempts before recording access-failed) and
sent no game input, so nothing was executed on an unread state
beyond the claim; the unit is consumed as failed, the tracker
is untouched, and the next tick re-produces gifts. The
deviation-watch verification restarts at ZERO honoring passes
a sixth time (0616 first honoring pass, broken by 0733's
claim-before-read; 0733 restated the warning, 0834 broke it
again, and this pass broke it again). The next pass must
re-read the newest queue-ticker record FIRST, before sync and
before any claim.

## Probe - three computer sessions, blocker unchanged

- Mac mini ONLINE per device.list (last_seen 2026-11-18T16:23:36Z
  at the first check, 18:20:33Z at the re-check - the Mac is
  back after the Nov 12 outage, and flapping: one
  computer.session start returned node_offline mid-pass and
  succeeded on retry). environment.describe confirms LastWar
  IS in running_apps, alongside Google Chrome (Recharge Center
  - LASTWAR window), ChatGPT and Finder. Accessibility and
  screen recording permissions are granted. Display 1920x1080.
  `agent_window.available` is false with reason
  `new_tab_in_existing_window`, the fifteenth pass in a row.
- Session cc-95: computer.control open_app "LastWar" returned
  outcome_unknown twice (actions 176107C1, 72BDB76D); no window
  appeared after 45 seconds. activate LastWar returned
  ax_windows_empty ("the selected app has no bound window").
  list_windows returned 11 windows three times (Typeless, 2x
  ChatGPT, Calendar, 2x Finder, 3x Chrome, BlueBubbles,
  Calculator), no LastWar entry in any of them; list_apps
  returned 8 apps with LastWar absent from the AX app list
  entirely while still listed in running_apps - the process is
  alive but exposes no window to Accessibility at all.
  open_app with file_path /Applications/LastWar.app returned
  invalid_params (the bundle exists per files.search, but is
  not accepted as a file). computer.observe and screen.snap
  both failed observation_unavailable. No game input was sent.
  No Escape, Return or Control-Command-F was used; the green
  zoom button stays untouched per the standing lesson.
- Sessions cc-96 and cc-97: the control channel itself is now
  wedged on the stale LastWar target - every window selection
  fails with stale_observation / geometry_mismatch
  (origin_delta=256+, size_delta=256+, agent_display=false),
  including activate Finder window 28, open_app Finder (twice,
  across both sessions), open_app Google Chrome (two running
  instances) and activate Chrome window 125. Unlike the
  settled #284 form, where Chrome windows observe normally and
  only the game window is off-screen, this pass could not bind
  ANY window - the channel is blind for all apps, a worsened
  form of the same outage.
- Probe classification: tools/mac_capture_probe.py v1.2.0 on
  the assembled evidence (/tmp/lastwar-probe-1010.json) returns
  OFF_SCREEN_WINDOW, high confidence, stop_pass true - the
  first high-confidence classification in this run of passes
  (0834 returned UNKNOWN on thinner evidence). The only
  missing checklist step is the View-menu inspect, which needs
  a bound window and cannot run in this state.
- The owner was already told after the 2nd and after the 3rd
  occurrence that he must exit fullscreen or restart the game
  at the Mac; as of about 10:28 PT there is no evidence he has done
  so. Recovery stays the owner step (issue #284): click the
  LastWar Dock icon once (or run tools/mac_lastwar_front.sh
  in Terminal), then re-probe. The remaining inbox units were
  left for the next tick; the next tick will hit the same
  blocker unless the Mac window is recovered first.

## Unit result

- status failed. stats: target "claim Regular and Premium
  alliance gifts", achieved "no game screen reached; 0
  claims", resources_gained none, costs "8 minutes 23 seconds
  device probe (503 s), no stamina or items", verified no,
  blocker_category e (repeated blocker). Correction noted:
  the unit was first completed with blocker_category f and
  corrected to e before delivery, matching the 0834 precedent
  for this identical blocker and the retro taxonomy. The
  tracker was left untouched (failed units do not move it).
  The gifts 0630 slot is consumed as failed; later gifts
  slots remain in inbox. Token held 10:14-10:18 and 10:19-10:23 PT
  (released and re-acquired mid-pass after a mistaken early
  release), released at close.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 3, Age of Science, 7.6 hours left at the 10:25
  read, day ends 18:00 PT Nov 18. Radar posture: RELEASE -
  claims score again today, release the stack built on Day 2.
  Research completions, valor badges and drone component
  chests also score today and are all missed while the window
  is down.

## Sync and pool

- Sync: reaped 0, expired 4 (arms-race, donations, survivors,
  training - all 2026-11-18-0603, expired unexecuted), due 22,
  produced 0, already queued 22 (mail, help, gifts, harvest,
  vip, passes, daily-missions, secrets, treasures, radar,
  survivors, trucks, train, training, donations, events,
  arms-race, star-ceremony, duel-score, scout, scout-midday).
  Completion marker reaped: radar-2026-11-18-0603. Branch
  reconcile warning: fetch of records/2026-11-18 failed (no
  remote ref), reconcile skipped (issue #446).
- Stats at sync: inbox 71, claimed 0, done 2422.
- Zombie chain stays closed (event ended 2026-10-30; last live
  check 2026-11-15 found no Zombie Invasion tab). No seeding.
- Tonight's pre-reset sweep pair is COMPLETE (zero-sweep-1630
  and 1730 in inbox); the Nov 17 pair already EXPIRED
  UNEXECUTED at 18:04:42 local (fourth consecutive missed
  night, Nov 14-17).

## Own PRs first

- VPS SSH still Permission denied (publickey), about 141 hours
  into the break (IONOS console route chosen 2026-11-14 17:37 PT
  still not complete, about 89 hours later). The VPS gh check
  could not run.
- Public PR list re-read 2026-11-18T18:13Z via the authenticated
  GitHub connector: exactly three open PRs - #711 (knowledge,
  Owner lastwar-knowledge-organizer, head e3c3dfd0, updated
  2026-11-12T20:04:57Z), #708 (records 2026-11-12, Owner
  lastwar-pr-integrator, head 2f59c270, updated
  2026-11-12T20:44:37Z), #425 (tools log gate, Owner
  lastwar-tool-developer, head 4f41cdd6, updated
  2026-11-12T19:29:37Z) - heads and updated_at unchanged since
  Nov 12. None owned by this job, no PR for records/2026-11-17
  or records/2026-11-18 exists. The #708 page text shows only
  commit-message snippets (Muse and lastwar-pr-integrator
  activity, Nov 12); no question addressed to this job, nothing
  to fix. The connector's read set does not expose PR review
  comments (pull_request_read / issue_read need write-capable
  approval), so comment review is limited to the page text.

## Owed work

- Tooling Issue for the repeated failure mode "game window lost
  in fullscreen Space, control channel blind" (class tooling) -
  filing owed at VPS recovery; gh unreachable while VPS SSH is
  down. Same owed item as every ticker pass since ticker-0443.
  This pass adds one new symptom to that issue: the control
  channel now fails to bind ANY window (stale_observation /
  geometry_mismatch on Finder and Chrome selects), not just the
  game window.
- Blocker write into a shared entry-route note (recording-rules
  Device access or queue design section 11, R2) - tier 2, cannot
  ride this tier-1 records commit; owed to the retro / the
  tooling issue above.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-1010-1118-delivery, UNPUSHED, push pending VPS
  recovery. No PR opened for records/2026-11-18.
