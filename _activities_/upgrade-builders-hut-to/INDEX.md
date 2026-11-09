---
title: Upgrade Builders Hut to Lv.26
created: 2026-11-09T20:32:17Z
modified: 2026-11-09T20:32:17Z
level: L1
version: 1.0.0
description: Banner quest to upgrade the Builders Hut from Lv.25 to Lv.26 - cost, time and panels measured read-only, owner-only, waits on the owners decision in Issue 517
status: unverified
grounded_in:
  - source: ticker-1204 scout discovery unit 018 execution record 2026-11-09 1204 queue run (done, Builders Hut Lv.26 banner quest profiled live - cost Iron 170.0M plus Food 56.9M plus Lv.26 HQ, all met, original time 15d 08:05:18, no reward shown, no deadline, upgrade panel X unresponsive to background clicks; record commit 6f18bc3be on records/2026-11-09)
  - source: ticker-0842 scout discovery unit 009 execution record 2026-11-09 0848 queue run (done, Builders Hut Lv.26 banner quest first explored read-only - cost, time and Finish Now measured, owner-decision Issue 517 filed; record commit ec55aa585 on records/2026-11-09)
---

# Upgrade Builders Hut to Lv.26

## What this activity is

The banner quest "Upgrade Builder's Hut to Lv.26 (0/1)" at the bottom
of the base screen. It completes when the Builder's Hut reaches Lv.26
- a one-off 0 of 1 quest with no deadline and no reward shown. The
action itself is owner-only: starting a building is red-lined, so
this quest can never execute as a unit - it waits on the owner's
decision in GitHub Issue #517 (owner-decision). If approved, the
building-queues regular (PR #515, Refs #513) would own the execution.
Until then this profile is learn-only. Executions are recorded in
`_records_/<date>/upgrade-builders-hut-to/`, one file per execution.

## How it is done

- Read the quest only: tap the banner to pan to the Builder's Hut
  (Lv.25, yellow arrow above it), open the Building Details panel
  (blue paw button) and the upgrade panel (green up-arrow button),
  read every field live, and close without tapping Upgrade, Finish
  Now or Quick Dispatch.
- Close the upgrade panel with the left-edge swipe-back gesture (drag
  from x 20 to 200 at y 500), one level per drag - the panel X does
  not respond to background clicks. Re-ground the entry fresh (R2)
  rather than assuming the panel's state.

## What is known from 2026-11-09 0848 and 1204

- Entry: banner quest at the bottom left of the base screen, above
  the HEROES button. Tapping it pans the camera to the Builder's Hut
  and selects it - a big yellow arrow marks it, with two round buttons
  beside it (blue paw, green up-arrow). No quest detail panel opens:
  the banner is a go-to link, not a quest sheet.
- Mechanism: the quest completes when the Builder's Hut reaches Lv.26.
  Current level Lv.25, progress 0 of 1.
- Building function, from the Building Details panel (blue paw
  button): the hut houses the 4 assigned Builders - Rebecca, James,
  Harry, Jolene - and banks Free Construction Speed-up Time, 6hr 32min
  at the 1204 reading.
- Upgrade panel (green up-arrow button), read in full: BUILDER'S HUT
  Lv.25 to 26, Hero EXP 22.0M; Power 90,800 to 108,300; Free
  Construction Speed-up Time 00:20:00 to 00:22:00.
- Cost, all three lines green-checked (affordable now): prerequisite
  Lv.26 Headquarters (met); Iron 170.0M (owned 871.8M at 1204,
  866.8M at 0848); Food 56.9M (owned 544.5M at 1204, 542.1M at
  0848).
- Time: Original Time 15d 08:05:18. The Upgrade button reads
  7d 07:16:49 with a clock icon; the 0848 unit read it as the
  effective time after bonuses as displayed, and the 1204 unit
  records the gap against the original time as unexplained -
  speedup reductions unmeasured, not inferred. Finish Now would cost
  18,188 diamonds (read only, never tapped).
- Reward: none shown on the banner or on either panel - no reward
  line exists for this quest as displayed. Whether the banner quest
  itself pays a separate reward on completion is untested - it was
  not checked against the daily-missions list.
- Deadline: none shown; it reads as a persistent banner quest, not a
  timed one. Cycle and scoring: none - a one-off 0 of 1 quest.
- Building queue read 1/4 at the time (Lv.29 Aircraft Center in
  progress, per the 0744 unit), so a free builder slot exists, but
  the 15-day build is the longest commitment measured so far.
- Close blocker (1204): the upgrade panel's X did not respond to
  background clicks - two single taps, one double-click and one
  1-second mouse down/up at the grounded X point (820, 238), plus
  one tap on the dimmed map outside the panel, all showed no change.
  Same background-click resistant class as the zombie Store button
  (units 057 and 058). The panel was left open at the unit's close -
  game state is safe (no upgrade started, queue still 1/4). The
  left-edge swipe-back gesture, verified by the 1220 harvest unit on
  the iron and gold mine panels, is the working close for this panel
  class; the successor closes it with the swipe, not the X.
- Base screen on entry (1204): Food 544.5M, Iron 871.8M, Coin 46.2M,
  Diamonds 6,077, Total Power 149,217,331, Stamina 120, building
  queue 1/4, research 1/2.

## Open questions

- Whether the banner quest pays a separate reward on completion
  (untested - not checked against the daily-missions list).
- The Upgrade-button time gap: original 15d 08:05:18 against the
  displayed 7d 07:16:49 - which speedup reductions produce it is
  unmeasured.
- The owner's decision in Issue #517: start the Lv.26 upgrade now,
  or leave it queued.

## What the 2026-11-09 1204 scout-discovery unit added - Builders Hut Lv.26 quest measured, upgrade panel X unresponsive

- Unit scout-scout-discovery-2026-11-09-018 by ticker-1204, about
  12:04 to 12:13 local, status done. Evidence in
  `_records_/2026-11-09/upgrade-builders-hut-to/1204-queue-run.md`
  (commit 6f18bc3be on records/2026-11-09). Read-only exploration:
  tapped the banner quest, opened the Building Details panel and the
  upgrade panel, read every field live. Nothing claimed, nothing
  spent, no upgrade started.
- The 0848 exploration (unit 009, ticker-0842, record
  `_records_/2026-11-09/upgrade-builders-hut-to/0848-queue-run.md`,
  commit ec55aa585 on records/2026-11-09) was sourced in
  perception-scout but never got its own profile until this fold; its
  cost, time and Finish Now reads are folded here alongside the 1204
  read, and its follow-up (Issue #517 filed) stands.
- The provisional profile was NOT written into `_activities_/` by
  either unit (tier 2, left for the knowledge PR flow); this profile
  is that write, by the knowledge organizer.
- Result stats: target learn-builders-hut-quest-profile-fields,
  achieved 1, resources_gained none, costs about 9 minutes of unit
  time, no items spent, verified yes, blocker_category none, points
  0, surfaces_walked base-screen-banner-quest-builders-hut-detail-
  upgrade-panel, items_observed 1, red_dots_seen 0,
  red_dots_explained 0, unexplained_red_dots 0, unknown_items 0.
