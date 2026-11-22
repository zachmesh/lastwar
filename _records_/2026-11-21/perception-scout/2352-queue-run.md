---
title: Perception scout queue run 2352
created: 2026-11-22T07:52:00Z
modified: 2026-11-22T07:52:00Z
version: 1.0.0
description: Queue unit scout-scout-2026-11-20-009, ticker-2334 - post-reset scout chain seq 9, Chat entry found, News Center NEW! does not clear after one card, WORLD badge confirmed as unread chat
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-21 about 23:50-23:52 PT
  - source: unit scout-scout-2026-11-20-009 in _queue_/claimed
---

# Perception scout queue run 2352 (ticker-2334)

Unit scout-scout-2026-11-20-009, regular scout, chain
scout-2026-11-20 seq 9. Executor ticker-2334. Computer
session cc-67. Session window about 23:50 to 23:52 PT.
Token held from seq 8 (lease to 23:53:36 PT; the
re-acquire at 23:50 returned the same lease, no
extension). Observe-only throughout - no claim, fight,
dispatch, donation or purchase. No "active on a
different device" dialog.

## Outcome

Partial - the Chat entry is FOUND (correction to seq 8),
the News Center NEW! check is DONE (reading one card
does NOT clear it), and the WORLD badge is CONFIRMED as
an unread-chat count (8 to 3 after opening Chat). Still
open: passes entry, the red target countdown, the green
19h timer, the March Queues gift badge 2, and read-only
exploration of 3v3 Brawl / Champion Duel (Issue #805).
Successor seq 10 enqueued with the remaining window.

## Chat entry - FOUND (correction to seq 8)

- On re-entering the game for this unit, the Chat
  screen was already open. The only candidate cause is
  seq 8's chat-ticker tap: the tap OPENS Chat, with a
  slow transition - seq 8's "ticker tap only scrolled"
  reading caught the screen mid-transition (base
  elements still visible, ticker lines shifted). The
  Chat entry is the chat ticker at the bottom of the
  base screen; allow time for the slow open and do not
  re-tap on the mid-transition view.

## Chat screen read live (about 23:50)

- Tabs: World (red dot), Alliance (selected, red dot),
  Moments (red dot), Private (red badge 3). Sub-tabs:
  Chat (selected), Alliance Announcement (red dot).
- Announcement popup still open: "AP3X | TANK SQUAD
  GEAR GUIDE", "Updated Tank Squad Dotting & Mythic
  Progression Guide!", "- Upgrade in pairs of 2 or 4
  dots....", "View All", "2026-11-21 21:14:06 StarFall",
  Comment, heart 2. Leader banner "Leader calls for
  enabling notifications for crucial Alliance news."
  with an Open button (NOT tapped).
- Messages: Jerry Apex (VIP 13, R4, Lv.30) "Reply
  GoldenSonya: Went to WC with ape... Checks out" and
  "Never heard of winco". Earlier lines from seq 7
  ("I had Winco pizza and Costco pizza today and Winco
  won", "pizza hut is better but Winco is good too")
  had scrolled up.
- The notepad icon (top right, about 858,52) still
  carries the red NEW! badge at entry to Chat.

## News Center - one card read, NEW! does NOT clear

- Notepad tap opened the NEWS CENTER. Tabs: News
  (NEW!), World, Alliance. Sub-tabs: System News
  (selected), Guides (NEW!). Top ticker: "Important:
  President HawksMav appoi...".
- Four cards, unchanged from seq 7 except likes:
  "1604 ROMO: Across borders, we are one family."
  [15596, was 15580]; "#2162 | Glitch: We Can Never
  Have Enough Speedups" [21905, was 21898]; "1.1
  million registrations achieved - claim 8,000 Gold
  B..." (claim-adjacent, NOT tapped); "#1574 | From
  the Battlefield to the Dance Floor: A Player-Run...".
- The ROMO card was tapped and its article READ:
  "1604 ROMO: Across borders, we are one family.",
  2026-11-16 10:28:20, story by Blue Doll - Server
  1604 / ROMO, 117475 views, 15596 likes, 278 shares,
  271 comments. A Cookiebot consent popup covered the
  middle ("This website uses cookies", Deny /
  Customize / Allow all) - NOT tapped, no consent
  choice made.
- After returning to the News Center list, the NEW!
  badges are STILL present on the News tab and the
  Guides sub-tab, and the Chat notepad icon STILL
  carries NEW! on return to Chat. Reading ONE card
  does NOT clear the News Center NEW! - clearing
  presumably needs every NEW! item read (News and
  Guides). The registrations card was not tapped, so
  whether reading it clears the badge is untested.

## WORLD badge - CONFIRMED as unread chat

- Base close re-read: WORLD badge 3, down from 8 at
  seq 8 close. Opening Chat in this unit read the
  unread messages and the count fell - the badge is
  an unread-chat count, confirmed. The residual 3
  matches the Private tab's red badge 3 (unread
  private messages); World / Alliance / Moments carry
  red dots only.

## Base close re-read (about 23:51)

- Power 149,417,850, unchanged. Food 762.6M, iron
  1.1G, coins 103.9M, diamonds 6,426, all unchanged.
- Lightning counter 114 (was 113 at seq 8 close,
  112 at seq 8 entry) - regen about 1 per 4 to 9
  minutes across the two units. Hammer 1/4 (red dot),
  flask 2/2.
- VS countdown 18:08:20 (was 18:13:5x at seq 8 close,
  18:19:36 at seq 8 entry) - still dropping faster
  than wall time, irregular ticking unexplained.
- Events badge 1, VS red dot. Build: Oil Well (0/1).
  The Event Reminder NEW! tag is still present on the
  base (the 3v3 / Champion Duel reminders are unread).
- NOT seen this unit: passes entry, red target
  countdown, green 19h timer, March Queues gift
  badge 2 (not re-checked).

## Result statistics

- surfaces_walked: 3 (Chat, News Center, base re-read)
- items_observed: 18 (day total 336)
- red_dots_seen: 12, red_dots_explained: 12,
  unexplained_red_dots: 0
- unknown_items: 3 still open (passes entry; red
  target countdown and green 19h timer not re-read;
  March Queues gift badge 2); 2 resolved this unit
  (Chat entry = chat ticker, slow open; WORLD badge =
  unread-chat count, confirmed); 1 answered (News
  Center NEW! does NOT clear after one card)
- target: find the Chat entry and verify News Center
  NEW! clearing; find the passes entry; re-read red
  target countdown and green 19h timer; confirm WORLD
  badge drops when Chat is opened; check March Queues
  gift badge 2; explore 3v3 / Champion Duel read-only
- achieved: Chat entry found; NEW! check done (does
  not clear); WORLD badge 8 to 3, confirmed; passes,
  red target, green timer, gift badge 2 unwalked
- resources_gained: none (observe-only)
- costs: about 3 minutes device time, no stamina or items
- verified: yes (all figures read live in this unit)
- blocker_category: h (by-design partial - chain continuation)

## Notes for the successor (seq 10)

- Passes entry still unidentified. Untested candidate:
  the Events hub tabs. The gold cup stays excluded per
  the seq 8 window.
- The News Center NEW! needs every NEW! item read to
  clear (one card was not enough); the claim-adjacent
  registrations card is still untapped - do NOT tap it
  for the badge check alone, note it as the open item.
- Re-read the red target countdown and the green 19h
  timer; check the March Queues gift badge 2 (open the
  gift icon on the world map and read the LOOT rows,
  do NOT tap Claim All); explore 3v3 Brawl and
  Champion Duel read-only per Issue #805.
- Token lease (15 minutes) does not extend on
  re-acquire; plan the unit inside one lease.
