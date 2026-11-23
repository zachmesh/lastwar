---
title: Duel day loss - what makes a day's score count
created: 2026-11-22T19:13:00-08:00
modified: 2026-11-22T19:13:00-08:00
level: L0
version: 1.0.0
description: Why an Alliance Duel day can be lost whole - the six-day point table, the per-day scoring window, the winner-takes-the-day rule, and the one live observation that would falsify it
status: unverified
grounded_in:
  - source: lastwarhub.com Alliance Duel VS guide, page updated 2026-11-11, accessed 2026-11-22, URL in Sources
  - source: Packsify Alliance Duel guide for R5s, published 2026-07-07 and last checked 2026-10-31, accessed 2026-11-22, URL in Sources
  - source: lastwargame.online Alliance VS Duel guide, accessed 2026-11-22, URL in Sources
  - source: execution record _records_/2026-11-22/alliance-duel/1400-queue-run.md, live Match Record read 2026-11-22 about 13-57 to 14-00 PT
  - source: execution record _records_/2026-11-03/alliance-duel/1809-queue-run.md, live per-day reset read 2026-11-03 about 18-06 to 18-09 PT
  - source: knowledge _knowledge_/events-and-cycles/INDEX.md 1.3.0 and activity _activities_/alliance-duel/INDEX.md 1.44.0
---

# Duel day loss

## Question

Why can an Alliance Duel day be lost whole, and what does the game
actually require for a day's duel score to count?

Decision it would change: whether a duel day with no in-window read
is recorded as **lost whole** (a play and measurement failure to be
prevented) or as **unknown** (a measurement gap only), and whether a
closing read before the day boundary becomes a hard requirement of
the duel-score regular rather than one scheduling note among others.

No game input was sent and the game is stopped, so the claim could
not be tested live this turn.

## Sources

External, all accessed 2026-11-22:

1. lastwarhub.com, "Alliance Duel (VS) - Daily Themes & Score
   Strategy", page updated 2026-11-11.
   https://lastwarhub.com/en/events/alliance-duel/
2. Packsify, "Last War Alliance Duel Guide for R5s (2026)",
   published 2026-07-07, page last checked 2026-10-31.
   https://www.packsify.com/blogs/last-war-alliance-duel-event-strategy-guide
3. lastwargame.online, "Alliance VS Duel in Last War: Survival",
   accessed 2026-11-22.
   https://lastwargame.online/en/game-alliance-duel/

Repository, read live this turn (no edits):

4. `_records_/2026-11-22/alliance-duel/1400-queue-run.md` - Match
   Record panel read live 2026-11-22 about 13:57 to 14:00 PT by
   ticker-1352 in session cc-155.
5. `_records_/2026-11-03/alliance-duel/1809-queue-run.md` - duel day
   rollover and per-day total read live 2026-11-03 about 18:06 to
   18:09 PT.
6. `_knowledge_/events-and-cycles/INDEX.md` 1.3.0 (off-theme actions
   score zero, duel-day boundary 02:00 UTC) and
   `_activities_/alliance-duel/INDEX.md` 1.44.0 (the 3,600,000 daily
   total read, the about-18:00 rollover, the previous-day tab
   precedent).

Source count: 3 independent external, 2 repository execution records.

## Claim

**C1 - the week is six independent day results.** Days 1 to 6 award
1, 2, 2, 2, 2 and 4 win points - 13 in the week, 7 to win. Each
day's points go to the higher-scoring alliance; the day's loser gets
none of that day's points. Sources 1, 2 and 3 agree on the table.
Source 4 corroborates the 13-point scale from the game itself: the
Match Record pairs it shows each sum to exactly 13 (9 vs 4, 11 vs 2,
13 vs 0, 13 vs 0), the only interpretation under which every pair
sums to the weekly maximum.

**C2 - a score counts only inside its own day.** The action must be
one of that day's scoring actions and must land inside that day's
window - the 02:00Z server day, about 18:00 local in winter. Off-theme
or out-of-window actions score zero. Sources 1, 2 and 3 agree; source
6 states the same for this account's knowledge; source 5 measured the
rollover at about 18:00 local. Source 3 adds that the reset itself has
a 5 to 7 minute dead gap in which points may not count.

**C3 - day totals do not carry.** The game resets the personal daily
total at the rollover and keeps the closed day's figure readable but
frozen on the previous-day tab. Source 5 is the measurement: the
Tues. tab read the closed total 2,014,950 while the Wed. tab already
read 0 on the new day.

