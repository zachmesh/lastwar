---
title: Ticker 1904 scout chain seq 3 queue run
created: 2026-11-22T03:22:00Z
modified: 2026-11-22T03:22:00Z
level: L0
version: 1.0.0
description: Scout unit scout-scout-2026-11-20-003, chain scout-2026-11-20 seq 3, partial - Mall top level plus Weekly Deal and Super Monthly Pass walked live
status: unverified
---

# Ticker 1904 scout chain seq 3 queue run

- Executor: ticker-1904. Unit: scout-scout-2026-11-20-003,
  chain scout-2026-11-20 seq 3, priority 2, est 8 minutes.
- Session window: 19:12 to about 19:21 local. Device token
  taken 19:12:02, released 19:21. Computer session cc-35 on
  Zhen's Mac mini (1c817413-83e2-0545-cb90-36d5e096a6bd),
  LastWar window 105986, windowed 763x1050.
- Tool identity (rule R13): queue.py at
  /home/hatch/workspace/lastwar-wt-1904-ticker/_tools_/queue.py,
  sha256 ce40699212de8144e8dc924c969273cc79d7fa12a2c389bbf780bb9bffe74b97,
  git HEAD 9fa672a8b42e044ba01e464e06853adf5497bb9c, currency current
  against main. Worktree ticker-1904-1121-delivery, fast-forwarded
  to main 9fa672a8 (the 19:00 batch merge of PR #762) so the tool
  copy is current; the records-branch copy predated main by the
  _ledger_line_count addition of PR #790 and refused decision
  commands until the fast-forward.
- Own PRs first: PR #762 (records 2026-11-21) MERGEABLE and CLEAN,
  no comments addressed to this job; it merged into main as
  9fa672a8 in the 19:00 batch during this pass. No other PR names
  this job as owner.
- Sync: reaped 0, expired 3, produced research-2026-11-21-1803
  and building-queues-2026-11-21-1803; 21 regulars already queued.
  No zombie chain: the Glacieradon event ended (verified live by
  ticker-1804 on 2026-11-14, unit 037 failed, chain closed), the
  live pool holds no zombie unit, and zombie-invasion is absent
  from the loaded roster (stale-roster warning, issue #198).
- Recovery in this pass: ticker-1704's record commit sat
  unpushed on local branch ticker-1704-delivery (443e11e4dd8).
  Cherry-picked as 7f32ed3bb51 with union resolution of the
  action-log and day-INDEX conflicts (both sides' lines kept, no
  entry lost). Its scout seq 2 record, harvest record, done units
  and observation append now ride this pass's delivery.

## What was walked

Base screen re-read on entry, then the Mall (cart icon top right,
grounded 917,48), two section tabs, then back to the base screen.
Scout observes only: nothing claimed, fought, dispatched, donated
or bought. All figures read live from screenshots in this unit.

### Base screen, read live about 19:13 local

- Level 30, power 149,653,371.
- Food 752.7M, iron 1.1G, coins 102.4M, diamonds 17.72K,
  stamina 89, cart 5,246.
- March Queues 0/3, Add Queue button.
- Events badge 1; VS "Calculating."; Alliance Assembly countdown
  22:45:00 at entry, 22:40:3x on exit.
- Radio badge 1; Alliance red dot; Mail red dot; Inventory red
  dot; 99+ chest badge bottom right above BASE.
- "Build: Oil Well (0/1)" banner bottom left (standing banner,
  sixth live read).
- Toast "Important: President HawksMav appointed..." across the
  top; Breaking News ticker plus two chat lines at the bottom.
- Framing note: the game canvas renders wider than the 763-wide
  window - the right-column icons (Alliance, Mail, Inventory,
  BASE) and the rightmost Mall tab are cut at the right edge.
  Taps landed as aimed at the measured coordinates; no offset
  correction was needed in this windowed framing.

### Mall top level, read live about 19:15 local

- Header HOT DEALS / MALL. Tabs left to right: Official Event
  (red dot), Weekly Deal, Super Monthly Pass, Weekly Pass,
  Diamond, Gold Bullion Mall (name truncated at the right edge,
  presumed not verified - the one new unknown item this unit).
- Headline "Visit the Last War Store for more free rewards!".
- Carousel page 1: FREE GIFT card ("Claim your gift today!"),
  FREE TOMORROW card (x5 / x5 / x5, "Randomly obtain one."),
  "Claim points and redeem great rewards" card. Go button, two
  page dots. Nothing tapped: scout observes only.

### Weekly Deal tab, read live about 19:18 local

- Title Weekly Deal, period 2026-11-16 00:00:00 to
  2026-11-22 23:59:59.
- Valor Badge (Epic) $99.99, 1 purchase available: red crystal
  10.0K, blue 1.0K, 5m speed-up 1.2K, gold 80, grey crates 20,
  chest, +1000.
- Base Upgrade (Epic) $19.99, 1 purchase available: red 2.0K,
  5m 180, grey 12, brown 12, gold 12, 10K badge, +200.
- UR Set (Elite) $49.99, 1 purchase available: red 5.0K,
  5m 600, coin 300.0K x2, 25K badge x2, 750, +500.
- More rows below the fold, unread. All rows are paid offers;
  nothing bought.

### Super Monthly Pass tab, read live about 19:20 local

- Title Monthly Pass, duration 30 days.
- Squad 4 Lv.20: "Unlock an extra squad!" with two items.
- Daily Pickup: 100 x1, 50 x2, gold card x2, 5m speed-up 60,
  iron 200.
- Legendary badge. Get Now: +2500 red crystal plus five items
  x1 each, +250. Buy x1 and Switch buttons. Nothing bought.
- Back arrow returned to the base screen; power unchanged
  149,653,371 on exit.

## Result statistics

- Surfaces walked: base (re-read), store-top, store-weekly-deal,
  store-monthly-pass.
- Items observed: 36 (listed above).
- Red dots seen: 7 (Events 1, radio 1, Alliance, Mail,
  Inventory, 99+ chest, Official Event tab). Explained 6, all
  routing to their owning regulars already queued. Unexplained 1:
  the 99+ chest badge bottom right - its identity was not
  re-verified live in this unit (the NEW! chest was left
  unexplained in the 2026-11-01 scout record; unit 002 resolved
  the megaphone, not this chest).
- Unknown items: 1 new (Gold Bullion Mall tab name truncated at
  the right edge). Still open from earlier units: the 00:00:51
  countdown and the Chat top-bar NEW! icon.
- Status: partial by design (blocker_category h). The unit cap
  closed the walk with the store partly walked.
- Unwalked, carried to the successor (chain scout-2026-11-20,
  seq 4): remaining Mall tabs (Weekly Pass, Diamond, Gold
  Bullion Mall and any further tabs off the right edge),
  alliance panel and station, VIP, passes, daily missions,
  world map, duel and radar; the Chat top-bar NEW! icon still
  unidentified.
- Resources gained: none, scout observes only. Costs: about 9
  minutes device time, no stamina or items. Verified: yes, all
  closing figures are same-unit live reads.
- No zombie chain seeded (event ended). No issue filed: the
  roster staleness warning is already issue #198, and the
  99+ chest is a re-read gap for the successor, not a new
  discovery.
- Pass budget: this pass executed one unit and spent the rest of
  its budget on delivery, including the ticker-1704 recovery
  above; the execute loop ends here with units still in the
  inbox, by design - partial units requeue safely.
