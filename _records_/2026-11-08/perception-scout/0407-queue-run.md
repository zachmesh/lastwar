---
title: Ticker 0404 perception-scout run
created: 2026-11-08T12:07:00Z
modified: 2026-11-08T12:15:00Z
level: L0
version: 1.0.0
description: Ticker-0404 scout-store remainder of the stale 2026-11-04 midday pass, five Mall tabs walked live, observe-only
status: done
grounded_in:
  - source: unit scout-midday-scout-mid-2026-11-04-003, chain scout-mid-2026-11-04, live game reads in this session
  - source: _activities_/perception-scout/INDEX.md
---

# Ticker-0404 perception-scout run

- Executor: ticker-0404. Unit: scout-midday-scout-mid-2026-11-04-003 (chain scout-mid-2026-11-04, seq 3). Session about 04:07 to 04:15 local (12:07 to 12:15Z), computer session cc-81 on the Mac mini. Status: done.
- Observe-only throughout: nothing claimed, fought, dispatched, donated, dug or bought. No price tag tapped, no paid button touched. Game left on the base screen.
- This unit completes the store remainder its predecessor (seq 002, partial) named: the five Mall tabs Super Monthly Pass, Weekly Pass, Diamond, Gold Brick Mall and Hot Sale Packs, all walked live and recorded in the day observation file (`perception-scout/observation.md`, appended section "Pass scout-mid-2026-11-04-003").
- Tracker untouched: this is a stale 2026-11-04 chain unit executed late; marking the scout-midday regular done would suppress the current reset day's own midday pass (staged head scout-midday-2026-11-08-0700 still in inbox). No successor unit enqueued: the chain is spent with this unit and the remaining groups of the current reset day belong to the current day's scout units already staged.

## Pool repair before the unit (Issue #441)

- `queue.py next` first returned `donations-2026-11-08-0745`, and `claim` failed with "state is None": no such file exists in any pool state folder. Cause: `_queue_/inbox/donations-2026-11-08-1146.md` as committed on records/2026-11-08 (head b50dc4bad9) still holds literal merge-conflict markers from the ticker-0334 branch-side resolution (merge e03673960e, whose message says every conflict resolves to the branch side). The file carried two `unit:` lines (1146 HEAD side, 0745 github/main side); the frontmatter parser keeps the last duplicate key, so `list_units` reported the unit as 0745 while `find_unit` looked for a 0745.md file that does not exist.
- Fix applied in this pass: rewrote the file keeping only the HEAD (1146) side, per the e03673960e merge message - 1146 is the live successor re-read unit (not_before 12:17Z); the 0745 side was superseded by the dedup to 0843 (done). `next`/`claim` then worked. Filed as GitHub Issue #441 (label tooling), proposing a guard that rejects unit files with conflict markers or duplicate top-level keys before they can land on the records branch. The repair itself is committed with this pass's records; it is tier-1 queue state, not a tool change.
- Own PRs first: PR #430 (records/2026-11-08) is open and CLEAN at head b50dc4bad9, awaiting the 07:00 batch; its comments are integrator re-checks only, nothing addressed to this job. No conflict to resolve, no reply owed.

## Entry state, read live

- Game found open on the Alliance Techs panel (Quick Construction detail), left there by the earlier donations unit: Quick Construction 8/10, Tech EXP 1.2M/6.0M, Current +20%, Next Level +22.5%, Donation Reward 50/50, Donation Count 1/30. HUD: food 478.8M, iron 802.1M, coin 6.9M, cart 4,217. Top banner truncated: "Important: President HawksMav appointed BambergSV as Secretary of Development...".
- Alliance panel about 04:09: [AP3x] The Apex, 5.0 stars, Leader Abŷss Apex, Power 13,363,455,935, Members 96/100 (was 94/100 in the 2026-11-03 reads), Language English. Red dots on Alliance Wars, Help, Alliance Gifts and Alliance Techs; none on Members or Alliance Store. Alliance Star (Event 40) banner, Time Left 13:41:28, Enter not tapped.
- Back-arrow grounding, session lesson: the Alliance panel back arrow does not answer centre taps. Five attempts at the visual centre norm (186, 893) - two single taps, one long-press, one snap-off exact tap, one double-click - produced no change; the overlapping circular portrait at the arrow's top-right corner swallows them. A tap at the arrow's lower-left norm (140, 905) returned to the base screen at once. When a centre tap fails twice, move to the lower-left corner instead of repeating the point.
- Base screen about 04:11: account power 149,850,353 (was 149,940,141 at the 2026-11-03 00:17 read); HUD food 478.8M, iron 802.1M, coin 6.9M, second row 25.0M and 922.2K, 13.22K with a plus button, stamina 120, cart 4,217. Left column: avatar Lv.30, hammer 2/4, flask 2/2, green face, truck, radio, survivor portraits badge 2, backpack 8. Right column: Events x2 badge, VS, 7d 13:49:24 timer, Season II, Alliance, Mail red dot, Inventory red dot, WORLD. Wanted Boss timer 00:00:43 with badge 2. Resource bubbles standing on many buildings, observed only. Furnace toast again "[22/60]", still unexplained, observed only. NEW! badge, 99+ chat badge, HEROES. Chat ticker: "Breaking News: Intense battle..." and "Cheese chocolate: #2092 [AoMF]...".

