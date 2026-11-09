---
title: Resource collection 2026-11-09 0340 queue run
created: 2026-11-09T11:52:00Z
modified: 2026-11-09T11:52:00Z
version: 1.0.0
description: Harvest unit by ticker-0334, resource quarter swept one tap per type, iron coin food EXP collected
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-09 03:40-03:52 PT
---

# Resource collection 2026-11-09 0340 queue run

- Unit: harvest-2026-11-09-0203, executor ticker-0334, session about 03:40-03:52 PT.
- Status: partial. The resource quarter was swept; the full-map zero-remaining
  acceptance is not met (other pans and the Armed Truck loot state unchecked).
- Entry: the game was on the world map after the radar unit's Iron Mine
  gathering dispatch (March Queues 1/4, Gathering 00:05:48 remaining at unit
  start). BASE returned to the base view. HUD at unit start, rounded as
  displayed: food 534.7M, iron 859.3M, coin 38.6M, second-row first resource
  13.22K, power 149,217,331, stamina 83.
- Recenter-first method executed: the centred base view showed no
  collectible bubble with a readable value label - the small green ticks on
  the iron-mine buildings are building status markers, not bubbles (verified
  on a 3x magnified crop). One long drag on empty road (norm 300,500 to
  700,500) panned the view west to the resource quarter, where the bubble
  cluster stood with readable labels.
- Bubble identification, read at full resolution before tapping: yellow
  circles with an EXP book icon and "1.8M" (experience), green circles with
  a blue iron ingot icon "876.8K", "1.0M", "974.9K", "974.9K" (iron), green
  circles with a gold coin icon "952.4K", "876.0K", "880.1K" (coin), yellow
  circles with a bread icon "1.1M" (food).
- Collections, each one tap on a freshly grounded bubble centre, HUD-verified
  in the same unit:
  - Iron: one tap on the 974.9K iron bubble centre (norm 671,397) cleared
    all four visible iron bubbles at once. Iron 859.3M to 864.2M, plus 4.9M.
  - Coin: one tap on the 952.4K coin bubble centre (norm 510,423) cleared
    all three visible coin bubbles at once. Coin 38.6M to 42.9M, plus 4.3M.
  - EXP: one tap on a 1.8M EXP bubble centre (norm 343,442) cleared all
    four EXP bubbles at once. No HUD resource measures EXP; clearance is
    verified visually on the follow-up screenshot.
  - Food: one tap on a 1.1M food bubble centre (norm 670,457) collected the
    food bubbles (bread icons seen flying in the collection animation).
    Food 534.7M to 540.1M, plus 5.4M.
- Totals this unit (HUD-rounded as displayed): iron plus 4.9M, coin plus
  4.3M, food plus 5.4M, EXP four 1.8M bubbles cleared.
- Mechanism finding, recorded as observed: one tap on a bubble of a
  resource type cleared every standing bubble of that type, not one bubble.
  This contradicts the 2026-11-08 1935 unit's iron one-by-one re-confirmation
  (one tap, exactly one iron bubble, plus 1.2M). The HUD deltas also exceed
  the sums of the visible bubbles of each type (iron plus 4.9M against
  3.83M visible, coin plus 4.3M against 2.71M visible, food plus 5.4M against
  about 3.3M visible), which suggests the tap collects that type base-wide,
  including bubbles off-frame - a candidate mechanism, NOT verified. The
  1935 one-by-one line is therefore suspect again, not settled; the
  knowledge organizer must reconcile it, and a knowledge Issue is filed
  from this unit naming the contradiction.
- Not done in this unit: the remaining base pans (farmland area, top and
  far-left edges) were not re-swept after the quarter clear; the Armed Truck
  loot state was not checked (its loot-panel entry is still unlocated);
  the Season 2 area at the bottom was left out of the sweep, per the
  standing rule that it is not main-base harvest. Bubbles regenerate within
  minutes, so the quarter will need re-sweeping by the next harvest unit.
- No diamonds or money spent, no Buy tapped, no building panel actioned,
  no other activity worked from this unit. Tracker untouched for partial,
  per the queue rules.

## Issue filed

- GitHub Issue #502 (label knowledge): one tap clears all bubbles of a
  resource type, contradicting the 1935 iron one-by-one re-confirmation.
