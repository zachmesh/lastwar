---
title: Events and Cycles
created: 2026-10-25T17:58:00Z
modified: 2026-10-26T05:20:00Z
level: L1
version: 1.2.0
description: Arms Race phases, the Alliance Duel VS week, the double-dip rule, and radar task discipline
status: unverified
grounded_in:
  - source: Last War Handbook arms race schedule guide, accessed 2026-10-25
  - source: Last War Vault arms race guide, accessed 2026-10-25
  - source: Packsify alliance duel strategy guide, accessed 2026-10-25
  - source: LDShop trucks and secret tasks guide, accessed 2026-10-25
  - source: in-game Alliance Duel weekly schedule and Radar Training theme page, observed 2026-10-25
---

# Events and cycles

External research. Event schedules were standardised across servers in a
November 2025 update (Handbook), so older guides may show per-server
times. The event page in game stays the final reference.

## Arms Race

- A daily individual event that never stops. The day splits into six
  four-hour slots rotating five phases — City Building, Unit Progression,
  Tech Research, Drone Boost, Hero Advancement — so one phase appears
  twice a day (Handbook; Vault agrees on slots and phases).
- Actions score at full or multiplied value only in their matching phase
  and nothing outside it (Packsify strategy guide; Vault). The discipline
  is to hold completions and spend until the matching window opens.
- One slot swap per day moves the current phase window; it changes timing,
  not scoring (Packsify alliance guide).
- The gold daily chest needs 18 badges a day, reachable by taking the
  second phase chest in each of the six slots (Packsify, single source).

## Alliance Duel — the VS week

Alliance Duel runs Monday to Saturday, one scoring theme per day, and
items spent off-theme score zero (Packsify; Handbook alignment table
agrees day by day) —

| Day | Theme |
|---|---|
| Monday | Radar Training |
| Tuesday | City Building |
| Wednesday | Tech Research |
| Thursday | Hero Training |
| Friday | Total Mobilization (troop training and promotion) |
| Saturday | Enemy Buster |

Sunday is the off day. Save speedups, hero EXP, skill items and training
for their theme day; the week, not the day, is the planning unit.

Verified in game on 2026-10-25 (Weekly Schedule page) — the day order
above is exact, with the in-game theme names and the win points each
day contributes to the weekly victory —

| Day | In-game theme | Win points |
|---|---|---|
| Day 1 (Mon) | Radar Training | 1 |
| Day 2 (Tue) | Base Expansion | 2 |
| Day 3 (Wed) | Age of Science | 2 |
| Day 4 (Thu) | Train Heroes | 2 |
| Day 5 (Fri) | Total Mobilization | 2 |
| Day 6 (Sat) | Enemy Buster | 4 |
| Day 7 (Sun) | off day | 0 |

- The duel day boundary is 02:00 UTC — 19:00 local (America Los
  Angeles). Day 1 of the current week opened Sunday 2026-10-25
  19:00 local with 21h22m left when read at 21:37, and the week
  timer read 5d 21h. Server weekdays in the table above therefore
  begin the previous local evening.
- This week's matchup — [AP3x] The Apex (warzone 2110) against
  [Sync] IMPERIUM (warzone 2111), week score 0 to 0 when read.
- Radar Training scoring, read off the theme page in game — Use 1
  Stamina +375; Complete 1 Radar Task +30,000; Use at least 660
  Hero EXP Points at a time +2.5; Use 1 Drone Battle Data point
  +7.5; Use 1 Drone Part +6,250; Buy Packs containing Diamonds
  +30 per diamond; Gather 100 Food +50, Gather 100 Iron +50,
  Gather 60 Coins +50 (radar gathering tasks excluded from the
  three gather rows); per Chip Chest opened and Premium Chip
  Material gained +2,812.5. Personal point chests at 2,600,000,
  3,600,000 and 7,200,000 points, ruby tagged 24,900, 46,900 and
  67,800. This account stood at 3,928,429 points for the day when
  read (the evening radar clear and the owner phone play both
  landed inside Day 1).
- The tooling form of this schedule is `tools/duel_schedule.json`,
  worked by `tools/duel.py`; the standing gates are in
  `_knowledge_/strategy-playbook`.

## The double dip

Since the alignment update, each VS day begins and ends with Arms Race
phases matching that day's theme, so one action scores in both events at
once (Handbook; Packsify explains the same mechanic). The high-value
windows are completions landing on theme — construction on Tuesday,
research on Wednesday, hero spending on Thursday, training on Friday.

## Radar tasks

- New secret tasks generate every six hours, in batches by radar level,
  with a storage cap on completed unclaimed tasks (LDShop).
- Completed tasks can be left unclaimed and cashed on a matching VS day
  for points. The trap is the cap — if storage fills, the refresh timer
  stops and a whole batch of tasks is lost overnight. Keep headroom
  before sleep (LDShop, single source for the timer-stop behaviour).
- Refined by the 2026-10-25 research brief (Handbook VS guide and the
  Kimikas guide agree): claims score on the **odd duel days (1, 3, 5)**
  at **claim time** — so the week runs stack days (complete, do not
  claim) and release days (claim early). The Handbook lists 10,000
  points per claim against the 30,000 the in-game Day 1 page displays;
  the in-game page governs and a watched one-task claim is the pending
  test. The operational rules live in the strategy playbook.
