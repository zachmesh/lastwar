---
title: Queue ticker run failure - game window missing, seventy-third consecutive occurrence
created: 2026-11-20T00:56:00Z
modified: 2026-11-20T00:56:00Z
version: 1.0.0
description: Queue ticker 2026-11-19 16:45 PT run failure, LastWar has no window on the Mac mini
status: run-failure
grounded_in:
  - source: _records_/2026-11-19/queue-ticker/1536-queue-run.md re-read during the run (route partially honored - see below)
  - source: _records_/2026-11-19/INDEX.md tail (pr-catchall-1539, pr-integration-1630, knowledge-organization-1632) re-read during the run
  - source: device.list and device.describe on 1c817413-83e2-0545-cb90-36d5e096a6bd, 2026-11-20T00:47Z
  - source: connection.health and environment.describe on the same device, 2026-11-20T00:47Z
  - source: computer sessions cc-143 and cc-144, computer.control list_windows, activate and open_app, computer.observe, 2026-11-20T00:48Z to 00:52Z
  - source: tools/mac_capture_probe.py --evidence /tmp/lw-probe-1645.json, 2026-11-20T00:53Z
  - source: tools/duel.py --json, 2026-11-20T00:53Z
  - source: tools/queue.py sync, token-acquire, next and token-release, 2026-11-20T00:46Z to 00:56Z
  - source: GitHub public web open-PR read on zachmesh/lastwar, 2026-11-20T00:53Z
  - source: VPS SSH probe, 2026-11-20T00:46Z
---

# Queue ticker 2026-11-19 16:45 to about 16:56 PT (ticker-1645) - FAILED

No unit claimed and no unit completed. The probe failed, so the
execute loop stopped here instead of burning the pass on identical
failures. No screen entered, nothing read or claimed. The blocker is
the seventy-third consecutive window-loss occurrence by chain
arithmetic (ticker-1536 at 15:36 PT Nov 19 was the seventy-second;
no ticker record exists for any slot between 15:36 and 16:45 on
Nov 19, so the count advances by this pass alone; the counting
basis is retro-owned - chain arithmetic here, process-failure-record
basis elsewhere).

## Route - PARTIALLY honored, deviation owned

This pass repeated the 1434/1536 ordering slip on the read order:
queue stats, sync, token-acquire and `next` all ran before the
newest queue-ticker record (1536) was read. The material part of
the route HELD this time, unlike 1536: the probe ran before any
claim, no unit was claimed, and no unit attempt was burned on a
known blocker. The token was, however, acquired before the probe
(the 1404 honoring pattern takes no token before the probe), so
the token-acquire-then-probe order is a second deviation from the
strict honoring order; the token was released at 00:56Z. The
deviation-watch therefore does NOT advance: it stays at THREE
full honoring passes (0434, 1347, 1404). The next pass must keep
the full honoring order - newest queue-ticker record first, then
sync, then probe, then token and claim only if the probe passes.

## Probe - two computer sessions, blocker unchanged

- Mac mini ONLINE per device.list, last_seen
  2026-11-20T00:16:13Z (16:16:13 PST). connection.health: both
  transports healthy, lastResponseAgeSeconds 0 (native) and 0
  (web), progressAgeSeconds 2059 on native and 2051 on web -
  about 34 minutes frozen. That is DOWN from the 1536 reading
  of 6414 (about 107 minutes frozen, anchored at 13:55 PT):
  the channel progressed between 15:36 and about 16:12 PT, so
  the freeze is no longer anchored at 13:55 PT. Fresh responses
  on a channel whose progress last advanced about 16:12 PT.
- environment.describe confirms LastWar IS in running_apps
  (LastWar, alongside Google Chrome, ChatGPT and Finder).
  Accessibility and screen recording permissions are granted.
  Display 1920x1080. `agent_window.available` is false with
  reason `new_tab_in_existing_window`.
- Session cc-143: list_windows with app LastWar returned 0
  windows; activate "LastWar" failed ax_windows_empty with
  brought_to_front false; open_app "LastWar"
  outcome_unknown; observe observation_unavailable. Second
  attempt in the same session: list_windows LastWar again 0;
  activate again ax_windows_empty. Identical failure.
- Session cc-144 (third attempt, per the retry rule, fresh
  session after ending cc-143): list_windows LastWar 0;
  activate ax_windows_empty, brought_to_front false.
  Identical failure, third time.
- 14 device invokes in total, all answered promptly, 0
  timeouts, 0 node_offline.
- Probe classification: tools/mac_capture_probe.py v1.2.0 on
  the assembled evidence (/tmp/lw-probe-1645.json) returns
  OFF_SCREEN_WINDOW, high confidence, stop_pass yes (exit
  10). Same label as 0534, 0704, 1504 and 1536. Two missing
  probe steps: the View-menu inspect, not runnable without a
  selected window; and the Chrome-window control observation,
  not re-tested this pass.
