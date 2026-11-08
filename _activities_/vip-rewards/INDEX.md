---
title: VIP Rewards
created: 2026-10-25T20:46:00Z
modified: 2026-11-08T03:44:20Z
level: L1
version: 1.12.0
description: Claiming the daily VIP gift and VIP level rewards, one activity folder for VIP claim knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner task request naming VIP rewards, 2026-10-25
  - source: pre-reset zero sweep execution record 2026-11-01 1757 queue run (lines 12-13)
  - source: ticker-1904 queue sync reap of expired units, 2026-11-01 (vip fix-up expired, attempts 0)
  - source: vip-rewards execution record 2026-11-02 0438 queue run
  - source: ticker-2134 vip-rewards execution record 2026-11-02 2138 queue run
  - source: ticker-0834 vip-rewards execution record 2026-11-04 0849 queue run (partial, VIP screen entry itself blocked, badge taps unresponsive, freebie/chest state unread)
  - source: ticker-1634 vip-rewards execution record 2026-11-06 1640 queue run (failed, Mac device offline, eighty-third consecutive ticker pass with a Mac device-access blocker, forty-fourth in the worsened zero-response form, Issue 284; last_seen 15:36:52Z stale about 33h, unchanged since the 1507, 1534 and 1604 passes; seven invokes, zero responses)
  - source: ticker-1727 vip-rewards execution record 2026-11-07 1747 queue run (partial, Freebie countdown to about 18:02 not the 19:00 reset, login chest already collected, VIP13 points 1,603,930 of 2,000,000, streak 1 day; record commit 69997e12a1 on records/2026-11-07)
  - source: ticker-1734 vip-rewards execution record 2026-11-07 1812 queue run (partial, login chest claimed plus 60 points to 1,603,990, streak 2 days, Freebie unlocked about 18:02 but Claim button unresponsive to four input variants including a foreground click; record commit 840094b6ad on records/2026-11-07)
  - source: ticker-1818 VIP execution record 2026-11-07 1830 queue run (partial, chest already claimed, freebie not retried, popularity popup on the avatar-tap route)
---


# VIP rewards

## What this activity is

Claiming what the VIP system pays this account - the daily free VIP
gift and any VIP level milestone rewards that are ready. Buying VIP
points or any paid VIP offer is never part of this activity.
Executions are recorded in `_records_/<date>/vip-rewards/`, one file per execution.

## How to enter

Measured on 2026-10-25.

- Tap the commander avatar at the top left of the base screen to open
  MY PROFILE.
- Tap the gold VIP badge on the profile (VIP13 on this account, with
  a red dot when the freebie is waiting). The VIP screen opens.
- Claim buttons are intermittently unresponsive, recorded by the
  retro of 2026-10-31 - 3 of the 4 queue-era VIP units closed
  partial. 2026-10-28 took the login chest but not the freebie,
  2026-10-29 took the freebie but not the login chest, and
  2026-10-31 took neither after 5 input variants on the freebie.
  Only 2026-10-30 took both. Attempt the freebie and the login
  chest independently, each with a live points read before and
  after, so one unresponsive button never skips the other item,
  and a failed claim re-enters the pre-reset sweep instead of
  waiting a full day. This is a repeat blocker under queue
  rule R2, not a one-day failure.

## Cadence

- The VIP Daily Freebie can be claimed once per day. After the claim
  its button becomes a countdown to the 19:00 daily reset (about
  4 hours 59 minutes at 14:00 on 2026-10-25).
- Reset rule, learned from a miss - because the reset is at 19:00
  local, a round that runs after 19:00 must claim the freebie AGAIN
  even when it was already claimed earlier the same calendar day.
  On 2026-10-25 the afternoon claim was made, the long evening
  sweep ran entirely after the reset and never opened the VIP
  screen, and the owner claimed the fresh freebie himself at about
  20:53. VIP is now on the daily umbrella list; do not close a
  round without it.
- Login points - the screen offered 200 VIP points for tomorrow
  login, on a 48 day streak. Points appear to land without a claim.
