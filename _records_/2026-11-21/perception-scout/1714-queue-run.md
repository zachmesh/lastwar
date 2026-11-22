---
title: Perception scout queue run 1714
created: 2026-11-22T01:14:00Z
modified: 2026-11-22T01:14:00Z
version: 1.0.0
description: Queue unit scout-scout-2026-11-20-002, ticker-1704 - post-reset scout chain seq 3, Arms Race tab read live, base NEW megaphone resolved (alliance announcement), chat and mail categories walked, store/alliance/VIP/passes/daily-missions/world-map still unwalked
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-21 17:05-17:14 PT
  - source: unit scout-scout-2026-11-20-002 in _queue_/done
---

# Perception scout queue run 1714 (ticker-1704)

Unit scout-scout-2026-11-20-002, regular scout, activity
perception-scout, priority 2, est 8 minutes, expires
2026-11-22T02:00:00Z (18:00 PT reset). Executor ticker-1704.
Session window about 17:05 to 17:14 PT. Token held 17:04
to 17:20 PT; unit claimed 17:05 PT, lease to 17:25 PT.
Chain scout-2026-11-20, seq 3.

## Outcome

Partial - the Arms Race tab was read live, the base "NEW"
megaphone was resolved (it opens Chat with the alliance
announcement), and the chat and mail-category surfaces were
walked, but the store, alliance panel and station, VIP,
passes, daily missions, world map and duel/radar surfaces
were not walked inside this unit. No claim, fight, dispatch,
donation or purchase was made - scout observes only. No
diamonds or money spent. The tracker is untouched (partial
re-produces next tick); the successor chain unit continues
the same pass.

## Device state

- Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd)
  online. Computer session cc-25.
- LastWar window 105986 (pid 5136, 763x1050) raised to the
  front with activate raise=true on the first attempt - the
  Issue #648 window precondition stays cleared (ticker-1434
  cleared it at 14:34 PT; ticker-1504 played 15:15-15:30 PT).
- No different-device dialog, no login demanded, no Touch
  ID, no password typed. The game canvas exposes no
  Accessibility controls; all reads are screenshots plus OCR.

## Observed items

### Base screen (re-read live about 17:07 PT)

- HUD unchanged from the 16:08 read: power 149,653,371;
  food 730.5M, iron 1.1G, coin 88.2M, diamonds 5,236,
  gold bars 17.72K.
- Red dots: Events 1, VS countdown 00:51:20 (duel day in
  progress; owning regular duel-score, unit in inbox),
  event countdown 1d 00:51:19, Alliance, Mail, Inventory,
  HEROES, WORLD 99+, construction hammer 1/4, trucks
  badge 3, hero badge 1. Research flask 2/2, no dot.
- "Build: Oil Well (0/1)" banner at the bottom.

### Arms Race tab (opened live about 17:11 PT)

- Phase: "Base Building", Contest Segment Lv.29-30,
  countdown 00:49:57 remaining. Calendar button top right.
- Tier chests: labels 2,360 / 4,800 / 11,800 above the
  thresholds 6,250 / 12,500 / 30,000. Star points 0;
  chest counter 0/2 top left.
- Scoring paths: Increase Building Power by 1pt, +1 star;
  Use 1-min Construction Speed-up, +10 stars; Buy Packs
  containing Diamonds (1 Diamond), +30 stars - the diamond
  path is a red-line spend and is never taken.
- Own row: #2110 [AP3x]Bears Lair, rank 11, score 400.
  Row above: #2112 [FLow]LuLLu, rank 10.
- The arms-race unit owns acting on this phase; scout
  records only.

### Base "NEW" megaphone - RESOLVED

- The megaphone icon (gold circle, "NEW" banner, bottom
  centre-right of the base screen, grounded at 684,857)
  opens the Chat screen on the Alliance tab with the
  Alliance Announcement popup. First tap at 511,886
  missed (landed on the glass dome building, no change);
  re-grounded by visual grounding and tapped at the
  corrected point.
- Alliance Announcement, 2026-11-21 16:09:35, from
  MesutCLK Apex: "Hey AP3X! Please send over your THP and
  Main Team screenshots for our weekly check-in. Would be
  awesome if you could get them in before reset...."
  Comment(1), 1 like. This is a request to the owner -
  THP and Main Team screenshots before the 19:00 reset.
- Banner below the popup: "Leader calls for enabling
  notifications for crucial Alliance news." with an Open
  button - NOT tapped (enabling notifications is an owner
  action, beyond observation). Popup closed with its X.
- Chat screen: tabs World / Alliance (active) / Moments /
  Private (red badge 3). Sub-tabs Chat / Alliance
  Announcement (red dot - the unread announcement above).
  Top bar carries a "NEW!" badge on an icon at top right
  next to the gear - identity unread, UNKNOWN item carried
  forward. The Alliance chat feed is active; no private
  chat text is recorded.

### Mail categories (opened live about 17:12 PT)

- Battle Report (red dot), Alliance (gift icon -
  claimable rewards inside), Event (gift icon - claimable
  rewards inside), System (avatar thumbnail on the row),
  Regular (red dot), In-app Purchases (red dot), Favorite.
- Footer: "Mails older than 30 days will be
  automatically deleted."
- The red dots and gift icons route to the mail unit in
  inbox (mail-2026-11-21-1830); scout claims nothing.

## Result stats

- target: finish the Arms Race tab, resolve the base NEW
  megaphone, and continue the post-reset pass across
  store, alliance, mail, VIP, passes, daily missions,
  world map
- achieved: Arms Race tab walked, megaphone resolved
  (alliance announcement), chat and mail categories
  walked; 27 items observed
- resources_gained: none (scout observes only)
- costs: about 9 minutes device time, no stamina or items
- verified: yes (all items read live from screenshots)
- blocker_category: h (by-design partial - unit cap
  reached mid-traversal)
- surfaces_walked: events-arms-race, base-megaphone,
  chat, mail-categories
- items_observed: 27
- red_dots_seen: 8
- red_dots_explained: 8
- unexplained_red_dots: 0
- unknown_items: 1

## Open for the successor (chain scout-2026-11-20, seq 4)

- Walk the remaining surfaces: store by section, alliance
  panel and station, VIP, passes, daily missions, world
  map, duel and radar.
- Identify the Chat top-bar "NEW!" icon at top right
  (next to the gear) - unknown item from this unit.
- The leader's announcement asks the owner for THP and
  Main Team screenshots before the 19:00 reset - an
  owner-facing request, named in the pass report.
- Note: the 00:00:51 countdown unknown item from the
  chain head is still open (no countdown of that shape
  was seen this unit).

## Delivery

- Commit to records/2026-11-21 via a temporary worktree;
  push via the VPS route; PR #762 already open for the
  branch, no new PR owed.
