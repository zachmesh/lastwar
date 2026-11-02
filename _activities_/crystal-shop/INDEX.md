---
title: Crystal Shop
created: 2026-11-01T05:00:00Z
modified: 2026-11-02T03:47:03Z
level: L1
version: 1.1.0
description: The Crystal Shop tab in the Store Building section - locating it, its collection mechanism and the daily crystal collection
status: unlocated
grounded_in:
  - source: owner named the crystal task on 2026-10-25
  - source: system patch-notes mail of 2026-10-21, recorded in the mail-rewards metadata
  - source: miss audit of 2026-10-31, item 8
  - source: crystal-shop execution record 2026-11-01 1241 queue run (first executed unit, tab row read live)
---


# Crystal shop

## What this activity is

The Crystal Shop - a tab announced for the Store, Building
section - and whatever crystal collection or task it holds. This
folder accumulates crystal knowledge. Executions are recorded in
`_records_/<date>/crystal-shop/`, one file per execution.

The owner named the crystal task on 2026-10-25. It was hunted
once that night and then dropped - the miss audit of 2026-10-31
counts it as the case of an owner-named task with no escalation
path, open six days with zero units. This folder is its modelling,
created 2026-11-01 under the fix. Until it closes, rule R5 of the
task unit queue design applies - it is named in every round
summary, with its age counted from 2026-10-25.

## What is known

- A system patch-notes mail dated 2026-10-21 announced a Crystal
  Shop tab added to the Store, Building section. That lead is
  recorded in `_activities_/mail-rewards/INDEX.md`. The shop units of 2026-10-30 and 2026-10-31 worked the Hot
  Deals storefront and the pass pages only, and the word
  building appears in neither day shop records. The 1241 unit
  (below) entered the shop from the base cart icon and read
  the full tab row live, but the Building section itself was
  still not entered, because no Building tab exists in that
  row - so the patch-note lead is not yet tested, only the
  cart-shop row is ruled out.
- The 2026-10-25 hunt ruled out Daily Tasks, Season tasks, the
  Hot Deals storefront and the Alliance Store as the crystal
  task location, and left the task identity itself unconfirmed.
- Mail reward popups have shown a crystal item among their
  contents - 1.6K in the 2026-10-31 mail 1947 batch, 2.8K in a
  2026-10-29 batch. Those are mail reward contents as displayed.
  They are not a Crystal Shop visit and not crystal task
  progress, and the two are never merged in a report.

## The job, until located

1. Open the Store from the base screen.
2. Enter the Building section of the Store - not the Hot Deals
   storefront.
3. Open the Crystal Shop tab and read it live - what it holds,
   its currency, any free or daily claim, any exchange list, and
   any task or progress state.
4. Claim everything claimable under the standing red lines - no
   spending of diamonds, rubies or money without owner approval.
5. Backfill the mechanism into this file in the same pass - what
   the tab is, how crystal is collected, and its cadence. From
   then on this activity is a daily collection line on the
   daily collection ledger, closed each day on a live read.

## Cadence

- Until located - attempted or reported by name every day, age
  counted from 2026-10-25.
- Once located - daily, per the mechanism the locating unit
  records here.

## What the 2026-11-01 1241 unit added

- Unit crystal-shop-2026-11-01-0500 by ticker-1234, session
  about 12:41 to 12:58, status partial. This is the first
  executed crystal-shop unit in the done pool (the 0404
  attempt the same day failed on the offline device channel
  with zero game observation and carries no profile
  knowledge). No spending, no claims, no purchases.
- Shop opened from the base cart icon onto the HOT DEALS
  tab row, as the shop-claims metadata describes. The tab
  row was scrolled fully, left to right, and read live in
  order: Official Event, Weekly Deal, Super Monthly Pass,
  Weekly Pass, Diamond, Gold Brick Mall, Hot Sale Packs.
  A second scroll attempt produced no further movement, so
  Hot Sale Packs is the last tab. No Building tab and no
  Crystal Shop tab appears in this row.
- MALL section header tap: the screen stayed on the HOT
  DEALS tab row, so the header tap did not switch sections
  in this unit.
- Gold Brick Mall tab: it opened only a four step tutorial
  popup for the Gold Brick Mall, steps 1 to 4, ending with
  "Get the pack rewards directly". It is not a Building
  section and it holds no Crystal Shop tab. Two taps on
  its X, the second at the freshly measured centre, did
  not dismiss it, so under rule R2 that method ended
  inside this unit and the popup was left open. The popup
  is harmless and the shop back arrow remains available
  to the next unit.
- Result: target not achieved - locate the Crystal Shop
  tab in the Store Building section and claim any free
  daily crystal. Cost about 17 minutes, no items spent.
  Blocker category f, missing precondition: the Building
  section the 2026-10-21 patch note names was not found
  in the shop UI reached from the base cart icon.
- Next crystal-shop unit, changed method, in the record's
  order. First, open the Diamond tab and read its inner
  categories, since diamond shop pages commonly carry
  their own category rows. Second, retry the MALL header
  tap below the scrolling announcement banner, which
  overlapped the header in this unit. Third, check whether
  the Building section sits outside the cart shop, for
  example as a building panel on the base screen, and
  record that route as learn-only if it touches a price,
  diamonds or a red line.
- Watermark-gap note: this unit was missed by the 1332
  organizer run's input list and is folded here by the
  1932 run's full ended-trade-day sweep, so the gap is
  closed, not carried. The tab stays unlocated and the
  age still counts from 2026-10-25.


## Open questions

- Everything about the tab itself - it has never been opened.
- Whether the Building section sits outside the cart shop (base-screen building panel) or inside the Diamond tab's inner categories - the two routes the next unit tries, in that order after the Diamond read.
