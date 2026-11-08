---
title: Queue Run 0110 Survivor Intake Contested
created: 2026-11-04T01:10:00-08:00
modified: 2026-11-04T01:10:00-08:00
version: 1.0.0
description: Ticker pass ticker-0104 survivors unit, contested, different-device dialog returned after two kick takeovers
status: partial
---

# 0110 queue run - survivor intake, contested

Session window: 2026-11-04 about 01:04 to 01:10 America/Los_Angeles.
Executor: ticker-0104. Unit: survivors-2026-11-03-2203 (regular
survivors, activity survivor-intake).

## Outcome

- Status: partial, contested, unverified. No survivor was
  processed, no recruit card appeared, no Quick Dispatch ran.
  Tracker left untouched, so the next tick re-produces this
  regular.
- The pass stopped under the owner kick rule: the
  different-device dialog was answered with Confirm twice in
  this pass and still came back a third time, so the owner is
  likely playing on another device at this moment. No third
  takeover was attempted. No user-facing report is made for a
  contested pass.
- No diamonds or money spent, no paid button tapped, no other
  activity worked from this unit.

## What was checked, in order

1. Own-PR check first: PR 258 (records/2026-11-04) is
   MERGEABLE with 0 comments; nothing addressed to this job.
   The other open records PRs (255, 256, 187) name Owner
   lastwar-pr-integrator, not this job.
2. Sync: reaped 0, expired 0, due 20, produced none - all due
   regulars were already queued. Pool at sync: inbox 68,
   claimed 0, done 773.
3. Zombie seeding: none. The chain zombie-2026-10-28 closed
   2026-10-30 and no Zombie Invasion tab was seen live in
   this pass, so no fresh chain was seeded.
4. Token acquired by ticker-0104. Next unit:
   survivors-2026-11-03-2203, claimed.
5. Entry state: LastWar showed a TIPS dialog "The server is
   under maintenance. Please wait a moment, we'll be back
   with you shortly!" over the login screen, with a "Login
   failed. Please retry or contact support." toast. This
   matches the ticker-0034 pass (00:34), which also met
   server maintenance at entry.
6. Confirm on the maintenance dialog dismissed it and the
   game went to its loading screen. After a 10 second wait
   the base screen was behind a TIPS dialog "Your account
   is currently active on a different device!" with a
   Confirm button.
7. Kick 1: Confirm tapped. The app exited, as the kick rule
   says it does. LastWar was reopened; the base screen was
   again behind the same different-device dialog.
8. Kick 2: Confirm tapped. The app exited again. LastWar was
   reopened; the base screen was a third time behind the
   same different-device dialog. Two takeovers already made
   in this pass, dialog still returning - stop, contested.
9. Base readings glimpsed behind the dialog, not used as
   closing figures because the base was never reached
   interactively: power 150,013,787. No gate, no survivor
   figure and no question-mark bubble was ever verified,
   so the gate line is NOT claimed empty and no survivor
   count is reported.

## Gate line

- Gate line text: NOT READ. The signed "Zombies" front gate
  was not located in this unit, so no gate line can be
  quoted verbatim and the gate is NOT claimed empty.
- The previous unit's rejected points (505,590 building
  bubble; 545,740 empty snow) were not re-tapped; this unit
  never got past the session dialogs to attempt a fresh
  full-perimeter read.

## Closing figures, read live in this unit

- Survivors processed: 0, unverified.
- Gate line at close: unverified, not claimed clear.
- Resources gained: none observed.
- verified: no. blocker_category: f (missing precondition -
  device session contested by another active device).

## Red lines

- No diamonds or money spent, no paid button tapped, no
  Renew, Finish Now, Legendary Claim All or Battle Pass paid
  unlock touched. No base move, no Assemble, no teleport.
  No furnace control touched.
