---
title: Alliance Help queue run
created: 2026-11-17T22:15:00Z
executor: ticker-1404
unit: help-2026-11-17-1030
regular: help
status: failed
---

# Alliance help 2026-11-17 14:04-14:15 PT (ticker-1404)

Unit claimed 14:06 PT, device sessions cc-36, cc-37 and cc-38 on
the Mac mini. Token held 14:05-14:15 PT, released at pass end.

## Access failure - game window lost (same blocker as ticker-0333 through ticker-1334)

- Mac mini ONLINE (device.list last_seen 2026-11-17T20:02:14Z,
  UNCHANGED since the ticker-1204 probe - now about 2 hours 10
  minutes stale at this pass's check, the same stamp every pass
  since 12:02 PT has read). connection.health: native and web
  transports healthy, last response 0-2 seconds ago, no terminal
  failure - the gateway is live, so this is not a connectivity
  outage. LastWar IS in running_apps (com.lastwar.ios) but
  exposes NO window: list_windows three times shows the same 10
  windows with no LastWar entry; open_app "LastWar" four times
  (outcome_unknown each time, across three sessions, including
  once after connection.repair on the web target); activate
  LastWar twice (ax_windows_empty, brought_to_front false);
  activate on a Chrome window also failed (geometry_mismatch,
  target stuck on com.lastwar.ios); computer.observe and
  screen.snap both report observation_unavailable.
  environment.describe twice confirms the process is running
  with accessibility and screen recording permissions granted.
  Display 1920x1080.
- The green zoom button was never touched (standing lesson
  from ticker-0333 - it moves the window to the unobservable
  fullscreen Space).
- No game screen was ever reached. No help bubble seen, no Help
  All pressed, nothing claimed, nothing spent. The alliance-help
  open questions (daily help cap, what helpers and helped
  players each receive) stay open.

## Blocker accounting (rule R2) - SEVENTEENTH consecutive occurrence

- This is the SEVENTEENTH consecutive ticker pass hitting this
  blocker (ticker-0333 harvest, ticker-0443 radar,
  ticker-0534 help, ticker-0722 probe, ticker-0804 probe,
  ticker-0834, ticker-0904, ticker-0934 probe, ticker-1004
  help, ticker-1034, ticker-1104, ticker-1134, ticker-1204
  survivors, ticker-1234 donations, ticker-1304 probe,
  ticker-1334 probe, then this help unit). Per R2 the third
  occurrence already triggered its actions, and the fourth was
  to be reported to the owner as a process failure: the owner
  was told after the 2nd and after the 3rd occurrence that he
  must exit fullscreen or restart the game at the Mac; as of
  14:15 PT there is no evidence he has done so - the
  last_seen stamp has not moved since 12:02 PT and the window
  is still missing. The standing route change stands: NO game
  unit runs until the window is recovered. This pass claimed
  its unit before the probe (as ticker-1204 and ticker-1234
  did); the pass stops after this unit rather than cascading
  failed units.
- No game unit has executed successfully since ticker-0214
  gifts at 02:14 PT (176 Regular + 67 Premium claimed) -
  about twelve hours of routine (mail, help, gifts, harvest,
  VIP, donations, trucks, training) now missed. Duel day 2
  Base Expansion ends 18:00 PT today: UR truck dispatches,
  Legendary secret tasks and survivor intake all score today
  and all stay missed while the window is down.

## Closing

- Unit help-2026-11-17-1030 completed FAILED (blocker_category
  e, repeated blocker; target 1, achieved 0, verified no).
  Tracker untouched; the next tick re-produces help.
- Sync: reaped 0, expired 2, due 22, produced 0, already queued
  22 (mail, help, gifts, harvest, vip, passes,
  daily-missions, secrets, treasures, radar, survivors,
  trucks, train, training, donations, events, arms-race,
  star-ceremony, duel-score, scout, scout-midday). Stats:
  inbox 71, claimed 0, done 2331; stalled priority-1 units:
  vip-2026-11-16-1800 (31.7h), zero-sweep-2026-11-17-1630
  (9.4h), zero-sweep-2026-11-17-1730 (8.3h),
  vip-2026-11-17-1800 (7.1h).
- Zombie chain stays closed (event ended 2026-10-30, unit 066;
  no seeding - the last live check, 2026-11-15, found no
  Zombie Invasion tab; most recent done zombie unit
  zombie-invasion-zombie-2026-11-10-037 finished
  2026-11-15T02:35:26Z failed, cleared false).
- Own PRs first: VPS SSH still Permission denied (publickey),
  so the VPS gh check could not run. The public PR list was
  read instead (browser.open, 2026-11-17T22:12Z): exactly
  three open PRs - #711 (knowledge), #708 (records
  2026-11-12), #425 (feat tools) - none owned by this job,
  no PR for records/2026-11-17 exists. No question addressed
  to this job, nothing to fix.
- Duel posture (tools/duel.py --json, 14:12 PT): day 2 Base
  Expansion, 3.8 hours left, day ends 18:00 PT. UR truck
  dispatches score (Handbook 100,000 each) and Legendary
  secret tasks score (75,000); survivor recruitment scores;
  radar posture stack (complete tasks, do NOT claim).
- Push and PR blocked - VPS SSH still Permission denied
  (publickey), about 121 hours into the outage; record
  committed locally only on ticker-1404-1117-delivery,
  UNPUSHED, push pending VPS recovery. No PR opened for
  records/2026-11-17.
- Issue filing owed at VPS recovery: repeated failure mode
  "game window lost in fullscreen Space, control channel blind"
  (class tooling) - gh is unreachable while VPS SSH is down,
  so no issue number exists yet. Same owed item as ticker-0443,
  ticker-0534, ticker-0722, ticker-0804, ticker-1204,
  ticker-1234, ticker-1304 and ticker-1334.
