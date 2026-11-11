---
title: Mail Rewards
created: 2026-10-25T18:58:00Z
modified: 2026-11-11T11:32:17Z
level: L1
version: 1.37.0
description: Claiming reward mail and checking report mail, one activity folder for mail knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner structure direction on activity folders, 2026-10-25
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1306 mail unit)
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1730 mail unit)
  - source: mail-rewards execution record 2026-11-01 2131 queue run (ticker-2104 unit, partial, Alliance-panel back arrow stalled on background input)
  - source: ticker-0034 mail-rewards execution record 2026-11-02 0042 queue run
  - source: ticker-0334 mail-rewards execution record 2026-11-02 0343 queue run (done, System 50 diamonds)
  - source: ticker-0834 mail-rewards execution record 2026-11-02 0840 queue run (done, all claimable categories answered No rewards available)
  - source: mail-rewards execution record 2026-11-02 1226 queue run (ticker-1204 unit, done, all categories swept, no reward available)
  - source: mail-rewards execution record 2026-11-02 2012 queue run (ticker-2004 unit, done, 7 mails claimed)
  - source: mail rewards execution record 2026-11-02 2313 queue run
  - source: ticker-0304 mail-rewards execution record 2026-11-03 0312 queue run (done, all categories empty, Escape crash recurrence)
  - source: ticker-0704 mail-rewards execution record 2026-11-03 0715 queue run (done, six categories swept, all answered No rewards available)
  - source: ticker-1034 mail-rewards execution record 2026-11-03 1055 queue run (partial, mail entry mis-targeted to Alliance twice then no-change, Issue 230)
  - source: ticker-1734 mail-rewards execution record 2026-11-03 1740 queue run (done, R2 fresh grounding opens Mail first try, Alliance Exercise claim, red dot is unread not claimable)
  - source: ticker-0204 mail-rewards execution record 2026-11-04 0212 queue run (done, Alliance claim verified by checkmarks, Regular notices already credited, notifications prompt declined, Issue 230)
  - source: ticker-0434 mail-rewards execution record 2026-11-04 0445 queue run (done, category rows grounded, Event train arrival reward claimed and verified gone)
  - source: ticker-0804 mail-rewards execution record 2026-11-04 0817 queue run (done, checked only, Claim All no-change in four categories, Event notice opened individually, no claimable mail)
  - source: ticker-1327 mail-rewards execution record 2026-11-04 1333 queue run (failed, Mac screen-capture channel failure on every capture step, no game input dispatched, second consecutive ticker pass to fail this way after help 1235, Issue 282)
  - source: ticker-0134 survivor-intake execution record 2026-11-05 0134 queue run and ticker-0204 alliance-gifts execution record 2026-11-05 0204 queue run (windowed 1920x1080 on an inactive Space, not native fullscreen - corrects the 1333 section wording)
  - source: ticker-1025 mail-rewards execution record 2026-11-05 1025 queue run (failed, Mac device offline, forty-second consecutive pass, zero-response form, Issue 284)
  - source: ticker-1804 mail-rewards execution record 2026-11-05 1804 queue run (failed, Mac device offline, fifty-seventh consecutive ticker pass with a Mac device-access blocker, eighteenth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 10h30m, unchanged since the 1025 pass; seven invokes, zero responses)
  - source: ticker-1727 mail-rewards execution record 2026-11-07 1740 queue run (done, all six claimable categories checked, nothing claimable; record commit 69997e12a1 on records/2026-11-07)
  - source: ticker-2006 mail-rewards execution record 2026-11-07 2028 queue run (done, Alliance Daily Donation Rankings and 3 Event mails claimed, other categories clear by list read, verified clean after claims; record commit e9bf320c92 on records/2026-11-07)
  - source: ticker-2034 mail-rewards execution record 2026-11-07 2052 queue run (done, Alliance and Event Claim All answered "No rewards available", nothing claimed, envelope grounded at norm 936,790, "Unclaimed -Daily Task- Reward" is notification-only; record commit 7a4a104930 on records/2026-11-07)
  - source: ticker-2119 mail-rewards execution record 2026-11-08 2132 queue run (done, Alliance and Event mail claimed in full, 10 mails, Claim All both categories; record commit fe08a0907 on records/2026-11-08)
  - source: ticker-0113 mail-rewards execution record 2026-11-09 0138 queue run (partial, Alliance and Event Claim All both "No rewards available", System/Regular/Battle Report not walked, leader row Jerry Apex read live on the Alliance page, Mail button flaky entry (652,793), VIP daily freebie flag; record commit c0ebf0c4f0 on records/2026-11-09)
  - source: ticker-0404 mail-rewards execution record 2026-11-09 0421 queue run (done, all three red-dot categories walked, no claimable attachments, envelope opened at once with no Alliance-first workaround; record commit 9fdcc4c9ee on records/2026-11-09)
  - source: ticker-1004 mail-rewards execution record 2026-11-09 1031 queue run (partial, Event and Alliance Claim All both "No rewards available", six train mails carry no attachments, Battle Report/System/Regular not walked, Mail entry (932,791) windowed first try; record commit 09e4f0863 on records/2026-11-09)
  - source: zero-sweep 001 execution record 2026-11-09 1657 queue run (partial, Mail red dot standing, three categories unopened; record commit c9a86fa74 on records/2026-11-09)
  - source: ticker-1822 mail-rewards execution record 2026-11-09 1838 queue run (done, 9 reward mails claimed, Alliance Event System Claim All, leadership transfer to Abyss Apex, Issue 230 entry datapoint, power 146736949; record commit 6761c35d1 on records/2026-11-09)
  - source: ticker-0134 mail-rewards execution record 2026-11-10 0143 queue run (done, Claim All sweep, no claimable rewards, Weekly Pass mail verified already claimed; record commit e3d186a38 on records/2026-11-10)
  - source: ticker-0334 mail-rewards execution record 2026-11-10 0355 queue run (done, Claim All sweep, no claimable rewards, R5 warning mail read; record commit b7e79a62 on records/2026-11-10)
  - source: ticker-0904 mail-rewards execution record 2026-11-10 0929 queue run (partial, entry blocked by camera framing, Mail panel never opened, fourth unit this reset day with the same blocker, Issue #580; record commit 31892dde on records/2026-11-10)
  - source: ticker-1234 mail-rewards execution record 2026-11-10 1259 queue run (done, Event train rewards claimed in full, mail-list back arrow re-grounded at norm 62,948; record commit 98abbc761 on records/2026-11-10)
  - source: ticker-0212 mail-rewards execution record 2026-11-11 0222 queue run (done, Alliance Daily Donation Rankings and Event Arms Race rewards claimed, both lists verified empty of gift icons; record commit b0615980f on records/2026-11-11)
---


# Mail rewards

## What this activity is

Opening Mail, claiming every claimable reward attachment, and checking
report tabs for anything that needs a decision. This folder accumulates
mail knowledge - tab behaviour, claim flow and recurring reward senders.
Executions are recorded in `_records_/<date>/mail-rewards/`, one file per execution.

## How to enter

- Base screen, Mail button on the right rail (envelope icon).
- Entry, windowed (2026-11-09 1031): the Mail button tap at the freshly grounded centre (932,791) in windowed 642x951 opened Mail at once - windowed background clicks reach the game, unlike the fullscreen Alliance taps in the sibling 1019 help unit. The point still drifts per session, so re-ground fresh each unit (Issue #230).
- The category rail, top to bottom, reads - Battle Report, Alliance,
  Event, Season, System, Regular, In-app Purchases (corrected
  2026-11-01 by the 1730 unit; the earlier list omitted Event and
  named the last category "Purchases"). The train arrival reward mail of
  the daily round was presented as an Event mail in game.
- Every category list ends with Delete All and Claim All buttons.
  Claim All claims every claimable attachment in that category at
  once. Purchases holds receipts only - nothing to claim.
- The back arrow sits at the bottom left of the mail screens, both in
  the category list and inside an open mail. (2026-11-10 1259 update: the mail-list back arrow's true centre in the 642x951 window is (62,948) - taps at (57,902), (40,900), (55,925) and (40,955) all missed high, the button sits at about y 869-935 px, centre about y 902 px; measure the centre fresh from a screenshot crop in each unit. The AX tree carries no back-button element (game canvas), so coordinate taps at the freshly measured centre are the working route; keyboard input is unavailable in this app - focus belongs to the other LastWar window.)

## Cadence

- Checked every round - the mail regular on `_tools_/regulars.json`.

## Scope and availability

- Claiming attachments is in scope. Deleting mail is never done;
  Delete All is never pressed.

## What is known from 2026-10-25

- Alliance and Event tabs held claimable rewards and were claimed in full.
- System and Regular held no claimable attachments that day.
- One claimed Alliance mail was the Alliance Exercise reward dated
  2026-10-24 16:31:06 as displayed.
- The late run at 21:20 pressed Claim All in Alliance, Season,
  System, Regular and Battle Report; the only visible effect was in
  Alliance, where a Weekly Donation Ranking mail left the list - the
  other categories held reports only (Ice Breaking reports under
  Season, patch notes under System, battle reports under Regular and
  Battle Report). A Storm Arena gift mail opened in detail showed its
  reward icons (20 and 100 as displayed) with no claim button after
  Claim All, consistent with the attachment already taken.
- A System patch-notes mail dated 2026-10-21 announced - Added the
  Crystal Shop tab to Store, Building section - the only in-game
  mention of anything crystal found so far (see the open question in
  `_activities_/daily-activities`).

## What is known from 2026-11-01

Measured in the 0139 mail unit (ticker-0134, window mode
642x951, no different-device dialog). Outcome: partial - no
mail was claimed, nothing was deleted, tracker untouched, so
the next tick re-produces this regular as a fresh unit.

- From the Alliance menu left open by the previous unit,
  the Help panel was closed and the Alliance menu back arrow
  returned to the base screen. The base screen showed the
  Mail envelope button on the right rail with a red dot, so
  claimable mail may exist - unverified, not claimed.
- Mail entry failed in this unit. Four input variants at the
  freshly measured Mail point (normalised 920-929, 755-760)
  all showed no change on a second observation each time:
  two standard clicks, one exact-pointer click with control
  snapping off, and one 1-second long press. The game stayed
  on the base screen and no Mail panel opened.
- Contrast, same pass: background input to panel screens
  worked (Alliance Gifts back arrow, Alliance menu Help
  tile, Help All, panel close and menu back arrow). The
  blocker is specific to the base-screen right rail in this
  background-input mode, not to game input in general.
- Blocker for the next mail unit (queue rule R2): the
  base-rail Mail entry method is exhausted for this unit.
  The next unit must arrive with a changed method - a
  foreground game window or a different entry route -
  before repeating the rail tap. Do not spend another unit
  on four more identical rail variants.



## What the 2026-11-01 1306 unit added

- Unit mail-2026-11-01-1030 by ticker-1304, session
  about 13:06 to 13:20, status done. The game was left on
  a Gold Brick Mall tutorial popup over the Mall screen;
  the popup was closed with its X, the Mall back arrow
  returned to the base screen, and no price tag or paid
  button was tapped.
- Mail entry, blocker resolved by fresh grounding: two
  taps at the earlier measured base-rail point
  (normalised 900-902, 755-757) showed no change, the
  same blocker the 0139 unit recorded. A fresh visual
  grounding put the Mail envelope at normalised 915,
  790, and a tap there opened Mail. Method rule under
  queue rule R2: measure the Mail icon fresh in each
  unit, do not reuse the 755-760 point. This refines
  the 0139 instruction, which framed the base-rail
  method as exhausted pending a foreground window or a
  different entry route: the stale point was exhausted,
  not the rail tap itself, and fresh grounding in the
  current window sufficed.
- Alliance: Claim All claimed the [Alliance Exercise]
  Alliance reward mail (3h ago). Congratulations popup
  read: EXP 105.8M, 50.0K, 4.6K, 5m speedups 12, 21, 41,
  26 and 20, coins 12.1M, food 19.0M, iron 19.0M. The
  mail's gift icon was gone afterwards. Remaining
  Alliance mails were markers and the Daily Donation
  Rankings report, nothing further claimable.
- Event: Claim All claimed the train arrival and event
  reward mails. Congratulations popup read: chests 3
  and 100, 2.5K medal 1, 100 gem 1, 8.5K, 5m speedups
  10, 9, 5, 4 and 12.
- Battle Report, Season, System and Regular were
  checked in turn: Battle Report held scout reports and
  Lv.17-20 Zombie Horde victory reports, Season held
  Ice Breaking reports, System held President mails and
  a Maintenance Completed notice, Regular held Invading
  Zombies victory reports. No claimable attachment was
  found in any of them; Claim All in Battle Report
  produced no popup and no change.
- Nothing was deleted. Delete All was never pressed. No
  other task type was touched. The pass ended at the
  base screen.
- Cross-unit confirmation, not a new claim: the 1324
  star-ceremony unit's base resource bar read food
  308.2M (was 289.2M), iron 496.2M (was 477.2M), coins
  22.7M (was 10.6M) - deltas of +19.0M, +19.0M and
  +12.1M, matching this unit's popup exactly, so the
  claims landed.

## What the 2026-11-01 1730 unit added

- Status partial: unit mail-2026-11-01-1430 by
  ticker-1704, third unit of the pass, session about
  17:23 to 17:31. No mail claimed, nothing deleted.
  Tracker untouched; the next tick re-produces the mail
  regular and the claim sweep resumes as a fresh unit.
- Navigation cost, measured: the Help dialog close X
  measured at norm 840,213 (an earlier tap at 888,219
  missed), and the Alliance panel back arrow measured
  at 162,934 (an earlier tap at 62,936 hit the small
  avatar below it instead). The unit reached Mail
  through the Alliance-panel exit path after the help
  unit; the pass budget (about 25 minutes from token
  taken at 17:06) ran out before any category was
  opened or any Claim All pressed. Next-unit lesson: a
  mail unit that inherits the Alliance-panel exit path
  pays this navigation cost first - entering Mail from
  the base rail is the cheaper route when the unit
  starts fresh.
- Category list corrected, read live: Battle Report,
  Alliance, Event, Season, System, Regular, In-app
  Purchases. No category showed a red dot. This
  corrects the profile's rail list, which omitted Event
  and named the last category "Purchases": Event sits
  between Alliance and Season, and the last category
  reads "In-app Purchases". The 1306 note that the
  train arrival reward mail was presented as an Event
  mail is consistent with Event being a full category,
  not a one-off label. No-red-dot here is a
  category-list read only - no category was opened, so
  no claimable mail is ruled in or out by this unit.
- Nothing was deleted. Delete All was never pressed. No
  other task type was touched.

## What the 2026-11-01 2131 unit added

- Partial, mail screen never reached: unit
  mail-2026-11-01-1830 by ticker-2104, fourth unit of the
  same pass after the training partial, gifts done and
  help done. The unit reached the Alliance panel (after
  closing the Help dialog from the previous unit with its
  X) but the panel's bottom-left back arrow took three
  no-change taps in a row - norm 55,964, then 97,964
  twice, the last after a fresh activate - and the panel
  stayed open each time, confirmed by screenshots.
- Under queue rule R2 (foreground precondition, retro of
  2026-10-31) two no-change taps end the background-input
  method inside the unit, so tapping stopped instead of
  repeating: the game window stays covered by Chrome and
  background input stopped reaching this control. A
  click_foreground attempt was refused for missing
  element_number, and no Escape key was used (it has
  crashed this app before). No foreground route was
  available inside this unit.
- Outcome discipline: no mail category was opened,
  nothing was claimed, and Delete All was never touched.
  Tracker untouched, so the next tick re-produces the
  regular. Note for the next mail unit: try the panel
  exit first with a fresh observation, and if the back
  arrow stalls again, treat it as the known foreground
  precondition rather than a dead entry route - earlier
  units the same day recovered from it. This also
  re-affirms the 1730 lesson: a mail unit that inherits
  the Alliance-panel exit path pays this navigation cost
  first, and entering Mail from the base rail is the
  cheaper route when the unit starts fresh.
  Evidence in `_records_/2026-11-01/mail-rewards/2131-queue-run.md`.



## What the 2026-11-02 0042 unit added

- Unit mail-2026-11-01-2230 by ticker-0034, session about
  00:39 to 00:42, status done. Entry: from the Alliance
  menu left by the help unit, the Alliance panel back
  arrow stalled twice on background input at norm 45,965
  and 55,967, then the proven point norm 162,934 returned
  to the base screen. Note the screen-dependence: 45,965
  served as a working back arrow in the 2026-11-01 0940
  help entry, but stalled here - when the panel back arrow
  stalls, try the proven 162,934 point before concluding
  the exit is blocked. The Mail envelope on the right
  rail opened Mail at norm 931,791.
- Category list, read live: Battle Report, Alliance,
  Event, Season, System, Regular, In-app Purchases -
  consistent with the corrected list. Gift icons
  (claimable attachments) showed only on Alliance and
  Event. Regular and In-app Purchases carried red dots
  only, no gift icons; the other categories showed
  neither. Lesson: a red dot on Regular or In-app
  Purchases is not a claim signal - only a gift icon
  marks a claimable attachment.
- Alliance: Claim All pressed at norm 766,946. The gift
  icons on Daily Donation Rankings (6h ago) and Weekly
  Donation Ranking (6h ago) were gone on the re-read;
  the rows remained as read mail. Event: Claim All
  pressed at the same point. The gift icons on Season
  Rewards (3h ago), Season Settlement - Faction Rewards
  (6h ago) and Arms Race Ranking Reward (6h ago) were
  gone on the re-read; the train mails above them were
  reports with red dots only. Totals: 5 mails with gifts
  claimed (2 Alliance, 3 Event). Nothing deleted.
  Evidence in `_records_/2026-11-02/mail-rewards/0042-queue-run.md`.

## What the 2026-11-02 0343 unit added

- Unit mail-2026-11-02-0230 by ticker-0334, session
  about 03:40 to 03:43, status done. Every claimable
  category was Claim All swept; one reward was
  claimed. Delete All was never pressed.
- By category: Event, two unread mails (red dot) -
  "[AP3x] Abuss Apex's Mega Exp..." and "[AP3x]
  Missile Apex's train has...", both 1h ago - Claim
  All answered "No rewards available.", both mails now
  read. Regular, battle reports (Victory vs Lv.160
  Doom Walker and Invading Zombies) - "No rewards
  available." Alliance, Weekly Donation Ranking,
  Daily Donation Ranking and New Alliance Marker
  mails - "No rewards available." Season, Ice Breaking
  Reports only - "No rewards available." System,
  Season Conclusion and (President Mail) items -
  Claim All produced a REWARD CLAIMED dialog showing
  50 diamonds, the unit's only claim. Battle Report,
  scout reports and Victory vs Lv.17 to Lv.20 Zombie
  Horde reports - Claim All pressed, no reward dialog
  appeared and the list was unchanged, no claimable
  attachment. In-app Purchases was not swept: it holds
  receipts only, per the activity metadata, and its
  red dot is unread receipts, not rewards.
- System is therefore claim-bearing in this unit, not
  report-only: the 50-diamond System claim is the
  first System claim recorded since the 2026-10-25
  note that System held no claimable attachments that
  day. The gift-icon rule from the 0042 unit still
  governs which rows are swept - Claim All answers
  "No rewards available." where no gift icon stands.
- Back-arrow screen-dependence, new measured point:
  the mail list arrow sits at normalized (64,952),
  while the Alliance panel arrow measured (163,935)
  - essentially the 0042 unit's (162,934) point, within
  rounding. Re-ground per screen, never reuse a
  back-arrow point across screens.
  Evidence in `_records_/2026-11-02/mail-rewards/0343-queue-run.md`.


## What the 2026-11-02 0840 unit added

- Unit mail-2026-11-02-0630 by ticker-0834, session about
  08:37 to 08:40, status done. All claimable mail
  categories swept; no reward was available to claim in
  any of them. Evidence in
  `_records_/2026-11-02/mail-rewards/0840-queue-run.md`.
- Mail entry, fresh grounding again: from the Help page,
  Help and the Alliance panel were closed back to the
  base screen, and a first tap meant for Mail opened the
  Alliance panel instead. The Mail button was re-grounded
  by visual measurement at norm (931,789) on the base
  screenshot (Alliance sits at norm (930,702)), and the
  corrected tap opened Mail. The two buttons share
  almost the same x, separated by only about 87 in y, so
  a mis-grounded Mail tap lands on Alliance; measure the
  Mail icon fresh in each unit, per the 1306 rule.
- Category list at entry: Event carried a red dot,
  In-app Purchases carried a red dot, the other
  categories showed none. Claim All pressed in each
  claimable category, each answered with the toast "No
  rewards available":
  - Event: train mails only (Abyss Apex, Missile Apex,
    Skinner Box trains, 22m to 8h ago); the red dot was
    unread train mail, not a reward.
  - Alliance: Weekly Donation Ranking and New Alliance
    Marker mails only.
  - Season: Ice Breaking reports only.
  - System: President Mail (Warzone 2110) notices only.
  - Regular: battle reports only (Victory over Lv.160
    Doom Walker, Invading Zombies victories).
  - Battle Report: scout reports and Lv.17 to Lv.20
    Zombie Horde victories only.
- Red-dot rule strengthened: a category red dot does not
  prove a reward - it can mean unread non-reward mail, as
  the Event dot here, and In-app Purchases was not
  claimed at all, since it holds receipts only, per the
  activity metadata, and nothing there is claimable.
  Delete All was never pressed in any category.

## What the 2026-11-02 1226 unit added

- Unit mail-2026-11-02-1030 by ticker-1204, session
  12:21 to 12:26, status done. All claimable categories
  swept; no reward was available in any of them.
  Evidence in
  `_records_/2026-11-02/mail-rewards/1226-queue-run.md`.
- Claim All pressed in Event, Alliance, Season,
  System, Regular and Battle Report, each answered
  "No rewards available". Contents repeat the 0840
  inventory exactly: train mails under Event, Weekly
  Donation Ranking and New Alliance Marker mails
  under Alliance, Ice Breaking reports under Season,
  President Mail (Warzone 2110) notices under System,
  battle reports under Regular, scout reports and
  Lv.17 to Lv.20 Zombie Horde victories under Battle
  Report. No new sender type appeared.
- In-app Purchases was not claimed: it holds receipts
  only, per the activity metadata, and its red dot is
  unread receipts, not a reward - re-confirming the
  0840 red-dot rule. Delete All was never pressed in
  any category. The game was left on the Mail
  category list.
- Back-arrow grounding lesson: from the Help page,
  the Help X at norm 877,210 closed Help to the
  Alliance panel, and a first panel back-arrow tap at
  norm 55,949 missed the button's centre and produced
  no change; the corrected centre at norm 117,946
  worked first try, and the same point then worked as
  the mail back arrow. Measure the back arrow's centre
  fresh in each unit; 55,949 is not a fixed point.
- Bounded re-press rule: the first System Claim All
  tap's toast was not captured in its receipt, so
  Claim All was pressed a second time and the toast
  was then read live - no further tap after
  confirmation. Re-press only until the answer is
  confirmed, then stop.
- Entry point re-confirmed: Mail at norm 931,789,
  the re-grounded point from the 0840 unit, opened
  Mail (Alliance sits at 930,702).


## What the 2026-11-02 2012 unit added

- Unit mail-2026-11-02-1830 by ticker-2004, session
  about 20:05 to 20:12, status done. 7 mails claimed,
  target 7 achieved 7, about 7 minutes. No diamonds
  spent, no purchase made, nothing deleted. Evidence
  in `_records_/2026-11-02/mail-rewards/2012-queue-run.md`.
- Entry correction: the right-rail icon first grounded
  as mail at norm 978,290 opened the Store Coupon Store
  page instead - a wrong entry, not the Mail button.
  The back arrow at norm 119,937 returned the game to
  the base screen with nothing bought. The true Mail
  button was then grounded at norm 885-978,740-823
  (centre 931,781, matching the standing record) and
  opened Mail. Lesson: 978,290 is the Coupon Store
  entry, not Mail; re-ground Mail fresh rather than
  trusting the first right-rail icon.
- Category list, read live at entry: gift icons
  (claimable attachments) on Alliance and Event only.
  Battle Report, Season and System showed neither gift
  icon nor red dot; Regular and In-app Purchases
  carried red dots only (reports and receipts,
  nothing claimable) - re-confirming the red-dot rule.
- Alliance: 4 mails with gift icons, all 2h ago -
  Daily Donation Rankings, Zombie Siege Report
  (Alliance), Zombie Siege Report (Individual),
  Defense Success Reward (Zombie). Claim All at norm
  749,949 pressed; re-read shows all 4 gift icons gone
  and the rows greyed as read. The two Zombie Siege
  Reports and the Defense Success Reward (Zombie) are
  new against the 1226 inventory. Nothing deleted.
- Event: 3 mails with gift icons, all 2h ago - Arms
  Race Ranking Reward, Unclaimed VIP Daily Level
  Reward, Unclaimed "Daily Task" Reward. Claim All at
  norm 749,949 pressed; re-read shows all 3 gift icons
  gone and the rows greyed as read. Title Assignment
  (1h ago), Daily Participation Rewards (2h ago) and
  Event Task EXP Reissue (2h ago) carried no gift icon
  and were left untouched. Nothing deleted.
- Navigation miss, recovered: the first tap on the
  Event row (norm 500,315) did not navigate; a second
  tap at the row centre (norm 500,334) opened Event.
  No repeat of the failed point.
- Mail closed back to the base screen with the
  category back arrow twice. No different-device
  dialog was seen in this unit.


## What the 2026-11-02 2313 unit added

- Unit mail-2026-11-02-2230 by ticker-2304, session
  about 23:13 to 23:19, status done. 0 rewards
  claimed, 0 mails deleted. Evidence in
  `_records_/2026-11-02/mail-rewards/2313-queue-run.md`.
- Mail category list at entry carried red dots on
  Battle Report, Alliance, Event, Regular and In-app
  Purchases. Season and System carried none.
- Claim All pressed in every category except In-app
  Purchases (receipts only, nothing to claim, per
  the activity metadata): Alliance, Event, Regular,
  Battle Report and Season each answered "No rewards
  available." Alliance list held Voting Results
  (unread, 2h ago, "Do you read the
  Announcements?"), Daily Donation Rankings, Zombie
  Siege Reports and a Defense Success Reward, all 5h
  or older. Event list held train departure notices,
  a Competition Item Expired notice, a Daily
  Participation Reward and a Race Ranking Reward row.
  Regular list held Victory reports (Lv.60 Doom
  Elite, Lv.160 Doom Walker, Lv.55 Doom Elite).
  Battle Report list held attack Victory reports
  (Lv.20 Zombie Raider, Lv.19 to Lv.16 Zombie
  Horde). Season list held Ice Breaking Reports only.
- System: Claim All pressed twice, no toast captured
  either time and the list unchanged (President
  Mails, Season Conclusion). Per queue rule R2 the
  method ended there; the honest read is no
  claimable attachment observed in System, not a
  captured "No rewards" toast. A System no-toast
  read must not be written up as a toast.
- Delete All was never pressed in any category. The
  Alliance Voting Results mail was left unread: it
  is a results announcement, not a claimable reward,
  and opening it was not needed to close this unit.
  Its unread state is why the Alliance category dot
  may persist - an unread announcement, not an
  unclaimed reward, keeps the dot.
- In-app Purchases was not opened: receipts only,
  nothing to claim.
- Mid-unit incident, do-not-reuse point: leaving
  the Alliance panel for the base, a tap grounded by
  visual grounding at (162,935) quit LastWar
  outright (app-exited evidence). The tap was not
  repeated. The game was relaunched with open_app
  plus activate, recovered with state intact at the
  base screen (power 149,940,141), and the mail unit
  continued from the base Mail button. Background
  input worked while Chrome stayed frontmost for the
  rest of the unit.
- On returning to the base at the end of the unit, a
  notification permission dialog appeared ("Enable
  notifications and never miss important messages
  again."). Cancel was tapped; Enable Now was not
  touched and no system setting was changed.


## What the 2026-11-03 0312 unit added - all categories empty, Escape crash recurrence

- Ticker-0304, unit mail-2026-11-03-0230, about 03:12
  local, status done. Evidence in
  `_records_/2026-11-03/mail-rewards/0312-queue-run.md`.
- Claim All pressed in every mail category, one at a
  time. Each answered "No rewards available": Event (the
  only claimable category carrying a red dot on entry),
  Alliance, Season, System, Regular, Battle Report, and
  In-app Purchases (receipts only, as recorded in the
  activity metadata; its red dot was receipts, not
  rewards). A red dot on a mail category is therefore
  not by itself a claimable reward: the Event category
  carried a red dot and still answered No rewards
  available.
- 0 rewards claimed, 0 mail deleted. Delete All was
  never pressed in any category.
- Reaching Mail, Escape crash recurrence: the Alliance
  panel back arrow took three background taps with no
  change, so the Esc key was tried and the game app
  quit. Esc is a known crash trigger for this app and
  must not be used again; this unit re-affirms the ban
  in this profile as well as in event-claims. The app
  was reopened with open_app, returned to the base
  screen with no takeover dialog, and Mail was then
  opened from the base right rail and swept normally.
  The gifts and help units completed before this
  incident were unaffected.

## What the 2026-11-03 0715 unit added - six categories swept, all empty, Battle Report double-tap

- Ticker-0704, unit mail-2026-11-03-0630, about 07:10
  to 07:15 local, status done. Evidence in
  `_records_/2026-11-03/mail-rewards/0715-queue-run.md`.
- From the base screen, Mail opened to the category
  list: Battle Report, Alliance, Event (red dot),
  Season, System (red dot), Regular, In-app Purchases.
  The game was left on the base screen at the close.
- Every claimable category was swept with its Claim All
  button (Delete All never pressed), each answering
  "No rewards available" live: Event (train arrival
  notices only, [AP3x] Sanction, [AP3x] Abyss Apex,
  [AP3x] KpyKat, 1h to 9h ago); System (Planned Update
  Notice 3h ago, President Mail purge request and
  conclusion 1d ago, correction and greeting mails);
  Alliance (announcements 10h ago, Daily Donation
  Rankings, Zombie War Report, Defense Success Reward
  (Zombie), Daily Donation Ranking - one Rankings row
  was not re-read by OCR in the post-tap observation,
  but the Claim All answer was "No rewards available",
  so nothing is recorded as claimed there); Season (Ice
  Breaking Reports from [AP3x] Abyss Apex, 6d ago);
  Regular (Victory battle reports: Lv.60 Doom Elite,
  Lv.160 Doom Walker, Lv.55 Doom Elite); Battle Report
  (Victory in Attack against RebelNova, 1,770 units
  defeated, 12h ago; Lv.20 Zombie Raider and Lv.19,
  Lv.18, Lv.17, Lv.16 Zombie Horde, 13h ago).
- Battle Report method note: the first Claim All tap's
  toast was missed by OCR timing, so Claim All was
  tapped a second time and its "No rewards available"
  answer was read live. When a toast is missed, re-tap
  to confirm the answer rather than assuming it.
- In-app Purchases was not swept: per the activity
  metadata it holds receipts only, nothing to claim.
  Red dots on Event and System again carried no
  rewards, re-affirming that a category red dot is not
  by itself a claimable reward.
- Result statistics: target 6 categories, achieved 6,
  verified yes. Nothing claimed, nothing bought,
  nothing deleted. Costs: 259 seconds, no stamina or
  items spent. Note on the record itself: the unit
  file's evidence path was first written as
  0728-queue-run.md at completion time and corrected
  to 0715-queue-run.md - a record-hygiene note, not a
  play claim.

## Open questions

- Which recurring senders are worth keeping unread as evidence, and which
  reward mails expire if not claimed in time.


## What the 2026-11-03 1055 unit added - mail entry mis-targeted to Alliance twice, then no-change, filed as Issue 230

- Ticker-1034, unit mail-2026-11-03-1030, about
  10:52 to 10:55 local, status partial. Evidence in
  `_records_/2026-11-03/mail-rewards/1055-queue-run.md`.
- Mail entry failed three times from the base view,
  so no mail category was swept and nothing was
  claimed: tap 1 at norm (895,725), measured from
  the training unit restored central frame, opened
  the Alliance panel instead of Mail; tap 2 at norm
  (895,731), measured fresh on the then-current base
  frame (envelope icon visible on the right edge),
  again opened the Alliance panel; tap 3 at norm
  (895,760), aiming lower to allow for a possible
  title-bar offset, produced no visible change (the
  base view stayed, no panel opened). Each Alliance
  panel was closed with its back arrow, returning to
  base. The Alliance panel Help and Alliance Gifts
  red dots were visible while it was open; both
  belong to other units and were left untouched.
- No Claim All was tapped, Delete All was never
  pressed, nothing was claimed, bought or deleted.
  Tracker untouched, per the rule for partial units.
- Rule R2, applied: the method ends inside this unit
  after the repeated misfires; the pass budget also
  ran out during this unit (the pass started at
  10:36), so the sweep could not be retried here even
  with a new method.
- Contrast with the 2026-11-01 rail failure already
  in this profile (four variants, all no-change):
  this failure is a mis-target, not a no-change, so
  the right-edge stack hit mapping itself, not only
  foreground mode, is suspect. Gap filed as Issue
  230 (labels knowledge, play), related entry-drift
  issues 220, 218 and 205.
- Follow-up for the next mail unit: re-measure the
  Mail envelope centre on the live frame before
  tapping, and verify the panel that opens is Mail
  before sweeping any category; if the fresh centre
  still opens Alliance, a different entry path is
  owed before further right-edge-stack taps. No
  profile claim is superseded: this profile records
  no Mail coordinate, only the right-rail envelope
  icon.

## What the 2026-11-03 1740 unit added - R2 fresh grounding opens Mail first try, Alliance Exercise claim, red dot is unread not claimable

- Ticker-1734, unit mail-2026-11-03-1430, about
  17:35 to 17:40 local, status done. Evidence in
  `_records_/2026-11-03/mail-rewards/1740-queue-run.md`.
- The game was found on the Alliance panel (left from
  the previous help unit), not on the base view. No
  "active on a different device" dialog appeared.
- Entry method changed per rule R2 after the 1055
  unit's misfires: instead of reusing the recorded
  right-edge tap, every centre was freshly measured
  on the live frame with visual grounding before
  tapping. The Alliance panel back arrow at grounded
  (162,936) returned to the base view; the earlier
  (89,941) estimate had produced no change. The Mail
  envelope on the right rail at grounded (929,783)
  opened the Mail category list. This is the first
  mail entry this day that did not open Alliance
  instead, and it answers the 1055 follow-up (fresh
  centre on the live frame, verify the panel that
  opens is Mail before sweeping) - the fresh centre
  worked on the first tap. Standing rule restated:
  re-ground the envelope on the live frame per
  session; (929,783) is this unit's measured centre,
  not a standing coordinate, and no profile claim is
  superseded - this profile still records no standing
  Mail coordinate, only the right-rail envelope icon.
  Related Issue #230 stays open: closure belongs to
  the daily retro, with evidence.
- Category screen on entry: Alliance carried a gift
  icon, Event carried a red dot, the other categories
  carried no gift icon and no red dot.
- Alliance: the top mail, [Alliance Exercise]
  Alliance R... dated 2h ago, carried the gift icon.
  Claim All claimed it. The congratulations popup
  read live: EXP 105.8M, a 50.0K card item, 4.6K of
  a blue item, 5m speedups in five stacks of 39, 21,
  16, 13 and 31 (120 in total), coin 12.1M, food
  19.0M, iron 19.0M. The popup was dismissed and the
  Alliance Exercise mail had left the list; the
  "Alliance Gifts received!" toast confirmed. HUD
  corroboration on the later base view: food 247.0M
  to 266.0M, iron 588.5M to 607.5M, coin 17.4M to
  29.5M, matching the popup food, iron and coin
  figures exactly.
- Event: train arrival mails (Sanction Apex, Abyss
  Apex, KpyKat trains, 9h to 17h ago) with no gift
  icons. Claim All produced no popup and no change,
  consistent with reports only. Lesson: the Event
  red dot was an unread train mail, not a claimable
  attachment - a category red dot signals unread, not
  claimable; only a gift icon evidences a claim.
- Battle Report, Season, System and Regular: swept
  by one batched tap sequence (category row, Claim
  All, back, repeated), ending cleanly back at the
  category list with no congratulations popup at any
  step, so no additional claimables are evidenced.
  Honest limit of this sweep, recorded not smoothed
  over: no per-category screenshot was taken during
  the batch, so the per-category evidence is the
  category screen's lack of gift or red-dot
  indicators plus the clean batch return, not a
  per-category live read.
- In-app Purchases was not opened: receipts only,
  nothing to claim, per the activity metadata.
  Delete All was never pressed. Nothing was bought,
  deleted or spent. The game was left on the Mail
  category list.
- Result stats: target 6, achieved 6, categories
  swept 6, resources gained EXP 105.8M plus coin
  12.1M plus food 19.0M plus iron 19.0M plus 120 5m
  speedups plus card items, costs 0 stamina,
  verified yes, blocker none.

## What the 2026-11-04 0212 unit added - Alliance claim verified by checkmarks, Regular notices already credited, notifications prompt declined

- Unit mail-2026-11-03-2230 by ticker-0204,
  02:08 to 02:12 local, status done. No "active on
  a different device" dialog appeared.
- Entry: Mail opened from the base right rail at
  grounded centre (931,804) - another first-try
  entry, evidence commented onto Issue #230 (the
  measured-envelope failure): fresh grounding, not
  the stale envelope point.
- Category list as standing: Battle Report (red
  dot), Alliance (gift icon), Event (gift icon),
  Season, System, Regular (red dot), In-app
  Purchases (red dot). Claim All pressed in every
  category, one at a time. Delete All was never
  pressed in any category, and 0 mail was deleted.
- Alliance claim verified in detail, not assumed
  from the missing toast: the top mail, Daily
  Donation Rankings dated 2026-11-3 18:03:11
  (No.17 on the alliance donation leaderboard),
  shows both reward icons with green checkmarks
  and no Claim button, i.e. claimed. A second
  Claim All tap in Alliance showed no change,
  consistent with nothing left to claim; under
  rule R2 that method was dropped and the detail
  check was used instead. Claimed count 1 for the
  unit (the Alliance Daily Donation Rankings
  rewards, verified by green checkmarks).
- Other categories: Event train arrival notices
  only ([AP3x] Abyss Apex, [AP3x] Nuna Knuckles
  and others), Claim All left the list unchanged,
  no claimable attachment. Battle Report Victory
  reports only (Lv.150 Walker, Zombie Raiders and
  Hordes), Claim All, no change. Season Ice
  Breaking Reports only, Claim All, no change.
  System Patch Notes, President Mail and a purge
  request notice, Claim All, no change. Regular
  resource notices (iron x1,800,000, 54m ago;
  coins x432,000, 56m ago) plus Victory reports
  (Vanguard Instructors, Doom Elite), Claim All
  left the list unchanged, so the resource notices
  read as already-credited notices, not claimable
  items. In-app Purchases receipts only (Research
  Speed-up Pack 2026-11-3, Fast Growth Pack
  2026-11-2), Claim All, no change.
- Exit: a notifications opt-in prompt appeared on
  exit ("Enable notifications and never miss
  important messages again"); Cancel was tapped,
  Enable Now was not touched, and the prompt
  closed. Lesson: decline the prompt, do not
  enable it.

## What the 2026-11-04 0445 unit added - category rows grounded, Event train arrival reward claimed

- Unit mail-2026-11-04-0230 by ticker-0434, 04:45 local, status done. The computer session dropped between units and was restarted (cc-414 to cc-415); no game state was lost. No "active on a different device" dialog appeared.
- Entry: Mail opened from the base right rail at the grounded point norm (930,800), consistent with the 0212 point (931,804) within session drift.
- Category rows grounded on the live list, because the first Event tap missed: Battle Report (500,152), Alliance (498,216), Event (500,368), Season (500,467), System (500,572), Regular (500,677). The earlier Event miss at norm (498,310) fell between rows - do not reuse it; the Event row is (500,368).
- Event claim: the list showed [AP3x] Abyss Apex train notices (35m ago, 2h ago), a "Train arrival reward!" (35m ago, gift icon), [AP3x] Missile Apex Mega Express (2h ago), Title Assignment (3h ago) and [AP3x] Nuna Knuckles train (4h ago). Claim All claimed the train arrival reward: the CONGRATULATIONS popup showed a 2.5K badge item x1, 50 crates and 8.5K triangle resource (item names from icons, figures as displayed). After dismissal the gift icon and the Claim All red dot were both gone from the Event list, verifying the claim complete.
- Other categories, no claim: Alliance (Daily Donation Rankings, Alliance Exercise, Voting Results, Zombie Siege Reports) answered Claim All with the toast "No rewards available." Season Ice Breaking Reports, System Patch Notes / President Mail / Season Conclusion, Regular Victory reports (Vanguard Instructor Lv.3/2/1 and Lv.55 Doom Elite) and Battle Report Victory reports (Lv.150 Walker, Rebel, Lv.20 Zombie Raider, Lv.19/18/17 Zombie Horde) all answered Claim All with no visible change. In-app Purchases was not opened: receipts only, nothing to claim, per the activity metadata. Delete All was never pressed in any category.
- Exit: Mail closed back to the base screen with the two back arrows. Nothing spent.

## What the 2026-11-04 0817 unit added - checked only, Claim All no-change in four categories, Event red dots are notices, done

- Unit mail-2026-11-04-0630 by ticker-0804, about 08:17 local, status done. Session cc-437. No 'active on a different device' dialog appeared; no takeover was needed. Evidence in `_records_/2026-11-04/mail-rewards/0817-queue-run.md`.
- Entry state: mail categories on entry carried red dots on Battle Report, Event and Regular; Alliance, Season and System carried none, and Purchases holds receipts only, so the dotted categories plus System were worked and the undotted ones were left alone.
- Event: Claim All pressed once with no visible change (both unread dots stayed). Changed method (rule R2): the newest unread mail was opened individually and proved to be a train arrival notice (conductor and passenger list) with no attachment and no Claim button, so the Event red dots are notices, not claimable rewards. The mail was left in place. This re-confirms the 1740 lesson that a red dot means unread, not claimable.
- System: reached on a mis-aimed category tap (the row centre read from the live category screen is Regular (500,679), consistent with the 0445 unit's (500,677); the earlier (498,620) tap landed on System). Category rows drift per session; re-ground the rows on the live list in every unit. Claim All pressed with no change; the visible items were patch notes and system notices, nothing claimable.
- Regular: Claim All pressed with no change. The visible items were resource reports (two x1,800,000 resource entries and one x432,000 coin entry) and Vanguard Instructor victory reports, none carrying an individual claim control - consistent with the 0212 read that Regular resource notices are already-credited notices, not claimable items.
- Battle Report: Claim All pressed with no change. The visible items were victory attack reports (zombie and walker targets), none claimable.
- Delete All was never pressed in any category. The mail screens were exited with the back arrow to the base screen; nothing was deleted, nothing was sent, nothing else was claimed.
- Why done: every dotted category was opened and its Claim All tried, and the one unread notice was opened individually to confirm it held no attachment. Nothing claimable was present in this round, so the check itself completes the regular: target 1 check, achieved 1, claimed 0 items.
- No new issue filed; mail entry (Issue #230) was not tested in this unit - no entry point is recorded here, so no #230 comment is made. No diamonds or money spent, no mail deleted, no other activity's work done.

## What the 2026-11-04 1333 unit added - screen-capture channel failure recurrence across activities, failed

- Unit mail-2026-11-04-1030 by ticker-1327, about 13:27 to 13:34 local, status failed (access-failed). Evidence in `_records_/2026-11-04/mail-rewards/1333-queue-run.md`. The record frontmatter says unverified while its Outcome section says failed (access-failed); the body outcome is followed here, and the frontmatter wording is left as recorded, not smoothed over.
- Capture sequence, all failed with the same error: open_app LastWar, computer.observe, computer.observe again, computer.control list_apps (confirmed LastWar running), computer.control activate, computer.observe with image view, computer.control describe, a fresh computer session with a second activate, computer.observe again, a screenshot action, and one more computer.observe after a short wait - every screen-capture step failed with "Failed to start stream due to audio/video capture failure". Device state at the time: Mac online, LastWar app running fullscreen, Google Chrome frontmost; the control channel itself answered throughout, so this is a capture-channel fault.
- Classification, stated explicitly: this is the same screen-capture channel failure class recorded for the 1235 help unit in `_activities_/alliance-help/INDEX.md` 1.25.0, now recurring in a second activity. It is NOT a mail entry failure (Issue #230 is not tested here - no entry point was reached, so no #230 comment is made), NOT a foreground or tap failure, NOT a missing owner authorization, and NOT a different-device dialog (no such dialog appeared). It does not contradict the foreground notes in this profile - those concern taps that dispatch but do not reach a control, while here no screenshot existed to tap from.
- No game input was dispatched and no tap was sent, so no in-game state changed. No mail tab was opened, no Claim All was pressed, and no reward count was read; nothing observed is claimed. Mails claimed: 0.
- Recurrence, the point of this fold: this is the second consecutive ticker pass to fail this way (ticker-1224 help 1235 failed identically about one hour earlier). The 1232 organizer run recorded this failure as a watch item that becomes a filed gap only if it persists across passes; it has now persisted across passes and activities, so the escalation is filed as Issue #282 (device-channel diagnosis, not another entry-point or coordinate change). The 1235 follow-up rule and this record agree: if the capture failure persists, it escalates as a device-channel fault, not as a repeat of the same taps.
- Retry rule satisfied: far more than 3 capture attempts were made in this pass (two sessions, repeated observe, describe and screenshot attempts) before the access failure was recorded.
- Follow-up from the record itself: the tracker is untouched per the failed-unit rule, the regular remains due, and the next tick re-produces it as a fresh unit with this unit retried first. No diamonds or money spent, no mail deleted, no other activity work done.

## Correction 2026-11-05 - the game window is windowed on an inactive Space, not in native fullscreen

- Source: the 0134 survivors record (`_records_/2026-11-05/survivor-intake/0134-queue-run.md`, ticker-0134, twenty-sixth consecutive capture failure), re-confirmed by the 0204 gifts record (`_records_/2026-11-05/alliance-gifts/0204-queue-run.md`, ticker-0204, twenty-seventh) and by the 0734 arms-race and 0804 donations records on the same day (thirty-seventh and thirty-eighth occurrences, probe OFF_SCREEN_WINDOW, Chrome observing normally in the same sessions). The View menu lists "Enter Full Screen", so the app is NOT in native fullscreen: it is a windowed 1920x1080 window on an inactive Space, and the capture failure is the pixel stream of an off-screen window, not a broken screen-recording permission.
- Superseded in this profile: the "LastWar app running fullscreen" wording in the 1333 section above. The rest of that section stands unchanged: the capture sequence, the classification (the same screen-capture channel failure class as the 1235 help unit, not a mail entry failure and not a different-device dialog), and the follow-up rule.
- Follow-up corrected: the unblock is getting the window back onto the active Space, and the owner clicking the LastWar Dock icon once is the known reliable step. This correction changes no Mail state: no mail tab was opened in the 1333 unit and no reward count was read, and none is asserted here.
- Scope correction 2026-11-05 (from the 0904, 0941 and 1025 records): the Dock-icon unblock in the bullet above holds for the window-stream (capture-failure) form only. It does not address a stalled invoke channel or an offline device: for the zero-response form the record inference is a Mac-side agent gateway restart before re-probing (unverified), and re-probing is owed only after device.list last_seen refreshes.

## What the 2026-11-05 1025 unit added - Mac device offline, forty-second consecutive pass, zero-response form

- Unit mail-2026-11-05-0630 by ticker-1025, about 10:25 to 10:36 local, status failed (access-failed). Evidence in `_records_/2026-11-05/mail-rewards/1025-queue-run.md`. No game screen was ever read and no game input was dispatched: every device invoke to the Mac mini returned node_offline or timed out, so no mail category was opened and no attachment was claimed.
- Attempts, five, zero responses: computer.session start on the Mac mini node_offline (device offline, no wake-up path) twice; connection.health on the Mac mini node_offline; connection.repair (web) on the Mac mini node_offline; connection.health on the recovery device node_invoke_timeout after 25s. device.list now reports the Mac mini offline (earlier passes saw it online-stale) with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 2 hours 55 minutes at pass time - the state has worsened from online-stale to offline.
- Classification: the forty-second consecutive ticker pass with a Mac device-access blocker (Issue #284, open, tooling), and the third in the worsened zero-response form after ticker-0904 (fortieth) and ticker-0941 (forty-first). The fail-fast probe (_tools_/mac_capture_probe.py 1.1.0, PR #321, merged 2026-11-05 09:47 PST) classifies CHANNEL_STALL (high confidence), stop_pass yes, exit 12. This is NOT a mail entry failure (Issue #230 is not tested here - no entry point was reached, so no #230 comment is made) and NOT a capture-channel fault of the 1333 form: the control channel itself returned no response at all.
- Scope correction: see the appended bullet in the Correction 2026-11-05 section above - the Dock-icon unblock holds for the window-stream form only, not for a stalled invoke channel. For the zero-response form the record inference is a Mac-side agent gateway restart before re-probing (unverified), and re-probing is owed only after device.list last_seen refreshes.
- Follow-up: tracker untouched per the failed-unit rule, the regular remains due, and the next tick re-produces it as a fresh unit. Sync reaped 0, expired 2 (training/survivors 0603), produced nothing (all 21 due regulars already queued). No diamonds or money spent, no mail deleted, no other activity work done. Forty-second occurrence commented onto Issue #282 by this run.

## What the 2026-11-05 1804 unit added - Mac device offline, fifty-seventh consecutive pass, zero-response form

- Unit mail-2026-11-05-1430 by ticker-1804, about 18:05 to 18:08 local, status failed (access-failed). Evidence in `_records_/2026-11-05/mail-rewards/1804-queue-run.md`. No game screen was ever read and no game input was dispatched: every device invoke to the Mac mini returned node_offline or timed out, so no mail category was opened, no attachment was claimed, and no report mail was checked. This was a segment 2 unit (planned_for 2026-11-05T22:30:00Z, expires 2026-11-06T02:30:00Z).
- Attempts, seven, zero responses: computer.session start on the Mac mini node_offline (device offline, no wake-up path) three times; connection.health on the Mac mini node_offline; connection.repair (web) on the Mac mini node_offline; connection.repair (native) on the recovery device node_invoke_timeout after 25s; connection.health on the recovery device node_invoke_timeout after 25s. device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 10 hours 30 minutes at pass time, unchanged since the ticker-1025 pass; the recovery device also reports offline with the same stale last_seen. This meets the standing at-least-3-attempts retry rule.
- No blind taps were dispatched: without an observation, any tap could land on the wrong control, so the unit stops here under the check-first rule. No different-device dialog was observed (no screen was ever captured) and no device takeover was needed.
- Classification: the fifty-seventh consecutive ticker pass with a Mac device-access blocker (Issue #284, open, tooling), and the eighteenth in the worsened zero-response form after ticker-1734 (fifty-sixth, seventeenth). This is NOT a mail entry failure (Issue #230 is not tested here - no entry point was reached, so no #230 comment is made) and NOT a capture-channel fault of the 1333 form: the control channel itself returned no response at all.
- Scope correction: see the appended bullet in the Correction 2026-11-05 section above - the Dock-icon unblock holds for the window-stream form only, not for a stalled invoke channel. For the zero-response form the record inference is a Mac-side agent gateway restart before re-probing (unverified), and re-probing is owed only after device.list last_seen refreshes.
- Reading warning: this failed unit gives zero evidence about the mail state. It must NOT be read as "no mail claimable" - the 0817 close (all dotted categories swept, Event red dots are notices) rests on live reads and stands as the last live read; this unit rests on no read at all.
- Follow-up: tracker untouched per the failed-unit rule, the regular remains due, and the next tick re-produces it as a fresh unit. The pass stopped after this one unit: a second unit would hit the same dead channel. Sync at pass start produced nothing new (21 due, all already queued; 1 expired). The Zombie Invasion chain stays closed: the event ended 2026-10-30 about 19:00 and no Zombie Invasion tab has been seen in the Events hub since, so no fresh chain was seeded. The pre-reset zero-sweep pair for tonight's 19:00 reset (chain pre-reset-sweep-2026-11-05) is staged in the inbox (units 001 and 002). No diamonds or money spent, no mail deleted, no other activity work done. Fifty-seventh occurrence commented onto Issue #282 by this run.

## What the 2026-11-07 1740 unit added - checked only, all six categories nothing claimable

- Unit mail-2026-11-07-1430 by ticker-1727, about 17:32 to 17:40 local, status done. Evidence in `_records_/2026-11-07/mail-rewards/1740-queue-run.md`. Computer session cc-20, LastWar already running.
- Claim All pressed in all six claimable categories; every one answered "No rewards available." - Battle Report, Alliance, Event, Season, System, Regular. Nothing was claimed, nothing was deleted (Delete All never pressed).
- Mail contents read live: Event held the Missile Apex train mails (45m, 9h, 11h, 13h, 15h ago) and a Title Assignment mail - no attachments left to claim. Alliance held the Alliance Exercise mail (2h ago), two New Alliance Assembly Point notices (20h ago), two New Alliance Marker notices (1d ago) and a Zombie Siege Report - no attachments. Regular held Victory reports (Lv.57 Doom Elite, 38m to 8h ago). Battle Report held the RebelNova attack victory (50m ago) and the Lv.16 to Lv.20 Zombie Horde victories (1d ago). Season held Alliance Loot Rewards (2d ago) and Ice Breaking Reports (11d ago). System held President mails, Pack and Event Adjustment, Maintenance Completed and Patch Notes (1d to 3d ago).
- In-app Purchases was not opened: receipts only, nothing to claim, per the activity metadata. Its red dot is unread receipts.
- Figures read live: Power 149,850,353; food 476.8M, iron 800.4M, coin 5.7M, stone 25.0M, 922.2K; diamonds 3,702.
- No diamonds, money, speedups or paid buttons were used. No login or verification was demanded, and no different-device dialog appeared.

## What the 2026-11-07 2028 unit added - done, Alliance and Event rewards claimed, other categories clear

- Unit mail-2026-11-07-1830 by ticker-2006, about 20:28 to 20:36 local, status done. Evidence in `_records_/2026-11-07/mail-rewards/2028-queue-run.md` (commit e9bf320c92 on records/2026-11-07). Computer session cc-45, LastWar already running on the base screen (eastern framing).
- Category list read live at entry: Alliance and Event carried gift icons; Battle Report, Season, System and Regular carried neither a gift icon nor a red dot; In-app Purchases carried a red dot only (receipts, not opened, per the activity metadata).
- Alliance: Claim All pressed. The claimable mail was Daily Donation Rankings (2h ago). CONGRATULATIONS popup: red gem x10, badge (50) x4. The other Alliance mails carried no attachments: [Alliance Exercise] Alliance R... (4h ago), two New Alliance Assembly Point notices (23h ago), two New Alliance Marker notices (1d ago).
- Event: Claim All pressed. Three mails claimed: Weekly Alliance Duel Defeat (2h ago), Daily Participation Rewards (2h ago), Unclaimed "Daily Task" Reward (2h ago). CONGRATULATIONS popup showed twelve items: grey chest x10, food crate x10, coin chest x10, blue badge x800; silver chest x10, red gem x500, food crate x30, grey chest x30; coin chest x30, EXP chest x30, bread 5.0K, iron 5.0K. The other Event mails carried no attachments: Event Task EXP Reissue (2h ago, red dot only), Title Assignment (3h ago), [AP3x] Missile Apex's train has... (12h ago).
- Verification: after both claims the category list was re-read live - no gift icon remained on Alliance or Event.
- Nothing was deleted (Delete All never pressed).
- Limit, stated plainly: Battle Report, Season, System and Regular were checked by the category-list read only (no gift icon, no red dot on entry); Claim All was not pressed inside those four categories this unit. The two gift-carrying categories were swept and verified clean.
- Figures read live: power 149,850,353; food 478.7M, iron 802.1M. The record's coin figure (802.1M) repeats the iron figure and is not used here; coin 6.9M stands from the bracketing 2026 training and 2000 survivors reads. No diamonds, money, speedups or paid buttons were used. No other task type was executed in this unit. No login or verification was demanded, and no different-device dialog appeared.

## What the 2026-11-07 2052 unit added - done, Alliance and Event checked, nothing claimable

- Unit mail-2026-11-07-1830 by ticker-2034, about 20:48 to 20:52 local, status done. Evidence in `_records_/2026-11-07/mail-rewards/2052-queue-run.md` (commit 7a4a104930 on records/2026-11-07). Computer session cc-49, LastWar already running on the Mac mini.
- Mail opened from the right-rail envelope button (grounded at norm 936,790). Category overview read live: Battle Report, Alliance, Event, Season, System, Regular, In-app Purchases. The only red dot in the overview stood on In-app Purchases, which holds receipts only and nothing to claim.
- Alliance opened: Daily Donation Ranking (2h ago), New Alliance Assembly Point (1d ago), New Alliance Marker Created (1d ago, twice). Claim All tapped; the game answered "No rewards available."
- Event opened: Weekly Alliance Duel Defeat (2h ago), a participation reward mail, "Unclaimed -Daily Task- Reward" (2h ago), The Assignment (4h ago), and an [AP3x] Missile Apex train mail. Claim All tapped; the game answered "No rewards available." The "Unclaimed" mail is notification-only: no attachment is claimable through Claim All. The Weekly Alliance Duel Defeat mail corroborates the duel week ending in defeat; the personal duel total is still unread (the duel-score-2026-11-07-1830 unit has no record on the branch, Issue #136 stays open).
- Battle Report, Season, System and Regular were not opened: no red dots stood on them, and the metadata records them as reports-only. Delete All was never pressed anywhere.
- Figures read live on screen: power 149,850,353 at entry and at close; food 478.8M, iron 802.1M, coin 6.9M. No diamonds, money, speedups or paid buttons were used. No other task type was executed in this unit. No login or verification was demanded, and no different-device dialog appeared.
- Result statistics: target 2, achieved 2, resources_gained none, costs about 4 minutes play, verified yes, blocker_category none, device_takeovers 0.

## What the 2026-11-08 2132 unit added - Alliance and Event mail claimed in full, 10 mails

- Unit mail-2026-11-08-1830 by ticker-2119, about 21:28 to 21:32 local, status done. Evidence in `_records_/2026-11-08/mail-rewards/2132-queue-run.md` (commit fe08a0907 on records/2026-11-08). All claimable mail claimed.
- Alliance - Claim All: five mails, all 3h ago, all with gift icons before the claim - Daily Donation Rankings; Weekly Donation Ranking; 3v3 Brawl, Major's Gift (three times). CONGRATULATIONS popup items as read from the zoomed screenshot (icon, count at bottom-right; a top-left number reads as the item denomination where present, that reading is the unit's inference): blue medal 750, iron crate 30, gold chest 240, food crate 30, gold badge 500 x2, coin chest 30, EXP crate 30, red gem 50, gold badge 50 x4. Verified after dismissing the popup: the gift icons are gone from all five mails (envelopes show opened), and the Claim All button lost its red dot. The New Alliance Marker mail below them never carried a gift icon.
- Event - Claim All: five mails with gift icons before the claim - "Weekly Pass" Unclaimed Reward (2h ago); Unclaimed VIP Daily Level Reward; Unclaimed Event Reward (3h ago); Alliance Star Scratch Card Reward (3h ago); Season Resource Conversion (4h ago). CONGRATULATIONS popup items as read from the zoomed screenshot (same two-number reading): gold puzzle piece 2, green gift box 2, gold badge 500 x1, red gem 1.5K, gold badge 50 x1, EXP book 1.0K x3, coin chest 13, food crate 13, iron crate 13, grey steel blocks 4, EXP book 100 x2.6K, red gem 10 x2. Verified after dismissing the popup: the gift icons are gone from all five mails, and the Claim All button lost its red dot. The [AP3x] Missile Apex's train mail (13h ago) never carried a gift icon. The scrolling alliance-appointment banner at the top of the Event list is informational only.
- Not opened: Battle Report, System, Regular - no gift icon on their category rows, so nothing claimable by the gift-icon indicator; not opened this unit. In-app Purchases keeps its red dot, but it holds receipts only, nothing to claim. Category-level re-check after both claims: no category row shows a gift icon.
- Note, against the 2052 unit's "Unclaimed" finding: the 2052 "Unclaimed -Daily Task- Reward" mail was notification-only (no attachment claimable through Claim All), but this unit's "Unclaimed" mails (Weekly Pass Unclaimed Reward, Unclaimed VIP Daily Level Reward, Unclaimed Event Reward) DID carry claimable attachments, verified by the popup items and the cleared gift icons. "Unclaimed" in a mail title does not by itself mean notification-only - the gift icon on the row is the indicator.
- Red lines held: Delete All never pressed, no diamonds or money spent, no mail deleted, no other unit's work touched.
- Result stats: target 10, achieved 10, resources_gained alliance 5 mails plus event 5 mails, popup items as listed above, costs 5 minutes, no items spent, verified yes.

## What the 2026-11-09 0138 unit added - Alliance and Event Claim All no rewards, System/Regular/Battle Report unwalked, leader row Jerry Apex, Mail button flaky

- Unit mail-2026-11-08-2230 by ticker-0113, about 01:20 to 01:38 local, status partial. Evidence in `_records_/2026-11-09/mail-rewards/0138-queue-run.md` (commit c0ebf0c4f0 on records/2026-11-09).
- Mail home read live at entry: red dots on Alliance, Event and In-app Purchases. Note under the list - mails older than 30 days are deleted automatically.
- Alliance list read live: Leadership Transfer Notice (red, 2h ago) - "Jerry Apex has become the new Alliance..." (full text not opened); Daily Donation Rankings (7h ago); Weekly Donation Ranking (7h ago); 3v3 Brawl Major's Gift x3 (7h ago). Claim All pressed - toast "No rewards available.", nothing claimed.
- Event list read live: "[AP3x] DCna8ive's train has arrived" (train arrival); "[AP3x] Missile Apex's Mega Ex..." (3h ago); "[AP3x] DCna8ive's train has departed" (3h ago); "Weekly Pass Unclaimed Rewards" (6h ago); "Unclaimed VIP Daily Level Rewards" (7h ago). Claim All pressed - toast "No rewards available.", nothing claimed. The two "Unclaimed" mails read as notifications, not claimable attachments - consistent with the 2132 gift-icon rule (neither carried a gift icon here; "Unclaimed" in a title does not by itself mean notification-only, the gift icon on the row is the indicator).
- Leadership change, read live: the Alliance page was opened once as a navigation check and its leader row reads Jerry Apex (previously Texan Apex per the repo), [AP3x] The Apex, 96/100 members. The Leadership Transfer Notice itself was not opened in full, so the transfer mechanics are not asserted - only the live leader row and the preview line. The next alliance-facing unit should confirm the leader row again live.
- Mail entry, flaky (Issue #230 evidence): the Mail button itself did not respond to five background taps at two grounded points ((707, 792) twice, (650, 791) single and double, manual mouse press) and only opened on a later tap at (652, 793) after the Alliance page had been visited. The entry point is flaky and the next mail unit should re-ground it fresh rather than reuse a stale point. Commented onto Issue #230 by this run.
- VIP flag, for the vip regular (not this unit's work): the "Unclaimed VIP Daily Level Rewards" mail (7h ago) suggests the VIP daily freebie may still be unclaimed - the vip unit in the inbox should check the VIP screen, not the mail.
- What was not done: System, Regular and Battle Report categories were not walked in this unit (unit cap reached at the Event Claim All). Per queue rule R7 they are the first action of the next mail unit. In-app Purchases was not opened (receipts only, nothing to claim, per the activity metadata).
- Figures read live: power 149,209,253; food 513.8M, iron 838.3M, coin 25.2M, diamonds 6,027. No diamonds or money spent. Delete All never pressed. No mail deleted. No login or verification was demanded, and no different-device dialog appeared.
- Result stats: target 5, achieved 2, resources_gained none, costs about 15 minutes of unit time, no items spent, verified yes, blocker_category c.

## What the 2026-11-09 0421 unit added - all three red-dot categories walked, no claimable attachments, envelope opened at once (no Alliance-first workaround)

- Unit mail-2026-11-09-0230 by ticker-0404, about 04:19 to 04:21 local, status done. Evidence in `_records_/2026-11-09/mail-rewards/0421-queue-run.md` (commit 9fdcc4c9ee on records/2026-11-09). Computer session cc-220 on the owner Mac mini.
- Entry: Mail envelope button grounded fresh at norm 931,790 on the base screen and tapped once; the Mail home opened at once (no Alliance-first workaround needed this unit, unlike the 0138 unit - the workaround is a fallback, not the entry route).
- Mail home red dots: Event, Regular, In-app Purchases. Battle Report, Alliance, System and Favorite carried no red dot.
- Event list: [AP3x] Missile Apex's train has... (22m ago, unread); [AP3x] Abyss Apex's Mega Exp... (2h ago, unread); [AP3x] Missile Apex's train has... (2h ago, unread); [AP3x] DCna8ive's train has a... (4h ago); [AP3x] Missile Apex's Mega Ex... (6h ago); [AP3x] DCna8ive's train has d... (6h ago). A new train mail arrived at the top during the visit (12m ago at the Claim All read). Claim All tapped at norm 746,948: toast "No rewards available." Nothing claimed. These are notification mails, not claimable attachments.
- Regular list: battle reports - Victory vs Lv.57 Doom Elite and similar, 1d ago and older. Claim All tapped at norm 746,948: toast "No rewards available." Nothing claimed.
- In-app Purchases list: receipts only, as the profile states - 2026-11-08 10:53:07, Pack purchased: Drone Great Value Pack; 2026-11-07 18:42:14, Pack purchased: Gear Master Pack. Claim All was not pressed here: the list holds receipts only, nothing to claim.
- Delete All was not pressed in any category. Nothing was deleted. Back arrow returned the game to the base screen. The game was left on the base screen. No diamonds or money spent.
- Result stats: target 3, achieved 3, resources_gained none, costs 2m_wall_no_stamina, verified yes, categories_walked 3, claimed 0, device_takeovers 0. 0 claimed is the complete result, not a miss.

## What the 2026-11-09 1031 unit added - Event and Alliance Claim All no rewards, train mails carry no attachments, partial

- Unit mail-2026-11-09-0630 by ticker-1004, about 10:23 to 10:31 local, status partial. Evidence in `_records_/2026-11-09/mail-rewards/1031-queue-run.md` (commit 09e4f0863 on records/2026-11-09).
- Entry: Mail opened from the base screen in windowed 642x951 mode - the Mail button tap at the freshly grounded centre (932,791) worked at once. Windowed background clicks reach the game, unlike the fullscreen Alliance taps in the sibling 1019 help unit. Entry point still drifts per session; re-ground fresh each unit (Issue #230).
- Event category (red dot on entry): six train mails - Abyss Apex 2h and 4h ago (unread, red dots), Missile Apex 6h ago, Abyss Apex Mega Express 8h ago, Missile Apex 8h ago, DCna8ive 10h ago. Claim All answered "No rewards available." The two red dots cleared and the envelopes show opened afterwards - the train mails carry no claimable attachments.
- Alliance category: leadership notice (11h ago), Daily Donation Rankings, Weekly Donation Ranking (16h ago), Major's Gift, 3v3 Brawl. Claim All answered "No rewards available." again - no claimable attachments in Alliance either.
- What was not done: Battle Report, System and Regular were not opened this cycle. On 2026-10-25 they held reports only, but no live read was taken today, so the unit closes partial and the next mail unit resumes with those three categories (queue rule R7).
- No mail deleted; Delete All never touched. No diamonds or money spent. No other unit's work touched.
- Result stats: target 1, achieved 0, resources_gained none, costs about 8 minutes of unit time, no items spent, verified yes, blocker_category h, points 0.

## What the 2026-11-09 1657 sweep read added - Mail red dot standing, three categories still unopened today

- Read, not a mail unit: the zero-sweep 001 unit (ticker-1635) read the Mail icon live about 16:47 local. Evidence in `_records_/2026-11-09/daily-activities/1657-queue-run.md` (commit c9a86fa74 on records/2026-11-09). No mail was opened in this read.
- Mail carries a red dot. Battle Report, System and Regular categories are still unopened today (Event and Alliance answered "No rewards available." at 10:31 per the 1031 unit). The next mail unit resumes with those three categories (queue rule R7, carried from the 1031 unit) - the mail-1430 unit was raised to priority 1 by this sweep. (2026-11-09 1838 update: the mail-1430 unit ran 18:29-18:38 and walked all three - System claimed the Season Closed gift, Regular and Battle Report held reports only. The R7 carry is closed.)
- No mail deleted; Delete All never touched. No diamonds or money spent.

## What the 2026-11-09 1838 unit added - 9 reward mails claimed, Alliance/Event/System Claim All, leadership transfer to Abyss Apex, entry (935,797)

- Unit mail-2026-11-09-1430 by ticker-1822, about 18:29 to 18:38 local, status done. Evidence in `_records_/2026-11-09/mail-rewards/1838-queue-run.md` (commit 6761c35d1 on records/2026-11-09). Computer session on the owner Mac mini. The 1657 sweep's R7 carry is closed by this unit: Battle Report, System and Regular are all walked here.
- Base screen at 18:33: Total Power 146,736,949; Coin 56.3M, Bread 560.7M, Iron 884.6M (top bar). Power datapoint for Issue #482: 146,736,949 is 6,000 ABOVE the radar unit's 146,730,949 at about 17:53 - the day's fall has levelled at the close, not continued. Commented on Issue #482 by this run.
- Entry, Issue #230 evidence: on entry the game still showed a leftover CONGRATULATIONS popup from the 17:54 radar claim (Radar x10, EXP 1.7M, x800, Bread 885.6K, Coin 136.8K) - observed, not claimed by this unit; dismissed with one tap below the popup. The Mail button: first tap at (935, 820) showed no change; a second tap at the freshly measured icon centre (935, 797) opened Mail. Background clicks reach the game in windowed 642x951 mode, but the first tap can land without effect - the entry point drifts per session, re-ground fresh each unit. Commented onto Issue #230 by this run.
- Alliance: Claim All claimed 5 mails - Daily Donation Rankings (29m ago), Zombie Siege Report (Alliance) and (Individual) (45m ago), Defense Success Reward (57m ago), [Alliance Exercise] Alliance Reward (3h ago). Rewards read live: Coin 12.1M, Bread 19.0M, Iron 19.0M, 5m speedups x24, x31, x18, x33 and x14, 1m speedups x225 and x225. The popup top row was partly hidden behind the banner (147.0M, 30.0K, 4.0K, 400 with icons obscured) and is recorded as read, labels unverified.
- Event: Claim All claimed 3 mails - Duel Progress / Alliance Duel Individual Reward (29m ago), Daily Participation Rewards (29m ago), Arms Race Ranking Reward (32m ago). Rewards read live: EXP item x30, Coin 30.0K x50, Bread 50.0K x50, coin bags x69, bread chest x69, iron chest x69, blue crystal 1.5K, Lv.2 chest x2, red gems 10 x5 and 50 x4. Top row again partly hidden behind the banner, recorded as read only. The Arms Race Ranking Reward arriving by Event mail is folded into arms-race 1.71.0 - ranking chests are claimed via Event mail, not on the phase page.
- Battle Report: 6 Victory reports vs Lv.15-20 Zombie Horde (48m to 54m ago), reports only, no attachments. Regular: battle reports only (Lv.1 CL-7 Victim 4h ago, Lv.1 and Lv.57 Doom Elite 2d ago), no attachments.
- System: Season Closed (1d ago) carried a gift icon; Claim All answered REWARD CLAIMED with red gems x50. Other System mails are notices only (President Mail transfer updates, Pack and Event Adjustment, Server 2110, Maintenance Completed).
- Leadership Transfer Notice in Alliance: Abyss Apex has become the new Alliance leader (title cut off on screen). Confirmed on the Alliance panel in the sibling 1842 gifts unit (Leader Abyss Apex, Power 13,577,450,619, Members 96/100). CORRECTION: the leader was Jerry Apex at the 0417 gifts read - the 0417 section's leader line is superseded as of this read. Scrolling banner: President HawksMav appointed YOUGO^Apex Secretary of Defense and another member Secretary of Science; the gifts unit also saw NERO appointed Secretary of Interior. Alliance news, no action.
- Favorite was not opened: no gift icon and no red dot on the category list.
- No mail deleted; Delete All never touched. No diamonds or money spent.
- Result stats: target 9, achieved 9, resources_gained Coin 12.1M plus Coin 30.0K x50, Bread 19.0M plus Bread 50.0K x50, Iron 19.0M, red gems 50 plus 10 x5 and 50 x4, EXP item x30, speedups 5m x106 and 1m x450, coin bags x69, bread chest x69, iron chest x69, blue crystal 1.5K, Lv.2 chest x2, costs about 9 minutes of unit time, no items spent, verified yes, points 0.

## What the 2026-11-09 2129 unit added - done, Event Weekly Pass rewards claimed, other categories reports only

- Unit mail-2026-11-09-1830 by ticker-2109, about 21:26 to 21:29 local, status done. Evidence in `_records_/2026-11-09/mail-rewards/2129-queue-run.md` (commit 88c1abf8e on records/2026-11-09).
- Mail category list: Battle Report (red dot), Alliance, Event (gift icon), System, Regular, In-app Purchases (red dot, receipts only), Favorite.
- Event: Claim All claimed the "Weekly Pass" Unclaimed Rewards mail (2h ago) - REWARD CLAIMED popup showed red gem x10 and white crystal x4, the only two items on the popup. After the claim its gift icon was gone and its envelope showed read. The other Event rows are reports with no attachments: Duel Progress (Alliance Duel Individual Reward, 3h ago), Daily Participation Rewards (3h ago), Arms Race Ranking Reward (3h ago), two [AP3x] Abyss Apex train arrival mails (13h and 15h ago).
- Alliance: Claim All pressed, no change - nothing claimable. Rows are Daily Donation Rankings (3h ago), Zombie Siege Report (Alliance) and (Individual) (3h ago), Defense Success Reward (3h ago), [Alliance Exercise] Alliance Reward (5h ago), Leadership Transfer Notice - Abyss Apex has become the new Alliance leader (18h ago).
- System: Claim All pressed, no change - notices only (Season Closed, President Mail, Server 2110 notice, Maintenance Complete). Regular: Claim All pressed, no change - Victory battle reports only (Lv.1 CL-7 Victim, Lv.1 and Lv.57 Doom Elite). Battle Report: Claim All pressed, no change - 6 Victory reports vs Lv.15-20 Zombie Horde (3h ago), reports only.
- No mail deleted anywhere; Delete All never touched. Returned to the base screen.
- Result stats: target 1, achieved 1, resources_gained Event "Weekly Pass" Unclaimed Rewards mail - red gem x10, white crystal x4 (as shown on the REWARD CLAIMED popup), costs about 4 minutes of unit time, no items spent, verified yes, points 0.

## What the 2026-11-10 0143 unit added - Claim All sweep, no claimable rewards, Weekly Pass mail verified already claimed, session drop recovered

- Unit mail-2026-11-09-2230 by ticker-0134, 01:43 to 01:46 local, status done. Evidence in `_records_/2026-11-10/mail-rewards/0143-queue-run.md` (commit e3d186a38 on records/2026-11-10). Computer session cc-373 dropped mid-unit (observe returned observation_unavailable); session cc-374 started and LastWar re-selected, no game state lost - a further Issue #282 device-channel datapoint; commented on #282 by this run.
- Mail category list at entry: red dots on Alliance, Event and In-app Purchases.
- Alliance: six "New Alliance Assembly Point" mails, all 1h ago. Claim All answered "No rewards available."
- Event: three unread notices ([AP3x] KaBoom420's train, [AP3x] Abyss Apex's Mega Exp..., second train mail) plus three read mails ("Weekly Pass" Unclaimed Rewards 6h ago, Duel Progress Alliance Duel Individual Reward 7h ago, Daily Participation Rewards 7h ago). Claim All marked the three unread mails read and showed no reward summary. The "Weekly Pass" mail was opened to verify: its two reward icons (red gem x10, grey item x4) both carry green checkmarks, dated 2026-11-9 18:47:54 - already claimed, no claim button. This corroborates the 18:47 pass claims (shop-claims 1850); the Duel Progress mail at about 18:43 (7h before 01:43) is consistent with the about-18:00 duel rollover (Issue #242). One tap on that mail row first returned a spurious "target app exited" error; the next observe showed the mail open normally - the app never exited. A spurious exit error on a mail-row tap is recorded here: re-observe before acting on it.
- System: "Season Closed", President Mails, "Maintenance Complete". Claim All answered "No rewards available."
- Regular: victory reports only (Lv.1 CL-7 Victim, Lv.1 and Lv.57 Doom Elite). Claim All answered "No rewards available."
- Battle Report: Zombie Horde victory reports Lv.15 to Lv.20, 7 to 8h ago. Claim All answered "No rewards available."
- In-app Purchases (receipts only) and Favorite were not opened; no claimable attachments live there per the activity metadata.
- Delete All was never pressed; the per-mail trash button in the Weekly Pass detail was not pressed either.
- Outcome: no claimable mail rewards in any category this round. Nothing claimed, nothing deleted. Returned to the base screen. No diamonds or money spent.

## What the 2026-11-10 0355 unit added - Claim All sweep, no claimable rewards, R5 warning mail read

- Unit mail-2026-11-10-0230 by ticker-0334, 03:55 to 03:58 local, status done. Evidence in `_records_/2026-11-10/mail-rewards/0355-queue-run.md` (commit b7e79a62 on records/2026-11-10). Computer session cc-394 on the owner Mac mini.
- Mail category list at entry: red dots on Alliance, Event, System and In-app Purchases; none on Battle Report, Regular or Favorite.
- Alliance: one "Attention" mail (R5, 1h ago) plus five "New Alliance Assembly Point" mails (3h ago). Claim All showed no reward summary. The Attention mail was opened to verify: a text-only announcement from Abyss Apex, dated 2026-11-10 01:59:02, warning that a few people will leave the server in the next few days and might target the alliance as they leave; it asks members to keep troops away from the walls for the next few days unless participating in an event, to garrison each other if attacked while awake and active, and to save energy and resources for upgrades. No rewards attached, no claim button. No reply was sent and no action was taken on it; it is recorded here as alliance information.
- Event: train notices ([AP3x] Abyss Apex's Mega Exp..., [AP3x] KaBoom420's train) plus "Weekly Pass" Unclaimed Rewards. Claim All marked the unread mails read and showed no reward summary (the Weekly Pass rewards were already claimed on 2026-11-9, per the 0143 unit).
- System: "Planned Update Notice" (46m ago), "(President Mail) Transfer Update" (19h ago), "Season Closed" (1d ago), "(President Mail) 2110 | Transfer..." (3d ago), "Pack and Event Adjustment Notice" (4d ago), "(President Mail) Server 2110 ..." (5d ago). Claim All showed no reward summary.
- Regular: victory reports only (Lv.1 CL-7 Victim, Lv.1 and Lv.57 Doom Elite). Claim All showed no reward summary.
- Battle Report: Zombie Horde victory reports Lv.15 to Lv.20, 10h ago. Claim All showed no reward summary.
- In-app Purchases (receipts only) and Favorite were not opened; no claimable attachments live there per the activity metadata.
- One spurious "target app exited or restarted" error appeared on a back tap between System and Regular; the next observe showed the System list open normally - the app never exited (same spurious error as in the 0143 unit). Re-observe before acting on a spurious exit error.
- Delete All was never pressed.
- Outcome: no claimable mail rewards in any category this round. Nothing claimed, nothing deleted. Returned to the base screen. No diamonds or money spent.

## What the 2026-11-10 0929 unit added - entry blocked by camera framing, Mail panel never opened, partial

- Unit mail-2026-11-10-0630 by ticker-0904, about 09:25 to 09:29 local, status partial. Evidence in `_records_/2026-11-10/mail-rewards/0929-queue-run.md` (commit 31892dde on records/2026-11-10). Computer session cc-429 on the owner Mac mini (cc-428 dropped between units, recovered).
- Entry attempt 1: Mail envelope tap at the fresh measured centre (931,757) on the standard base framing delivered as a camera pan, not a button tap - the Mail panel never opened, and the view jumped to a panned framing (Drill Ground Lv.25, "15:26" timer) with the right rail (Mail, Alliance, Inventory, WORLD) off-frame. This is the background-input tap-delivers-as-drag failure mode the 0304 pass named the same morning.
- Recovery attempt 1: drag from (200,500) to (450,500) moved the camera back toward the standard framing (top HUD and HQ back in view) but still panned down-left, right rail still off-frame.
- Recovery attempt 2: reverse drag from (450,500) to (200,500) moved the camera back to the panned-right framing (Drill Ground Lv.25, "15:27"). The two drags oscillate between two panned framings; neither restores the right rail.
- Per queue rule R2, the entry attempts stop here: no further blind taps or drags inside this unit. The Mail panel was never opened, no category was swept, nothing was claimed, nothing was deleted.
- Blocker: camera framing (audit class c/e - tap method / repeated blocker): background-input taps intermittently deliver as map drags, and the base camera then sits in a panned state where the fixed right-rail shortcut column is off-frame. This is the fourth unit this reset day with the same blocker (the 0304 pass's radar, survivors and donations units), so it is a repeated failure mode, not a one-off. Filed as GitHub issue #580 (play) from this record.
- LESSON: the next mail unit must reset the camera framing first (the standard framing WAS present at 09:14 this pass, so the framing changes between passes) or find a Mail entry that does not depend on the right rail.
- No diamonds or money spent, no mail claimed or deleted (Delete All never pressed, Claim All never reached), no building or research started. The trucks screen was not re-entered in this unit.
- Result stats: target all mail categories swept, claimable rewards claimed, achieved 0 categories swept, Mail panel never opened, resources_gained none, costs about 8 minutes, no items spent, verified yes (the non-entry is observed live in this unit), blocker_category e (repeated blocker - camera framing, fourth unit this reset day).

## What the 2026-11-10 1259 unit added - Event train rewards claimed in full, mail-list back arrow re-grounded at (62,948), done

- Unit mail-2026-11-10-1030 by ticker-1234, about 12:45 to 12:59 local, status done. Evidence in `_records_/2026-11-10/mail-rewards/1259-queue-run.md` (commit 98abbc761 on records/2026-11-10). Session cc-454 on the owner Mac mini.
- Entry worked on standard framing: the Mail panel opened and the category list read red dots on Alliance and In-app Purchases, a gift icon on Event, no dots on Battle Report, Regular or Favorite. The #580 framing blocker is intermittent - the framing changes between passes; this unit needed no framing reset. Commented on Issue #580 by this run.
- Event: train mails ([AP3x] Missile Apex's and [AP3x] Abyss Apex's trains, 4h to 10h ago) plus "Train arrival reward!". Claim All produced a CONGRATULATIONS summary: gold badge 2.5K x1, supply chest x3, red gem 100 x1, supply chest x50, blue crystal 2.0K, 5m speedups x3, x2, x1, x8 and x6 (20 in total). All claimed.
- Alliance: five "New Alliance Assembly Point" mails (8h and 12h ago) plus the "Attention" mail (10h ago, R5-marked, already read in full by the 0355 unit - Abyss Apex warning about leavers targeting the alliance). Claim All showed no reward summary. No claimable attachments.
- System: "Planned Update Notice", "(President Mail) Transfer Update", "Season Closed", "Pack and Event Adjustment Notice", "(President Mail) Server 2110 ...". Claim All showed no reward summary.
- Regular: victory reports only (Lv.1 CL-7 Victim, Lv.1 and Lv.57 Doom Elite). Claim All showed no reward summary.
- Battle Report: Zombie Horde victory reports Lv.15 to Lv.20, 19h ago. Claim All showed no reward summary.
- In-app Purchases (receipts only) and Favorite were not opened; no claimable attachments live there per the activity metadata.
- Delete All was never pressed.
- BACK-ARROW BLOCKER RESOLVED IN-UNIT: the mail list back arrow did not respond to taps at (57,902) and (40,900) on window 489932, nor to a press-hold or taps at (55,925) and (40,955) on window 508052 - four no-change attempts in total. A fresh screenshot crop measured the arrow's true centre in the 642x951 window at (62,948); a tap there worked at once, and the same point worked for every later back tap in this unit. Earlier taps missed high (the button sits at about y 869-935 px, centre about y 902 px). Keyboard input is unavailable in this app - focus belongs to the other LastWar window - and the AX tree carries no back button element (game canvas), so coordinate taps at the freshly measured centre are the working route. See the updated How to enter entry.
- Figures read live: food 615.9M, iron 938.8M, coin 84.1M, power 148,765,978, diamonds 6,207 at entry and at close (unchanged). No login or verification demanded, no different-device dialog.
- Result stats: target 1, achieved 1, resources_gained Event train bundle (gold badge 2.5K x1, supply chests x53, red gem 100 x1, blue crystal 2.0K, 5m speedups x20), costs about 14 minutes play, verified yes, blocker_category none, device_takeovers 0.

## What the 2026-11-11 0222 unit added - Alliance and Event Claim All, Daily Donation Rankings and Arms Race rewards claimed

- Unit mail-2026-11-10-2230 by ticker-0212, 02:20 to 02:22 local, status done. Evidence in `_records_/2026-11-11/mail-rewards/0222-queue-run.md` (commit b0615980f on records/2026-11-11). Computer session cc-539 on the owner Mac mini.
- Category list at entry: Battle Report no gift icon; Alliance gift icon; Event gift icon; System one mail with a player avatar, no gift icon; Regular unread red dot, no gift icon; In-app Purchases unread red dot, receipts only; Favorite no icon. Only Alliance and Event carried a gift icon, so only those two categories were opened and claimed. Regular, System and Battle Report were not opened in this unit; they showed no gift icon on the category row.
- Alliance: list - Daily Donation Rankings (8h ago, gift icon), Voting Results (10h ago, unread), New Alliance Assembly Point (21h ago), Attention (1d ago, R5), New Alliance Assembly Point (1d ago, twice). Claim All tapped. Summary dialog: red gem x10, gold badge 50 x4. The Daily Donation Rankings gift icon was gone afterwards.
- Event: list - train mails from [AP3x] Missile Apex and [AP3x] MrCallejon (12m, 2h and 4h ago) plus "Unclaimed Arms Race event re..." (4h ago, gift icon). Claim All tapped. Summary dialog tiles read live: grey crates x57, grey-blue crates x30, blue crystal 38.0K, gold coins x57, blue triangle x500, iron x4, Lv.2 chest x1, red gem 50 x2, red gem 10 x5, 5m speedup x8. One further row of tiles at the top of the dialog was cut off by the banner and is not recorded - its icons and counts were not read live.
- After the tap the list showed no red dots and no gift icon on the Arms Race mail; all rows greyed. Delete All was never pressed.
- Outcome: done. Alliance Daily Donation Rankings claimed; Event Arms Race and train mail attachments claimed. No diamonds or money spent. The game was left on the base screen.
- Result stats: target claim every claimable reward attachment in mail, achieved Alliance Daily Donation Rankings claimed and Event Arms Race and train mail attachments claimed, resources_gained Alliance red gem x10, gold badge 50 x4; Event grey crates x57, grey-blue crates x30, blue crystal 38.0K, gold coins x57, blue triangle x500, iron x4, Lv.2 chest x1, red gem 50 x2, red gem 10 x5, 5m speedup x8 (plus one cut-off top row not read), costs about 2 minutes play, verified yes, blocker_category none, categories_with_gift_icons 2, categories_checked 2, device_takeovers 0.
