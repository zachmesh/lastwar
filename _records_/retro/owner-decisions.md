---
title: Owner decisions register
created: 2026-11-01T05:42:09Z
modified: 2026-11-07T05:05:00Z
version: 1.7.0
description: The standing register of items that only the owner can decide - each with its context, the exact decision needed, and its age - maintained by the daily retro and reported until decided
status: active
grounded_in:
  - source: owner instruction of 2026-10-31 - add or modify steps so every open item has a closed loop
  - source: improvements backlog in this folder - the companion register IMP-20261031-08
---

# Owner decisions register

Items the loop cannot close by itself, because the decision
belongs to the owner alone - a red-line exception, a one-off
in-game choice, anything consequential that the standing
rules deliberately leave unapproved. The register exists so
a pending decision ages in the open instead of sinking after
one mention in a summary.

## Entry fields

- id - OD-<YYYYMMDD>-<n>, assigned at filing, never reused.
- opened - the local date the item first needed a decision.
- item - the decision, in one line.
- context - the evidence, with record pointers.
- decision needed - the exact question put to the owner.
- age tracking - days since opened, recomputed by the retro
  at every run and reported with the item until it closes.
- status - open or decided (with the decision and its date
  recorded under the entry).

## Maintenance rules

- The daily retro maintains this register in the same run
  that maintains the improvements backlog - new
  skipped-needs-owner outcomes and new owner-gated items are
  filed here the day they occur.
- Every retro reports the open items with their ages in its
  delivery, however quiet the rest of the run is. An open
  item is never dropped from the report because it is old.
- When the owner decides, the retro records the decision
  and its date under the entry and marks it decided. The
  entry stays in this file as the decision's record.
- An item whose in-game window expires undecided is marked
  decided by expiry, with the expiry noted - it is never
  silently deleted.

## Open

### OD-20261031-01 - arms race phases with no scoring path inside the red lines

- opened: 2026-10-31
- item: whether Arms Race Base Building and Tech Research
  phases may ever use an exception means when no scoring
  path exists inside the standing red lines.
- context: these phases repeatedly close as
  skipped-needs-owner with a tier-3 gap of 30,000 and every
  scoring path inside a red line. On 2026-10-31 alone, three
  units closed this way - Tech Research at 02:11 (research
  queues idle, no completion landing in the window) and Base
  Building at 06:15 and 18:44 (building queue holding only
  long upgrades). Records -
  _records_/2026-10-31/arms-race/0211-queue-run.md,
  0615-queue-run.md and 1844-queue-run.md. Earlier instances
  of the same pattern are in the miss audit of 2026-10-31,
  root cause class g.
- decision needed: give a standing exception rule for these
  phases (and its limits), or keep deciding case by case -
  in which case each occurrence keeps filing here until
  answered.
- age tracking: opened 2026-10-31, age 0 days at filing;
  the retro recomputes and reports the age every run.
  2026-11-01 retro: age 1 day. Recurrence noted -
  Nov 1 adds a Base Building skipped-needs-owner
  (1803 unit, building timers 11d and 2d, tier-3 gap
  30,000) and a Tech Research partial at 0 of 30,000
  (1403 unit, no research completing in window).
  No owner decision appeared for this item in the
  records, chat or Slack DM since it opened.
  2026-11-02 retro: age 2 days. No new
  skipped-needs-owner on Nov 2 - arms units closed
  partial, not skipped (1803 unit, Unit Progression,
  score 9,300, tier-3 gap 65,700, training queues
  named as the only legal path). The gap persists in
  partial form. No owner decision appeared for this
  item in the records, chat or Slack DM.
  2026-11-03 retro: age 3 days, now over the 48-hour
  naming line. No new skipped-needs-owner on Nov 3 -
  arms units closed done (Hero Advancement tier-3,
  Base Building 50,800 over 30,000) or partial
  (Drone Boost tier-3 gap 20,000). The gap persists
  in partial form for Drone Boost but narrows for
  Base Building. No owner decision appeared for this
  item in the records, chat or Slack DM.
- status: open

### OD-20261031-02 - Halloween Day 07 decoration choice

- opened: 2026-10-31
- item: the Halloween Check-In Day 07 reward is a Decoration
  Choice Chest VI (UR) x2; only the preview has been seen
  and no decoration has been chosen.
