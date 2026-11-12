---
title: Owner decisions register
created: 2026-11-01T05:42:09Z
modified: 2026-11-12T05:00:00Z
version: 2.2.0
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

### OD-20261108-01 - PR 425 log-gate policy amendment

- opened: 2026-11-08
- item: whether the log-append-delivery-gate
  policy amendment (PR #425) should be approved
  as a mandatory gate, merged as-is once rebased,
  or split into a tool change and a separate
  policy change.
- context: PR #425 amends the log-gate policy
  (tooling, records). The integrator escalated it
  to the owner on 2026-11-07 22:45 local as
  owner-gated, and re-verified it on Nov 8 with
  no owner decision since. The retro's own
  action-log line in this delivery rides the
  records branch under the current (pre-amendment)
  policy.
- decision needed: approve the mandatory log
  gate, merge PR #425 as-is once rebased, or
  split it into a tool change and a separate
  policy change.
- age tracking: opened 2026-11-08, age 0 days at
  filing; the retro recomputes and reports the age
  every run.
- status: open

### OD-20261108-02 - live-checkout re-sync mechanism for _tools_ drift

- opened: 2026-11-08
- item: whether the live-checkout re-sync
  mechanism (#415) should be wired as a drift
  check into the ticker/planner pre-step, or kept
  as the documented manual procedure.
- context: the tool-developer 1832 run on Nov 8
  surfaced the drift (live tools/queue.py older
  than main's) and did the manual re-sync to
  main 9479c3eb at about 18:42 (19 files match,
  IN SYNC). The next _tools_ merge will go stale
  the same way until the mechanism is decided.
  Filed as GitHub issue #415 (labels tooling,
  owner-decision).
- decision needed: wire the drift check into the
  ticker/planner pre-step, or keep the documented
  manual procedure.
- age tracking: opened 2026-11-08, age 0 days at
  filing; the retro recomputes and reports the age
  every run.
- status: open


### OD-20261109-01 - Transfer Surge warzone transfer

- opened: 2026-11-09
- item: whether Bears Lair should stay in Warzone
  #2110 or apply to transfer to another warzone
  during Application Day (ends 2026-11-12 18:00
  UTC), and if so to which warzone.
- context: discovered 2026-11-09 by scout
  exploration unit scout-scout-discovery-2026-11-09-004
  (executor ticker-0804), record
  _records_/2026-11-09/season-ii-countdown-6d/0812-queue-run.md.
  The Season II countdown opens TRANSFER SURGE, the
  cross-warzone transfer event. Application Day runs
  11/8 18:00:00 to 11/12 18:00:00 UTC, then Transfer
  Day to 11/13 and Display Stage to 11/15. Transfer
  Warzone Group (32) includes our #2110. Applying
  would move Bears Lair out of Warzone #2110 (and out
  of the AP3x alliance) into a chosen warzone,
  subject to mutual approval. The full carry-over
  rules were read live into the record. No Apply was
  tapped. Filed as GitHub issue #514 (labels
  owner-decision).
- decision needed: stay in #2110, or apply to
  transfer - and if so to which warzone - before
  2026-11-12 18:00 UTC.
- age tracking: opened 2026-11-09, age 0 days at
  filing; the retro recomputes and reports the age
  every run. The item is window-bound: it expires
  undecided at 2026-11-12 18:00 UTC.
- status: open

### OD-20261109-02 - start Builders Hut Lv.25 to Lv.26 upgrade

- opened: 2026-11-09
- item: whether to start the Builders Hut Lv.25 to
  Lv.26 upgrade (15-day build, measured
  2026-11-09).
- context: measured live 2026-11-09 about 08:48 PT
  by scout exploration unit
  scout-scout-discovery-2026-11-09-009 (ticker-0842),
  record _records_/2026-11-09/upgrade-builders-hut-to/0848-queue-run.md.
  Builder's Hut Lv.25 to 26: power 90,800 to 108,300;
  Free Construction Speed-up Time 00:20:00 to
  00:22:00; Hero EXP 22.0M shown on the panel. Cost,
  all prerequisites met (green checks): Lv.26
  Headquarters, Iron 170.0M (have 866.8M), Food 56.9M
  (have 542.1M). Original time 15d 08:05:18; the
  Upgrade button shows 7d 07:16:49 (effective time
  after bonuses, as displayed). Finish Now would
  cost 18,188 diamonds - never tapped, red line.
  Building queue 1/4 at the time (Lv.29 Aircraft
  Center in progress), so a free builder slot exists.
  Starting a building is owner-only by red line, and
  the 15-day build is the longest commitment measured
  so far. Filed as GitHub issue #517 (labels
  owner-decision).
