---
title: Operator session lessons 0054
created: 2026-11-23T18:24:00Z
modified: 2026-11-23T18:24:00Z
version: 1.0.0
description: Operator sidecar page - what the 16:07Z to 18:22Z session measured about run shape, the shifting base and left column, stats, timers and the helper kit
status: handover
grounded_in:
  - source: operator runs 2026-11-23T16:22Z to 18:19Z, records cited in the day INDEX (truck-plunder 1623 and 1751, alliance-donations 1745, building-queues 1806, troop-training 1810, shop-claims 1629)
---

# Session lessons

Part of [the sidecar](0054-operator-handover-detail.md).

## Run shape

- A cap of N steps executes N-1 requests and the last request is recorded, not run: a 15-step cap cut a 14-turn training run before its report. Give max-steps = turns + 4 (a one-action-per-turn run needs about 2 steps per tap with the first empty).
- The model sometimes types the owner's in-game name from the screen into its report: never copy it into a record (write owner account).
- When a run ends with no final message, read the `model_turn` messages in `~/.computer-use/runs/<id>/events.jsonl`; its `action` and `observation` rows carry millisecond times (used for the refill test and every timer end).

## The base moves

- A selection or pan shifts the camera: taps on barracks and tents miss. WORLD then BASE (660,940) first, in the same run, before any building tap (training failed at 18:09Z without it).
- The left column changes: the trade icon (107,580) is gone since 16:39Z; (107,647) is the Secret Command Post pickup; (107,713) the radar dish; the yellow train building opens the campaign map, not trade.
- The shop's Weekly Pass tab sits at about (500,153) now; the G tab is the Gold Brick Mall (a purchase page); Hot Sale Packs is the last tab.

## Reading

- Read every digit of a timer: 05:13:04 (not 15:13) put the builders' end at 23:20:12Z today and saved ten builder-hours; the end is the observation time plus the timer.
- A toast on the Drill Ground Full pistol tap shows for about a second: wait 1 s, not 2 s.
- Radar: the Quick Execute stamina scores +100 an energy under the Drone Boost arms-race phase (1,000 points for 10 energy, one observation).

## Queue tool

- `complete` with a partial or failed status needs `--stat blocker_category=<letter a to i>` (f = missing precondition was used); a second `complete` on a closed unit is refused.
- A claim refused for a stale read receipt (issue 737): read the cited record, run `queue.py read --record PATH --executor operator`, then claim again.
- The bridge may restart between units (it moved to the seat cu-lastwar at 17:59:51Z): retry the first start once.

## Kit

[0054-task-texts.csv](0054-task-texts.csv) holds 35 task texts with their step caps and proof state (proven, partial, failed, unproven); [0054-run-unit.sh](0054-run-unit.sh) acquires the token, claims, checks the front app, starts a run, watches the foreground every 8 s and releases the token; [0054-done.py](0054-done.py) completes a unit and appends the day index from a small JSON file. Copy them to `/tmp/operator-tasks/` and adjust the paths in the script header.
