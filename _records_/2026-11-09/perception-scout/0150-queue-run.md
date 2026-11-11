---
title: Perception scout queue run 0150
created: 2026-11-09T09:50:00Z
modified: 2026-11-09T09:50:00Z
version: 1.0.0
description: Station panel and Wars dot check, stale scout-2026-11-02 chain seq 017, no train preparing, Wars dot absent, fullscreen tap failure re-confirmed
status: partial
grounded_in:
  - source: live game screen on the owner Mac mini, 2026-11-09 01:41-01:50 PT
---

# Perception scout queue run 0150 (ticker-0140)

Unit: scout-scout-2026-11-02-017. Status: partial.
Activity: perception-scout. Chain: scout-2026-11-02, seq 17.
Window: station panel only - train entry and preparation state; Wars dot Issue #212.
Computer session cc-205. Observe-only throughout: nothing claimed,
fought, dispatched, donated, dug or bought.

## Live reads

- Entry: the game was left on the Mail EVENT tab by the 0113 mail
  unit. EVENT list read (observed only): "[AP3x] DCna8ive's train
  has arrived" (1h ago); "[AP3x] Missile Apex's Mega Ex..."
  (3h ago); "[AP3x] DCna8ive's train has departed" (3h ago);
  "Weekly Pass Unclaimed Rewards" (6h ago); "Unclaimed VIP Daily
  Level Rewards" (7h ago); "Unclaimed Event Reward" (7h ago).
  Claim All and Delete All untouched (red line).
- Base screen about 01:45: power 149,209,253 (unchanged from the
  0113 read); food 513.8M, iron 838.3M, coin 25.2M, diamonds
  6,027; 13.22K with a plus button; stamina 60, rising to 61
  during the unit. VS timer 16:16:29, Season II 6d 16:16:29.
  Left column: hammer 1/4 (red dot), flask 2/2, blue bus icon
  (red dot), white truck, radio, hammer, hero portrait, gift
  chest. Right column: Events badge 3, VS, Season II, Alliance
  (red dot), Mail (red dot), Inventory (red dot). Task:
  "Upgrade Builder's Hut to Lv.26 [0/1]". Chat ticker:
  "Breaking News: Intense battle..."; "MittyMoe: (hearts)";
  "Cheese chocolate: #2103 [7YUB]g...". A large gift-box
  decoration stands centre-right on the base.
- Alliance panel about 01:54: [AP3x] The Apex, Overall Rating
  5.0, Leader Jerry Apex, Power 13,532,886,654, Members 96/100,
  Language English. Motto: "We are The Apex. An alliance of
  veteran players. All are welcomed - messages sent in multiple
  languages. (Korean welcome line, messages translated to
  Korean and Portuguese.)" Panel dots: Help, Alliance Gifts.
  NO dot on Alliance Wars, Members, Alliance Store, Alliance
  Techs, Assemble, Strength Ranking, Alliance Events or
  Alliance City.
- Leader change confirmed live: Jerry Apex is the leader row
  (was Abuss Apex / Texan Apex in earlier records); the 0113
  mail unit's Leadership Transfer Notice named the same change.
  Members 96/100 (was 95/100 at the 18:40 read on 2026-11-08).
- Wars dot, Issue #212: ABSENT on Alliance Wars. Seventh
  same-day datapoint (after absent at 12:43, 15:45 and 16:15;
  present with a rally waiting at 18:39, cleared on return).
  No rally waiting per the dot signal. The Rally Intel tab
  itself was not opened this unit; the tab read belongs to the
  alliance group remainder of the current day's scout pass.
- Station / train: BOTH preparation signals absent. No
  "Boarding closes in" banner under the resource bar (the
  ticker shows a treasure-dig line and battle news instead).
  No train icon in the left column: the blue bus icon at
  (55,573) opens the TRUCKS screen, not the station -
  re-confirming the 2026-10-28 / 2026-11-01 entry-icon
  correction (the 1813 unit hit the same). Sixteenth
  same-day no-train confirmation, fourteenth in chain
  scout-2026-11-02. Mail corroboration: DCna8ive's train
  arrived 1h ago and departed 3h ago, so the last train
  already ran.
- Trucks screen, opened by the bus-icon tap (observed only):
  "Today's Trade Count: 0/5"; "Filter out trucks from your
  Warzone" checked; a truncated "Important: President
  HawksMav appointe..." banner; History button top-right;
  four yellow trucks shown with blue cargo icons; "Mega Mode"
  button; tabs "Others' Trucks" (badge 4) and "Your Truck"
  (badge 4, selected); Recover button (red dot) bottom-left.
  Nothing dispatched, nothing claimed: the trucks regular
  owns this surface and trucks-2026-11-08-2257 is already
  in the inbox.
- NEW unexplained signal, about 01:57: a skull icon with a
  red badge 1 and a 00:00:24 countdown appeared at the right
  edge mid-screen on the base view. Meaning unverified -
  not opened (observe-only), carried to the current day's
  scout pass. Candidate readings: a boss or rally timer;
  needs identification before any action.
- Fullscreen tap failure re-confirmed, Issue #475: in
  fullscreen 1920x1080 a tap at (838,700) on the Alliance
  icon did nothing, while the mail back arrow at (323,951)
  worked in the same geometry - the failure is
  button/area-specific, not total. After View menu, Exit
  Full Screen (menu action with path ["View",
  "Exit Full Screen"]), the Alliance button opened at once
  at (931,705) in the 642x951 window. Never use Ctrl+Cmd+F
  or Esc on this app (crash risk).

## Red dot accounting

- Badge signals seen: 10 (Events 3, Alliance dot, Mail dot,
  Inventory dot, bus-icon dot, 99+ badge, panel Help dot,
  panel Gifts dot, skull badge 1, hammer 1/4 counter).
- Explained 6: Events 3 to the events / arms-race regulars;
  Alliance dot as the roll-up of Help and Gifts; Help dot to
  the help regular; Gifts dot to the gifts regular; bus-icon
  dot to the trucks regular (unit queued); Mail dot to the
  mail regular (System / Regular / Battle Report still
  unwalked per the 0113 record).
- Unexplained 4: Inventory dot (store group, carried);
  99+ badge (carried); skull badge 1 with the 00:00:24
  timer (new, carried); hammer 1/4 counter (construction
  queue signal, carried - no owning regular).
- Unknown items 2: furnace overdrive toast (not re-read this
  unit); skull timer meaning.

## What was not done

- Wars Rally Intel tab not opened; store, base-remainder and
  alliance-remainder groups not walked. They belong to the
  current reset day's scout heads (scout-2026-11-08-1800 and
  scout-midday-2026-11-08-0700, both in the inbox). No
  successor unit is enqueued from this stale-chain unit
  under the (regular, planned_for) anti-duplication
  invariant. Tracker untouched.
- The perception-scout activity metadata (grounded_in entry
  for this run) is NOT updated in this pass: _activities_ is
  tier 2 and stays out of the records commit per the
  recording rules. The knowledge flow may add it.

## Red lines

- No diamonds or money spent. Nothing claimed, fought,
  dispatched, donated, dug or bought. Delete All never
  pressed. No mail deleted. No login or verification was
  demanded, and no different-device dialog appeared.

## Stats

- target: 2
- achieved: 2
- resources_gained: none
- costs: about 9 minutes of unit time, no items spent
- verified: yes
- blocker_category: c
