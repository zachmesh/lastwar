---
title: Queue ticker process failure - game window missing, thirty-second consecutive occurrence
created: 2026-11-18T06:42:00Z
modified: 2026-11-18T06:42:00Z
version: 1.0.0
description: Queue ticker 2026-11-17 22:34 PT process failure, LastWar has no window on the Mac mini
status: process-failure
grounded_in:
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-18T06:37Z
  - source: computer.session cc-62, computer.control list_windows, open_app, activate, computer.observe, connection.health, 2026-11-18T06:38Z to 06:40Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lastwar-probe-2236.json, 2026-11-18T06:41Z
  - source: tools/duel.py --json, 2026-11-18T06:38Z
  - source: _records_/2026-11-17/queue-ticker/1804-process-failure.md and _records_/2026-11-17/alliance-donations/2134-queue-run.md re-read before any claim
  - source: VPS SSH probe, 2026-11-18T06:37Z
---

# Queue ticker 2026-11-17 22:34-22:44 PT (ticker-2236) - PROCESS FAILURE

No unit was executed. This pass hit the windowless-LastWar blocker
for the thirty-second consecutive ticker pass, by the running count
in the records (ticker-2134: 31st). The ticker-0534 standing route
change was followed: the newest queue-ticker record (1804) and the
newest failure record (2134) were re-read, no unit was claimed, and
the device token was taken but released unused. One ordering note,
stated plainly: this pass's `queue.py sync` and `token-acquire` ran
BEFORE the 1804 record was re-read - the same ordering deviation
shape as ticker-1704's claim-before-read. No unit was claimed, so
nothing was executed on an unread state, but the next pass should
still re-read the newest queue-ticker record first, before sync.

## Probe - one fresh session, blocker unchanged

- Mac mini ONLINE per device.list (last_seen 2026-11-18T06:04:28Z,
  fresh at pass start). No evidence the owner has done the
  Dock-icon step: the window is still missing.
- environment.describe confirms LastWar IS in running_apps,
  alongside Google Chrome, ChatGPT and Finder. Accessibility and
  screen recording permissions are granted. Display 1920x1080.
  `agent_window.available` is false with reason
  `new_tab_in_existing_window`, the fourth pass in a row.
