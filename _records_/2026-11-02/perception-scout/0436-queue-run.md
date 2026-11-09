---
title: Queue Run 0440 Scout Midday Base Group
created: 2026-11-02T12:36:00Z
modified: 2026-11-02T12:36:00Z
level: L0
version: 1.0.0
description: Scout unit partial, base group only, observe-only
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-02
---

# 0440 queue run - perception scout, base group (partial)

Unit scout-midday-2026-11-01-0700, executor ticker-0434, session
cc-152 on the Mac mini, LastWar window 137757, about 04:35 to 04:36 America/Los_Angeles. Status partial: only the base group
was walked; events, store and alliance groups are unwalked.
Observe-only; nothing claimed, fought, dispatched, donated,
dug or bought. No different-device dialog, no login demand.

## Slot note - late execution, filed under the current reset day

This unit was staged for the 2026-11-01 07:00 midday pass, in
the reset day that ended 2026-11-01 19:00. It executed late, in
the current reset day (started 2026-11-01 19:00), so its
observation is filed in the 2026-11-02 observation file as a
read of the current game state, not as a read of the old
midday window. No successor scout unit is enqueued from this
unit: the post-reset scout head for the current reset day,
scout-2026-11-01-1900, is already in inbox and will walk the
remaining groups; enqueuing another scout head would duplicate
it under the (regular, planned_for) invariant.

## What was walked

- Entry: the game was left on the Secret Command Post Hidden
  Treasure map tab, read live on entry and matching the
  0424 treasures record exactly: treasure progress 2/15,
  M1 x13, M2 x14, M3 x0, M4 x9, M5 x3, M6 x6, M7 x13.
  Nothing dug.
- Back navigation: the verified back-arrow tap at norm
  [163,947] returned to the base screen at once, confirming
  the 1437 grounding again.
- Base screen and HUD, read live about 04:36 local:
  account power 149,296,925 (up from 148,957,193 at the
  2026-11-01 14:47 read). Top row 379.7M, 571.7M, 45.7M;
  second row power 149,296,925 and 11.72K with a plus
  button; cart 2,526 (was 2,366). Left column: hammer
  2/4, bottle 2/2, truck, radio badge 3, survivor portrait.
  Right column: Events badge 1 (was x2), Capitol, VS
  timer 13:23:53, Season II badge 1, Alliance, Mail,
  Inventory. Bottom: HEROES, chat ticker, 99+ badge,
  WORLD.
- Resource bubbles: many bubbles visible across the left
  and centre buildings (gold, food and iron bubbles on
  several buildings) - observed only, not collected; the
  harvest regular owns collection and its 0603 unit is
  already queued.
- Furnace toast again, unchanged: "Furnace total overdrive
  time (in sec) [22/60]". Still unexplained; furnace is a
  red-line surface, observed only.
- Chat ticker top line: a treasure-map congratulation
  line about digging up Golden Mobile Squad units; not
  attributed to this account in this read, recorded as
  seen only.
- Duel posture from tools/duel.py at unit start: duel
  day 1, Radar Training, radar release day, day ends
  19:00 local. Radar claims score today; the scout
  claimed nothing.

## Red dot accounting for this unit

- Seen 5 badge signals: radio 3, Events 1, Season II 1,
  99+ badge, plus the Inventory panel (no dot verified in
  this capture - recorded as not seen, not as cleared).
- Explained 2: radio 3 maps to the help regular, Events 1
  to the events regular; units for both are queued.
- Unexplained 3: Season II badge 1, 99+ badge, and the
  Alliance dot state (alliance group not walked).
- Unknown items carried: furnace overdrive toast, 780 km
  home icon meaning (not re-verified this unit).
- unmatched_labels: none in the surfaces actually walked.

## Unwalked, carried to the post-reset scout head

- scout-events group in full: Events hub tabs, duel page,
  Arms Race phase and score, radar.
- scout-store group in full: Store sections, markets, VIP,
  passes, daily missions, Inventory dot resolution.
- scout-alliance group in full: alliance panel and
  station, Alliance dot resolution, 99+ badge resolution.
- scout-base remainder: building badges building by
  building, Armed Truck state verification, gate and wall
  signals, per-building bubble inventory.

## Follow-up

Carried to scout-2026-11-01-1900 (already in inbox). This
unit closes partial under the zero-unexplained-red-dots
closing condition. Tracker untouched (scout regulars are
observation-only; no tracker mark for a partial).
