---
title: Zero sweep 1630 queue run
created: 2026-11-23T00:58:00Z
modified: 2026-11-23T00:58:00Z
executor: ticker-1634
unit: zero-sweep-2026-11-22-1630
chain: pre-reset-sweep-2026-11-22 seq 1
status: partial
---

# Zero sweep 1630 (pre-reset, reset 18:00 PST)

First of the two pre-reset sweeps for the 2026-11-22 reset day.
Session 16:41-16:48 PST (computer session cc-171, window
127196, window mode, never brought to front). Base power
147,972,269. Resources at sweep start: food 765.4M, iron 1.1G,
coins 109.2M, diamonds 6,456, Gold Bricks 17.72K, lightning 120.

## Lines read live

- **Bubbles (food, iron, coin)** - food, iron and coin bubbles
  standing across the farmland on the base view at about 16:44
  (several food bubbles in the 765.4K class, iron and coin
  bubbles alongside). Not at zero. Fix-up unit
  harvest-2026-11-22-1630 already in inbox. EXP and titanium
  bubbles not separately read in this unit.
- **Survivors at the front door** - two "?" icons standing at
  the front door on the base view at about 16:44. Not at zero.
  Fix-up unit survivors-2026-11-22-1803 already in inbox.
- **VIP** - VIP13, logged in 4 days in a row, points
  1,666,520/2,000,000. Daily Freebie shows a timer of 01:13:18
  at about 16:48, not claimable now (available after the reset,
  about 18:01 PST). The login chest icon top-right of the VIP
  panel was not read this unit. Fix-up unit
  vip-2026-11-22-1630 already in inbox.
- **Badges read, not opened** - Events badge 1, radar dish
  badge 11, trucks red dot, WORLD 99+, hammer 1/4 (red dot),
  flask 2/2. Their producing units sit in the inbox for their
  slots (events-2026-11-22-1857, radar-2026-11-22-1630,
  trucks-2026-11-22-1630).
- **Right-rail timers** - the two unidentified timer icons read
  01:16:34 and 01:16:33 at about 16:44, still unidentified, same
  as the ticker-1604 scout read earlier today.
- **Build** - Oil Well [0/1].

## Lines unread in this unit (closed at 7.4 minutes, token lease ending)

Mail categories, alliance gifts tabs, donations count, trucks
dispatch/plunder counters, train station panel, daily activity
chests, duel daily total, radar posture, shop Daily Pickup /
Free Supply, pass daily pickups, drone components, upgrade ore,
screws, Armed Truck timer, secrets, treasures, arms-race phase.
Crystal: not located (rule R5, age 28 days from 2026-10-25).
Glittering Market: not located (rule R5, age 22 days from
2026-10-31). No new information on either this unit.

## Fix-ups

None enqueued. Every not-at-zero line found already has a
producing unit in the inbox for its slot (harvest-1630,
survivors-1803, vip-1630); the VIP freebie is timer-gated, not
claimable. Crystal and Glittering Market have no producing unit
but their status is not-located, so no fix-up unit can act on
them; the 17:30 sweep re-checks.

## Method notes (R2)

- The VIP back-arrow tap at the measured point (109,936) first
  returned outcome_unknown with a permissions error and no
  verified change; a second tap at the same point closed the
  VIP panel to Profile. A single measured point retried once
  after a verified no-change is the pivot, not a blind repeat.
- Element-number close-button clicks (element 29 on the VIP
  panel, element 1 on the Profile panel) twice produced a
  "Google Chrome came to the front" artifact with no verified
  close. The next unit should close panels with coordinate
  taps on the panel's own back arrow, never element-number
  close buttons.

## Follow-up

- Second sweep zero-sweep-2026-11-22-1730 already staged for
  17:30 PST; it re-walks the lines this unit could not reach.
- The VIP login chest state (top-right chest icon) was not
  read; vip-2026-11-22-1630 must read it.

## Result stats

- target: walk the daily collection ledger item by item before the 18:00 reset, read each line live, enqueue priority 1 fix-ups for lines not at zero
- achieved: base screen and VIP lines read live (bubbles standing, survivors waiting, VIP freebie timer-gated, badges read); mail, gifts, donations, trucks, train, missions, duel, radar, shop, passes, secrets, treasures, arms-race, crystal, glittering market unread in this unit
- resources_gained: none
- points: 0
- costs: about 8 minutes device time, no spend, no items (unit
  duration 443 seconds, 16:42:05-16:49:28 PST)
- verified: yes (base counters, bubbles, VIP points and freebie timer read live in this unit)
- blocker_category: h (by-design partial - unit closed at 7.4 minutes with the token lease ending, second sweep staged)

## Red lines

No diamonds or money spent. The VIP Exclusive $99.99 offer was
not tapped. No claim, fight, dispatch, donation or purchase.
The Profile panel was left open at session end (its close
button misbehaved per the method note above); the next unit
navigates from there.
