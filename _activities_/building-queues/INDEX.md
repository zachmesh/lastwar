---
title: Building Queues
created: 2026-10-25T18:58:00Z
modified: 2026-11-09T17:32:17Z
level: L1
version: 1.2.0
description: Checking build queues and upgrade state, one activity folder for building knowledge
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-10-25
  - source: owner structure direction on activity folders, 2026-10-25
  - source: ticker-0736 scout-discovery execution record 2026-11-09 0744 queue run (done, building queue read live - Lv.29 Aircraft Center 2d 18:40:11 left, slots 2-4 idle, hammer entry (44,195), 2.5-day clock gap flagged; record commit 36992d92e on records/2026-11-09)
  - source: ticker-0842 scout-discovery execution record 2026-11-09 0848 queue run (done, Builders Hut Lv.26 banner quest measured read-only - Lv.25 to 26, Iron 170.0M, Food 56.9M, Original Time 15d 08:05:18, Upgrade button 7d 07:16:49, Finish Now 18,188 diamonds, owner-decision Issue #517; record commit ec55aa585 on records/2026-11-09)
---


# Building queues

## What this activity is

Checking the four build queues, recording long running upgrades and
noting idle slots. This folder accumulates building knowledge - queue
count, upgrade times and panel safety lessons. Starting an upgrade
spends resources and locks a queue for a long time, so it needs the
owner choice unless it was already queued. Executions are recorded in
`_records_/<date>/building-queues/`, one file per execution.

## How it is done

- Open the build queue list from the base screen queue icons. The hammer icon opens the panel - tap [44,195] measured 2026-11-09.
- Record each running upgrade, its level and its time left.
- Close building panels from their panel base area with care - see the
  safety lesson below.

## What is known from 2026-10-25

- Four build slots exist. Running (2026-10-25 read) - a level 29 Aircraft Center upgrade
  with 19 days 18 hours left, and a level 29 Drill Ground upgrade with
  8 days 12 hours left. Two slots were idle then.
- Correction, live read 2026-11-09 0744 (scout-discovery unit, ticker-0736): slot 1 holds the same Lv.29 Aircraft Center upgrade, now 2d 18:40:11 left and about two thirds full; slots 2, 3 and 4 are idle. The 2026-10-25 time-left figure is superseded by this newest verified read. The Drill Ground upgrade was NOT re-read in this unit, so its state is unverified - its 8d 12h window from 2026-10-25 has elapsed, so it is expected finished, but that is inference, not a live read. Open question: about 2.5 days are unaccounted between the 2026-10-25 read (19d 18h left, arithmetic expects about 4d 18h left after 15 days) and the live 2d 18:40 read - possibly speedups applied by the owner at some point, or the earlier read captured a different state. The live figure stands; the gap is flagged, not resolved.
- Builders Hut Lv.26 quest, measured 2026-11-09 0848 (scout-discovery unit, ticker-0842, read-only): the banner quest "Upgrade Builder's Hut to Lv.26 (0/1)" sits at the bottom left of the base screen, above the HEROES button; tapping it pans the camera to the Builder's Hut (Lv.25) and selects it, and the green up-arrow opens the upgrade panel. Lv.25 to Lv.26: Power 90,800 to 108,300, Free Construction Speed-up Time 00:20:00 to 00:22:00, Hero EXP 22.0M shown on the panel. Cost, all prerequisites met (green checks): Lv.26 Headquarters; Iron 866.8M/170.0M (have 866.8M, need 170.0M); Food 542.1M/56.9M (have 542.1M, need 56.9M). Original Time 15d 08:05:18; the Upgrade button shows 7d 07:16:49 (effective time after bonuses, as displayed). Finish Now would cost 18,188 diamonds. Building queue read 1/4 at the time (Lv.29 Aircraft Center in progress), so a free builder slot exists. Starting a building is owner-only (red line) - the Upgrade button was NOT tapped and Finish Now was NOT tapped. Owner-decision Issue #517 filed. Whether the banner quest itself pays a separate reward on completion is untested - it was not checked against the daily-missions list in this unit.
- Safety lesson, from the disclosure in the 2026-10-25 play record -
  closing a Gold Mine panel with a tap at its base appears to have hit
  Upgrade, and base power then rose by exactly the next level preview
  of 14,800. The green up arrow on a selected building is an upgrade
  shortcut and is never used to close a panel.
- No new build was deliberately started that day.

## Open questions

- What the idle slots should build next. That choice is with the
  owner, together with the research direction. (2026-11-09 0744 update: three slots are idle now, not two; the Drill Ground upgrade's fate is unverified, see the correction above.)
- The about 2.5-day gap in the Aircraft Center upgrade clock (2026-10-25 read 19d 18h left, arithmetic expects about 4d 18h left after 15 days, live read 2d 18:40) - possibly owner-applied speedups or a different earlier state. Flagged, not resolved. (Added 2026-11-09 0744.)
- Whether the Lv.26 Builders Hut upgrade should start now (owner-decision Issue #517): the 15d 08:05:18 original time (7d 07:16:49 effective as displayed) is the longest build commitment measured so far, and it would occupy the slot the Lv.29 Aircraft Center finishes into; if approved, the building-queues regular (PR #515, Refs #513) owns the execution. Whether the banner quest pays a separate reward on completion is untested. (Added 2026-11-09 0848.)

## What the 2026-11-09 0744 scout-discovery unit added - Aircraft Center 2d 18:40 left, three slots idle, 2.5-day clock gap flagged

- Unit scout-scout-discovery-2026-11-09-002 by ticker-0736, about 07:44 to 07:53 local, status done. Evidence in `_records_/2026-11-09/building-queue-1-of/0744-queue-run.md` (commit 36992d92e on records/2026-11-09). Read-only exploration of the building and research queue state; the research half is folded in research-queue 1.1.0.
- Entry point (measured): the hammer icon on the base screen opens the building queue panel - tap [44,195] worked at once.
- Building queue, read live 07:46 PT: slot 1 Lv.29 Aircraft Center upgrade in progress, Time Left 2d 18:40:11, progress bar about two thirds full. Speed Up button present, NOT tapped (speedups are a red line). Slots 2, 3, 4 idle, Construct button each, NOT tapped - never start buildings on own initiative, owner-only. Header text: "Commander, manage your Building Queues here. Enhance development speed by hiring more queues or accelerating building." The cost of hiring an extra queue was NOT read (it would need opening a priced hire control - learn-only, left untested).
- Correction of the standing claim: the 2026-10-25 figure of 19d 18h left for the Aircraft Center is superseded by this live read of 2d 18:40:11. The old figure stands as dated history in the section above, not deleted. The Drill Ground upgrade from the same 2026-10-25 read was NOT re-read; its state is unverified.
- Open question, not a conclusion: about 2.5 days are unaccounted - the 2026-10-25 read at 19d 18h left, 15 days later, arithmetically expects about 4d 18h left, but the live read is 2d 18:40. Possibly speedups applied by the owner at some point, or the earlier read captured a different state. The live figure stands; the gap is flagged in the open questions, not resolved.
- Base HUD at entry (07:45 PT): food 542.1M, iron 866.8M, coin 44.2M, diamonds 6,077, hero EXP 13.22K, Total Power 149,217,331, stamina 120. Banner quest: "Upgrade Builder's Hut to Lv.26 (0/1)" - owner-only, not started.
- Result stats: target learn-building-research-queue-state, achieved 1 (both panels read live), resources_gained none, costs about 13 minutes, no items spent, verified yes (same-unit live reads), blocker_category none.

## What the 2026-11-09 0848 scout-discovery unit added - Builders Hut Lv.26 quest measured read-only, owner-decision #517

- Unit scout-scout-discovery-2026-11-09-009 by ticker-0842, about 08:48 to 08:53 local, status done. Evidence in `_records_/2026-11-09/upgrade-builders-hut-to/0848-queue-run.md` (commit ec55aa585 on records/2026-11-09). Read-only exploration of the banner quest; nothing was started, no Upgrade or Finish Now tap.
- Entry point (measured): the banner quest "Upgrade Builder's Hut to Lv.26 (0/1)" sits at the bottom left of the base screen, above the HEROES button. Tapping it pans the camera to the Builder's Hut (Lv.25) and selects it - yellow arrow above the building, paw and green up-arrow buttons. Tapping the green up-arrow opens the upgrade panel; everything below was read live on that panel.
- Measured on the panel: Builder's Hut Lv.25 to Lv.26. Hero EXP 22.0M shown on the panel. Power 90,800 to 108,300. Free Construction Speed-up Time 00:20:00 to 00:22:00. Cost, all prerequisites met (green checks): Lv.26 Headquarters; Iron 866.8M/170.0M (have 866.8M, need 170.0M); Food 542.1M/56.9M (have 542.1M, need 56.9M). Original Time 15d 08:05:18. The Upgrade button shows 7d 07:16:49 (effective time after bonuses, as displayed). Finish Now would cost 18,188 diamonds.
- No deadline or countdown was seen on the quest banner or the panel. Whether the banner quest itself pays a separate reward on completion is untested - it was not checked against the daily-missions list in this unit.
- Building queue read 1/4 at the time (Lv.29 Aircraft Center in progress, per the 0744 unit), so a free builder slot exists, but the 15-day build is the longest commitment measured so far. Starting a building is a red line (never start buildings on own initiative), so the Upgrade button was NOT tapped and Finish Now was NOT tapped.
- Owner decision: Issue #517 filed (owner-decision) - start the Lv.26 Builders Hut upgrade now, or leave it queued? If approved, the building-queues regular (PR #515, Refs #513) would own the execution. Candidate stays learn-only until the owner decides.
- Result stats: target explain-builders-hut-lv26-quest-mechanism-cost-time-rewards, achieved 1, resources_gained none, costs about 5 minutes, no items spent, no diamonds spent, verified yes (same-unit live reads), blocker_category none.
