---
title: Alliance donations queue run 1308
created: 2026-11-22T21:08:00Z
modified: 2026-11-22T21:08:00Z
level: L0
version: 1.0.0
description: Donations unit donations-2026-11-22-1003, ticker-1234, 14 coin donations verified live on Quick Gathering, count 15/30 to 1/30, stopped at the 1/30 floor per the changed route
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-22 about 12:59-13:08 PT
  - source: unit donations-2026-11-22-1003 in _queue_/done
  - source: _activities_/alliance-donations/INDEX.md version 1.103.0
---

# Alliance donations queue run 1308 (ticker-1234)

Unit donations-2026-11-22-1003, regular donations, segment 1.
Executor ticker-1234. Computer session cc-149. Session window
about 12:59 to 13:08 PT. Game windowed 642x951, window 127196,
activated with raise=true after list_windows (the duplicate
window 127250 was left untouched, per Issue #822). No "active
on a different device" dialog. No login or verification demanded.

## Outcome

Partial - 14 coin donations verified live, Donation Count
15/30 to 1/30 on Quick Gathering, stopped at the live-read
1/30 floor per the changed route (no tap from 1/30). The coin
Donate button stayed green with no cooldown timer at the
close. The last donation falls to the next staged donations
unit (donations-2026-11-22-1403, 14:03 slot); no separate
re-read unit is enqueued - the close is verified by the live
1/30 read and the button is green with no timer, so the next
regular unit continues. Tracker untouched (partial).

## Entry - read live about 13:00

- Base screen: power 147,972,169, food 765.4M, iron 1.1G,
  coin 109.2M, diamonds 6,436. "Build: Oil Well [0/1]"
  banner at the bottom. The 2026-11-21 1340 entry blocker
  (Alliance button unresponsive in windowed 788x1083) is
  NOT present in this 642x951 window state.
- Alliance shield grounded fresh from the current base
  screenshot at norm (929, 706) - opened the Alliance
  menu on the first try ([AP3x] The Apex, Leader Abyss
  Apex, Power 14,495,773,681, Members 99/100, Language
  English). Alliance Techs tile grounded fresh at
  (687, 682) - opened ALLIANCE TECHS on the first try.

## Tree - read live about 13:01-13:03

- Development tab at entry: Auto Rally Max Level, Quick
  Construction 9/10 (was 8/10 on 2026-11-10), Great
  Helper Max Level, one node 2/10 below the fold.
  Footer Tech Donation Today 6900 at entry (display only,
  disqualified per Issue #558).
- The red-panda recommended badge sat on the partially
  visible 2/10 node (grounded 724, 714 on the first view).
  One upward drag (500, 550) to (500, 300) scrolled the
  tree and revealed it as Quick Gathering 2/10, badge
  re-grounded at (538, 330) on its tile, with Iron Output
  1/10, Food Output 1/10 and Coin Output 2/10 below it.

## Donations - every figure read live in this unit

- Quick Gathering panel: 2/10, "Faster Resource Gathering
  for Allies", Tech EXP Required 40.9K/600.0K at entry,
  Current +8%, Next Level +12%, Donation Reward 50 EXP +
  50 badge, coin Donate 300, diamond Donate 2 (never
  tapped). Weekly settlement countdown 04:56:06 at panel
  open.
- Donation Count chain, one coin tap per step, each step
  verified by a screenshot read before the next tap:
  15/30, 14/30, 13/30, 12/30, 11/30, 10/30, 9/30, 8/30,
  7/30, 6/30, 5/30, 4/30, 3/30, 2/30, 1/30. Fourteen
  coin donations landed, 4,200 coin spent (14 x 300).
- Tech EXP moved 40.9K to 42.3K across the unit (+1.4K
  for 14 donations at +50 each = +700 expected): the node
  EXP also moves with other members' donations, so it is
  not a per-tap landing check at this scale; the count
  chain is the deciding read. Top-bar badge item 349.2K
  at entry to 350.4K at close, observed only (meaning
  unpinned, not used as evidence).
- Footer Tech Donation Today 6900 at tree entry, 8350 at
  tree close (+1450 across 14 own donations, about +104
  per donation) - display only, disqualified per Issue
  #558, not used as a closing figure.
- Changed route HELD: stopped at the live-read 1/30 with
  the button green and no cooldown timer, the same end
  state as the 2249, 2354 and 0024 units. No tap was made
  from 1/30.

## Exit - read live about 13:07-13:08

- Panel X closed the Quick Gathering panel, tree X closed
  ALLIANCE TECHS, the Alliance menu back arrow returned
  to the base screen, verified (power 147,972,169, coin
  109.2M, "Build: Oil Well [0/1]" banner).
- No diamonds or money spent, no paid button tapped, no
  red line touched.

## Result stats

- target 30, achieved 14, verified yes, blocker_category h
  (by-design partial - changed-route stop at the 1/30
  floor, last donation handed to the next staged unit)
- count_before 15, count_after 1, coin_spent 4200,
  donations 14, node Quick Gathering, cost_per_donation 300
