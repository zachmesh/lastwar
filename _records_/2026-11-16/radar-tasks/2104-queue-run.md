---
title: Radar tasks 2026-11-16 ticker-2102 done, stack day, Mac back online
created: 2026-11-17T05:10:00Z
modified: 2026-11-17T05:10:00Z
version: 1.0.0
description: Radar unit radar-2026-11-16-1803 done, duel day 2 stack posture, Mac mini online again
status: done
grounded_in:
  - source: tools/duel.py --json, 2026-11-17T05:04Z
  - source: Last War on Zhen's Mac mini, radar screen read 2026-11-17T05:10Z
  - source: GitHub public pull request list for zachmesh/lastwar via browser.open, 2026-11-17T05:09Z
  - source: VPS SSH probe, 2026-11-17T05:03Z
---

# Radar tasks 2026-11-16 ticker-2102 done, stack day, Mac back online

- Executor: ticker-2102
- Unit: radar-2026-11-16-1803, regular radar, activity radar-tasks, priority 2, est 5 minutes
- Session window: 21:04-21:10 local, token held 21:03-21:19 local

## What happened

- The Mac mini (Zhen's Mac mini, 1c817413-83e2-0545-cb90-36d5e096a6bd)
  is ONLINE again - device.list shows online, last_seen
  2026-11-17T05:00:41Z, and the game was driven live in this unit.
  This is the first unit to finish done since Nov 14 18:35 PT: the
  planner-2040 run counted 237 done files since then with 0 done
  (194 expired, 43 failed), and ticker-1949's harvest-1803 failure
  was the 29th consecutive ticker pass to fail on the offline Mac.
  The failure streak is broken by this unit.
- On entry a Monica dialog announced the Champion Duel has begun;
  one tap at the bottom of the dialog dismissed it. Base HUD before
  radar entry: food 639.6M, iron 1.0G, coin 27.7M, power
  149,482,045.

## Duel posture - live read overrides the unit's stale window label

- tools/duel.py at 21:04 PT: duel day 2, Base Expansion, radar
  posture STACK. Day ends 18:00 PT Nov 17.
- The unit's window field said "duel day 1 - radar release" - it
  was stamped at production (14:22Z) while day 1 was still running.
  The 19:00 reset moved the duel to day 2 before this unit ran, so
  the live read governs: STACK posture, no claims, no pins tapped.

## Radar reads (screen-verified, 21:10 PT)

- Lv.13, radar points 468, stored 0/40, stamina 55 (lightning pill,
  partial green fill, cap 120).
- Restore line: 12 Radar Task(s) will be restored in 02:41:22.
- Radar sweep bar top centre reads 100% (what it measures is
  unverified - recorded as observed, not interpreted).
- Bottom bar presents Claim All only: "5 task rewards can be
  claimed". No Quick Execute offer - the 2026-10-31 trap shape,
  recorded here by name with the pending count 5. Stored reads
  0/40, so no ordinary task was executable anyway and nothing was
  blocked in practice; the 5 pending rewards carry into the next
  unit's opening read and await the day-3 release.
- Nothing executed, nothing claimed, nothing spent - correct for a
  stack day with an empty store.

## Pin inventory (stack posture - inventoried, not tapped)

Six pins plus one unidentified round icon, positions in normalized
0-1000 coordinates:

- Blue pickaxe pin, top-right, red dot - norm 712,331.
- Purple skull pin, centre-left, no red dot - norm 436,489.
- Orange map pin, centre-right, red dot - norm 615,489.
- Purple skull pin, bottom-left, red dot - norm 245,652.
- Orange pickaxe pin, bottom-centre, red dot - norm 439,652.
- Purple pickaxe pin, bottom-right, red dot - norm 634,652.
- Round animal-face icon, bottom-left map edge - norm 89,736,
  unidentified, not tapped (may be a map control, not a pin).

## Own PRs first

- VPS route down (SSH Permission denied, see below), so the check ran
  through the public GitHub pull request list for zachmesh/lastwar.
- Open PRs, unchanged since Nov 12: #711 (knowledge, Owner
  lastwar-knowledge-organizer), #708 (records 2026-11-12, Owner
  lastwar-pr-integrator), #425 (tooling, Owner
  lastwar-tool-developer). None is owned by this job; no open PR
  for records/2026-11-15 or records/2026-11-16. No question
  addressed to this job, nothing to fix.
- Limitation: the text fetch of the PR list shows titles only; no new
  question addressed to the ticker is visible.

## Sync and seeding

- Sync: reaped 0, expired 0, due 22, produced 0 (all 22 already
  queued); completion marker reaped: harvest-2026-11-16-1803.
  Branch reconcile skipped with a warning: fetch of
  records/2026-11-16 failed (remote ref missing), issue #446.
- Zombie seeding no-op: the Zombie Invasion event ended at about the
  19:00 reset on 2026-10-30 (unit 066); chain zombie-2026-10-28 is
  closed, and no fresh chain is seeded until a Zombie Invasion tab is
  seen live in the Events hub again.

## Delivery blocked

- VPS SSH still Permission denied (publickey), probed 21:03 PT, about
  104.3 hours into the break (since ~12:46 PT Nov 12). No bundle, no
  push, no PR. The 15:00 PT integrator batch point passed with PR
  #708 still open and no records PR for 2026-11-16.
- Delivery PARTIAL: this record is committed locally on delivery
  branch ticker-2102-1116-delivery, UNPUSHED, push pending VPS
  recovery; the live-tree mirror and the identical backup in the goal
  hidden_files are in place.
- No Slack sync. Chat report owed per the ticker rule (previous pass
  also access-failed, and this pass breaks the streak with the first
  done unit since Nov 14); this pass's final message carries it.