- context: Days 01-06 are claimed. Across the 2026-10-31
  events sweeps the Day 07 tile opened only a preview with
  no Claim button, and no decoration was chosen - records
  in _records_/2026-10-31/INDEX.md and
  _records_/2026-10-31/event-claims/0812-queue-run.md,
  1244-queue-run.md and 1745-queue-run.md.
- decision needed: whether a decoration should be chosen at
  all, and if so which one - or whether the item should be
  left unclaimed.
- age tracking: opened 2026-10-31, age 0 days at filing;
  the retro recomputes and reports the age every run. Note
  the item is event-bound and can expire undecided.
  2026-11-01 retro: age 1 day. Unaddressed on Nov 1 -
  no Nov 1 events record mentions the Day 07 tile or a
  decoration choice. If the event window passes
  undecided, this item is marked decided by expiry
  per the maintenance rules, never silently deleted.
  2026-11-02 retro: age 2 days. Unaddressed a second
  day - no Nov 2 events record mentions the Day 07
  tile or a decoration choice, and the Nov 2 events
  hub reads contain no Halloween surface. The window
  is treated as possibly passed, but the item is NOT
  marked decided by expiry: no record states the
  Halloween event ended. It crosses the 48-hour
  naming line at the next retro if still undecided.
  2026-11-03 retro: age 3 days, now over the 48-hour
  naming line. Unaddressed a third day - no Nov 3
  events record mentions the Day 07 tile or a
  decoration choice, and the Nov 3 events hub reads
  contain no Halloween surface. Still NOT marked
  decided by expiry: no record states the Halloween
  event ended.
- status: open


### OD-20261031-03 - whether to keep, change or pause the survivor method

- opened: 2026-10-31
- item: whether the survivor intake method should be
  kept running as-is, changed, or paused pending a
  method change.
- context: the Oct 31 retro named this decision (its
  action M5, 22 consecutive partials meeting the
  fourth-identical-partial threshold) but never
  registered it; this entry files it. The question
  has narrowed since: Nov 1 produced the first
  verified survivors done of the queue era (1403
  unit, record _records_/2026-11-01/survivor-intake/1644-queue-run.md,
  gate line clear, target 1 over achieved 1),
  folded as survivor-intake 1.9.0 (streak broken
  at 25) - but Quick Dispatch has still never run
  (no recruit card in the done unit), and the
  other Nov 1 survivors units closed partial or
  failed with the gate line explicitly not
  verified. Intake is no longer 0-done; the
  method as a whole is still unproven.
- decision needed: keep the current method
  running, change it, or pause the type pending a
  method change - with Quick Dispatch unproven
  either way.
- age tracking: opened 2026-10-31 (first needed
  by the Oct 31 retro), age 1 day at the
  2026-11-01 retro; recompute on each retro run.
  2026-11-02 retro: age 2 days. Nov 2 survivors units
  (5 partial) keep the close discipline (gate line
  explicitly not verified, never presumed); Quick
  Dispatch still never ran. The decision (keep,
  change, or pause the method) is unchanged.
  2026-11-03 retro: age 3 days, now over the 48-hour
  naming line. Nov 3 survivors units (4 partial)
  keep the close discipline (gate line explicitly
  not verified, never presumed); Quick Dispatch
  still never ran; consecutive non-done run since
  the Nov 1 done is now 12 partials. The decision
  is unchanged.
- status: open

### OD-20261101-01 - whether to add a Season 2 event calendar

- opened: 2026-11-01
- item: whether the old unconfirmed event-calendar proposal should become scoped work.
- context: the legacy idea combined a Season 2 topic page with an event calendar. `_knowledge_/season-two-winter/` already supplies the topic page; a live event calendar is not established by that article. The task intake workflow migration table preserves the proposal's source.
- decision needed: whether an account-relevant event calendar is wanted, and its scope and freshness expectations if approved. This migration does not approve it or claim the present season was rechecked.
- age tracking: opened 2026-11-01, age 0 days at filing; recompute on each retro run.
  2026-11-02 retro: age 1 day, unaddressed.
  2026-11-03 retro: age 2 days, unaddressed.
- status: open

### OD-20261101-02 - whether to extend end-of-event results recording