**C4 - therefore a day is lost whole, not partially.** Once the day's
window closes, an alliance that did not beat the opponent gets 0 for
that day, and no later day can add to it - the remaining days can only
add their own points against the same 13-point ceiling. This is an
arithmetic consequence of C1 and the reason a 4-point Day 6 loss is
the most expensive single day. It also compounds: if days 2 to 6 are
all lost, 12 of 13 points are gone and the week is unwinnable on the
table alone, whatever the opponent does.

**C5 - no per-day score minimum was found.** The only participation
gates any source states are event eligibility: HQ 10 or higher, an
alliance of at least 20 members, and top 32 alliances in the warzone.
That is source 2 only, so `unverified`. The repository's 3,600,000
daily target is a personal chest threshold (chest 8 in source 2's
table), not a win condition - the day is decided by the two alliance
totals, not by the personal target.

## Two source defects found

- **Repository label, not applied as an edit.** Source 4's prose calls
  the Match Record pairs "alliance day scores only". The arithmetic
  contradicts the label - all four pairs sum to 13, the weekly
  maximum - so the panel is showing week win-point totals, not per-day
  scores. The record is append-only and is not edited here; a
  correction note or issue is proposed to the coordinator.
- **External, not adopted.** Source 2 says an alliance can win Days 1
  to 5 and still lose to a Day 6 loss. That is false against the
  13-point table: 1+2+2+2+2 = 9, already past the 7-point win. Source
  1's arithmetic (seven by Thursday) is consistent and is the one
  used. The Packsify sentence is recorded here only so a later unit
  does not cite it.

## What this means for the 2026-11-21 day 6

The repository's "lost whole" (2026-11-21 retro, top leak 1) is an
operational claim, and it is the strong form: Enemy Buster ended 18:00
PT on 2026-11-21 with no duel-score unit executed, no alliance-duel
record, and no duel read since 2026-11-10. Under C1 to C4 that day is
lost to the loop whatever the game would have shown, because its
window is closed: no read and no scoring action can be taken in it
again.

What remains unverified is the game-side result. The repository has
no in-window alliance total for 2026-11-21, so it cannot say whether
the alliance beat or trailed its opponent that day, and the "five
consecutive days lost" series is an inference from missing reads, not
an observed score. If the alliance did in fact trail on each of days 2
to 6, the week was already unwinnable by C4; if it did not, the
repository has been understating its own week. Either way the
prevention lesson is the same - a day with no in-window read is
unrecoverable, and the record should say **loss** or **unknown**, not
silence.

## The one local observation that would falsify it

On a live duel day, the operator completes a radar task before the
02:00Z rollover and leaves it unclaimed, then claims it after the
rollover and reads the previous-day Ranking tab. If the closed day's
total increases, the window does not bind and a day can be backfilled
after all: C2 and C3 are false and the "whole loss" reading collapses
to a bookkeeping problem. If only the new day's total moves, the
mechanic stands. Only the operator may run this - this seat sends no
game input.

## Verdict

`supported` for C1 to C3 - three independent dated sources agree, and
two repository live reads corroborate the 13-point scale and the
per-day reset. `unverified` for the 2026-11-21 game-side outcome, for
C5, and for the no-backfill half of C3 and C4 until the test above
runs.

## Proposed play rule (for the coordinator, not applied)

**Close every duel day on the two alliance totals, not only the
personal total.** In the last duel-score unit before the 02:00Z
rollover, read the Today's Theme panel's two alliance totals (the
panel carries both - the 2026-11-01 2154 read showed 262,665,994
against 415,384,521) and close the day as win, loss or unknown from
them; if the in-window read is missed, the first post-rollover unit
reads the previous-day Ranking tab on the 2026-11-03 1809 precedent.
Verification: one week of duel days where every day closes with two
alliance totals and a verdict, and no day closes on silence.

## Follow-up

- Correction of the Match Record label in source 4 - coordinator to
  decide note or issue; this seat does not rewrite records.
- Falsification test - coordinator to assign to the operator on the
  next live duel day.
- No `_knowledge_` or `_activities_` edit proposed this turn; the
  knowledge articles already state the day boundary and the off-theme
  rule, and the play-rule change above belongs in the activity profile
  by the scribe if the owner accepts it.
