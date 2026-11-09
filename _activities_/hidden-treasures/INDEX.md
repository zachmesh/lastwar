---
title: Hidden Treasures
created: 2026-10-26T04:00:00Z
modified: 2026-11-09T13:32:17Z
level: L1
version: 1.14.0
description: Treasure map fragment collection, ally exchange and digging, one activity folder for hidden treasure knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner direction to register each learned task type as metadata, 2026-10-25
  - source: hidden-treasures execution record 2026-11-01 0150 PST
  - source: perception-scout execution record 2026-11-01 0215 PST, cross-check read
  - source: hidden-treasures execution record 2026-11-01 1420 PST
  - source: ticker-0204 hidden-treasures execution record 2026-11-02 0207 queue run
  - source: ticker-0404 hidden-treasures execution record 2026-11-02 0424 queue run (done, checked only)
  - source: ticker-1004 hidden-treasures execution record 2026-11-02 1009 queue run (done, checked only)
  - source: ticker-1336 hidden-treasures execution record 2026-11-02 1352 queue run (done, checked only)
  - source: ticker-2134 hidden-treasures execution record 2026-11-02 2135 queue run
  - source: ticker-0004 hidden-treasures execution record 2026-11-03 0014 queue run (done, checked only, M3 at zero)
  - source: ticker-0334 hidden-treasures execution record 2026-11-03 0349 queue run (done, checked only, counts identical to 0014, M3 at zero)
  - source: ticker-0834 hidden-treasures execution record 2026-11-03 0838 queue run (done, checked only, counts identical to 0349, M3 at zero)
  - source: ticker-1234 hidden-treasures execution record 2026-11-03 1243 queue run (done, checked only, counts identical to 0838, M3 at zero, leftover Gold Mine panel entry)
  - source: ticker-0834 hidden-treasures execution record 2026-11-04 0847 queue run (done, checked only, fragment counts identical to 0838/1243, M3 still binding)
  - source: ticker-1434 hidden-treasures execution record 2026-11-08 1459 queue run (done, one dig executed, fragments M1-M7 each down 1, chest progress 6/15 to 7/15, tab badge 1 while stock allowed 3 digs - badge-equals-digs rule disproved); record commit dfd3c87f9 on records/2026-11-08
  - source: ticker-2235 hidden-treasures execution record 2026-11-08 2255 queue run (done, one dig executed, fragments M1-M7 each down 1, chest progress 7/15 to 8/15, 2 digs remain capped by M3, tab badge 1 re-confirmed not the dig count; record commit 0c9686b4f on records/2026-11-08)
  - source: ticker-0504 hidden-treasures execution record 2026-11-09 0525 queue run (done, 1 dig executed, fragments M1-M7 each down 1, chest progress 9/15 to 10/15, M3 binding at x1, tab badge 1 with exactly 1 dig possible; record commit be01e91134 on records/2026-11-09)
---

# Hidden treasures

## What this activity is

The treasure digging system inside the Secret Command Post. Completing
secret missions earns Treasure Map Shards; collecting all seven kinds
digs one treasure. This folder accumulates fragment, exchange and dig
knowledge. Executions are recorded in
`_records_/<date>/hidden-treasures/`, one file per execution. The post
itself and its dispatches belong to
[`secret-missions`](../secret-missions/INDEX.md).

## How to enter

- Open the Secret Command Post (see the entry notes in
  secret-missions) and tap the Hidden Treasures tab. The tab carries a
  red count badge - the badge showed 1 on first entry on 2026-10-25.
  CORRECTED 2026-11-08 1459: the badge is NOT the number of digs
  currently possible - on 2026-11-08 it read 1 while the fragment
  stock (M3 and M5 at 3) allowed 3 digs. The dig count is capped by
  the scarcest fragment stock, not by the badge; what the badge counts
  is unconfirmed (see Open questions).

## How it is done

- The info panel states the rules - one, complete secret missions to
  earn Treasure Map Shards; two, shards can be exchanged with allies;
  three, collect all 7 kinds of fragments to dig once; four, a dig
  can win a Golden Mobile Squad Decoration.
- A dig consumes one each of fragments M1 through M7. The scarcest
  fragment caps the dig count - on 2026-10-25 the stock was M1 14,
  M2 13, M3 4, M4 4, M5 1, M6 6, M7 8, so M5 limited the account to
  the 1 dig the stock allowed (the badge happened to read 1 then; the
  badge is not the dig count - see the 2026-11-08 correction above).
