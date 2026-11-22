---
title: Survivor intake queue run 2116
created: 2026-11-22T05:30:00Z
modified: 2026-11-22T05:30:00Z
version: 1.0.0
description: Queue unit survivors-2026-11-21-1803, ticker-2104 - 3 survivors recruited at the front gate (Charles, Alyssa, Chloe); line clear of question-mark bubbles; Quick Dispatch not run inside the unit cap
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-21 21:16-21:30 PT
  - source: unit survivors-2026-11-21-1803 in _queue_/done
---

# Survivor intake queue run 2116 (ticker-2104)

Unit survivors-2026-11-21-1803, regular survivors,
activity survivor-intake, priority 3, est 3 minutes,
expires 2026-11-22T06:03:00Z (22:03 PT). Executor
ticker-2104. Session window about 21:16 to 21:22 PT.
Token held 21:16 to 21:22 PT (released 21:22; lease ran to 21:31); unit claimed
21:16 PT, lease to 21:36 PT. Computer session cc-43
(shared with the radar unit of the same pass).

## Outcome

Partial - 3 survivors recruited at the front gate and
the line verified clear of question-mark bubbles, but
the standing Quick Dispatch step was not run inside
the unit cap. No diamonds or money spent, no stamina
spent, no items used. The tracker is untouched
(partial re-produces next tick). This partial is NOT
identical to the 22 queue-era partials the retro of
2026-10-31 records: those never verified a gate line;
this unit grounded the line fresh, verified three
figures before tapping, and worked it to clear. The
remainder is only Quick Dispatch.

## Device state

- Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd)
  online. Computer session cc-43.
- LastWar window 105986 in windowed mode (763x1050),
  frontmost on entry; no different-device dialog, no
  login demanded, no Touch ID, no password typed.

## What happened

- Gate line verified before any tap (retro R2 rule):
  visual grounding on a fresh base screenshot found
  3 survivor figures with question-mark bubbles at
  norm (119,739), (154,717), (185,698). A fourth
  bubble was visible but its figure was not grounded
  as a survivor; it resolved during the unit as the
  visitor below.
- Tap 1 on (119,739) opened "New Survivor Incoming!"
  - CHARLES, Gold Miner, Gold Mine, Boost Coin Output
  +16.00%. Recruit tapped at norm 493,760; the card
  closed back to the base (no auto-advance this
  time). Bubble count at the gate fell from 4 to 3.
- Tap 2 on the re-grounded leftmost figure (104,710)
  opened no card and no dialog on the screenshot
  after it; the bubble count fell from 3 to 2
  question marks plus 1 yellow exclamation bubble.
  Read as a dialog-type survivor who spoke and walked
  in without a card (the profile's dialog-survivor
  case), though no dialog text was captured on the
  follow-up screenshot - the count change is the
  evidence, and the survivor is unnamed in this
  record. A blue-capped figure was seen walking
  mid-base in the same screenshots, consistent with
  a processed survivor walking to post.
- Tap 3 on the re-grounded figure (185,710) opened
  "New Survivor Incoming!" - ALYSSA, Keeper,
  Increase Coin Protection +2.00%. Recruit tapped;
  the card advanced to the next survivor.
- Tap 4 on Recruit for the advanced card - CHLOE,
  Farmer, Farmland, Boost Food Output +16.00%.
  Recruit tapped; the card closed back to the base.
- Closing gate read: no question-mark bubbles remain
  at the gate. One yellow exclamation-mark bubble
  stands - a visitor, not a recruit, per the profile;
  left untouched (tapping it opens a Friendly
  Visitor dialog asking to enable notifications).
- Quick Dispatch: one attempt, one no-change tap on
  the Farmland crop fields at norm 432,448 - no
  building panel opened. Per R2 the method ends
  there inside this unit. The unit closed at 21:22
  with token time still remaining, so the step was
  left as the named remainder rather than forced
  through a second entry route in the same unit.
  The 2026-10-25 precedent records Quick Dispatch as
  a no-op when tried (posts already full, assignment
  automatic), so the risk of leaving it is low, but
  it stays the named remainder for the next unit.

## Closing reads

- Recruits: Charles (Gold Miner, Gold Mine, Boost
  Coin Output +16.00%), Alyssa (Keeper, Increase
  Coin Protection +2.00%), Chloe (Farmer, Farmland,
  Boost Food Output +16.00%), plus one unnamed
  dialog-type survivor taken in without a card.
- Gate line: clear, 0 question-mark bubbles; 1
  visitor exclamation bubble standing, untouched.
- Base totals unchanged across the unit: food
  755.0M, iron 1.1G, coin 103.9M, diamonds 5,246,
  gold 17.72K, power 149,653,371; stamina 83 to 84
  (regenerating).

## Remaining work

- Quick Dispatch in a building panel for the new
  recruits (Farmland for Chloe, Gold Mine for
  Charles) - first action of the next survivors unit,
  per R7 (a subtask deferred inside its unit becomes
  the first action of the next unit of that type).
- The visitor exclamation bubble stays untouched
  unless the owner asks otherwise.

## Result stats

- target: take in every waiting survivor at the front gate, then run Quick Dispatch
- achieved: 3 named recruits (Charles, Alyssa, Chloe) plus 1 unnamed dialog survivor; gate line clear; Quick Dispatch not run
- resources_gained: 3 posted survivors (Boost Coin Output +16.00%, Increase Coin Protection +2.00%, Boost Food Output +16.00%)
- points: 0
- costs: about 6 minutes device time, no stamina or items
- verified: yes (figures grounded before tapping, cards read live, gate re-read clear at close)
- blocker_category: h (by-design partial - unit cap reached with Quick Dispatch still to run)
- survivors_recruited: 3
- survivors_dialog: 1
- gate_clear: yes
- quick_dispatch_run: no

## Delivery

- Commit to records/2026-11-21 via a temporary worktree;
  push via the VPS route; PR #793 already open for the
  branch, no new PR owed.
