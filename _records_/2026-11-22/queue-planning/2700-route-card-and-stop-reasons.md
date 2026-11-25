---
title: Route Card And Stop Reasons For The Unit Briefs 2700 2026-11-23
created: 2026-11-23T05:40:00-08:00
modified: 2026-11-24T07:20:00-08:00
level: L0
version: 1.17.0
description: The short card the unit briefs point to - the stop reasons, the stats for idle-slot reads and a pointer to the verified route table in the CSV beside it, written against the Coach's top partial causes
status: done
activity: queue-planning
run_id: queue-planning-2026-11-23-0540-route-card
trigger: coordinator message with Steer A's flip plan and the 56 percent growth partial rate
started_at: 2026-11-23T05:34:00-08:00
finished_at: 2026-11-23T06:20:00-08:00
verified: every route copied from the operator record named in the CSV; none invented
grounded_in:
  - source: _records_/2026-11-22/coach/0501-conformance-report-2.md
  - source: _records_/2026-11-22/queue-planning/2700-routes.csv
---

# Route card and stop reasons, 2700

## Routes

The verified tap routes are in [2700-routes.csv](2700-routes.csv). The safe empty-ground tap is the bare spot (310,660); (400,640) is NOT safe after a camera shift: WORLD then BASE first. Follow a row exactly; failing twice: 'blocked by route'.

## Drags

A drag that starts on a card moves nothing. THE RECIPE (Weekly Pass page: 150 px, no fling): in ONE message: mouse_move to the blank right margin (x 685), left_mouse_down, wait 1 s, ONE 175 px move, wait 1 s, left_mouse_up, the screenshot after; THE START IS PAGE-SPECIFIC (routes CSV row 'pan start by page'; a Backpack grid: the centre of a tile gap); a malformed wait refuses the whole batch and nothing runs; then tap the visible claim once only if plain. NEVER hold a button across model turns.

## Stop reasons, one phrase each

A unit that cannot do its step writes one of: **blocked by capacity** ('Drill Ground Full'); **blocked by the owner on another device** (a TIPS dialog); **blocked by cost** (resource, shortfall); **blocked by prerequisite**; **blocked by route**; **blocked by window**; **blocked by another app**.

## Standing rule, Steer A, 2026-11-23, after the T3 incident

Any action that could open another app, a browser, a store or a payment surface needs Steer A's approval IN ADVANCE, with an exit plan. NEVER click Go on the check-in banner (web store). An unexpected foreground switch stops the run: touch nothing, tell the Coordinator. Consent requests are human-only. Only the operator and the bridge touch the desktop.

## HUD icons and known dialogs

Before each HUD icon tap a frame must show its LABEL or GLYPH; identify a dialog BY ITS TEXT in a frame just before the tap; one tap. TIPS 'Enable notifications': Cancel, never Enable Now. TIPS about another device: stop, never Confirm (only the relaunch unit may Confirm once, Steer A's standing order). The radar claim 'Completing Radar Tasks today will not grant Alliance Duel points, and you are about to claim 10 radar task rewards at once. Continue?': Confirm allowed for that exact text. Profile popularity dialog (one blue 'Awesome!'): tap it once, then the X. NEVER tap the avatar (110,100): it opens the owner's profile. Any other dialog: stop.

## Classes for a slot read

The pistol press tells the class: the TRAIN UNITS panel opens with no toast = EMPTY QUEUE (close it; never press Train); the toast 'Drill Ground Full' = a FINISHED BATCH waiting behind no room. Press the pistol once per barracks per read when room could exist; record the ready bubble and digits per tent. Crop the digits from the SAVED frame at 6x (never a zoom action). A collect admits what fits. A wrapped gift box is FINISHED WAITING, not idle.

## Stats for idle-slot reads

Reads of building queues, research and troop training close with `--stat slots_idle=<N>` (TOTAL open slots) and, for slots stopped on a full Drill Ground, `--stat slots_blocked_by_capacity=<N> --stat capacity_blocker="Drill Ground Full"`.