- Dig odds shown in game - Chest UR 10 percent, SSR 30 percent, SR
  60 percent, and an opened chest pays 10 rewards.
- Tick Skip Animation, then tap Dig 1 time.
- A chest progress track sits at the right of the screen - it read
  9 of 15 before the dig and 10 of 15 after on 2026-10-25, and it
  read 1 of 15 on 2026-11-01. The track appears reset since
  2026-10-25 - noted, not assumed, as the record words it; whether
  it reset, restarted, or counts a new track is unconfirmed.

## Cadence

- Dig whenever a full set of seven fragments is on hand, which the
  scarcest fragment stock counts - NOT the tab badge (CORRECTED
  2026-11-08 1459: the badge read 1 while stock allowed 3 digs).
  Fragment income is a by-product of the secret missions cadence.

## Scope and availability

- Permanent system tied to the Secret Command Post, no season gating
  observed.
- Exchange - the Exchange Items view has Your Exchange and Allies
  Exchange. One completed own history was visible (gained M5, lost
  M6, partner Mistress Sam). One open ally offer was visible
  (receive M4 with 3 owned, send M3 with 3 owned, from
  another commander). Trading fragments away is an exchange of
  account assets - it was inspected only on 2026-10-25, not executed.

## What is known from 2026-10-25

- One dig executed with Skip Animation on. Rewards - chests times 4,
  coin piles times 6, 1 minute speedups times 50, 50 and 100, blue
  triangles times 400 and silver ingots times 200, with a few item
  names not fully read. The chest tier won was not displayed.
- After the dig - M1 13, M2 12, M3 3, M4 3, M5 0, M6 5, M7 7; chest
  progress 10 of 15; the red badge cleared and the Dig button greyed
  out, as expected with no complete set left.

## What is known from 2026-11-01

Measured in the 0150 unit (ticker-0136, unit
treasures-2026-10-31-2257, status done, checked, nothing to dig),
entered from the Secret Command Post already open from the secrets
unit of the same pass, Hidden Treasures tab tapped, screen verified
as Hidden Treasure.

- Fragment counts read live on the map - M1 x13, M2 x11, M3 x0,
  M4 x9, M5 x0, M6 x4, M7 x13. No complete set of seven fragments -
  M3 and M5 are both 0, so no dig is possible. Both Dig buttons
  (Dig 1 time, Dig 2 time(s)) are greyed out. Skip Animation is
  checked.
- Chest progress track reads 1 of 15, against 10 of 15 on
  2026-10-25 - see the reset note in the how-it-is-done section.
- No fragment exchange executed - exchanges need owner approval
  per the activity limits and none was attempted. Nothing claimed,
  no diamonds or money touched.
- Cross-check - the scout 0204 unit about half an hour later read
  the identical counts and the identical 1 of 15 track from the
  same screen, so the 0150 read is confirmed by a second live read
  the same morning, not a single-read figure.
- Forward note from the record, not a measured fact - the 9 secret
  tasks dispatched in the preceding secrets unit will drop
  fragments when they finish, and M3 and M5 may refill then. The
  next treasures unit re-reads the counts rather than assuming
  that refill.

## What the 2026-11-01 1420 unit added

- Unit treasures-2026-11-01-1057 by ticker-1404, status
  done. Entered from the Secret Command Post screen left
  open by the secrets unit of the same pass; the Hidden
  Treasures tab was tapped at norm (439,133) and the tab
  title was verified.
- Live before dig: tab badge 1; fragments M1 x13, M2
  x13, M3 x1, M4 x10, M5 x3, M6 x7, M7 x13; chest progress
  1/15; Skip Animation ticked; Dig 1 time enabled, Dig 2
  time(s) greyed. Scarcest fragment M3 x1 caps the
  account at exactly the 1 dig the badge advertised - a
  second confirmation of the badge-equals-digs rule.
- Dig: Dig 1 time tapped at norm (380,938) with Skip
  Animation on; the CONGRATULATIONS panel read live: 6
  reward tiles - crate-type icon x12, coin-pile icon x12,
  1m speedup x25, 1m speedup x100, blue triangles x400,
  silver ingots x100. The first two tiles carried no text
  label in the panel, so their item names are recorded
  as icons only, not named. No chest tier was displayed.
  Reward counts differ from the 2026-10-25 dig, so
  per-dig figures are not fixed - re-read each dig.
