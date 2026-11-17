---
title: Alliance Help queue run
created: 2026-11-17T14:14:00Z
executor: ticker-0534
unit: help-2026-11-17-0230
regular: help
status: failed
---

# Alliance help 2026-11-17 06:06-06:14 PT (ticker-0534)

Unit claimed 06:06 PT, device sessions cc-12 and cc-13 on the Mac mini.
Token held 06:05-06:14 PT, released at pass end.

## Access failure - game window lost (same blocker as ticker-0333 and ticker-0443)

- Mac mini ONLINE (device.list last_seen 2026-11-17T13:31:32Z).
  LastWar IS in running_apps (com.lastwar.ios) but exposes NO
  window: list_windows twice shows the same 10 windows with no
  LastWar entry; open_app "Last War" (no match), open_app
  "LastWar" (outcome_unknown, no window appeared), open_app
  "Last War: Survival" (no match); activate LastWar twice
  (ax_windows_empty), the second time in a fresh session cc-13
  after ending cc-12; computer.observe and screen.snap both
  report observation_unavailable.
- NEW evidence this pass: the blindness is no longer game-only.
  Activating ordinary windows also fails now - Finder window 28
  and Chrome window 125 both refuse with geometry_mismatch
  (origin_delta 256+, size_delta 256+, agent_display=false),
  and a Ctrl+Right keypress is refused for lack of a bound
  target (input_dispatched=false). The control channel cannot
  bind ANY window on the Mac right now, not just the game
  window. In ticker-0333 the channel could still select Finder;
  that route is now closed too.
- No game screen was ever reached. No help bubble seen, no Help
  All pressed, nothing claimed, nothing spent. The alliance-help
  open questions (daily help cap, what helpers and helped
  players each receive) stay open.

## Blocker accounting (rule R2) - THIRD consecutive occurrence

- This is the THIRD consecutive failed unit with this blocker
  (ticker-0333 harvest-2026-11-17-0203, ticker-0443
  radar-2026-11-17-0203, then this help unit). Per R2 the third
  occurrence triggers three actions:
  - (a) Write the blocker into the activity metadata. DEFERRED
    with reason: the blocker is cross-type (harvest, radar,
    help - three different types, one entry failure), so it
    does not belong in alliance-help metadata, and the proper
    home is a shared entry-route note (tier 2, recording-rules
    Device access or the queue design), which cannot ride this
    tier-1 records commit. The write is owed work for the
    retro / the tooling issue below, not skipped.
  - (b) Change the entry route before any further unit of that
    type runs. The route change: NO further game unit can run
    until the window is recovered. The green zoom button must
    never be clicked (learned in ticker-0333 - it moves the
    window to the unobservable fullscreen Space). Recovery
    needs owner action at the Mac (leave fullscreen via View
    menu / Mission Control) or a fresh app launch into a
    normal Space; the open_app relaunch was already tried this
    pass and produced no bound window. The pass stops after
    this unit rather than cascading failed units.
  - (c) Name it in the day round summary - see the day INDEX
    entry for this run.
- A FOURTH identical failure is a process failure to report to
  the owner (R2). The next pass that hits this blocker must
  report it as such, not as another routine failed unit.
- Issue filing owed at VPS recovery: repeated failure mode
  "game window lost in fullscreen Space, control channel blind"
  (class tooling) - gh is unreachable while VPS SSH is down,
  so no issue number exists yet. Same owed item as ticker-0443.

## Closing

- Unit help-2026-11-17-0230 completed FAILED (blocker_category
  e, repeated blocker). Tracker untouched; the next tick
  re-produces help.
- Sync: reaped 0, expired 4, due 22, produced 0, already queued
  22 (mail, help, gifts, harvest, vip, passes,
  daily-missions, secrets, treasures, radar, survivors,
  trucks, train, training, donations, events, arms-race,
  star-ceremony, duel-score, scout, scout-midday);
  completion markers reaped: radar-2026-11-17-0203. Stats:
  inbox 69, claimed 0, done 2296; newest finished
  2026-11-17T12:50:13Z (74 minutes before the stats read);
  stalled priority-1: vip-2026-11-16-1800, age 23.7h.
- Zombie chain stays closed (event ended 2026-10-30, unit 066;
  no seeding - the last live check, 2026-11-15, found no
  Zombie Invasion tab; most recent done zombie unit
  zombie-invasion-zombie-2026-11-10-037 finished
  2026-11-15T02:35:26Z failed, cleared false).
- Own PRs first: VPS SSH still Permission denied (publickey),
  so the VPS gh check could not run. The public PR list was
  read instead (browser.open, 2026-11-17T14:05Z): exactly
  three open PRs - #711 (knowledge), #708 (records
  2026-11-12), #425 (feat tools) - none owned by this job,
  no PR for records/2026-11-17 exists. No question addressed
  to this job, nothing to fix.
- Push and PR blocked - VPS SSH still Permission denied
  (publickey), about 113 hours into the outage; record
  committed locally only on ticker-0534-1117-delivery,
  UNPUSHED, push pending VPS recovery. No PR opened for
  records/2026-11-17.
