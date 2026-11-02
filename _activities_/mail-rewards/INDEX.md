---
title: Mail Rewards
created: 2026-10-25T18:58:00Z
modified: 2026-11-02T05:39:49Z
level: L1
version: 1.5.0
description: Claiming reward mail and checking report mail, one activity folder for mail knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner structure direction on activity folders, 2026-10-25
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1306 mail unit)
  - source: in-game screens observed on the owner Mac mini, 2026-11-01 (1730 mail unit)
  - source: mail-rewards execution record 2026-11-01 2131 queue run (ticker-2104 unit, partial, Alliance-panel back arrow stalled on background input)
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


## Open questions

- Which recurring senders are worth keeping unread as evidence, and which
  reward mails expire if not claimed in time.
