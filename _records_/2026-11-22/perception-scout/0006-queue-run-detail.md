---
title: Perception scout queue run 0006 detail
created: 2026-11-23T08:12:00Z
modified: 2026-11-23T08:12:00Z
version: 1.0.0
description: Sidecar with the taps, panel rows and counters of the growth snapshot run 0006
status: run-done
grounded_in:
  - source: events.jsonl of run 20261123T080610Z-7faa88 and frame step-0004.png, 2026-11-23T08:06Z to 08:07Z
---

# Detail for perception scout run 0006

Companion to [0006-queue-run.md](0006-queue-run.md). Pixel points are in the 1920x1080
screen frame, game window at about x 73-715.

## Taps, in order

| Step | Time Z | Action | Effect |
|---|---|---|---|
| 1 | 08:06:17 | click (450,634), Lv.30 tent roof, wait 1 s | tag Barracks Lv.30 |
| 2 | 08:06:21 | click (448,680), pistol, wait 2 s | TRAIN UNITS, no toast |
| 3 | 08:06:31 | click (611,281) panel X, click (383,585) Lv.27 tent roof | tag Barracks Lv.27 |
| 4 | 08:06:37 | click (381,632), pistol, wait 2 s | TRAIN UNITS, no toast |
| 5 | 08:06:45 | click (611,281), panel X | base |
| 6 | none | final report | base |

## Panel rows

| Row | Lv.30 | Lv.27 |
|---|---|---|
| Power | 1647 | 1352 |
| Morale | 750.0 | 625.0 |
| Squad Load Capacity | 2200 | 2000 |
| Unit HP | 4779.05 | 4167.45 |
| Unit Attack | 38.87 | 33.87 |
| Unit Defense | 7.96 | 6.96 |
| Selected tier | Lv.10 | Lv.9 |
| Batch | Lv.10 x793 | Lv.9 x726 |
| Time left | 1d 03:12:00 | 11:49:49 |
| Finish Z | 2026-11-24 11:18:31 | 2026-11-23 19:56:34 |

## Tier counts

| Tier | Count |
|---|---|
| Lv.6 | cut off |
| Lv.7 | 1,116 |
| Lv.8 | 2,141 |
| Lv.9 | 1,878 |
| Lv.10 | 35.1K (locked on the Lv.27 panel) |

## Counters

- Steps 6, actions done 12, refused 0, cost 0.078709 USD, model time 29.7 s.
