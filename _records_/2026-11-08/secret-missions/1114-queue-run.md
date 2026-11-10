---
title: Secret missions queue run 1114
created: 2026-11-08T19:07:00Z
modified: 2026-11-08T19:15:00Z
level: L0
version: 1.0.0
description: Ticker-1049 secrets unit, 4 finished tasks claimed with PERFECT stamps, Mega Deploy and Reward Recovery not reached in cap
status: unverified
---

# 1114 queue run - secret missions

Executor: ticker-1049. Unit: secrets-2026-11-08-0657.
Session window about 11:07 to 11:15 America/Los_Angeles.

## Performed

- Duel posture read first (tools/duel.py --json): Day 7,
  off day - settlement, no scoring actions - so the
  duel-day Mega Refresh rule does not apply and normal
  Mega Deploy is the default.
- Mac mini online and Last War already running
  (com.lastwar.ios). At entry the game sat on the
  Alliance Contribution Ranking screen left over from
  the previous unit of this pass; navigated back through
  the Season Calculating screen and the Season hub to
  base without touching anything. Total Power read live
  on base: 149,850,353.
- Secret Command Post opened from the base left-column
  slot at norm 53,625 and its title verified before any
  further tap. Live state read: Assist Allies 0/5,
  Plunder Others 0/5, Your Tasks badge 17, Ally Tasks
  badge 5. Four finished tasks visible, each with a
  green Claim button: UR Rescue Test Subject (Lv.5),
  SSR Train Refugees (Lv.5), SSR Provide Tech Support
  to Refugees (Lv.5), SSR Search for Missing Refugees
  (Lv.5).
- Claim: one tap on the first task's Claim button
  (norm 753,471) opened the CONGRATULATIONS panel
  listing four helpers who helped claim task rewards
  (three Mobile Squad Members and [AP3x]YOUGO Apex,
  timestamps 11-7 18:00 and 11-7 20:43). The Like All
  button (plain blue, no price tag) was tapped once and
  disappeared; the panel was then dismissed with the
  back arrow. Verified on the post screen afterwards:
  all four tasks now carry gold PERFECT stamps and no
  Claim button remains; Your Tasks badge reads 8
  (down from 17). The claim collected all four finished
  tasks at once, as the activity metadata states. This
  unit's Claim tap worked on the first try - unlike the
  2026-11-04 unit, whose Claim buttons were
  unresponsive to background taps; no R2 pivot was
  needed.
- Rewards as displayed on the four task cards before
  claiming (item identities for the two crate icons are
  unverified - the icons are recorded as shown):
  UR Rescue Test Subject - orange crate x5, green crate
  x57, 12.3M Hero EXP, puzzle piece x1, 2.4K blue
  triangle; SSR Train Refugees - orange crate x1, green
  crate x57, 2.4M Hero EXP, 480, 150; SSR Provide Tech
  Support to Refugees - orange crate x1, green crate
  x57, 2.4M Hero EXP, 290, Lv.1 chest x5; SSR Search
  for Missing Refugees - orange crate x1, green crate
  x57, 2.4M Hero EXP, puzzle piece x1, 370.
- Token note: the token lease from the previous unit
  expired at 19:08:38Z during this unit and the
  re-acquire issued at 19:08:35Z landed 3 seconds
  before expiry, so it reported the token still held
  and did not renew; the game input between 19:09 and
  19:14 therefore ran with no token held. No other pass
  could have taken it - the 11:04 tick fired while the
  first lease was still live and skipped, and the next
  tick is 11:34 - so no collision occurred. The token
  was re-acquired at 19:14:44Z (held until 19:29:44Z)
  before the unit closed.

## Not performed

- Mega Deploy of the remaining pending tasks (UR Only
  off, every task re-checked by hand) was not reached:
  the pass budget ended first. Your Tasks badge 8
  means pending tasks remain for the next secrets unit.
- Reward Recovery (Recover button) was not checked.
- Ally assists (0/5, Ally Tasks badge 5) were not used.
- Plunder Others was not touched (PvP, needs owner
  instruction).
- The Hidden Treasures tab carries a red badge 1, seen
  live on the post screen - that is the sibling
  hidden-treasures regular's work, not this unit's,
  and was not touched.

## Other pass steps

- The pass ran a passes unit first; see
  shop-claims/1054-queue-run.md.
- Tracker untouched: a partial unit does not mark the
  regular, so the next tick re-produces the secrets unit.
- Delivery note: the local working tree sits on branch
  work/ops-execution-records and holds another job's
  in-flight state (unrelated modifications and deletions),
  so this pass's outputs are delivered through a temporary
  worktree onto the records/2026-11-08 branch, leaving that
  state undisturbed. PR 430 already covers the branch, so no
  new PR is opened.

## Outcome

Partial. Four finished secret tasks claimed and verified
with PERFECT stamps; Mega Deploy, Reward Recovery and
ally assists carry to the next secrets unit. No diamonds,
money or other spending; no Mega Refresh tapped; no
alliance diplomacy, no assembly, no teleport.

## Result stats

- target 3, achieved 1, resources_gained (see Performed),
  costs 7min-no-items-spent, verified yes,
  blocker_category h, device_takeovers 0,
  follow_up mega-deploy
