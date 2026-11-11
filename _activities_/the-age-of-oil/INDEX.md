---
title: The Age of Oil
created: 2026-11-09T20:32:17Z
modified: 2026-11-09T20:32:17Z
level: L1
version: 1.0.0
description: Season II warzone collective-progression event in the Events hub - three warzone-wide counters with per-commander ranking rewards, ends about 2026-11-15 in the late afternoon PT, no recurring agent action
status: unverified
grounded_in:
  - source: ticker-1134 scout discovery unit 014 execution record 2026-11-09 1146 queue run (done, Age of Oil explored read-only - warzone counters tech 2607/500, building 11186/500, heroes 9465/10000, Research Ranking read in full with top-20 reward tiers, Base Expansion II icon corrected to a stage-info button; record commit d2df49670 on records/2026-11-09)
  - source: ticker-0804 scout discovery unit 007 execution record 2026-11-09 0829 queue run (done, Age of Oil first explored read-only - mechanism explained, counters tech 2383/500, building 10721/500, heroes 8833/10000, reward claim state unmeasured; record commit b58fc31b6 on records/2026-11-09)
  - source: ticker-1851 event-claims execution record 2026-11-08 1914 queue run (partial, Age of Oil discovered, milestone 1 claimed, milestone 2 chest unresponsive blocker class c; record commit cff344153 on records/2026-11-08)
  - source: ticker-0204 event-claims execution record 2026-11-09 0224 queue run (partial, Age of Oil milestone 2 chest claimed after the 1914 blocker; record commit facef628c on records/2026-11-09)
  - source: ticker-0434 event-claims execution record 2026-11-09 0450 queue run (partial, Age of Oil milestones verified claimed, both chests gone; record commit b6ed78edd0 on records/2026-11-09)
---

# The Age of Oil

## What this activity is

The Season II warzone collective-progression event, the leftmost tab
of the Events hub. Three warzone-wide counters advance as the whole
warzone plays - Tech Research, Building Upgrades, Hero Recruitments -
toward stage unlocks, with a per-commander ranking per task that pays
reward tiers to the top 20. The account's own research and building
activity feeds the warzone totals, but there is no personal target and
no recurring agent action on this page: the goals advance passively,
and the only thing to watch is the Hero Mobilization count and its
unmeasured chest. This is not a scoring event for the account and not
a routine executable task. Executions are recorded in
`_records_/<date>/the-age-of-oil/`, one file per execution. The
candidate is tracked in GitHub Issue #477.

## How it is done

- Enter from the Events hub, The Age of Oil tab (leftmost tab; the tab
  strip scrolls horizontally, two rightward drags may be needed to
  bring it into view).
- Read the three task cards and their counters, the stage track 1-2-3-4
  across the top (stage 1 highlighted), and the countdown timer.
- The small bars icon at a card's top right opens that task's ranking;
  the ranking popup carries the full reward tiers. Read the tiers
  before closing it.
- The circular icons below the cards are stage-info buttons, not
  rewards: one tap opens a stage popup with a Go button. Do not tap Go
  - it navigates toward the base expansion, an action outside
  read-only learning. Do not tap any chest or priced button without
  the owner's direction.

## What is known from 2026-11-09 0829 and 1146

- Entry: Events hub, The Age of Oil tab (leftmost). Tab order: The Age
  of Oil, Arms Race, Winter Battlefield, Desert Battlefield, Wanted
  Boss, Survey Center, Community. No Zombie Invasion tab - the event
  is still ended.
- Mechanism: warzone-wide collective counters toward stage unlocks -
  500 Tech Research, 500 Building Upgrades, 10000 Hero Recruitments -
  plus a per-commander ranking per task, ranked top 20. The warzone
  totals are the whole warzone's counts; the ranking counts each
  commander separately.
- Counters, two live reads: 2026-11-09 08:29 PT - Tech 2383/500,
  Building 10721/500, Heroes 8833/10000, timer 6d 09:28:43;
  2026-11-09 11:38 PT - Tech 2607/500, Building 11186/500, Heroes
  9465/10000, timer 6d 06:20:41. The first two goals are already
  exceeded by the warzone; the third is at about 95% and still
  filling.
- Cycle and deadline: one event window, ends about 2026-11-15 17:56 PT
  (derived from the 6d 06:20 timer at 11:36 PT; the 0829 timer implies
  the same end within a minute).
