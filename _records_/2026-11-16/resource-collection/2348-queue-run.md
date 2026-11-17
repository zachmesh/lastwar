---
title: Resource Collection 2026-11-16 ticker-2348 partial, no bubbles collected
created: 2026-11-17T08:14:00Z
modified: 2026-11-17T08:14:00Z
version: 1.0.0
description: Harvest unit harvest-2026-11-16-2203 partial, base checked, no ready bubbles collected
status: unverified
grounded_in:
  - source: live game screens on Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd), 2026-11-17T07:58Z to 08:13Z, four screenshots
  - source: tools/queue.py sync and stats, 2026-11-17T07:50Z
  - source: GitHub connector list_pull_requests on zachmesh/lastwar, 2026-11-17T07:51Z
  - source: VPS SSH probe, 2026-11-17T07:49Z
---

# Resource Collection 2026-11-16 ticker-2348 partial, no bubbles collected

- Executor: ticker-2348
- Unit: harvest-2026-11-16-2203, regular harvest, activity resource-collection, priority 3, est 9 minutes, expires 2026-11-17T10:03:00Z (02:03 PT Nov 17)
- Session window: 23:48-00:14 local, token held 23:58-00:14 local

## What happened

- The Mac mini is back ONLINE (device.list, last_seen 2026-11-17T07:31:15Z) after the Nov 12-16 outage. Last War was running on the Secret Command Post screen, left over from the ticker-2236 secrets unit. The back arrow returned to the base screen.
- Base HUD read live at 23:59 and again at 00:13, unchanged across the unit: Food 643.5M, Iron 1.0G, Coin 27.7M, Gold 14.72K, Power 149,482,045, diamonds 8,096, stamina 88 rising to 89 by regeneration. No spend, no items used.
- Two candidate icons were tapped at freshly measured centres and neither collected anything:
  - Yellow diamond over the right-side building, window (565, 435), display (638, 466): no change, icon still present, totals unchanged.
  - Small yellow icon over the purple building, window (464, 574), display (537, 605): the tap selected the Wild Rhythm Lv.1 building and panned the camera; no collection, totals unchanged.
- Both icons are therefore NOT ready resource bubbles (or not bubbles at all). The next harvest unit must not re-tap them; it should sweep the base for genuine bobbing bubbles instead.
- Near-miss, cancelled safely: after the camera pan, a tap meant to deselect on empty ground at window (300, 700) landed on a building control and opened a confirm dialog ("want to retrait it?", Cancel / Confirm). Cancel was tapped at once; the dialog closed, the base screen returned, nothing was retreated, removed or spent. Lesson for the next unit (rule R2): never tap blind after a camera pan - re-ground the view first, and treat any building-selection icons as off-limits in a harvest unit.
- The 15 minute unit cap was reached with the full-base sweep and the Armed Truck check still unexecuted, so the unit closes partial. The tracker is untouched; the next tick re-produces the harvest regular.

## Own PRs first

- VPS route down (SSH Permission denied, see below), so the check ran through the GitHub connector (list_pull_requests on zachmesh/lastwar).
- Open PRs: #711 (knowledge, Owner lastwar-knowledge-organizer), #708 (records 2026-11-12, Owner lastwar-pr-integrator), #425 (tooling, Owner lastwar-tool-developer). Heads and updated_at unchanged since Nov 12. None is owned by this job; no open PR for records/2026-11-16. No question addressed to this job, nothing to fix. PR comment reads were not attempted - the live connector exposes list/get tools only for this check, as in the ticker-2236 pass.

## Sync and seeding

- Sync: reaped 0, expired 0, due 22, produced 0, already queued 22 (mail, help, gifts, harvest, vip, passes, daily-missions, secrets, treasures, radar, survivors, trucks, train, training, donations, events, arms-race, star-ceremony, duel-score, scout, scout-midday); completion markers reaped: passes-2026-11-16-1857, secrets-2026-11-16-1857. Branch reconcile skipped with a warning: fetch of records/2026-11-16 failed (remote ref missing), issue #446.
- Zombie seeding no-op: the Zombie Invasion event ended (live check by unit zombie-invasion-zombie-2026-11-10-037, finished 2026-11-15T02:35:26Z, no Zombie Invasion tab in the Events hub), the chain zombie-2026-11-10 stays closed, and no zombie-invasion unit sits in inbox or claimed. No fresh chain is seeded until a Zombie Invasion tab is seen live in the Events hub again.

## Delivery

- VPS SSH still Permission denied (publickey), probed 07:49Z, about 106.4 hours into the break (outage since about 12:46 PT 2026-11-12; owner chose the IONOS console route 2026-11-14 17:37 PT; no fix yet). Push and PR are blocked.
- Delivery PARTIAL: record committed locally on ticker-2348-1116-delivery, UNPUSHED, push pending VPS recovery; mirror copy in the live tree plus identical backup in the goal hidden_files. No Slack sync.
