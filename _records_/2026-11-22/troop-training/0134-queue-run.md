---
title: Troop training queue run 0134
created: 2026-11-22T09:58:00Z
modified: 2026-11-22T09:58:00Z
version: 1.0.0
description: Ticker 0134 training unit - Lv.27 barracks requeued, Drill Ground Full blocker did not reproduce
status: partial
---

# 0134 queue run - troop training (partial)

- Session: 01:34-01:42 PT (09:34-09:42 UTC), executor ticker-0134, computer session cc-78, unit training-2026-11-21-2203.
- Game state on entry: the game was left on the Alliance Tech screen (Quick Construction 9/10, 3.6M/8.0M EXP, Tech Donation Today 4450) by the ticker-0113 donations pass; closed both panels back to the base screen.
- Total power 149,417,850. Resources on entry: food 764.9M, iron 1.1G, coins 103.9M, diamonds 345.8K. Build slot busy: Oil Well (0/1).

## Done - Lv.27 barracks requeued

- Tapped the Lv.27 barracks tent; TRAIN UNITS panel showed T9 preselected, count 726, cost 4.1M food and 4.1M iron, time 1d 10:19:35.
- Tapped Train. Food fell 764.9M to 760.8M (minus 4.1M, the exact batch cost); iron stayed at the rounded 1.1G display. No toast, no Drill Ground Full error.
- Re-opened the same panel minutes later: Lv.9, 726 units, "Training in progress 1d 10:17:42". The batch is running.
- Headline: the standing Drill Ground Full blocker (Issue #678, four consecutive partials 2026-11-10 to 2026-11-11, Lv.27 idle since 2026-11-10 21:46) did NOT reproduce. The requeue worked on the first try. The Drill Ground count must have freed up since 2026-11-11 (cause unknown - no Drill Ground screen was located this pass either).

## Not verified - the other three barracks

- Lv.30 barracks: selected (label "Barracks Lv.30"); a button-row tap landed on Building Details instead of TRAIN UNITS. Details read: Training Count +793, instructors Marcus, Taylor, Daniel, Michael; Quick Dispatch not used. Training state (running or idle) NOT verified.
- Lv.24 barracks and the fourth barracks (T8 / T7 per 2026-10-25 notes): tent taps selected the tent and showed a small round indicator below it, but the TRAIN UNITS panel did not open with the taps tried. Training state NOT verified.
- Button-row lesson: tapping a tent selects it and shows the paw / pistol / green-arrow row below it; the buttons are small and the tap point must be precise - one tap opened Building Details when TRAIN UNITS was intended, and one stray tap opened the world map instead. Do not tap the green up arrow (upgrade shortcut).
- Incidental world-map sighting (for the radar unit, not acted on here): radar 14/40 tasks, 8 task rewards claimable, "12 Radar Task(s) will be restored in 05:00:33", stamina 120.

## Outcome

- Status partial: 1 of 4 barracks verified and requeued; 3 barracks unverified. Tracker untouched; the next tick re-produces the training regular.
- Follow-up: comment Issue #678 with this pass's non-reproduction (blocker not seen, Lv.27 requeued cleanly); the activity metadata's standing-blocker section still needs a fresh-entry update, left for the knowledge flow (tier-2 change, not swept into this record commit).
- No diamonds spent, no speedup used, no Finish Now, no other purchase or consequential action.

## Post-close note (same pass)

- The `complete` call closed without the five always-required result stats keys (target, achieved, resources_gained, costs, verified) and without blocker_category, so the unit file records `stats_missing` and the closing counts as unverified in the retro aggregation. The values that would have applied: target 4 barracks checked/requeued, achieved 1, resources_gained 0, costs 4.1M food + 4.1M iron, verified true for the Lv.27 requeue (live-read), blocker_category for the three unverified barracks: panel not reached (tap precision / UI). The tool refuses a second `complete` on a done unit, so the stats stand as recorded; the gap is noted here, not backfilled.
