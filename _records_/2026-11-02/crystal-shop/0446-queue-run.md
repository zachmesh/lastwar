---
title: Queue Run 0446 Crystal Shop
created: 2026-11-02T12:46:00Z
modified: 2026-11-02T12:46:00Z
level: L0
version: 1.0.0
description: Crystal shop unit partial - Building section not found in Mall tabs, tab not located
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-02
---

# 0446 queue run - crystal shop (partial)

Unit crystal-shop-2026-11-01-0500, executor ticker-0434,
session cc-153 on the Mac mini, LastWar window 137757,
about 04:45 to 04:46 America/Los_Angeles. Status partial:
the Crystal Shop tab was not located, nothing claimed.
Owner-named 2026-10-25, age 8 days, rule R5: this item
stays named in the round summary until it closes. No
different-device dialog, no login demand, nothing spent,
no diamond or money button tapped.

## Navigation notes (for the next hunt)

- Mission back arrow centre re-grounded at norm
  [62,941] for the Mission screen: taps at [101,941]
  and [163,947] both missed on that screen (the
  first lands near the arrow right edge, the second
  in the dark margin right of it). Back arrows differ
  per screen; do not inherit one screen grounding.
- Shop opened from the base cart icon at norm
  [940,85], confirming the 2017 grounding.
- The Mall tab strip scrolls horizontally with a drag
  (used [800,125] to [300,125], twice): the strip end
  was reached on the second drag, which changed
  nothing.

## What was walked - Mall tabs, enumerated live

- Tab strip, in order, read live across two strip
  positions: Official Event, Weekly Deal, Super
  Monthly Pass, Weekly Pass, Diamond, Gold Brick
  Mall, Hot Sale Packs. No Building tab exists in
  this strip, and no Crystal Shop tab was seen.
- Diamond tab opened and read: diamond purchase
  packs only (10000 for $99.99, 5000 for $49.99,
  2000 for $19.99, 1000 for $9.99, 500 and 100
  below the fold), Initial Buy Reward double
  diamonds banner. No Building sub-section inside
  it, and no pack was tapped.
- The top MALL header tap at norm [670,63] changed
  nothing; it is a screen title, not a section
  switch.
- Not walked in this unit (time, and purchase
  surfaces): Gold Brick Mall and Hot Sale Packs
  tab contents, and any non-Mall store surface.
  The 2026-10-21 patch-notes lead says "Store,
  Building section" - that section was not found
  under any Mall tab walked, so either the section
  lives outside the Mall tab strip or the lead's
  section naming does not match the current UI.
  That mismatch is the finding, stated here rather
  than resolved by guesswork.

## Outcome

- Status: partial, unverified under queue rule R1
  for the locate objective (target 1, achieved 0).
  Claimed: nothing. Tracker untouched.
- No activity-metadata backfill was made: the
  mechanism is still unknown, and backfilling a
  guess would violate the evidence rule. The
  negative finding above is the record for the
  next hunt.
- Follow-up: Issue #128 commented from this unit
  (its crystal-shop half was claimed and run, but
  not located); the item remains open under R5.
  Game left on the Shop Diamond tab.
- Red lines: nothing spent, no diamonds, no paid
  button, no Buy in any shop.

## Delivery note - stale local pool copy, queue state kept

- At the records-branch head this pass delivered to, this
  unit id was already in `_queue_/done` from ticker-1234
  on 2026-11-01 (evidence
  `_records_/2026-11-01/crystal-shop/1241-queue-run.md`,
  follow-up: Diamond tab inner categories first, then
  MALL header below banner, then base building route).
  This pass claimed a stale copy still sitting in the
  local working tree inbox and re-ran the hunt.
- Delivery therefore keeps ticker-1234 done file
  untouched (records are append-only; overwriting it
  would destroy the original result). This 0446 record
  stands as a re-execution observation, not as the
  unit first completion. Its Diamond-tab and MALL-header
  checks follow ticker-1234 follow-up in part: the
  Diamond tab holds purchase packs only with no inner
  categories found, and the MALL header tap changed
  nothing.
