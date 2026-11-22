---
title: Shop claims 2026-11-16 ticker-2236 partial, pass gifts already claimed, check-in gift unreachable
created: 2026-11-17T06:40:00Z
modified: 2026-11-17T06:40:00Z
version: 1.0.0
description: Passes unit passes-2026-11-16-1857 partial, monthly and weekly pass gifts already claimed, Hot Deals check-in FREE GIFT not reached
status: partial
grounded_in:
  - source: Last War on Zhen's Mac mini, shop screens read 2026-11-17T06:37Z to 06:49Z
  - source: GitHub public pull request list for zachmesh/lastwar via browser.open, 2026-11-17T06:35Z
  - source: VPS SSH probe, 2026-11-17T06:34Z
---

# Shop claims 2026-11-16 ticker-2236 partial, pass gifts already claimed, check-in gift unreachable

- Executor: ticker-2236
- Unit: passes-2026-11-16-1857, regular passes, activity shop-claims, priority 2, est 4 minutes
- Session window: 22:36-22:40 local, token held 22:36-22:51 local

## What happened

- Mac mini online, Last War driven live. Base HUD on entry:
  food 639.6M, iron 1.0G, coin 27.7M, power 149,482,045 -
  identical to the ticker-2102 read, no change in between.
- Nothing claimed in this unit - every pass gift already stood
  claimed, and the one remaining free item could not be reached
  (see below). No paid button was tapped; the Legendary Take All
  $19.99 row was seen and left alone.

## Weekly Pass tab

- Free Supply chest reads Claimed (auto-claimed on page open,
  per the standing note).
- S2 Drone Components Weekly Pass (Legendary): Daily Pickup x2,
  Total x7, button Get Now $4.99 - a purchase offer, pass not
  owned. S1 Drone Parts Weekly Pass (Epic): Daily Pickup x15,
  Total 105, button Get Now $4.99 - same, not owned. No Daily
  Pickup is claimable; on 2026-10-25 both passes were owned,
  so both have lapsed since.
- The list does not scroll further in this view (scroll and drag
  produced no change); no Coin Weekly Pass card is visible.

## Super Monthly Pass tab

- Monthly Pass, Squad 4 Lv.20, Days Left 5, Rewards Left 5.
- Daily Pickup items: red diamonds 1000, gold tickets x2, gold
  bars x2, stamina 60, iron 200. Button reads Claimed - today's
  gift was already taken.
- Monthly Pass Extension x1 and Get Now +2500 are paid offers,
  not tapped.

## Hot Deals - check-in FREE GIFT not reached

- Hot Deals shows no free pack on the page itself, only the vault
  promo and a two-banner carousel: (a) check-in event, FREE GIFT
  "Claim your gift today!", FREE TOMORROW x5/x5/x5; (b) points,
  "Claim points and redeem great rewards", 1000 POINTS.
- The carousel rotates between the two banners on its own. Taps
  on the banner area advance the carousel instead of opening the
  destination. Three taps on the Go button (bottom centre) while
  the check-in banner was centred produced no change at all, and
  a click_element for label "Go" failed: no enabled control in
  the window is labelled "Go" - the game canvas exposes no
  Accessibility element for it. The control channel itself notes
  background clicks do not reach some controls. This is a tooling
  gap, not a game state: the FREE GIFT is unverified - it may
  still be claimable today.
- Follow-up for the next passes unit: try the check-in event from
  the base Events screen (red badge 1 was showing) instead of the
  shop banner, or drive the game window frontmost before tapping
  Go. If the gift is still unclaimed at the 19:00 reset it lapses.

## Own PRs first

- VPS route down (SSH Permission denied, see below), so the check
  ran through the public GitHub pull request list for
  zachmesh/lastwar.
- Open PRs, unchanged since Nov 12: #711 (knowledge, Owner
  lastwar-knowledge-organizer), #708 (records 2026-11-12, Owner
  lastwar-pr-integrator), #425 (tooling, Owner
  lastwar-tool-developer). None is owned by this job; no open PR
  for records/2026-11-15 or records/2026-11-16. No question
  addressed to this job, nothing to fix.

## Sync and seeding

- Sync: reaped 0, expired 8, due 22, produced 0 (all 22 already
  queued); completion markers reaped: radar, survivors and
  training 2026-11-16-1803. Branch reconcile skipped with a
  warning: fetch of records/2026-11-16 failed (remote ref
  missing), issue #446.
- Zombie seeding no-op: the Zombie Invasion event ended at about
  the 19:00 reset on 2026-10-30 (unit 066); chain
  zombie-2026-10-28 is closed, and no fresh chain is seeded until
  a Zombie Invasion tab is seen live in the Events hub again.

## Delivery blocked

- VPS SSH still Permission denied (publickey), probed 22:34 PT,
  about 105.8 hours into the break (since ~12:46 PT Nov 12). No
  bundle, no push, no PR. The 23:00 PT integrator batch point has
  not yet passed; PR #708 still open and no records PR for
  2026-11-16.
- Delivery PARTIAL: this record is committed locally on delivery
  branch ticker-2236-1116-delivery, UNPUSHED, push pending VPS
  recovery.
- No Slack sync. Chat report owed only if this pass's final
  outcome is material (a miss or a skipped-needs-owner item);
  the check-in gift gap is recorded here and in the unit result.

## Tracker

- Untouched (partial). The regular stays due; the next tick
  re-produces it and the work resumes as a fresh unit.