- opened: 2026-11-01
- item: whether every VS and alliance event should gain a dedicated end-of-event results record beyond existing execution records and duel-total reads.
- context: this was an unconfirmed idea in the retired task list. Existing `_activities_/alliance-duel/` already requires the personal daily total and dated results; that does not approve a new reporting scope for every event. The migration table retains the distinction.
- decision needed: whether the broader reporting is wanted, which events it covers, and the minimum result fields. Leave it unapproved until the owner decides; continue existing recording duties.
- age tracking: opened 2026-11-01, age 0 days at filing; recompute on each retro run.
  2026-11-02 retro: age 1 day, unaddressed.
  2026-11-03 retro: age 2 days, unaddressed.
- status: open

### OD-20261101-03 - whether to do the Season Photo alliance-facing actions

- opened: 2026-11-01
- item: whether to edit and save the alliance group
  photo once and post once in the alliance message
  board, and if so which photo edit and what message.
- context: discovered 2026-11-01 about 22:19 local by
  ticker unit passes-2026-11-01-1857 (record
  _records_/2026-11-01/shop-claims/2220-queue-run.md),
  filed as GitHub issue #154 after the 2026-11-01
  retro. Season hub (Season II) Season Photo page,
  Rewards panel: two tasks, both Not Achieved, Claim
  All greyed - edit and save your group photo 1 time
  (100 red diamonds); post 1 message in the alliance
  message board (100 red diamonds). Achieving either
  is an alliance-facing action, which under the
  recording rules needs owner approval before it
  happens, so the ticker did not do them. Until
  decided, the 200 red diamonds stay unclaimed and
  the Season Photo red badge is explained, not a
  missed shop claim.
- decision needed: do these two actions, and if so
  which photo edit and what message - or leave the
  rewards unclaimed.
- age tracking: opened 2026-11-01, age 1 day at the
  2026-11-02 retro; recompute on each retro run.
  2026-11-03 retro: age 2 days. The pr-catchall runs
  through Nov 3 keep noting issue #154 as awaiting
  the Season Photo decision (about 33 hours old at
  the 07:39 run); the 200 red diamonds stay
  unclaimed. No owner decision appeared.
- status: open

### OD-20261105-01 - records batch checker due: merge-aware or window-membership only

- opened: 2026-11-05
- item: whether the records-batch checker `due` should
  become merge-aware, or the integrator job body
  should be amended so window membership alone
  governs batch passes.
- context: on 2026-11-05 the 1500 batch window saw
  two merges - PR #310 at 15:12 and PR #330 at
  15:52. The checker `due` is clock-only by design
  (window [point, point+60min)), so it reported due
  for the 1545 pass; the integrator job body step 2
  NOTE says a pass inside a batch window where a
  batch merge already happened is NOT a batch pass
  (only the first pass at or after a batch point
  merges), while the checker-gate paragraph says the
  checker verdict is the mechanical definition. Two
  consecutive passes resolved the same situation
  differently. Filed as GitHub issue #335 (labels
  tooling, records, owner-decision); the
  pr-catchall triage classified the choice itself
  as owner-gated. Impact of the instance: none on
  data (PR #330 was verified clean, merged by
  merge commit, 12 commits, branch kept).
  Branch (a) is implemented as PR #337
  (records_batch.py 1.1.0, due gains optional
  --merges) and awaits integrator review; the tool
  alone changes no pass behaviour until the
  integrator job body adopts due --merges.
- decision needed: either make due merge-aware
  (consult the last records-merge time) so a second
  pass in a window reports not due, or amend the
  body so window membership alone governs and the
  first-pass NOTE is removed.
- age tracking: opened 2026-11-05, age 0 days at
  filing; the retro recomputes and reports the age
  every run. Interim rule until decided: integrator
  passes apply the already-merged check on top of
  the checker, as the 1530 pass did.
- status: open

## 2026-11-04 retro notes (all items, ages recomputed)