- Live after dig, panel closed by a tap at norm
  (500,850): tab badge cleared; fragments M1 x12, M2 x12,
  M3 x0, M4 x9, M5 x2, M6 x6, M7 x12 - exactly one of
  each consumed; chest progress 2/15; both Dig buttons
  greyed. No complete set remains, so no further dig is
  due. The 1/15 to 2/15 advance confirms the track
  increments one per dig on the current track; whether
  the 1/15 start was a reset of the 2026-10-25 10/15
  track is still unconfirmed.
- No fragment exchange was executed (owner approval
  required, and none was sought). No diamonds, money or
  paid button touched.

## Limits

- No fragment exchange is executed without owner approval - fragments
  are scarce (M5 above all) and an exchange is hard to undo.


## What the 2026-11-02 0207 unit added - checked, nothing to dig, no fragment income since the 1420 dig

- Unit treasures-2026-11-01-2257 by ticker-0204, status
  done (checked, nothing to dig). Entry: the game was
  already open on the Secret Command Post screen from
  the preceding secrets work; the Hidden Treasures tab
  was tapped at norm (439,133) and the screen was
  verified as Hidden Treasure.
- Fragment counts read live on the map: M1 x12, M2 x12,
  M3 x0, M4 x9, M5 x2, M6 x6, M7 x12. These are identical
  to the post-dig counts of the 2026-11-01 1420 unit, so
  no fragment income has arrived since that dig - a
  measured zero-income interval from the 1420 dig to this
  02:07 read. No complete set of seven fragments exists:
  M3 is 0, so no dig is possible. Both Dig buttons (Dig
  1 time, Dig 2 time(s)) are greyed out. Skip Animation
  is checked.
- Chest progress track reads 2/15, unchanged since the
  1420 dig, corroborating the per-dig increment with no
  intervening dig.
- No fragment exchange executed: exchanges need owner
  approval per the activity limits and none was
  attempted. Nothing claimed, no diamonds or money
  touched.
  Evidence in `_records_/2026-11-02/hidden-treasures/0207-queue-run.md`.

## What the 2026-11-02 0424 unit added - fragment income resumed, M3 still 0

- Unit treasures-2026-11-02-0257 by ticker-0404,
  session about 04:24, status done as checked only:
  the tab was opened and read live, and no dig is
  possible, so the tracker is marked done for the
  regular.
- Entry: the game was already on the Secret Command
  Post screen from the preceding secrets work, with
  the Reward Recovery panel still open. The panel's X
  button took no effect twice (background tap, then
  title-bar foregrounding tap plus X tap) - per queue
  rule R2 that method ended there. The post screen's
  back arrow at norm [62,962] closed the panel, and
  the Hidden Treasures tab opened at once.
- Fragment stocks, read live: M1 x13, M2 x14, M3 x0,
  M4 x9, M5 x3, M6 x6, M7 x13. Against the 0207 read:
  M1 plus 1, M2 plus 2, M5 plus 1, M7 plus 1; M3, M4
  and M6 unchanged. The zero-income interval recorded
  at 0207 has therefore ended - fragments arrived
  between the 02:07 and 04:24 reads. Attribution is
  partial only: the same-pass secrets claims (0426)
  paid Treasure Map Fragment #1 x1, #5 x1 and #7 x1,
  matching the M1, M5 and M7 gains of 1 each, but the
  M2 gain of 2 is NOT explained by that report and is
  not attributed here.
- M3 at zero still means no complete set of seven
  exists, so no dig is possible: both Dig buttons
  (Dig 1 time, Dig 2 time(s)) are greyed out, Skip
  Animation is ticked, chest progress reads 2 of 15,
  unchanged, and the tab carries no red badge. No
  fragment exchange was executed (exchanges need
  owner approval per the activity limits) and none
  was inspected beyond the map stocks. Nothing
  claimed, no diamonds or money touched.
  Evidence in `_records_/2026-11-02/hidden-treasures/0424-queue-run.md`.


## What the 2026-11-02 1009 unit added

- Unit treasures-2026-11-02-0657 by ticker-1004, session
  about 10:09, status done as checked only: the tab was
  opened and read live, and no dig is possible, so the
  tracker is marked done. Evidence in
  `_records_/2026-11-02/hidden-treasures/1009-queue-run.md`.
