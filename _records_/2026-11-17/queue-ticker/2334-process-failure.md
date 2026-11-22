---
title: Queue ticker process failure - game window missing, thirty-fourth consecutive occurrence
created: 2026-11-18T07:42:00Z
modified: 2026-11-18T07:42:00Z
version: 1.0.0
description: Queue ticker 2026-11-17 23:34 PT process failure, LastWar has no window on the Mac mini
status: process-failure
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-18T07:34Z
  - source: computer.session cc-65, computer.control open_app and list_windows, computer.observe, environment.describe, 2026-11-18T07:36Z to 07:38Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lastwar-probe-2334.json, 2026-11-18T07:39Z
  - source: tools/duel.py --json, 2026-11-18T07:36Z
  - source: _records_/2026-11-17/queue-ticker/2236-process-failure.md and _records_/2026-11-17/resource-collection/2310-queue-run.md re-read before the probe
  - source: VPS SSH probe, 2026-11-18T07:35Z
  - source: browser fetch of github.com/zachmesh/lastwar/pulls, crawled 2026-11-18T07:11Z
---

# Queue ticker 2026-11-17 23:34-23:42 PT (ticker-2334) - PROCESS FAILURE

No unit was executed. This pass hit the windowless-LastWar blocker
for the thirty-fourth consecutive ticker pass, by the running count
in the records (ticker-2304 at 23:04 PT was the thirty-third). The
ticker-0534 standing route change was followed: the newest
queue-ticker records (2236 and the 2304 record in
resource-collection/2310) were re-read, no unit was claimed, and
the device token was taken but released unused. One ordering note,
stated plainly: this pass's `queue.py sync` ran BEFORE the 2236
record was re-read - the same ordering deviation shape as
ticker-1704's and ticker-2236's. No unit was claimed, so nothing
was executed on an unread state, but the next pass should still
re-read the newest queue-ticker record first, before sync.

## Probe - one fresh session, blocker unchanged

- Mac mini ONLINE per device.list (last_seen 2026-11-18T07:28:57Z,
  about 6 minutes before pass start). No evidence the owner has
  done the Dock-icon step: the window is still missing.
- environment.describe confirms LastWar IS in running_apps,
  alongside Google Chrome, ChatGPT and Finder. Accessibility and
  screen recording permissions are granted. Display 1920x1080.
  `agent_window.available` is false with reason
  `new_tab_in_existing_window`, the fifth pass in a row.
- Session cc-65: open_app LastWar outcome_unknown (action
  AADCC5B9-8F3E-432A-9D76-0731677BDA6C); list_windows (all)
  11 windows, 0 LastWar; computer.observe observation_unavailable
  ("No current target window can be observed. Select an app with
  computer.control open_app or activate, then observe again.").
  The 11 windows are identical in composition to the 2304 pass
  (Typeless, 2x ChatGPT, Calendar, 2x Finder, 3x Chrome,
  BlueBubbles, Calculator). No Touch ID, no password, no game
  input of any kind was sent.
- Probe classification: tools/mac_capture_probe.py on the
  assembled evidence returns OFF_SCREEN_WINDOW, medium
  confidence, stop_pass yes (exit 10). The one missing probe
  step is the View-menu inspect (Enter/Exit Full Screen), which
  cannot be read without a bound window. The recovery stays the
  same owner step (issue #284): click the LastWar Dock icon once
  (or run tools/mac_lastwar_front.sh in Terminal), then re-probe.
- A first probe run with an incomplete evidence file returned
  UNKNOWN (low confidence, exit 1) because the window.on_screen
  field was missing; re-run with the proper schema classified
  OFF_SCREEN_WINDOW. The blocker itself did not change between
  the two runs.

## Own PRs first

- VPS route down (SSH Permission denied, see below), so no fresh
  gh check was possible this pass. The public PR list was
  re-read via browser fetch (crawled 2026-11-18T07:11Z, about
  23 minutes before this pass started): exactly three open PRs -
  #711 (knowledge, Owner lastwar-knowledge-organizer), #708
  (records 2026-11-12, Owner lastwar-pr-integrator), #425
  (tooling, Owner lastwar-tool-developer). Same three as the
  2304 pass, heads and updated_at unchanged since Nov 12.
  None is owned by this job; no open PR for records/2026-11-17.
  No question addressed to this job, nothing to fix.

## Sync and seeding

- Sync: reaped 0, expired 0, due 22, produced 0, already queued
  22 (mail, help, gifts, harvest, vip, passes, daily-missions,
  secrets, treasures, radar, survivors, trucks, train,
  training, donations, events, arms-race, star-ceremony,
  duel-score, scout, scout-midday). One completion marker
  reaped (harvest-2026-11-17-2203, the 2304 failed unit).
  Branch reconcile skipped with a warning: fetch of
  records/2026-11-17 failed (remote ref missing), issue #446.
  Inbox holds 67 units; no unit was executed. The next unit
  (radar-2026-11-17-2203) was read but left unclaimed under
  the route change.
- Zombie seeding no-op: the Zombie Invasion event ended
  2026-10-30; the chain stays closed. No fresh chain is seeded
  until a Zombie Invasion tab is seen live in the Events hub
  again.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 3, Age of Science, 18.4 hours left at the 23:36 read,
  day ends 18:00 PT Nov 18. Research completions land today;
  valor badges are spent only inside today (owner decision);
  drone component chests score only today (owner inventory);
  radar posture: RELEASE - claims score again today, release the
  stack built on Day 2.
- The day-3 scoring (research, valor badges, drone chests, radar
  release) is all missed while the window is down. The 19:00
  reset is about 19 hours past; tonight's pre-reset sweep pair
  will hit the same blocker unless the window recovers before
  then. No game unit has executed since ticker-0214 gifts at
  02:14 PT, about twenty-one and a half hours of routine now
  missed.

## Delivery

- VPS SSH still Permission denied (publickey), probed 23:35 PT,
  about 130.6 hours into the break (outage since about 12:46 PT
  2026-11-12; owner chose the IONOS console route 2026-11-14
  17:37 PT; no fix yet). Push and PR are blocked.
- Delivery PARTIAL: record committed locally on
  ticker-2334-1117-delivery, UNPUSHED, push pending VPS recovery.
  No PR opened for records/2026-11-17. No Slack sync. Chat
  report owed per the ticker rule (previous pass also
  access-failed); this pass's final message carries it.

## Standing git status anomaly in the live mirror (persists)

- `git status` in the live mirror still reports a large changed
  set (modified activity files, deleted inbox unit files, deleted
  tools entries that exist on disk) while the queue tools run
  against the files on disk. The live tree sits on branch
  work/ops-execution-records, another job's in-flight state; no
  commit was attempted from this tree. The delivery commit goes
  through a temporary worktree on ticker-2334-1117-delivery,
  based on ticker-2304-1117-delivery, as in the previous passes.
  The live mirror's _records_/2026-11-17/ tree is untracked
  there, so the delivery branch carries only this job's ticker
  sections of the day INDEX, not the other jobs' sections.

## Owed work

- Tooling Issue for the repeated failure mode "game window lost
  in fullscreen Space, control channel blind" (class tooling) -
  filing owed at VPS recovery; gh unreachable while VPS SSH is
  down. Same owed item as every ticker pass since ticker-0443.
- Blocker write into a shared entry-route note (recording-rules
  Device access or queue design section 11, R2) - tier 2, cannot
  ride this tier-1 records commit; owed to the retro / the
  tooling issue above.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  ticker-2334-1117-delivery, UNPUSHED, push pending VPS recovery.
  No PR opened for records/2026-11-17.
