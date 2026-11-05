---
title: Mail Rewards
created: 2026-10-25T18:58:00Z
modified: 2026-11-05T16:36:24Z
level: L1
version: 1.20.0
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
---


# Mail rewards

## What this activity is

Opening Mail, claiming every claimable reward attachment, and checking
report tabs for anything that needs a decision. This folder accumulates
mail knowledge - tab behaviour, claim flow and recurring reward senders.
Executions are recorded in `_records_/<date>/mail-rewards/`, one file per execution.

## How to enter

- Base screen, Mail button on the right rail (envelope icon).
- The category rail, top to bottom, reads - Battle Report, Alliance,
  Event, Season, System, Regular, In-app Purchases (corrected
  2026-11-01 by the 1730 unit; the earlier list omitted Event and
  named the last category "Purchases"). The train arrival reward mail of
  the daily round was presented as an Event mail in game.
- Every category list ends with Delete All and Claim All buttons.
  Claim All claims every claimable attachment in that category at
  once. Purchases holds receipts only - nothing to claim.
- The back arrow sits at the bottom left of the mail screens, both in
  the category list and inside an open mail.

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