- decision needed: start the Lv.26 upgrade, or leave
  the Builders Hut at Lv.25.
- age tracking: opened 2026-11-09, age 0 days at
  filing; the retro recomputes and reports the age
  every run.
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

## 2026-11-07 retro notes (all items, ages recomputed)

- OD-20261031-01: age 7 days. NEW skipped-needs-owner on Nov 7 (arms-race 1403, Base Building, tier-3 gap 30,000, no path inside red lines - record _records_/2026-11-07/arms-race/1633-queue-run.md); the Drone Boost phase read at 19:23 is a first-unit-in-phase read under R4, not a skip. No owner decision appeared in the records, chat or Slack DM.
- OD-20261031-02: age 7 days, event-bound. Unaddressed a seventh day: no Nov 7 events record mentions the Day 07 tile or a decoration choice, and no Nov 7 events unit executed at all. Still NOT marked decided by expiry: no record states the Halloween event ended.
- OD-20261031-03: age 7 days. Nov 7 survivors units (4 expired, 2 partial) keep the close discipline, Quick Dispatch still never ran; consecutive non-done run now 36 - but the 1803 unit verified and cleared a 4-figure gate line (target 4 of 4, identities unread). Decision unchanged.
- OD-20261101-01: age 6 days, unaddressed.
- OD-20261101-02: age 6 days, unaddressed.
- OD-20261101-03: age 6 days. The pr-catchall runs keep noting issue #154 as awaiting the Season Photo decision; the 200 red diamonds stay unclaimed.
- OD-20261105-01: age 2 days. New evidence: the 2300 window Nov 6 saw two records merges (PR 374 at 23:02 and PR 379 at 23:49), the second named a cadence miss by the integrator's own 2345 run; the tool's window-membership audit reports 0 violations, so the audit cannot see a second-merge-in-window. PR #337 implements branch (a), awaiting integrator review and adoption; the owner choice between (a) and (b) is still owed.
- No other new owner-decision item from the Nov 7 window: no new skipped-needs-owner type on Nov 7 (the arms skip is the same OD-20261031-01 pattern), and no owner-gated PR escalated by the integrator. All seven items are open longer than 48 hours and are named in the Nov 7 retro chat report and Slack sync until decided.

## 2026-11-08 retro notes (all items, ages recomputed)