- Entry: the game was already on the Secret Command Post
  screen (Secret Mobile Squad tab) when the unit started.
  Tab-switching quirk, per queue rule R2: a click on the
  Hidden Treasures tab's grounded point (374,147) did
  nothing twice (once as click_element, once as a
  coordinate click; the first click only opened a Hero
  EXP reward tooltip on a task row). A double-click at
  the same point switched to the Hidden Treasures page at
  once. Single taps on this tab are unreliable in this
  session; double-click is the working variant.
- Fragment stocks, read live: M1 x13, M2 x14, M3 x0,
  M4 x9, M5 x3, M6 x6, M7 x13. Identical to the 0424 run's
  stocks: no fragment movement since then. M3 at zero
  means no complete set of seven exists, so no dig is
  possible: both Dig buttons (Dig 1 time, Dig 2 time(s))
  are greyed out, Skip Animation is ticked, chest
  progress reads 2 of 15, and the tab carries no red
  badge. No fragment exchange was executed (exchanges
  need owner approval per the activity limits) and none
  was inspected beyond the map stocks. Nothing claimed,
  nothing spent.


## What the 2026-11-02 1352 unit added

- Unit treasures-2026-11-02-1057 by ticker-1336, session
  about 13:47 to 13:50 by unit timestamps (the file name
  1352 reflects the estimate at writing time; the unit
  timestamps govern), status done as checked only: the
  tab was opened and read live, and no dig is possible,
  so the tracker is marked done for the regular.
  Evidence in
  `_records_/2026-11-02/hidden-treasures/1352-queue-run.md`.
- Entry: the base left-column slot norm (48,643) opened
  SECRET COMMAND POST on the first tap, title verified -
  the same entry point the same-pass secrets unit used.
  The Hidden Treasures tab switched with a double-click
  at norm (374,147), the working variant from the 1009
  run; the page verified as Hidden Treasure before
  reading.
- Fragment stocks, read live: M1 x13, M2 x14, M3 x0,
  M4 x9, M5 x3, M6 x6, M7 x13. Identical to the 1009
  run's stocks and to the 0424 stocks: no fragment
  movement since the 04:24 read. M3 at zero means no
  complete set of seven exists, so no dig is possible:
  both Dig buttons (Dig 1 time, Dig 2 time(s)) are
  greyed out, Skip Animation is ticked, chest progress
  reads 2 of 15, and the tab carries no red badge.
- No fragment exchange was executed (exchanges need
  owner approval per the activity limits) and none was
  inspected beyond the map stocks.
- Exit corroboration: the back arrow centre norm
  (128,959) returned to base on the first tap - the same
  point the same-pass secrets unit re-grounded to after
  (88,957) failed. The (128,959) centre is now the
  standing exit point for this panel; see the secrets
  profile's 1345 section.
- Outcome: no dig made, nothing claimed, nothing
  exchanged. Tracker marked done.

## Open questions

- What the chest progress track pays at 15 of 15.
- What the Hidden Treasures tab badge counts - it read 1 on
  2026-11-08 while the fragment stock allowed 3 digs, so it is not
  the dig count; its meaning is unconfirmed. (Added 2026-11-08 1459;
  re-confirmed 2026-11-08 2255: badge 1 both before and after the
  dig while stock allowed 3 digs before and 2 after.) (2026-11-09 0525 update: badge 1 again, this time with the stock allowing exactly 1 dig (M3 binding at x1) - badge 1 when 1 dig is possible is consistent with the disproved rule's coincidence, not evidence for it; the 1459/2255 disproofs stand and the badge's meaning stays open.)
- Whether the 1 of 15 track read on 2026-11-01 is a reset of the
  10 of 15 track, a new track, or a different counter - the change
  is recorded, the mechanism is not. The 1420 dig advanced it
  1 of 15 to 2 of 15, so it increments per dig; the reset
  question itself is still open.
- Whether particular secret missions drop particular fragment kinds -
  the morning claims dropped fragments number 7, 4 and 1, and the
  recovery record dropped five kinds, but no controlled mapping yet.
- Whether the Golden Mobile Squad Decoration has dropped for this
  account in the past.

## What the 2026-11-02 2135 unit added - 2 digs, done

- Unit treasures-2026-11-02-1857 by ticker-2134, about 21:35 to
  21:38, status done: two complete fragment sets were on hand and
  both were dug. Evidence in
  `_records_/2026-11-02/hidden-treasures/2135-queue-run.md`.
