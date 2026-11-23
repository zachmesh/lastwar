---
title: Operator run recipe and hazards 0054
created: 2026-11-23T16:12:00Z
modified: 2026-11-23T21:37:00Z
version: 1.3.0
description: Operator sidecar page - the run recipe and hazards moved verbatim from handover 0.9.0, plus the run-shape and never-press lines from the route tables
status: handover
grounded_in:
  - source: handover 0.9.0 section Run recipe and hazards, moved 2026-11-23T15:12Z into the sidecar detail page and split out 2026-11-23T16:12Z
  - source: sidecar rows Run shape (records alliance-donations 1441, resource-collection 1445) and Never (shop-claims 1528-t3-focus-incident.md)
---

# Run recipe and hazards

Part of [the sidecar](0054-operator-handover-detail.md). The seat page `_seats_/operator/handover.md` holds the current short form; where a point below was superseded, the line says so.

- Token-acquire, claim BY NAME (stale read receipt: `queue.py read --record PATH --executor operator`), then in one shell `killall -9 UserNotificationCenter NotificationCenter`, `lsappinfo front` names LastWar, `cu_bridge.py start --app com.lastwar.ios --model claude-gateway/claude-sonnet-5-5`. Task text: never ask a question, one action per turn, never zoom or Escape, turn 1 a NO-CLICK frame (dialog check, HUD), last turn a report. Release the token after the run.
- Safe point for menus (400,640), never (200,610) (a Gold Mine). SUPERSEDED 2026-11-23 15:26Z: (400,640) selected a Barracks after a camera shift; use the bare spot (310,660) or WORLD then BASE first. Never tap bubbles over buildings (a Farmland tap collected food). One building per fresh frame (WORLD then BASE at (660,940), only with no menu open).
- The Backpack Resources tab opens with the 5,000 Diamonds tile SELECTED and a live Use; the number field cannot be typed (plus and minus only).
- A `local_input` pause: stop, retry once, record the time to the millisecond and the other jobs. Desktop gate (D-024): save the `run-lock.mjs status` JSON at each refusal; Owner-idle wait: restored 20:04Z (OD-23), then TEMPORARILY 0 from the restart after 21:20Z (OD-27) until CU-720 arrives with the tree move; the code default is 300 s, from the launcher branch (d762ffce), live after the Integrator merges it, the launcher line says 0 (restore: set it to None). Log the wait rows until the coordinator says the restart landed; after that no manual idle reads.
- Chrome came to the front at about 19:24:50Z in run c7ba46 with no tap of mine (the run stopped on a consent request, nothing answered); never take the window back unless the counter shows 300 s or more, then run `mac_lastwar_front.sh` once. The idle counter counts the harness's own clicks (every reading after a run equals the run's last click, measured 19:33, 20:00 and 20:05Z), so the 19:24Z reading was this run's own last drag, not proof of the owner at the Mac; the cause of the switch is open.
- TIPS "active on a different device": STOP, press nothing, release the token, report; never Confirm without the owner (the second Confirm was Steer B's).

## Run shape (14:40Z, session f364ec2c)

An 8-step cap gives 7 effective actions (the 8th turn never runs); a click plus a wait in one turn closes a panel; three harvest panels take 11 turns, so two runs.

## Never

The Go button on the check-in banner opens the web store in Chrome ([1528-t3-focus-incident.md](../shop-claims/1528-t3-focus-incident.md)); a consent request is human-only.
