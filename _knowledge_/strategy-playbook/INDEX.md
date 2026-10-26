---
title: Strategy Playbook
created: 2026-10-26T04:45:00Z
modified: 2026-10-26T04:45:00Z
level: L1
version: 1.0.0
description: How this account is played day to day - duel week timing gates, radar discipline, resource floors and the tools that enforce them
status: unverified
grounded_in:
  - source: owner direction on duel schedule discipline and resource mapping, 2026-10-25
  - source: in-game Alliance Duel schedule and theme page, observed 2026-10-25
  - source: events-and-cycles knowledge in this repository
---

# Strategy playbook

Owner direction, evening of 2026-10-25 - keep the Alliance Duel
weekly schedule in this repository, arrange the daily work around it,
keep a current map of all resources, and build tools that enforce
the plan. Everything about how this account is played lives in this
repository - schedules, strategy, tools, resource maps and records.

## The planning unit is the duel week

The Alliance Duel week (full table in `_knowledge_/events-and-cycles`)
sets when things are spent. Items and actions spent off-theme score
zero in the duel, so the week - not the day - decides timing.

- **Day 1, Radar Training** - radar tasks are worth 30,000 points
  each. Empty the radar completely, special pins included, and let
  stamina burn on scoring work.
- **Day 2, Base Expansion** - building power day. Completions should
  land today; nothing is rushed with speedups (red line).
- **Day 3, Age of Science** - research day. Research completions
  land today where the queue allows; starting research stays an
  owner decision.
- **Day 4, Train Heroes** - hero spending day. Hero EXP, skill
  medals and shards wait for today. The owner spends these himself
  unless he delegates it; a run flags the day, it does not spend.
- **Day 5, Total Mobilization** - troop training and promotion day.
  Keep every barracks queue full and rolling today.
- **Day 6, Enemy Buster** - the 4-point day. From today the radar
  is no longer emptied (see radar discipline).
- **Day 7, off day** - settlement. Preserve radar all day.

## Radar discipline

- Radar tasks are the Day 1 currency. On Day 6 and the off day,
  do not empty the radar - let the stock build so Day 1 opens with
  a full board (storage cap 40 as observed; the refresh stalls at
  the cap per LDShop, so on Day 1 the stock is spent early, not
  hoarded past the cap).
- Open question, to test at the next Day 1 - whether an unclaimed
  completed task scores when claimed on Day 1, or only tasks
  completed on the day score. The theme page wording (Complete 1
  Radar Task +30,000) reads as completion; LDShop describes leaving
  tasks unclaimed and cashing them on the theme day. One stored
  task claimed just after the 19:00 boundary, watched against the
  duel score, settles it.

## The double dip

Arms Race phases bookend each duel day on theme (events-and-cycles),
so a completion landing in the matching Arms Race window scores in
both events. Where a regular already produces completions -
training queues, building and research queues - prefer the timing
that lands them on theme, without burning anything to force it.

## Resource map and floors

- Every run that reads the HUD records a snapshot with
  `tools/resource_map.py snap`, and every run checks
  `tools/resource_map.py check` before spending anything.
- Floors live in `tools/resources.json`: coin warns below 10M and
  is critical below 2M; food and iron warn below 50M.
- State on 2026-10-25 evening - **coin is critical at 565.1K**
  (the owner's own Lv.30 building and research session spent it
  down). Push plan, in order: intercity trucks (1.2M to 2.4M gold
  per truck, four a day), truck plunder under the shard rule
  (about 600K gold per UR truck), VIP freebie boxes, radar rewards.
  No new coin-heavy commitment is started while coin is critical -
  coin-heavy starts are owner decisions in any case.
- Food 276.9M and iron 267.6M are healthy against their floors;
  their steady sinks are training batches (5.5M each at T10) and
  they refill from the same truck cycle.

## Enforcement

- `tools/duel.py` prints today's duel day, theme, gate and radar
  posture. Every scheduled run reads it first and follows the gate:
  on preserve days the radar regular is marked skip with the duel
  reason instead of being emptied; on Day 1 it is worked first.
- `tools/regulars.py` remains the per-day ledger of what was done;
  the gates change how a regular is worked, never whether it is
  accounted for.
- `tools/resource_map.py check` output rides along in run reports
  whenever a flag is raised.

## Standing boundaries

The recording rules red lines are unchanged and override this
playbook wherever they touch - no purchases, no diamond spending,
no speedup or stamina item burning to score, no research or
building starts on the agent's own initiative, no coal decisions.
The playbook times what is already allowed; it never widens it.