- Entry: the base left-column slot norm (56,643) opened SECRET
  COMMAND POST on the first tap, title verified. The Hidden
  Treasures tab at norm (369,139) switched the page on the first
  tap, page verified as Hidden Treasure. A single tap worked here,
  unlike the 1009 and 1352 runs where a double-click was the
  working tab variant - re-ground the tab tap from the current
  screenshot each unit, never inherit the variant.
- Fragment stocks, read live before the dig: M1 x14, M2 x14, M3 x2,
  M4 x9, M5 x4, M6 x7, M7 x13. M3, at zero in the 1352 run, is back
  to x2, so two complete sets of seven exist. Chest progress 2 of
  15. Skip Animation was already ticked. The fragment income
  between the 1352 and 2135 reads is recorded, not attributed: no
  claim in this record ties it to specific secret-mission claims.
- Mis-tap note, method: a first tap aimed at Dig 2 time(s) at the
  estimated norm (810,950) did NOT land on the button - it opened
  the EXCHANGE ITEMS panel instead. That panel is history only:
  it shows the completed 2026-10-25 trade (gained M5, lost M6,
  partner Mistress Sam) and no new exchange was made - New
  Exchange was never tapped. The panel was closed with its X at
  norm (880,163) and the map re-read. Pivot: the Dig 2 time(s)
  button was re-grounded on the fresh screenshot (visual
  grounding point (627,955)), and that tap dispatched the dig at
  once. Lesson for the next unit: ground the Dig button on the
  current screenshot; the (810,950) estimate lands right of the
  button.
- Dig and rewards: one tap on Dig 2 time(s) at the grounded point
  (627,955) ran the dig animation, then a CONGRATULATIONS panel.
  Rewards panel as read (the panel presented after the Dig 2 tap;
  the split between the two digs is not separately visible, so
  the panel is reported as presented, not per dig): grey boxes
  x12, gold coin piles x24, medal 1.2K, 1 minute speedups x50,
  x75 and x125, blue triangles x400, silver ingots x100. Chest
  tier won was not displayed.
- Fragment stocks, read live after the dig: M1 x12, M2 x12, M3 x0,
  M4 x7, M5 x2, M6 x5, M7 x11. Exactly minus 2 on every fragment,
  and chest progress 2 of 15 to 4 of 15: both digs consumed. Both
  Dig buttons are greyed out after the dig, as expected with M3
  at zero.
- Exit: back arrow centre norm (128,959) returned to base on the
  first tap - the standing exit point, confirmed again.
- No fragment exchange was executed (exchanges need owner
  approval per the activity limits). Nothing spent, no paid button
  tapped.


## What the 2026-11-03 0014 unit added - checked only, M3 at zero, no dig

- Unit treasures-2026-11-02-2257 by ticker-0004, session
  about 00:14 local, status done, checked only.
  Evidence in
  `_records_/2026-11-03/hidden-treasures/0014-queue-run.md`.
- Entry: Secret Command Post entered from the base
  left-column white pickup icon at norm 53,653 (same
  slot as the secrets unit this pass). Hidden
  Treasures tab tapped at norm 369,139; title
  verified as Hidden Treasure. The Hidden Treasures
  tab carried no red dig badge at entry, consistent
  with the counts below.
- Fragment counts, read live from the map: M1 x12, M2
  x12, M3 x0, M4 x7, M5 x2, M6 x5, M7 x11. Chest
  progress track reads 4/15 at the top right of the
  map screen. These stocks are exactly the post-dig
  stocks of the 2135 unit - no fragment income
  between the 2135 dig and this read is recorded,
  and none is attributed.
- Outcome: M3 is at zero, so no complete set of seven
  fragments is on hand and no dig is possible; both
  Dig buttons are greyed out. No dig was attempted
  and no fragment exchange was executed (exchanges
  need owner approval per the metadata limits).
  Target 1 dig if a full set were on hand;
  achieved 0 digs, for the stated reason - M3 x0 is
  the binding fragment. No diamonds, no money, no
  exchange touched. Game left on the base screen.

## What the 2026-11-03 0349 unit added - checked only, counts identical to 0014, M3 still binding

- Unit treasures-2026-11-03-0257 by ticker-0334, session
  about 03:49 local, status done, checked only. Evidence
  in `_records_/2026-11-03/hidden-treasures/0349-queue-run.md`.
  No diamonds, no money, no exchange touched.
