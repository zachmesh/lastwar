---
title: Resource Collection 2026-11-17 ticker-0333 failed, game window lost after zoom click
created: 2026-11-17T11:41:00Z
modified: 2026-11-17T11:41:00Z
version: 1.0.0
description: Harvest unit harvest-2026-11-17-0203 failed, Last War window unrecoverable after green zoom click moved it to a fullscreen Space
status: unverified
grounded_in:
  - source: live device reads on Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd), 2026-11-17T11:30Z to 11:40Z, two screenshots of the Alliance Gifts screen
  - source: tools/queue.py sync and stats, 2026-11-17T11:34Z
  - source: GitHub connector list_pull_requests on zachmesh/lastwar, 2026-11-17T11:33Z
  - source: VPS SSH probe, 2026-11-17T11:33Z
---

# Resource Collection 2026-11-17 ticker-0333 failed, game window lost after zoom click

- Executor: ticker-0333
- Unit: harvest-2026-11-17-0203, regular harvest, activity resource-collection, priority 3, est 9 minutes, expires 2026-11-17T14:03:00Z (06:03 PT Nov 17)
- Session window: 03:34-03:40 local, token held 03:34-03:49 local

## What happened

- The Mac mini is ONLINE (device.list, last_seen 2026-11-17T11:30:28Z). Last War was running, window 351 (642x951) on the Alliance Gifts screen, left over from the ticker-0214 gifts unit (which claimed 176 Regular + 67 Premium gifts at 02:14 PT; the 18 gifts visible now accumulated since, and belong to the gifts regular, not this unit).
- Two back-arrow taps at (40, 897) showed no change. Two causes, both mine: the window was in background mode, covered by Chrome ("Recharge Center - LASTWAR"), and background clicks do not reach game controls (same failure as the ticker-2236 Hot Deals Go button); and computer.control coordinates are normalized 0-1000 within the window, so (40, 897) landed at pixel (26, 853), just above the back-arrow button (pixels about x 8-72, y 868-928). The correct normalized centre is about (62, 944). Per rule R2 the tap method ended after the second no-change tap.
- Switched variant: clicked the green zoom button (element 4) to bring the covered window forward. The window left the Accessibility window list (geometry_mismatch, size_delta 16-64) and has not been enumerable since: list_windows shows no LastWar window, activate and open_app both fail with ax_windows_empty, computer.observe reports no current target. The app is still running (environment.describe). The window most likely moved to a native fullscreen Space, where this control channel cannot see or select it.
- Recovery attempts, all failed:
  - Ctrl+Right Arrow was delivered to Finder as a plain Right Arrow (column-view navigation); F3 likewise navigated Finder instead of opening Mission Control.
  - Cmd+Tab was refused outright by the channel as a macOS system command (app switching, Spaces, Dock and Spotlight shortcuts are not sent).
  - Re-selecting Finder and re-listing windows changed nothing; the LastWar window stays unbound. No stuck modifier: the Command hold from the refused batch auto-released (release_key reports no matching key held).
- The unit closes failed: no HUD read, no bubbles collected, no Armed Truck check, nothing spent. The tracker is untouched; the next tick re-produces the harvest regular. The pass stops after this unit rather than cascading failed units.
- Lessons for the next pass (record-level; R2 metadata write needs a third occurrence of the same blocker, this is the first):
  - Never click the green zoom button while the game window is covered or in the background; it moves the window to an unobservable fullscreen Space.
  - Background clicks do not reach game controls: bring the window forward first, and only then tap. A title-bar click did not raise it; try the Dock icon or relaunch the app if the window is still unbound.
  - Re-ground every tap target in normalized 0-1000 coordinates; the back arrow centre is about (62, 944).

## Own PRs first

- VPS route down (SSH Permission denied, see below), so the check ran through the GitHub connector (list_pull_requests on zachmesh/lastwar).
- Open PRs: #711 (knowledge, Owner lastwar-knowledge-organizer), #708 (records 2026-11-12, Owner lastwar-pr-integrator), #425 (tooling, Owner lastwar-tool-developer). Heads and updated_at unchanged since Nov 12. None is owned by this job; no open PR for records/2026-11-16 or records/2026-11-17. No question addressed to this job, nothing to fix. PR comment reads were not attempted - the live connector exposes list/get tools only for this check, as in the ticker-2236 pass.

## Sync and seeding

- Sync: reaped 0, expired 0, due 22, produced 0, already queued 22 (mail, help, gifts, harvest, vip, passes, daily-missions, secrets, treasures, radar, survivors, trucks, train, training, donations, events, arms-race, star-ceremony, duel-score, scout, scout-midday); completion markers reaped: gifts-2026-11-16-2230. Branch reconcile skipped with a warning: fetch of records/2026-11-17 failed (remote ref missing), issue #446.
- Zombie seeding no-op: the Zombie Invasion event ended (live check by unit zombie-invasion-zombie-2026-11-10-037, finished 2026-11-15T02:35:26Z, no Zombie Invasion tab in the Events hub), the chain zombie-2026-11-10 stays closed, and no zombie-invasion unit sits in inbox or claimed. No fresh chain is seeded until a Zombie Invasion tab is seen live in the Events hub again.

## Delivery

- VPS SSH still Permission denied (publickey), probed 11:33Z, about 110.9 hours into the break (outage since about 12:46 PT 2026-11-12; owner chose the IONOS console route 2026-11-14 17:37 PT; no fix yet). Push and PR are blocked.
- Delivery PARTIAL: record committed locally on ticker-0333-1117-delivery, UNPUSHED, push pending VPS recovery; mirror copy in the live tree plus identical backup in the goal hidden_files. No Slack sync.
