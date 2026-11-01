---
title: Reflection 2026-10-31
created: 2026-11-01T05:00:00Z
modified: 2026-11-01T05:00:00Z
level: L2
version: 1.0.0
description: Reflection on the 2026-10-31 miss audit - what went wrong, and the fix landed for each root cause, named by file
status: fixes-landed
grounded_in:
  - source: miss audit of 2026-10-31 in this folder
  - source: owner instruction of 2026-10-31 to reflect and fix
---

# Reflection 2026-10-31

The owner asked for this reflection after two days of misses, and
then named the gaps himself - uncollected food, iron, coin and EXP,
drone components, ore and screws, trucks not collected and not all
plundered, daily claims and VIP claims unclaimed, the duel daily
target of 3.6M not reached, daily activities not collected, train
activities not all joined, crystal never fought for, and alliance
donations not completed. The audit of the same two days is
[miss audit 2026-10-31](miss-audit-2026-10-31.md). This document
accepts its findings, states what was wrong in plain terms, and maps
every fix to the file it landed in. Nothing here is a promise - each
fix below already exists in the repository or in the queue.

## 1. What the audit proved

- 198 units executed on 2026-10-30 and 2026-10-31. 98 done, 96
  partial, 4 skipped-needs-owner, 0 failed, 0 expired. 100 units
  closed non-done - half of everything that ran.
- The largest root cause is E, the same blocker repeated partial
  after partial with no escalation - 42 units. Second is C, a tap
  or point method failing with no effective method change inside
  the unit - 19 units. Together they are 61 of the 100.
- True red-line misses, where every scoring path was proven on
  screen to sit inside a red line, are only 4 units. 11 partials
  were by design - chain continuation and radar stack posture.
  The work was far less impossible than the raw partial count
  made it look. The failure was repetition without a pivot.
- Reported numbers were not all live reads. Four donation units
  closed on arithmetic final counts, truck counts closed on
  presumed and by-result figures, and the harvest records
  contradict each other on the name of one resource total.
- Whole items had no execution channel at all. Daily missions
  were never scheduled - metadata existed but the type was not in
  tools/regulars.json, so the planner never produced a unit. The
  duel daily total was never read on either day. The train was
  never checked per service. The Armed Truck was never claimed in
  two days. Screws and drone components have no claim record of
  any kind. And the crystal task, named by the owner on
  2026-10-25, produced zero units in six days because nothing
  owned its escalation.

## 2. What was wrong, in my own terms

- I treated partial as an ending. A unit that hit a blocker closed,
  and the next unit of the same type walked into the same blocker
  with the same method - 11 survivor units in two days, and Quick
  Dispatch did not run once.
- I let figures stand in for reads. When a counter was hidden, I
  closed on arithmetic instead of closing unverified and reading
  it later. The owner was given numbers I had not seen.
- I ran types, not a day. Each regular did its own pass, but no
  list anywhere said what a complete day of collection looks
  like, so entire lines - activity chests, the Armed Truck, the
  duel total - were invisible in every per-unit count, mine
  included.
- An owner-named task aged in silence. Crystal was hunted once on
  2026-10-25, the one lead (the Crystal Shop tab in the Store
  Building section, from the 2026-10-21 patch mail) was never
  walked, and no report in six days named it as still open. That
  is the worst failure in the audit because the owner had asked
  for it by name.

## 3. The fixes, and where each one landed

Queue discipline rules R1 to R8 are written into the
[task unit queue design](task-unit-queue-design.md), section 11,
version 0.7.0. The collection fixes live in the new
[daily collection ledger](daily-collection-ledger.md) and in the
activity metadata named below.