- The recovery stays the same owner step (issue #284): click
  the LastWar Dock icon once (or run
  tools/mac_lastwar_front.sh in Terminal), then re-probe.
- No game input was sent in this pass. No Escape, Return or
  Control-Command-F was used; the green zoom button stays
  untouched per the standing lesson. No Touch ID, no password.

## Unit - none claimed

- `next` (read-only pick, before the probe) returned
  vip-2026-11-18-1800. It was NOT claimed. The unit itself is
  stale - planned for the Nov 18 18:00 slot, its VIP rewards
  expired at the 19:00 reset Nov 18, so even with game access
  this pass would have claimed Nov 19 VIP under a Nov 18 unit.
  `next` handed out the oldest due unit although its game
  window had passed - the same queue-pick observation 1536
  made for daily-missions. Noted for the retro; no new issue
  filed (gh unreachable, see below). The unit stays in inbox
  for a future pass once the window returns.
- Token acquired 00:46Z, released 00:56Z. Tracker untouched
  (no unit was executed).

## Own PRs first

- VPS route down (SSH Permission denied, see below), so no gh
  check was possible this pass. The open PR list was re-read
  via the public GitHub web (2026-11-20T00:53Z): exactly
  three open PRs - #711 (knowledge: fold ticker-1047 pass
  into 4 profiles, opened Nov 12), #708 (records:
  2026-11-12, opened Nov 12), #425 (feat(tools): add
  pre-delivery log gate, opened Nov 8). Titles, authors and
  dates identical to the 1536 read; no new PR activity. The
  public web list shows no head SHAs, so the byte-identical
  heads (711 e3c3dfd0, 708 2f59c270, 425 4f41cdd6, all
  2026-11-12) stand as last verified by the 1536 pass and were
  not re-verified this pass. None is owned by this job; no open
  PR for records/2026-11-19; no new question addressed to this
  job. This job's one adopted PR 137 stays merged.

## Sync and seeding

- Sync: reaped 0, expired 0, due 23, produced 0, already
  queued 23 (mail, help, gifts, harvest, vip, passes,
  daily-missions, secrets, treasures, radar, survivors,
  trucks, train, training, donations, events, arms-race,
  ghost-ops, star-ceremony, duel-score, scout, scout-midday).
  Branch reconcile skipped with a warning: fetch of
  records/2026-11-19 failed (remote ref missing), issue #446.
  Pool at the 00:47Z stats read: inbox 77, claimed 0, done
  2559.
- Zombie seeding: none. The most recent done zombie unit (037,
  chain zombie-2026-11-10, finished 2026-11-15T02:35Z) closed
  the chain because the Zombie Invasion event had ended - no
  Zombie Invasion tab in the Events hub - and the activity
  metadata forbids seeding a fresh chain until a Zombie tab is
  seen live again. No zombie unit sits in inbox or claimed,
  and none was enqueued.

## Duel posture (read from tools/duel.py, not from the screen)

- Duel day 4, Train Heroes, 1.1 hours left at the 16:52 read,
  day ends 18:00 PT Nov 19. Day 3 Age of Science is now
  definitively closed with its scoring (research completions,
  valor badges, drone component chests, radar release) all
  missed. Day 4 is a hero day: hero EXP, shards, skill medals
  and recruitment tickets score, and the owner spends those
  consumables; radar posture is STACK - complete but do not
  claim. None of it is reachable while the window is down. No
  game unit has executed since ticker-0214 gifts at 02:14 PT
  Nov 17, about sixty-two and a half hours of routine now
  missed. Seventh consecutive missed VIP day; fifth
  consecutive missed pre-reset sweep night (tonight's sweep
  pair sits in the pool, 1630 seq 1 + 1730 seq 2, unexecuted).

## Delivery

- VPS SSH still Permission denied (publickey), probed 16:46 PT,
  about 172 hours into the break (outage since about 12:47 PT
  2026-11-12; owner chose the IONOS console route 2026-11-14
  17:37 PT, about 111 hours ago; no fix yet). Push and PR are
  blocked.
- Delivery PARTIAL: record committed locally on
  records/2026-11-19, UNPUSHED, push pending VPS recovery. No
  PR opened for records/2026-11-19. No Slack sync. Chat report
  owed per the ticker rule (previous pass also access-failed);
  this pass's final message carries it.
- Missed batches stay 42 per the adopted definition (the 15:00
  point was covered by pr-integration-1530, which started
  in-window; next point 19:00 PT Nov 19). Retro flag (i)
  carried: MEMORY.md states 43 as of the 15:00 batch, counting
  the due-but-blocked batch as missed - this run adopts 42 per
  the first-hand 1530 record, retro to rule.
- Live mirror log note: the append to the live tree's
  _logs_/repo-actions/action-log.jsonl landed; the file still
  carries the 5 pre-existing lines that do not parse as JSON
  (lines 59, 106, 374, 380, 381 - concatenated pairs and a
  blank line from the Nov 3 era, the #401/#422 class). The
  delivery-branch copy (from records/2026-11-19) is the
  committed record; the live tree's log still needs the gate
  repair (PR #425) at route recovery.

## Standing git status anomaly in the live mirror (persists)

- `git status` in the live mirror still reports a large changed
  set (modified activity files, deleted inbox unit files,
  deleted tools entries that exist on disk) while the queue
  tools run against the files on disk. The live tree sits on
  branch work/ops-execution-records, another job's in-flight
  state; no commit was attempted from this tree. The delivery
  commit goes through the records worktree on
  records/2026-11-19, as the 1504 and 1536 passes did. The
  live mirror's _records_/2026-11-19/ tree is untracked there,
  so the delivery branch carries only this job's ticker
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
  This pass adds two observations beyond the 1536 record:
  (a) connection.health progressAgeSeconds fell from 6414 at
  1536 to about 2055 now - the channel progressed around
  16:12 PT, so the freeze is no longer anchored at 13:55 PT;
  (b) `next` again handed out a stale unit whose game window
  had already passed (vip-2026-11-18-1800, expired Nov 18
  19:00) - a queue-pick observation for the retro.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey). Record committed locally only on
  records/2026-11-19, UNPUSHED, push pending VPS recovery. No
  PR opened for records/2026-11-19.
