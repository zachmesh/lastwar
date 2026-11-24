---
title: Route Card And Stop Reasons For The Unit Briefs 2700 2026-11-23
created: 2026-11-23T05:40:00-08:00
modified: 2026-11-24T05:15:00-08:00
level: L0
version: 1.13.0
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

The verified tap routes are in [2700-routes.csv](2700-routes.csv), one row per target with its operator record. The safe empty-ground tap is the bare spot (310,660); (400,640) is NOT safe after a camera shift: WORLD then BASE first. Follow a row exactly; failing twice: 'blocked by route'.

## Drags

A drag that starts on a card moves nothing. THE RECIPE (13:01Z: the Weekly Pass page moved 150 px, no fling): in ONE message: mouse_move to the blank right margin (x about 685), left_mouse_down, wait 1 s, ONE 175 px move, wait 1 s, left_mouse_up, the screenshot after; a malformed wait refuses the whole batch and nothing runs; then tap the visible claim once only if plain. Plain drags: 250 px flings, 70 and 135 px move nothing. NEVER hold a button across model turns.

## Stop reasons, one phrase each

A unit that cannot do its step stops and writes one of: **blocked by capacity** ('Drill Ground Full', with the tag text); **blocked by the owner on another device** (a TIPS dialog); **blocked by cost** (resource, shortfall); **blocked by prerequisite**; **blocked by route**; **blocked by window**; **blocked by another app** (an unexpected foreground switch).

## Standing rule, Steer A, 2026-11-23, after the T3 incident

Any action that could open another app, a browser, a store or a payment surface needs Steer A's approval IN ADVANCE, with the exit plan stated. NEVER click Go on the check-in banner (web store). An unexpected foreground switch stops the run at once: press, answer and touch nothing in the other app, tell the Coordinator. Consent requests are human-only. Only the operator and the bridge touch the desktop.

## HUD icons and known dialogs

Start every HUD icon tap with a frame that shows its LABEL or GLYPH; identify a dialog BY ITS TEXT in a frame just before the tap; one tap. TIPS 'Enable notifications': Cancel, never Enable Now. TIPS about another device: stop, never Confirm. The radar claim 'Completing Radar Tasks today will not grant Alliance Duel points, and you are about to claim 10 radar task rewards at once. Continue?': Confirm allowed for that exact text. Any other dialog: stop.

## Three classes for a slot read

The toast 'Drill Ground Full' is identical for an empty queue and a FINISHED BATCH waiting behind no room. Classify each slot as EMPTY QUEUE, FINISHED BATCH WAITING or BLOCKED BY THE TOAST in THIS read. Press the pistol once per barracks per read when room could exist; record the ready bubble and its digits per tent (portrait finished, clock training, none empty); a collect admits what fits [D]. A wrapped gift box is FINISHED WAITING, not idle.

## Stats for idle-slot reads

Reads of building queues, research and troop training close with `--stat slots_idle=<N>` (the TOTAL open slots, blocked ones included) and, for slots stopped on a full Drill Ground, `--stat slots_blocked_by_capacity=<N> --stat capacity_blocker="Drill Ground Full"` (blocker at most 40 characters).
