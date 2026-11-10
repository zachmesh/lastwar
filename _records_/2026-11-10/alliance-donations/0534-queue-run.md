---
title: Alliance donations queue run 0534
created: 2026-11-10T13:52:00Z
modified: 2026-11-10T13:52:00Z
version: 1.0.0
description: Ticker-0534 donations unit - 7 coin donations verified live 8/30 to 1/30 on Quick Construction, stopped at 1/30 per the changed route, partial
status: unverified
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-10 05:37-05:51 PT
---

# Alliance donations queue run 0534 (ticker-0534)

Unit: donations-2026-11-10-0415. Status: partial.
Activity: alliance-donations.

## Entry - Alliance shield label point, Techs first try

- Base screen at entry: full-base framing, shortcut columns
  visible (the zoomed/panned state that blocked the 0323 unit
  is gone). The Alliance shield is visible at the right column.
- First tap at norm (934,685), the shield icon centre, produced
  no change. Second tap at norm (930,721), the "Alliance" label
  area below the shield, opened the Alliance menu at once -
  the same label-area point the 0011 unit used. The shield
  centre is not a reliable tap point in this framing; the label
  area is.
- Alliance Techs tile tapped at norm (709,683), the tile centre
  on the current menu screenshot, opened ALLIANCE TECHS at
  once. No entry blocker this unit (contrast the 0323 unit).

## Target and live reads

- Node: Quick Construction, Development tab, 8/10, Increased
  Building Speed for Allies. Donation Reward +20%. Tech EXP
  Required 2.6M/6.0M. Current +20%, Next Level +22.5%.
  Donation Reward row: 50 EXP + 50 badge item per donation.
  Coin Donate button: 900 coin per donation (matches the 0234
  unit; the 800-coin price of 2026-10-25 no longer applies).
  Diamond Donate button (2 diamonds) never used.
- Donation Count, every figure read live in this unit:
  8/30 at entry, then 7/30, 6/30, 5/30, 4/30, 3/30, 2/30,
  1/30 at close, one coin tap each. Seven coin donations are
  confirmed by the live reads at both ends of each step.
- Image verification: 6/30, 5/30 and the closing 1/30 were
  confirmed on screenshots. The compact OCR misreads 6 as 5
  ("5130" for 6/30) and once rendered 5/30 as "130" - the
  2026-11-01 2348 unit's OCR 6-as-5 warning still applies,
  so OCR-only steps in this unit were cross-checked against
  the monotonic sequence and the image reads.
- Tech Donation Today footer: 5100 at entry on the tree screen,
  unchanged from the 0323 unit's last-known 5100. Closing
  footer unread (display only; disqualified as a closing figure
  per Issue #558, not re-read). Coin balance 84.1M at entry and
  close (HUD rounds to 0.1M; no exact delta derived from it).
- Badge counter at the top bar moved 384.6K at entry to 385.3K
  at close (+700 across 7 donations, i.e. not +50 each) - it
  moves for reasons beyond this unit's donations, so no
  per-donation value is derived from it.

## What was done

- 7 coin donations on Quick Construction, 6,300 coin spent,
  Donation Count 8/30 to 1/30 live. No diamonds or money spent.
- Stopped at the live-read 1/30 per the changed route from the
  2026-11-08 0920 unit (third consecutive partial on the 1/30
  blocker, R2): do NOT tap from 1/30 on Quick Construction.
  The final donation goes via the War-tab node (Rallied Attack)
  in the re-read unit enqueued from this unit.
- Tap 6 anomaly: the control call returned "The target app
  exited or restarted" (stale_observation evidence error), but
  the re-observe showed the ALLIANCE TECH panel intact in the
  same window and the count reading 2/30 - the tap had landed
  (3 to 2) and no replay was made. Recorded as an evidence-route
  artifact, not an app exit; the 2026-11-01 lesson (re-read live
  before continuing after a suspected exit) was followed.
- The "Hold down for easier continuous donations" tooltip
  appeared after tap 3. Single taps were kept throughout; no
  long-press was used (the 0920 unit proved long-press
  dispatches nothing on this button).
- Recommended marker: on the Development tree screenshot the
  small round red-panda badge sat mid-tree below Auto Rally and
  above the partly visible 2/10 node - it did not sit clearly
  on Quick Construction's tile, so which node it marks on this
  tab is unverified. The 2350 unit's marker read (Rallied
  Attack, War tab) stands; the Development-tab marker form
  stays unverified. This unit donated on Quick Construction
  because it is the count-bearing node from the prior unit, not
  on a fresh marker read.

## Replenishment data point (Issue #160)

- The count read 0/30 at the 0234 unit's close about 02:53 PT
  and 8/30 live at this unit's entry about 05:38 PT: +8 over
  about 2 hours 45 minutes, about 1 per 20 minutes, consistent
  with the earlier two-endpoint estimate. Still not a measured
  rate. A 0/30 read stays a momentary state, not a day-done
  state.

## Closing reads

- Alliance Techs entered: yes. Donation Count: 1/30 remaining,
  read live and image-verified in this unit. Tech Donation
  Today: 5100 at entry, closing unread. Coin button: green at
  close, no timer shown. Donations made: 7. Coins spent: 6,300.

## Outcome

Partial. Seven of the eight remaining coin donations are done
and verified live; the last one is deliberately left for the
re-read unit via the War-tab route, per the changed-route rule.
The tracker is left untouched, so the next tick re-produces the
donations regular and the work resumes as a fresh unit. The
quota checkpoint rule R3 still applies - the remaining count
must be read live six hours and two hours before the 19:00
reset.

## Red lines

- No diamonds or money spent. No priced button tapped. No
  blind tap on a grounding point or an inherited centre (the
  first shield-centre tap that did nothing was re-grounded,
  not repeated). No other activity's rewards touched. The
  diamond Donate button was never tapped.

## Result stats

- target 8, achieved 7, resources_gained 350 Tech EXP plus 350
  badge item, costs 6300 coin plus about 14 minutes, verified
  yes, blocker_category h, donations_made 7,
  donation_count_before 8, donation_count_after 1, coin_spent
  6300, device_takeovers 0, entry_attempts 2
