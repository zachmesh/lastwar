---
title: Alliance Help queue run
created: 2026-11-17T18:15:00Z
executor: ticker-1004
unit: help-2026-11-17-0630
regular: help
status: failed
---

# Alliance help 2026-11-17 10:04-10:15 PT (ticker-1004)

Unit claimed 10:05 PT, device sessions cc-23 and cc-24 on the Mac mini.
Token held 10:05-10:15 PT, released at pass end.

## Access failure - game window lost (same blocker as ticker-0333 through ticker-0934)

- Mac mini ONLINE (device.list last_seen 2026-11-17T17:33:34Z,
  about 32 minutes before the probe). LastWar IS in
  running_apps (com.lastwar.ios) but exposes NO window:
  list_windows three times shows the same 10 windows with no
  LastWar entry; open_app "LastWar" three times
  (outcome_unknown each time, no window appeared even after
  15 and 20 second waits); activate LastWar twice
  (ax_windows_empty), the second time in a fresh session cc-24
  after ending cc-23; computer.observe and screen.snap both
  report observation_unavailable. environment.describe twice
  confirms the process is running with accessibility and
  screen recording permissions granted.
- The green zoom button was never touched (standing lesson
  from ticker-0333 - it moves the window to the unobservable
  fullscreen Space).
- No game screen was ever reached. No help bubble seen, no Help
  All pressed, nothing claimed, nothing spent. The alliance-help
  open questions (daily help cap, what helpers and helped
  players each receive) stay open.

## Blocker accounting (rule R2) - NINTH consecutive occurrence

- This is the NINTH consecutive ticker pass hitting this
  blocker (ticker-0333 harvest, ticker-0443 radar,
  ticker-0534 help, ticker-0722 probe, ticker-0804 probe,
  ticker-0834, ticker-0904, ticker-0934 probe, then this
  help unit). Per R2 the third occurrence already triggered
  its actions, and the fourth was to be reported to the owner
  as a process failure: the owner was told after the 2nd and
  after the 3rd occurrence that he must exit fullscreen or
  restart the game at the Mac; as of 10:15 PT there is no
  evidence he has done so. The standing route change stands:
  NO game unit runs until the window is recovered. The pass
  stops after this unit rather than cascading failed units.
- No game unit has executed successfully since ticker-0214
  gifts at 02:14 PT (176 Regular + 67 Premium claimed) -
  about eight hours of routine (mail, help, gifts, harvest,
  VIP, donations, trucks, training) now missed.

## Closing

- Unit help-2026-11-17-0630 completed FAILED (blocker_category
  e, repeated blocker). Tracker untouched; the next tick
  re-produces help.
- Sync: reaped 0, expired 5, due 22, produced 0, already queued
  22 (mail, help, gifts, harvest, vip, passes,
  daily-missions, secrets, treasures, radar, survivors,
  trucks, train, training, donations, events, arms-race,
  star-ceremony, duel-score, scout, scout-midday). Stats:
  inbox 71, claimed 0, done 2314; newest finished
  2026-11-17T18:04:46Z (the stats read itself, about
  0 minutes before the read - this pass's own failed unit
  is the newest done entry).
- Zombie chain stays closed (event ended 2026-10-30, unit 066;
  no seeding - the last live check, 2026-11-15, found no
  Zombie Invasion tab; most recent done zombie unit
  zombie-invasion-zombie-2026-11-10-037 finished
  2026-11-15T02:35:26Z failed, cleared false).
- Own PRs first: VPS SSH still Permission denied (publickey),
  so the VPS gh check could not run. The public PR list was
  read instead (browser.open, 2026-11-17T18:13Z): exactly
  three open PRs - #711 (knowledge), #708 (records
  2026-11-12), #425 (feat tools) - none owned by this job,
  no PR for records/2026-11-17 exists. No question addressed
  to this job, nothing to fix.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey), about 117 hours into the outage; record
  committed locally only on ticker-1004-1117-delivery,
  UNPUSHED, push pending VPS recovery. No PR opened for
  records/2026-11-17.
- Issue filing owed at VPS recovery: repeated failure mode
  "game window lost in fullscreen Space, control channel blind"
  (class tooling) - gh is unreachable while VPS SSH is down,
  so no issue number exists yet. Same owed item as ticker-0443,
  ticker-0534, ticker-0722 and ticker-0804.
