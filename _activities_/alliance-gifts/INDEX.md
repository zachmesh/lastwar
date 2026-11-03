---
title: Alliance Gifts
created: 2026-10-25T18:58:00Z
modified: 2026-11-03T07:37:53Z
level: L1
version: 1.14.0
description: Claiming alliance gifts, one activity folder for gift knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner structure direction on activity folders, 2026-10-25
  - source: owner direction to claim both gift pages, evening of 2026-10-25
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (0935 gifts unit)
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1221 gifts unit)
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1718 gifts unit)
  - source: alliance-gifts execution record 2026-11-01 2122 queue run (ticker-2104 unit, done, 221 Regular plus 70 Premium)
  - source: alliance-gifts execution record 2026-11-02 0023 queue run (ticker-0004 unit, done, 45 Regular plus 5 Premium)
  - source: ticker-0334 alliance-gifts execution record 2026-11-02 0338 queue run (done, 54 Regular and 12 Premium)
  - source: ticker-0804 alliance-gifts execution record 2026-11-02 0817 queue run (done, 1 Regular and 1 Premium)
  - source: alliance-gifts execution record 2026-11-02 1215 queue run (ticker-1204 unit, done, counter anomaly filed as issue 183)
  - source: perception-scout execution record 2026-11-02 1801 queue run (ticker-1755 unit, partial, Gift Level 28 progress read, Issue #183 evidence)
  - source: alliance-gifts execution record 2026-11-02 2018 queue run (ticker-2004 unit, done, 31 Regular plus 3 Premium)
  - source: alliance gifts execution record 2026-11-02 2305 queue run
---


# Alliance gifts

## What this activity is

Claiming the gifts the alliance generates for its members. Gifts are
produced by ally activity - defeating Doom Elites and CL-7 Victims
generates Regular gifts, and ally purchases generate Premium gifts.
This folder accumulates gift knowledge - gift levels, tiers and claim
flow. Executions are recorded in `_records_/<date>/alliance-gifts/`,
one file per execution.

## How to enter

- Open the Alliance panel from the base right column (Alliance)
  and tap Alliance Gifts. The entry carries a red dot while gifts
  wait.
- Foreground precondition, recorded by the retro of 2026-10-31 -
  the 2026-10-31 1030 unit never opened the Alliance panel
  because Chrome stayed frontmost and background taps did not
  reach the Alliance button. Two no-change taps end the
  background-input method inside the unit under queue rule R2 -
  bring the game window to the foreground and re-observe before
  tapping again. The same-day later units recovered, so this
  blocker is transient, not a dead entry route.

## How it is done

- The gifts screen has two tabs, Regular and Premium. Each tab has a
  Claim All button. Claim All on BOTH tabs every round - the owner
  confirmed this explicitly on the evening of 2026-10-25.
- Claim All pays the whole tab in one tap and shows a summary dialog
  naming the count claimed.
- Gifts keep arriving as allies play, so a tab can show new gifts
  minutes after a claim - one extra Regular gift arrived and was
  claimed during the same evening visit. The Alliance Gifts entry
  keeps its red dot while any gift waits.

## Cadence

- Every daily round, and opportunistically whenever the gifts entry
  shows a red dot. There is no observed cap on claims.

## Scope and availability

- Gift Level 28 on 2026-10-25, with progress 161,149,070 of
  206,300,000 before the evening claims and about 161,153,870 after -
  claimed gifts feed the level progress.

## What is known from 2026-10-25

- Morning round - the claim read 844 plus 2 Regular and 72 Premium,
  as displayed. What the 844 figure counts is not yet confirmed.
- Evening round - Regular Claim All collected 453 gifts in one tap
  (mostly Violet's Gift, worth 10 points each, sourced from allies
  defeating CL-7 Victims and Doom Elites), plus 1 more that arrived
  right after (dontard defeating a Doom Elite). Premium Claim All
  collected 34 gifts - UR gifts worth 500 and R gifts worth 50,
  sourced from ally purchases such as Drone Parts and the Coin
  Weekly Pass.

## What the 2026-11-01 0110 unit added

- Measured points, 0110 (ticker-0104): Alliance at norm
  933,735 opened the panel at once; Alliance Gifts carried a
  red dot and its grounded button at norm 315,606 opened the
  gifts screen. Gift Level 28, progress 177,052,730 of
  206,300,000 at entry.
- Claim All points differ by tab, ground each separately:
  Regular Claim All at norm 500,935; Premium Claim All
  re-grounded on this unit's own screenshot at norm 754,944.
- Counts, dialog-confirmed: Regular Claim All claimed 47
  (dialog: "A total of 47 Regular Alliance Gifts were claimed
  this time"); progress then read 177,053,200. Premium badge
  read 5 but the dialog read 6 - one gift arrived between the
  badge read and the tap. A second Premium sweep read badge 2:
  two new SSR gifts from Janet ^ (Premium Glitter Coin Pack)
  that arrived during the unit, claimed at the same point.
  Premium total 8; progress closed at 177,055,050 of
  206,300,000.
- Dismiss: a tap below the dialog at norm 500,850; a first
  dismiss attempt returned outcome unknown with the dialog
  still up, and a second tap at the same point closed it.
- Two-sweep rule: expect new gifts to keep arriving during the
  unit; two sweeps clear a tab, and chasing further arrivals is
  not required.
- Checkbox untouched: the "Hide your name on Gifts" checkbox
  was left unchecked and untouched.
- Foreground nuance: Chrome stayed frontmost for part of the
  unit and every grounded tap still reached the game, so
  background input is control-dependent (matching the
  survivors profile's framing). This does not supersede the
  queue rule R2 practice that two no-change taps end the
  background-input method inside a unit.



## What the 2026-11-01 0935 unit added

- Performed, ticker-0934, session about 09:35 to 09:38:
  both tabs claimed. This pass is the first successful game
  execution after the device-offline run on 2026-11-01
  (last seen 01:47 local, thirteen consecutive
  access-failed passes through 0834); the Mac mini channel
  was online again at pass start. Alliance panel read
  [AP3x] The Apex, 95/100 members.
- Entry, reconciling the 0110 unit: the first Alliance tap
  at norm 933,735 showed only a press effect and left the
  base screen unchanged - the background-input pattern
  recorded in the 2026-10-31 retro - while the 0110 unit
  had opened the panel at once from the same point. The
  difference is foreground state, not a superseded point:
  a title-bar left-segment tap followed by a second
  Alliance tap at norm 924,733 opened the panel at once.
  Chrome stayed the frontmost app throughout and input
  still reached the game after the title-bar tap, so no
  foreground escalation was needed. If the first Alliance
  tap shows only a press effect, tap the title-bar left
  segment first and retry before concluding entry failed.
- Alliance Gifts button at norm 314,614 opened the gifts
  screen, matching the 2026-10-31 1924 unit. Gift Level 28,
  progress 178,139,340 of 206,300,000 at entry.
- Regular Claim All at norm 498,931, dialog-confirmed:
  "A total of 222 Regular Alliance Gifts were claimed this
  time". A second sweep showed no new badge and rows
  reading Claimed; progress read 178,141,560 (plus 2,220,
  matching 222 gifts at 10 points each). No third sweep
  was needed this unit.
- Premium tab tapped at norm 694,269. Premium Claim All
  at norm 767,931 - the 2026-10-31 1924 unit point of
  763,931 within a few points, so ground the Premium point
  fresh each unit rather than reusing a pinned point. Badge
  and dialog both read 18 Premium gifts: "A total of 18
  Premium Alliance Gifts were claimed this time". The "Hide
  your name on Gifts" checkbox was left unchecked and
  untouched. Verification: Premium rows read Claimed, the
  Claim All badge was gone, and Gift Level progress closed
  at 178,149,760 of 206,300,000. The game was left on the
  Alliance Gifts Premium list.

## What the 2026-11-01 1221 unit added

- Performed, ticker-1204, session about 12:21, status
  done: the Alliance panel opened from the base on the
  first tap, and the Alliance Gifts entry carried a red
  dot. Gift Level 28, progress 178,322,940 at entry.
- Regular tab: Claim All badge 20 claimed 21 gifts in one
  tap (one arrived during the claim), summary dialog "A
  total of 21 Regular Alliance Gifts were claimed this
  time". Progress moved 178,322,940 to 178,323,150,
  plus 210, exactly 21 times 10 points - the same
  badge-versus-dialog arrival gap the 0110 unit measured,
  so a badge count is never the claimed count until the
  dialog confirms it.
- Premium tab: the first tab tap did not switch the tab,
  the second tap at norm 700,250 did (one no-change tap,
  not a blocker). Claim All badge 3 claimed 3 gifts: two
  Alliance Gift (SSR) at plus 200 points each and one
  Alliance Gift (MR) at plus 1000 points. Progress moved
  178,323,150 to 178,324,550, plus 1400, exactly 200 plus
  200 plus 1000.
- Re-check discipline, the two-sweep rule in action:
  back on the Alliance panel the Gifts entry still showed
  a red dot, so the unit re-entered the gifts screen
  instead of closing. One new Regular gift had arrived
  (ANGEL777 Apex, Defeated Doom Elite, plus 10) and was
  claimed with Claim All badge 1; the summary dialog
  confirmed 1 Regular gift claimed. Unit total: 22
  Regular gifts and 3 Premium gifts, 25 gifts claimed.
  Progress after the final gift was not re-read live, so
  the last live progress figure is 178,324,560, read on
  the re-entry screen before the final claim; the final
  gift's plus 10 points are counted in the claimed total,
  not in a derived progress figure.
- No Alliance Store opened, no purchase made. The game
  was left on the Alliance panel, not on another
  regular's screen.

## What the 2026-11-01 1718 unit added

- Performed, ticker-1704, session about 17:06 to 17:18,
  status done: Regular 4 claimed, Premium 0 new. Gift
  Level 28 throughout.
- Device takeover, first of the pass: the game showed
  the "account active on a different device" dialog at
  session start; Confirm was tapped once, the app
  exited as expected, and the game was reopened on the
  Mac. No second dialog appeared. This is the standing
  kick rule working as written, not a blocker.
- Entry correction, measured fresh: the first
  Alliance-button tap landed on the Alliance Wars rally
  screen. Visual grounding corrected the base Alliance
  button centre to norm 929,688 and Alliance Gifts on
  the Alliance panel to norm 313,621. The Alliance
  Gifts entry carried a red dot.
- Regular tab: Claim All badge 4 claimed 4 gifts; the
  summary dialog read live "A total of 4 Regular
  Alliance Gifts were claimed this time". Badge and
  dialog agree this time - unlike the 1221
  badge-20-to-21 arrival gap, no gift arrived mid-claim
  here, so the badge-versus-dialog rule stands (dialog
  confirms), with this unit as the agree-case.
- Reward icons read live in the dialog: 1.0K, 5 and
  600. Progress bar read 178,677,740 of 206,300,000 on
  entry and 178,687,430 after the Regular claim; the
  bar moved during the unit, so the plus 9,690 delta is
  NOT attributed to this unit's 4 gifts alone, and no
  per-gift point value is derived from it. This
  contrasts with the 1221 exact plus 210 for 21 gifts -
  a progress delta is only evidence when the unit
  attributes it.
- Premium tab: every visible row read Claimed,
  including one scrolled page further down (SSR, MR
  and UR rows from Supreme, Premium and Luxury Glitter
  Coin Packs and the Super Monthly Pass). No Claim All
  button was offered on Premium. Premium new claims: 0.
  A Premium tab with nothing claimable offers no Claim
  All - the claim-both-pages rule is satisfied by
  checking both tabs, not by a button existing on both.
- No diamonds or money spent, no red line touched.

## What the 2026-11-01 2122 unit added

- Done, Claim All on BOTH tabs as the owner directed:
  unit gifts-2026-11-01-1830 by ticker-2104, session about
  21:16 to 21:22. Regular 221 gifts and Premium 70 gifts,
  each confirmed by its own summary dialog. Gift Level 28
  progress read live: 179,652,510 of 206,300,000 before
  the Regular claim, 179,654,720 after it (plus 2,210,
  exactly 221 times 10 points), and 179,664,120 after the
  Premium claim (plus 9,400). Closing verification read
  live: both tabs show their visible gifts as Claimed, no
  Claim All button and no red dot remains on either tab.
  No new gifts arrived between the two claims and the
  closing read.
- Entry lessons, measured fresh: the Alliance panel
  carried a red dot on Gifts, but the first tap aimed at
  the Gifts button from a screenshot estimate opened
  Alliance Wars instead; the back arrow returned to the
  panel, and the second tap used the OCR text position
  (norm 303,595) and opened Alliance Gifts. Lesson for
  the next unit: trust OCR norm positions over screenshot
  pixel estimates for panel buttons. Regular tab Claim
  All sits centred (norm 498,967); Premium tab Claim All
  sits right-shifted beside the "Hide your name on
  Gifts" checkbox (norm 718,967) - a tap at the Regular
  position missed it and left the 70 badge standing, and
  the corrected tap paid 70. Each Claim All summary
  dialog was dismissed with a tap on the dialog itself,
  and the unit closed only after both tabs were re-read
  live. The accidental Alliance Wars open was left
  immediately via the back arrow and nothing was done
  there.
- No diamonds or money spent, no paid button tapped.
  Evidence in `_records_/2026-11-01/alliance-gifts/2122-queue-run.md`.


## What the 2026-11-02 0023 unit added

- Done, Claim All on BOTH tabs as the owner directed:
  unit gifts-2026-11-01-2230 by ticker-0004, session about
  00:18 to 00:23. Regular 45 gifts and Premium 5 gifts,
  each confirmed by its own summary dialog. Gift Level 28
  progress read live: 179,803,870 of 206,300,000 before
  the Regular claim, 179,804,320 after it (plus 450,
  exactly 45 times 10 points), and 179,805,720 after the
  Premium claim (plus 1,400; list entries SSR plus 200, R
  plus 50, SR plus 100, R plus 50, and a fifth gift below
  the fold). Closing verification read live: both tabs
  show their visible gifts as Claimed, and the Alliance
  Gifts entry red dot cleared on both tabs.
- Entry lessons, measured fresh: a first tap on the base
  right column at norm 849,683 hit the tan button left of
  Alliance, not Alliance itself, and produced no change.
  The right-column crop then measured the Alliance star
  icon centre at norm 941,701, and one tap there opened
  the Alliance panel ([AP3x] The Apex, 95/100 members,
  power 12,845,055,755). A first tap inside the panel at
  norm 311,536 opened Alliance Wars instead of Alliance
  Gifts: the window's title bar shifts content
  coordinates, so the Gifts button centre is norm
  313,595, not 536. Correction for the next unit that
  taps panel buttons from a screenshot: add about 30
  pixels of title bar to the content pixel before
  normalising. This refines the 2122 OCR-over-estimate
  lesson - the offset is the title bar.
- The accidental Alliance Wars open was left immediately
  via the back arrow from its Rally Intel screen ("No
  Alliance Rally currently"); nothing was joined,
  started or changed there.
- Foreground nuance: the two no-change taps in this unit
  were both coordinate misses, not background-input
  failures - the drags and corrected taps all reached the
  game while Chrome stayed frontmost, so the 2026-10-31
  foreground precondition did not recur here. This does
  not supersede the queue rule R2 practice that two
  no-change taps end the background-input method inside
  a unit, as the 0110 nuance already records.
- Evidence in `_records_/2026-11-02/alliance-gifts/0023-queue-run.md`.

## What the 2026-11-02 0338 unit added

- Done, Claim All on BOTH tabs: unit
  gifts-2026-11-02-0230 by ticker-0334, session about
  03:35 to 03:38. Regular tab: Claim All claimed 54
  Regular Alliance Gifts in one tap (summary dialog:
  "A total of 54 Regular Alliance Gifts were claimed
  this time"). Premium tab: Claim All claimed 12
  Premium Alliance Gifts in one tap (summary dialog:
  "A total of 12 Premium Alliance Gifts were claimed
  this time").
- Gift Level 28 progress read live: 180,150,630 before
  the Regular claim, 180,151,170 after it (plus 540,
  exactly 54 times 10 points, consistent with the
  0023 per-Regular rate), and 180,153,970 after the
  Premium claim (plus 2,800 across 12 gifts of mixed
  rarities - no single per-gift rate is stated for
  Premium from this unit), against 206,300,000.
  After both claims every visible gift row on both
  tabs read Claimed and neither tab carried a red dot.
- The "Hide your name on Gifts" checkbox was left
  untouched, and the Alliance Store was not opened.
- Entry lessons, measured fresh: two early background
  clicks missed their targets by about 30 px
  (Alliance icon, then the Alliance panel rows). Both
  were re-grounded with fresh measured points before
  retrying: the Alliance base icon sits at normalized
  (934,707) and the Alliance Gifts button at (313,595)
  in the 642x951 game window - the (313,595) point
  re-confirms the 0023 unit's title-bar-corrected
  point. One stray tap opened Alliance Wars instead
  of Gifts; it was closed with the back arrow, no
  action taken there. The game window was moved to x
  1278 so it sits clear of the frontmost Chrome
  window; it is restored to its usual spot at pass
  end.
- Evidence in `_records_/2026-11-02/alliance-gifts/0338-queue-run.md`.


## What the 2026-11-02 0817 unit added

- Done, Claim All on BOTH tabs: unit gifts-2026-11-02-0630
  by ticker-0804, session 08:11 to 08:17. Regular tab: Claim
  All at norm 498,952 claimed 1 gift (Commander Supa
  defeated Doom Elite, +10), progress 180,508,620 to
  180,508,630, and the pending gift showed Claimed with no
  Claim All button remaining on the Regular tab. Premium
  tab: Claim All at norm 763,952 claimed 1 gift (Alliance
  Gift R, +50, Drone Components Weekly Pass, 23:49:27
  remaining), the summary dialog read "A total of 1
  Premium Alliance Gifts were claimed this time", and
  progress moved to 180,508,680. Gift Level 28 unchanged,
  against 206,300,000. Total gift progress 180,508,620 to
  180,508,680 (+60).
- Completion sweep: returning to the Alliance panel, the
  Alliance Gifts entry no longer carried a red dot, and
  both tabs showed no pending Claim All.
- Entry lessons, measured fresh: the Alliance panel was
  opened from the base right column (Alliance button at
  norm 903,731). A first tap on the Alliance panel at norm
  311,515 opened Alliance Wars, not Alliance Gifts: the
  panel's button rows sit at norm y 509, 595, 679, 766 and
  849 (read from the panel's OCR labels), so 515 landed on
  the Wars row. The corrected tap at norm 303,595 opened
  Alliance Gifts, re-confirming the 595 row the 0023 and
  0338 units measured (313,595), with a 10-point x
  variance that the next unit re-grounds fresh.
- The Premium Claim All point 763,952 differs from the
  2122 unit's 718,967; the next unit re-grounds it fresh
  rather than treating either as fixed.
- Exit nuance, not a failure: the game was left on the
  Alliance panel after two back-arrow taps (norm 62,941
  and 62,973) produced no change, so that method was
  stopped under queue rule R2 rather than repeated. This
  does not affect the unit's result.
- Evidence in `_records_/2026-11-02/alliance-gifts/0817-queue-run.md`.


## What the 2026-11-02 1215 unit added

- Done, Claim All on BOTH tabs plus a mid-unit second
  Regular claim: unit gifts-2026-11-02-1030 by
  ticker-1204, session 12:06 to 12:15. Evidence in
  `_records_/2026-11-02/alliance-gifts/1215-queue-run.md`.
- Dialog-confirmed counts: Regular 182, then 5 more
  that arrived mid-unit, 187 total; Premium 10. Gift
  Level 28 unchanged, progress 180,734,910 to
  180,779,650 of 206,300,000 across the three claims.
- Regular points exact in a quiet window: the first
  Regular claim moved progress 180,734,910 to
  180,736,730, exactly 182 x 10. Premium visible rows:
  R +50 (Daily Sale Transfer Pack), SR +100 (Daily
  Premium Transfer Pack), R +50 (Advanced Training
  Pass), SSR +200 (Premium Training Pass); the other 6
  claimed premium rows sat below the fold and their
  per-gift points are unverified.
- Counter anomaly, filed as Issue #183: the Premium
  window delta (+35,580) and the second Regular window
  delta (+7,340, against 5 x 10 = +50 expected) both
  exceed this unit's own claims in those windows. The
  progress counter is therefore NOT attributable to
  the unit's own claims during an active window - the
  claimed counts are governed by the summary dialogs,
  not the counter. Leading hypothesis, unverified:
  the counter is alliance-shared and concurrent ally
  claims moved it (allies were demonstrably active -
  new gifts arrived every minute); alternative: an
  unmeasured high-value premium tier (a partly visible
  MR row sat below the fold). Earlier quiet-window
  units matched exactly, which favours the concurrent
  activity hypothesis. The list scroll and drag both
  produced no view change and were retired inside the
  unit per queue rule R2, so below-fold rows are not
  re-read that way.
- Completion sweep rule confirmed: after the first
  claims, the Regular tab showed a fresh red dot - 5
  new Regular gifts (LAMP 1 defeating Doom Elites, +10
  each) - and a second Claim All cleared them; both
  tabs showed no red dot and no Claim All button at
  close. Re-check both tabs after claiming; gifts keep
  arriving mid-unit.
- Entry and claim points re-confirmed, not just
  reused: Alliance 903,731, Gifts 303,595, Regular
  Claim All 498,952, Premium Claim All 763,952 - the
  same points the 0817 unit measured.


## What the 2026-11-02 1801 scout read added

- Observe-only scout read, not a gifts claim: unit
  scout-midday-scout-mid-2026-10-31-002 by ticker-1755,
  session about 17:58 to 18:01, status partial. Evidence in
  `_records_/2026-11-02/perception-scout/1801-queue-run.md`.
- Gift Level 28, progress 181,429,280 of 206,300,000 read
  live about 18:00 (measured value). Regular tab selected,
  Premium tab carrying a red dot, Claim All button badge
  201, visible Regular rows +10 each (PrincessEsra10xoxo
  Defeated Doom Elite 23:51:32; Niermeat 23:40:52; Niermeat
  23:4x partially obscured; Niermeat 23:28:11; further rows
  below the fold, not read). Nothing claimed - the gifts
  regular owns claims.
- Counter movement with no intervening own claim, new
  evidence for Issue #183: no gifts unit ran between the
  1215 close (progress 180,779,650) and this 18:00 read
  (181,429,280), yet the counter rose 649,630. Movement
  with zero intervening own claims excludes an
  own-claims-only attribution of the counter and is
  consistent with the alliance-shared-counter hypothesis;
  the below-fold premium-tier alternative cannot explain
  movement with no own claims in between. The hypothesis
  stays unverified - the counter's exact sharing rule is
  still unmeasured - but the 1215 anomaly is no longer a
  single-unit curiosity: the counter moves without this
  account claiming. Evidence commented on Issue #183 by
  this run.


## What the 2026-11-02 2018 unit added

- Unit gifts-2026-11-02-1830 by ticker-2004, session
  about 20:13 to 20:18, status done. Dialog-confirmed
  31 Regular and 3 Premium, 34 total, target 34
  achieved 34, about 5 minutes. No diamonds spent, no
  purchase made, nothing deleted. Evidence in
  `_records_/2026-11-02/alliance-gifts/2018-queue-run.md`.
- Entry, measured fresh this unit: Alliance button
  grounded at norm 882-980,652-722 (centre 931,687) on
  the base screen; Alliance Gifts button grounded at
  norm 134-493,576-653 (centre 313,614) on the
  Alliance panel, carrying a red dot.
- Gift level read live at entry: Level 28, progress
  181,714,890 of 206,300,000. Regular tab: Claim All
  badge 31; the summary dialog read "A total of 31
  Regular Alliance Gifts were claimed this time".
  Progress after: 181,715,610 (plus 720). Premium tab:
  Claim All badge 3; the summary dialog read "A total
  of 3 Premium Alliance Gifts were claimed this time".
  Progress after: 181,715,830 (plus 220). In-unit
  total plus 940.
- Counter movement with no intervening own claim,
  further evidence for Issue #183: no gifts unit ran
  between the 1801 scout read (181,429,280 about
  18:00) and this unit's entry (181,714,890), yet the
  counter rose 285,610. Evidence commented on Issue
  #183 by this run, since the record itself does not
  mention #183.
- Regular Claim All centre 494,938 re-confirmed
  (against 498,967 from the 2122 unit). Premium Claim
  All lesson: the first tap reused the Regular-tab
  button centre (494,938) but the Premium layout puts
  Claim All at the right, so the tap landed on the
  "Hide your name on Gifts" area and nothing changed
  - one no-change tap, method pivoted per queue rule
  R2. Claim All re-grounded at norm 600-891,889-977
  (centre 745,933) and pressed. Premium Claim All
  points now measured at 718,967 (2122), 763,952
  (0817) and 745,933 (2018): layout-dependent, so
  re-ground each unit and never reuse the Regular
  centre.
- Verification: the Premium list re-read shows the 3
  gifts (Coin Weekly Pass R, Drone Components Weekly
  Pass R, Diamond N) all marked Claimed and the Claim
  All badge gone. On exit the Alliance Gifts red dot
  on the Alliance panel is gone.
- Exit miss, recovered: the Alliance panel back arrow
  sits further right (norm 120,939) than the Mail
  screens arrow (norm 58,939); one tap at 58,939 did
  nothing, the tap at 120,939 returned the game to the
  base screen. Back-arrow positions are panel-specific.


## What the 2026-11-02 2305 unit added

- Unit gifts-2026-11-02-2230 by ticker-2304, session
  about 23:05 to 23:10, status done. Evidence in
  `_records_/2026-11-02/alliance-gifts/2305-queue-run.md`.
- Opened the Alliance panel from the base and tapped
  Alliance Gifts (entry carried a red dot). Gift
  Level 28 throughout. Progress bar read live at each
  step: 182,891,070 of 206,300,000 at entry.
- Regular tab, first Claim All: badge 40, dialog "A
  total of 40 Regular Alliance Gifts were claimed
  this time". Progress after: 182,891,480 of
  206,300,000 (plus 410 for 40 gifts, about 10 each,
  matching the 1215 Regular window).
- Premium tab, first Claim All: button badge read 82,
  dialog "A total of 62 Premium Alliance Gifts were
  claimed this time". Progress after: 182,998,450 of
  206,300,000. The badge read (82) and the dialog
  count (62) differ by 20; both are recorded as read
  and the difference is unexplained, not derived
  away. This badge-versus-dialog gap is new evidence
  for the gift-counting anomaly tracked as Issue
  #183, commented there by this run.
- Re-sweep, Regular tab: badge 6, dialog 6 Regular
  gifts claimed. Progress after: 182,999,710 of
  206,300,000 (plus 1,260 for 6 gifts, 210 each -
  against about 10 each in the first Regular window,
  so the per-gift progress movement is not stable
  within one tab in one unit; further #183 evidence).
  All Regular rows read Claimed and the Regular
  Claim All badge cleared.
- Re-sweep, Premium tab: badge 2 (one SSR, one R),
  dialog 2 Premium gifts claimed. Progress after:
  183,001,720 of 206,300,000. All Premium rows read
  Claimed and the Premium Claim All badge cleared.
- Totals: Regular claimed 46 (40 plus 6), Premium
  claimed 64 (62 plus 2), total 110 gifts. Gift level
  progress 182,891,070 to 183,001,720 of 206,300,000
  (plus 110,650 over the unit, as read live at each
  step). Both tabs were verified badge-clear at
  close. Gifts keep arriving while allies play, so
  the zero-badge state is momentary by the
  activity's own note, not a permanent clear.

## Open questions

- What raises the gift level, and what each level unlocks.
- What the 844 figure in the morning claim counted.
- Whether unclaimed gifts expire.

## Changelog

- 1.3.0 (2026-11-01): measured 0110 entry and per-tab Claim
  All points, dialog-confirmed counts (47 Regular, 8 Premium
  across two sweeps), the badge-versus-dialog arrival gap,
  the 500,850 dismiss behaviour, the two-sweep rule, and the
  Chrome-frontmost background-input nuance, folded from the
  0110 gifts unit.
- 1.4.0 (2026-11-01): measured 0935 entry and per-tab Claim All points, dialog-confirmed counts (222 Regular, 18 Premium), first successful execution after the device-offline run, and the title-bar-then-retry entry reconciliation, folded from the 0935 gifts unit.
- 1.5.0 (2026-11-01): dialog-confirmed counts (22 Regular,
  3 Premium, 25 total) with the badge-versus-dialog arrival
  gap repeated, the Premium tab no-change first tap at
  700,250, the SSR 200 and MR 1000 point values, and the
  re-check re-entry that caught a newly arrived gift,
  folded from the 1221 gifts unit.

- 1.6.0 (2026-11-01): dialog-confirmed 4 Regular and 0
  Premium, the entry correction (Alliance 929,688;
  Gifts 313,621; first tap landed on the Alliance Wars
  rally screen), the device-takeover Confirm once with
  no second dialog, the progress delta explicitly not
  attributed to the 4 gifts, and Premium all-Claimed
  with no Claim All offered, folded from the 1718 gifts
  unit.

- 1.7.0 (2026-11-01): dialog-confirmed 221 Regular and 70 Premium, Gift Level 28 progress 179,652,510 to 179,664,120 of 206,300,000, the OCR-over-screenshot-estimate panel-button lesson, and the right-shifted Premium Claim All point (718,967) versus the centred Regular point (498,967), folded from the 2122 gifts unit.

- 1.8.0 (2026-11-02): dialog-confirmed 45 Regular and 5 Premium, Gift Level 28 progress 179,803,870 to 179,805,720 of 206,300,000, the title-bar 30-pixel offset correction (Gifts 313,595, not 536), and the Alliance star icon centre 941,701, folded from the 0023 gifts unit.

- 1.9.0 (2026-11-02): dialog-confirmed 54 Regular and 12 Premium, Gift Level 28 progress 180,150,630 to 180,153,970 of 206,300,000, Alliance base icon 934,707 and Gifts button 313,595 re-grounded, folded from the 0338 gifts unit.

- 1.10.0 (2026-11-02): dialog-confirmed 1 Regular (+10) and 1 Premium (+50), Gift Level 28 progress 180,508,620 to 180,508,680 of 206,300,000, Alliance Wars row at y 509 versus the Gifts row at y 595 with the 303,595 corrected tap, Premium Claim All at 763,952 against the 2122 unit's 718,967, and the no-change back-arrow exit, folded from the 0817 gifts unit.

- 1.11.0 (2026-11-02): dialog-confirmed 187 Regular (182 plus 5 mid-unit arrivals) and 10 Premium, Gift Level 28 progress 180,734,910 to 180,779,650 of 206,300,000, the exact 182 x 10 Regular window, the visible premium rows R 50, SR 100, R 50 and SSR 200, the counter anomaly filed as Issue #183 with the alliance-shared-counter hypothesis, the below-fold scroll and drag retired per rule R2, and the completion sweep that caught 5 mid-unit arrivals, folded from the 1215 gifts unit.

- 1.12.0 (2026-11-02): Gift Level 28 progress 181,429,280 of 206,300,000 read live about 18:00 by the observe-only 1801 scout unit (Claim All badge 201, Premium tab dotted, nothing claimed), and the 649,630 counter rise since the 1215 close with no intervening gifts unit, folded as new evidence for Issue #183.

- 1.13.0 (2026-11-02): dialog-confirmed 31 Regular and 3 Premium, Gift Level 28 progress 181,714,890 to 181,715,830 of 206,300,000 (plus 940 in-unit), the 285,610 counter rise since the 1801 scout read with no intervening gifts unit as further Issue #183 evidence commented by this run, the Premium Claim All point 745,933 against 718,967 and 763,952 so the point is layout-dependent and the Regular centre must never be reused, the panel-specific Alliance back arrow at 120,939, and the Premium re-read verification, folded from the 2018 gifts unit.

- 1.14.0 (2026-11-02): dialog-confirmed 46 Regular and 64 Premium (110 total), Gift Level 28 progress 182,891,070 to 183,001,720 of 206,300,000 (plus 110,650 in-unit), Premium badge 82 against dialog 62 as a new badge-versus-dialog gap, Regular re-sweep plus 1,260 for 6 gifts against about 10 each in the first window so per-gift progress movement is unstable within one tab, both tabs verified badge-clear at close with the zero-badge state momentary, and the anomaly evidence commented onto Issue #183 by this run, folded from the 2305 gifts unit.
