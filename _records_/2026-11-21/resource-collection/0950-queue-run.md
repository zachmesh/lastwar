---
title: Harvest queue run 0950
created: 2026-11-21T17:52:00Z
executor: ticker-0934
unit: harvest-2026-11-21-0603
status: failed
---

# Harvest - 0950 queue run (failed)

Session 09:50-09:52 PT (17:50-17:52Z), executor ticker-0934, unit
harvest-2026-11-21-0603 (planned for 2026-11-21 14:03Z, expires
2026-11-21 18:03Z). Fourth consecutive game unit blocked by the
fullscreen precondition (radar 0201 at 02:01 PT, harvest 0312 at
03:12 PT, radar 0433 at 04:33 PT, harvest 0950 at 09:50 PT).

## What happened

- Mac mini online (device list 09:45 PT, last seen 16:38:20Z);
  computer session cc-6 started 09:50 PT. Last War IS running
  (window 96101, pid 95844) at the base view. No login was
  demanded, no "active on a different device" dialog appeared.
- Blocker - the LastWar window is in native fullscreen 1920x1080
  on its own Space (on_current_space false). Window state
  UNCHANGED since the 02:01 PT read: same window id, same pid,
  same geometry. Per the radar-tasks 1.92.0 stop rule (retry only
  on a changed window state), NO tap route was re-attempted this
  pass: the coordinate-click, menu Exit Full Screen,
  activate-raise and batched routes were each refused in this
  exact state at 02:01, 03:12 and 04:33 PT, and re-running them
  would repeat a failed method with no pivot (R2). Today's
  channel guidance re-confirms it: "Pointer input, scrolling and
  drags need it on the user's Space."
- Probe only: activate selected the window without switching
  Spaces (observation 8A98FF74-F7C3-4428-B91E-493BBC0D4C96);
  screen capture at 09:50 PT reads live: food 665.3M, iron 1.0G,
  coin 50.2M, diamonds 17.72K, 4,706; "Alliance Gifts received!"
  toast; Component Factory Lv.20; many green/white resource
  bubbles visible over the farmland and the gold buildings,
  uncollected. HUD identical to the 03:14 PT and 04:33 PT reads -
  no play between units.
- Result: NO game action taken. No bubble collected, no truck
  check, no stamina spent, no items used. The harvest target was
  not met on any line. Tracker untouched (failed).
  Blocker_category c (matching the 0433 classification of the
  same mode; the 0201/0312 failures used f - carried as recorded,
  not harmonised, per KO-0432).

## Remaining work

- Many resource bubbles remain visible and uncollected; the Armed
  Truck loot state is still unchecked. The next tick re-produces
  this regular as a fresh unit (failed: tracker untouched) - but
  every further unit will hit the same precondition until the
  window state changes, so the next pass should probe state first
  and fail without input again unless the window is windowed.
- The owner action that unblocks this in seconds: on the Mac mini,
  switch to the Last War window or exit fullscreen (menu View ->
  Exit Full Screen). An Issue for this failure mode (fullscreen
  off-Space window blocks the ticker) is owed once the gh route
  via the VPS returns; it cannot be filed now (VPS SSH still
  Permission denied, gh unauthenticated locally) - same standing
  note as 0159/0312/0433. The fullscreen blocker has now stopped
  four consecutive game units; it appeared between 00:49 PT
  (ticker-0048 tapped fine) and 02:01 PT and has persisted since,
  now about 8 hours.

## Delivery

- VPS SSH still Permission denied (publickey) - probed 09:45 PT
  at pass start and again at delivery, the outage since
  2026-11-12 continues (about 213 hours). Push and PR delivery
  are impossible this pass; the commit sits on the local
  records/2026-11-21 branch (from main 22601972), push pending
  VPS recovery.
- Own PRs first: open PRs via the GitHub connector
  (list_pull_requests, zachmesh/lastwar) are exactly 3, all
  unchanged since 2026-11-12 - #711 knowledge fold (Owner
  lastwar-knowledge-organizer), #708 records 2026-11-12 (Owner
  lastwar-pr-integrator), #425 tools log gate (Owner
  lastwar-tool-developer); no PR for records/2026-11-21, none
  names this job, nothing to address.
- Zombie Invasion not seeded (event ended, last live check
  2026-11-15). Sync produced 0 new units (22 due, all already
  queued); pool inbox 77, claimed 0, done 2741 at pass start;
  sync reaped the radar-2026-11-21-0203 completion marker.
- Loop closed after this one unit: the blocker is global to the
  session (every due unit would fail on the same precondition),
  so no second unit was attempted.

## Ordering note

- Newest-record re-read first (day INDEX through the 09:32 KO
  pass), device probe second (Mac online), then sync, then
  token - the fully-honoring order. Token acquired 09:49 PT,
  unit claimed 09:49 PT, probe 09:50 PT, token released at pass
  end.
