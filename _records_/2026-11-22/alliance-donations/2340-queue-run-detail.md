---
title: Alliance donations queue run 2340 detail
created: 2026-11-23T07:46:00Z
modified: 2026-11-23T07:46:00Z
version: 1.0.0
description: Sidecar with the taps, count chain and counters of donations run 2340
status: run-partial
grounded_in:
  - source: events.jsonl of run 20261123T074058Z-7f1217 and frames step-0003.png and step-0006.png, 2026-11-23T07:40Z to 07:42Z
---

# Detail for donations run 2340

Companion to [2340-queue-run.md](2340-queue-run.md). Pixel points are in the 1920x1080
screen frame, game window at about x 73-715.

## Taps, in order

| Step | Time Z | Action | Effect |
|---|---|---|---|
| 1 | 07:41:04 | click (670,708), Alliance, wait 2 s | Alliance hub |
| 2 | 07:41:09 | click (514,677), Alliance Techs tile, wait 2 s | tree, Development tab |
| 3 | 07:41:15 | click (245,522), Quick Construction node, wait 2 s | node panel, count 4/30 |
| 4 | 07:41:20 | click (495,756), coin Donate, wait 1 s | reward animation over the count |
| 5 | 07:41:33 | wait 2 s | count 3/30 |
| 6 | 07:41:39 | click (495,756), coin Donate, wait 2 s | count 2/30 |
| 7 | none | final report | node panel open |

## Count chain

| Frame | Count | Coin Donate | Note |
|---|---|---|---|
| step-0003 | 4/30 | 1000, green | entry |
| after tap 1 | hidden, then 3/30 | 1000 | animation, 2 s wait |
| after tap 2 | 2/30 | 1000, green | no cooldown timer |

## Panel rows

- Quick Construction 9/10, Increased Building Speed for Allies, Donation Reward +20%.
- Tech EXP Required 4.2M/8.0M, Current +22.5%, Next Level +25%.
- Donation Reward 50 EXP and 50 badge. Diamond Donate 2, never tapped.
- Alliance badge item on the top bar 80.7K at entry, 81.0K at the close, observed only.

## Counters

- Steps 7, actions done 11, refused 0, cost 0.092926 USD, model time 36.1 s.
- Count before 4, after 2, donations 2, coin spent 2000.