- Entry: Secret Command Post entered with the unsnapped
  exact-centre pickup tap [55,632] learned in the
  secrets unit of this pass (see secret-missions); title
  verified as SECRET COMMAND POST before any further
  tap. Hidden Treasures tab tapped at norm [369,139];
  title verified as Hidden Treasure. The tab carried no
  red dig badge at entry.
- Fragment counts, read live from the map, unchanged
  from the 2026-11-03 0014 unit in every figure: M1 x12,
  M2 x12, M3 x0, M4 x7, M5 x2, M6 x5, M7 x11. Chest
  progress track reads 4/15 at the top right of the map
  screen, also unchanged from 0014. Skip Animation is
  ticked. Both Dig buttons are greyed out.
- Outcome: done, checked only. M3 is at zero, so no
  complete set of seven fragments is on hand and no dig
  is possible; no dig was attempted and no fragment
  exchange was executed (exchanges need owner approval
  per the metadata limits). Target: 1 dig if a full set
  were on hand; achieved: 0 digs, for the stated reason
  - M3 x0 is the binding fragment, now for the second
  consecutive treasures read with zero fragment movement
  between them (0014 to 0349). Tracker: marked done for
  treasures by this pass. Game left on the base screen.

## What the 2026-11-03 0838 unit added - checked only, counts identical to 0349, folded late by the 1332 run

- Unit treasures-2026-11-03-0657 by ticker-0834, session
  about 08:38 local, status done, checked only. Evidence
  in `_records_/2026-11-03/hidden-treasures/0838-queue-run.md`.
  No diamonds, no money, no exchange touched. This record
  was folded by the 1332 organizer run, after the 0349
  fold: the intervening hourly runs folded other
  activities and left this treasures read unfolded, so it
  is folded here together with the 1243 read to keep the
  fragment chain continuous.
- Entry: Secret Command Post opened on the first try
  with the unsnapped exact-centre pickup tap at norm
  [55,632]; Hidden Treasures tab tapped next.
- Fragment counts, read live from the map, identical to
  the 0349 unit in every figure: M1 x12, M2 x12, M3 x0,
  M4 x7, M5 x2, M6 x5, M7 x11. Chest progress 4/15,
  unchanged. Both Dig buttons greyed out.
- Outcome: done, checked only. M3 is at zero, so no
  complete set of seven fragments is on hand and no dig
  is possible; no dig was attempted and no fragment
  exchange was executed (exchanges need owner approval
  per the metadata limits). Tracker: marked done for
  treasures by this pass. Game left on the base screen.


## What the 2026-11-03 1243 unit added - checked only, counts identical to 0838, M3 still binding, leftover panel entry

- Unit treasures-2026-11-03-1057 by ticker-1234, session
  about 12:43 local, status done, checked only. Evidence
  in `_records_/2026-11-03/hidden-treasures/1243-queue-run.md`.
  No diamonds, no money, no exchange touched.
- Entry, with the 1204 entry lesson applied: a Gold Mine
  Lv.29 building panel was open at entry (leftover from
  the ticker-1204 secrets unit's entry failure, recorded
  in secret-missions/1223-queue-run.md). It was closed
  with its X; Quick Dispatch was not tapped, and no
  survivor was dispatched. The base left column was
  re-measured fresh from the same screenshot it was
  tapped from (visual grounding on that screenshot):
  green face centre norm 52,580, white pickup centre
  norm 52,630, radar dish with badge 11 at 52,707. The
  pickup tap at norm 52,630 opened SECRET COMMAND POST
  on the first try, title verified. Hidden Treasures tab
  tapped at norm 369,139; title verified as Hidden
  Treasure. The tab carried no red dig badge at entry.
- Fragment counts, read live from the map, identical to
  the 2026-11-03 08:38 unit in every figure: M1 x12,
  M2 x12, M3 x0, M4 x7, M5 x2, M6 x5, M7 x11. Chest
  progress 4/15, unchanged. Skip Animation is ticked.
  Both Dig buttons (Dig 1 time, Dig 2 time(s)) are
  greyed out.
- Outcome: done, checked only. The regular is fully
  checked for this slot. Target: 1 dig if a full set
  were on hand; achieved: 1 check, 0 digs, for the stated
  reason - M3 x0 is the binding fragment, now for the
  fourth consecutive treasures read with zero fragment
  movement since the 2135 post-dig stocks (0014, 0349,
  0838, 1243). No dig was attempted and no fragment
  exchange was executed (exchanges need owner approval
  per the metadata limits).
