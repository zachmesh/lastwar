---
title: Perception scout queue run 1613
created: 2026-11-22T00:16:00Z
modified: 2026-11-22T00:16:00Z
version: 1.0.0
description: Queue unit scout-scout-2026-11-20-001, ticker-1604 - post-reset scout chain seq 2, Events hub finished live (Black Market, Desert Battlefield, Wanted Boss, Community), two new candidate task types found, Arms Race tab and the base/store/alliance/mail/VIP/passes/daily-missions/world-map surfaces still unwalked
status: unverified
grounded_in:
  - source: live game screen on the Mac mini, 2026-11-21 16:13-16:16 PT
  - source: unit scout-scout-2026-11-20-001 in _queue_/done
---

# Perception scout queue run 1613 (ticker-1604)

Unit scout-scout-2026-11-20-001, regular scout, activity
perception-scout, priority 2, est 8 minutes, expires
2026-11-22T02:00:00Z (18:00 PT reset). Executor ticker-1604.
Session window about 16:13 to 16:16 PT. Token held 16:07
to 16:22 PT (acquired by the chain head unit); unit claimed
16:13 PT, lease to 16:32 PT. Chain scout-2026-11-20, seq 2.

## Outcome

Partial - all seven Events hub tabs are now walked, two new
candidate task types were found (Black Market, Wanted Boss),
and the Community tab's identity is resolved, but the Arms
Race tab and the base/store/alliance/mail/VIP/passes/daily
missions/world-map surfaces were not walked inside this
unit. No claim, fight, dispatch, donation or purchase was
made - scout observes only. No diamonds or money spent. The
tracker is untouched (partial re-produces next tick); the
successor chain unit continues the same pass.

## Observed items

### Events hub (continued from the chain head)

- "Black Market" tab - resolved, NEW candidate task type
  (no regular owns it). 22d 01:46:36 remaining; Black
  Market Cash balance 7190. Top row all Sold Out,
  Availability 0: Free item (gear chest x1), Featured item
  (chest x1), Fantastic item (5m speed-up x12). Bottom row,
  500 cash each, Availability 1: orange chest "IV" x5,
  purple crystal x1, blue chest x6. Refreshes (today):
  46/46; Refresh button Free; Quick Buy unchecked. "Pack"
  button top right carries a red badge. The tab's red "!"
  badge is explained by the Pack button / the sold-out Free
  item state - the Free slot reads Sold Out, so nothing free
  is claimable right now. Candidate profile fields: entry
  Events hub > Black Market; currency Black Market Cash
  (earned from Bingo Task rewards); cost 500 cash per item;
  cycle daily refresh, 46 refreshes a day; deadline 22d
  01:46:36; rewards chests, crystals, speed-ups.
- "Desert Battlefield" tab, full name "Desert Storm
  Battlefield" - resolved, the red "New" badge is explained
  (tab never visited). "Event ends in 01:45:52" with the
  banner "The event is over!" - the event already ended;
  "Enter Battlefield" is greyed. Buttons: Rules,
  Achievement, History, Logs. Nothing playable; no owning
  regular needed beyond the events record.
- "Wanted Boss" tab - resolved, NEW candidate task type
  (no regular owns it). Boss "Code 39", "Appears at server
  time: 00:00". "Aircraft heroes deal 50% extra damage on
  the Wanted Boss." "Complete 1 attacks to get the
  following rewards:" coin x6, 5m speed-up x5, red crystal
  x10, blue triangle x250, gold shard x25. "Go" button with
  a red dot and countdown 00:45:32 - the boss is LIVE and
  attackable now, windowed. Buttons: Rankings, Rewards,
  Goals, Battle Record. Top ticker: "...ointed Niermeat as
  Secretary of Science!" (alliance appointment news).
  Candidate profile fields: entry Events hub > Wanted Boss;
  mechanism one attack on the boss (aircraft heroes +50%
  damage); cost none visible (stamina/march cost unread);
  cycle daily appearance at server 00:00; deadline Go
  countdown 00:45:32 at the 16:15 PT read; rewards as
  listed. Needs an exploration unit before any attack -
  attack cost and march rules are unread.
- Fourth tab, "Community" - resolved (label was "Cor..."
  in the chain head read). "Join our community and dive
  into the latest game news..." Visit any community: 200
  Diamonds bonus; link Discord after HQ Lv.8: extra 500
  Diamonds. The 500 Diamonds reward shows "Claimed"
  (green) - already collected. Buttons: Facebook, Discord,
  X, Reddit. Nothing actionable.
- "Arms Race" tab: NOT opened this unit - successor.
- No Zombie Invasion tab anywhere in the strip
  (consistent with the event having ended, verified
  2026-11-14).

### Not walked this unit

- Arms Race tab (Events hub).
- Base "NEW" megaphone (unknown item from the chain head).
- Store by section, alliance panel and station, mail, VIP,
  passes, daily missions, world map, duel and radar.

## Result stats

- target: finish the Events hub tabs and continue the
  post-reset pass across the remaining surfaces
- achieved: Events hub fully walked (7 of 7 tabs), 2 new
  candidate task types recorded, 14 items observed
- resources_gained: none (scout observes only)
- costs: about 3 minutes device time, no stamina or items
- verified: yes (all items read live from screenshots)
- blocker_category: h (by-design partial - unit cap
  reached mid-traversal)
- surfaces_walked: events-complete
- items_observed: 14
- red_dots_seen: 3
- red_dots_explained: 3
- unexplained_red_dots: 0
- unknown_items: 0

## Open for the successor (chain scout-2026-11-20, seq 3)

- Open the Arms Race tab and record the live phase, score
  and tier progress.
- Open the base "NEW" megaphone and record what it is.
- Walk the remaining surfaces: store by section, alliance
  panel and station, mail, VIP, passes, daily missions,
  world map, duel and radar.
- Candidates filed as Issues this pass: Black Market is
  Issue #783 (class idea - new candidate task type, no
  regular owns it, profile fields in this record); Wanted
  Boss is Issue #784 (class play - known event under
  event-claims since Code 87 on 2026-10-25, but no owning
  regular, so live Go windows are only observed, never
  acted on; Code 39 is a rotation, not a new type). The
  Wanted Boss Go window (about 45 minutes at the 16:15 PT
  read) needs an exploration unit before any attack, and
  the Black Market's 7190 cash with three 500-cash items
  needs a spend decision from the owner (never spend
  without approval).
- Note: the day observation.md exists (created by
  ticker-1549 at 15:55 PT); this pass appends its sections
  to it in delivery, per the queue design section 13.

## Delivery

- Commit to records/2026-11-21 via a temporary worktree;
  push via the VPS route; PR #762 already open for the
  branch, no new PR owed.
