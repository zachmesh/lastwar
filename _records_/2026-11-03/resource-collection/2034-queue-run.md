---
title: Harvest queue run ticker-2034
created: 2026-11-04T04:50:00Z
modified: 2026-11-04T05:10:00Z
status: partial
---

# Harvest unit harvest-2026-11-03-1803, partial, ticker-2034

Session window: unit claimed 2026-11-03 20:36 local; game play about
20:50 to 21:05 local. The pass opened with own-PR work first (see the
pass note): PR 207's long-standing conflict was resolved branch-side
on the VPS and pushed before game work began, which left this unit
against its 15-minute cap.

## What was done

- Game already running on the Mac mini (LastWar, com.lastwar.ios).
  Entry found the Alliance Techs panel open, left over from the
  2004 donations unit: inner detail closed at (855,195), the Techs
  list closed at (854,146), the Alliance screen closed with its back
  arrow at (140,915). No donation was made here; the donations
  counter (Donation Count 2/30 at entry) belongs to the donations
  unit, not this one.
- Base view at entry, HUD read live from screenshots: food 275.0M,
  iron 612.5M, coin 34.2M, second-row resource 19.0M, 505.1K, total
  power 149,948,901.
- One verified collection: the first-view teal bubble tap at
  (397,413) moved the second-row resource from 19.0M to 20.6M
  (+1.6M, HUD read live on the next screenshot). No resource name
  is claimed for that row; the record states only the row and the
  delta.
- Two taps collected nothing and are recorded as a method lesson:
  grounding points (435,442) and (501,532) for "small circular
  resource bubble above a building" selected Titanium Alloy
  Factory No.1 and No.3 (both Lv.30) instead. The factory-top
  markers look like bubbles to the grounding pass. Both selections
  were cleared by tapping empty ground (200,780); no panel was
  opened, nothing was built or spent.
- The white bubble above the central house cluster was tapped at
  (485,575): it produced only the toast "Game season event not
  yet started or has ended" and stayed on screen. It is a season
  entry icon, not a collectible bubble.

## What was not done (partial, tracker untouched)

- The full edge-drag sweep of the Nov 1 rule was not completed:
  the left-side coin and stone buildings, the drone-component
  bubbles, and the armed-truck loot check were not reached inside
  the unit cap. The next harvest unit resumes from the sweep, with
  the factory-icon confusion (Issue #250) as its first caution.
- No truck top bubble was claimed; the "ready to depart again"
  tooltip seen near the top of the base view was not probed, as
  truck work belongs to the trucks unit under one-unit-one-type.
- No diamonds, money, speedup, or paid button was touched. No
  Delete All, no assembly, no teleport.

## Evidence and follow-up

- Evidence: this file; screenshots in the pass working files
  (base views before and after the verified collection).
- Follow-up: Issue #250 (tooling) filed for the bubble-grounding
  confusion; the next harvest unit should verify every tap against
  HUD movement and treat grounding hits over factory rows as
  suspect.
- Result stats: target full base sweep, achieved 1 verified
  bubble (+1.6M second-row resource), verified yes for the
  +1.6M delta, blocker_category b (crowding out: own-PR
  resolution consumed the pass window before game work).
