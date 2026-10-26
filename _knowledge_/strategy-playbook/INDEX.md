---
title: Strategy Playbook
created: 2026-10-26T04:45:00Z
modified: 2026-10-26T05:20:00Z
level: L1
version: 1.2.0
description: How this account is played day to day - the objective, duel week timing gates, radar discipline, resource floors and the tools that enforce them
status: unverified
grounded_in:
  - source: owner direction on duel schedule discipline and resource mapping, 2026-10-25
  - source: owner statement of the ultimate goal, 2026-10-25
  - source: in-game Alliance Duel schedule and theme page, observed 2026-10-25
  - source: in-game profile and Individual Power ranking, observed 2026-10-25
  - source: events-and-cycles knowledge in this repository
---

# Strategy playbook

## Objective

Owner, 2026-10-25 - the ultimate goal is to **increase Hero Power
and Total Power**, while balancing the use of available resources
and supporting the alliance, including the Alliance Duel and other
alliance activities. Everything in this playbook and in the daily
regulars is a means to that end: growth is the point, resources
are the constraint, the duel week is the calendar, and alliance
support is both a duty and a growth channel (gifts, help, tech and
events flow back as resources and power).

Baseline, read in game on 2026-10-25 - Total Power 149,689,618,
warzone Individual Power rank 113. Alliance benchmarks in the same
ranking: ItStartsWithaDream 247,971,851 (rank 2), Abyss Apex
227,095,526 (rank 3), StarFall 205,162,283 (rank 4); warzone top
[B3WB] RonMexico 277,043,357. The first growth gap to close is
therefore about 55M to the alliance's 200M band. Roster state -
the top heroes are Lv.150 five-star UR across the squads, with a
second band at Lv.140 to 145 and reserves at Lv.120; Squad 1
march power 24.96M as read on march panels. Progress against this
baseline is re-read from the ranking and recorded with resource
snapshots (`tools/resource_map.py`), so growth, not activity, is
what gets measured.

Owner direction, evening of 2026-10-25 - keep the Alliance Duel
weekly schedule in this repository, arrange the daily work around it,
keep a current map of all resources, and build tools that enforce
the plan. Everything about how this account is played lives in this
repository - schedules, strategy, tools, resource maps and records.

## The planning unit is the duel week

The Alliance Duel week (full table in `_knowledge_/events-and-cycles`)
sets when things are spent. Items and actions spent off-theme score
zero in the duel, so the week - not the day - decides timing.

- **Day 1, Radar Training** - radar release day (see radar
  discipline). Claims score at the in-game displayed +30,000 per
  task; stamina use scores +375 a point; drone parts +6,250.
- **Day 2, Base Expansion** - building power day. Finished upgrades
  are *collected* today (power registers on collection - "gift
  wrapping"), nothing is rushed with speedups (red line). **UR
  truck dispatches score today** (Handbook 100,000 each) and
  Legendary secret tasks score (75,000) - trucks go UR today and
  secret missions are refreshed toward gold, contracts permitting
  (keep a contract buffer, about 40; stock was 127).
- **Day 3, Age of Science** - research day. Research completions
  land today; **valor badges are spent only inside today** (same
  research, zero points outside the window); **drone component
  chests score only today**. Radar claims score again (release).
- **Day 4, Train Heroes** - hero spending day, the week's hoard
  release. Hero EXP, shards, skill medals and recruitment tickets
  wait all week for today. The owner spends these himself unless
  he delegates it; a run flags the day, it does not spend.
- **Day 5, Total Mobilization** - everything counts: training and
  promotions per unit, building and tech power, radar claims.
  The efficient pattern is waterfall promotions - low tiers
  trained in advance, promoted step by step today, each step
  scoring separately. Barracks stay full and rolling.
- **Day 6, Enemy Buster** - the 4-point day; combat is owner-led
  (a run never attacks outside the standing truck plunder rule).
  UR trucks and Legendary secret tasks also score. Radar stacking
  resumes.
- **Day 7, off day** - settlement and setup. Stack radar for
  Day 1, and mind the pre-matchmaking power assessment: finished
  upgrades are not collected during the Sunday assessment window
  where avoidable (Packsify) - they collect on Day 2 instead.
- **Dead window** - the roughly five minutes after each 19:00
  roll award no points (Handbook). Claims and spends wait until
  the new day is fully live.

## Radar discipline

The researched rule (Handbook and the Kimikas guide agree) is
finer than "save for Monday": **radar claims score on the odd
duel days only - Day 1, Day 3 and Day 5 - and points land at
claim time, not completion time.** The radar therefore runs on a
two-day rhythm all week:

- **Stack days (2, 4, 6, 7)** - complete tasks as they generate
  (Quick Execute and the special pins) but leave the rewards
  **unclaimed** in storage. Unclaimed tasks do not expire.
- **Release days (1, 3, 5)** - claim the whole stack early in the
  day (after the dead window), then keep completing and claiming
  as tasks regenerate.
- **Cap discipline outranks points.** Storage caps at 40 as
  observed (it scales with radar level in the guides). New tasks
  generate about every six hours, and if storage is full when a
  batch lands the refresh stalls and the batch is lost (LDShop) -
  so on stack days keep headroom of at least one batch under the
  cap, claiming a few early if a refresh would overflow.
- Value check still open - the in-game Radar Training page showed
  +30,000 per task where the Handbook lists 10,000 for days 1, 3
  and 5 (a Duel research multiplier may explain the difference).
  The in-game page governs; a one-task claim watched against the
  duel score on the next release day settles the number.

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
  down). Research is the giant coin sink at this tier - the four
  T10 gatekeeper nodes in Special Forces cost over 500M coin
  combined (Packsify research guide) - so coin is a campaign,
  not a one-day fix: research and construction pacing is the
  throttle (owner decisions), and income is pushed steadily.
  Push plan, in order: the weekly Gold Zombie event (the largest
  gold source in the guides - hoard stamina for it, rally the
  boss), intercity trucks (1.2M to 2.4M gold per truck, four a
  day), truck plunder under the shard rule (about 600K gold per
  UR truck), Monica-led world map zombie kills (+25% gold per
  the guides, if she is the fielded treasure hunter), VIP
  freebie boxes, radar rewards. No new coin-heavy commitment is
  started while coin is critical.
- The user's word "stone" maps to iron - the base game has food,
  iron and coin; seasons add their own (this season: coal and
  titanium alloy, both tracked in the resource map).
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
