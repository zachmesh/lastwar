---
title: Decoration Gallery Overview
created: 2026-11-09T20:32:17Z
modified: 2026-11-09T20:32:17Z
level: L1
version: 1.0.0
description: Decoration Gallery Overview on the base screen - collection progress and combat bonuses read-only, entry point unreliable, tabs beyond Overview unmeasured
status: unverified
grounded_in:
  - source: ticker-1134 scout discovery unit 017 execution record 2026-11-09 1158 queue run (partial, Decoration Gallery entry not re-located - the 44,284 point opened the MEGA EXPRESS CONTRACT 99.99 dollar offer popup instead, Overview values already measured by unit 002, tabs beyond Overview unmeasured; record commit d2df49670 on records/2026-11-09)
  - source: ticker-0736 scout discovery unit 002 execution record 2026-11-09 0744 queue run (done, Decoration Gallery sighted - Overview read in full, Collection Progress UR 18/39, SSR 7/19, SR 4/4, Total Decor Combat Power 6,160,413, seven bonuses; record commit 36992d92e on records/2026-11-09)
---

# Decoration Gallery Overview

## What this activity is

The Decoration Gallery's Overview tab, an info-only surface reached
from the base screen. It shows the account's decoration collection
progress by rarity and the total combat power and bonuses the
collection confers. It pays nothing, scores nothing and takes no
recurring action - a read-only reference for what the collection is
worth. Executions are recorded in
`_records_/<date>/decoration-gallery-overview-ur/`, one file per
execution. No GitHub Issue tracks this surface; the Overview is
already measured and the entry problem is a method note, not a
knowledge gap.

## How it is done

- Enter from the base screen left-edge icons. The entry point is
  unreliable - the point that opened the gallery once now opens a
  paid offer, so re-ground the entry fresh from a current base
  screenshot instead of re-tapping a stored point (R2).
- Read the Overview tab in full: Collection Progress per rarity, Total
  Decor Combat Power, and the seven bonuses. Close with the blue back
  arrow. Nothing inside the gallery is tapped, claimed or bought.

## What is known from 2026-11-09 0744 and 1158

- Entry: base screen left-edge icon. The [44,284] point opened the
  gallery once (0744, a mis-tap while grounding the research flask
  icon) and opened the MEGA EXPRESS CONTRACT offer popup instead on
  the 1158 retry. The left-edge icons shift with the base view, so a
  stored point goes stale; the next unit must re-ground fresh (R2).
- Overview, read in full 2026-11-09 07:44 PT and re-confirmed matching
  the day observation file by the 1158 unit: Collection Progress UR
  18/39, SSR 7/19, SR 4/4. Total Decor Combat Power 6,160,413.
  Bonuses - Hero Attack +5494, Hero Defense +810, Hero HP +172515,
  March Size +2, Damage to Monsters +1.62%, Construction Speed
  +15.00%, Secret Mobile Squad Dispatch +3.
- The gallery was closed with the blue back arrow at [156,952] (0744).
  Nothing was tapped inside it; closed untouched.
- Tabs beyond Overview: unmeasured. The gallery itself was not opened
  in the 1158 unit, so its tabs beyond Overview and any per-rarity
  detail stay unmeasured.
- Incidental, 2026-11-09 11:58 PT: the MEGA EXPRESS CONTRACT offer
  popup - a golden train, "Availability today: 0/2", Rewards (red gem
  10.0K, a ticket x1, blue gem 1.0K, 5m speedup x600, a gear-crate
  item), "Use to instantly call a highly rewarding Alliance Trade
  Train!", priced $99.99 for 1000 purple gems, with a Refund Policy
  link. Closed with its X, untouched - no purchase, nothing claimed.
  The $99.99 button was never tapped. It is recorded here as an
  observed paid offer, not a task; no owning regular or issue exists
  for it.
- Cost: free to read. No diamonds, no money, no priced button tapped
  on this path.
- Scoring: none - an info surface, not a scoring event.
- Base screen on return: coin 46.2M, power 149,217,331 - unchanged.

## Open questions

- The gallery entry, re-grounded fresh from a current base screenshot
  (R2) - the [44,284] point is retired.
- The tabs beyond Overview and any per-rarity detail: unmeasured
  until a successor unit re-grounds the entry and reads them.

## What the 2026-11-09 1158 scout-discovery unit added - Decoration Gallery entry unreliable, Overview already measured

- Unit scout-scout-discovery-2026-11-09-017 by ticker-1134, about
  11:58 local, status partial. Evidence in
  `_records_/2026-11-09/decoration-gallery-overview-ur/1158-queue-run.md`
  (commit d2df49670 on records/2026-11-09). One entry attempt: the tap
  at normalized [44,284] opened the MEGA EXPRESS CONTRACT $99.99
  offer popup instead of the gallery; the popup was closed with its X,
  untouched, and the game returned to the base screen. Nothing
  claimed, nothing spent.
- The 0744 sighting (unit 002, ticker-0736, record
  `_records_/2026-11-09/building-queue-1-of/0744-queue-run.md`, commit
  36992d92e on records/2026-11-09) was sourced in perception-scout
  but never got its own profile until this fold; its full Overview
  read is folded here alongside the 1158 entry failure.
- The provisional profile was NOT written into `_activities_/` by
  either unit (tier 2, left for the knowledge PR flow); this profile
  is that write, by the knowledge organizer.
- Result stats: target learn-decoration-gallery-profile-fields,
  achieved 0, resources_gained none, costs about 3 minutes, no items
  spent, verified yes, blocker_category c, points 0, surfaces_walked
  base-screen, mega-express-contract-popup, items_observed 0,
  red_dots_seen 0, red_dots_explained 0, unexplained_red_dots 0,
  unknown_items 1.