- Login chest, corrected 2026-10-27 - the points do need a claim.
  The chest icon at the top right of the VIP screen carries a red
  dot while the day login points wait, and the profile VIP badge
  keeps its red dot for it even after the Daily Freebie is
  claimed. Tapping the chest pays the day points (200 points on
  a 51 day streak, 2026-10-27) and clears the dot. A VIP visit
  is not finished until the chest is claimed too.
- VIP level milestone rewards are claimed once, when a level is
  reached. None was pending at the first check.

## Scope and availability

- This account is VIP 13 - 1,538,920 of 2,000,000 points toward
  VIP 14 after the first claim (1,538,720 on entry).
- The Daily Freebie scales with level - at VIP 13 it paid a puzzle
  piece item times 2 and food, iron and coin crates times 13 each.
- The VIP Exclusive offer on the same screen (99 dollars 99) is a
  purchase and out of scope. The points plus button and the cart
  shortcut lead to spending - never tapped.
- VIP 13 privileges include Activate the Mega Mode of Trade Trucks,
  which unlocks the Mega Mode in
  [truck-plunder](../truck-plunder/INDEX.md).

## What is known from 2026-10-25

- VIP13 privileges as displayed - Crafting Speed 50 percent,
  Research Speed 20 percent, Food, Iron and Coin Output 25 percent,
  Construction Speed 50 percent, March Speed 15 percent, Max Units
  5 percent, Mega Mode of Trade Trucks active.
- First freebie claim itemised in the execution record of this date.

## What the 2026-11-01 1757 sweep found

- VIP lines 12 (Daily Freebie) and 13 (login chest) were
  not at zero at about 17:55: never attempted that trade
  day. The state file carries no vip entry for 2026-11-01
  and no pre-reset vip unit existed, so the sweep itself
  enqueued the fix-up vip-2026-11-02-0151 (priority 1,
  expires at the 19:00 reset). The outcome is pending the
  final sweep and is NOT claimed here.
- This is the same miss pattern the profile warns about
  from 2026-10-25 (a trade day closing with VIP unopened),
  caught this time by the sweep mechanism itself instead
  of by the owner after the reset. If the fix-up closes
  the lines before the reset, the mechanism worked as
  designed; if it does not, the recurrence belongs in the
  daily retro, not in a silent carry-over.
- Final-sweep outcome: the 1849 final sweep found the
  vip-2026-11-02-0151 fix-up still in inbox at 18:43,
  never attempted that trade day, about 17 minutes before
  the reset. The sweep's own assessment is that the lines
  were likely to expire unclaimed at 19:00. Confirmed by the ticker-1904 sync reap: the fix-up
  expired with attempts 0 (result finished
  2026-11-02T03:04:31Z), so lines 12-13 did expire
  unclaimed at the 19:00 reset. The sweep detected the
  miss but the schedule did not close it; the recurrence
  belongs in the daily retro. A new-day vip unit
  (vip-2026-11-01-1900) sits in inbox for the new trade
  day, so the new day's VIP lines start fresh there.



## What the 2026-11-02 0438 unit found

- Unit vip-2026-11-01-1900 by ticker-0434, about 04:36 to 04:38,
  status partial. Evidence in
  `_records_/2026-11-02/vip-rewards/0438-queue-run.md`.
- Entry re-grounded - commander avatar at norm 60,85 opened MY
  PROFILE (Lv.30 [AP3x]Bears Lair, likes 1,797, up from 1,796 on
  2026-10-31, no popularity popup this time); VIP13 badge at norm
  514,352, carrying a red dot, opened the VIP screen.
- State read live - VIP13, 56 days logged in a row, 200 VIP points
  tomorrow, points 1,585,960 of 2,000,000 toward VIP 14 on entry.
- Login chest claimed, measured - chest at norm 833,195 tapped
  once: CONGRATULATIONS popup read Today's VIP Points 200,
  Consecutive Login Days 56, Next Day's VIP Points 200. Points
  after: 1,586,160, exactly plus 200, and the chest red dot
  cleared on the closing screenshot.
