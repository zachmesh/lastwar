---
title: Troop Training Execution 2026-10-28 0634 Queue Run
created: 2026-10-28T13:38:00Z
modified: 2026-10-28T13:38:00Z
level: L0
version: 1.0.0
description: One execution record for the 2026-10-28 0634 queue run, unit training-2026-10-28-0603, Drill Ground Full verified again on a barracks tent tap
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-28
  - source: owner queue design of 2026-10-28, unit training-2026-10-28-0603
---

# Troop training — execution, 2026-10-28 0634 queue run

A single execution, recorded as its own file. Status —
not performed, blocked by the game (Drill Ground Full).
Metadata for this type lives in
[`_activities_/troop-training/`](../../../_activities_/troop-training/INDEX.md).

## 2026-10-28 — Drill Ground Full verified again

- Queue unit training-2026-10-28-0603, executor ticker-0634,
  session cc-62. Opening HUD food 138.6M, iron 331.4M,
  coin 41.4M, titanium 11.72K, total power 149,351,992.
- The barracks tents were located north-east of the drill
  ground (the beige tents with blue roofs). Tapping one
  tent returned the toast Drill Ground Full, unable to
  add units (OCR read 464 units) - the same game-state
  block as the 0203 run. No Train button was pressed, no
  food or iron was spent, Finish Now was never touched.
- The drill ground troop mass still shows its long timer
  (7d 19:47 at sight), so no requeue is possible at any
  barracks while capacity stays full.
- Completed in the queue as failed (execution impossible
  on a game-state block) and marked skip in the tracker
  with the block as the reason. Nothing bought, no
  diamond spent, no speedup burned.
