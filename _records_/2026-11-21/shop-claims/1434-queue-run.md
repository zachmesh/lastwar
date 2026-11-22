---
title: Passes queue run 1434
created: 2026-11-21T22:45:00Z
modified: 2026-11-21T22:45:00Z
version: 1.0.0
description: Queue unit passes-2026-11-21-1057, ticker-1434 - Hot Deals free Military Training Pack claimed; Weekly Pass Free Supply already claimed; no owned pass daily pickup outstanding; monthly pass not owned
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-21 14:38-14:49 PT
  - source: unit passes-2026-11-21-1057 in _queue_/done
  - source: GitHub Issue #648 (window state), read live via the VPS gh CLI
---

# Passes queue run 1434 (ticker-1434)

Unit passes-2026-11-21-1057, regular passes, window 10:57 PT slot,
expires 14:57 PT. Executor ticker-1434. Session window about
14:38 to 14:49 PT. Token acquired 14:34 PT, released before expiry.

## Outcome

Done - one free claim made, everything else checked and nothing
further claimable. This is the first successful game unit since
ticker-1318 (13:20-13:31 PT) and ends the run of seven consecutive
game units blocked by the Issue #648 window precondition: the
Last War window (105986, pid 5136, 788x1083) is back on the user's
current Space - activate with raise=true returned brought_to_front
true and raised true this pass, where ticker-1404 at 14:08 PT was
refused with "raising it would switch the user's Space".

## What was claimed

- Hot Deals free pack - Military Training Pack, Free Claim button:
  Iron Chest (UR) x1, Food Chest (UR) x1, Coin Chest (UR) x1,
  5m Speed-up x200. CONGRATULATIONS popup confirmed the payout;
  the pack then read "Packs sold out". Timer on the pack before
  claiming showed 03:22:48 remaining.

## What was checked

- Weekly Pass tab: Free Supply chest reads "Claimed" (already
  claimed today, auto-claims on page open). No owned pass has a
  claimable Daily Pickup: the S2 Drone Components Weekly Pass
  (Legendary), the S1 Drone Parts Weekly Pass (Epic), the middle
  card and the Coin Weekly Pass (Elite, Daily Pickup x3, Total 21)
  all show a $4.99 "Get Now" button - repurchase offers, not
  owned passes. The Legendary row's "Take All $19.99" was not
  tapped (red line). List scrolled to the bottom; Coin Weekly
  Pass is the last card.
- Super Monthly Pass tab: Monthly Pass page shows a "Buy x1"
  button (250) and "Switch" - the pass is not currently owned,
  so there is no daily gift to claim. Nothing was bought.
- Season passes were not hunted in the Season hub: per the
  activity metadata (2026-11-08 check, Issue #469) the Season
  II Week 8 hub path is stale and holds no pass claim.

## What was verified live

- Mac mini (Zhen's Mac mini, 1c817413-83e2-0545-cb90-36d5e096a6bd)
  is online; computer.session cc-14 started and ended cleanly.
- HUD at the base screen, unchanged through the unit: food
  730.5M, iron 1.1G, coin 88.2M, diamonds 5,236, total power
  149,653,371, survivors 17.72K. The account state matches
  ticker-1318/1404 exactly - the owner did not play between
  13:31 and 14:38 PT.
- Own PRs first: PR #762 "records: 2026-11-21" is OPEN,
  mergeable CLEAN, zero comments, zero reviews, read live via
  the VPS gh CLI. Nothing addressed to this job, nothing to fix.
- Zombie seeding: not done. The Zombie Invasion event ended
  2026-10-30; no fresh chain is seeded until the tab is seen
  live again.
- No Touch ID was used, no password was typed, no login was
  demanded, no "active on a different device" dialog appeared.
  No diamonds or money were spent; no paid button was tapped.

## Result stats

- target: claim the Hot Deals free pack, Weekly Pass Free Supply
  and daily pickups, Monthly Pass daily gift
- achieved: 1 claim (Military Training Pack free)
- resources_gained: Iron Chest (UR) x1, Food Chest (UR) x1,
  Coin Chest (UR) x1, 5m Speed-up x200
- costs: about 11 minutes device time, no stamina or items
- verified: yes (claim popup, Free Supply Claimed state, and
  the $4.99 offer buttons all read live in this unit)
- blocker_category: none

## Delivery

- Commit to records/2026-11-21 via a temporary worktree;
  push via the VPS route, ls-remote verified. PR #762
  already open for the branch, no new PR owed.

## Delivery addendum (15:00 PT, rebased onto the remote tip)

- The local records/2026-11-21 branch (b980487a, ticker-1404's held
  commit) and the remote branch tip share no merge base: the remote
  tip moved to 2f36482d3b (pr-integration 1410, rebuilt line) and
  then 40381750c6 (tool-development 1432), and neither contains
  ticker-1404's mail record. This pass's commit was therefore
  re-applied onto the remote tip 40381750c6 in a fresh delivery
  worktree instead of pushing the stale-based commit: the two new
  files and the INDEX / action-log appends land cleanly on top of
  it (no file in this commit exists in the remote tree). The local
  commit e92d9331 on records/2026-11-21 stays as the held local
  line alongside ticker-1404's b980487a; landing that held line
  (mail-1404 record + unit) remains the integrator/recovery
  route's job, not this pass's.