- Exit note: the exit tap from the Hidden Treasures tab
  switched tabs rather than leaving the post; no task,
  Mega button or ally row was touched. Game left in the
  Secret Command Post on the Secret Tasks tab - the post
  is where the next secrets unit enters anyway, so the
  position is carried, not a stray state.

## What the 2026-11-04 0847 unit added - checked only, counts identical to 0838/1243, M3 still binding

- Unit treasures-2026-11-04-0657 by ticker-0834, about 08:47 local, status done, checked only. Evidence in `_records_/2026-11-04/hidden-treasures/0847-queue-run.md`. Session cc-440. No diamonds, no money, no exchange touched. No different-device dialog appeared.
- Entry from the Secret Command Post screen left by the secrets unit; the Hidden Treasures tab tap registered on the first tap (unlike the Claim buttons in the secrets unit of the same pass, which stayed unresponsive - tab taps and Claim buttons do not share this failure).
- Fragment counts read live from the map, identical to the 2026-11-03 0838 and 1243 units in every figure: M1 x12, M2 x12, M3 x0, M4 x7, M5 x2, M6 x5, M7 x11. Chest progress 4/15, unchanged. Skip Animation is ticked.
- M3 at zero caps complete sets at zero, so no dig is possible; the Dig buttons were not tapped. No fragment exchange was made (exchanges need owner approval).
- The Secret Task tab's red dot is the secrets unit's unclaimed tasks, not this unit's work; nothing there was touched.
- Back arrow tap did not navigate; a left-edge swipe drag returned to the base screen, as in the earlier units of this pass. Outcome: done, checked, no dig available.

## What the 2026-11-08 1459 treasures unit added - one dig executed, badge-equals-digs rule disproved, chest progress 7/15

- Unit treasures-2026-11-08-1057 by ticker-1434, about 14:57 to 15:00
  local, status done - one treasure dig executed and verified, chest
  progress 6/15 to 7/15, 2 digs remain by stock. Evidence in
  `_records_/2026-11-08/hidden-treasures/1459-queue-run.md` (commit
  dfd3c87f9 on records/2026-11-08). Tracker untouched.
- Session: computer session cc-134 on the owner Mac mini, LastWar
  already running. The deployed secret tasks from the previous unit
  of this pass showed running countdowns (UR Rescue Missing Agent
  about 01:57, SSR tasks about 00:57). No device-access error, no
  different-device dialog, no login demanded. Total Power read live
  on base at entry and at close: 149,850,353.
- Fragment stock read live before the dig: M1 x16, M2 x15, M3 x3,
  M4 x7, M5 x3, M6 x7, M7 x13. Scarcest M3 and M5 at x3, so 3 digs
  were possible by stock, while the tab badge still read 1 - the
  badge does NOT match the stock count this unit. CORRECTION: this
  disproves the badge-equals-digs rule this profile carried since
  2026-10-25 (first read) and re-confirmed on 2026-11-01 (second
  confirmation) - in both earlier reads the badge happened to read 1
  when the stock allowed exactly 1 dig, so the rule was never
  actually tested until now. The standing claims in How to enter and
  Cadence are corrected above; what the badge counts is an open
  question. Chest progress read 6/15 before the dig. Skip Animation
  was already ticked.
- Dig: tapped Dig 1 time only, per the activity metadata (one dig
  per unit). CONGRATULATIONS panel verified. Rewards as shown (item
  identities for the icons are unverified, recorded as shown): grey
  crates x24, orange food(?) x12, coin piles x12, medal 900, blue
  triangle 400, silver ingots x100. No chest tier was displayed.
- Verified after dismissing the panel: each fragment down exactly 1
  (M1 x15, M2 x14, M3 x2, M4 x6, M5 x2, M6 x6, M7 x12); chest
  progress 6/15 to 7/15; Dig buttons now read Dig 1 time and Dig 2
  time(s), so 2 more digs remain possible by stock. The tab badge
  still reads 1.
- The remaining 2 possible digs were not taken: one dig per unit is
  the activity's standing pattern, and the stock stays for the next
  treasures unit.
