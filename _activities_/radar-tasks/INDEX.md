---
title: Radar Tasks
created: 2026-10-25T18:58:00Z
modified: 2026-11-02T03:47:03Z
level: L1
version: 1.9.0
proficiency: learning
description: Radar stored tasks, Quick Execute coverage and exceptions, map pin handling, stack and release completion standards and duel scoring
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25 to 2026-10-31
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1904 radar release unit)
  - source: owner structure direction on activity folders, 2026-10-25
  - source: owner live guidance during the evening radar clear, 2026-10-25
  - source: Last War Wiki Radar Tasks page on Fandom, accessed 2026-11-01
  - source: LDShop radar and secret tasks guide, accessed 2026-11-01
  - source: GrindnStrat radar tasks guide, accessed 2026-11-01
  - source: Last War Handbook VS schedule guide, accessed 2026-11-01
  - source: lastwar.wiki Alliance Duel page, accessed 2026-11-01
  - source: radar tasks execution record 2026-11-01 1122 queue run
  - source: radar tasks execution record 2026-11-01 1629 queue run
---


# Radar tasks

## What this activity is

Working the radar - executing stored ordinary tasks with Quick
Execute, claiming their rewards on the days claims score, and
handling the map pin tasks that Quick Execute does not cover.
This profile was hardened on 2026-11-01 under the learning and
knowledge hardening protocol (perception-driven queue design,
section 10), as the first retrospective hardening target. Every
field below carries its evidence basis - measured in game,
dual-source web agreement, single source, or still open - and
the profile stays at proficiency learning until the open fields
in the proficiency table close.

Executions are recorded in `_records_/<date>/radar-tasks/`, one file per execution.

## Knowledge sources

- In-game execution records, 2026-10-25 to 2026-10-31 (this
  repo, `_records_` radar folders) - the primary source; where
  web sources disagree with a live in-game read, the in-game
  read governs and the disagreement is noted.
- Last War Wiki (Fandom), Radar Tasks page, accessed
  2026-11-01 - level table (refresh quantity, storage,
  maximum concurrent tasks), task type probabilities, quality
  distribution.
- LDShop, Last War Trucks and Secret Tasks guide, accessed
  2026-11-01 - refresh cycle, storage cap behaviour, stacking
  strategy for duel days 1, 3 and 5.
- GrindnStrat, Last War Radar Tasks guide, accessed
  2026-11-01 - refresh cycle, per-task expiry timers,
  cap-stops-refresh behaviour.
- Last War Handbook, VS schedule guide, and lastwar.wiki,
  Alliance Duel page, both accessed 2026-11-01 - radar task
  duel value of 10,000 points per task (base, before research
  bonuses).
- One dissenting source was rejected - a GeekVibesNation
  guide claims an 8 hour refresh; the Fandom table, LDShop
  and GrindnStrat agree on 6 hours, and the in-game restore
  line (12 tasks per restore at this level) matches the
  Fandom row for levels 12 and 13, so 6 hours stands.

## How to enter - hardened against the rotating shortcut

- The radar opens from the satellite dish icon in the base
  left icon column. That slot is a ROTATING shortcut - the
  same slot can open Secret Command Post or Intercity Trade
  instead (see `_activities_/secret-missions`). A tap on the
  slot is never proof of entry.
- Ground the icon fresh from a current screenshot in every
  unit. On a fresh 2026-10-29 screenshot the dish with its
  red badge sat at norm 62,727 and opened the radar on the
  first tap. The earlier estimate norm 54,667 opened Secret
  Command Post in the 06:44 and 11:19 units of 2026-10-29 -
  two whole units lost to a stale coordinate.
- ENTRY VERIFICATION, mandatory before any work - the radar
  screen is confirmed only when the screen shows radar level
  and points top left, stored tasks out of 40, and the
  stamina figure top right. If Secret Command Post, Intercity
  Trade or anything else opens, back out untouched, re-ground
  and retry; never do another activity's work from a radar
  unit (one unit, one type). Neighbouring icons that are NOT
  radar, both hit on 2026-10-29 - the magnifier (world search
  panel) and the yellow radio device (Mission screen; its
  Claim buttons belong to daily-missions).