- Popup dismissal method, corrected - two taps on the popup X at
  norm 802,384 and 799,382 (the second a double tap) left the
  popup open; a tap on the dimmed area outside the popup at norm
  120,700 dismissed it at once. Dismiss this popup via the dimmed
  area, not the X.
- Daily Freebie, button-specific failure - contents shown: puzzle
  piece x2, food crate x13, iron crate x13, coin crate x13, with
  a green Claim button. Two single taps on the freshly grounded
  Claim centre, at norm 818,631 and 825,628, each verified by a
  following screenshot: button stayed green, points stayed
  1,586,160, no popup appeared. Per queue rule R2 the Claim
  method ends inside this unit after two no-change taps.
- The distinction is new and refines the blocker paragraph above -
  the login chest on the same screen, in the same session, via
  the same background input, worked at once, so the failure is
  specific to the Daily Freebie Claim button, not a general
  background-input failure. The same pattern appears in the
  daily-missions 0444 unit the same morning (green Claim buttons
  unresponsive on the Mission screen while navigation taps
  worked), filed as GitHub Issue 171 (play class). The freebie
  remains unclaimed for the current reset day and is the
  pre-reset sweep's item; the next tick re-produces this
  regular.
- Contents note - the freebie contents match the VIP 13 scale
  already in this profile (puzzle x2, crates x13 each); the open
  question whether contents rotate stays open, with one more
  same-contents observation.

## Open questions

- Whether the freebie contents rotate or are fixed per level.
- What reaching VIP 14 pays and unlocks.

## What the 2026-11-02 2138 unit found - checked only, both items already claimed

- Unit vip-2026-11-02-1900 by ticker-2134, about 21:38 to 21:41,
  status done as checked only: the VIP screen was opened and read
  live, and neither the Daily Freebie nor the login chest had
  anything left to claim. Evidence in
  `_records_/2026-11-02/vip-rewards/2138-queue-run.md`.
- Entry: commander avatar at norm (60,85) opened MY PROFILE
  (Lv.30 [AP3x]Bears Lair, likes 1,800, up from 1,797 in the 0438
  run). Gold VIP13 badge, grounded on the fresh screenshot at
  (575,328), opened the VIP screen.
- VIP state read live: VIP13, logged in 57 days in a row, points
  1,589,450 of 2,000,000 toward VIP 14. The rise from the 0438
  post-claim 1,586,160 is recorded, not attributed: this record
  does not say what paid it.
- Daily Freebie: the button is grey with a countdown (20:20:15 at
  first read, ticking down on re-reads), not a green Claim button
  - the freebie for this reset day is already claimed.
- Login chest: the profile VIP13 badge carried no red dot, and
  the chest icon at the top right of the VIP screen (grounded at
  (800,195)) carried no red dot either. Two taps on it, each
  verified by a following screenshot, produced no popup and no
  points change (points stayed 1,589,450). That is consistent
  with the chest already claimed, not with the unresponsive
  button blocker of earlier units: in the 0438 run a live chest
  claim paid at once with a CONGRATULATIONS popup, and here
  there is no dot to claim. Diagnostic distinction added: no dot
  plus no popup plus no points change means already claimed; a
  green Claim button that stays green after taps means button
  failure, the 0438 freebie pattern.
- The VIP Exclusive $99.99 offer was not tapped, and no
  points-plus button or cart shortcut was tapped.
- Open note, carried not resolved: who claimed this reset day's
  freebie and login chest is not established by this unit (no VIP
  record after the 19:00 reset precedes it today); the screen
  state alone proves they are claimed, not who claimed them.
- Exit: VIP screen back arrow returned to MY PROFILE, and the
  profile X returned to base, both on the first tap.

## What the 2026-11-04 0849 unit added - VIP screen entry itself blocked, badge taps unresponsive, freebie/chest state unread

