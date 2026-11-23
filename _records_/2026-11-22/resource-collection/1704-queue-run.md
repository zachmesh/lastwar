---
title: Harvest 1704 queue run
created: 2026-11-23T01:26:00Z
modified: 2026-11-23T01:26:00Z
executor: ticker-1704
unit: harvest-2026-11-22-1630
status: partial
---

# Harvest 1704 (pre-reset fix-up, reset 18:00 PST)

Session 17:09-17:24 PST (computer session cc-172, window
127196, window mode, never brought to front). Base power
147.9M (Profile panel read). **0 bubbles collected, 0 panels
read, base view never reached** - the whole unit budget went
to closing the MY PROFILE panel left open by the ticker-1634
zero-sweep unit.

## What happened

- At session start the MY PROFILE panel was open (left open by
  ticker-1634, as its record discloses). Lv.30 [AP3x]Bears
  Lair, Power 147.9M, 48.6K, Lv.63, Lv.2, [AP3x]The Apex,
  VIP13, #2110, Moments "No posts found."
- First three close attempts went to the wrong surface: taps
  on the X (896,50, exact-pointer), on the dimmed area
  (50,500) and a snapped X tap were sent while window 127196
  (the base view) was selected, so they passed through to the
  base underneath and did nothing to the panel. A drag
  (swipe-back) was refused outright: "Window 127250 of this
  app, such as a sheet, popover or panel, covers this point,
  and a drag goes only to the selected window."
- **Surface finding:** the Profile panel lives on a separate
  surface, window 127250 (642x919, accessibility=false),
  covering the base window 127196. It must be activated by
  surface_id before any tap reaches it. This is the first
  unit to record the two-surface structure explicitly.
- After activating 127250, three more X taps (896,50;
  grounded 834,54; visually-estimated centre 880,52) each
  produced only a press-highlight visual change in the X
  region (7-12% changed area) and no close. A swipe-back
  drag on the screenshot-only surface is unsupported
  ("can't send drag to it... Use click at a point of its
  image").
- The X-tap method is now a repeated failure: ticker-1634
  (element-number close clicks, Chrome-front artifact) plus
  this unit (four coordinate X taps, highlight only). Filed
  as GitHub Issue #854 (tooling class). Per R2 the next unit
  of any type that finds the Profile panel open must arrive
  with a changed close method (candidates: double-tap on
  the X, long-press, or relaunching the game so the panel
  is not open at session start); a third consecutive unit
  blocked the same way is a process failure to report to
  the owner.

## Live reads (same-unit screen reads)

- Profile: Power 147.9M, VIP13, rank #2110, 1,840 likes.
- **Zombie Siege banner:** "Zombie Siege is about to
  attack: 00:02:49" at about 17:20, ticking to 00:02:19 by
  17:23 - a live event signal, not the ended Glacieradon
  Zombie Invasion chain. No Zombie Invasion tab state was
  read this unit; the chain stays unseeded per the 1634
  read and the Nov 14 closure.
- Bottom-left toast fragment "...re fully loaded, ...m them"
  visible behind the panel at about 17:20 - the same
  fully-loaded notice the harvest lineage tracks (Issue
  #566); the Armed Truck loot state is still unverified,
  sixteenth deferral in the lineage, retro action
  A-2026-11-11-05 still unmet.
- Timer top-right 23:12 to 23:15 across the unit - the game
  is live.

## Not done

- No resource bubble tapped, no panel Collect run (food /
  iron / coin panels unread), no Armed Truck location
  attempt. The 1630 sweep fix-up (bubbles standing at
  16:44) is unverified at zero; the 17:30 sweep unit must
  re-check it.
- Tracker untouched (partial), so the regular stays due
  and the next tick re-produces it.

## Result stats

- target: collect the standing resource bubbles (pre-reset fix-up for the 1630 zero sweep) and verify the Armed Truck loot state
- achieved: base view never reached; 0 bubbles collected, 0 panels read; Profile panel close blocker documented with the two-surface finding; Issue #854 filed
- resources_gained: none
- points: 0
- costs: about 15 minutes device time, no spend, no items (unit duration about 900 seconds, 17:09-17:24 PST)
- verified: yes (Profile figures, Zombie Siege banner and timer read live in this unit; the zero collections are a verified absence - no bubble was tapped)
- blocker_category: c (tap method - panel X unresponsive to coordinate taps; second consecutive unit blocked by the same close failure)

## Red lines

No diamonds or money spent. No claim, fight, dispatch,
donation or purchase. No panel opened beyond the Profile
panel that was already open at session start. The Profile
panel was left open at session end, same state as session
start.