- OD-20261031-01: age 8 days. NEW skipped-needs-owner on Nov 8 (arms-race 2127, Unit Progression, tier-3 gap 75,000, no idle barracks, phase ends about 14:00 - record _records_/2026-11-08/arms-race/1342-queue-run.md); the 1003 unit read the phase first under R4 and enqueued the successor per R6. The Tech Research phase read by the scout at 17:03 (score 0, timer 01:03:01, ends about 18:06) was never worked: its 1803 unit sat in inbox and its window passed. No owner decision appeared in the records, chat or Slack DM.
- OD-20261031-02: age 8 days, event-bound. Unaddressed an eighth day: no Nov 8 events record mentions the Day 07 tile or a decoration choice, and the Nov 8 events hub reads contain no Halloween surface. Still NOT marked decided by expiry: no record states the Halloween event ended.
- OD-20261031-03: age 8 days. Nov 8 survivors units (4 expired, 2 partial) recruited 5 named survivors with identities read live (JAVIER Lawyer, JAVIER Builder, ELINA Instructor, CHLOE Keeper, MICHAEL Hospital), gate line verified live; the 6th card (JAVIER Barn Keeper) stayed open unrecruited, and Quick Dispatch still never ran; consecutive non-done run now 41. Decision unchanged.
- OD-20261101-01: age 7 days, unaddressed.
- OD-20261101-02: age 7 days, unaddressed.
- OD-20261101-03: age 7 days. The pr-catchall runs keep noting issue #154 as awaiting the Season Photo decision; the 200 red diamonds stay unclaimed.
- OD-20261105-01: age 3 days. New evidence: the 1100 window Nov 8 had 3 merges (PR 449 at 11:20, PR 430 at 11:28, PR 458 at 11:38); PR 458 was named a cadence miss by the integrator's own 1130 run; the tool now flags both violations (records_batch 1.2.0, PR #420 merged Nov 7 21:48). PR #337 implements branch (a), awaiting integrator review and adoption; the owner choice between (a) and (b) is still owed.
- OD-20261108-01: age 0 days at filing (PR #425 log-gate policy amendment, owner-gated, escalated 2026-11-07 2245, still undecided Nov 8).
- OD-20261108-02: age 0 days at filing (#415 live-checkout re-sync mechanism, surfaced by the tool-developer 1832 run; manual re-sync done Nov 8 18:42).
- Two new owner-decision items from the Nov 8 window (OD-20261108-01, OD-20261108-02). All nine items are open; the seven carried items are open longer than 48 hours and are named in the Nov 8 retro chat report and Slack sync until decided.

## 2026-11-09 retro notes (all items, ages recomputed)

- OD-20261031-01: age 9 days. No new skipped-needs-owner on Nov 9 (Nov 9 day skipped 0 in either pool); the arms-race 1803 unit closed partial (Unit Progression, score 0, timer 02:42:34, tier-3 gap 75,000 via training queues only). The gap persists in partial form, now in a fourth phase shape. No owner decision appeared in the records, chat or Slack DM.
- OD-20261031-02: age 9 days, event-bound. Unaddressed a ninth day: no Nov 9 events record mentions the Day 07 tile or a decoration choice, and the Nov 9 events hub reads contain no Halloween surface. Still NOT marked decided by expiry: no record states the Halloween event ended.
- OD-20261031-03: age 9 days. Nov 9 survivors 0203 done (gate line verified clear, 0 recruits) - the 41-run non-done streak is broken; Quick Dispatch still never ran. Decision unchanged.
- OD-20261101-01: age 8 days, unaddressed.
- OD-20261101-02: age 8 days, unaddressed.
- OD-20261101-03: age 8 days. No Nov 9 record mentions the Season Photo actions; the 200 red diamonds stay unclaimed. No owner decision appeared.
- OD-20261105-01: age 4 days. New evidence: 0 batch violations out of 6 merges today, so the process half had no new instance to catch; PR #337 still implements branch (a), awaiting integrator review and adoption; the owner choice between (a) and (b) is still owed.
- OD-20261108-01: age 1 day. PR #425 still open, still awaiting owner decision (integrator's 19:40 Slack note names it).
- OD-20261108-02: age 1 day. No new drift evidence today; Issue #415 still open.
- OD-20261109-01: age 0 days at filing (Issue #514, Transfer Surge; decision needed before 2026-11-12 18:00 UTC).
- OD-20261109-02: age 0 days at filing (Issue #517, Builders Hut Lv.26 upgrade).
- Two new owner-decision items from the Nov 9 window (OD-20261109-01, OD-20261109-02). All eleven items are open; the nine carried items are open longer than 48 hours and are named in the Nov 9 retro chat report and Slack sync until decided.

## 2026-11-10 retro notes (all items, ages recomputed)

- OD-20261031-01: age 10 days. TWO new skipped-needs-owner on Nov 10, both the standing pattern: arms-race 0203 (ticker-0334, record 0342, Base Building, score 0 of 30,000, only free path Oil Well in progress) and arms-race 2203 (ticker-0004, record 0006, Tech Research, score 0 of 30,000, only research completes in 1d 10h). The building-identity question inside the first skip (#595: Oil Well vs Lv.29 Aircraft Center) is unresolved. No owner decision appeared in the records, chat or Slack DM.
- OD-20261031-02: age 10 days, event-bound. Unaddressed a tenth day: no Nov 10 events record mentions the Day 07 tile or a decoration choice, and the Nov 10 events hub reads contain no Halloween surface. Still NOT marked decided by expiry: no record states the Halloween event ended.
- OD-20261031-03: age 10 days. Nov 10 survivors 4 partial, 0 done; gate line not verified; Quick Dispatch still never ran. Decision unchanged.
- OD-20261101-01: age 9 days, unaddressed.
- OD-20261101-02: age 9 days, unaddressed.
- OD-20261101-03: age 9 days. No Nov 10 record mentions the Season Photo actions; the 200 red diamonds stay unclaimed. No owner decision appeared.
- OD-20261105-01: age 5 days. New evidence: 1 batch violation out of 6 merges today (PR 556 merged 22:59:55, 5 seconds before the 2300 window), so the process half now has a caught instance; the 5-second margin raises the grace question for #418. PR #337 still implements branch (a), awaiting integrator review and adoption; the owner choice between (a) and (b) is still owed.
- OD-20261108-01: age 2 days. PR #425 still open, still awaiting owner decision.
- OD-20261108-02: age 2 days. New drift evidence: the records/2026-11-10 branch pool's _tools_ is 1.5.2 while main's is 1.5.3 (PR #587), so the branch's own tool under-measures attainment; Issue #415 still open.
- OD-20261109-01: age 1 day. Transfer Surge decision still needed before 2026-11-12 18:00 UTC; Issue #514 still open.
- OD-20261109-02: age 1 day. Builders Hut Lv.26 upgrade decision still needed; Issue #517 still open.
- No new owner-decision items from the Nov 10 window (the two arms skips are the OD-20261031-01 pattern; no owner-gated PR was escalated; the Survey Center survey stays on #506, not a register item). All eleven items are open; the nine carried items are open longer than 48 hours and are named in the Nov 10 retro chat report and Slack sync until decided.

## 2026-11-11 retro notes (all items, ages recomputed)

- OD-20261031-01: age 11 days. ONE new skipped-needs-owner on Nov 11 (arms-race-2026-11-11-0203, Tech Research, score 0 of 30,000, no in-scope path - record _records_/2026-11-11/arms-race/0535-queue-run.md); the 0112 unit read Base Building at 21,600 of 30,000 (tier 3 missed by 8,400, only the Lv.29 Aircraft Center upgrade in the queue). No owner decision appeared in the records, chat or Slack DM.
- OD-20261031-02: age 11 days, event-bound. Unaddressed an eleventh day: no Nov 11 events unit executed at all, and no Nov 11 events record mentions the Day 07 tile or a decoration choice. Still NOT marked decided by expiry: no record states the Halloween event ended.
- OD-20261031-03: age 11 days. Nov 11 survivors 0603 processed 1 gate survivor; the 1003 unit hit the new Zoom-to-Fit window failure and never reached the gate; Quick Dispatch still never ran. Decision unchanged.
- OD-20261101-01: age 10 days, unaddressed.
- OD-20261101-02: age 10 days, unaddressed.
- OD-20261101-03: age 10 days. No Nov 11 record mentions the Season Photo actions; the 200 red diamonds stay unclaimed. No owner decision appeared.
- OD-20261105-01: age 6 days. New evidence: 1 batch violation out of 7 merges today (PR 636 merged 11:07:03, second records merge in the 11:00 window after PR 615 at 11:06:27 - a Nov 10 straggler branch merging in Nov 11's window). PR #337 still implements branch (a), awaiting integrator review and adoption; the owner choice between (a) and (b) is still owed.
- OD-20261108-01: age 3 days. PR #425 still open, still awaiting owner decision (integrator's 2030 run re-verified it CLEAN against main decf48bb59, no repeat comment).
- OD-20261108-02: age 3 days. No new drift evidence today; the branch tool is 1.5.4, matching main, so the drift that motivated this item is resolved at the tool level - the mechanism decision (wire the drift check in, or keep the manual procedure) is still owed. Issue #415 still open.
- OD-20261109-01: age 2 days. Transfer Surge decision still needed before 2026-11-12 18:00 UTC (about 10:00 PST Nov 12); Issue #514 still open. The item expires undecided tomorrow morning unless the owner decides.
- OD-20261109-02: age 2 days. Builders Hut Lv.26 upgrade decision still needed; Issue #517 still open.
- No new owner-decision items from the Nov 11 window (the arms skip is the OD-20261031-01 pattern; no owner-gated PR was escalated; the Survey Center survey stays on #506, not a register item). All eleven items are open; the ten carried items are open longer than 48 hours and are named in the Nov 11 retro chat report and Slack sync until decided.