- Rewards, Research Ranking read in full 2026-11-09 11:42 PT: No.1 -
  gold badge 25K x1, gold x20, 5m speedup x20, red gem x100; No.2 -
  500 badge x4, gold x15, 5m x15, red x80; No.3 to 5 - 500 badge x3,
  gold x12, 5m x12, red x60; No.6 to 10 - 500 badge x2, gold x10, 5m
  x10, red x50; No.11 to 20 - 500 badge x1, gold x8, 5m x8, red x40.
  No tiers below No.20 - the list ends there. The first item's exact
  name is unread (a gold medal/badge icon); the red gem is likewise
  unnamed in the popup. Both are recorded by icon and count only.
- Research Ranking, 2026-11-09 11:42 PT: rank 1 [AP3x] Teemo 31, rank
  2 [AP3x] Bamie 29, rank 3 [W77] 25, rank 4 [B3WB] etre 22, rank 5
  [CTR1] Lt grills 21, rank 6 [aP3x] jbG 16, rank 7 [W77] 16. The
  owner, [AP3x] Bears Lair, is Unlisted at 0 - no Tech Research
  counted in this window.
- Milestone claim state: milestone 1 (Unlock Tech) claimed by the
  2026-11-08 1914 unit - CONGRATULATIONS paid coin chest x3, red
  diamond x50, Oil 3.0K x6, 5-minute speedup x2. Milestone 2 (Unlock
  Stage, Base Expansion II) claimed by the 2026-11-09 0224 unit after
  the 1914 chest blocker. Both verified gone by the 0450 unit at
  04:44-04:50 PT; no chest sits on cards 1-2 at the 11:38 read. The
  0829 unit's "reward claim state unmeasured" is superseded by the
  0224 claim and the 0450 verification.
- Base Expansion II icon, corrected 2026-11-09 11:45 PT: the circular
  green-arrows icon below card 2 is NOT a chest and NOT unresponsive.
  One tap opened a popup - "Stage: Base Expansion II - A new stage is
  unlocked, your base is ready to expand further." - with a blue Go
  button, which was NOT tapped. This corrects Issue #477's "Base
  Expansion II chest unresponsive": that phrase conflated the
  milestone-2 chest (unresponsive at the 1914 unit, claimed by the
  0224 unit) with this stage-info icon, which responds and is not a
  reward.
- Cost: free. No diamonds, no money, no priced button anywhere on
  this path.
- Scoring: per-commander counts per task, ranked top 20; the owner
  sits at 0 research, leader at 31.
- Base screen on return: coin 46.2M, power 149,217,331 - unchanged.

## Open questions

- Hero Mobilization gold chest (at the right end of the card-3
  progress bar) and the greyed-out hexagon below card 3: contents
  unmeasured, not tapped in either exploration. Follow-up is on Issue
  #477.
- The play button at the stage track's right end: not tapped,
  contents unknown.
- The Building Upgrades and Hero Recruitments ranking tables and
  reward tiers: not opened, assumed parallel to the Research Ranking,
  not verified.
- A red "!" badge sits at the right edge of the tab bar in every Age
  of Oil screenshot; it was not attributed to a tab in either
  exploration (likely Desert Battlefield's badge, not verified).

## What the 2026-11-09 1146 scout-discovery unit added - Age of Oil learned with ranking rewards, Base Expansion II icon corrected

- Unit scout-scout-discovery-2026-11-09-014 by ticker-1134, about
  11:36 to 11:46 local, status done. Evidence in
  `_records_/2026-11-09/the-age-of-oil/1146-queue-run.md` (commit
  d2df49670 on records/2026-11-09). Read-only exploration: opened The
  Age of Oil, read all three cards and the stage track, opened the
  Research Ranking and its full Rewards list, and tested the Base
  Expansion II circular icon with one tap, reading its popup and
  closing it without tapping Go. Returned the game to the base screen.
  Nothing claimed, nothing spent, nothing answered, nothing navigated
  to.
- The 0829 exploration (unit 007, ticker-0804, record
  `_records_/2026-11-09/the-age-of-oil/0829-queue-run.md`, commit
  b58fc31b6 on records/2026-11-09) was sourced in perception-scout
  but never got its own profile until this fold; its mechanism read
  and first counter values are folded here alongside the 1146 read.
- The provisional profile was NOT written into `_activities_/` by
  either unit (tier 2, left for the knowledge PR flow); this profile
  is that write, by the knowledge organizer.
- Result stats: target learn-the-age-of-oil-profile-fields, achieved 6
  of 7 (Hero Mobilization chest contents unmeasured), resources_gained
  none, costs about 10 minutes of unit time, no items spent, verified
  yes, blocker_category none, points 0, surfaces_walked events-hub,
  the-age-of-oil-page, research-ranking, ranking-rewards,
  stage-info-popup, items_observed 3 task cards (tech 2607/500,
  building 11186/500, heroes 9465/10000), red_dots_seen 1,
  red_dots_explained 0, unexplained_red_dots 1, unknown_items 1.
