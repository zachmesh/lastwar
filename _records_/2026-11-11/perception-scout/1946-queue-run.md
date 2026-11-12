---
title: Perception scout queue run 1946
created: 2026-11-12T03:46:00Z
modified: 2026-11-12T03:46:00Z
version: 1.0.0
description: Queue unit scout-scout-2026-11-10-002, events group of pass scout-2026-11-10 - all six Events tabs, Alliance Duel page, radar, observe-only
status: verified
grounded_in:
  - source: live game screens on Zhen's Mac mini, sessions cc-660 and cc-661, 2026-11-11 19:33-19:46 PT
---

# Perception scout — queue run 1946 (unit 002, chain scout-2026-11-10)

- Unit: `scout-scout-2026-11-10-002`, chain `scout-2026-11-10` seq 2
- Executor: ticker-1919; token re-acquired 19:33 PT, claimed about 19:33 PT; finished about 19:46 PT
- Sessions: cc-660, cc-661; Last War window 676414 (windowed 642x951, not fullscreen); no drop, no "active on a different device" dialog, no access error
- Status: partial — events-group remainder fully walked, but 2 red dots unexplained (a closing condition, not a report nicety); successor enqueued for the store group. Continuation of ticker-1843 unit 001, which walked the hub strip, Arms Race and Age of Oil and left VS, Wanted Boss, Desert Battlefield and radar unwalked; this unit walked that remainder plus re-reads of Zombie Invasion, The Age of Oil and Community.

## What was walked

- Events hub, all six tabs: The Age of Oil, Arms Race (carried read 19:23 local from the zombie unit in this same pass), Desert Storm Battlefield, Zombie Invasion - Glacieradon (re-read), Wanted Boss, Community.
- Alliance Duel page (Duel Progress, Today's Duel).
- Radar screen (dish icon, third icon in the map's left column).
- Observe-only throughout: nothing claimed, fought, dispatched, donated, dug or bought; no map pin tapped on the radar screen; no Community link tapped; Quick Execute not tapped.

## Observations (detail in the day observation file)

- Zombie Invasion: timer 1d 22:25:35, next wave in 00:20:14, 40/40 bar, Alliance Finding Lv.80/Lv.85 bosses at 138-294km.
- Desert Storm Battlefield: alliance matchmaking in progress, 04:25:15, [AP3x] The Apex, 20 sign-ups, 0-0.
- Wanted Boss Code 87: appears at server time 00:00, Go timer 21:24:57, tank heroes +50% damage, rewards crates x6/x6/x6, 5m speedup x5, diamond x10.
- The Age of Oil: Tech Research 9511/500, Building Upgrades 22379/500, both far past target, 3d 22:21:10 left.
- Community: 500-diamond Discord-link reward already Claimed; 200-diamond visit bonus offered for joining a community.
- Alliance Duel: Train Heroes theme, 22:23:30 left, [AP3x] The Apex 374,461,602 (46%) vs [TFox] Fox 433,586,724 (54%); top scorer [TFox] Mihye 26,797,330.
- Radar: Lv.13, 427 points, 100%, 1/40 (meaning unverified), 12 tasks restore in 03:59:00, 5 tasks need 50 stamina.

## Red dots

- Seen 7, explained 5, unexplained 2: the Zombie Invasion Store button dot and the Desert Battlefield tab badge (!).
- The unidentified centre-tab red dot from the first hub opening is resolved: it was the Wanted Boss tab's dot.
- VS icon carried no red dot at the 19:44 map read.
- Day counters updated in the observation file: items 21 to 29, red dots seen 25 to 32, explained 18 to 23, unexplained 7 to 9 (base was ticker-1634 unit 001 plus ticker-1843 unit 001's walk; this unit adds 8 items, 7 red dots seen, 5 explained, 2 unexplained).

## Notes

- The Events tab bar scrolls horizontally and shifts position between openings — re-ground every tab per opening, never reuse a position. The bar's left end holds The Age of Oil / Arms Race; the right end holds Wanted Boss / Community.
- The first hub tab's icon (present/gift) is The Age of Oil page; its badge 1 marks progress-track step 1.
- The scout_diff.py run is left for the successor unit — this unit's follow-up is the store-group successor, not a diff application.

## Result stats

- surfaces_walked: 3 (events-hub, duel-page, radar)
- items_observed: 8
- red_dots_seen: 7
- red_dots_explained: 5
- unexplained_red_dots: 2
- unknown_items: 4
- target: walk the events surface group of pass scout-2026-11-10, observe-only
- achieved: all six Events tabs, Alliance Duel page and radar screen observed and recorded; 2 red dots unexplained
- resources_gained: none (observe-only)
- costs: about 13 minutes, no stamina or resources spent
- verified: yes
- blocker_category: h
