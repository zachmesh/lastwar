---
title: Resource Collection Execution 2026-10-30 0226 Queue Run
created: 2026-10-30T09:26:00Z
modified: 2026-10-30T09:26:00Z
level: L0
version: 0.1.0
description: Harvest queue unit harvest-2026-10-30-0203 - iron and coin bubbles collected, food total unchanged on HUD rounding, batch tapping opened an Iron Mine panel which was closed without dispatch, remaining bubbles and the Armed Truck unchecked at the pass budget
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-30
  - source: owner directions of 2026-10-25, 2026-10-26 and 2026-10-28 - the standing routine, Mac control authorization and the task unit queue ticker
---

# Resource collection — execution, 2026-10-30 0226 queue unit

A single task unit, executed by executor ticker-0204 under the
task unit queue. Unit harvest-2026-10-30-0203, priority 3.
Session window 02:20 to about 02:26 America/Los_Angeles.
Status — performed in part: iron and coin bubbles were
collected and verified by HUD totals, but not every
bubble on the base was collected and the Armed Truck
was not checked, so the tracker is untouched and the
next tick re-produces this regular.

## What was observed

- Base totals at entry (after the radar unit) — food
  269.3M, iron 454.5M, coin 126.5M, stamina 52.
- First tap — a visually grounded bubble at centre
  168,309 collected iron: iron rose 454.5M to
  461.4M (plus 6.9M), food and coin unchanged on
  the HUD. The grounded label "food bubble" for
  that point was therefore wrong; the bubble was
  iron, so bubble types are not trusted from
  grounding labels alone.
- Batch taps — seven further bubble centres from a
  fresh visual grounding were tapped in one batch.
  Coin rose 126.5M to 131.7M (plus 5.2M), iron
  stayed 461.4M and food stayed 269.3M on HUD
  rounding. The batch's last tap fell through to
  a building after its bubble was already gone and
  opened an Iron Mine Lv.27 Building Details panel
  (Output per hour plus 129,258, Max Production
  Time 11hr 36min, Survivors Taylor, Harry,
  Samantha and Javier, all Miner). The panel was
  closed with its X without tapping Quick Dispatch
  — survivor dispatch belongs to the survivors
  regular, not this unit — and no survivor was
  dispatched.
- End state — food 269.3M, iron 461.4M, coin
  131.7M. Whether every bubble on the base is now
  collected was not verified in this unit: the
  pass budget (about 25 minutes from the 02:04
  token) ended the unit at 02:26, before a final
  bubble scan and before the Armed Truck check.
  Both fall to the next tick's fresh harvest unit.
- Nothing else spent — no diamonds, no money, no
  speedup items, no building or research started.
  No other regular was merged into this unit.
