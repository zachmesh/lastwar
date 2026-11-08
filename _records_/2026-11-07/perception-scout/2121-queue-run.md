---
title: Queue Run 2121 Perception Scout Alliance Remainder
created: 2026-11-08T05:21:00Z
modified: 2026-11-08T05:21:00Z
level: L0
version: 1.0.0
description: Scout chain scout-2026-11-02 unit 005, alliance remainder, partial with successor enqueued
status: unverified
grounded_in:
  - source: in-game screens observed on the owner Mac mini, 2026-11-07
---

# 2121 queue run - perception scout, alliance remainder (partial)

Unit scout-scout-2026-11-02-005, executor ticker-2104, session
cc-50 about 21:07 to 21:21 America/Los_Angeles. Status partial:
the alliance remainder was walked observe-only as far as the
unit cap allowed; Alliance Star, Settings, the Record
Member/Message/Event tabs, the station panel and the loot box
pin are unwalked and carried to the successor unit, so the
tracker is left untouched.

## What was walked, observe-only

- Base screen and HUD, read live about 21:07 local: power
  149,850,353; resources 478.8M, 802.1M, 6.9M, 25.0M,
  922.2K; diamonds 13.22K; cart 4,217; stamina 120. Events
  badge 1, Season II badge 1, Alliance dot, skull timer
  00:00:20 with badge 2, Inventory dot, 99+ badge. Furnace
  toast again: "h-temp Furnace total overdrive time (in
  sec) [22/60]", still unexplained. Resource bubbles
  observed only, not collected.
- Alliance panel: [AP3x] The Apex, 5.0 stars, Leader Abyss
  Apex, Power 13,355,288,388 at entry rising to
  13,360,041,845 during the unit, Members 96/100, Language
  English. Dots on Alliance Wars, Help, Alliance Gifts only.
  Lower panel scrolled: Assemble, Strength Ranking,
  Alliance Events, Alliance City (gold), Season
  Contributions (gold), Season Milestones (gold), one more
  gold row below the fold, unread. Alliance Star (Event 40)
  banner, Time Left 20:41:09 falling to 20:36:40.
- Members: 18 online; R5 Abyss Apex; Warlord
  ItStartsWithaDream, Recruiter KAGE, Muse StarFall,
  Butler KillerInstinct14; R4 "The elected" 2/10; R3
  "Armed Guards" 10/59 with four Lv.30 members read
  (Captain Landmine 131.3M, Dw1968 110.2M, Commander Supa
  93.5M, Raze Cromwell 145.4M, all Online). Manage buttons
  not tapped.
- Strength Ranking, all three tabs: Power top 6 and own
  #34 Bears Lair 147,744,234 (HUD read 149,850,353 minutes
  earlier; discrepancy noted, unverified); Kills top 6 and
  own #94 Bears Lair 48,638; Donation Daily top 5 and own
  #46 Bears Lair 1150. Donate and Rewards buttons observed
  only, not tapped. Weekly subtab not opened.
- Alliance Events: single tab seen, Zombie Siege, mode
  Alliance Exercise (30-minute Battle Stage, top-damage
  Commander may multiply all members' rewards by 10x,
  Offline Participation auto-joins rallies when offline).
  Preparing 41:48:23; Your Time Zone 2026-11-9 15:00:00;
  Offline Participation already checked. Rewards, Build
  and View not tapped. This is a NEW label for the roster.
- Record (Alliance Logs), War tab: six identical entries of
  one member attacking Jujuliano1's base #2110, victory,
  server times 02:36:01 to 02:36:20; next entry another
  member attacking Valerunomu's base #2110. Member,
  Message and Event tabs not opened.
- Applicants: two taps produced no page change; the second
  surfaced the toast "Permission needed to execute this
  action." R3 Bears Lair cannot open Applicants
  (officer-only surface). Resolved by permission, not
  unwalked.
- Nothing claimed, fought, dispatched, donated, joined or
  bought anywhere in this unit.
- Observation appended to
  `_records_/2026-11-02/perception-scout/observation.md`
  (pass day file, ticker-2104 section).

## Red dot accounting

- Seen 8 signals: Alliance Wars, Help, Alliance Gifts dots;
  base Events 1, Season II 1, skull-timer 2, Inventory dot,
  99+ badge.
- Explained 3: the three panel dots map to their owning
  regulars.
- Unexplained 5: the five base badges, carried to their
  owning groups.
- Unknown items 5: furnace overdrive toast [22/60]; the
  gold-row label below Season Milestones; the "Important:
  President..." scrolling banner; a Tactical Master Supply
  Box toast seen mid-unit; the HUD-vs-ranking power
  discrepancy.
- unmatched_labels: Zombie Siege, Alliance Exercise,
  Offline Participation, Alliance City, Season
  Contributions, Season Milestones.

## Outcome

- Status: partial (alliance remainder, unit cap). Successor
  unit enqueued under chain scout-2026-11-02 for Alliance
  Star, Settings, Record Member/Message/Event tabs, the
  station panel and the loot box pin.
- Issue filed: #419 (idea, knowledge) - new alliance event
  Zombie Siege / Alliance Exercise, explore before
  2026-11-09 15:00; Offline Participation already enabled.
- Tracker: untouched (partial rule).
- No zombie chain seeded: no Zombie Invasion tab was seen
  anywhere in the alliance panel or the base screen; the
  event ended 2026-10-30 and the chain stays closed until
  its tab is seen live again.
- Red lines: nothing spent, no paid button tapped, no
  donation, no rally join, no toggle changed.

## Correction (same pass, from unit timestamps)

- The session window above is corrected: the unit file
  records started_at 2026-11-08T05:07:06Z and finished_at
  2026-11-08T05:16:08Z, i.e. 21:07:06 to 21:16:08 local,
  duration 542 seconds. The 21:21 end in the header is the
  device-token lease expiry, not the execution end. The
  file name 2121 reflects the estimate at writing time;
  the unit timestamps govern.
- Tier-2 change left untouched: the working tree holds a
  modified `_activities_/alliance-donations/INDEX.md`
  (uncommitted, another job's in-flight state). It was not
  staged, not edited, and not included in this pass's
  commit, per the tier-1 pathspec discipline.
- Branch already carries this unit: the records branch
  holds `_queue_/done/scout-scout-2026-11-02-005.md` as
  failed by ticker-1834 (2026-11-06 02:43Z, Mac offline,
  Issue 284). The branch file is kept; this partial is
  the re-attempt evidence, per the ticker-0127 precedent
  for the same situation. The successor 006 chains from
  005 regardless.
- Observation file divergence (known gap, Issue 415):
  the branch observation file lacks five disk sections
  (ticker-0404, ticker-0504 x2, ticker-0904, ticker-1304)
  and the disk file lacks the branch's 1801 section
  (ticker-1755); the five disk sections' run records
  (0410, 0508, 0510, 0910, 1314) are likewise unpushed.
  This pass appends only its own section to the branch
  file; the union is left for the retro/integrator under
  Issue 415.