- Session cc-62: open_app LastWar outcome_unknown (action
  C0958A02-BE6D-490C-A5CB-1892631C9FC6); activate LastWar
  brought_to_front false, ax_windows_empty (action
  B63F5405-3869-4913-95A2-10AEF9E9770E); list_windows (all)
  11 windows, 0 LastWar; computer.observe observation_unavailable
  ("No current target window can be observed. Select an app with
  computer.control open_app or activate, then observe again.").
- NEW SHADE persists, twelfth pass in a row - the control channel
  cannot bind ANY window, not just LastWar. Activate Chrome
  window 125 failed with geometry_mismatch (origin_delta=256+
  size_delta=256+ agent_display=false, phase=select),
  input_dispatched false (action
  55732459-0935-42B4-9D87-250C1B9936D3). connection.health reports
  both transports connected and healthy (native lastResponse 0s,
  web 3s). One change in the numbers: progressAgeSeconds reads
  2054 on both transports now, against 5693 at ticker-2134 - the
  counter did not keep growing, it moved (last progress about
  22:06 PT). That is a gateway-counter movement, not a window
  recovery: the window is still missing. No Touch ID, no
  password, no game input of any kind was sent.
- Probe classification: tools/mac_capture_probe.py on the
  assembled evidence returns OFF_SCREEN_WINDOW, high confidence,
  stop_pass yes (exit 10). The one missing probe step is the
  View-menu inspect (Enter/Exit Full Screen), which cannot be
  read without a bound window. The recovery stays the same owner
  step (issue #284): click the LastWar Dock icon once (or run
  tools/mac_lastwar_front.sh in Terminal), then re-probe.

## R2 accounting - thirty-second consecutive occurrence

- 1st-25th: per the 1804 record (25th: ticker-1804, 18:04 PT).
- 26th: ticker-1834 (delivery branch, commit "twenty-sixth").
- 27th: ticker-1904 (delivery branch, commit "twenty-seventh").
- 28th: ticker-1934 (deviation-watch process failure, named in
  the 2134 record; no delivery branch or record file in the
  mirror).
- 29th: ticker-2004 (deviation-watch process failure, named in
  the 2134 record; survivor-intake/2004-queue-run.md is the only
  2004 record file in the mirror).
- 30th: ticker-2034 (training unit claimed and failed).
- 31st: ticker-2104 AND ticker-2134 both say thirty-first - the
  running count is muddled by one (2104's commit subject and
  2134's record both claim 31st). This pass counts as 32nd by
  following 2134's stated 31st.
- Unverified slot: no 2204 ticker record or delivery branch
  exists in the mirror, so whether a 22:04 pass hit the blocker
  is unknown. If it did, this pass is the 33rd, not the 32nd.
- No game unit has executed since ticker-0214 gifts at 02:14 PT,
  about twenty and a half hours of routine now missed.

## Own PRs first

- VPS route down (SSH Permission denied, see below), so no fresh
  gh check was possible this pass. The freshest GitHub-connector
  check stands: tool-development-2232 at 22:32 PT, about 8
  minutes before this pass started.
- Open PRs: #711 (knowledge, Owner lastwar-knowledge-organizer),
  #708 (records 2026-11-12, Owner lastwar-pr-integrator), #425
  (tooling, Owner lastwar-tool-developer). Heads and updated_at
  unchanged since Nov 12 (#708 2026-11-12T20:44:37Z, #711
  2026-11-12T20:04:57Z, #425 2026-11-12T19:29:37Z); #425 was
  re-verified CLEAN against current main at 22:32 PT. None is
  owned by this job; no open PR for records/2026-11-17.
- No new comment can exist without moving updated_at, which has
  not moved since the 2232 check. No question addressed to this
  job, nothing to fix.

## Sync and seeding

- Sync: reaped 0, expired 6, due 22, produced 0, already queued 22
  (mail, help, gifts, harvest, vip, passes, daily-missions,
  secrets, treasures, radar, survivors, trucks, train, training,
  donations, events, arms-race, star-ceremony, duel-score, scout,
  scout-midday). Branch reconcile skipped with a warning:
  fetch of records/2026-11-17 failed (remote ref missing),
  issue #446. Inbox holds 61 units; no unit was executed. The
  next unit (`passes-2026-11-17-1857`) was read but left
  unclaimed under the route change.
- Zombie seeding no-op: the Zombie Invasion event ended - the
  most recent done zombie unit (zombie-invasion-zombie-2026-11-10-037,
  finished 2026-11-15T02:35:26Z, status failed) found no Zombie
  Invasion tab in the Events hub and closed chain
  zombie-2026-11-10 with no successor. No fresh chain is seeded
  until a Zombie Invasion tab is seen live in the Events hub again.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 3, Age of Science, 19.4 hours left at the 22:38 read,
  day ends 18:00 PT Nov 18. Research completions land today;
  valor badges are spent only inside today (owner decision);
  drone component chests score only today (owner inventory);
  radar posture: RELEASE - claims score again today, release the
  stack built on Day 2.
- The day-3 scoring (research, valor badges, drone chests, radar
  release) is all missed while the window is down. Tonight's
  pre-reset sweep pair will hit the same blocker unless the
  window recovers before then.

## Delivery

- VPS SSH still Permission denied (publickey), probed 22:36 PT,
  about 129.9 hours into the break (outage since about 12:46 PT
  2026-11-12; owner chose the IONOS console route 2026-11-14
  17:37 PT; no fix yet). Push and PR are blocked.
- Delivery PARTIAL: record committed locally on
  ticker-2236-1117-delivery, UNPUSHED, push pending VPS recovery.
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
  through a temporary worktree on ticker-2236-1117-delivery,
  based on ticker-2134-1117-delivery, as in the previous passes.
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
  ticker-2236-1117-delivery, UNPUSHED, push pending VPS recovery.
  No PR opened for records/2026-11-17.
