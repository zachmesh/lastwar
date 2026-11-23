---
title: Perception scout queue run 2305 detail
created: 2026-11-23T07:10:00Z
modified: 2026-11-23T07:10:00Z
version: 1.0.0
description: Sidecar with the taps, panel rows and timings of the Quick Dispatch probe runs of unit scout-midday-2026-11-23-0656
status: run-done
grounded_in:
  - source: events.jsonl of runs 20261123T070509Z-97f307 and 20261123T070656Z-449145, action and observation timestamps, 2026-11-23T07:05Z to 07:08Z
---

# Detail for scout run 2305

Companion to [2305-queue-run.md](2305-queue-run.md). Pixel points are in the 1920x1080
screen frame, game window at about x 73-715.

## Part A taps, run 20261123T070509Z-97f307

| Step | Time Z | Action | Effect |
|---|---|---|---|
| 1 | 07:05:17 | click (184,372), ground below a bubble | bubbles hidden for a moment, nothing selected |
| 2 | 07:05:28 | wait 2 s | nothing selected |
| 3 | 07:05:35 | click (216,404), iron mine derrick body | tag "Iron Mine Lv.27", round buttons: group icon and green up arrow |
| 4 | 07:05:45 | click (184,459), the group icon | Building Details panel |
| 5 | 07:05:53.7 | click (393,823), Quick Dispatch, the only press | frame at 07:05:56.9: no toast, no dialog, list unchanged, a game-wide announcement banner at the top |
| 6 | 07:06:03 | click (607,252), panel X | base, no troop leaving |
| 7 | none | final report | base |

## Part A panel rows

- IRON MINE Lv.27, Output/hr +136688, Max Production Time 11hr 36min, heading Survivors.
- Four cards, posts Miner, Miner, Miner, Miner, stars about one to three each, per-card (i) corner.
- Button "Quick Dispatch", blue, no help text.

## Part B taps, run 20261123T070656Z-449145

| Step | Time Z | Action | Effect |
|---|---|---|---|
| 1 | 07:07:02 | click (532,632), sand tent roof | tag "Barracks Lv.30" |
| 2 | 07:07:09 | click (456,652), blue group icon | Building Details panel |
| 3 | 07:07:16 | wait 1 s | panel read |
| 4 | 07:07:20 | click (607,252), panel X | base |
| 5 | 07:07:31 | wait 1 s | base confirmed |

## Part B panel rows

- BARRACKS Lv.30, Training Count +793, heading Survivors, four cards all post Instructor.
- Button "Quick Dispatch", no help, question-mark or (i) text beside it or the count.
- The first Part B frame showed the red target icon without a countdown.

## Counters

- Steps 7 and 6, actions done 6 and 5, refused 0 and 0, cost 0.101255 and 0.079079 USD,
  model time 46.4 s and 29.6 s.
