---
title: 99 badge at chat exploration 0718 queue run
created: 2026-11-09T15:18:23Z
modified: 2026-11-09T15:29:00Z
version: 1.0.0
description: Scout discovery exploration - learn what the 99+ badge at the chat icon is, read-only
status: done
grounded_in:
  - source: live game screens on the owner Mac mini, 2026-11-09 07:18-07:29 PT
  - source: scout observation of 2026-11-09, surface base/hud
---

# 99 badge at chat - 0718 queue run

Unit scout-scout-discovery-2026-11-09-001, executor ticker-0704,
chain scout-discovery-2026-11-09. Read-only exploration of the
candidate filed by the scout diff (99+ badge at chat icon,
base/hud, first classified after the 06:05 scout pass closed).

## Learning checklist (measured live in this unit)

- Entry point (measured): base screen left edge, speech-bubble
  chat icon (red badge 3 at entry); the bottom chat ticker also
  carries the count. Tapping the ticker text itself does nothing;
  the chat icon opens the Chat panel. Tapping a player avatar
  inside the chat list opens that player's profile - read-only,
  closed untouched (no player details recorded here).
- Mechanism (measured): the 99+ badge sits on the Alliance tab
  of the Chat panel and counts unread Alliance channel messages.
  Opening the Alliance tab clears it - verified live: badge
  present on entry to Chat, gone after the Alliance tab opened.
  World sub-tabs carry their own small red dots (Season, English,
  Duel); the World list showed a "470 new message(s)" banner.
  Private tab carries a red badge 2 (not opened in this unit).
- Rewards (measured): none - reading chat pays nothing.
- Cost (measured): none - no diamonds, no items, no stamina.
- Cycle and deadline shape (measured): none - the count grows
  with unread messages and clears on read; no expiry.
- Scores anywhere (measured): no.

## Verdict

Candidate REJECTED as a task - the 99+ badge is an informational
unread-message counter for Alliance chat, not a playable task:
no reward, no cost, no deadline, no scoring. No execution unit
should be produced from it; the owner reads alliance chat
himself when he wants to. The provisional profile filing stays
in `_records_/2026-11-09/perception-scout/scout-diff-output/scout-candidates-2026-11-09.md`;
filing the rejected profile under `_activities_` is tier-2 work
left for the knowledge flow, not swept into this pass.

## Side observation (game state, not chat content)

- Opening the Alliance tab showed an Alliance Announcement:
  season skills reset - the season has ended, all season skills
  are now inactive, spent points fully refunded. Noted here as
  a state fact; no action taken.
- A leader banner asks members to enable notifications for
  crucial Alliance news (Open / X). Not tapped - a settings
  change is the owner's decision, not this unit's.

## Stats

- target: explain the 99+ badge mechanism from live reads
- achieved: 1 mechanism explained and verified (badge clears on opening Alliance tab)
- resources_gained: none
- costs: 11 minutes, no items spent
- verified: yes (same-unit live reads)
- blocker_category: none
