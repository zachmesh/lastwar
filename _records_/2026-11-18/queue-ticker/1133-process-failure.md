---
title: Queue ticker process failure - game window missing, forty-fifth consecutive occurrence
created: 2026-11-18T19:47:00Z
modified: 2026-11-18T19:47:00Z
version: 1.0.0
description: Queue ticker 2026-11-18 11:33 PT process failure, LastWar has no window on the Mac mini
status: process-failure
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-18T19:33Z
  - source: computer.session cc-98 and cc-99, computer.control open_app, activate and list_windows, computer.observe, screen.snap, environment.describe, 2026-11-18T19:35Z to 19:47Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lastwar-probe-1133.json, 2026-11-18T19:45Z
  - source: tools/duel.py --json, 2026-11-18T19:40Z
  - source: _records_/2026-11-18/queue-ticker/0733-process-failure.md and _records_/2026-11-18/INDEX.md re-read AFTER sync and claim (ordering deviation, see below)
  - source: VPS SSH probe, 2026-11-18T19:34Z
  - source: GitHub connector list_pull_requests on zachmesh/lastwar, 2026-11-18T19:44Z
---

# Queue ticker 2026-11-18 11:33-11:47 PT (ticker-1133) - PROCESS FAILURE

One unit was claimed and closed failed, and the pass hit the
windowless-LastWar blocker for the forty-fifth consecutive ticker
pass, by the running count in the records (ticker-1010 at 10:14 PT
was the forty-fourth). The counting-label contradiction the
knowledge-organization 0032 pass flagged persists for the retro:
ticker-2104 and ticker-2134 both recorded as the 31st, and the
2204 slot is still unknown. This run's trigger_reason was
dependency_probe; the 11:04 tick fired late (pass started 11:33
PT), the 11:00 batch point passed before this run with no records
PR merged, so missed batches stay 36 (counted by queue-planning
1040 and pr-integration 1100).

## Ordering deviation - stated plainly

This pass ran sync and claimed harvest-2026-11-18-1003 BEFORE
re-reading the newest queue-ticker record (1010), against the
ticker-0534 route change (claim no unit until the window is
recovered) and the explicit warnings in the 0004, 0733, 0834 and
1010 records. The deviation watch restarts at zero a seventh
time and two more consecutive honoring passes are needed again
before the route change counts as verified. The claim should not
have happened; the probe itself was still required by the retry
rule and sent no game input. The next pass must re-read the
newest queue-ticker record FIRST, before sync and before any
claim.

## Probe - two computer sessions, blocker unchanged

- Mac mini ONLINE per device.list (last_seen 2026-11-18T19:03:24Z,
  about 30 minutes before the pass). No evidence the owner has
  done the Dock-icon step: the window is still missing.
- environment.describe confirms LastWar IS in running_apps,
  alongside Google Chrome, ChatGPT and Finder. Accessibility and
  screen recording permissions are granted. Display 1920x1080.
  `agent_window.available` is false with reason
  `new_tab_in_existing_window`, the sixteenth pass in a row.
  All 15 device invokes in this pass that completed returned
  promptly; the channel is not stalled. No connection.repair was
  run this pass.
- Session cc-98: open_app "Last War" failed (no matching app);
  open_app "LastWar" outcome_unknown (action
  05F3F5C4-A96D-4A8A-8400-EE4EF2D59869); computer.observe
  returned observation_unavailable ("No current target window
  can be observed."); environment.describe shows the process
  running; activate LastWar without window_id dispatched but
  brought nothing to front (ax_windows_empty); list_windows
  returned 11 windows with no LastWar entry (three checks, one
  after a 20-second wait); screen.snap observation_unavailable.
  One launch attempt satisfies the retry rule (the 1010 pass ran
  two). Session cc-99 (fresh, after ending cc-98): open_app
  "Finder" failed stale_observation/geometry_mismatch with
  target_bundle_id still com.lastwar.ios - the control channel
  is wedged on the stale LastWar target and cannot bind ANY
  window, confirming ticker-1010's NEW symptom in a fresh
  session. The pass stops here on the window, not on the token.
  The unit was closed failed before the probe detail was written
  up, token released 11:47 PT.
- Methodology note, stated plainly: no game input was sent in
  this pass. No Escape, Return or Control-Command-F was used;
  the green zoom button stays untouched per the standing
  lesson. No Touch ID, no password. Chrome window 125 was not
  tested for selectability this pass (0500 tested it and it
  failed with geometry_mismatch); the probe lists that as a
  missing step, same as before.
- Probe classification: tools/mac_capture_probe.py v1.2.0 on the
  assembled evidence (/tmp/lw-probe-1133.json) returns
  OFF_SCREEN_WINDOW, high confidence, stop_pass yes. Same label
  as the 0616, 0733 and 1010 passes. The missing probe steps are
  the same as 0353, 0500, 0616 and 0733: the View-menu inspect
  (Enter/Exit Full Screen) and one control observation of a
  Chrome window, neither reachable without a bound window. The
  recovery stays the same owner step (issue #284): click the
  LastWar Dock icon once (or run tools/mac_lastwar_front.sh in
  Terminal), then re-probe.

## Own PRs first

- VPS route down (SSH Permission denied, see below), so no fresh
  gh check was possible this pass. The public PR list was
  re-read via the GitHub connector (list_pull_requests,
  2026-11-18T19:44Z): exactly three open PRs - #711
  (knowledge, Owner lastwar-knowledge-organizer, head e3c3dfd0,
  updated 2026-11-12T20:04:57Z), #708 (records 2026-11-12,
  Owner lastwar-pr-integrator, head 2f59c270, updated
  2026-11-12T20:44:37Z), #425 (tooling, Owner
  lastwar-tool-developer, head 4f41cdd6, updated
  2026-11-12T19:29:37Z). Same three as the 0004, 0034, 0134,
  0243, 0353, 0500, 0616, 0733, 0834 and 1010 passes, heads and
  updated_at unchanged since Nov 12 (so no new comments on any
  of them). None is owned by this job; no open PR for
  records/2026-11-17 or records/2026-11-18. No question
  addressed to this job, nothing to fix.

