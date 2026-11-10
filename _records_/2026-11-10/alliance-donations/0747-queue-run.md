---
title: Alliance donations queue run 0747
created: 2026-11-10T15:58:00Z
modified: 2026-11-10T15:58:00Z
version: 1.0.0
description: Ticker-0734 donations unit, 7 count-verified coin donations plus 1 EXP-verified War-tab tap, close unverified behind the cooldown timer
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-10 07:47 to 08:02 local
---

# Alliance donations - ticker-0734 queue run

- Executor: ticker-0734
- Unit: donations-2026-11-10-0603, claimed 07:44:52 local
- Session window: about 07:47 to 08:02 local
- Status: partial, verified no (no live 0/30 count read; final tap EXP-verified only)
- Tracker: untouched

## Entry

- The game was left on the Events hub Drone Boost screen by the
  ticker-0704 pass. The back arrow returned to the base screen
  (Total Power 148,058,020 live).
- Alliance shield grounded fresh from the current base screenshot
  at norm (931, 714); the tap opened the Alliance menu on the
  first try. Alliance Techs tile grounded fresh at (686, 674);
  opened on the first try. The (903, 787) centre stays withdrawn.
- Development tab at entry: Auto Rally Max Level, Quick
  Construction 8/10, Great Helper Max Level, one node 2/10 below
  (uninspected). Tech Donation Today footer 6,000 at entry,
  display only, never a closing figure (Issue #558).

## Quick Construction - 7 coin donations, count-verified

- Panel live at entry: Quick Construction 8/10, Increased Building
  Speed for Allies, Donation Reward plus 20 percent, Tech EXP
  2.6M/6.0M, Current plus 20 percent, Next Level plus 22.5
  percent, Donation Reward EXP 50 plus badge 50 per donation,
  coin Donate 900, diamond Donate 2 (never used). The red-panda
  badge sits on this panel.
- Donation Count, every figure read live in this unit: 8/30 at
  entry, then 7/30, 6/30, 5/30, 4/30, 3/30 (image-verified at
  3/30), one coin tap each. Seven coin donations confirmed by
  those live count reads. Coin spent 6,300.
- Tap 6 first dispatch failed with a control-channel
  outcome_unknown ("target closed or changed before dispatch");
  the count still read 3/30 live afterwards, so no donation
  landed from it. The retry landed: 2/30 image-verified.
- The "Hold down for easier continuous donations" tooltip
  appeared after tap 3; single taps were kept, no long-press used.
- Footer after the Quick Construction donations: 6,500,
  observed only. Plus 500 for 7 donations does not divide by
  50 per donation; the footer stays disqualified (Issue #558).
- Tech EXP display stayed 2.6M/6.0M throughout (too coarse to
  show a per-donation step).

## The 1/30 stop and the War-tab changed route

- At the live-read 1/30 the unit stopped on Quick Construction
  per the changed route (standing, R2): no tap from 1/30 on
  Quick Construction.
- War tab: two upward drags scrolled the tree (World
  Interception, Rapid Siege, Quick Garrison 5/10, Troop
  Movement 5/10, then the Rallied row). Rallied HP 7/10,
  Rallied Attack 7/10, Rallied Defense 7/10, all unchanged
  since the 2026-11-08 23:51 full read.
- The red-panda badge now sits on the Troop Movement tile,
  not on Rallied Attack as in the 2026-11-08 2350 read. The
  recommended marker has moved; the next unit reads it fresh
  instead of assuming Rallied Attack.

## Rallied Attack - the 1/30 tap, EXP-verified

- Panel live at entry: Rallied Attack 7/10, Increased Hero
  Attack in Rallies for Allies, Tech EXP 24.5K/4.5M, Current
  plus 7 percent, Next Level plus 8 percent, Donation Reward
  EXP 50 plus badge 50 per donation, coin Donate 800, diamond
  Donate 2 (never used).
- Donation Count 1/30 live on Rallied Attack, read minutes
  after Quick Construction read 1/30 live. Paired-read
  evidence for the shared/global count model (Issues #160,
  #450), matching the 2026-11-10 0129 paired read.
- The first 1/30 tap dispatch failed with a control-channel
  stale_observation ("target app exited or restarted",
  input_dispatched false). The app had NOT exited: on
  re-observe the Rallied Attack panel was still open with
  the count still 1/30 live. The retry dispatched.
- After the tap the coin button greyed with a 00:07:30
  cooldown timer, hiding the count label. Tech EXP moved
  24.5K to 24.6K, plus 100: by the 2026-11-02 0259
  EXP-delta check the tap LANDED. The closing 0/30 was
  NOT read live, so per the hard closing rule this unit
  does not claim the day done: status partial, verified
  no, tracker untouched. Same close shape as the
  2026-11-08 2350 unit.
- Coin spent on Rallied Attack: 800 for the one tap.

## Totals

- Coin donations: 8 (7 count-verified on Quick Construction,
  1 EXP-verified on Rallied Attack). Coin spent 7,100.
- No diamonds spent, no diamond button tapped.
- Replenishment data point (Issue #160): count 1/30 at
  01:29 (0129 unit) to 8/30 at about 07:52, plus 7 over
  about 6 hours 23 minutes, about 1 per 55 minutes as a
  two-endpoint estimate only, NOT a measured rate. Slower
  than the about 1 per 20 minutes estimate from
  2026-11-01 and 2026-11-02.
- Follow-up: a named re-read unit is enqueued for after the
  00:07:30 cooldown (not before 08:08 local). The next
  unit re-reads the Donation Count live first; a live 0/30
  read closes the burst, a replenished count above zero
  means donate again. The next unit also re-reads the
  recommended marker fresh (now on Troop Movement).
