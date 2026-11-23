---
title: Zero sweep 1730 queue run
created: 2026-11-23T02:00:00Z
modified: 2026-11-23T02:00:00Z
executor: ticker-1734
unit: zero-sweep-2026-11-22-1730
chain: pre-reset-sweep-2026-11-22 seq 2
status: partial
---

# Zero sweep 1730 (pre-reset, reset 18:00 PST)

Second of the two pre-reset sweeps for the 2026-11-22 reset day.
Session 17:44-17:59 PST (computer sessions cc-175 and cc-177,
window 127196, then window 136620 after a relaunch). Base power
147,972,269. Resources at sweep start: food 765.4M, iron 1.1G,
coins 109.2M, diamonds 6,456, Gold Bricks 17.72K, lightning 120.

## Profile panel close - breakthrough (R2)

The MY PROFILE panel was still open at session start, as
ticker-1704 left it. Two changed methods were tried on its X
(880,52) and both failed with press-highlight only: a
double-tap, then a 1-second long-press. The third candidate
from 1704's list worked: Cmd+Q quit the app cleanly and a
relaunch (new pid 13567, window 136620) restored the base view
with the panel gone. No Touch ID, no password, no verification
demanded. This breaks the three-unit close blocker chain
(1634 element-number clicks, 1704 coordinate X taps, this
unit's double-tap and long-press) with a working method:
relaunch the game. Evidence for Issue #854 (commented this
pass). Note: this session's window list showed no separate
127250 panel surface - the panel's elements were listed
directly under window 127196 - so the two-surface structure
1704 recorded may vary by session; relaunch sidesteps it
either way.

## Lines read live

- **Bubbles (food, iron, coin)** - dozens standing across the
  farmland on the base view at about 17:51 (food bubbles in the
  765.4K class, iron and coin alongside). Not at zero. The
  fix-up harvest-2026-11-22-1630 closed partial with 0
  collected (ticker-1704); the tracker still shows harvest due
  and the next tick re-produces it for the new day. EXP and
  titanium bubbles not separately read in this unit.
- **Survivors at the front door** - "?" icons standing at the
  front door at about 17:51. Not at zero. Fix-up unit
  survivors-2026-11-22-1803 sits in inbox for the post-reset
  slot; the closing-day line closes uncollected.
- **Armed Truck** - the fully-loaded notice seen live: the
  bottom-left toast fragment reads "truck is full, waiting for
  your command" at about 17:52. Handed to harvest (next tick
  re-produces it); not claimed in this unit - claiming is the
  harvest type's work, not the sweep's. Whether the notice
  survives the reset is unverified.
- **Secrets** - the Secret Command Post read live at about
  17:55: Assist Allies 5/5, Plunder Others 0/5; four tasks
  standing, all Lv.5 (Rescue Test Subject UR, Disrupt electric
  grid UR, Capture the Oil Depot UR, Provide Tech Support to
  Refugees SSR). No task dispatched in this unit. Producing
  unit secrets-2026-11-22-1857 sits in inbox for the
  post-reset slot. (Entry note: the post's left-rail icon is
  the truck-shaped icon at about 47,641 - the same icon the
  trucks entry was mistaken for; the trucks entry point is
  still unpinned.)
- **Alliance** - [AP3x] The Apex, Overall Rating 5.0, Leader
  Abŷss Apex, Power 14,582,845,980, Members 99/100, Language
  English. Red dots live on Help, Alliance Gifts, Alliance
  Store, Alliance Techs and Alliance Events. Assemble button
  visible, not tapped.
- **Donations** - Alliance Techs panel read live at about
  17:59: Tech Donation Today 8,350 contribution points
  (reward threshold 1,000 met); Development tab shows Auto
  Rally Max Level, Quick Construction 9/10, Great Helper Max
  Level, next tech 2/10. The remaining-donation count for the
  30/30 line was NOT read - points are not the count, so
  ledger line 17 does not close on this figure; the count read
  stays owed to a donations unit.
- **Duel** - Alliance Duel League S39 read live at about
  17:59: [AP3x] The Apex ranked 4th, Gold Tier 38-10, Week 1
  Win, Week 2 loss, Weeks 3-4 pending; season ends in 20d
  02:05. The personal daily total against the 3.6M target was
  NOT read - the League screen shows alliance ranking, not
  the personal total, and the Infinite Roulette tab shows
  spins (1/10) with a Sunday 24:00 reset; the personal-total
  location stays unpinned. Ledger line 21 unread for the
  closing day.
- **Right-rail timers** - 00:11:35 and 00:11:36 at about
  17:51, still unidentified (were 01:16:34/01:16:33 at 16:44),
  counting down to about 18:03.
- **VIP** - not re-read this unit (1634: freebie timer-gated
  to about 18:01, points 1,666,520/2,000,000; login chest
  state unread).

## Lines unread in this unit (closed at the 15-minute cap, reset arriving)

Mail categories, alliance gifts tabs, trucks dispatch/plunder
counters, train station panel, daily activity chests, radar
posture, shop Daily Pickup / Free Supply, pass daily pickups,
drone components, upgrade ore, screws, arms-race phase.
Crystal: not located (rule R5, age 28 days from 2026-10-25).
Glittering Market: not located (rule R5, age 22 days from
2026-10-31). Zombie Invasion tab state not re-checked (Events
hub never opened this unit); the chain stays unseeded per the
Nov 14 closure and 1704.

## Fix-ups

None enqueued. Every not-at-zero line found already has a
producing unit in inbox for its post-reset slot
(survivors-1803, secrets-1857, donations-1803, trucks-1857)
or stays due in the tracker (harvest, re-produced next tick);
no duplicate per the (regular, planned_for) invariant. The
closing-day units expiring at the 02:00Z reset lapse with
their lines uncollected or unverified for the day: bubbles,
survivors, trucks counters, duel personal total, donations
count, mail, gifts.

## Result stats

- target: walk the daily collection ledger item by item before the 18:00 reset, read each line live, enqueue priority 1 fix-ups for lines not at zero
- achieved: base screen, secrets, alliance, donations-points and duel-league lines read live (bubbles standing, survivors waiting, truck fully-loaded notice seen, secrets 4 tasks standing, Tech Donation Today 8350, Apex rank 4 Gold Tier); mail, gifts, trucks counters, train, missions, radar, shop, passes, duel personal total, arms-race, crystal, glittering market unread in this unit
- resources_gained: none
- points: 0
- costs: about 15 minutes device time, no spend, no items (unit duration about 900 seconds, 17:44:46-17:59:46 PST)
- verified: yes (base counters, bubbles, survivors, truck notice, secrets counts, Techs points and league rank read live in this unit)
- blocker_category: h (by-design partial - unit closed at its 15-minute cap with the reset arriving; second sweep of the pair)

## Red lines

No diamonds or money spent. No bubbles collected, no secret
task dispatched, no donation made, no roulette spin, no
claim of any kind - the sweep reads lines, it does not
execute other types' work. Assemble not tapped. No
teleport, no research, no building started. The game was
quit with Cmd+Q and relaunched once to clear the stuck
Profile panel; state is server-side and intact (power and
resources identical before and after).

## Follow-up

- The 18:03-slot units carry the new day (survivors-1803,
  donations-1803, trucks-1857, secrets-1857, radar-1803,
  events-1857); the next tick picks them up.
- Issue #854: commented with the relaunch resolution this
  pass; closure belongs to retro.
- The trucks entry point and the duel personal-total location
  stay unpinned - both are sweep-read gaps for the next
  zero-sweep pair to close.
