---
title: Survivor intake queue run 0548
created: 2026-11-22T13:49:00Z
modified: 2026-11-22T13:49:00Z
version: 1.0.0
description: Queue unit survivors-2026-11-22-0203, ticker-0537 - gate line cleared, 7 named recruits plus 1 dialog survivor taken in; Quick Dispatch not run, building panel entry not located
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-22 about 05:40 to 05:48 PT
  - source: unit survivors-2026-11-22-0203 in _queue_/done
---

# Survivor intake queue run 0548 (ticker-0537)

Unit survivors-2026-11-22-0203, regular survivors,
activity survivor-intake, priority 3, est 3 minutes,
expires 2026-11-22T14:03:00Z (06:03 PT). Executor
ticker-0537. Session window about 05:40 to 05:48 PT.
Token acquired 05:40 PT (lease to 05:55 PT); unit
claimed 05:40 PT, lease to 06:00 PT. Computer session
cc-104. Unit duration about 8 minutes.

## Outcome

Partial - the gate line was cleared and verified
clear by screenshot, but Quick Dispatch was NOT run.
Seven named survivors were recruited and one dialog
survivor walked in. No diamonds or money spent, no
stamina spent, nothing enabled, no message sent. The
tracker is untouched (partial re-produces next tick).

## Device state

- Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd)
  online. Computer session cc-104.
- LastWar running on entry, left on the radar screen
  (11 task rewards claimable, radar restore in
  00:56:43). The radar Claim All was NOT tapped - it
  belongs to the radar regular, not this unit. The
  home button at norm 896,936 returned to the base.
  No different-device dialog, no login demanded, no
  Touch ID, no password typed.

## What happened

- Gate grounding: visual grounding on a fresh base
  screenshot located a survivor figure with a "?"
  bubble at norm 105-160, 645-760 (centre 132,702)
  and the front gate entrance at 125-320, 575-755.
  The tap on the figure opened the New Survivor
  Incoming card chain.
- Recruits, each read live from its card and
  recruited with the Recruit button at norm 495,754:
  1. CATHERINE, Vault Keeper, Coin Vault, Increase
     Coin Protection +3.00%
  2. MARCUS, Attendant, Tavern, Free Hero Recruitment
     CD reduced 3hr
  3. JOLENE, Mechanic, Gear Factory, Crafting Speed
     +4.80%
  4. MARIA, Mechanic, Gear Factory, Crafting Speed
     +4.80%
  5. MICHAEL, Gold Miner, Gold Mine, Boost Coin Output
     +32.00%
  6. LAUREN, Nurse, Hospital, Unit Healing Speed
     +10.00%
  7. ELINA, Hunter, Armed Truck, Increases the time
     that armed truck loot can accumulate 1hr 30min
  ELINA was recorded on 2026-10-25 as Keeper,
  Warehouse - names repeat across roles, as the
  activity metadata already notes.
- Dialog survivor: after the card chain closed, two
  "?" figures remained at the gate. The first tap
  (norm 110,694) opened a dialog survivor whose line
  read "...welcome"; it walked in with no card. The
  second (norm 164,704) opened ELINA's card above.
- Gate clear verified: after ELINA's Recruit the
  card closed and a fresh screenshot showed no "?"
  bubbles remaining at the front gate.
- Quick Dispatch NOT run (named remainder, R7):
  the tap on the grounded Iron Mine cluster centre
  (norm 343,205) selected the Smelter Lv.26 and
  showed only its label tag - no details panel, no
  paw button. A second tap on the Smelter body
  (norm 358,168) scrolled the map and selected the
  Eternal Pyramid Lv.3, showing a radial menu
  (recycle icon and green up-arrow) - again no
  details panel and no paw button. Per R2 the
  tap-the-building-centre method ends here inside
  this unit: it selects and labels, it does not open
  the Building Details panel. The next survivors
  unit must try a different entry - tap the
  building's label tag itself, or long-press the
  building, or use the selected building's name
  plate - before concluding Quick Dispatch cannot
  run. This is the 23rd consecutive queue-era
  survivors unit without a Quick Dispatch run; the
  blocker is the panel entry, not the line.

## Remaining work

- Quick Dispatch in a building panel for the 7
  recruits taken in this unit (Coin Vault for
  Catherine, Tavern for Marcus, Gear Factory for
  Jolene and Maria, Gold Mine for Michael, Hospital
  for Lauren, Armed Truck for Elina) is the first
  action of the next survivors unit per R7, with
  the changed entry method above.
- The gate line is clear as of 05:48 PT; the next
  unit re-verifies it fresh before any tap.

## Result stats

- target: take in every waiting survivor at the front gate, then run Quick Dispatch
- achieved: 8 survivors taken in (7 named recruits plus 1 dialog survivor); gate verified clear; Quick Dispatch not run
- resources_gained: 7 recruits posted with traits (Coin Protection +3.00%, Hero Recruitment CD -3hr, Crafting Speed +4.80% x2, Coin Output +32.00%, Unit Healing Speed +10.00%, armed truck loot accumulation +1hr 30min)
- points: 0
- costs: about 8 minutes device time, no stamina or items
- verified: yes (intake counts and gate-clear read live in this unit; Quick Dispatch honestly not run)
- blocker_category: e (repeated blocker - building panel entry for Quick Dispatch, 23rd consecutive survivors unit without it)
- survivors_recruited: 7
- survivors_dialog: 1
- gate_clear: true
- quick_dispatch_run: no

## Delivery

- Commit to records/2026-11-22 via a temporary worktree;
  push via the VPS route; PR #812 already open for the
  branch, no new PR owed.