- Unit vip-2026-11-03-1900 (current reset day's VIP unit, expires 2026-11-05T03:00:00Z) by ticker-0834, about 08:48 to 08:49 local, status partial. Session cc-440. Evidence in `_records_/2026-11-04/vip-rewards/0849-queue-run.md`. Nothing was claimed, and no paid VIP offer, points plus button or cart shortcut was tapped. No different-device dialog appeared.
- MY PROFILE opened from the base commander avatar. A "You're very popular!" popup from [AP3x]papillon707 (1,805 +1 likes) was dismissed with Awesome!, taking likes to 1,806 as displayed.
- Profile read live: Lv.30 [AP3x]Bears Lair, VIP13 badge with no red dot visible on it. No red dot means the freebie state could not be confirmed from the badge alone, so the VIP screen itself had to be opened.
- VIP screen entry blocked by tap method (rule R2): two taps on the VIP13 badge (norm 475,389 and the gold icon at 428,389) showed no change; a pivot closed the profile and re-entered it fresh, and a further badge tap at 475,389 again showed no change. A screenshot after the pivot verifies the profile still open with the VIP screen never reached.
- Consequence: neither the Daily Freebie state nor the login chest state could be read live in this unit, and no VIP points read before/after exists to report. Diagnostic correction to the 2138 section: no dot plus no popup plus no points change means already claimed ONLY when the VIP screen was actually opened and read (as in 2138); here the screen was never reached, so the badge's no-dot must NOT be read as claimed.
- This is a new variant of the standing repeat blocker, not a repeat of the 0438 freebie-button failure: the failure is at VIP screen entry, before any Claim button is reached. The entry-route change owed for secrets (genuine foreground activation) is the same candidate route for the next VIP unit. No new Issue filed: this blocker is already recorded in the activity metadata as a repeat blocker under rule R2.
- Tracker untouched, per the rule for partial units; the next tick re-produces vip and resumes the claim, and a failed claim re-enters the pre-reset sweep instead of waiting a full day, per the activity note. Profile closed with the X, back to the base screen.

## What the 2026-11-06 1634 unit added - Mac device offline, eighty-third consecutive pass, zero-response form

- Unit vip-2026-11-05-1800 by ticker-1634, about 16:34 to 16:40 local, status failed. Evidence in `_records_/2026-11-06/vip-rewards/1640-queue-run.md`. No VIP screen was opened, no Daily Freebie was claimed, no login chest was claimed, and no VIP points were read. This was a stale unit from the 2026-11-05 18:00 slot (planned_for 2026-11-06T02:00:00Z, expires 2026-11-07T02:00:00Z).
- No game screen was ever read and no game input was dispatched. Seven device invokes, zero responses: computer.session start on the Mac mini three times node_offline (device offline, no wake-up path), connection.health on the Mac mini node_offline, connection.repair (target web) on the Mac mini node_offline, connection.repair (target native) on the recovery device node_invoke_timeout after 25 seconds, connection.health on the recovery device node_invoke_timeout after 25 seconds. device.list reports the Mac mini offline with last_seen 2026-11-05T15:36:52Z (07:36 local), stale about 33 hours at pass time, unchanged since the ticker-1507, ticker-1534 and ticker-1604 passes; the recovery device also reports offline with the same stale last_seen. This meets the standing at-least-3-attempts retry rule.
- Recurrence, not a new failure class: this is the eighty-third consecutive ticker pass with a Mac device-access blocker, forty-fourth in the worsened zero-response form after ticker-1604 (eighty-second, forty-third). The blocker is filed as Issue #284 (tooling) alongside the knowledge Issue #282; this pass commented on #284 instead of filing a duplicate, and this run comments the eighty-third occurrence onto #282.
- Reading warning: this failed unit gives zero evidence about the VIP state. It must NOT be read as "freebie claimed" or "chest claimed" - the last live VIP state read is the 2026-11-02 2138 unit (both items already claimed for that reset day); the 2026-11-04 0849 unit could not even reach the VIP screen, so no VIP state has been read live since 2026-11-02; this unit rests on no read at all.
- The pass stopped after this one unit: a second unit would hit the same dead channel. Sync at pass start reaped 0, expired 0, produced 0 new units; 22 regulars already queued. Queue stats at 00:37Z: inbox 71, claimed 0, done 976, upcoming 53. The Zombie Invasion chain stays closed: the event ended 2026-10-30 about 19:00 and no Zombie Invasion tab has been seen in the Events hub since, so no fresh chain was seeded. The pre-reset zero-sweep pair for tonight's 19:00 reset (chain pre-reset-sweep-2026-11-06) sits in the inbox (pending 2), not yet due.
- Tracker untouched for failed, per the queue rules; the next tick re-produces this regular.

## What the 2026-11-07 1747 and 1812 units added - Freebie unlocks about 18:02 on its own 24-hour cycle, chest claimed for 60 points, Freebie button dead to four variants

- Unit vip-2026-11-06-1900 by ticker-1727, about 17:43 to 17:47 local, status partial. Evidence in `_records_/2026-11-07/vip-rewards/1747-queue-run.md`. Computer session cc-20, LastWar already running. One stale-observation error on a back tap (input not sent); a fresh observe showed the app unchanged and the retry landed.
- VIP screen: VIP13, points 1,603,930 of 2,000,000 toward VIP 14 (live read). Login streak reads 1 day in a row, "Collect 60 VIP points tomorrow".
- Daily Freebie NOT claimable in this unit: its button is a live countdown reading 00:16:52, then 00:16:40, then 00:15:48 across the unit's reads - it unlocks at about 18:02, not at the 19:00 reset. The rewards shown are the usual VIP13 set (puzzle piece x2, crates x13, x13, coin x13).
- Login chest (top right): no red dot; one tap produced no change, so today's login points are already collected. Nothing further was claimed.
- Unit vip-2026-11-06-1800 by ticker-1734, about 17:57 to 18:12 local, status partial. Evidence in `_records_/2026-11-07/vip-rewards/1812-queue-run.md`. Computer session cc-28, LastWar already running on the base screen. One stale-observation error on the first avatar tap (input not sent); a fresh observe and the retry landed.
- Login chest: red dot present. One tap opened a CONGRATULATIONS popup - "Today's VIP Points 60, Consecutive Login Days 2, Next Day's VIP Points 80". Points after: 1,603,990 of 2,000,000 (plus 60, live read). The chest stands open afterwards and its red dot is gone. The streak display moved from 1 day / 60 tomorrow (the 1747 pre-claim read) to 2 days / 80 tomorrow with no new login in between: the day-2 chest claim itself pays 60 and advances the streak to 2. No contradiction; the 1747 read was the pre-claim state.
- Daily Freebie: green Claim button by about 18:02, rewards puzzle piece x2, crates x13, x13, coin x13. The button did NOT respond to four input variants, each with a fresh observation and a fresh measured centre (norm about 739,637): two background clicks, one 1-second long-press, and one click after the game window came to the foreground. Points and button unchanged after every attempt. This is the known repeat blocker the activity metadata already names (2026-10-31 took neither after 5 variants). New against the 0438 unit: the foreground-window variant was tried here, and the chest tap on the same screen in the same session DID land, so input reaches the screen and only the Freebie button is dead.
- The VIP Exclusive offer ($99.99), the points + button and the cart shortcut were not tapped in either unit.
- An "Alliance Gifts received!" toast crossed the screen during the 1812 unit; it is a background event, not this unit's work, and nothing was claimed for it here.
- Contents note: the freebie contents match the VIP 13 scale already in this profile (puzzle x2, crates x13 each); the open question whether contents rotate stays open, with two more same-contents observations.
- No diamonds, money, speedups or paid buttons were used in either unit. No login or verification was demanded, and no different-device dialog appeared.
- Follow-up: the failed Freebie claim re-enters the pre-reset sweep per the metadata: the 18:30 zero sweep (unit 002) retries the claim before the 19:00 reset.

## Correction 2026-11-07 - the Daily Freebie runs on its own roughly 24-hour cycle, not on the 19:00 reset clock

- Source: the 1747 and 1812 records above, plus a re-read of the 2138 unit in this profile.
- Superseded in this profile: the Cadence claim "After the claim its button becomes a countdown to the 19:00 daily reset (about 4 hours 59 minutes at 14:00 on 2026-10-25)". The countdown runs about 24 hours from the last claim: the 1747 unit read a live countdown unlocking at about 18:02 on 2026-11-07, 58 minutes before the reset, and the 1812 unit found the Freebie green and claimable from about 18:02. The last claim was about 18:02 on 2026-11-06. The 2026-10-25 observation (countdown 4h59m at 14:00, unlock about 18:59) is consistent with the same cycle - last claim about 18:59 the previous day - and was misread as a reset clock.
- Supporting re-read: the 2138 unit on 2026-11-02 read a grey countdown of 20:20:15 at about 21:38, after the reset. Under a reset clock the countdown at 21:38 would read about 21h22m to the next 19:00 reset; observed 20:20:15 puts the unlock at about 17:58 the next day, which matches a 24-hour cycle from a claim at about 17:58 on 2026-11-02. The 2138 section's "the freebie for this reset day is already claimed" is re-read as: already claimed for the running 24-hour cycle, unlock about 17:58 the next day.
- The reset-rule paragraph in Cadence is revised with it: a round that runs after 19:00 does NOT automatically find a fresh freebie. Whether it is claimable depends on when it was last claimed (unlock is last claim plus about 24 hours), so units must read the countdown or the button live rather than assume a refresh at the reset. The 2026-10-25 owner claim at about 20:53 is re-read as the about-18:59 unlock claimed late, not as a reset-driven refresh; the paragraph's "afternoon claim" can only be the previous day's claim, since the 14:00 countdown reading rules out a claim that afternoon. The standing rule that a round is not closed without opening the VIP screen stands - as a check, not as an assumption of a fresh freebie.
- No other claim in this profile changes: the login chest, the streak and points reads, and the Freebie-button failure mode are all re-confirmed by the two units.

## What the 2026-11-07 1830 unit added - avatar-tap route blocked by the popularity popup, VIP entry not located, freebie not retried

- Unit vip-2026-11-06-1800 by ticker-1818, about 18:29 to 18:30 local, status partial. Evidence in `_records_/2026-11-07/vip-rewards/1830-queue-run.md` (commit f04c2b11d on records/2026-11-07). Computer session cc-30 dropped after the previous unit; session cc-33 was started, LastWar re-selected, and no game state was lost.
- Login chest: already claimed by ticker-1734 (+60 VIP points, 1,603,930 to 1,603,990, streak 2 days, per vip-rewards/1812-queue-run.md). Nothing to claim in this unit.
- Daily Freebie: NOT retried in this unit. The avatar tap opened MY PROFILE, but a "You're very popular!" popup covered it ([AP3x]Roronoa zo liked the profile, 1,806 likes +1); the popup was dismissed with the plain blue "Awesome!" button (no price tag, no spend), and the clean profile then showed likes 1,810, Moments "No posts found", and bottom tabs Record, Account, Settings, Rankings, Follow - no VIP entry on this screen. The VIP screen entry was not located before the token was released.
- Entry-route correction: the "How to enter" route (avatar tap, then the gold VIP badge on the profile) can be obstructed by the popularity popup, and the profile's bottom tabs carry no VIP entry - the badge sits elsewhere on the profile and its position needs a fresh read on the next unit. Do not assume the badge is on the tabs row, and do not treat a popup-covered profile as the VIP screen. The freebie button's standing repeat blocker (ticker-1734: unresponsive across four input variants at norm about 739, 637) therefore stands, and this unit adds no new variant to it.
- The token was released at 18:30 so the 18:34 tick can take it and run the 18:30 zero sweep (unit 002), which retries the freebie before the 19:00 reset per the ticker-1734 handoff. Whether that retry ran is unknown at this run's close; the freebie was still unclaimed at the reset, and the next claim window is the next cycle's units (the freebie unlocks about 18:02 daily on its own roughly 24-hour cycle, per the Correction above).
- Figures read live: power 149,850,353; food 476.8M, iron 800.4M, coin 5.7M. Profile likes 1,806 before the popup dismissal, 1,810 after (measured). No diamonds, money, speedups or paid buttons were used. No login or verification was demanded, and no different-device dialog appeared.
