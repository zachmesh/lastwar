---
title: Radar tasks queue run
created: 2026-11-17T12:50:00Z
executor: ticker-0443
unit: radar-2026-11-17-0203
regular: radar
status: failed
---

# Radar tasks 2026-11-17 04:43-05:00 PT (ticker-0443)

Stack day (duel day 2, Base Expansion, radar posture STACK per
tools/duel.py --json: complete tasks but do NOT claim). Unit
claimed 04:46 PT, device session cc-11 on the Mac mini.

## Access failure - game window lost (same blocker as ticker-0333)

- Mac mini ONLINE (device.list last_seen 2026-11-17T11:30:28Z).
  LastWar IS in running_apps (com.lastwar.ios) but exposes NO
  window: three open_app attempts (04:47, 04:49, 04:52 PT, each
  outcome_unknown), one activate (ax_windows_empty), and
  list_windows four times all show the same 10 windows with no
  LastWar entry. computer.observe reports observation_unavailable;
  screen.snap the same.
- This is the SAME state ticker-0333 left at 03:41 PT: its green
  zoom click moved the game window to a native fullscreen Space
  where this control channel cannot see it (ax_windows_empty;
  app still running). Its recovery tries (Ctrl+Right, F3,
  Cmd+Tab refused) also failed.
- Pivot tried this pass: open_app "Mission Control" (04:59 PT,
  outcome_unknown, no observable window after). No further
  recovery route exists through this channel - no shell on the
  Mac, no Dock click available without a selected window, and
  Cmd+Tab is refused by the channel as a system command.
- No game screen was ever reached. No HUD read, no radar entry,
  no tasks executed, nothing claimed, nothing spent. The 01:01
  unit's open questions (stored 7/40 unmoved after Quick
  Execute; pending 10 vs stored 7) stay open for the release-day
  unit, which now also inherits a possibly-stale pin inventory.

## Blocker accounting (rule R2)

- This is the SECOND consecutive failed unit with this blocker
  (ticker-0333 harvest-2026-11-17-0203, then this radar unit).
  Per R2 the second consecutive partial/failed unit with the
  same blocker must arrive with a changed method - the Mission
  Control pivot was that change and it failed. The THIRD
  occurrence writes the blocker into the activity metadata and
  changes the entry route before any further unit of that type
  runs; a fourth identical failure is a process failure to
  report to the owner.
- Issue filing owed at VPS recovery: repeated failure mode
  "game window lost in fullscreen Space, control channel blind"
  (class tooling) - gh is unreachable while VPS SSH is down,
  so no issue number exists yet.

## Closing

- Unit radar-2026-11-17-0203 completed FAILED (blocker_category
  f, missing precondition - no game window). Tracker untouched;
  the next tick re-produces radar. Stamina, pins and stored
  count all unread this pass.
- Sync: 22 due, 0 produced (all already queued), 0 expired, 0
  reaped; completion marker reaped harvest-2026-11-17-0203.
  Zombie chain stays closed (event ended 2026-10-30, unit 066;
  no seeding - the last live check, 2026-11-15, found no
  Zombie Invasion tab).
- Own PRs first: VPS SSH still Permission denied (publickey),
  so the VPS gh check could not run. Per the day INDEX, the
  open PRs re-verified by other passes today via the
  authenticated GitHub connector are #711, #708, #425 only,
  none owned by this job; no PR for records/2026-11-16 or
  records/2026-11-17 exists.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey), about 112 hours into the outage; record
  committed locally only on ticker-0443-1117-delivery,
  UNPUSHED, push pending VPS recovery. No PR opened for
  records/2026-11-17.