- OD-20261031-01: age 4 days. No new skipped-needs-owner on Nov 4 (arms units closed partial or capture-failed); gap persists in partial form (Tech Research and Base Building tier-3 unreachable inside red lines, Unit Progression tier-3 gap 75,000). No owner decision appeared in the records, chat or Slack DM.
- OD-20261031-02: age 4 days, event-bound. Unaddressed a fourth day: no Nov 4 events record mentions the Day 07 tile or a decoration choice, and the Nov 4 events hub reads contain no Halloween surface. Still NOT marked decided by expiry: no record states the Halloween event ended.
- OD-20261031-03: age 4 days. Nov 4 survivors units (4 partial, 1 capture-failed) keep the close discipline, Quick Dispatch still never ran, with one live gate-line verification (3 waiting, 0 recruited, unit cap reached). Decision unchanged.
- OD-20261101-01: age 3 days, unaddressed.
- OD-20261101-02: age 3 days, unaddressed.
- OD-20261101-03: age 3 days. The pr-catchall 1939 run keeps noting issue 154 as awaiting the Season Photo decision; the 200 red diamonds stay unclaimed.
- No new owner-decision item from the Nov 4 window: no skipped-needs-owner outcome on Nov 4 in the live pool, and no owner-gated PR escalated by the integrator. All six items are open longer than 48 hours and are named in the Nov 4 retro chat report and Slack sync until decided.

## 2026-11-05 retro notes (all items, ages recomputed)

- OD-20261031-01: age 5 days. No new skipped-needs-owner on Nov 5 (no arms unit executed); the gap persists in partial form from Nov 4 (Tech Research and Base Building tier-3 unreachable inside red lines, Unit Progression tier-3 gap 75,000). No owner decision appeared in the records, chat or Slack DM.
- OD-20261031-02: age 5 days, event-bound. Unaddressed a fifth day: no Nov 5 events record mentions the Day 07 tile or a decoration choice, and no Nov 5 events unit executed at all. Still NOT marked decided by expiry: no record states the Halloween event ended.
- OD-20261031-03: age 5 days. Nov 5 survivors units (3 expired, 3 failed) keep the close discipline, Quick Dispatch still never ran; consecutive non-done run now 23. Decision unchanged.
- OD-20261101-01: age 4 days, unaddressed.
- OD-20261101-02: age 4 days, unaddressed.
- OD-20261101-03: age 4 days. The pr-catchall runs keep noting issue #154 as awaiting the Season Photo decision; the 200 red diamonds stay unclaimed.
- OD-20261105-01: age 0 days at filing (issue #335, records batch checker due). PR #337 implements branch (a); the owner choice between (a) and (b) is still owed.
- No other new owner-decision item from the Nov 5 window: no skipped-needs-owner outcome on Nov 5 in either pool, and no owner-gated PR escalated by the integrator. All six older items are open longer than 48 hours and are named in the Nov 5 retro chat report and Slack sync until decided.

## Decided

None yet.

## 2026-11-06 retro notes (all items, ages recomputed)

- OD-20261031-01: age 6 days. No new skipped-needs-owner on Nov 6 (no arms unit executed); the gap persists in partial form from Nov 4 (Tech Research and Base Building tier-3 unreachable inside red lines, Unit Progression tier-3 gap 75,000). No owner decision appeared in the records, chat or Slack DM.
- OD-20261031-02: age 6 days, event-bound. Unaddressed a sixth day: no Nov 6 events record mentions the Day 07 tile or a decoration choice, and no Nov 6 events unit executed at all. Still NOT marked decided by expiry: no record states the Halloween event ended.
- OD-20261031-03: age 6 days. Nov 6 survivors units (5 expired, 2 failed) keep the close discipline, Quick Dispatch still never ran; consecutive non-done run now 30. Decision unchanged.
- OD-20261101-01: age 5 days, unaddressed.
- OD-20261101-02: age 5 days, unaddressed.
- OD-20261101-03: age 5 days. The pr-catchall runs keep noting issue #154 as awaiting the Season Photo decision; the 200 red diamonds stay unclaimed.
- OD-20261105-01: age 1 day. The 1940 planner run re-verified the comment count (3, unchanged); PR #337 implements branch (a), awaiting integrator review and adoption; the owner choice between (a) and (b) is still owed.
- No other new owner-decision item from the Nov 6 window: no skipped-needs-owner outcome on Nov 6 in either pool, and no owner-gated PR escalated by the integrator. All six older items are open longer than 48 hours and are named in the Nov 6 retro chat report and Slack sync until decided.
