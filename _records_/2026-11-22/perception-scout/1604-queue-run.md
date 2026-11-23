---
title: Scout queue run 1604
created: 2026-11-23T00:23:49Z
modified: 2026-11-23T00:23:49Z
level: L0
version: 1.0.0
description: Scout unit scout-scout-2026-11-21-001, ticker-1604, chain head of scout-2026-11-21 - base re-read done, two right-rail timer icons unresolved (HUD taps landed on the map), Events hub not opened, successor seq 2 enqueued
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-22 about 16:13-16:25 PT
  - source: unit scout-scout-2026-11-21-001 in _queue_/claimed
  - source: _activities_/perception-scout/INDEX.md and the day observation file _records_/2026-11-21/perception-scout/observation.md v1.17.0
---

# Scout queue run 1604 (ticker-1604)

Unit scout-scout-2026-11-21-001, regular scout, chain
scout-2026-11-21 seq 1 (chain head, staged by planner 1540).
Executor ticker-1604. Computer session cc-170, window
127196 (window mode, never brought to front). Session
window about 16:13 to 16:23 PT; the session closed with
the token expiry (16:25) approaching and the pass budget
ending, before the unit cap arrived.
Observe-only throughout.

## Outcome

Partial - the base re-read is done and appended to the day
observation file (v1.17.0, 532 items), but the chain head's
surface groups are not finished: the two right-rail timer
icons are still unidentified, the Events hub was not opened
(no zombie-tab enumeration, no 3v3 / Champion Duel look),
and the passes entry was not located. The successor unit
(scout-2026-11-21 seq 2) is enqueued for the remainder.
Tracker untouched.

## What was read live

- Base re-reads (entry about 16:17, close about 16:25):
  power 147,972,269 (unchanged from seq 19); food 765.4M
  (up from 760.6M); iron 1.1G; coins 109.2M; diamonds
  6,456 (up from 6,436, plus 20, cause not established -
  no claim was made by this unit); Gold Bricks 17.72K;
  lightning counter 120; hammer 1/4 (red dot), flask 2/2;
  Events badge 1; Build: Oil Well [0/1]; two survivor
  "?" icons at the front door; radar dish badge 11;
  trucks red dot; WORLD badge 99+; chat ticker
  "Breaking News: Intense battle...",
  "ArchManningIsBunz:", "scrap yard: ty Tex".
- Right-rail timers: the two icons (helmet-like upper,
  meteor-like lower) BOTH read 01:47:39 at about 16:17
  and 01:46:29 at about 16:19 - identical to each other,
  decreasing about 1 per minute of wall time.
- Base clock building: digital display read 22:14 at
  about 16:23 (server time, counting up slowly).
- NEW tag on the glowing orange-topped building at the
  top-right of the base (about (540,225) in the about
  16:19 view), identity open.
- Drone Center Lv.1 selected by the second tap; radial
  menu shows a plane icon and an info icon, neither
  tapped.

## What failed (R2)

Two taps at HUD-rail points landed on the map instead of
their icons: the tap at the upper timer icon's measured
point (595,175) panned the map slightly, and the tap at
the Events point (595,140) selected the Drone Center.
The background-input point mapping for the right rail
needs re-grounding by the successor - fresh screenshot,
re-measure the rail icons before tapping, do not re-tap
the same points blindly. This is the first consecutive
partial of this regular with this blocker, so the method
change (re-grounding) is the required pivot; the blocker
is recorded here and in the observation file.

## Not done this unit

- Events hub not opened: zombie tab not enumerated, so
  the zombie chain stays unseeded; 3v3 Brawl / Champion
  Duel (Issue #805) not explored.
- Passes entry not located.
- Portrait corner mark (News Center portrait) not
  re-checked.
- Timer icon identities open (see R2 above).

## Result stats

- target: walk the chain head's surface groups (base re-read, timer icon identification, Events hub tab enumeration, passes entry, 3v3 / Champion Duel look) and append the reads to the day observation file with zero unexplained red dots
- achieved: base re-read done and appended (18 items, 532 total); timer icons, Events hub, passes entry, 3v3 / Champion Duel not done
- resources_gained: none
- points: 0
- costs: about 12 minutes device time, no spend, no items
- verified: yes (base counters, both timers, clock display and the NEW tag read live in this unit)
- blocker_category: c (tap method - HUD-rail taps landed on the map)
- surfaces_walked: base, Drone Center selection
- items_observed: 18
- red_dots_seen: 10
- red_dots_explained: 10
- unexplained_red_dots: 0
- unknown_items: 4 still open (two timer icon identities, passes entry, 3v3 / Champion Duel, portrait corner mark) plus 1 new (NEW tag on the glowing orange-topped building)
- follow_up: successor seq 2 of chain scout-2026-11-21 enqueued for the remainder (Events hub enumeration, passes entry, 3v3 / Champion Duel, portrait corner mark, NEW-tag building identity)
- evidence: _records_/2026-11-21/perception-scout/observation.md (v1.17.0)

## Delivery note - two observation files

- This unit appended to the live tree's day observation
  file, `_records_/2026-11-21/perception-scout/observation.md`
  (v1.16.0 to v1.17.0), the file the 1540 planner read as
  current. The branch copy of that file sits at v1.15.0
  (seq 19, ticker-1021, not yet landed), so this delivery
  carries v1.15.0 to v1.17.0 in one commit - seq 19's
  sections land with mine, verified by diff (branch blob
  against the live pre-append file: only the frontmatter
  version and the seq-19 sections differ).
- A second observation file exists: ticker-1543 created
  `_records_/2026-11-22/perception-scout/observation.md`
  ("reset day 2026-11-22", 20 items, 1 unexplained red
  dot) in commit e69c91c40, which sits on VPS branch
  ticker-1543-records-1122 and is NOT on
  records/2026-11-22 and NOT in the live tree. This unit
  could not append there - the file is not in the working
  pool. The two files cover the same reset day under two
  names; reconciling them (and the observation-file
  naming rule) belongs to the integrator / retro, not to
  this pass.

## Red lines

No diamonds or money spent. No claim, fight, dispatch,
donation or purchase. No panel was left open by this unit
except the Drone Center radial menu, which was closed by
the final map tap (base view confirmed on the close
read).
