---
title: Donations re-read 0406 queue run
created: 2026-11-08T12:07:00Z
modified: 2026-11-08T12:07:00Z
version: 1.0.0
description: Ticker-0334 donations re-read unit - 2 coin donations landed live, third tap unconfirmed behind cooldown timer
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-08 about 03:57 to 04:06 local
---

# Donations re-read - 0406 queue run

Unit donations-2026-11-08-0843 by ticker-0334, session about
03:52 to 04:06 local. Status partial with an unverified close
under the hard closing rule. The tracker is untouched and a
named re-read unit is enqueued for after the cooldown
(not-before about 04:17 local).

## Entry

- The game opened on the Events hub with a REWARDS panel for
  Frontline Breakthrough (all three rows 0 progress, Claim
  buttons greyed). The panel X at norm (819, 200) closed it;
  nothing was claimed. The back arrow at norm (183, 946)
  returned to the base screen.
- Alliance button re-grounded fresh from the base screenshot
  at norm (935, 708) (shield centre, matches the 0259/2348
  groundings) and opened the alliance menu at once.
  [AP3x] The Apex, Power 13,363,455,935, Members 96/100.
- Alliance Techs tile re-grounded at norm (674, 679) and
  opened ALLIANCE TECHS at once. Development tab selected.
- Recommended marker (red thumbs-up) sits on Quick
  Construction, 8/10, Development tab - not on a War-tab
  node this unit. Tech Donation Today footer read live 2950
  at tree entry (above the 1000 reward line).
- Quick Construction node re-grounded at norm (280, 515) and
  opened its panel at once.

## Target panel, read live

- Quick Construction 8/10, Increased Building Speed for
  Allies, Donation Reward +20%.
- Tech EXP Required 1.2M/6.0M, Current +20%, Next Level
  +22.5%, Donation Reward EXP 50 + badge 50.
- Donate buttons: diamond 2 (Unlimited Attempts, never
  tapped) and coin 900 (green).

## Donations, every figure read live in this unit

- Donation Count 3/30 at entry (screenshot-verified).
- Tap 1 on the coin Donate button at norm (648, 764):
  count re-read 2/30 live. One donation landed, 900 coin.
- Tap 2 on the same button: count re-read 1/30 live. One
  donation landed, 900 coin.
- Tap 3 on the same button: the coin button greyed with a
  00:10:25 cooldown timer and the Donation Count label is
  hidden behind the timer. The "Hold down for easier
  continuous donations" tooltip appeared. The closing 0/30
  was NOT read live in this unit.
- Per the hard closing rule this unit does not claim the day
  done on arithmetic: status partial, verified no, tracker
  untouched. Two coin donations are confirmed landed
  (3/30 to 1/30); the third tap is unconfirmed - a tap that
  greys the button is not a landed donation until the count
  is re-read after the timer (2018 lesson).
- Supporting only, not a closing figure: the alliance badge
  count in the top bar moved 301.0K to 301.2K to 301.3K
  across the three taps, consistent with donations landing
  but at 0.1K rounding it proves nothing alone.

## Replenishment data point, GitHub Issue #160

- The 0034 unit left this count at a live-read 1/30 plus
  one unconfirmed tap at about 00:43 local. This unit read
  3/30 live at about 04:00 - the count rose by about 2 over
  about 3 hours 17 minutes. Third confirmation of the
  between-units rise; the mechanism measurement per #160
  (short-interval reads across one cooldown cycle, the cap,
  the 19:00 reset behaviour) is still owed. A comment with
  this data point belongs on #160.
- The cooldown timer seen here, 00:10:25, sits inside the
  15 to 19 minute range recorded for #160.

## Pass context

- This pass's first job was the PR #430 conflict: the
  records/2026-11-08 branch conflicted against main 0b4a8a41
  (PR 426 merged at the 03:00 batch) on 11 files. Resolved
  branch-side by merging main into records/2026-11-08
  (merge commit f5442a885b after an amend): done add/add
  results kept from the branch (later, evidence-backed
  executions), the donations re-read duplicate dropped to the
  fresher 0843 unit, the scout successors kept, the
  observation file unioned (728 lines), the action log
  unioned and timestamp-sorted (1119 lines), six stale
  2026-11-07 2230 inbox copies removed (expired by
  planner-0240). One self-caught error during the merge: the
  first merge commit staged the 0843 file with unresolved
  conflict markers still inside it; caught by the queue
  tool returning unit 0745 for file 0843.md, fixed by
  restoring the branch version and amending before any push.
  Merge-tree probe clean after the fix. The resolution is
  reported on PR #430.
- Root cause note for the retro: the 11 conflicts all trace
  to the records/2026-11-07 and records/2026-11-08 branches
  staging and executing the same pool units while 426 was
  unmerged - the same duplicate-execution pattern the 0244
  pass filed as a pool-divergence issue. The three done
  add/add files are duplicate executions of the same unit
  ids on the two branches.
- No zombie chain seeded: the event ended 2026-10-30,
  chain closed at unit 066.
- Game left safe: Alliance Tech panel open on Quick
  Construction (greyed coin button, 00:10:25 timer running),
  base framing untouched, no purchase, no diamond spent.

## Result stats

- target: 3
- achieved: 2
- resources_gained: none
- costs: 3m_wall_1800_coin
- verified: no
- blocker_category: h
- donations_landed: 2
- donation_count_before: 3
- donation_count_after: 1
- follow_up: re-read enqueued for about 04:17 local
