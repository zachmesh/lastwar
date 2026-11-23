---
title: Queue Planning Exact Funding Plan In The Builder Units 2570 2026-11-23
created: 2026-11-23T03:38:00-08:00
modified: 2026-11-23T03:38:00-08:00
level: L0
version: 1.0.0
description: Planner pass after the RC1 chest limits - the exact funding plan for the three Drill Ground starts written into three builder units and two sheets, with the diamond-tile hazard, bounded speed-up use, and a split of the work into runs
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0338-exact-funding-plan
trigger: coordinator message with the RC1 facts and the plan
started_at: 2026-11-23T03:26:00-08:00
finished_at: 2026-11-23T03:38:00-08:00
verified: RC1 record read in full; chest and coin arithmetic recomputed; unit and sheet word counts under 450 or 400; validate exit 0
grounded_in:
  - source: _records_/2026-11-22/growth/1115-rc1-chest-limits.md
  - source: _records_/2026-11-22/queue-planning/2540-drill-ground-sheet.md and 2541-conversion-and-speedup-sheet.md
---

# Exact funding plan, 2570

## 1. Plan as written

(a) One Use of 59 UR Coin Chests, 59 x 2.4364M = 143.75M, for the Lv.26 and Lv.27 steps (142.8M). (b) One Use of about 19,834 plain Resource Chests, choosing only the 6K Coin option, 119.0M, for the Lv.28 step; 19,700 to 20,000 is accepted because the slider moves about 80 chests per pixel, and the default 20,862 is 125.2M, acceptable only if said. (c) Coin lands at about 15M after all three starts, above the 10M floor; fixed chests left are UR 28, SSR 71 and SR 122, about 138M, which funds the Builders Hut if ranked. Recomputed: the coin path is 14.4M, then +143.75M, then -142.8M, then +119.0M, then -119.0M, leaving 15.35M.

## 2. Hazards written in

The Resources tab opens with the 5,000 Diamonds x16 tile selected and a live Use, and the plain chest defaults to its full stock. Every unit says: tap the intended tile first, confirm its name in a frame, never Use with any other tile selected, read the number field in a frame before Use, stop on a choice popup that shows anything but the coin option or a cost.

## 3. Runs

Each conversion is its own run, so the work is three units. `-001`: run 1 conversion (a), run 2 starts the Lv.26 and Lv.27 grounds. `-002`: run 1 conversion (b), run 2 starts the Lv.28 ground and the fourth builder. `-003` (new, 386 words, window 09:22Z to 10:50Z, expiry order after the others): reads the Duel screen, then applies the speed-ups. Speed-ups use construction items first and the large ones first (8h x10 is 4,800 minutes, 1h x26 is 1,560), stop at 10,000 minutes per upgrade and 30,000 in all, reduce a defaulted quantity before pressing, and write the minutes after every press. The briefs are 398, 439 and 386 words. The sheets are split: 2540 (where, previews, funding, hazards) and 2541 (procedure, speed-up use).

## 4. Watch

The slider precision and the choice popup are untested. The Duel screen decides the Tuesday window. The fixed 11-24 fills run between the units but only read.