## The five Mall tabs, read live

- Mall entry: cart icon top-right, grounded this session at norm (917, 52). The strip scrolls horizontally; Hot Sale Packs sits right of Gold Brick Mall and needs one leftward drag on the strip to reach.
- Super Monthly Pass (about 04:12): Monthly Pass, Days Left 14, Squad 4 Lv.20, "Unlock an extra squad!". Daily Pickup row (items x1, x2, x2; 5m speedup x60; 200 currency). Get Now +2500 red gems plus four item icons x1 each. Rewards Left: 14, "Claimed" greyed - today's pickup already claimed, passes regular has nothing to do here today. Monthly Pass Extension $24.99, paid, never tapped. "Legendary" badge.
- Weekly Pass (about 04:12): "Weekly Pass rewards reset at 18:00:00" - fifth confirmation, closing the open re-read item the 0122 unit carried (18:00:00, not 19:00). Free Supply box; "Legendary" banner; "Get all at a discount"; "Instant Gain on Purchase" (300 x5, 2.5K red gems, purple item x1); "Take All $19.99" with a 200 badge, paid, never tapped. $2 Drone Components Weekly Pass (Legendary), Validity 7 Day(s): Daily Pickup Lv.4 item x1, Total Lv.4 x7, Get Now (500, 100, green item x1), $4.99 with a 50 badge. $1 Drone Parts Weekly Pass (Epic), Validity 7 Day(s): Daily Pickup gear x15, Total gear x105, Get Now (red gem, 100, green item), $4.99 with a 50 badge. Rows below the fold not read.
- Diamond (about 04:13): "Initial Buy Reward - Enjoy Double Diamonds". Every tier x2: 10000 diamonds $99.99 (+1000), 5000 $49.99 (+500), 2000 $19.99 (+200), 1000 $9.99 (+100), 500 $4.99 (+50), 100 $0.99 (+10). All paid, observe only.
- Gold Brick Mall (about 04:13): "Gold Brick Mall - Extra 5% Bonus". Every pack "INITIAL BUY REWARD" with a "Free Gift" badge. Visible tiers: x500 gold bricks $4.99 (Free Gift x500), x1000 $9.99 (Free Gift x1000), x100000 $999.9 (Free Gift x5000), x50000 $499.9 (Free Gift x2500). Rows below the fold partly visible, not read. All paid, observe only.
- Hot Sale Packs (about 04:14): empty page, gift-box art, "Packs sold out". Nothing on sale.
- Mall tab strip verified end to end: Official Event, Weekly Deal, Super Monthly Pass, Weekly Pass, Diamond, Gold Brick Mall, Hot Sale Packs - seven tabs, no Crystal Shop tab and no Glittering Market tab, consistent with the 0504 and 0514 reads. HOT DEALS tab carries a red dot, explained by the check-in banner: "Participate in the check-in event and claim great rewards!", FREE GIFT "Claim your gift today!", FREE TOMORROW (x5, x5, x5, "Randomly obtain one."). The claim belongs to the shop-claims regular; this unit claimed nothing.

## Red dot accounting

- Seen 12, explained 7, unexplained 5. Explained: HOT DEALS dot (shop-claims regular, check-in FREE GIFT claimable today); Help, Gifts and Techs dots (help, gifts, donations regulars, units queued); Events x2 and Mail dots (events, mail regulars, units queued); Wanted Boss badge 2 (Wanted Boss tab read as ended today by the 0004 pass). Unexplained 5, all outside this unit's store group and carried by the current day's scout pass: Alliance Wars dot (Issue #212, open), Season II badge 1 (standing unexplained), backpack 8 and Inventory dot (inventory surface not opened in this unit), 99+ chat badge (chat surface not walked). No red dot is unexplained inside the five store tabs walked: none of the five tabs carries a dot.
- Unknown items 0 in the surfaces actually walked. unmatched_labels: none in the surfaces actually walked.

## Result statistics

- target: 5 tabs. achieved: 5 tabs. resources_gained: none. verified: yes. surfaces_walked: 5. items_observed: 12. red_dots_seen: 12. red_dots_explained: 7. unexplained_red_dots: 5. unknown_items: 0.
- Follow-up: Issue #441 (pool guard for conflict markers in unit files); Issue #212 stays open (Alliance Wars dot); the current day's scout pass owns the five carried dots.
