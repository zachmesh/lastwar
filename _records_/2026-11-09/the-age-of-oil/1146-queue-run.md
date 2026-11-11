---
title: The Age of Oil queue run 1146
created: 2026-11-09T19:46:00Z
modified: 2026-11-09T19:46:00Z
version: 1.0.0
description: Ticker-1134 scout discovery unit 014, The Age of Oil read-only exploration - mechanism and ranking rewards learned, Base Expansion II icon corrected from chest to info button
status: done
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-09 11:36-11:46 PT
---

# The Age of Oil queue run 1146 (ticker-1134)

Unit: scout-scout-discovery-2026-11-09-014. Status: done.
Activity: the-age-of-oil (candidate exploration, read-only learning).
Chain: scout-discovery-2026-11-09, seq 14.

## Live reads

- Events hub tab bar, scrolled end to end: The Age of Oil is the
  leftmost tab, then Arms Race, Winter Battlefield, Desert
  Battlefield, Wanted Boss (red dot), Survey Center (red dot
  badge 1), Community. No Zombie Invasion tab - event still
  ended, no chain seeded.
- The Age of Oil page, read live about 11:38-11:46 PT: a stage
  track 1-2-3-4 across the top, stage 1 highlighted, with a
  circular play button at the right end (not tapped - unknown
  whether it plays an intro video). Three task cards, each with
  a countdown timer reading 6d 06:20:41 at first read and
  6d 06:14:49 at last read, so the event ends about 2026-11-15
  17:56 PT (derived from the timer).
- Card 1, "Unlock Tech: The Age of Oil": "Complete a total of
  500 Tech Research in this Warzone", progress 2607/500, gold
  full bar. The small bars icon at the card's top right opens
  the Research Ranking.
- Card 2, "Unlock Stage: Base Expansion II": "Complete a total
  of 500 Building Upgrades in this Warzone", progress 11186/500,
  gold full bar.
- Card 3, "Hero Mobilization": "Perform a total of 10000 Hero
  Recruitments in this Warzone", progress 9465/10000, green
  bar still filling. A gold chest icon sits at the right end of
  its progress bar, and a greyed-out hexagon sits below the
  card (contents unmeasured - not tapped in this unit).
- Research Ranking, read live about 11:42 PT: per-commander
  Tech Research counts for this event window. Rank 1 [AP3x]
  Teemo 31, rank 2 [AP3x] Bamie 29, rank 3 [W77] 25, rank 4
  [B3WB] etre 22, rank 5 [CTR1] Lt grills 21, rank 6 [aP3x]
  jbG 16, rank 7 [W77] 16. The owner, [AP3x] Bears Lair, is
  Unlisted at 0 - no Tech Research counted in this window.
  The warzone total 2607 on card 1 is the whole warzone's
  count; the ranking counts each commander separately.
- Ranking Rewards (Research Ranking, read in full): No.1 - gold
  badge 25K x1, gold x20, 5m speedup x20, red gem x100; No.2 -
  500 badge x4, gold x15, 5m x15, red x80; No.3 to 5 - 500
  badge x3, gold x12, 5m x12, red x60; No.6 to 10 - 500 badge
  x2, gold x10, 5m x10, red x50; No.11 to 20 - 500 badge x1,
  gold x8, 5m x8, red x40. No tiers below No.20 - the list
  ends there. (The first item's exact name is unread - a gold
  medal/badge icon; the red gem is likewise unnamed in the
  popup. Both are recorded by icon and count only.)
- Base Expansion II icon, tested live about 11:45 PT: the
  circular green-arrows icon below card 2 is NOT a chest and
  NOT unresponsive. One tap opened a popup: "Stage: Base
  Expansion II - A new stage is unlocked, your base is ready
  to expand further." with a blue Go button. The Go button was
  NOT tapped. This corrects Issue #477's "Base Expansion II
  chest unresponsive": the icon responds, it is a stage-info
  button, and there is no claimable chest on that card.
- Base screen on return: coin 46.2M, power 149,217,331 -
  unchanged.

## What was learned (profile fields)

- Entry: Events hub, The Age of Oil tab (leftmost tab).
- Mechanism: warzone-wide collective counters toward stage
  unlocks - 500 Tech Research, 500 Building Upgrades, 10000
  Hero Recruitments - plus a per-commander ranking per task
  (Research Ranking read; the other two cards carry the same
  bars icon, their rankings not opened in this unit).
- Rewards: ranking rewards measured in full above (top 20
  only). No separate stage-unlock reward was seen - the
  circular icons below cards 1 and 2 are stage-info buttons,
  not rewards. The Hero Mobilization gold chest and the grey
  hexagon below card 3 are unmeasured.
- Cost: free. No diamonds, no money, no priced button anywhere
  on this path.
- Cycle and deadline: one event window, ends about 2026-11-15
  17:56 PT (derived from the 6d 06:20 timer at 11:36 PT).
- Scoring: per-commander counts per task, ranked top 20; the
  owner sits at 0 research, leader at 31.

## What was done

- Opened The Age of Oil, read all three cards and the stage
  track, opened the Research Ranking and its full Rewards
  list, and tested the Base Expansion II circular icon with
  one tap, reading its popup and closing it without tapping
  Go. Returned the game to the base screen. Nothing claimed,
  nothing spent, nothing answered, nothing navigated to.

## Not done in this unit

- The Go button on the Base Expansion II popup: not tapped -
  it would navigate toward the base expansion, an action
  outside read-only learning.
- The Hero Mobilization gold chest and grey hexagon: not
  tapped, contents unmeasured.
- The play button at the stage track's right end: not tapped,
  contents unknown.
- The ranking icons on cards 2 and 3 (Building Upgrades,
  Hero Recruitments): not opened, so their ranking tables
  and reward tiers are unmeasured - assumed parallel to
  Research Ranking, not verified.
- A red "!" badge sits at the right edge of the tab bar in
  every Age of Oil screenshot; it was not attributed to a
  tab in this unit (likely Desert Battlefield's badge, not
  verified).
- The provisional profile was NOT written into _activities_/
  (tier 2, left for the knowledge PR flow). The candidate is
  tracked in Issue #477, commented with this unit's findings.

## Red lines

- No diamonds or money spent. No priced button tapped. No
  Go button tapped, no chest claimed, no other unit's work
  touched.

## Stats

- target: learn-the-age-of-oil-profile-fields
- achieved: 6 of 7 fields (Hero Mobilization chest contents unmeasured)
- resources_gained: none
- costs: about 10 minutes of unit time, no items spent
- verified: yes
- blocker_category: none
- points: 0
- surfaces_walked: events-hub, the-age-of-oil-page, research-ranking, ranking-rewards, stage-info-popup
- items_observed: 3 task cards (tech 2607/500, building 11186/500, heroes 9465/10000)
- red_dots_seen: 1
- red_dots_explained: 0
- unexplained_red_dots: 1
- unknown_items: 1
