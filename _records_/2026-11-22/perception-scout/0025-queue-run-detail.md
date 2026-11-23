---
title: Perception scout queue run 0025 detail
created: 2026-11-23T08:30:00Z
modified: 2026-11-23T08:30:00Z
version: 1.0.0
description: Sidecar with the taps and readings of the growth snapshot T2 run 0025
status: run-partial
grounded_in:
  - source: events.jsonl of run 20261123T082546Z-831319 and frames step-0003.png to step-0005.png, 2026-11-23T08:25Z to 08:26Z
---

# Detail for perception scout run 0025

Companion to [0025-queue-run.md](0025-queue-run.md). Pixel points are in the 1920x1080
screen frame, game window at about x 73-715.

## Taps, in order

| Step | Time Z | Action | Effect |
|---|---|---|---|
| 1 | 08:25:51 | click (250,650), empty ground, wait 1 s | Hospital radial menu closed |
| 2 | 08:26:00 | click (518,532), upper right tent roof | tag Barracks Lv.20 |
| 3 | 08:26:10 | click (250,650), empty ground | selection cleared |
| 4 | 08:26:17 | click (474,558), lower right tent roof | tag Barracks Lv.24 |
| 5 | 08:26:24 | click (468,615), pistol, wait 1 s | toast Drill Ground Full |
| 6 | 08:26:33 | click (570,800), red troop formation | tag Drill Ground Lv.28 |
| 7 | none | final report | base, Drill Ground menu open |

## Readings

| Item | Reading |
|---|---|
| HUD | food 638.0M, iron 1.0G, coin 9.6M, 26.72K, diamonds 11,136 |
| Total Power | 150,211,809 |
| Barracks Lv.20 tag | seen at the upper right tent, idle status not read |
| Barracks Lv.24 pistol | toast "Drill Ground Full: Unable to add more units.", no panel |
| Drill Ground tag | Lv.28 |
| Drill Ground menu | blue details, blue officer hat, green up arrow, none tapped |
| Unit Count | not re-read; +9211 at 07:48Z |

## Counters

- Steps 7, actions done 12, refused 0, cost 0.094026 USD, model time 48.5 s.