- Navigation slip: the batched double back-tap out of the post
  opened the Chat screen on the second tap (the post's back arrow and
  the base screen's chat entry share the spot in sequence). No chat
  content was read, tapped or recorded; the Chat screen was exited at
  once with its back arrow. The game was left on the base screen.
  Lesson: do not batch the post-exit back-tap with a second tap - the
  second tap lands on whatever the base screen shows under that spot.
- Game left safe: base screen. No diamonds, money or other spending;
  no exchange touched.

## What the 2026-11-08 2255 unit added - 1 dig, chest 8/15, 2 digs remain capped by M3

- Unit treasures-2026-11-08-1857 by ticker-2235, about 22:54 to 22:55 local, status done. Evidence in `_records_/2026-11-08/hidden-treasures/2255-queue-run.md` (commit 0c9686b4f on records/2026-11-08).
- One treasure dig executed (Dig 1 time, Skip Animation on). Congratulations panel rewards, read live from its six tiles: chest stack x24, coin sacks x12, gold coins x24, medal 600, blue triangle 400, silver ingots 100. The chest tier won was not displayed on the panel.
- Fragment stocks verified live before and after the dig. Before: M1 x17, M2 x14, M3 x3, M4 x7, M5 x5, M6 x7, M7 x13. After: M1 x16, M2 x13, M3 x2, M4 x6, M5 x4, M6 x6, M7 x12 - exactly one of each fragment consumed. Chest progress 7/15 before, 8/15 after. The Dig button now reads "Dig 2 time(s)": 2 digs remain by stock, capped by M3 x2.
- The remaining 2 possible digs were not taken: one dig per unit is the activity's standing pattern, and the stock stays for the next treasures unit.
- Tab badge re-confirmation: the Hidden Treasures tab badge read 1 both before and after the dig, while the stock allowed 3 digs before and 2 after, so the badge does not count digs possible by stock - re-confirmed against the 1459 disproof of the badge-equals-digs rule. Its meaning stays open (see Open questions).
- No fragment exchange was opened or executed (needs owner approval).
- Red lines held: no diamonds or money spent. No speedups burned. No paid button tapped. No fragment exchange. No login or verification was demanded, and no different-device dialog appeared.
- Result stats: target 1, achieved 1, resources_gained (chest-stack x24, coin-sacks x12, gold-coins x24, medal 600, blue-triangle 400, silver-ingots 100), costs 2min-no-items-spent, verified yes, device_takeovers 0, follow_up none.

## What the 2026-11-09 0525 unit added - 1 dig, chest 10/15, M3 binding at zero, badge 1 with exactly 1 dig possible

- Unit treasures-2026-11-09-0257 by ticker-0504, about 05:20 to 05:25 local, status done. Evidence in `_records_/2026-11-09/hidden-treasures/0525-queue-run.md` (commit be01e91134 on records/2026-11-09). Computer session cc-224, same session as the secrets unit of this pass.
- Hidden Treasures tab opened from the Secret Command Post; the tab badge read 1, exactly the number of digs possible this time.
- Fragment stock before the dig, read live: M1 x15, M2 x12, M3 x1, M4 x5, M5 x3, M6 x5, M7 x11. M3 was the binding fragment, so exactly 1 dig was possible. Skip Animation was already ticked. Tapped Dig 1 time.
- CONGRATULATIONS panel paid 5 visible stacks: chest x24, coin x36, 1m speedup x50, 1m speedup x25, silver ingot x200. The chest tier won was not displayed, and the two speedup stacks carry different icons (types not fully identified); recorded as displayed.
- Verified live after the dig: fragment stock M1 x14, M2 x11, M3 x0, M4 x4, M5 x2, M6 x4, M7 x10 - each down by exactly 1, one full set consumed. Chest progress track 9/15 to 10/15. Both Dig buttons now greyed and the tab badge cleared - no complete set left (M3 at 0 is the binding fragment).
- No further dig is possible until M3 (and the other kinds) are restocked by secret mission claims. The next treasures unit re-checks. The one-dig-per-unit standing pattern was followed; the stock stays for the next unit.
- Badge note: badge 1 with exactly 1 dig possible is consistent with the disproved badge-equals-digs rule's coincidence (badge 1 when 1 possible), not evidence for it - the 1459 and 2255 disproofs stand. See the updated Open questions entry.
- No diamonds or money spent. No fragment exchange executed (needs owner approval). No login or verification was demanded, and no different-device dialog appeared.
- Result stats: target 1, achieved 1 (1 dig from badge 1), resources_gained chest x24, coin x36, 1m speedup x50, 1m speedup x25, silver ingot x200, costs 5min-no-items-spent, verified yes, device_takeovers 0, follow_up none.