- The radar screen shows the restore line ("N Radar Task(s)
  will be restored in HH:MM:SS"), the full restore time, the
  bottom action bar, and the task pins on the map itself.

## Mechanism

- Radar level - Lv.13 since the level-up in the 2026-10-30
  06:23 unit (Lv.12 before). Storage cap 40 at both levels
  (measured; Fandom agrees).
- Refresh - the restore line restores 12 tasks per cycle at
  this level (measured repeatedly, e.g. "12 Radar Task(s)
  will be restored in 04:05:40" at the 2026-10-29 18:47
  close). Cycle length about 6 hours (dual source - Fandom
  level table and LDShop; consistent with stored counts
  rising between units). Whether the restore lands as one
  batch or trickles is not yet settled - see open questions.
- Cap behaviour - when storage hits the cap, the refresh
  timer stops and no new tasks generate (dual source -
  LDShop and GrindnStrat). Stack discipline therefore keeps
  headroom - leave stored at or below 39 of 40 whenever a
  restore cycle will land before the next unit.
- Task expiry - uncompleted tasks carry their own timers
  and disappear when the timer runs out (GrindnStrat; the
  in-game pin cards show countdowns, e.g. about 7 hours 56
  minutes on the 2026-10-25 story pin). Completed but
  unclaimed tasks also expire if never claimed (GrindnStrat)
  - on release days, claim before expiry, do not admire the
  stack.
- Task types (Fandom, single source, not yet verified
  in game) - guaranteed daily one Eliminate Rebels and one
  Defeat Doom Elites; the random pool is Ally Assistance
  30 percent, Zombie Sampling 30 percent, Geological
  Sampling 20 percent, Rare Resource Mining 20 percent,
  each with a 0.25 percent chance to upgrade to a Treasure
  Digging task. Qualities run Common to Legendary with
  type-specific distributions.
- Radar points counter - claiming a task adds 1 radar point
  (measured many times, e.g. 39 claims moved 2,950 to 2,989
  on 2026-10-29). After the Lv.13 level-up the counter
  displayed small numbers again (29 on 2026-10-31 morning
  against 2,989 the day before) - an apparent per-level
  progress reset, observed once, mechanism unverified. The
  radar points counter is NOT the duel score; see Scoring.

## Stamina

- Cap 120, regenerating 1 point every 300 seconds
  (measured).
- Ordinary task through Quick Execute - 10 stamina each
  (measured across dozens of batches).
- Pin task march costs vary by type (measured) - story pin
  march 5, Doom Walker rally 20, gathering pins 0.
- Free stamina claim - the Regain Stamina panel offers 75
  stamina free, cooldown 4 hours, twice a day (measured -
  Remaining Today reads 2 of 2 down to 0 of 2; taken in the
  2026-10-29 02:24 and 18:47 units). Always take the free
  claim first when stamina blocks execution.
- Paid option - Buy 100 stamina for 300 rubies. NEVER use
  it (red line).
- Stamina items (10 and 50) exist in inventory in the
  hundreds (measured counts in the Regain panel). Use only
  under the standing stamina rules for scoring pushes -
  Free Claim first, then items, never rubies.

## Quick Execute - coverage and exceptions

Coverage (measured in game; web sources do not document
Quick Execute's exact scope, so this section rests on the
execution records):

- COVERS - ordinary stored tasks, executed in batches. The
  bottom bar states how many tasks can be completed and the
  stamina required. After the marches, the bar flips to
  Claim All with the count of rewards waiting.
- DOES NOT COVER - every map pin task (story pins, Doom
  Legion base, Doom Walker, gathering mines), finished-task
  pins waiting on the map, and anything resolved on the
  world map. A radar clear is never proven by the bottom bar
  alone; the pin scan decides.
- Behaviour trap, measured across 2026-10-31 - the bottom
  bar presents ONE offer at a time. In the 06:12, 14:15,
  18:38 and 22:06 units it presented Claim All (rewards
  waiting) and no Quick Execute, so the stored tasks could
  not be executed at all; that is the structural reason the
  stack day stalled - the 02:39 unit executed 6 tasks, and
  most later units were locked out, with stored tasks
  sitting at 21 of 40 unexecuted by 14:15. But the block is
  not absolute - the 10:40 unit was presented a Quick
  Execute offer (1 task) despite 7 rewards pending from the
  06:12 close, and ran it. What selects which offer the bar
  presents is not understood (open question); never assume
  either way - read the bar that is actually shown.
- With too little stamina, tapping Quick Execute opens the
  Regain Stamina panel instead of failing - use the free
  claim there and continue.

## Map pins - taxonomy and handling protocol

Pins are not one thing. Classes proven in game:

- Finished-task pins - a completed ordinary task standing on
  the map with a red dot. Tapping it claims INSTANTLY - a
  CONGRATULATIONS popup, no card, no chance to back out
  (measured twice on 2026-10-29, a blue person pin at 02:24
  and a purple skull pin at 14:52; each paid at once and
  added 1 radar point). This is how part of the stacked
  rewards present on the map.
- Story pins - a purple question mark pin, NOT covered by
  Quick Execute. Full verified flow under Special pin tasks
  below (A Distressed Survivor, 2026-10-25).
- Doom Legion base pin - jumps to a legion base on the world
  map; attacking destroyed it outright (loot about food
  1.4M, iron 1.4M, coin 0.9M to 1.7M as read).
- Doom Walker pin - a world boss rally (cost 20 stamina,
  rally about 7 minutes here). A launch is real only when
  stamina drops by 20 AND the march timer appears - the
  first launch on 2026-10-25 was a silent no-op.
- Gathering pins - purple mine pins (Diamond Mine, Rare Gold
  Mine, 2026-10-26). Card names the spot, rewards and a
  despawn timer of about 3 hours; Go, advance any story
  dialog, tap the pickaxe button, a full squad gathers at
  no stamina cost. The pin reward is claimed at the radar
  afterwards (Claim All or tapping the finished pin); the
  gathered yield itself lands in the HUD on squad return.
- Unidentified standing pins - an orange arrow pin, a purple
  axe pin and an orange axe pin stood on the map through the
  2026-10-29 release units, plus a portrait pin on 2026-10-29
  22:21, none ever tapped, type unknown. Do not guess their
  class from colour; they head the open questions.

Handling by posture (binding):

- RELEASE posture - every pin is worked to a closing read
  in the unit: tapped and completed, claimed, or identified
  with the reason it is left. "Pins left unattempted" is a
  partial, never a done - the 2026-10-29 18:47 and 22:21
  units both closed partial on exactly this, and the pins
  were still standing the next day.
- STACK posture - do NOT tap pins. A finished-task pin pays
  instantly on tap and leaks the claim onto a non-scoring
  day. Instead the unit records a pin inventory (class if
  known, position, red dot or not) as part of its closing
  read, so the release-day unit inherits a checklist rather
  than a surprise.
- Either posture - the pin scan is part of the closing read
  of every radar unit. No scan, no done.

## Special pin tasks - verified flow (A Distressed Survivor)

1. Tap the pin on the radar map. A bottom card opens with
   the task title, a countdown (about 7 hours 56 minutes
   remaining), the reward area and a Go button. Rewards may
   be hidden behind a state line - here "Break the ice to
   view rewards".
2. Tap Go. The view jumps to the task location on the world
   map and the card shows the situation state - here Thawing
   Soon with a timer, a snowflake bar at 1,000 of 1,000, and
   one large round contextual action button (a hammer here).
3. Tap the contextual button. A march panel opens - squad,
   power versus Unknown, a match rating, march time and a
   stamina cost (5 here). Tap March. The squad marches
   (March Queues 1 of 4, back to 0 of 4 on arrival) and the
   situation resolves.
4. Go back to the radar screen and tap the same pin again.
   The card has changed - the reward list is now revealed
   (here a survivor times 1, a paw print item times 200 and
   black rock times 207.3K).
5. Tap Go again. On the world map the card is simplified and
   the round button is now a green magnifier.
6. Tap the magnifier. A story conversation opens with a
   large character portrait. Keep tapping the bottom of the
   dialog to advance it to the end - complete the
   conversation with clicks only. If a chat screen opens by
   an extra tap, the Back Arrow at the bottom left exits it.
7. Return to the radar screen. The bottom bar reads "1 task
   rewards can be claimed" with a Claim All button. Claim
   All pays the revealed rewards and adds 1 radar point.
   The pin and its red dot disappear.

## Scoring - duel days

- Posture follows the duel day (_tools_/duel.py) - stack on
  even days (complete, do not claim), release on odd days
  1, 3 and 5 (claims score). Radar claims score at the
  moment of claiming, not at completion - the whole stack
  and release rhythm rests on this (owner-taught rule,
  corroborated by LDShop and the tkw FAQ page, both accessed
  2026-11-01 - save radar tasks for days 1, 3 and 5).
- Per-task duel value - the Handbook and lastwar.wiki both
  list Complete 1 Radar Task at 10,000 points (base, before
  Alliance Duel research bonuses). The in-game VS panel on
  this account displays plus 30,000 per task (recorded in
  _tools_/duel_schedule.json). The in-game value governs
  planning; the gap is presumed to be duel research bonus
  but is NOT verified - the delta test (read duel score,
  claim one batch, read again) is still owed and heads the
  open questions.
- Do not read the radar points counter as duel score - it
  moves 1 point per claim and says nothing about the duel.

## Stack day completion standard

A stack-day radar unit is done only when ALL of these hold:

- The radar screen was entered and verified (level, stored
  count, stamina read on the radar screen itself).
- Every executable ordinary task was executed - Quick
  Execute batches run until no offer remains or the stamina
  floor under the standing rules is hit, free claim taken
  first when stamina blocks.
- Closing reads are recorded - stored count, pending reward
  count on the Claim All bar, stamina, and the pin
  inventory (untapped, per the stack handling rule).
- If the bar presents Claim All and no Quick Execute (the
  2026-10-31 trap - rewards left pending by an earlier unit
  can lock later units out of execution), the unit records
  that blocker by name with the pending count - not a
  generic partial - and the block is carried into the next
  unit's opening read, so the stack is planned around it
  instead of rediscovered hourly.

## Release day completion standard

A release-day radar unit is done only when ALL of these hold:

- Claim All worked until the bar disappears; Quick Execute
  batches interleaved until stored reads 0 of 40 or only
  restoring tasks remain (the 2026-10-29 18:47 shape - 39
  claimed, 12 executed, stored 0 of 40).
- Every map pin has a closing read per the release handling
  rule - completed, claimed, or identified with a reason.
- Closing reads recorded - stored count, radar points,
  stamina, restore line - and, on a scoring day, the duel
  score before and after where the panel allows the read
  (this is also how the pending delta test gets done).

## Red lines

- Never tap Buy in the Regain Stamina panel (100 stamina
  for 300 rubies).
- Never tap map pins and never tap Claim All on a stack
  posture day.
- Never claim another activity's rewards from a radar unit
  (the Mission screen belongs to daily-missions).

## Red dots and red badges - the owner rule

- A red badge number on a tab or icon means that many tasks
  or claims are ready to do there (owner, 2026-10-25).
- A red dot on a radar map pin means that pin is clickable
  and its task can be done now (owner, 2026-10-25). Do not
  treat a pin with a red dot as decoration - open it (on a
  release day; on a stack day, inventory it instead - see
  the pin handling protocol).

## Failure history this profile is hardened against

- 2026-10-29 06:44 and 11:19 - two stack-day units never
  entered the radar screen; the stale dish coordinate opened
  Secret Command Post both times and the units closed
  without a single radar read.
- 2026-10-29 18:47 and 22:21 - release-day units claimed 39
  tasks and cleared ordinary tasks to 0 of 40, then left
  three standing pins (orange arrow, purple axe, orange
  axe) untapped with "falls to the next tick"; the pins
  were never closed by any later unit.
- 2026-10-25 - the special story pin (A Distressed
  Survivor) was invisible to Quick Execute and surfaced
  only when the owner pointed at the still-standing pin;
  it had no completion standard until its flow was worked
  and written down the same evening.
- 2026-10-31 - stack day closed with stored tasks at
  21 of 40 unexecuted; the bottom bar presented Claim All
  instead of Quick Execute in four units, locking out
  execution, and the block was treated as weather instead
  of a named blocker with a plan.

## Proficiency by field

- Entry and entry verification - proficient (measured,
  including the failure and its correction on 2026-10-29).
- Storage cap 40 - proficient (measured; Fandom agrees).
- Ordinary task stamina cost 10 - proficient (measured).
- Free stamina claim terms - proficient (measured).
- Refresh quantity 12 per cycle - proficient (measured).
- Refresh cycle length 6 hours - supported (dual source;
  no direct in-game timing measurement yet).
- Cap stops refresh - supported (dual source; not yet
  measured in game on this account).
- Quick Execute coverage of ordinary tasks - supported
  (measured repeatedly; web sources silent on exact scope).
- Bottom bar single-offer behaviour (Claim All presented
  instead of Quick Execute) - supported as behaviour
  (measured four times on 2026-10-31, with one counter-
  observation the same day); the rule that selects the
  offer is open.
- Pin taxonomy - learning (four classes measured; the
  standing arrow and axe pins are unidentified).
- Task types and probabilities - learning (single source,
  Fandom; guaranteed daily pair unverified in game).
- Duel scoring per task - learning (dual source base value
  10,000 against an in-game display of 30,000; delta test
  owed).
- Radar points counter behaviour across level-up - learning
  (one observation).

Profile level stays learning - the weakest key fields
(scoring value, pin taxonomy, Quick Execute re-offer rule)
are still open, per the protocol.

## What the 2026-11-01 1122 unit added

- Stack posture held throughout, status done
  (ticker-1114, session about 11:16 to 11:22, duel day 7
  off-day settlement, radar posture stack per
  tools/duel.py): tasks executed, nothing claimed, no
  map pin tapped. This unit was missed by the 1132
  organizer run's input list and is folded here, so the
  watermark gap is closed, not carried.
- Entry verified on the radar screen itself: satellite
  dish icon at norm 62,727 opened the radar on the first
  tap. Lv.13, radar points 45, stored 33 of 40, stamina
  135, restore line 12 tasks in 03:29:29.
- Quick Execute: the bottom bar offered 5 tasks for 50
  stamina and no Claim All at entry, so the batch ran.
  Stamina 135 to 85, exactly 5 tasks at 10 stamina each.
  Radar points stayed 45, confirming nothing was
  claimed.
- Closing reads: stored 33 of 40 (unchanged by execution;
  the executed tasks moved to the pending-reward count),
  restore 12 tasks in 03:28:04, stamina 85, radar points
  45.
- Named blocker carried forward: after the batch the bar
  flipped to Claim All only, 11 task rewards pending (6
  already pending at entry plus the 5 just executed),
  with no further Quick Execute offer. Claim All was NOT
  tapped, per the stack-day red line. The next radar unit
  inherits this blocker and the pending count of 11, per
  the stack-day completion standard's named-blocker rule.
- Pin inventory, untapped per the stack handling rule,
  all red-dotted: grey handshake pin, green handshake
  pin, and orange skull pin on the radar map. No pin was
  tapped, so no claim leaked onto this non-scoring day.
- Headroom warning with a deadline: stored 33 of 40 sits
  below the 39 cap guard, but the 12-task restore landing
  in about 3.5 hours - about 14:50 - would overshoot the
  40 cap if no unit executes or claims before then. A
  later unit must act before the restore lands; on a
  stack day that action is execution, not a claim, and
  execution is currently locked behind the Claim All
  only bar above, so the next radar unit faces the
  blocker and the deadline together.


## What the 2026-11-01 1629 unit added

- Unit radar-2026-11-01-1403 by ticker-1604, session
  about 16:19 to 16:29, status partial. Duel day 7,
  off-day settlement, radar posture stack. Nothing was
  executed and nothing was claimed. The tracker is
  untouched, so the next tick re-produces this regular.
- Entry failure mode: radar entry was attempted from
  a fresh base screenshot. The dish icon was grounded
  at 53,688 on that screenshot and tapped. The
  resulting screen was not the radar screen - it showed
  base buildings and production bubbles in a panned
  view, with no radar level, no stored count, no
  stamina figure and no bottom action bar. Entry
  verification therefore failed. No Secret Command
  Post and no Intercity Trade opened, and no other
  activity was worked from this unit. A dish tap that
  lands on a panned base view is a failed entry, not a
  radar read; the entry must be re-grounded from a
  verified base view, not retried blind.
- Recovery cut short, and correctly stopped: the
  computer session dropped twice during this pass and
  had to be restarted, and a visual grounding call for
  the recovery controls timed out after three minutes.
  With the pass budget nearly spent, no further
  navigation tap was attempted, because a blind tap on
  an ungrounded control risked opening another
  activity. No map pin was tapped and no Claim All was
  tapped, so the stack posture held with no claim
  leaked onto this non-scoring day.
- First read owed by the next radar unit: the stored
  count. The opening state carried in (1122 unit,
  11:22 local) was entry verified Lv.13, radar points
  45, stored 33 of 40, stamina 85, restore 12 tasks in
  03:29:29, with the bar flipped to Claim All only and
  11 task rewards pending. The 12-task restore landing
  about 14:45 local would have pushed stored toward
  the 40 cap. This unit obtained no fresh stored count,
  so whether stored now sits at the cap is unverified
  and is the first read the next unit must make.

## What the 2026-11-01 1904 unit added

- Unit radar-2026-11-01-1803 by ticker-1904, session about
  19:05 to 19:35, status partial. The unit window text still
  read "duel day 7 - radar stack" (stamped at production
  before the 19:00 reset); the live posture from
  tools/duel.py governs, so this unit ran as a release
  unit: duel day 1, Radar Training, radar posture release,
  day ends 2026-11-02 19:00 local, more than 5 minutes
  after the 19:00 roll, past the dead window named in the
  duel gate.
- Entry verified on the first tap at norm 62,727 (the
  2026-10-29 measured dish point): Lv.13, radar points 66,
  stored 19 of 40, stamina 145, restore line "Fully
  restore at 11-2 03:31:43 local time" at entry. Later
  reads in the same unit showed 15:31:43; the hour figure
  is recorded as displayed and is unverified - neither
  figure is adopted over the other here.
- Batch 1: Quick Execute 4 tasks, stamina 145 to 105. Bar
  flipped to Claim All, 10 task rewards. Claim All claimed
  10, radar points 66 to 76. Rewards: chest times 25, radar
  item 100, EXP 14.1M, drone item 3.2K, blue triangle 450,
  iron 3.9M, food 2.3M, coin 2.0M.
- Batch 2: Quick Execute 3 tasks, stamina 105 to 75,
  stored 9 of 40. Bar flipped to Claim All, 8 task rewards.
  Claim All claimed 8, radar points 76 to 84. Rewards:
  radar item 70, EXP 14.2M, drone item 3.2K, speedup 5m
  times 7, speedup 1m times 85, iron 4.4M, food 3.6M, coin
  1.3M.
- Batch 3: Quick Execute 4 tasks, stamina 75 to 35, stored
  1 of 40. Bar flipped to Claim All, 7 task rewards. Claim
  All claimed 7, radar points 84 to 91. Rewards: radar item
  70, EXP 13.2M, drone item 2.4K, iron 3.3M, food 2.4M, coin
  1.3M.
- Totals in this unit: 11 tasks executed, 25 rewards
  claimed, radar points 66 to 91, stamina 145 to 35, coin
  claimed across the three popups 2.0M plus 1.3M plus 1.3M
  equals 4.6M (popup figures, not HUD totals).
- Contradiction resolved in favour of the newest live
  read: the prior radar unit 1629 never entered the radar
  screen, so its reads were carried from unit 1122 (stored
  33 of 40, stamina 85, 11 task rewards pending). Those
  carried figures are superseded by this unit's live
  re-read (stored 19 of 40 at entry, 0 of 40 at close,
  stamina 145 to 35). The stored-count first read the 1629
  unit owed is now answered: 19 of 40 at entry.
- Closing state (live reads, same unit): Radar Lv.13,
  radar points 91, stored 0 of 40, stamina 35, restore line
  "12 Radar Task(s) will be restored in 02:16:05", fully
  restore 11-2 15:31:43 local time as displayed.
- Offer-versus-stored mismatch, carried as an open rule:
  the bottom bar offers 1 more task for 10 stamina while
  stored reads 0 of 40, so the offer count and the stored
  count do not move together. The next unit must read the
  bar it is actually shown, not infer it from stored.
- Pin inventory, untapped in this unit: purple
  question-mark story pin top centre, purple skull pin
  centre, orange axe pin lower left, blue skull pin lower
  centre, plus one alliance portrait pin ([AP3x]Black
  Death) that is not a task. The green and blue skull pins
  with red dots seen at entry are gone after the claims.
  Per the release standard, pins left unattempted make
  this unit partial, never done; the next radar unit must
  work the pins to a closing read (completed, claimed, or
  identified with a reason) and run the remaining 1-task
  offer.
- Duel delta test still owed: the VS panel was not opened
  in this unit, so no duel score before and after was
  read. The 25 claims on a scoring day are the batch the
  delta test should measure against (see alliance-duel
  1.8.0).
- Entry method note: a visual grounding call during entry
  timed out after 3 minutes; entry then succeeded on the
  documented coordinate, so no method change was needed.
- No diamonds or money spent, no Buy tapped, no map pin
  tapped, no other activity worked from this unit. Tracker
  untouched for partial, per the queue rules.


## Open questions

- Duel delta test - on the next release day, read the duel
  score, claim exactly one batch, read again; settle whether
  a radar claim pays 10,000, 30,000 or another figure on
  this account, and what the bonus source is.
- Bottom bar offer selection - the bar presents one offer
  at a time; why did the 2026-10-31 10:40 unit get Quick
  Execute despite 7 pending rewards, when the 06:12, 14:15,
  18:38 and 22:06 units got Claim All and no Quick Execute?
  Candidate factors to test - completable task count at
  entry, pending count, restore timer state.
- Standing pin types - identify the orange arrow, purple
  axe, orange axe and portrait pins (class, cost, reward)
  on the next release day, by tapping them under the
  release handling rule.
- Restore shape - does the 12-task restore land as a batch
  at the 6 hour mark or trickle? Compare stored counts
  against the restore line across one full cycle.
- Where a survivor gained from a special radar task reports
  to - base gate queue or straight onto the roster.
- How often special pins appear, and whether the skull and
  handshake pins seen on 2026-10-25 follow the story flow.
- Whether manual per-task execution ever beats Quick
  Execute (cost or reward difference), untested.

## Changelog

- 1.9.0, 2026-11-01 - 1904 duel day 1 release unit folded:
  live re-read supersedes the 1629 carried figures (stored 19
  of 40 at entry, 0 of 40 at close; stamina 145 to 35; points
  66 to 91 over 11 tasks and 25 claims); offer-versus-stored
  mismatch recorded; pins left unattempted so the unit stays
  partial; duel delta test still owed.
- 1.8.0, 2026-11-01 - 1629 entry-failure unit folded:
  dish tap at 53,688 landing on a panned base view is a
  failed entry, not a radar read; recovery correctly stopped
  rather than blind-tapped; stack posture held on duel day 7
  off-day settlement; the next unit's first read is the stored
  count against the 40 cap after the about 14:45 restore.
- 1.6.0, 2026-11-01 - first retrospective hardening pass,
  worked as the knowledge organizer's first work order under
  the learning and knowledge hardening protocol. Entry
  section rewritten around the rotating shortcut with
  mandatory screen verification; mechanism table completed
  from the 2026-10-25 to 2026-10-31 records (refresh
  quantity, cap behaviour, expiry, task types); Quick
  Execute coverage and exceptions made explicit, including
  the Claim All bar trap measured on 2026-10-31; pin
  taxonomy and posture-dependent handling protocol added;
  stack and release completion standards stated as checkable
  closing reads; scoring section records the 10,000 dual
  source base against the in-game 30,000 display with the
  delta test owed; proficiency table added per field.
  Web research accessed 2026-11-01 - Fandom Radar Tasks,
  LDShop guide, GrindnStrat guide, Last War Handbook VS
  schedule, lastwar.wiki Alliance Duel; one dissenting
  8 hour refresh claim rejected against dual source and the
  in-game restore quantity. Registration note - the retro
  improvements backlog (_records_/retro/improvements.md)
  does not exist yet at the time of this pass; it is to be
  created by the first retro run, so this work order is
  registered here rather than in a backlog file, and the
  first retro should lift it into the backlog as a
  knowledge-organization task pending closure by field
  verification in later execution units.
- 1.5.0 and earlier - incremental field notes from the
  2026-10-25 to 2026-10-29 executions (entry grounding,
  pin tap caution, special pin flow, doom pins, gathering
  pins), preserved in git history.
- 1.7.0, 2026-11-01 - stack-day 1122 unit folded (missed
  by the 1132 run's input list, gap closed here): 5-task
  Quick Execute batch at 10 stamina each, points held at
  45, bar flipped to Claim All only with 11 rewards
  pending, handshake and skull pins inventoried untapped,
  and the 12-task restore landing about 14:50 that would
  overshoot the 40 cap. (1.6.1 was a minor bump without
  a changelog line; the numbering is preserved, not
  rewritten.)
