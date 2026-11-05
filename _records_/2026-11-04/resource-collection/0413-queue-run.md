---
title: Harvest queue run ticker-0404
created: 2026-11-04T12:13:00Z
modified: 2026-11-04T12:13:00Z
status: partial
---

# Harvest unit harvest-2026-11-04-0203, partial, ticker-0404

Session window: unit claimed 2026-11-04 04:05 local; game work
about 04:06 to 04:13 local, Mac mini sessions cc-411 and cc-412.
Base view reached via the world-map back arrow after two home-icon
taps did not switch views. The full edge-drag sweep of the Nov 1
rule was not completed.

## Own-PR check first

- Open records PR for today, PR 264 (records/2026-11-04, opened
  by the ticker-0304 pass): body names Owner:
  lastwar-pr-integrator, zero comments. Nothing addressed to
  this job, nothing to fix, no reply owed. PR 265 (records
  2026-11-02) carries an integrator conflict note, but it is
  not this job's PR and the integrator owns its resolution.

## Zombie seeding

- Not seeded. No zombie-invasion unit sits in inbox or claimed,
  and the chain closed on 2026-10-30 (unit 066: Events hub with
  no Zombie Invasion tab). The activity metadata bars a fresh
  chain until the tab is seen live again; this pass never
  reached a live Events hub, so no seed was made.

## What was done

- HUD at base entry (live screenshot reads): food 395.0M, iron
  732.0M, coin 3.1M, second row 21.0M and 922.2K, total power
  150,028,269, diamonds 12.72K.
- One verified collection: a farmland bubble tap at (395,415)
  moved food 395.0M to 397.0M (+2.0M, HUD read live on the
  next screenshot), consistent with the standing rule that one
  farmland tap collects all farmland bubbles at once.
- Base view panned with a drag (300,500) to (600,500), which
  brought the left-side iron-mine and factory row fully into
  view.

## What collected nothing (method lesson, Issue #250)

- Tap at (148,405) on a left-side marker: no HUD movement.
- Tap at (833,391) selected Headquarters Lv.30 (panel closed
  by an empty-ground tap, nothing spent).
- Grounded tap at (369,273) opened the Gear Factory panel
  (closed with its back arrow; Craft at 495.0K coin was NOT
  tapped).
- Tap at (389,363) selected Component Factory Lv.20.
- Tap at (467,405) selected Iron Mine Lv.27.
- Tap at (86,315) on the small icon floating above the
  leftmost blue building: no HUD movement, no panel.
- Pattern: the gold circles and small icons above the
  iron-mine and factory row are building markers, not
  collectible bubbles, at this screenshot resolution; only
  the farmland bubble verified. The floating-icon tap is
  the closest miss and is the next unit's first retry
  candidate, but it did not verify this unit.

## What was not done (partial, tracker untouched)

- The full edge-drag sweep of the Nov 1 rule was not
  completed: the left-side coin and stone building bubbles,
  the drone-component bubbles, the EXP and screw bubbles,
  and the armed-truck loot check were not reached or not
  verified inside the unit cap. The next harvest unit
  resumes from the sweep, with the marker-confusion
  caution above as its first note.
- No truck top bubble was claimed; truck work belongs to
  the trucks unit under one-unit-one-type.
- No diamonds, money, speedup, or paid button was touched.
  No Delete All, no assembly, no teleport. No Craft, no
  building, no research was started.

## Evidence and follow-up

- Evidence: this file; screenshots in the pass working files
  (base views before and after the verified collection).
- Follow-up: Issue #250 (tooling, bubble-grounding
  confusion) already covers this failure mode; this unit's
  evidence is noted here and will be commented on #250
  rather than filed as a duplicate.
- Result stats: target full base sweep, achieved 1 verified
  bubble (food +2.0M), resources_gained food +2.0M,
  verified yes for the +2.0M delta, blocker_category c
  (tap method: remaining bubbles not distinguished from
  building markers at this resolution).
