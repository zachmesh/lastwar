---
title: Alliance donations queue run 0554
created: 2026-11-22T13:55:00Z
modified: 2026-11-22T13:55:00Z
version: 1.0.0
description: Queue unit donations-2026-11-22-0203, ticker-0537 - 3 coin donations to Rallied Attack, burst exhausted, final Donation Count unreadable behind the cooldown timer
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-22 about 05:50 to 05:54 PT
  - source: unit donations-2026-11-22-0203 in _queue_/done
---

# Alliance donations queue run 0554 (ticker-0537)

Unit donations-2026-11-22-0203, regular donations,
activity alliance-donations, priority 2, est 7 minutes,
expires 2026-11-22T14:03:00Z (06:03 PT). Executor
ticker-0537. Session window about 05:50 to 05:54 PT.
Token renewed 05:50 PT (lease to 06:05 PT, re-acquired
between units after the first lease lapsed); unit
claimed 05:50 PT, lease to 06:10 PT. Computer session
cc-106. Unit duration about 4 minutes.

## Outcome

Partial - 3 coin donations landed on Rallied Attack
and the burst is exhausted (coin button greyed with a
00:04:45 cooldown timer), but the final Donation Count
was NOT read live: the timer covers the count label,
exactly the trap the hard closing rule names. Per that
rule the unit closes unverified, the tracker stays
untouched, and the re-read is the next tick's
re-produced donations unit (06:03 slot, due after the
cooldown ends about 05:59 PT). No diamonds spent, no
diamond button touched. 2,400 coin spent (3 x 800).

## Device state

- Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd)
  online. Computer session cc-106.
- LastWar running on entry, left on the base in the
  scrolled-up view from the survivors unit (Eternal
  Pyramid Lv.3 selected, radial menu open, right
  column hidden). No different-device dialog, no login
  demanded, no Touch ID, no password typed.

## What happened

- Framing restore: a tap on empty road at norm
  514,652 dismissed the building selection and the
  radial menu; the default base framing returned with
  the right column visible.
- Entry route (changed route from the 2026-11-02 R2
  note, working): visual grounding measured the
  Alliance shield centre fresh at norm 933,715 on
  this screenshot (the stored 903,787 centre belongs
  to a different framing) and the tap opened the
  Alliance menu at once - no Drill Ground pan, no
  camera move. Alliance Techs tapped at norm
  670,683.
- Tree state, War tab (live): Unit Load Capacity
  2/10, Quick Training 1/10, Expert Trainer 2/10,
  Troop Movement 5/10, Rallied HP 7/10, Rallied
  Attack 7/10, Rallied Defense 7/10. Development
  tab: Auto Rally Max Level, Quick Construction 9/10,
  Great Helper Max Level, next node 2/10. The
  recommended marker was not identified on any node
  in the views obtained; donations went to Rallied
  Attack, the standing target. The red thumbs-up icon
  seen at the top of the Development tab is
  unexplained and is not claimed as the marker.
- Rallied Attack panel, entry live read: 7/10,
  Increased Hero Attack in Rallies for Allies, Tech
  EXP Required 25.4K/4.5M, Current +7%, Next Level
  +8%, Donation Reward star 50 plus badge 50,
  Donation Count 3/30 (remaining), coin Donate 800
  active, diamond Donate 2 untouched.
- Donations, each verified by the count and EXP
  moving: 1st - count 3/30 to 2/30, EXP 25.4K to
  25.5K; 2nd - count 2/30 to 1/30, EXP 25.5K to
  25.6K; 3rd - EXP 25.6K to 25.7K, and the coin
  button greyed with a 00:04:45 timer (a "Hold down
  for easier continuous donations" tooltip showed on
  the 3rd tap; single taps were used throughout, no
  hold). The count label was not re-read after the
  3rd donation - the timer covers it.
- Corroboration: Tech Donation Today footer read
  5850 on entry and 6100 after the panel closed, a
  +250 rise. That does NOT match 3 donations at the
  50-points-each rate recorded on 2026-10-26 (+150
  expected). The mismatch is unresolved - either the
  per-donation points changed with the 800 coin cost
  (was 700), or the footer counts something beyond
  this unit's donations. The footer is not used as
  the closing count; only the panel Donation Count
  closes a donations unit.

## Remaining work

- Re-read the Donation Count live after the cooldown
  (timer 00:04:45 from about 05:54 PT, ends about
  05:59 PT): the next tick's re-produced donations
  unit (06:03 slot) is the named re-read unit. If it
  reads 0/30, the day's burst is done; if it reads a
  refilled count, donations continue under the
  refill-timer model (Issue #813).
- The +250 footer rise against +150 expected stays
  open: the next donations unit should record the
  footer before and after its own donations and
  state the per-donation points it actually observes.

## Result stats

- target: donate the remaining coin donations to the recommended technology until the button greys, closing on a live Donation Count read
- achieved: 3 coin donations to Rallied Attack, burst exhausted, final Donation Count not read live
- resources_gained: Rallied Attack EXP 25.4K to 25.7K, Tech Donation Today footer 5850 to 6100
- points: 150 contribution points expected at 50 per donation, footer rise 250 observed and unexplained
- costs: about 4 minutes device time, 2400 coin, no stamina or items
- verified: no (final Donation Count not read live; the timer covers the label)
- blocker_category: d (inference over live read - the 0/30 final is inferred from the greyed button, not read)
- donations_made: 3
- donation_count_before: 3
- donation_count_after: unread
- tech_donation_today_before: 5850
- tech_donation_today_after: 6100
- cooldown_timer: 00:04:45

## Delivery

- Commit to records/2026-11-22 via a temporary worktree;
  push via the VPS route; PR #812 already open for the
  branch, no new PR owed.