| Audit cause | Fix | Landed in |
| --- | --- | --- |
| D - inference instead of a live read, 6 units | R1 - a unit closes only on a same-unit live read. A hidden or blocked counter closes the unit as unverified and auto-enqueues a named re-read. Arithmetic, presumed, by-result and ranking-row figures are banned as closing counts | task-unit-queue-design.md section 11; alliance-donations INDEX closing rule |
| C - tap method failed, no pivot, 19 units | R2 - two no-change taps end the method. The executor re-grounds the point fresh, observes twice, and switches variant inside the same unit - measured centre, long-press, or a different entry path | task-unit-queue-design.md section 11 |
| E - same blocker, no escalation, 42 units | R2 - the second same-cause partial must change method. The third writes the blocker into the activity metadata, changes the entry route before any further unit of that type runs, and is named in that day round summary. A fourth identical partial is a process failure, not a result | task-unit-queue-design.md section 11 |
| A and F - quota gaps found at the deadline, slots and preconditions unread | R3 - quota types (trucks dispatch 5 and plunder 4, donations 30) carry two checkpoints per cycle, six hours and two hours before the cycle end. A checkpoint reads the counter live; a shortfall raises the next unit of that type to priority 1 | task-unit-queue-design.md section 11; alliance-donations INDEX scheduling rule |
| A and G - Arms Race phases judged at the end, 4 true misses | R4 - the phase is evaluated at its start. The first unit inside a phase reads the score and every scoring path; a phase with no path inside the red lines is reported to the owner as skipped-needs-owner early in the phase, never discovered at its end | task-unit-queue-design.md section 11 |
| A - gaps deferred across a window boundary, 6 units | R6 - no gap may be deferred across a window boundary inside the last 60 minutes of the window. The unit finishes inside itself or enqueues a priority 1 successor expiring at the window close, named in its summary | task-unit-queue-design.md section 11 |
| B - a subtask starved inside its own unit, 6 units | R7 - a subtask deferred twice in one day is promoted to the first action of the next unit of that type, or to a unit of its own | task-unit-queue-design.md section 11 |
| H - by-design partials counted as failure noise, 11 units | R8 - chain continuation and stack posture get their own label in reporting, split from misses, so the daily miss count only counts units that failed their own objective | task-unit-queue-design.md section 11 |
| I - owner-named task with no escalation, crystal, 6 days, 0 units | R5 - an owner-named task incomplete after 24 hours rises to priority 1 and is named in every round summary until it closes. Crystal itself is now modelled and queued - see section 4 | task-unit-queue-design.md section 11; _activities_/crystal-shop/INDEX.md; queue unit crystal-shop-2026-11-01-0503 |
| Checklist item 4 - daily missions never scheduled | daily-missions added to tools/regulars.json as a daily-reset regular on the VIP pattern, so the planner and the ticker sync produce its units. Validated by a scratch-root planner run before commit - see section 5 | tools/regulars.json |
| Unmodelled item, same class - the Glittering Market, named 2026-10-31 | Known only by its residue - a Glittering Market Unclaimed mail claimed through Event Claim All on 2026-10-27, 2026-10-29 and 2026-10-30 - while the market itself was never opened, located or worked on any day. Modelled as its own activity type, entered on the ledger with a closing standard that mail residue can never satisfy, and queued at priority 1 to be located - the daily-missions and crystal pattern applied from its first day instead of its sixth | _activities_/glittering-market/INDEX.md; daily-collection-ledger.md line 23; queue unit glittering-market-2026-11-01-0501 |
| Checklist item 5 - duel daily total never read | The alliance-duel metadata now requires a live personal daily total read per duel day against the owner target of 3.6M, the gap recorded, an unread total reported as unread, and a re-read enqueued - a fragment score never substitutes | _activities_/alliance-duel/INDEX.md |
| Checklist umbrella - whole lines invisible | The master daily collection ledger lists every daily line with its closing read, and two pre-reset zero sweep units walk it item by item before each 19:00 reset. The pair for 2026-11-01 is enqueued - see section 4 | daily-collection-ledger.md; task-unit-queue-design.md section 12; queue chain pre-reset-sweep-2026-11-01 |
| Owner-named gap - alliance donations not completed | The donations metadata now states the daily target as the full 30 of 30, the closing count as a same-unit live read of the remaining count, the timer-hidden fallback, and early-day scheduling under the R3 checkpoints | _activities_/alliance-donations/INDEX.md |

## 4. Crystal and the zero sweeps, as queued

- Crystal is modelled as its own activity type in
  `_activities_/crystal-shop/`, registered in the activities
  index, and one priority 1 unit is in the inbox -
  crystal-shop-2026-11-01-0500. Its body carries the whole job -
  Store, then the Building section, then the Crystal Shop tab;
  read the tab live, record the mechanism, claim what is
  claimable under the red lines, and backfill the mechanism into
  the metadata. Under R5 it stays named in every round summary
  until it closes.
- The zero sweep pair for the 2026-11-01 reset is enqueued as the
  chain pre-reset-sweep-2026-11-01 - unit 001 actionable from
  17:30 local and unit 002 from 18:30 local, both expiring at the
  19:00 reset (2026-11-02T03:00:00Z). Each walks the ledger item
  by item; a line not at zero gets a priority 1 unit of its own
  type enqueued before the sweep closes, named in the sweep
  record.

## 5. Validation and honest limits

- tools/regulars.json parses, the tracker lists daily-missions as
  due on the daily-reset rule, and a planner run against a scratch
  pool root produced the daily-missions unit for the current reset
  period alongside the other regulars, with no duplication on a
  second run. The live pool was not touched by the validation.
- The planner cannot yet express fixed clock slots such as 17:30
  and 18:30 - its cadences are the 4 hour segment anchors, the
  daily reset and Thursdays. Section 12 of the queue design
  documents the planner-side interface still to build and the
  manual enqueue practice in force until then. The sweep pair
  above was enqueued by that practice.
- These fixes change rules, scheduling and checklists. They do
  not play the game. Whether they work is measurable from the
  same place the audit read - the queue stats and the round
  summaries of the next days. The miss count, the unverified
  count and the named open items are the scoreboard.