## Sync and seeding

- Sync: reaped 0, expired 0, due 22, produced 0, already queued
  22 (mail, help, gifts, harvest, vip, passes, daily-missions,
  secrets, treasures, radar, survivors, trucks, train,
  training, donations, events, arms-race, star-ceremony,
  duel-score, scout, scout-midday). One completion marker
  reaped (gifts-2026-11-18-0630). Branch reconcile skipped with
  a warning: fetch of records/2026-11-18 failed (remote ref
  missing), issue #446. Inbox holds 77 units, claimed 0, done
  2433 at the 11:34 read; one unit (harvest-2026-11-18-1003)
  was claimed and closed failed under the deviation above.
  Token held 11:35-11:47 PT, released.
- Zombie seeding no-op: the Zombie Invasion event ended
  2026-10-30 (chain zombie-2026-11-10 closed by unit 037 on
  2026-11-15 after the Events hub showed no Zombie Invasion
  tab); the chain stays closed. No fresh chain is seeded until
  a Zombie Invasion tab is seen live in the Events hub again.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 3, Age of Science, 6.3 hours left at the 11:40 read,
  day ends 18:00 PT Nov 18. Research completions land today;
  valor badges are spent only inside today (owner decision);
  drone component chests score only today (owner inventory);
  radar posture: RELEASE - claims score again today, release
  the stack built on Day 2.
- The day-3 scoring (research, valor badges, drone chests, radar
  release) is all missed while the window is down. No game unit
  has executed since ticker-0214 gifts at 02:14 PT Nov 17,
  about thirty-three and a half hours of routine now missed.
  Tonight's pre-reset sweep pair is COMPLETE (staged by the
  0440 and 0540 planners); the Nov 17 pair already expired
  unexecuted, the fourth consecutive missed night (Nov 14-17).

## Delivery

- VPS SSH still Permission denied (publickey), probed 11:34 PT,
  about 143 hours into the break (outage since about 12:46 PT
  2026-11-12; owner chose the IONOS console route 2026-11-14
  17:37 PT, about 90 hours ago; no fix yet). Push and PR are
  blocked.
- Delivery PARTIAL: record committed locally on
  ticker-1133-1118-delivery, UNPUSHED, push pending VPS recovery.
  No PR opened for records/2026-11-18. No Slack sync. Chat
  report owed per the ticker rule (previous pass also
  access-failed); this pass's final message carries it.
- The 11:00 PT batch point passed before this run with no
  records PR merged, so missed batches stay 36; next point
  15:00 PT.

## Standing git status anomaly in the live mirror (persists)

- `git status` in the live mirror still reports a large changed
  set (modified activity files, deleted inbox unit files, deleted
  tools entries that exist on disk) while the queue tools run
  against the files on disk. The live tree sits on branch
  work/ops-execution-records, another job's in-flight state; no
  commit was attempted from this tree. The delivery commit goes
  through a temporary worktree on ticker-1133-1118-delivery,
  based on ticker-1010-1118-delivery, as in the previous passes.
  The live mirror's _records_/2026-11-18/ tree is untracked
  there, so the delivery branch carries only this job's ticker
  sections of the day INDEX, not the other jobs' sections.
- Root cause of the tools/ deletions pinned at 0500: `tools`
  is a symlink to `_tools_` (Nov 8), while git tracks
  `tools/duel.py` and friends as real paths, so git reports
  every tools/ entry as deleted although the files run fine
  through the symlink. Cosmetic only; no repair attempted.

## Owed work

- Tooling Issue for the repeated failure mode "game window lost
  in fullscreen Space, control channel blind" (class tooling) -
  filing owed at VPS recovery; gh unreachable while VPS SSH is
  down. Same owed item as every ticker pass since ticker-0443.
  This pass adds one new observation to that issue's evidence:
  the control channel stays wedged on the stale LastWar target
  even in a FRESH computer session (cc-99) - every window
  selection fails stale_observation/geometry_mismatch,
  including Finder.
- Blocker write into a shared entry-route note (recording-rules
  Device access or queue design section 11, R2) - tier 2, cannot
  ride this tier-1 records commit; owed to the retro / the
  tooling issue above.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-1133-1118-delivery, UNPUSHED, push pending VPS recovery.
  No PR opened for records/2026-11-18.
