---
title: Mail Rewards
created: 2026-10-25T18:58:00Z
modified: 2026-11-01T09:36:45Z
level: L1
version: 1.2.0
description: Claiming reward mail and checking report mail, one activity folder for mail knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner structure direction on activity folders, 2026-10-25
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
  Season, System, Regular, Purchases. The train arrival reward mail of
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


## Open questions

- Which recurring senders are worth keeping unread as evidence, and which
  reward mails expire if not claimed in time.
