---
title: VIP Rewards
created: 2026-10-25T20:46:00Z
modified: 2026-11-02T13:45:00Z
level: L1
version: 1.7.0
description: Claiming the daily VIP gift and VIP level rewards, one activity folder for VIP claim knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner task request naming VIP rewards, 2026-10-25
  - source: pre-reset zero sweep execution record 2026-11-01 1757 queue run (lines 12-13)
  - source: ticker-1904 queue sync reap of expired units, 2026-11-01 (vip fix-up expired, attempts 0)
  - source: vip-rewards execution record 2026-11-02 0438 queue run
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
