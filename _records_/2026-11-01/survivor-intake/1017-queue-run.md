---
title: Survivors diagnostic queue run
created: 2026-11-01T17:17:00Z
modified: 2026-11-01T17:17:00Z
version: 1.0.0
description: Survivors diagnostic unit survivors-diagnostic-001 executed by ticker-1004, partial, gate not located, Quick Dispatch not located, factory panel verified without it
status: partial
---

# Survivors diagnostic queue run 2026-11-01 about 10:17 PDT

- Unit: survivors-diagnostic-001, executor ticker-1004, status partial.
- Session window: about 10:05 to 10:17 PDT. No different-device dialog,
  no login or verification demanded, signed in as HidingAnt504,
  power 148,957,193. One computer session drop mid-unit (cc-4 lost,
  cc-5 restarted, LastWar re-selected, no game state lost).
- Survivor-intake metadata read before acting, including the
  2026-10-31 retro standing blocker (22 of 22 queue-era survivor
  units partial, Quick Dispatch never ran) and the M5 method-change
  decision behind this diagnostic unit.

## Entry path measured fresh in this unit

Ordered screens from the base screen, with controls measured
fresh in this unit (no coordinate copied from an earlier unit):

1. Base screen (window mode, LastWar on the Mac mini).
   - Map drag pan, measured as a drag from norm 600,600 to
     300,400, then reversed 300,400 to 600,600, restoring the
     original base view. Both pans produced a visible map shift.
2. Building selection screen (same base screen, building selected).
   - Control: a resource house building, tapped at norm 144,295
     in the panned view. Selection label read
     "Titanium Alloy Factory No.1, Lv.30" at the top left.
   - Control: orange info "i" button for that building, tapped
     at norm 111,329 in the panned view.
3. Building Details panel for Titanium Alloy Factory No.1.
   - Panel read verbatim: "TITANIUM ALLOY FACTORY NO.1",
     "Lv.30", "Power 36,900", "Output/hr 21,600",
     "Max Production Time 1d 00:00:00", "Maximum Level Reached",
     and a note line "This building will disappear when the
     season ends".
   - Survivor list: none shown. Quick Dispatch button: none
     shown. This building type therefore does NOT carry the
     Quick Dispatch path; a later unit must try a survivor-post
     building (Iron Mine, Farmland) specifically, not a
     seasonal factory.
   - Panel closed with the X at norm 900,186; the base screen
     returned, verified on a second observation.
4. Second building selection, original base view.
   - Control: a centre resource house, tapped at norm 472,448.
     A small round selection icon appeared beside it, and a
     second tap at norm 478,438 selected the central tower,
     labelled "High-heat Furnace, Lv.30".
   - Furnace controls measured fresh, panel NOT opened in this
     unit (unit time cap): flame button at about norm 459,448
     and info "i" button at about norm 524,448. These are
     measured points for the next unit, not a verified panel.
   - Quick Dispatch: not located. Written as not located, never
     inferred from the older metadata description.

## Gate line

- Gate line text: NOT READ. The signed "Zombies" front gate
  itself was not located in this unit, so no gate line can be
  quoted verbatim and the gate is NOT claimed empty.
- Areas inspected in this unit, with what they actually showed:
  - Original base view centre resource row: small houses with
    286.4K resource bubbles, a helicopter vehicle, a green
    turret building; no question-mark bubble, no survivor figure.
  - Bottom-left STOP road barrier area: STOP sign, cannons,
    a tree, a brown circular ground mark; no question-mark
    bubble, no survivor figure.
  - Top-left road (enlarged crop): a zombie figure with red
    splatter on the road and a small walking figure near the
    headquarters; no question-mark bubble, no survivor line.
  - Panned view (base shifted to the top left): same resource
    row and snow area; no question-mark bubble, no survivor line.
- No survivor figure was verified, so no survivor was tapped,
  no recruit card or dialog was opened, and no live Quick
  Dispatch was completed through the map. Survivor count
  before/after: not applicable, 0 recruited, 0 dispatched.

## Closing

- Status partial: the diagnostic map is incomplete - the gate
  was not located and Quick Dispatch was not located. The
  deliverable of this unit is the fresh-measured partial map
  above plus the verified negative result that the seasonal
  factory panel carries no Quick Dispatch, which narrows the
  next attempt to survivor-post buildings.
- No other regular was merged into this unit. The game was left
  on the base screen.
- Tracker untouched (partial unit), per the queue rules.
- No diamonds, money, speedups or paid buttons were used. No
  building, research or assembly action was taken. One tap at
  norm 472,448 collected a resource bubble as a side effect of
  selecting a building (iron read 16.7M before, 18.1M after in
  the HUD); that collection is not claimed as survivor work.

## Result statistics

- survivors_recruited: 0
- question_bubbles_found: 0
- live_quick_dispatch_completed: no
- gate_located: no
- quick_dispatch_located: no
- target: complete verified map from base to Quick Dispatch, gate line verbatim
- achieved: 0
- resources_gained: none claimed as survivor work
- costs: about 12 minutes, no items consumed
- verified: no
- blocker_category: c
